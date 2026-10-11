"""PROTECTED. Ruleset 8, first part (Fin, 2026-10-08): H0 is retired and cash is the
default champion. A test that begins while the champion's config is retired is
judged against cash, and against the champion account from the moment a config
takes the title inside its window; the tests that began against H0 are judged
against the champion account as before, with what cash would make of them
measured beside; every test that begins under ruleset 8 has its drawdown guard
set against the equal weight basket's fall; an idle slot holds cash; a
promotion judged against cash is guarded by cash; when no test needs H0 any
more the champion account holds cash too. PROMOTION.md has the rule in words,
FINDINGS.md (2026-10-10) the measurements behind it."""
import csv
import json

import pandas as pd
import pytest

from bot import backtest, bench, config, promote, report, run, shadow, slot, strategy

from .test_replay import RCFG
from .test_rule_one_edges import equity_at_day_end, moving_market
from .test_two_looks import (CHAMP, DAY, LOSING, RULES, STEADY, STRONG, at, equity, ledger,  # noqa: F401
                             sandbox, set_rules, trades)

RETIRED = {"retired_champions": ["H0"]}
CASH = config.CASH_CFG
H6 = {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 99}}


def ruleset_8(root, **changes):
    set_rules(root, **{**RETIRED, **changes})
    body = config.load_yaml(root / "configs" / "risk.yaml")
    config.dump_yaml(root / "configs" / "risk.yaml", {**body, "ruleset": 8})


@pytest.fixture
def cash_rules(sandbox, monkeypatch):
    """The sandbox with ruleset 8's rules: H0 retired, cash's usual exposure nothing."""
    ruleset_8(sandbox)
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: 0.0 if config.is_cash(cfg) else 0.5)
    return sandbox


def cash_test(root, returns, name="challenger1", hyp="H5", started=0, ruleset=8, against="cash", sell_price=101.0):
    """A running test. sell_price=99.0: its finished trades lose, so it is not kept on their value."""
    meta = {"status": "testing", "hypothesis": hyp, "started_at": started,
            "start_equity": {"champion": 10000.0, name: 10000.0}, "ruleset": ruleset}
    if against is not None:
        meta["against"] = against
    slot.save(name, meta)
    if returns is not None:
        equity(root, name, returns)
    trades(root, name, sell_price=sell_price)
    (root / "state" / name / "account.json").write_text(json.dumps({"cash": 1}))


def flat_rows(root, name, from_ts, days, value=10_000.0):
    """An account that holds cash: the same equity every day from `from_ts`."""
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "equity", "cash", "gross_exposure", "n_positions",
                                          "fees_paid", "slippage_paid"])
        w.writeheader()
        for k in range(days):
            w.writerow({"ts": from_ts + k * DAY, "equity": value, "cash": value, "gross_exposure": 0.0,
                        "n_positions": 0, "fees_paid": 0.0, "slippage_paid": 0.0})


def add_hypothesis(root, hyp, title="another"):
    text = ledger(root)
    head, sep, results = text.partition("\n## Results")
    (root / "LEDGER.md").write_text(head.rstrip("\n") + f"\n\n## {hyp}: {title}\n- Expected gross bps per round "
                                    f"trip: 100\n- Status: testing\n" + (sep + results if sep else ""))


def rules():
    return config.risk_cfg()["challenger"]


# --- cash itself ---------------------------------------------------------------------------------------

def test_cash_holds_nothing_and_is_not_the_agents_to_change(monkeypatch):
    """bot/strategy.py is the agent's file. Cash lives in bot/run.py, which is protected, and is found there
    whatever bot/strategy.py registers under the same name."""
    frames = {"BTC": pd.DataFrame({"close": [1.0, 2.0]}), "ETH": pd.DataFrame({"close": [3.0, 4.0]})}
    got = run.strategy_fn("cash")(frames, {}, {"BTC": 0.25})
    assert {p: t.weight for p, t in got.items()} == {"BTC": 0.0, "ETH": 0.0}
    assert all(t.reason == "cash: holds nothing" for t in got.values())
    monkeypatch.setitem(strategy.STRATEGIES, "cash",
                        lambda c, p, w: {pair: strategy.Target(0.25, "not cash") for pair in c})
    assert run.strategy_fn("cash") is run._cash
    assert run.strategy_fn("ts_momentum") is strategy.get("ts_momentum")
    assert config.is_cash(CASH) and not config.is_cash({"strategy": "ts_momentum"}) and not config.is_cash(None)


def test_cash_on_history_holds_nothing_and_pays_nothing():
    hours = 24 * 40
    candles = {"BTC": pd.DataFrame({"time": [i * 3600 for i in range(hours)], "open": 100.0, "high": 101.0,
                                    "low": 99.0, "close": [100.0 + (i % 7) for i in range(hours)], "vwap": 100.0,
                                    "volume": 1.0, "count": 1})}
    m = backtest.run_backtest(candles, CASH, {**RCFG, "pairs": ["BTC"]})
    assert m["avg_gross_exposure"] == 0.0 and m["n_trades"] == 0


def test_the_usual_exposure_of_cash_is_nothing_with_no_backtest(monkeypatch):
    monkeypatch.setattr(backtest, "run_backtest", lambda *a, **k: (_ for _ in ()).throw(AssertionError("ran")))
    assert promote.design_exposure(dict(CASH), 10 ** 9) == 0.0


def test_the_bench_has_nothing_to_read_in_a_slot_that_holds_cash(cash_rules):
    config.write_challenger_idle("challenger2")
    used, problems = bench.configs_in_use()
    assert [cfg["hypothesis"] for _, cfg in used] == ["H0", "H5"] and problems == []


# --- idle slots hold cash ------------------------------------------------------------------------------

def test_a_new_slot_is_created_holding_cash(cash_rules):
    (cash_rules / "configs" / "challenger2.yaml").unlink()
    assert config.ensure_slot_configs() == ["challenger2"]
    assert config.account_cfg("challenger2") == CASH and not slot.configs_differ("challenger2")
    assert slot.describe_one("challenger2", at(1)) == "challenger2: idle, holds cash (free for a hypothesis)"


