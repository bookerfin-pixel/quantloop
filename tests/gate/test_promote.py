"""PROTECTED. The promotion rule, early kill, slot bookkeeping and legacy migration."""
import csv
import json

import pytest

from bot import config, promote, slot

# The rule these older tests were written for: one look, raw return, no floor under skill, no fast pass, no
# cost kill. Every line is in the file, and what that rule did not have is written `off` (YAML reads the bare
# word as False). A line left out would now mean its documented value, not "off".
RULES = {"slots": 3, "window_days": 21, "confirm_days": 60, "min_trades": 20, "max_dd_ratio": 1.5,
         "max_dd_floor": 0.10, "min_return_edge": 0.0, "early_kill_drawdown": 0.15, "compare_on": "return",
         "min_skill": False, "two_looks_from_ruleset": False, "fast_pass_skill_t": False, "min_skill_t": False,
         "min_trade_profit": 0.0, "treadmill_kill_multiple": False, "treadmill_min_days": 14,
         "retired_champions": False, "cash_guard_skill_t": 1.0, "confidence": {"prior": 0.10, "edge_sharpe": 1.5}}


def m(ret, dd, trades, gross=None, notional=0.0):
    bps = gross / (notional / 2) * 1e4 if gross is not None and notional else None
    return {"return": ret, "max_drawdown": dd, "trades": trades, "bars": 500, "fees": 10.0,
            "gross_pnl": gross, "traded_notional": notional, "realised_bps": bps}


def test_decide_rules():
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.06, 30), RULES)[0] == "promoted"
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.06, 5), RULES)[0] == "killed"     # too few fills
    assert promote.decide(m(0.02, -0.05, 30), m(0.01, -0.02, 30), RULES)[0] == "killed"    # worse return
    assert promote.decide(m(0.01, -0.05, 30), m(0.02, -0.12, 30), RULES)[0] == "killed"    # 12% > max(7.5%, 10%)
    assert promote.decide(m(None, None, 0), m(0.02, -0.01, 30), RULES)[0] == "killed"      # no data


def test_drawdown_floor_protects_against_a_flat_champion():
    # champion sat in cash: 0% drawdown. Without the floor any risk at all would be a kill.
    verdict, _ = promote.decide(m(0.0, 0.0, 0), m(0.04, -0.06, 30), RULES)
    assert verdict == "promoted"
    verdict, _ = promote.decide(m(0.0, 0.0, 0), m(0.04, -0.11, 30), RULES)
    assert verdict == "killed"


def test_early_kill():
    """Ended early when it has lost more than the limit since the test began AND
    more than the market itself over the same days. Until ruleset 7 it was 15%
    under its high whatever the market had done, which in a falling market
    ended most tests, good or bad."""
    lost = m(-0.16, -0.16, 3)
    said = promote.early_kill(lost, RULES, basket_return=-0.05)
    assert said == ("challenger has lost 16.00% since its test began, past the 15% early kill limit, and more than "
                    "the market itself over the same days (the basket lost 5.00%); no need to wait for the window "
                    "to end")
    assert "the basket made 2.00%" in promote.early_kill(lost, RULES, basket_return=0.02)
    assert promote.early_kill(lost, RULES, basket_return=-0.20) is None       # the market lost more: not its doing
    assert promote.early_kill(lost, RULES, basket_return=-0.16) is None       # no worse than the market
    assert promote.early_kill(lost, RULES) is None                            # no figure for the market: no kill
    assert promote.early_kill_waits(lost, RULES, None) and not promote.early_kill_waits(lost, RULES, -0.05)
    assert promote.early_kill(m(-0.15, -0.15, 3), RULES, basket_return=0.0) is None       # at the limit is not past it
    # 16% under its high but still above where it began: not a loss since the test began
    assert promote.early_kill(m(0.05, -0.16, 3), RULES, basket_return=0.0) is None
    assert promote.early_kill(m(-0.10, -0.16, 3), RULES, basket_return=0.0) is None       # 16% under its high, 10% down
    assert promote.early_kill(m(-0.05, -0.08, 3), RULES, basket_return=0.0) is None
    assert promote.early_kill(m(None, None, 0), RULES, basket_return=0.0) is None
    assert not promote.early_kill_waits(m(-0.05, -0.08, 3), RULES, None)
    off = {**RULES, "early_kill_drawdown": False}                             # `off` in the file
    assert promote.early_kill(lost, off, basket_return=0.0) is None and not promote.early_kill_waits(lost, off, None)
    assert promote.early_kill(lost, {**RULES, "early_kill_drawdown": 0}, basket_return=0.0) is None
    left_out = {k: v for k, v in RULES.items() if k != "early_kill_drawdown"}  # a line left out is not "off"
    assert "past the 15% early kill limit" in promote.early_kill(lost, left_out, basket_return=0.0)


