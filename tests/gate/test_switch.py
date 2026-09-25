"""PROTECTED. A new strategy starts from its own decisions, not another strategy's book."""
import json

import pytest

from bot import config, data, paper, strategy
from bot.run import run_account, step

RCFG = {"fee_bps": 10, "slippage_bps": 5, "impact_bps": 2, "initial_cash": 10_000, "pairs": ["BTC", "ETH"],
        "history_hours": 720, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0,
        "min_trade_notional": 50, "rebalance_threshold": 0.05, "daily_loss_halt": 0.05}
PRICES = {"BTC": 100.0, "ETH": 50.0}


def candles():
    src = data.SyntheticSource(["BTC", "ETH"], n=300, seed=3, start=1_700_000_000)
    return {p: src.ohlc(p) for p in ["BTC", "ETH"]}


def holds_what_it_holds(c, params, w):
    """Never enters, but keeps anything it already holds: the shape of every
    strategy here that has a separate exit rule (stay long until X)."""
    return {p: strategy.Target(0.2 if w.get(p, 0.0) > 0 else 0.0, "stay long" if w.get(p, 0.0) > 0 else "flat")
            for p in c}


def test_fresh_step_decides_as_if_flat_and_trades_from_the_real_book():
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("BTC", 2000.0, 100.0, 1, "inherited")
    _, fills, _ = step(acct, {"params": {}}, holds_what_it_holds, candles(), PRICES, 1_700_000_000, RCFG)
    assert not fills and "BTC" in acct.positions                       # a normal hour keeps it
    decisions, fills, _ = step(acct, {"params": {}}, holds_what_it_holds, candles(), PRICES, 1_700_003_600, RCFG,
                               fresh=True)
    assert [f.side for f in fills] == ["sell"] and "BTC" not in acct.positions
    assert all("decided as if flat" in d["reason"] for d in decisions)


def test_an_exit_later_in_the_list_funds_an_entry_earlier_in_the_list():
    """Fully invested in ETH (second in the list); the strategy switches to BTC
    (first). Before 2026-09-25 the BTC buy ran first, found no cash and did
    nothing, then ETH sold and the cash sat idle for an hour."""
    acct = paper.PaperAccount("t", 10_000, 10, 5)
    acct.trade("ETH", 2500.0, 50.0, 1, "seed")
    acct.state["cash"] = 0.0                                             # nothing spare
    rc = {**RCFG, "max_weight_per_pair": 1.0}
    switch = lambda c, p, w: {"BTC": strategy.Target(0.2, "enter"), "ETH": strategy.Target(0.0, "exit")}  # noqa: E731
    decisions, fills, _ = step(acct, {"params": {}}, switch, candles(), PRICES, 1_700_000_000, rc)
    assert [f.side for f in fills] == ["sell", "buy"] and acct.positions.get("BTC", 0) > 0
    assert [d["pair"] for d in decisions] == ["BTC", "ETH"]              # the log keeps pairs order


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "ROOT", tmp_path)
    monkeypatch.setattr(config, "CONFIGS", tmp_path / "configs")
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    (tmp_path / "configs").mkdir()
    config.dump_yaml(tmp_path / "configs" / "risk.yaml", {**RCFG, "challenger": {"slots": 1}})
    config.dump_yaml(tmp_path / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "always_btc", "params": {}})
    monkeypatch.setitem(strategy.STRATEGIES, "holds_what_it_holds", holds_what_it_holds)
    monkeypatch.setitem(strategy.STRATEGIES, "always_btc",
                        lambda c, p, w: {"BTC": strategy.Target(0.2, "enter"), "ETH": 0.0})
    return tmp_path


def _cfg(root, strat, hyp):
    config.dump_yaml(root / "configs" / "challenger1.yaml", {"hypothesis": hyp, "strategy": strat, "params": {}})


def test_run_account_is_fresh_only_on_a_strategy_change(sandbox):
    ts = 1_700_000_000
    _cfg(sandbox, "always_btc", "H0")
    run_account("challenger1", candles(), PRICES, ts, RCFG)
    state = json.loads((sandbox / "state" / "challenger1" / "account.json").read_text())
    assert state["positions"].get("BTC", 0) > 0 and state["strategy_sig"]
    # same strategy next hour: nothing changes
    run_account("challenger1", candles(), PRICES, ts + 3600, RCFG)
    assert json.loads((sandbox / "state" / "challenger1" / "account.json").read_text())["positions"].get("BTC", 0) > 0
    # a new hypothesis lands in the slot: it does not inherit the BTC position
    _cfg(sandbox, "holds_what_it_holds", "H9")
    run_account("challenger1", candles(), PRICES, ts + 7200, RCFG)
    state = json.loads((sandbox / "state" / "challenger1" / "account.json").read_text())
    assert "BTC" not in state["positions"]


def test_an_account_from_before_the_rule_is_not_disturbed_on_deploy(sandbox):
    ts = 1_700_000_000
    _cfg(sandbox, "holds_what_it_holds", "H9")
    acct = paper.PaperAccount("challenger1", 10_000, 10, 5)
    acct.trade("BTC", 2000.0, 100.0, 1, "opened under this same strategy before signatures existed")
    acct.save(sandbox / "state" / "challenger1" / "account.json")
    run_account("challenger1", candles(), PRICES, ts, RCFG)
    state = json.loads((sandbox / "state" / "challenger1" / "account.json").read_text())
    assert state["positions"].get("BTC", 0) > 0 and state["strategy_sig"]