def test_an_idle_slot_is_described_as_what_it_holds(cash_rules):
    assert slot.describe_one("challenger2", at(1)) == ("challenger2: idle, holds the champion's config until the "
                                                       "next ruling moves it to cash (free for a hypothesis)")
    config.dump_yaml(cash_rules / "configs" / "challenger2.yaml", H6)
    assert slot.describe_one("challenger2", at(1)) == ("challenger2: idle until the next hourly run, which starts "
                                                       "a test of H6 in it")
    (cash_rules / "configs" / "challenger2.yaml").write_text("strategy: [cut")
    assert slot.describe_one("challenger2", at(1)).startswith("challenger2: idle; its config cannot be read (")


def test_an_idle_slot_on_the_champions_config_is_moved_to_cash_at_the_hourly_ruling(cash_rules, capsys):
    """Today no slot is idle; one idle at the deploy, on H0's config as before ruleset 8, is moved by the
    first ruling after it, and it sells what it holds at the next hourly run."""
    cash_test(cash_rules, STEADY, ruleset=6, against=None)                     # a test that still needs H0
    assert config.account_cfg("challenger2")["hypothesis"] == "H0" and slot.load("challenger2")["status"] == "idle"
    assert promote.main(["--now", str(at(1))]) == 0
    assert config.account_cfg("challenger2") == CASH and config.account_cfg("champion")["hypothesis"] == "H0"
    assert "idle slots moved to cash: challenger2" in capsys.readouterr().out
    assert promote.idle_slots_to_cash() == []                                   # cash already: nothing written
    assert config.account_cfg("challenger1")["hypothesis"] == "H5"             # a config of its own is a test


# --- what a new test is judged against -------------------------------------------------------------------

def test_a_test_that_begins_while_the_champions_config_is_retired_is_judged_against_cash(cash_rules, capsys):
    config.dump_yaml(cash_rules / "configs" / "challenger2.yaml", H6)
    started = slot.maybe_start(at(1), {"champion": 10000.0, "challenger2": 10000.0})
    assert started["challenger2"]["against"] == "cash" and started["challenger2"]["ruleset"] == 8
    assert "challenger2: test started for H6 at 1970-01-02 02:00Z, judged against cash" in capsys.readouterr().out
    assert "testing H6, judged against cash since" in slot.describe_one("challenger2", at(2))