def _write_equity(root, name, rows):
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "equity", "cash", "gross_exposure", "n_positions",
                                          "fees_paid", "slippage_paid"])
        w.writeheader()
        for ts, eq, fees in rows:
            w.writerow({"ts": ts, "equity": eq, "cash": eq, "gross_exposure": 0, "n_positions": 0,
                        "fees_paid": fees, "slippage_paid": 0})


def _write_trades(root, name, rows):
    p = root / "state" / name / "trades.csv"
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "account", "pair", "side", "qty", "price", "ref_price",
                                          "notional", "fee", "slippage_cost", "reason", "equity_after"])
        w.writeheader()
        # a buy, then the sell that closes it, and so on: since ruleset 7 nothing is promoted without an exit
        for i, (ts, notional) in enumerate(rows):
            w.writerow({"ts": ts, "account": name, "pair": "BTC", "side": "sell" if i % 2 else "buy", "qty": 1,
                        "price": 1, "ref_price": 1, "notional": notional, "fee": 0, "slippage_cost": 0,
                        "reason": "", "equity_after": 0})


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    root = tmp_path
    (root / "configs").mkdir()
    (root / "state").mkdir()
    monkeypatch.setattr(config, "ROOT", root)
    monkeypatch.setattr(config, "CONFIGS", root / "configs")
    monkeypatch.setattr(config, "STATE", root / "state")
    monkeypatch.setattr(config, "ARCHIVE", root / "state" / "archive")
    monkeypatch.setattr(config, "LEDGER", root / "LEDGER.md")
    config.dump_yaml(root / "configs" / "risk.yaml", {"challenger": RULES, "pairs": ["BTC"], "initial_cash": 10000,
                                                      "fee_bps": 10, "slippage_bps": 5})
    monkeypatch.setattr(config, "CANDLES", root / "state" / "candles")
    monkeypatch.setattr(config, "HISTORY", root / "state" / "history")
    config.dump_yaml(root / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    config.dump_yaml(root / "configs" / "challenger1.yaml",
                     {"hypothesis": "H1", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    config.dump_yaml(root / "configs" / "challenger2.yaml",
                     {"hypothesis": "H2", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    config.write_challenger_from_champion("challenger3")
    (root / "LEDGER.md").write_text(
        "# Ledger\n\n## H0: base\n- Status: champion\n\n## H1: longer\n- Expected gross bps per round trip: 150\n"
        "- Status: testing\n\n## H2: mr\n- Expected gross bps per round trip: 300\n- Status: testing\n")
    for name in ("champion", "challenger1", "challenger2", "challenger3"):
        (root / "state" / name).mkdir(parents=True, exist_ok=True)
        (root / "state" / name / "account.json").write_text(json.dumps({"cash": 1}))
    return root


def test_window_metrics_realised_bps(sandbox):
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (3600, 10100, 20)])   # +100 net, 20 costs -> 120 gross
    _write_trades(sandbox, "challenger1", [(1000, 3000), (2000, 3000)])         # 6000 traded = 3000 per round trip
    w = promote.window_metrics("challenger1", 0, 3600, 10000)
    assert w["gross_pnl"] == pytest.approx(120)
    assert w["realised_bps"] == pytest.approx(120 / 3000 * 1e4)


def test_promotion_copies_slot_into_champion_and_resets_that_slot_only(sandbox):
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0, "start_equity": {}})
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": 0, "start_equity": {}})
    promote.update_ledger("H1", "promoted", "because", m(0.01, -0.05, 30, 100, 1000),
                          m(0.02, -0.06, 30, 300, 3000), 0, 21 * 86400, "challenger1")
    promote.apply("promoted", "H1", "challenger1")
    champ = config.account_cfg("champion")
    assert champ["hypothesis"] == "H1" and champ["params"]["lookback_hours"] == 168
    assert config.is_cash(config.account_cfg("challenger1"))                    # an idle slot holds cash (ruleset 8)
    assert config.is_cash(config.account_cfg("challenger3"))                    # and so does the one idle on H0
    assert slot.load("challenger1")["status"] == "idle"
    assert slot.load("challenger2")["status"] == "testing"                       # untouched
    assert config.account_cfg("challenger2")["hypothesis"] == "H2"
    assert not (sandbox / "state" / "challenger1" / "account.json").exists()     # archived
    assert list((sandbox / "state" / "archive").iterdir())
    text = (sandbox / "LEDGER.md").read_text()
    assert "- Status: promoted" in text and "### Result H1: promoted" in text and "- Slot: challenger1" in text
    assert "realised gross bps per round trip 2000 (ledger expected 150)" in text
    assert "## H2: mr\n- Expected gross bps per round trip: 300\n- Status: testing" in text   # H2 untouched


def test_kill_keeps_champion(sandbox):
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": 0, "start_equity": {}})
    promote.update_ledger("H2", "killed", "nope", m(0.02, -0.05, 30), m(0.01, -0.06, 30), 0, 21 * 86400, "challenger2")
    promote.apply("killed", "H2", "challenger2")
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    assert config.account_cfg("challenger2") == config.CASH_CFG                 # the freed slot holds cash
    assert slot.load("challenger2")["status"] == "idle"
    assert "- Status: killed" in (sandbox / "LEDGER.md").read_text()


def test_slots_start_independently(sandbox):
    metas = slot.maybe_start(1000, {"champion": 10_000.0, "challenger1": 10_000.0,
                                     "challenger2": 9_000.0, "challenger3": 10_000.0})
    assert metas["challenger1"]["status"] == "testing" and metas["challenger1"]["hypothesis"] == "H1"
    assert metas["challenger2"]["status"] == "testing" and metas["challenger2"]["start_equity"]["challenger2"] == 9_000.0
    assert metas["challenger3"]["status"] == "idle"
    assert slot.free_slots() == ["challenger3"]
    # second call does not restart the clocks
    metas = slot.maybe_start(2000, {"champion": 1, "challenger1": 1, "challenger2": 1, "challenger3": 1})
    assert metas["challenger1"]["started_at"] == 1000


def test_main_early_kills_and_rules_at_window_end(sandbox):
    now = 21 * 86400 + 100
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0,
                              "start_equity": {"champion": 10000, "challenger1": 10000}})
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": now - 3 * 86400,
                              "start_equity": {"champion": 10000, "challenger2": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (now, 10300, 8)])
    _write_trades(sandbox, "challenger1", [(i * 3600, 1000) for i in range(25)])
    _write_equity(sandbox, "challenger2", [(now - 3 * 86400, 10000, 0), (now, 8200, 3)])   # -18%: early kill
    _write_trades(sandbox, "challenger2", [(now - 3600, 1000)])
    _write_candles(sandbox, "BTC", 0, [100.0] * (22 * 24))                                 # in a flat market
    assert promote.main(["--now", str(now)]) == 0
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: promoted" in text
    assert "### Result H2: killed" in text and "early kill" in text
    assert "has lost 18.00% since its test began" in text and "the basket made 0.00%" in text
    assert config.account_cfg("champion")["hypothesis"] == "H1"
    assert slot.load("challenger1")["status"] == "idle" and slot.load("challenger2")["status"] == "idle"


