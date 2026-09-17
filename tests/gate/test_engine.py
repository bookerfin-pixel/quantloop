"""PROTECTED. The decision step and the backtest share one code path."""
import pytest

from bot import backtest, config, data, paper, strategy
from bot.run import step

RCFG = {
    "fee_bps": 10, "slippage_bps": 5, "initial_cash": 10_000, "pairs": ["BTC", "ETH"],
    "history_hours": 720, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0,
    "min_trade_notional": 50, "rebalance_threshold": 0.05, "daily_loss_halt": 0.05,
    "backtest_gate": {"min_days": 7, "max_days": 120, "max_drawdown": 0.3,
                      "min_cost_coverage": 1.0, "max_trades_per_pair_per_day": 4},
}


def candles(n=400, seed=1):
    return {p: data.SyntheticSource(["BTC", "ETH"], n=n, seed=seed, start=1_700_000_000).ohlc(p)
            for p in ["BTC", "ETH"]}


def test_step_fills_toward_target_and_logs_reason():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    fn = lambda c, p, w: {"BTC": strategy.Target(0.2, "because"), "ETH": 0.0}  # noqa: E731
    decisions, fills, equity = step(acct, {"params": {}}, fn, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_000_000, RCFG)
    assert len(fills) == 1 and fills[0].side == "buy"
    assert fills[0].notional == pytest.approx(2000.0, rel=1e-3)
    btc = next(d for d in decisions if d["pair"] == "BTC")
    assert btc["action"] == "buy" and "because" in btc["reason"]
    assert equity < 10_000  # costs were paid


def test_strategy_error_goes_flat_not_crash():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 1000.0, 100.0, 1, "seed")
    def boom(c, p, w):
        raise RuntimeError("bad")
    decisions, fills, _ = step(acct, {"params": {}}, boom, candles(), {"BTC": 100.0, "ETH": 50.0}, 1_700_000_000, RCFG)
    assert fills and fills[0].side == "sell" and "BTC" not in acct.positions
    assert "strategy error" in decisions[0]["reason"]


def test_daily_halt_flattens_and_blocks_new_entries():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 2000.0, 100.0, 1, "seed")
    fn = lambda c, p, w: {"BTC": 0.25, "ETH": 0.25}  # noqa: E731
    ts = 1_700_000_000
    step(acct, {"params": {}}, fn, candles(), {"BTC": 100.0, "ETH": 50.0}, ts, RCFG)      # sets the day open
    _, fills, _ = step(acct, {"params": {}}, fn, candles(), {"BTC": 60.0, "ETH": 50.0}, ts + 3600, RCFG)
    assert all(f.side == "sell" for f in fills) and not acct.positions
    assert acct.state["halted_day"] is not None


def test_backtest_costs_match_paper_model_and_metrics_are_consistent():
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum",
           "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
    m = backtest.run_backtest(candles(n=600), cfg, RCFG, max_days=None)
    assert m["bars"] > 100 and m["n_trades"] > 0
    assert m["net_pnl"] == pytest.approx(m["gross_pnl"] - m["fees"] - m["slippage"], abs=0.05)
    assert m["final_equity"] == pytest.approx(RCFG["initial_cash"] * (1 + m["total_return"]), rel=1e-4)
    assert -1 < m["max_drawdown"] <= 0
    assert m["fees"] > 0 and m["slippage"] > 0
    # fee per unit notional is exactly fee_bps: slippage is exactly slippage_bps of notional at the ref price
    assert m["fees"] == pytest.approx(m["slippage"] * 2, rel=0.02)


def test_backtest_refuses_thin_data():
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}}
    with pytest.raises(ValueError):
        backtest.run_backtest(candles(n=60), cfg, RCFG)


def test_config_loader_rejects_incomplete_config(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "CONFIGS", tmp_path)
    (tmp_path / "risk.yaml").write_text("challenger:\n  slots: 3\n")
    (tmp_path / "challenger1.yaml").write_text("strategy: ts_momentum\n")
    with pytest.raises(ValueError):
        config.account_cfg("challenger1")
    with pytest.raises(ValueError):
        config.account_cfg("challenger9")


def test_backtest_tolerates_a_pair_with_shorter_history():
    cfg = {"hypothesis": "H0", "strategy": "ts_momentum",
           "params": {"lookback_hours": 48, "ema_hours": 12, "vol_lookback_hours": 96}}
    c = candles(n=600)
    c["ETH"] = c["ETH"].iloc[300:].reset_index(drop=True)      # ETH only exists for the second half
    m = backtest.run_backtest(c, cfg, RCFG, max_days=None)
    assert m["bars"] > 500                                     # the clock is BTC's full length
    assert m["pairs"] == 2
    assert m["final_equity"] == pytest.approx(RCFG["initial_cash"] * (1 + m["total_return"]), rel=1e-4)