def test_once_a_config_holds_the_title_a_new_test_is_judged_against_the_champion_account(cash_rules):
    config.dump_yaml(cash_rules / "configs" / "champion.yaml",
                     {"hypothesis": "H7", "strategy": "ts_momentum", "params": {"lookback_hours": 99}})
    config.dump_yaml(cash_rules / "configs" / "challenger2.yaml", H6)
    assert slot.maybe_start(at(1), {"champion": 1.0, "challenger2": 1.0})["challenger2"]["against"] == "champion"
    # while the champion's config is cash itself, against cash again
    config.dump_yaml(cash_rules / "configs" / "champion.yaml", dict(CASH))
    slot.reset("challenger2")
    assert slot.maybe_start(at(2), {"champion": 1.0, "challenger2": 1.0})["challenger2"]["against"] == "cash"
    # with retirement switched off, H0 is the champion it always was
    set_rules(cash_rules, retired_champions=False)
    config.dump_yaml(cash_rules / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    slot.reset("challenger2")
    assert slot.maybe_start(at(3), {"champion": 1.0, "challenger2": 1.0})["challenger2"]["against"] == "champion"


# --- the rule against cash ---------------------------------------------------------------------------------

def mc(basket_return=0.0, basket_dd=0.0):
    return {"basket_return": basket_return, "basket_max_dd": basket_dd, "gap": None}


def side(skill, dd=-0.05, fills=40, ret=None, skill_t=None):
    ret = skill if ret is None else ret
    return {"return": ret, "max_drawdown": dd, "trades": fills, "skill": skill, "skill_exposure": 0.5,
            "skill_basis": "usual", "edge_t": None, "edge_days": 0, "skill_t": skill_t, "skill_days": 60}


def test_cash_side_makes_nothing_and_sets_the_drawdown_guard_by_the_basket():
    c = promote.cash_side(mc(0.10, -0.20), 0.10)
    assert c["return"] == 0.0 and c["skill"] == 0.0 and c["trades"] == 0 and c["max_drawdown"] == 0.0
    assert c["skill_exposure"] == 0.0 and c["avg_exposure"] == 0.0 and c["basket_return"] == 0.10
    assert c["guard_drawdown"] == pytest.approx(0.20) and promote.side_name(c) == "cash"
    blank = promote.cash_side(mc(None, None), None)
    assert blank["skill"] is None and blank["guard_drawdown"] == 0.0           # no market data: no skill to set
    assert promote.side_name({"return": 0.0}) == "champion"


def test_against_cash_the_bar_is_skill_above_nothing():
    verdict, why = promote.decide(promote.cash_side(mc(), 0.0), side(0.02), RULES)
    assert verdict == "promoted"
    assert why == ("challenger skill +2.00% (net +2.00%, benchmark exposure 0.50) beat cash, which makes nothing "
                   "(skill +0.00%) with max drawdown 5.00% against the equal weight basket's 0.00%")
    verdict, why = promote.decide(promote.cash_side(mc(), 0.0), side(-0.01), RULES)
    assert verdict == "killed" and why.startswith("challenger skill -1.00% (net -1.00%, benchmark exposure 0.50) "
                                                   "did not beat cash, which makes nothing (skill +0.00%)")
    assert promote.decide(promote.cash_side(mc(), 0.0), side(0.0), RULES)[0] == "killed"      # nothing is not more
    verdict, why = promote.decide(promote.cash_side(mc(), 0.0), side(0.02, fills=12), RULES)
    assert verdict == "killed" and "made 12 fills, fewer than the 30" in why     # the challenger's fills still count


def test_against_cash_the_drawdown_guard_is_the_baskets_fall_and_never_cash_s():
    """Against cash's own drawdown (none) the guard would be its 10% floor, which in the twin study killed
    four tests in five, edges and all. Against the basket's fall every figure came out as against H0."""
    calm = promote.cash_side(mc(0.0, 0.0), 0.0)
    verdict, why = promote.decide(calm, side(0.03, dd=-0.12), RULES)
    assert verdict == "killed" and why.startswith("challenger max drawdown 12.00% exceeded the limit 10.00% (the "
                                                  "larger of 1.5x the equal weight basket's 0.00% and the 10% floor)")
    assert why.endswith("although its skill was +3.00% ahead of cash")
    rough = promote.cash_side(mc(-0.15, -0.20), -0.15)
    verdict, why = promote.decide(rough, side(0.03, dd=-0.25), RULES)            # inside 1.5x the basket's 20%
    assert verdict == "promoted" and why.endswith("with max drawdown 25.00% against the equal weight basket's 20.00%")
    assert promote.decide(rough, side(0.03, dd=-0.31), RULES)[0] == "killed"


def test_the_guard_on_a_promotion_judged_against_cash_asks_a_clear_fall_and_no_fills_of_cash():
    """The shadow holds cash: it makes no bets, and the fills a promotion needs are there to tell a
    strategy's bets from luck. Skill below nothing over 60 days is as likely as not for a config with no
    edge, so a revert asks for a daily skill t at or below minus min_skill_t."""
    cash = promote.cash_side(mc(), 0.0)
    cash.pop("guard_drawdown")                                                  # the shadow's own record, read as cash
    verdict, why = promote.decide(side(-0.02, skill_t=-1.5), cash, RULES, absolute=False)
    assert verdict == "promoted" and why == ("cash, which makes nothing (skill +0.00%) beat champion skill -2.00% "
                                             "(net -2.00%, benchmark exposure 0.50), and the promoted config's daily "
                                             "skill t is -1.50 over 60 days on 40 fills")
    verdict, why = promote.decide(side(-0.02, skill_t=-0.5), cash, RULES, absolute=False)
    assert verdict == "killed" and why.endswith("but the promoted config's daily skill t is -0.50 over 60 days, not "
                                                "at or below the -1.0 a revert to cash asks for: a fall that size "
                                                "over the guard's window can be noise")
    assert promote.decide(side(-0.02, skill_t=-1.0), cash, RULES, absolute=False)[0] == "promoted"    # at the bar
    assert promote.decide(side(-0.02), cash, RULES, absolute=False)[0] == "killed"         # no t: no revert
    assert promote.decide(side(-0.02), cash, {**RULES, "cash_guard_skill_t": False}, absolute=False)[0] == "promoted"
    # the bar is its own: a stricter or a switched off bar for promotions does not move it
    for promotion_bar in (2.5, False):
        assert promote.decide(side(-0.02, skill_t=-1.2), cash, {**RULES, "min_skill_t": promotion_bar},
                              absolute=False)[0] == "promoted"
    assert promote.decide(side(-0.02, skill_t=-1.2), cash, {**RULES, "cash_guard_skill_t": 1.5},
                          absolute=False)[0] == "killed"
    # one losing day in otherwise flat ones reads a t of exactly -1, whatever its size: a fall that only just
    # reaches the bar is read on 30 fills or more
    verdict, why = promote.decide(side(-0.002, skill_t=-1.0, fills=4), cash, RULES, absolute=False)
    assert verdict == "killed" and why.endswith("and the promoted config's daily skill t is -1.00 over 60 days, but "
                                                "the promoted config made 4 fills in the guard's window, fewer than "
                                                "the 30 a revert to cash asks for unless the t is -2.0 or lower: too "
                                                "few separate bets to read a fall that size")
    # one that buys and holds into a fall makes few fills and falls steadily: at twice the bar it is reverted
    held_into_a_fall = {**side(-0.11, skill_t=-8.3, fills=10), "avg_exposure": 0.9, "basket_return": -0.15}
    verdict, why = promote.decide(held_into_a_fall, cash, RULES, absolute=False)
    assert verdict == "promoted" and why.endswith("and the promoted config's daily skill t is -8.30 over 60 days on "
                                                  "10 fills")
    assert promote.decide(side(-0.02, skill_t=-2.0, fills=3), cash, RULES, absolute=False)[0] == "promoted"
    assert promote.decide(side(-0.02, skill_t=-1.2, fills=30), cash, RULES, absolute=False)[0] == "promoted"  # 30 is enough
    strict = {**RULES, "cash_guard_skill_t": 1.5}                               # twice the bar is then -3.0
    verdict, why = promote.decide(side(-0.02, skill_t=-2.0, fills=3), cash, strict, absolute=False)
    assert verdict == "killed" and why.endswith("unless the t is -3.0 or lower: too few separate bets to read a fall "
                                                "that size")
    assert promote.decide(side(0.0, skill_t=-1.5), cash, RULES, absolute=False)[0] == "killed"   # nothing is not less
    verdict, why = promote.decide(side(0.01, skill_t=-3.0), cash, RULES, absolute=False)
    assert verdict == "killed" and why.startswith("cash, which makes nothing (skill +0.00%) did not beat champion "
                                                  "skill +1.00%")


def test_the_words_against_the_champion_are_as_they_were():
    champ = side(-0.01, dd=-0.08)
    verdict, why = promote.decide(champ, side(0.02), RULES)
    assert why == ("challenger skill +2.00% (net +2.00%, benchmark exposure 0.50) beat champion skill -1.00% (net "
                   "-1.00%, benchmark exposure 0.50) with max drawdown 5.00% vs 8.00%")
    assert promote.decide(side(0.01, dd=-0.02), side(0.03, dd=-0.12), RULES)[1].endswith(
        "although its skill was +2.00% ahead of the champion's")
    assert promote.decide(side(-0.01, dd=0.0), side(0.02), RULES)[1].endswith("with max drawdown 5.00% vs 0.00%")
    assert promote.decide(side(0.01), side(0.01), RULES, absolute=False)[0] == "killed"           # level is not ahead
    # a test begun under ruleset 8 and judged against the champion account: the guard is the basket's fall
    verdict, why = promote.decide({**side(0.01, dd=-0.02), "guard_drawdown": 0.20}, side(0.03, dd=-0.25), RULES)
    assert verdict == "promoted" and why.endswith("with max drawdown 25.00% against the equal weight basket's 20.00%")


# --- through the hourly ruling ---------------------------------------------------------------------------

def falling_market(root, fall=-0.20, days=60):
    step = (1 + fall) ** (1 / days) - 1
    moving_market(root, [step] * days)
    return step


def test_in_a_falling_market_the_guard_of_a_ruleset_8_test_is_the_baskets_fall(cash_rules, monkeypatch):
    """The basket falls 20% over the window and the test holds the whole market plus a steady skill: it falls
    about 18%, past the 10% floor and inside one and a half times the basket's fall."""
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: 0.0 if config.is_cash(cfg) else 1.0)
    step = falling_market(cash_rules)
    cash_test(cash_rules, None)
    equity_at_day_end(cash_rules, "challenger1", [step + s for s in STRONG[:61]], exposure=1.0)
    equity_at_day_end(cash_rules, "champion", [step] * 61, exposure=1.0)
    champ, chal, m = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), rules())
    assert -0.21 < m["basket_max_dd"] < -0.19 and champ["guard_drawdown"] == pytest.approx(-m["basket_max_dd"])
    assert -0.19 < chal["max_drawdown"] < -0.15 and chal["skill"] > 0 > chal["return"]
    assert chal["edge_t"] == pytest.approx(chal["skill_t"])                    # against cash, the edge is its own skill
    as_cash = slot.load("challenger1")
    assert "worst fall in the window, -20.00% so far" in report.test_section(at(60))
    # the same test judged against the champion account, begun under ruleset 8: the same guard
    champ, _, _ = promote.paired_slot("challenger1", {**as_cash, "against": "champion"}, at(60), rules())
    assert champ["guard_drawdown"] == pytest.approx(-m["basket_max_dd"])
    # and one from before ruleset 8: the champion's own fall, as it began
    old = {k: v for k, v in as_cash.items() if k != "against"}
    assert "guard_drawdown" not in promote.paired_slot("challenger1", old, at(60), rules())[0]
    slot.save("challenger1", as_cash)
    promote.main(["--now", str(at(60))])
    text = ledger(cash_rules)
    assert "### Result H5: killed" not in text and "### Result H5: promoted" in text
    assert "with max drawdown 15.08% against the equal weight basket's 20.00%" in text
    assert "its drawdown guard is set against the equal weight basket's worst fall over the window, -20.00%" in text