def test_a_test_that_fell_with_the_market_is_not_ended_early(sandbox, capsys):
    """The same 18% loss in three days, in a market that lost 25% over those days."""
    now = 21 * 86400 + 100
    start = now - 3 * 86400
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": start,
                              "start_equity": {"champion": 10000, "challenger2": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    _write_equity(sandbox, "challenger2", [(start, 10000, 0), (now, 8200, 3)])
    _write_trades(sandbox, "challenger2", [(now - 3600, 1000)])
    hours = 22 * 24
    _write_candles(sandbox, "BTC", 0, [100.0 if i * 3600 < start else 75.0 for i in range(hours)])
    assert promote.main(["--now", str(now)]) == 0
    assert "### Result H2" not in (sandbox / "LEDGER.md").read_text()
    assert slot.load("challenger2")["status"] == "testing"
    # and with no candles at all there is no figure for the market, so no early kill, and the log says so
    (sandbox / "state" / "candles" / "BTC.csv").unlink()
    getattr(__import__("bot.data", fromlist=["x"]), "_READ_CACHE", {}).clear()
    capsys.readouterr()
    assert promote.main(["--now", str(now)]) == 0
    out = capsys.readouterr().out
    assert "WARNING: challenger2: H2 has lost 18.00% since its test began, past the early kill limit, but" in out
    assert "no early kill this hour" in out and "### Result H2" not in (sandbox / "LEDGER.md").read_text()


def test_two_winners_same_hour_promotes_one_and_restarts_the_other(sandbox):
    now = 21 * 86400 + 100
    for name, hyp, end_eq in (("challenger1", "H1", 10300), ("challenger2", "H2", 10500)):
        slot.save(name, {"status": "testing", "hypothesis": hyp, "started_at": 0,
                         "start_equity": {"champion": 10000, name: 10000}})
        _write_equity(sandbox, name, [(0, 10000, 0), (now, end_eq, 8)])
        _write_trades(sandbox, name, [(i * 3600, 1000) for i in range(25)])
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    assert promote.main(["--now", str(now)]) == 0
    assert config.account_cfg("champion")["hypothesis"] == "H2"                  # the stronger one
    assert slot.load("challenger2")["status"] == "idle"
    meta1 = slot.load("challenger1")
    assert meta1["status"] == "testing" and meta1["started_at"] == now and meta1["restarted_against"] == "H2"
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: restarted" in text
    assert "## H1: longer\n- Expected gross bps per round trip: 150\n- Status: testing" in text


def test_legacy_single_challenger_is_migrated_into_slot_one(sandbox):
    (sandbox / "configs" / "challenger1.yaml").unlink()
    config.dump_yaml(sandbox / "configs" / "challenger.yaml",
                     {"hypothesis": "H9", "strategy": "ts_momentum", "params": {"lookback_hours": 9}})
    import shutil
    shutil.rmtree(sandbox / "state" / "challenger1")
    (sandbox / "state" / "challenger").mkdir()
    (sandbox / "state" / "challenger" / "meta.json").write_text(json.dumps(
        {"status": "testing", "hypothesis": "H9", "started_at": 5, "start_equity": {"challenger": 1.0}}))
    config.prepare()
    assert config.account_cfg("challenger1")["hypothesis"] == "H9"
    assert not (sandbox / "configs" / "challenger.yaml").exists()
    assert slot.load("challenger1")["hypothesis"] == "H9"
    assert not (sandbox / "state" / "challenger").exists()


def _write_candles(root, pair, start, closes):
    import pandas as pd
    (root / "state" / "candles").mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"time": [start + i * 3600 for i in range(len(closes))], "open": closes, "high": closes,
                  "low": closes, "close": closes, "vwap": closes, "volume": 1, "count": 1}
                 ).to_csv(root / "state" / "candles" / f"{pair}.csv", index=False)


