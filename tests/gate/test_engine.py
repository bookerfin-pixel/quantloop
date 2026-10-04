"""PROTECTED. The decision step and the backtest share one code path."""
import pandas as pd
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


GATE_RULES = {"min_days": 7, "max_days": 365, "min_trades": 30, "max_cost_drag": 0.15,
              "max_avg_fills_per_pair_per_day": 1.0, "max_drawdown": 0.30, "drawdown_vs_basket": 0.75}


def _metrics(**kw):
    base = {"days": 365.0, "pairs": 10, "n_trades": 400, "fees": 500.0, "slippage": 250.0,
            "max_drawdown": -0.20, "total_return": 0.05, "avg_gross_exposure": 0.5, "equity_curve": []}
    base.update(kw)
    return base


def test_plausibility_is_regime_independent():
    bear = {"basket_return": -0.565, "basket_max_dd": -0.715, "basket_path": None}
    calm = {"basket_return": 0.10, "basket_max_dd": -0.15, "basket_path": None}
    # a 45% drawdown passes in a year whose basket fell 71.5% (limit 0.75 x 71.5% = 53.6%) ...
    problems, report = backtest.plausibility(_metrics(max_drawdown=-0.45), GATE_RULES, bear, 10_000)
    assert problems == [] and report["drawdown_limit"] == pytest.approx(-0.536, abs=1e-3)
    # ... and fails in a calm year (limit is the 30% floor)
    problems, _ = backtest.plausibility(_metrics(max_drawdown=-0.45), GATE_RULES, calm, 10_000)
    assert any("drawdown" in p for p in problems)
    # losing money in sample is not a gate failure; it is reported as skill vs benchmark
    problems, report = backtest.plausibility(_metrics(total_return=-0.31, avg_gross_exposure=0.38), GATE_RULES, bear, 10_000)
    assert problems == []
    assert report["exposure_matched_benchmark"] == pytest.approx(-0.565 * 0.38, abs=1e-4)
    assert report["skill_vs_benchmark"] == pytest.approx(-0.31 + 0.565 * 0.38, abs=1e-4)


def test_plausibility_catches_the_fee_treadmill_and_thin_evidence():
    problems, report = backtest.plausibility(_metrics(fees=1800.0, slippage=900.0, n_trades=2775), GATE_RULES, None, 10_000)
    assert report["cost_drag_per_year"] == pytest.approx(0.27)
    assert any("treadmill" in p for p in problems)
    problems, _ = backtest.plausibility(_metrics(n_trades=12), GATE_RULES, None, 10_000)
    assert any("fewer than the 30" in p for p in problems)
    problems, _ = backtest.plausibility(_metrics(n_trades=4000, fees=100.0, slippage=50.0), GATE_RULES, None, 10_000)
    assert any("fills per pair per day" in p for p in problems)


def test_gate_skips_when_no_slot_config_changed():
    import importlib.util, os, sys
    spec = importlib.util.spec_from_file_location("bg", os.path.join(os.getcwd(), "gate", "backtest_gate.py"))
    bg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bg)
    assert bg.slot_from_paths(["notes/2026-09-17.md", "hypotheses/backlog.md"]) is None
    assert bg.slot_from_paths(["LEDGER.md", "configs/challenger2.yaml"]) == "challenger2"
    assert bg.slot_from_paths(["configs/champion.yaml", "configs/risk.yaml"]) is None


def _needs(n):
    def fn(c, params, w):
        out = {}
        for p, df in c.items():
            if len(df) < n:
                out[p] = strategy.Target(0.0, f"flat: only {len(df)} candles, need {n}")
            else:
                out[p] = strategy.Target(0.2, "enter")
        return out
    return fn


def test_a_short_backtest_still_hands_the_strategy_its_full_history(monkeypatch):
    """Until 2026-10-04 a short backtest cut the history to the replayed window
    plus the largest single *_hours parameter, so a strategy needing more sat
    flat on "only N candles" for the whole run and the result looked like calm."""
    monkeypatch.setitem(strategy.STRATEGIES, "needs_400", _needs(400))
    cfg = {"hypothesis": "HX", "strategy": "needs_400", "params": {"x_hours": 50}}
    m = backtest.run_backtest(candles(n=700), cfg, RCFG, max_days=3)
    assert m["n_trades"] >= 1 and m["starved_share"] == 0.0


def test_a_strategy_that_needs_more_history_than_it_can_get_fails_the_gate(monkeypatch):
    monkeypatch.setitem(strategy.STRATEGIES, "needs_5000", _needs(5000))     # history_hours is 720 here
    cfg = {"hypothesis": "HX", "strategy": "needs_5000", "params": {"x_hours": 50}}
    m = backtest.run_backtest(candles(n=900), cfg, RCFG, max_days=20)
    assert m["starved_share"] == 1.0
    rules = {"max_drawdown": 0.3, "max_cost_drag": 0.15, "max_avg_fills_per_pair_per_day": 1.0, "min_trades": 0}
    problems, _ = backtest.plausibility(m, rules, None, 10_000)
    assert any("too few candles" in p for p in problems)


def test_a_strategy_held_back_only_by_the_fill_cap_fails_the_gate(monkeypatch):
    def flip(c, params, w):
        return {p: strategy.Target(0.0, "exit") if w.get(p, 0) > 0 else strategy.Target(0.2, "enter") for p in c}
    monkeypatch.setitem(strategy.STRATEGIES, "flip", flip)
    cfg = {"hypothesis": "HX", "strategy": "flip", "params": {"x_hours": 24}}
    rc = {**RCFG, "max_fills_per_pair_per_day": 4}
    m = backtest.run_backtest(candles(n=900), cfg, rc, max_days=20)
    assert m["trades_per_pair_per_day_max"] <= 5 and m["pair_days_at_fill_cap"] > 20     # buys stopped most days
    rules = {"max_drawdown": 0.3, "max_cost_drag": 10.0, "max_avg_fills_per_pair_per_day": 10.0, "min_trades": 0,
             "max_pair_days_at_fill_cap": 12}
    problems, _ = backtest.plausibility(m, rules, None, 10_000)
    assert any("loop" in p for p in problems)


def test_a_long_run_is_read_out_by_calendar_year_against_that_year_s_basket():
    start = 1_640_995_200                                    # 2022-01-01 00:00 UTC
    hours = 24 * 365 * 2
    curve = [(start + i * 3600, 10_000 * (1 + 0.5 * i / hours)) for i in range(hours)]   # +50% over two years
    asked = []

    def market_fn(a, b):
        asked.append((a, b))
        year = pd.to_datetime(a, unit="s").year
        return {"basket_return": {2022: -0.60, 2023: 0.90}[year], "pairs": {2022: 9, 2023: 10}[year]}
    m = _metrics(days=730.0, equity_curve=curve)
    _, report = backtest.plausibility(m, GATE_RULES, None, 10_000, market_fn=market_fn)
    assert [y["year"] for y in report["years"]] == [2022, 2023] and len(asked) == 2
    assert report["years"][0]["basket"] == -0.60 and report["years"][0]["pairs"] == 9
    assert report["years"][0]["strategy"] == pytest.approx(0.25, abs=0.01)
    line = backtest.format_report(report).splitlines()[-1]
    assert line.startswith("by calendar year") and "2022 +25.0% / -60.0% (9 pairs)" in line and "(10 pairs)" not in line
    # the gate's own 365 day run never asks for it
    _, short = backtest.plausibility(_metrics(equity_curve=curve[:24 * 365]), GATE_RULES, None, 10_000, market_fn=market_fn)
    assert short["years"] == [] and len(asked) == 2