def test_the_usual_exposure_of_a_cash_judged_test_is_worked_out_once(cash_rules, monkeypatch):
    calls = []
    monkeypatch.setattr(promote, "design_exposure", lambda cfg, before_ts, days=365: calls.append(cfg) or 0.5)
    cash_test(cash_rules, STEADY)
    for day in (5, 6, 7):
        promote.paired_slot("challenger1", slot.load("challenger1"), at(day), rules())
    assert len(calls) == 1 and slot.load("challenger1")["usual_exposure"] == {"start": 0, "challenger1": 0.5}
    # a window that starts again (a restart) is worked out again, and so is a record that lacks the slot's figure
    slot.save("challenger1", {**slot.load("challenger1"), "started_at": at(2)})
    promote.paired_slot("challenger1", slot.load("challenger1"), at(8), rules())
    assert len(calls) == 2 and slot.load("challenger1")["usual_exposure"]["start"] == at(2)
    slot.save("challenger1", {**slot.load("challenger1"), "usual_exposure": {"start": at(2)}})
    promote.paired_slot("challenger1", slot.load("challenger1"), at(9), rules())
    assert len(calls) == 3 and slot.load("challenger1")["usual_exposure"]["challenger1"] == 0.5


def test_a_cash_judged_test_that_passes_is_promoted_and_cash_guards_the_promotion(cash_rules, capsys):
    cash_test(cash_rules, STRONG)
    equity(cash_rules, "champion", CHAMP)                                      # H0 still runs for the old tests
    assert promote.main(["--now", str(at(60))]) == 0
    text = ledger(cash_rules)
    assert "### Result H5: promoted" in text and "beat cash, which makes nothing (skill +0.00%)" in text
    assert ("- Judged against: cash: makes nothing and holds nothing; its drawdown guard is set against the equal "
            "weight basket's worst fall over the window, 0.00%") in text and "daily edge t over cash" in text
    assert "- Champion change:" not in text
    assert config.account_cfg("champion")["hypothesis"] == "H5"
    assert config.account_cfg("shadow") == CASH and shadow.load()["hypothesis"] == "cash"
    changes = promote.champion_changes()
    assert [(c["from"], c["to"], c["why"]) for c in changes] == [("H0", "H5", "promotion")]
    assert config.account_cfg("challenger1") == CASH and config.account_cfg("challenger2") == CASH
    assert "shadow: cash, which H5 was judged against, held since" in shadow.describe(at(61))
    assert ("falls below cash's, which is nothing with a daily skill t of -1.0 or lower, on 30 fills or more unless "
            "the t is -2.0 or lower") in shadow.describe(at(61))
    set_rules(cash_rules, **RETIRED, cash_guard_skill_t=1.5)
    assert "a daily skill t of -1.5 or lower, on 30 fills or more unless the t is -3.0 or lower" in shadow.describe(at(61))
    set_rules(cash_rules, **RETIRED, cash_guard_skill_t=False)
    assert shadow.describe(at(61)).endswith("falls below cash's, which is nothing")