def test_market_context_reads_the_window(sandbox):
    # a candle's close is the price one hour after it opens: these are the prices at 1h, 2h, 3h and 4h
    _write_candles(sandbox, "BTC", 0, [100, 101, 102, 110])
    _write_candles(sandbox, "ETH", 0, [50, 50, 50, 45])
    mc = promote.market_context(3600, 4 * 3600, ["BTC", "ETH"])
    assert mc["pairs"] == 2
    assert mc["btc_return"] == pytest.approx(0.10)
    assert mc["basket_return"] == pytest.approx((0.10 - 0.10) / 2)
    assert "BTC +10.00%" in promote.format_market(mc)
    # a window that ends at 3h does not use the candle still forming then (it closes at 4h)
    assert promote.market_context(3600, 3 * 3600, ["BTC"])["btc_return"] == pytest.approx(0.02)


def test_the_market_window_starts_at_the_tests_own_start_not_up_to_an_hour_later(sandbox):
    """A test that begins 21 minutes into an hour in which the market jumps 10%
    lived through 65% of that jump. Its benchmark used to begin at the hour's
    close and so had none of it, for the whole length of the test."""
    _write_candles(sandbox, "BTC", 0, [100, 100, 110, 110, 110])     # the jump is between 2h and 3h
    start = 2 * 3600 + 21 * 60
    mc = promote.market_context(start, 5 * 3600, ["BTC"])
    began_at = 100 + (21 / 60) * 10                                  # the price 21 minutes into the hour, read in proportion
    assert mc["btc_return"] == pytest.approx(110 / began_at - 1)
    assert float(mc["basket_path"].iloc[0]) == pytest.approx(1.0) and int(mc["basket_path"].index[0]) == start - 3600
    assert promote.market_context(2 * 3600, 5 * 3600, ["BTC"])["btc_return"] == pytest.approx(0.10)   # on the hour: exact
    # no price at or before the start (the pair is new, or the record has a hole): start at its first price inside
    _write_candles(sandbox, "ETH", 6 * 3600, [50, 55, 55])
    late = promote._window_closes(__import__("pandas").read_csv(sandbox / "state" / "candles" / "ETH.csv"), 3600, 9 * 3600)
    assert list(late.to_numpy()) == [50.0, 55.0, 55.0]
    assert promote._window_closes(__import__("pandas").read_csv(sandbox / "state" / "candles" / "ETH.csv"), 0, 3600) is None


def test_a_pair_listed_after_the_window_opened_is_not_in_the_basket(sandbox):
    """Carried as flat from the window's start it shrank the basket's move by its share."""
    fall = [100 - i for i in range(51)]                            # 100 to 50 over fifty hours
    for pair in ("BTC", "ETH", "SOL"):
        _write_candles(sandbox, pair, 0, fall)
    _write_candles(sandbox, "XRP", 40 * 3600, [1.0] * 11)          # exists only for the last ten hours
    mc = promote.market_context(0, 51 * 3600, ["BTC", "ETH", "SOL", "XRP"])
    assert mc["pairs"] == 3
    assert mc["basket_return"] == pytest.approx(-0.50)
    assert float(mc["basket_path"].iloc[-1]) == pytest.approx(0.50)
    late = promote.market_context(40 * 3600, 51 * 3600, ["BTC", "ETH", "SOL", "XRP"])
    assert late["pairs"] == 4                                      # and it is in the basket of a window it was there for


def test_the_hourly_run_kills_a_treadmill_through_main(sandbox):
    """early_kill only fires if main hands it the days elapsed, the starting equity and the gate's limit."""
    now = 20 * 86400
    risk = config.load_yaml(sandbox / "configs" / "risk.yaml")
    risk["challenger"] = {**RULES, "window_days": 60, "treadmill_kill_multiple": 3.0, "treadmill_min_days": 14}
    risk["backtest_gate"] = {"max_cost_drag": 0.15}
    config.dump_yaml(sandbox / "configs" / "risk.yaml", risk)
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0,
                              "start_equity": {"champion": 10000, "challenger1": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (now, 9800, 300)])      # 300 in 20 days is 55% a year
    _write_trades(sandbox, "challenger1", [(i * 3600, 1500) for i in range(200)])
    assert promote.main(["--now", str(now)]) == 0
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: killed" in text and "fees treadmill" in text
    assert slot.load("challenger1")["status"] == "idle"


def test_promotion_starts_a_shadow_that_can_revert(sandbox):
    from bot import shadow
    now = 60 * 86400 + 100
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0,
                              "start_equity": {"champion": 10000, "challenger1": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (now, 10300, 8)])
    _write_trades(sandbox, "challenger1", [(i * 3600, 1000) for i in range(35)])
    assert promote.main(["--now", str(now)]) == 0
    assert config.account_cfg("champion")["hypothesis"] == "H1"
    meta = shadow.load()
    assert meta["status"] == "active" and meta["hypothesis"] == "H0" and meta["replaced_by"] == "H1"
    assert config.account_cfg("shadow")["hypothesis"] == "H0" and config.shadow_active()
    assert "shadow" in config.accounts()
    # guard window: the deposed H0 config (shadow) does much better than the promoted H1 champion
    later = now + 60 * 86400 + 100
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5), (later, 9800, 9)])
    _write_equity(sandbox, "shadow", [(now, 10000, 0), (later, 10500, 6)])
    _write_trades(sandbox, "shadow", [(now + i * 3600, 1000) for i in range(35)])
    assert promote.main(["--now", str(later)]) == 0
    assert config.account_cfg("champion")["hypothesis"] == "H0"          # reverted
    assert shadow.load()["status"] == "idle" and not config.shadow_active()
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: reverted" in text and "- Status: reverted" in text
    assert "Deposed config (shadow)" in text