def guard_after_promotion(root, champion_daily, now_day=121):
    """H5 promoted against cash on day 60; the champion account runs it from then, the shadow holds cash."""
    shadow.start(dict(CASH), "H5", at(60), 10000.0, 10000.0)
    config.dump_yaml(root / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (root / "LEDGER.md").write_text(ledger(root).replace("- Status: testing", "- Status: promoted"))
    equity(root, "champion", [0.0] * 60 + champion_daily)
    trades(root, "champion", n=now_day + 2)                                     # one fill a day
    flat_rows(root, "shadow", at(60), now_day - 60 + 1)
    return at(now_day)


def test_the_guard_reverts_to_cash_a_promoted_config_that_falls_clearly_below_it(cash_rules):
    now = guard_after_promotion(cash_rules, [-0.002, 0.0005] * 31)
    promote.rule_on_shadow(now, rules())
    text = ledger(cash_rules)
    assert "### Result H5: reverted" in text
    assert "cash, which the promoted config was judged against, beat the promoted one over the guard window" in text
    assert "- Cash, the deposed side (shadow):" in text
    assert config.account_cfg("champion") == CASH and shadow.load()["status"] != "active"
    assert promote.champion_changes()[-1]["to"] == "cash" and promote.champion_changes()[-1]["exposure"] == 0.0


def test_the_guard_holds_a_promoted_config_whose_fall_below_cash_can_be_noise(cash_rules):
    now = guard_after_promotion(cash_rules, [-0.0021, 0.002] * 31)              # a little below nothing, t about -0.2
    promote.rule_on_shadow(now, rules())
    text = ledger(cash_rules)
    assert "### Result H5: held" in text and "the promoted config held against cash over the guard window" in text
    assert "a revert to cash asks for" in text and config.account_cfg("champion")["hypothesis"] == "H5"


def test_the_guard_holds_a_promoted_config_that_beats_cash(cash_rules):
    now = guard_after_promotion(cash_rules, [0.002, -0.001] * 31)
    promote.rule_on_shadow(now, rules())
    assert "### Result H5: held" in ledger(cash_rules)
    assert config.account_cfg("champion")["hypothesis"] == "H5"


def test_the_cash_guard_reads_skill_not_return(cash_rules):
    """The promoted config held half the market while it fell 20%: it lost money, and did better than holding
    that half all the same. Cash does not beat it on skill, and the promotion stands."""
    step = 0.8 ** (1 / 61) - 1
    moving_market(cash_rules, [0.0] * 60 + [step] * 61)
    now = guard_after_promotion(cash_rules, [0.5 * step + s for s in [0.0015, -0.0005] * 31][:61] + [0.0])
    champ, shad, _, _ = promote._guard_reading(shadow.load(), now, rules())
    assert champ["return"] < -0.05 < 0 < champ["skill"] and promote.side_name(shad) == "cash"
    promote.rule_on_shadow(now, rules())
    text = ledger(cash_rules)
    assert "### Result H5: held" in text and "did not beat champion skill +" in text
    assert config.account_cfg("champion")["hypothesis"] == "H5"


def test_a_cash_judged_test_that_loses_is_killed_and_its_slot_holds_cash(cash_rules):
    cash_test(cash_rules, LOSING, sell_price=99.0)
    equity(cash_rules, "champion", CHAMP)
    promote.record_champion_change(at(30), "H0", "cash", "H0 retired (configs/risk.yaml, retired_champions)", 0.0)
    config.dump_yaml(cash_rules / "configs" / "champion.yaml", dict(CASH))
    promote.main(["--now", str(at(60))])
    text = ledger(cash_rules)
    assert "### Result H5: killed" in text and "did not beat cash, which makes nothing" in text
    assert "- Champion change:" not in text                                     # H0's retirement is not its business
    assert config.account_cfg("challenger1") == CASH and slot.load("challenger1")["status"] == "idle"


def test_a_cash_judged_test_that_passes_without_the_fast_pass_is_kept_for_its_second_look(cash_rules):
    cash_test(cash_rules, STEADY)
    equity(cash_rules, "champion", CHAMP)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(cash_rules)
    assert slot.load("challenger1")["first_look"]["on"] == "rule"
    assert config.account_cfg("champion") == CASH                              # no test needs H0 any more


def test_a_damaged_stamp_is_said_and_nothing_is_ruled_on_it(cash_rules, capsys):
    cash_test(cash_rules, LOSING, against="cahs")
    equity(cash_rules, "champion", CHAMP)
    promote.main(["--now", str(at(60))])
    out = capsys.readouterr().out
    assert "challenger1: H5 could not be looked at this hour" in out and "judged against 'cahs'" in out
    assert slot.load("challenger1")["status"] == "testing" and "### Result" not in ledger(cash_rules)
    assert config.account_cfg("champion")["hypothesis"] == "H0"               # it may need H0: no retirement


def test_a_cash_judged_test_can_be_voided_and_its_slot_goes_back_to_cash(cash_rules):
    cash_test(cash_rules, STEADY)
    config.dump_yaml(cash_rules / "configs" / "void.yaml",
                     {"requests": [{"slot": "challenger1", "hypothesis": "H5", "reason": "a broken signal"}]})
    promote.main(["--now", str(at(20))])
    text = ledger(cash_rules)
    assert "### Result H5: voided" in text and "- Judged against: cash: makes nothing" in text
    assert config.account_cfg("challenger1") == CASH and slot.load("challenger1")["status"] == "idle"


# --- when a config takes the title inside a test's window -----------------------------------------------------

def title_goes_to_h6(root, day=30):
    promote.record_champion_change(at(day), "H0", "H6", "promotion", 0.5)
    config.dump_yaml(root / "configs" / "champion.yaml", H6)


def test_a_test_judged_against_cash_keeps_its_window_when_a_config_takes_the_title(cash_rules):
    """It is judged against cash until then and against the champion account's record from then: a config
    that beat cash does not reset its window, as a change of champion never reset one before ruleset 8."""
    cash_test(cash_rules, STRONG)
    equity(cash_rules, "champion", CHAMP)
    title_goes_to_h6(cash_rules)
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(50), rules())
    eq = pd.read_csv(cash_rules / "state" / "champion" / "equity.csv").set_index("ts")["equity"]
    made = float(eq.loc[50 * DAY + 3600] / eq.loc[30 * DAY + 3600] - 1)        # the account from the change on
    assert champ["title_from"] == at(30) and champ["title_to"] == "H6" and promote.side_name(champ) == "champion"
    assert champ["return"] == pytest.approx(made) and champ["skill"] == pytest.approx(made)   # a flat market
    assert champ["exposure_schedule"] == [(0, 0.0), (at(30), 0.5)] and champ["guard_drawdown"] == 0.0
    assert champ["trades"] == 0 and chal["edge_t"] is not None
    assert "  so far: the title -0.40% (cash, then H6 from 1970-01-31) (max drawdown" in report.test_section(at(50))
    promote.main(["--now", str(at(60))])                                        # the fast pass, against the title
    text = ledger(cash_rules)
    assert "### Result H5: promoted" in text and "beat champion skill" in text
    assert ("- Champion change: the champion's title was cash when this test began, and it changed during it "
            "(1970-01-31 to H6 (promotion)). The side this test is judged against is the title's record: cash while "
            "the title was cash, and the champion account's own record while a config held it, its skill measured "
            "against the usual exposure of each config that held the title; its drawdown guard is the basket's fall "
            "over the whole window") in text
    assert config.account_cfg("shadow") == H6                                   # what it beat from then guards it