def test_a_second_promotion_during_a_guard_window_says_the_first_guard_ended(sandbox):
    """The shadow account is handed to the newly deposed champion. The earlier
    promotion was neither confirmed nor reverted, and the ledger must not leave
    it looking confirmed (bot/shadow.py promised this line; it was never written)."""
    from bot import shadow
    day = 86400
    first, start2 = 60 * day + 100, 50 * day
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0,
                              "start_equity": {"champion": 10000, "challenger1": 10000}})
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": start2,
                              "start_equity": {"champion": 10050, "challenger2": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (start2, 10050, 3), (first, 10100, 5)])
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (first, 10300, 8)])
    _write_trades(sandbox, "challenger1", [(i * 3600, 1000) for i in range(35)])
    _write_equity(sandbox, "challenger2", [(start2, 10000, 0), (first, 10100, 2)])
    assert promote.main(["--now", str(first)]) == 0
    assert config.account_cfg("champion")["hypothesis"] == "H1" and shadow.load()["hypothesis"] == "H0"
    assert "superseded" not in (sandbox / "LEDGER.md").read_text()     # a first promotion supersedes nothing
    # eleven days into H1's guard, H2's own window ends and it wins too
    second = start2 + 21 * day + 200
    _write_equity(sandbox, "champion", [(0, 10000, 0), (start2, 10050, 3), (first, 10100, 5), (second, 10120, 9)])
    _write_equity(sandbox, "shadow", [(first, 10000, 0), (second, 9900, 4)])
    _write_equity(sandbox, "challenger2", [(start2, 10000, 0), (first, 10100, 2), (second, 10500, 7)])
    _write_trades(sandbox, "challenger2", [(start2 + i * 3600, 1000) for i in range(25)])
    assert promote.main(["--now", str(second)]) == 0
    assert config.account_cfg("champion")["hypothesis"] == "H2"
    meta = shadow.load()
    assert meta["status"] == "active" and meta["hypothesis"] == "H1" and meta["replaced_by"] == "H2"
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: superseded" in text and "- Slot: shadow" in text
    assert "H2 was promoted on day 11.0 of the 21 day guard" in text
    assert "the deposed H0 was dropped as the shadow and the guard now watches H2" in text
    assert "neither confirmed nor reverted" in text
    assert text.index("### Result H2: promoted") < text.index("### Result H1: superseded")   # cause, then consequence
    assert "## H1: longer\n- Expected gross bps per round trip: 150\n- Status: promoted" in text   # status untouched


def test_shadow_holds_when_the_promotion_is_real(sandbox):
    from bot import shadow
    now = 100
    shadow.start(config.account_cfg("champion"), "H1", now, 10000.0, 10000.0)
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H1", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (sandbox / "LEDGER.md").write_text((sandbox / "LEDGER.md").read_text().replace(
        "## H1: longer\n- Expected gross bps per round trip: 150\n- Status: testing",
        "## H1: longer\n- Expected gross bps per round trip: 150\n- Status: promoted"))
    later = now + 60 * 86400 + 100
    _write_equity(sandbox, "champion", [(now, 10000, 0), (later, 10400, 5)])
    _write_equity(sandbox, "shadow", [(now, 10000, 0), (later, 10100, 6)])
    _write_trades(sandbox, "shadow", [(now + i * 3600, 1000) for i in range(35)])
    promote.rule_on_shadow(later, RULES | {"window_days": 60, "min_trades": 30})
    assert config.account_cfg("champion")["hypothesis"] == "H1"
    assert shadow.load()["status"] == "idle"
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: held" in text and "- Status: promoted" in text


def test_a_fees_treadmill_is_killed_before_the_window_ends():
    rules = {**RULES, "treadmill_kill_multiple": 3.0, "treadmill_min_days": 14}
    chal = m(-0.04, -0.05, 200)
    chal["fees"] = 300.0                                  # 300 in 20 days on 10,000 is 55% a year
    assert "treadmill" in promote.early_kill(chal, rules, 20.0, 10_000, 0.15)
    assert promote.early_kill(chal, rules, 10.0, 10_000, 0.15) is None        # too early to call a rate
    chal["fees"] = 200.0                                  # 36% a year: over the gate's 15%, under three times it
    assert promote.early_kill(chal, rules, 20.0, 10_000, 0.15) is None
    assert promote.early_kill(chal, RULES, 20.0, 10_000, 0.15) is None        # rule not configured: no kill


def _two_tests_running(sandbox, now):
    slot.save("challenger1", {"status": "testing", "hypothesis": "H1", "started_at": 0, "ruleset": 5,
                              "start_equity": {"champion": 10000, "challenger1": 10000}})
    slot.save("challenger2", {"status": "testing", "hypothesis": "H2", "started_at": 0,
                              "start_equity": {"champion": 10000, "challenger2": 10000}})
    _write_equity(sandbox, "champion", [(0, 10000, 0), (now, 10100, 5)])
    _write_equity(sandbox, "challenger1", [(0, 10000, 0), (now, 9600, 280)])
    _write_trades(sandbox, "challenger1", [(i * 3600, 1500) for i in range(120)])
    risk = config.load_yaml(sandbox / "configs" / "risk.yaml")
    config.dump_yaml(sandbox / "configs" / "risk.yaml", {**risk, "ruleset": 6})


def test_a_voided_test_is_recorded_and_its_slot_freed(sandbox):
    now = 9 * 86400
    _two_tests_running(sandbox, now)
    config.dump_yaml(sandbox / "configs" / "void.yaml", {"requests": [
        {"slot": "challenger1", "hypothesis": "H1", "reason": "enter and exit loop in the strategy code"},
        {"slot": "challenger2", "hypothesis": "H9", "reason": "names the wrong hypothesis"}]})
    assert promote.process_voids(now, RULES) == ["H1"]
    text = (sandbox / "LEDGER.md").read_text()
    assert "### Result H1: voided" in text and "enter and exit loop" in text
    assert "ruleset 5 at the start, 6 at the verdict" in text
    assert "- Status: voided" in text and "### Result H2" not in text
    assert slot.load("challenger1")["status"] == "idle" and slot.load("challenger2")["status"] == "testing"
    assert config.account_cfg("challenger1") == config.CASH_CFG                 # the freed slot holds cash
    assert config.load_yaml(sandbox / "configs" / "void.yaml")["requests"] == []
    assert promote.process_voids(now, RULES) == []                      # nothing left to do


@pytest.mark.parametrize("body", [
    "requests:\n  slot: challenger1\n  hypothesis: H1\n",          # a mapping where the list should be
    "requests:\n- challenger1\n",                                   # a bare word for a request
    "requests:\n-\n",                                               # an empty item
    "requests: H1\n",                                                # a bare word for the list
    "- slot: challenger9\n  hypothesis: H1\n",                      # a list at the top, and an unknown slot
    "requests:\n- slot: [challenger1\n",                            # not yaml at all
    "",                                                              # empty file
])
def test_a_badly_written_void_file_cannot_stop_the_hourly_run(sandbox, body):
    """promote runs every hour before the summary and the commit. Whatever a
    hand edited file holds, it must rule on the other tests and return 0."""
    now = 9 * 86400
    _two_tests_running(sandbox, now)
    (sandbox / "configs" / "void.yaml").write_text(body)
    assert promote.process_voids(now, RULES) == []
    assert slot.load("challenger1")["status"] == "testing"             # nothing was voided by accident
    assert promote.main(["--now", str(now)]) == 0


def test_a_misspelt_key_in_the_void_file_is_said_out_loud(sandbox, capsys):
    now = 9 * 86400
    _two_tests_running(sandbox, now)
    (sandbox / "configs" / "void.yaml").write_text("request:\n- slot: challenger1\n  hypothesis: H1\n  reason: typo in the key\n")
    assert promote.process_voids(now, RULES) == []
    assert "no `requests` list" in capsys.readouterr().out
    assert slot.load("challenger1")["status"] == "testing"