def test_the_title_record_counts_only_the_stretches_a_config_held_it(cash_rules):
    """H6 takes the title on day 20, its guard puts H0 back on day 40 (retired: it stands in for cash), and H7,
    whose usual exposure is not on record, takes it on day 50. Only days 20 to 40 and 50 on count, each from the
    reading at its change; the rest is cash's."""
    daily = [0.001 * ((k % 5) - 1) for k in range(80)]                          # a record that moves every day
    cash_test(cash_rules, STRONG)
    equity(cash_rules, "champion", daily)
    eq_file = cash_rules / "state" / "champion" / "equity.csv"
    rows = pd.read_csv(eq_file)
    rows["slippage_paid"] = 0.005 * rows.index                                  # costs of both kinds, so each counts
    rows.to_csv(eq_file, index=False)
    trades(cash_rules, "champion", n=70)                                        # one fill a day, days 1 to 70
    for day, frm, to, why, e in ((20, "H0", "H6", "promotion", None), (40, "H6", "H0", "revert", None),
                                 (50, "H0", "H7", "promotion", None)):
        promote.record_champion_change(at(day), frm, to, why, e)
    config.dump_yaml(cash_rules / "configs" / "champion.yaml",
                     {"hypothesis": "H7", "strategy": "ts_momentum", "params": {"lookback_hours": 33}})
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), rules())
    eq = pd.read_csv(cash_rules / "state" / "champion" / "equity.csv").set_index("ts")["equity"]
    row = lambda k: float(eq.loc[k * DAY + 3600])                               # noqa: E731
    made = (row(40) / row(20)) * (row(60) / row(50)) - 1                        # rows 21 to 40 and 51 to 60
    assert champ["return"] == pytest.approx(made) and champ["skill"] == pytest.approx(made)   # a flat market
    assert champ["trades"] == 20 + 10 and champ["title_from"] == at(20) and champ["title_to"] == "H6"
    assert champ["exposure_schedule"] == [(0, 0.0), (at(20), 0.5), (at(40), 0.0), (at(50), 0.5)]   # each its own
    assert champ["avg_exposure"] == pytest.approx(0.5 * 30 / 60, abs=0.02)      # half held, half the window
    assert champ["fees"] == pytest.approx(30 * (0.01 + 0.005))                  # paid in the 30 days a config held it
    path = [1.0]
    for k in range(1, 61):
        held = 20 < k <= 40 or 50 < k <= 60
        path.append(path[-1] * (row(k) / row(k - 1) if held else 1.0))
    peak = pd.Series(path).cummax()
    assert champ["max_drawdown"] == pytest.approx(float((pd.Series(path) / peak - 1).min()))
    assert champ["max_drawdown"] < 0
    assert promote.title_words(champ) == "cash, then H6 from 1970-01-21, then cash from 1970-02-10, then H7 from 1970-02-20"
    twice = {"title_steps": [(at(20), "H6", True, "promotion"), (at(40), "H0", False, "revert"),
                             (at(40), "cash", False, "H0 retired (configs/risk.yaml, retired_champions)")]}
    assert promote.title_words(twice) == "cash, then H6 from 1970-01-21, then cash from 1970-02-10"   # said once
    note = promote.title_note(champ)
    assert ("(1970-01-21 to H6 (promotion); 1970-02-10 back to cash, H0 standing in for it (revert); 1970-02-20 to "
            "H7 (promotion))") in note
    assert "the account's own average exposure for H6, H7, whose usual exposure is not on record" in note
    # the edge t sets the challenger's daily skill against the title's, cash's days counting as nothing
    plain = promote.edge_t(None, "challenger1", 0, at(60), slot.load("challenger1")["start_equity"],
                           promote.cash_side({}, 0.0), chal, None, "return")
    assert chal["edge_t"] is not None and chal["edge_t"] != pytest.approx(plain[0])


def test_a_reading_at_the_moment_of_a_change_is_the_config_before_it(cash_rules):
    cash_test(cash_rules, STRONG)
    equity(cash_rules, "champion", [0.01] * 40)                                 # one reading a day, at 01:00
    promote.record_champion_change(30 * DAY + 3600, "H0", "H6", "promotion", 0.5)    # ruled in the hour of a reading
    config.dump_yaml(cash_rules / "configs" / "champion.yaml", H6)
    champ, _, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(35), rules())
    assert champ["return"] == pytest.approx(1.01 ** 5 - 1)                     # rows 31 to 35: that reading is H0's