def test_a_request_that_fails_half_way_does_not_stop_the_others(sandbox, monkeypatch):
    now = 9 * 86400
    _two_tests_running(sandbox, now)
    _write_equity(sandbox, "challenger2", [(0, 10000, 0), (now, 9900, 30)])
    config.dump_yaml(sandbox / "configs" / "void.yaml", {"requests": [
        {"slot": "challenger1", "hypothesis": "H1", "reason": "first"},
        {"slot": "challenger2", "hypothesis": "H2", "reason": "second"}]})
    real = promote.update_ledger

    def flaky(hyp, *a, **k):
        if hyp == "H1":
            raise RuntimeError("ledger not writable")
        return real(hyp, *a, **k)
    monkeypatch.setattr(promote, "update_ledger", flaky)
    assert promote.process_voids(now, RULES) == ["H2"]
    assert slot.load("challenger1")["status"] == "testing" and slot.load("challenger2")["status"] == "idle"
    assert config.load_yaml(sandbox / "configs" / "void.yaml")["requests"] == []


def test_a_test_whose_record_cannot_be_read_can_still_be_voided(sandbox, capsys):
    """Broken data is what a void is for, and a record that cannot be read was
    the one state in which no look, no early kill and no void could end a
    test: the request failed on the same file and was dropped."""
    now = 9 * 86400
    _two_tests_running(sandbox, now)
    (sandbox / "state" / "challenger1" / "trades.csv").write_text("")          # cut to nothing
    config.dump_yaml(sandbox / "configs" / "void.yaml", {"requests": [
        {"slot": "challenger1", "hypothesis": "H1", "reason": "its trades file was cut to nothing"}]})
    assert promote.process_voids(now, RULES) == ["H1"]
    assert slot.load("challenger1")["status"] == "idle"
    block = (sandbox / "LEDGER.md").read_text().split("### Result H1: voided")[1]
    assert "- Rule: voided by Fin, not a verdict on the idea: its trades file was cut to nothing. Its numbers so far " \
           "could not be read (Unreadable: challenger1/trades.csv cannot be read" in block
    assert "- Champion: no data" in block and "- Challenger: no data" in block


def test_the_void_file_in_the_repo_is_well_formed():
    """The real file is edited by hand. Catch a typo here, not in the hourly run."""
    from pathlib import Path
    body = config.load_yaml(Path(__file__).resolve().parents[2] / "configs" / "void.yaml")
    assert isinstance(body, dict) and isinstance(body.get("requests"), list)
    for req in body["requests"]:
        assert isinstance(req, dict) and set(req) == {"slot", "hypothesis", "reason"}
        assert str(req["slot"]).startswith("challenger") and str(req["hypothesis"]).startswith("H")
        assert len(str(req["reason"]).strip()) > 20


def test_report_marks_an_open_position_even_when_the_stored_name_is_stale(sandbox):
    from bot import paper, report
    from bot.run import DECISION_FIELDS
    adir = sandbox / "state" / "challenger1"
    acct = paper.PaperAccount("challenger", 10_000, 10, 5)     # the name the file carried before slots were numbered
    fill = acct.trade("DOGE", 1000.0, 0.10, 100, "enter")
    acct.state["created_at"] = 100
    acct.save(adir / "account.json")
    paper.append_rows(adir / "trades.csv", paper.TRADE_FIELDS, [paper.fill_row(fill)])
    paper.append_rows(adir / "decisions.csv", DECISION_FIELDS, [
        {"ts": 200, "account": "challenger1", "pair": "DOGE", "price": 0.11, "signal_weight": 0.1,
         "target_weight": 0.1, "current_weight": 0.1, "action": "hold", "reason": "stay", "half_spread_bps": 1.0}])
    _write_equity(sandbox, "challenger1", [(100, 10000, 0), (200, 10098, 2)])
    section = report.account_section("challenger1", 300)
    line = next(l for l in section.splitlines() if l.startswith("- DOGE"))
    assert "gross pnl +99.95" in line and "+1999 bps" in line      # marked at 0.11; the bug showed -1,000 and -20,000 bps