def test_in_the_hour_of_a_change_the_title_has_made_nothing_yet(cash_rules):
    cash_test(cash_rules, STRONG)
    equity(cash_rules, "champion", CHAMP[:31])                                  # readings to day 30, 01:00
    promote.record_champion_change(30 * DAY + 3700, "H0", "H6", "promotion", None)
    config.dump_yaml(cash_rules / "configs" / "champion.yaml", H6)
    champ, _, _ = promote.paired_slot("challenger1", slot.load("challenger1"), 30 * DAY + 4000, rules())
    assert champ["return"] == 0.0 and champ["max_drawdown"] == 0.0 and champ["trades"] == 0
    assert champ["exposure_schedule"] == [(0, 0.0), (30 * DAY + 3700, 0.0)]  # no reading of H6 yet: nothing held
    text = report.test_section(30 * DAY + 4000)
    assert "no usable equity record for champion" not in text and "the title +0.00% (cash, then H6 from" in text


def test_a_window_with_no_reading_of_the_champion_yet_reads_as_nothing_made(cash_rules):
    cash_test(cash_rules, STEADY, started=at(26))
    equity(cash_rules, "champion", CHAMP[:26])                                  # readings to day 25 only
    title_goes_to_h6(cash_rules, day=30)
    champ, _, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(32), rules())
    assert champ["return"] == 0.0 and champ["max_drawdown"] == 0.0 and champ["avg_exposure"] == 0.0


def test_a_start_equity_that_is_not_a_record_does_not_stop_the_title_side(cash_rules):
    cash_test(cash_rules, STRONG)
    slot.save("challenger1", {**slot.load("challenger1"), "start_equity": "cut"})
    equity(cash_rules, "champion", CHAMP)
    title_goes_to_h6(cash_rules)
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(50), rules())
    assert champ["title_to"] == "H6" and chal["return"] is not None


def test_two_cash_judged_winners_in_one_hour_the_second_is_restarted_and_says_it_beat_cash(cash_rules):
    cash_test(cash_rules, STRONG)
    cash_test(cash_rules, [0.0038, -0.0020] * 60, name="challenger2", hyp="H6")   # also a fast pass, a little weaker
    add_hypothesis(cash_rules, "H6")
    config.dump_yaml(cash_rules / "configs" / "challenger2.yaml", H6)
    equity(cash_rules, "champion", CHAMP)
    promote.main(["--now", str(at(60))])
    text = ledger(cash_rules)
    assert "### Result H5: promoted" in text and "### Result H6: restarted" in text
    assert "- Rule: beat cash (first look: challenger skill" in text and "but H5 won by more this hour" in text
    assert slot.load("challenger2")["against"] == "champion" and slot.load("challenger2")["started_at"] == at(60)


def test_a_promotion_during_a_cash_guard_supersedes_it_and_the_new_shadow_runs_the_deposed_config(cash_rules):
    now = guard_after_promotion(cash_rules, [0.001, -0.0005] * 31, now_day=100)
    cash_test(cash_rules, STRONG, name="challenger2", hyp="H6", started=at(40), against="champion")
    add_hypothesis(cash_rules, "H6")
    config.dump_yaml(cash_rules / "configs" / "challenger2.yaml", H6)
    promote.apply("promoted", "H6", "challenger2", now, {"champion": 10000.0})
    text = ledger(cash_rules)
    assert "### Result H5: superseded" in text and "the deposed cash was dropped as the shadow" in text
    assert "- Cash, the deposed side (shadow):" in text
    assert config.account_cfg("shadow")["hypothesis"] == "H5" and config.account_cfg("champion")["hypothesis"] == "H6"


# --- the tests that began against H0 ----------------------------------------------------------------------

def test_an_old_test_is_judged_against_h0_as_before_with_cash_measured_beside(cash_rules):
    cash_test(cash_rules, STRONG, ruleset=6, against=None)                     # began before ruleset 8: one look
    equity(cash_rules, "champion", CHAMP)
    promote.main(["--now", str(at(60))])
    text = ledger(cash_rules)
    assert "### Result H5: promoted" in text and "beat champion skill -1." in text and "vs 1." in text
    assert ("- Against cash (measured, not applied to this test): by its one look rule, on today's numbers it would "
            "be promoted, the same as against the champion\n") in text
    assert config.account_cfg("shadow")["hypothesis"] == "H0"                  # the side it beat is the one guarding


def test_what_cash_makes_of_an_old_test_can_differ_and_is_said(cash_rules):
    cash_test(cash_rules, STEADY, ruleset=6, against=None)
    equity(cash_rules, "champion", [0.0012, 0.0] * 60)                         # a champion that makes more than it
    meta = slot.load("challenger1")
    champ, chal, m = promote.paired_slot("challenger1", meta, at(30), rules())
    said = promote.against_cash_reading(champ, chal, m, rules(), meta, 30.0)
    assert said.startswith("by its one look rule, on today's numbers it would be promoted at day 60, where against "
                           "the champion it would be kept on value: challenger skill")
    assert promote.against_cash_reading(champ, chal, m, RULES, meta, 30.0, early=True).startswith(
        "an early kill reads only the test's own record")
    # an old test kept on value at its one look: the First look block says what cash makes of it too
    promote.main(["--now", str(at(60))])
    text = ledger(cash_rules)
    assert "### First look H5: kept on value" in text
    assert "- Against cash (measured, not applied to this test): by its one look rule, on today's numbers it would " \
           "be promoted, where against the champion it would be kept on value" in text


def test_at_the_verdict_of_a_kept_test_the_reading_against_cash_says_unproven_in_words(cash_rules):
    cash_test(cash_rules, STEADY, ruleset=6, against=None)
    meta = {**slot.load("challenger1"), "first_look": {"at": at(60), "start": 0, "reason": "kept", "on": "value"}}
    equity(cash_rules, "champion", CHAMP)
    champ, chal, m = promote.paired_slot("challenger1", meta, at(120), rules())
    thin = {**chal, "trades": 12}                                               # the numbers pass, the fills do not
    assert promote._outcome(promote.cash_side(m, 0.0), thin, rules(), meta)[0] == "left unproven"
    assert promote.against_cash_reading(champ, thin, m, rules(), meta, 120.0).startswith(
        "by the rule it began under, on today's numbers it would be left unproven, the same as against the champion")


def test_the_summary_shows_each_kind_of_test_in_its_own_words(cash_rules):
    cash_test(cash_rules, STEADY, ruleset=6, against=None)
    cash_test(cash_rules, STRONG, name="challenger2", hyp="H6")
    equity(cash_rules, "champion", CHAMP)
    text = report.test_section(at(30))
    old, new = text.split("- challenger2:")
    assert "  so far: champion " in old and "against cash (measured, not applied to this test): by its one look " in old
    assert "drawdown guard" not in old
    assert "testing H6, judged against cash since" in new and "  so far: cash +0.00% (holds nothing) vs challenger2" in new
    assert "skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing)" in new
    assert "judged against cash: its drawdown guard is set against the equal weight basket's worst fall" in new
    assert "against cash (measured" not in new and "champion change" not in new


def test_the_champions_heading_says_what_it_is_and_what_it_still_runs_for(cash_rules):
    cash_test(cash_rules, STEADY, ruleset=6, against=None)
    equity(cash_rules, "champion", CHAMP)
    (cash_rules / "state" / "champion" / "account.json").write_text(json.dumps({
        "cash": 10000.0, "initial_cash": 10000.0, "created_at": 0, "fees_paid": 0.0, "slippage_paid": 0.0,
        "n_trades": 0, "positions": {}, "last_run_ts": at(30), "halted_day": None}))
    text = report.account_section("champion", at(30))
    assert ("retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This "
            "account runs H0 only as the yardstick for the tests judged against this account (H5 in challenger1), "
            "and holds cash once they end") in text
    slot.reset("challenger1")
    assert "only as the yardstick for no test any more, so its config becomes cash at the next ruling" in \
        report.account_section("champion", at(30))
    config.dump_yaml(cash_rules / "configs" / "champion.yaml", dict(CASH))
    assert ("the champion's config is cash: no config holds the title now, so a new test is judged against cash and "
            "this account holds nothing") in report.account_section("champion", at(30))
    set_rules(cash_rules, retired_champions=False)
    config.dump_yaml(cash_rules / "configs" / "champion.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    assert "retired" not in report.account_section("champion", at(30))


# --- when no test needs H0 any more ------------------------------------------------------------------------

def test_the_champion_account_holds_cash_once_no_test_is_judged_against_it(cash_rules, capsys):
    cash_test(cash_rules, LOSING, ruleset=6, against=None, sell_price=99.0)    # the last test against H0
    equity(cash_rules, "champion", CHAMP)
    promote.main(["--now", str(at(30))])                                       # running: H0 stays
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    promote.main(["--now", str(at(60))])                                       # killed at its look
    assert "### Result H5: killed" in ledger(cash_rules)
    assert config.account_cfg("champion") == CASH
    assert "H0 is retired and no test is judged against it any more" in capsys.readouterr().out
    last = promote.champion_changes()[-1]
    assert (last["from"], last["to"], last["exposure"]) == ("H0", "cash", 0.0)
    assert last["why"] == "H0 retired (configs/risk.yaml, retired_champions)"
    assert promote.retire_champion(at(61), promote.rule_settings(rules())[0]) is False


def test_what_holds_the_switch_to_cash(cash_rules):
    st = promote.rule_settings(rules())[0]
    cash_test(cash_rules, STEADY)                                               # judged against cash: holds nothing
    meta2 = cash_rules / "state" / "challenger2" / "meta.json"
    meta2.parent.mkdir(parents=True, exist_ok=True)
    config.dump_yaml(cash_rules / "configs" / "challenger2.yaml", H6)          # a config of its own
    for bad in ("{cut", "[]", json.dumps({"hypothesis": "H6"})):               # a record that cannot be read as one
        meta2.write_text(bad)
        assert promote.switch_holders() == ["challenger2, whose record cannot be read"], bad
        assert promote.retire_champion(at(5), st) is False
    (cash_rules / "configs" / "challenger2.yaml").write_text("strategy: [cut")   # nor can its config be read
    assert promote.switch_holders() == ["challenger2, whose record cannot be read"]
    config.write_challenger_idle("challenger2")                                 # on cash, it holds no test
    assert promote.switch_holders() == []
    slot.reset("challenger2")
    shadow.start({"hypothesis": "H9", "strategy": "ts_momentum", "params": {}}, "H0", at(5), 1.0, 1.0)
    assert promote.retire_champion(at(5), st) is False                          # a promotion is being guarded
    shadow.stop("test")
    # a slot beyond `challenger.slots` that still holds a test from before ruleset 8
    ruleset_8(cash_rules, slots=1)
    cash_test(cash_rules, STEADY, name="challenger2", hyp="H6", ruleset=6, against=None)
    assert promote.switch_holders() == ["H6 in challenger2"] and promote.retire_champion(at(5), st) is False
    slot.reset("challenger2")
    assert promote.retire_champion(at(5), st) is True and config.account_cfg("champion") == CASH
    assert slot.load("challenger1")["against"] == "cash"                        # the cash test carries on as it was


def test_a_champion_yaml_that_cannot_be_written_stops_the_hour(cash_rules, monkeypatch):
    def refuse(*a, **k):
        raise OSError("disk full")
    monkeypatch.setattr(config, "dump_yaml", refuse)
    with pytest.raises(OSError):
        promote.retire_champion(at(5), promote.rule_settings(rules())[0])
