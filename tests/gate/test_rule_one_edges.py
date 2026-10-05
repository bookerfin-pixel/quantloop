"""PROTECTED. Rule 1 at its edges: the cases four rounds of independent review
found on 2026-10-05 before ruleset 7 shipped (gaps in the record, a champion
that changes during a test, idle slots after a promotion, settings that cannot
be used, readings that are not numbers, market data that is missing in part,
the early kill, and every bar at its exact value)."""
import csv
import json
import math

import numpy as np
import pandas as pd
import pytest
import yaml

from bot import config, data, promote, report, shadow, slot

from .test_two_looks import (CHAMP, DAY, RULES, STEADY, STRONG, THIN, at, equity, ledger,  # noqa: F401
                             sandbox, set_rules, start_test, trades)


# --- a market that moves, so the basket leg of the skill is really in the sum ----------------------

def moving_market(root, daily_market_returns, days=125):
    """BTC candles whose price steps once a day, at noon, by that day's return."""
    rows, price = [], 100.0
    for h in range(days * 24):
        d, hour = divmod(h, 24)
        o = price
        if hour == 12 and d < len(daily_market_returns):
            price *= 1 + daily_market_returns[d]
        rows.append({"time": h * 3600, "open": o, "high": max(o, price), "low": min(o, price), "close": price,
                     "vwap": price, "volume": 1, "count": 1})
    pd.DataFrame(rows).to_csv(root / "state" / "candles" / "BTC.csv", index=False)
    getattr(data, "_READ_CACHE", {}).clear()


def equity_at_day_end(root, name, daily_returns, skip_days=(), exposure=0.5):
    """One row at 23:30 of each day; a skipped day has no row and its return lands on the next one.
    exposure: the share of equity invested, one number or one per day."""
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    eq = 10_000.0
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "equity", "cash", "gross_exposure", "n_positions",
                                          "fees_paid", "slippage_paid"])
        w.writeheader()
        for k, r in enumerate(daily_returns):
            eq *= 1 + r
            e = exposure[k] if isinstance(exposure, (list, tuple)) else exposure
            if k not in skip_days:
                w.writerow({"ts": k * DAY + 23 * 3600 + 1800, "equity": eq, "cash": eq * (1 - e),
                            "gross_exposure": eq * e, "n_positions": 1, "fees_paid": 0.01 * k, "slippage_paid": 0})


def hourly_world(root, name, daily_skill, market_hourly, skip_hours=()):
    """Hourly candles and an hourly equity record that go together: the account
    holds half the market, rebalanced every hour, and adds that day's skill in
    the day's first hour. Rows sit 25 minutes past each hour, as the live ones
    do, and are valued at the last candle that had closed by then."""
    rows, price = [], 100.0
    for h, m in enumerate(market_hourly):
        o = price
        price *= 1 + m
        rows.append({"time": h * 3600, "open": o, "high": max(o, price), "low": min(o, price), "close": price,
                     "vwap": price, "volume": 1, "count": 1})
    pd.DataFrame(rows).to_csv(root / "state" / "candles" / "BTC.csv", index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    eq, out = 10_000.0, []
    for h in range(1, len(market_hourly) + 1):                 # at h o'clock the candle that opened at h-1 has closed
        eq *= 1 + 0.5 * market_hourly[h - 1]
        if h % 24 == 0 and h // 24 - 1 < len(daily_skill):
            eq *= 1 + daily_skill[h // 24 - 1]
        if h not in skip_hours:
            out.append({"ts": h * 3600 + 1500, "equity": eq, "cash": eq / 2, "gross_exposure": eq / 2,
                        "n_positions": 1, "fees_paid": 0.0, "slippage_paid": 0.0})
    p = root / "state" / name / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(out).to_csv(p, index=False)


def chal_at(day, rules=RULES):
    return promote.paired_slot("challenger1", slot.load("challenger1"), at(day), rules)[1]


def test_the_basket_is_taken_out_of_the_daily_skill(sandbox):
    """With a moving market, daily skill is the account's return minus its
    benchmark exposure (0.5 here) times the basket's. Leaving the basket in, or
    taking it out with the wrong sign, gives a different t."""
    market = [0.01, -0.006] * 60                                     # the market itself drifts up 0.2% a day
    moving_market(sandbox, market)
    start_test(sandbox, STEADY)
    equity_at_day_end(sandbox, "challenger1", [0.5 * m + s for m, s in zip(market, STEADY)])
    chal = chal_at(120)
    s = np.array(STEADY)
    want = s.mean() / (s.std(ddof=1) / math.sqrt(len(s)))
    assert chal["skill_days"] == 120 and chal["skill_t"] == pytest.approx(want, abs=0.05)
    raw = np.array([0.5 * m + x for m, x in zip(market, STEADY)])
    assert abs(raw.mean() / (raw.std(ddof=1) / math.sqrt(120)) - want) > 0.5     # the two are not the same number


def test_days_missing_from_the_record_do_not_bend_the_daily_skill_t(sandbox):
    """Three days with no rows while the market rises 26%. The first row back
    carries the account's return for all of them, and the basket's return over
    the same span must come off it. It used to take off one day's: the gap then
    read as a 12% day of pure skill."""
    market = [0.001] * 70 + [0.08] * 3 + [0.001] * 47
    moving_market(sandbox, market)
    start_test(sandbox, STEADY)
    account = [0.5 * m + s for m, s in zip(market, STEADY)]
    equity_at_day_end(sandbox, "challenger1", account)
    whole = chal_at(120)
    equity_at_day_end(sandbox, "challenger1", account, skip_days={70, 71, 72})
    gapped = chal_at(120)
    assert whole["skill_days"] == 120 and gapped["skill_days"] == 117
    assert whole["skill"] == pytest.approx(gapped["skill"])                      # the same account, the same total
    assert abs(gapped["skill_t"] - whole["skill_t"]) < 0.5
    assert 1.0 < gapped["skill_t"] < 2.5 and 1.0 < whole["skill_t"] < 2.5
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)
    assert chal["edge_t"] is not None and abs(chal["edge_t"]) < 5                # the edge t shares the fix


def test_a_gap_in_a_rising_market_does_not_turn_a_thin_test_into_a_promotion(sandbox):
    """The case the review ran: skill too thin to tell from luck, three days
    missing while the market rose. Read as one 12% day of skill, the t cleared
    the bar and `unproven` became `promoted`."""
    market = [0.0] * 70 + [0.05] * 3 + [0.0] * 47
    moving_market(sandbox, market)
    start_test(sandbox, THIN)
    account = [0.5 * m + s for m, s in zip(market, THIN)]
    equity_at_day_end(sandbox, "champion", [0.5 * m + c for m, c in zip(market, CHAMP)])
    equity_at_day_end(sandbox, "challenger1", account, skip_days={70, 71, 72})
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    gapped = chal_at(120)
    assert gapped["skill"] > 0 and gapped["skill_days"] == 117
    assert 0 < gapped["skill_t"] < 0.6                           # one 8% day of "skill" alone makes a t of about 1
    promote.main(["--now", str(at(120))])
    assert "### Result H5: unproven" in ledger(sandbox) and config.account_cfg("champion")["hypothesis"] == "H0"


@pytest.mark.parametrize("move", [0.12, -0.12])
def test_an_outage_that_starts_inside_a_day_does_not_bend_the_daily_skill_t(sandbox, move):
    """The bot stops six hours into day 70 and the market moves 12% in the rest
    of that day. The account's reading for day 70 ends at hour six, before the
    move, so the basket's must end there too. Read at the day's end instead,
    day 70 showed 6% of false skill one way and day 73 the same the other way,
    and a t of 1.7 fell to 0.6."""
    hours = 121 * 24
    market = [0.0] * hours
    market[70 * 24 + 12] = move                                   # one candle, at noon on day 70
    start_test(sandbox, STEADY)
    hourly_world(sandbox, "champion", CHAMP, market)
    hourly_world(sandbox, "challenger1", STEADY, market)
    whole = chal_at(120)
    down = set(range(70 * 24 + 6, 73 * 24 + 1))                   # no rows from 06:25 on day 70 until day 73
    hourly_world(sandbox, "champion", CHAMP, market, skip_hours=down)
    hourly_world(sandbox, "challenger1", STEADY, market, skip_hours=down)
    gapped = chal_at(120)
    assert whole["skill_days"] == 120 and gapped["skill_days"] == 118
    assert 1.3 < whole["skill_t"] < 2.3
    assert abs(gapped["skill_t"] - whole["skill_t"]) < 0.3
    assert abs(gapped["edge_t"] - whole["edge_t"]) < 0.5


def test_the_edge_t_takes_the_basket_out_at_each_sides_own_exposure(sandbox, monkeypatch):
    """The challenger usually holds 80% of the market and the champion 20%. Their
    daily edge is then mostly the market's own moves unless each side's
    benchmark comes off first."""
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: 0.8 if cfg["hypothesis"] == "H5" else 0.2)
    market = [0.02, -0.018] * 60
    moving_market(sandbox, market)
    start_test(sandbox, STEADY)
    equity_at_day_end(sandbox, "champion", [0.2 * m + c for m, c in zip(market, CHAMP)])
    equity_at_day_end(sandbox, "challenger1", [0.8 * m + x for m, x in zip(market, STEADY)])
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)
    edge = np.array(STEADY) - np.array(CHAMP)
    want = edge.mean() / (edge.std(ddof=1) / math.sqrt(120))
    assert chal["edge_days"] == 120 and chal["edge_t"] == pytest.approx(want, rel=0.1)
    raw = np.array([0.6 * m for m in market]) + edge                # what is left if the basket stays in
    assert raw.mean() / (raw.std(ddof=1) / math.sqrt(120)) < want / 2


def test_a_last_day_that_has_barely_begun_is_not_a_reading_of_its_own(sandbox):
    start_test(sandbox, STEADY)
    hourly = sandbox / "state" / "challenger1" / "equity.csv"
    rows = [{"ts": h * 3600 + 1500, "equity": 10_000 * (1 + 0.00002 * h + 0.001 * (h % 7 == 0)), "cash": 1,
             "gross_exposure": 1, "n_positions": 1, "fees_paid": 0, "slippage_paid": 0} for h in range(62 * 24)]
    pd.DataFrame(rows).to_csv(hourly, index=False)
    d = promote._daily("challenger1", 0, 60 * DAY + 2 * 3600, 10_000.0)          # two hours into day 60
    assert len(d) == 60
    assert len(promote._daily("challenger1", 0, 60 * DAY + 13 * 3600, 10_000.0)) == 61   # past half way it counts
    whole = promote._daily("challenger1", 0, 60 * DAY + 2 * 3600, 10_000.0)["ret"]
    last_equity = rows[60 * 24 + 1]["equity"]
    assert (1 + whole).prod() == pytest.approx(last_equity / 10_000.0)           # and nothing is dropped


def test_no_reading_from_a_handful_of_days_or_a_series_with_no_spread(sandbox):
    ten = pd.Series([0.001, 0.003] * 5)
    assert promote._t_stat(ten, promote.MIN_SKILL_T_DAYS)[0] is not None         # ten readings are enough
    assert promote._t_stat(ten.iloc[:9], promote.MIN_SKILL_T_DAYS) == (None, 9)  # nine are not
    start_test(sandbox, STRONG)
    assert chal_at(8)["skill_t"] is None                                         # 8 or 9 days: no t at all
    assert chal_at(8)["skill_days"] < promote.MIN_SKILL_T_DAYS
    assert "10%, the starting figure for any idea (no reading of the daily skill t yet" in \
        promote.confidence_text(chal_at(8), RULES)
    assert chal_at(12)["skill_t"] is not None
    equity(sandbox, "challenger1", [0.001] * 120)                                # the same return every day
    flat = chal_at(59.9)
    assert flat["skill_days"] == 60 and flat["skill_t"] is None                  # a spread of 1e-17 is not a reading
    assert promote.confidence(flat["skill_t"], flat["skill_days"], RULES) is None
    t, n = promote._t_stat(pd.Series([0.001, float("inf"), 0.002, float("nan")] + [0.001, 0.002] * 6), 10)
    assert n == 14 and t is not None and math.isfinite(t)                        # not finite values are left out


# --- readings that are not numbers never pass a bar ------------------------------------------------

def test_no_reading_is_never_a_pass():
    good = {"return": 0.05, "max_drawdown": -0.01, "trades": 40, "round_trips": 20, "skill": 0.05,
            "avg_exposure": 0.5, "skill_exposure": 0.5, "skill_days": 120, "edge_t": None}
    champ = {"return": 0.0, "max_drawdown": -0.01, "trades": 40, "skill": 0.0, "skill_exposure": 0.5}
    for t in (None, float("nan"), float("inf") * 0, "x"):
        verdict, why = promote.decide_final(champ, {**good, "skill_t": t}, RULES)
        assert verdict == "unproven" and "no reading of the daily skill t" in why
        assert promote.fast_pass({**good, "skill_t": t}, RULES) is None
    assert promote.confidence(float("nan"), 120, RULES) is None
    assert promote.confidence(float("inf"), 120, RULES) is None
    # and each bar at its exact value passes; a hair under does not
    assert promote.decide_final(champ, {**good, "skill_t": 1.0}, RULES)[0] == "promoted"
    assert promote.decide_final(champ, {**good, "skill_t": 0.999}, RULES)[0] == "unproven"
    assert "+0.96 over 120 days, under the 1.0" in promote.decide_final(champ, {**good, "skill_t": 0.96}, RULES)[1]
    assert promote.fast_pass({**good, "skill_t": 1.999}, RULES) is None


# --- the second look reads all 120 days ------------------------------------------------------------

def test_the_second_look_reads_the_whole_test_not_either_half(sandbox):
    # a good first half followed by a noisy flat one: the first 60 days alone would clear the bar
    start_test(sandbox, STEADY[:60] + [0.006, -0.006] * 30)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    assert chal_at(60)["skill_t"] > 1.0 > chal_at(120)["skill_t"] > 0
    promote.main(["--now", str(at(120))])
    assert "### Result H5: unproven" in ledger(sandbox)


def test_a_strong_second_half_does_not_carry_a_test_whose_whole_record_is_thin(sandbox):
    # a noisy first half that barely passes, then 60 tidy days: the last 60 alone would clear the bar
    series = [0.0104, -0.0096] * 30 + [0.0025, -0.0015] * 30
    start_test(sandbox, series)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    last = np.array(series[60:])
    assert last.mean() / (last.std(ddof=1) / math.sqrt(60)) > 1.5 and chal_at(120)["skill_t"] < 1.0
    promote.main(["--now", str(at(120))])
    assert "### Result H5: unproven" in ledger(sandbox)


# --- the ordinary rule still stands at both looks ----------------------------------------------------

def test_beating_a_weak_champion_with_skill_below_zero_does_not_pass_the_first_look(sandbox):
    """It beat a champion that lost more, and made less than holding its usual
    share of the market. That is not a pass. Whether it is killed then turns on
    its trades: they lost money, so it is."""
    start_test(sandbox, [-0.0006, 0.0002] * 60, champion_returns=[-0.0030, 0.0010] * 60)
    trades(sandbox, "challenger1", sell_price=99.0)
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "first look:" in text and "but not the +0.00% floor" in text
    assert "it did no better than holding the basket at its usual exposure 0.50" in text
    assert "It is not kept on value either: its 20 finished trades made -2.00%" in text


@pytest.mark.parametrize("sell_price,verdict", [(99.0, "killed"), (101.0, "unproven")])
def test_a_test_that_gives_it_all_back_does_not_pass_the_second_look_even_above_the_champion(sandbox, sell_price, verdict):
    """It passed its first look and lost it all in the next 60 days: skill below
    zero on the whole test, still ahead of a champion that lost more. Not a
    promotion. A kill if its trades lost money, unproven if they made some."""
    start_test(sandbox, STEADY[:60] + [-0.0025, 0.0010] * 30, champion_returns=[-0.0030, 0.0010] * 60)
    trades(sandbox, "challenger1", n=100, sell_price=sell_price)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert f"### Result H5: {verdict}" in text and "second look:" in text and "but not the +0.00% floor" in text
    if verdict == "killed":
        assert "It is not kept on value either: its 50 finished trades made -5.00% of its starting equity" in text
    else:
        assert "Its trades are of value all the same (its 50 finished trades made +5.00%" in text


def test_a_test_whose_trades_made_money_but_which_made_less_than_holding_its_usual_share_is_unproven(sandbox, monkeypatch):
    """The market rises 0.2% a day. The challenger usually holds 80% of it but
    held 20% on average. Holding its usual 80% would have made far more, so it
    does not pass the rule. Its finished trades made money, so it is not
    killed either."""
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: 0.8 if cfg["hypothesis"] == "H5" else 0.5)
    market = [0.002] * 120
    moving_market(sandbox, market)
    start_test(sandbox, STEADY)
    equity_at_day_end(sandbox, "champion", [0.5 * m + c for m, c in zip(market, CHAMP)])
    equity_at_day_end(sandbox, "challenger1", [0.2 * m + x for m, x in zip(market, STEADY)], exposure=0.2)
    chal = chal_at(60)
    assert chal["skill"] < -0.03 and chal["trade_profit"] > 0                    # behind its usual share, trades in profit
    promote.main(["--now", str(at(60))])
    assert "### First look H5: kept on value" in ledger(sandbox)
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: unproven" in text and "Its trades are of value all the same" in text
    assert "but not the +0.00% floor" in text or "did not beat champion skill" in text


def test_an_old_test_with_skill_below_zero_is_not_promoted_by_its_one_look(sandbox):
    start_test(sandbox, [-0.0006, 0.0002] * 60, ruleset=6, champion_returns=[-0.0030, 0.0010] * 60)
    trades(sandbox, "challenger1", sell_price=99.0)
    promote.main(["--now", str(at(60))])
    assert "### Result H5: killed" in ledger(sandbox) and "but not the +0.00% floor" in ledger(sandbox)
    assert "first look:" not in ledger(sandbox)


def test_the_drawdown_guard_holds_at_the_second_look(sandbox):
    # 60 good days, a slide of 11% (inside the 15% early kill, outside the 10% guard), then a strong recovery
    series = STEADY[:62] + [-0.012] * 10 + [0.006, 0.002] * 24
    start_test(sandbox, series)
    promote.main(["--now", str(at(60))])
    for day in (70, 73, 90):
        promote.main(["--now", str(at(day))])
    assert "### Result H5" not in ledger(sandbox)                                # no early kill
    final = chal_at(120)
    assert final["skill"] > 0 and final["max_drawdown"] < -0.10
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "second look:" in text and "exceeded the limit" in text


def test_the_cost_kill_applies_to_a_two_look_test(sandbox):
    rules = {**RULES, "treadmill_kill_multiple": 3.0, "treadmill_min_days": 14}
    config.dump_yaml(sandbox / "configs" / "risk.yaml",
                     {"ruleset": 7, "challenger": rules, "pairs": ["BTC"], "initial_cash": 10000, "fee_bps": 10,
                      "slippage_bps": 5, "backtest_gate": {"max_cost_drag": 0.15}})
    start_test(sandbox, STEADY)
    eq = pd.read_csv(sandbox / "state" / "challenger1" / "equity.csv")
    eq["fees_paid"] = 15.0 * np.arange(len(eq))                                  # 15 a day on 10,000 is 55% a year
    eq.to_csv(sandbox / "state" / "challenger1" / "equity.csv", index=False)
    promote.main(["--now", str(at(20))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "fees treadmill" in text and "- Confidence: " in text


def test_the_early_kill_still_applies_between_the_two_looks(sandbox):
    """A test that has had its first look is still watched every hour: a slide
    past the 15% limit ends it that day, not at day 120."""
    start_test(sandbox, STEADY[:62] + [-0.02] * 10 + [0.0] * 48)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    promote.main(["--now", str(at(66))])                                         # down 8% from its high: carries on
    assert "### Result H5" not in ledger(sandbox)
    promote.main(["--now", str(at(75))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "early kill limit" in text and "- Status: killed" in text
    assert slot.load("challenger1")["status"] == "idle" and config.account_cfg("champion")["hypothesis"] == "H0"


# --- the state machine --------------------------------------------------------------------------------

def test_the_first_look_and_the_verdict_never_fall_in_the_same_hour(sandbox):
    """The bot comes back from an outage past day 120 with no first look on record."""
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(121))])
    text = ledger(sandbox)
    assert "### First look H5: passed" in text and "### Result H5" not in text
    assert slot.load("challenger1")["status"] == "testing"
    promote.main(["--now", str(at(121) + 3600)])
    assert "### Result H5: promoted" in ledger(sandbox) and ledger(sandbox).count("### First look H5") == 1


def test_a_first_look_belongs_to_the_window_it_was_taken_in(sandbox):
    """A slot clock reset by hand (as H2's and H3's were) starts a new window.
    The old pass must not stand in for the new window's first look."""
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    meta = slot.load("challenger1")
    assert promote.first_look_of(meta) and meta["first_look"]["start"] == 0
    meta["started_at"] = 30 * DAY                                                # the clock is reset to day 30
    slot.save("challenger1", meta)
    trades(sandbox, "challenger1", n=95)                                         # enough fills inside the new window
    assert promote.first_look_of(meta) is None
    assert "first look at day 60 (two look rule)" in slot.describe_one("challenger1", 31 * DAY)
    assert "first look passed" not in slot.describe_one("challenger1", 31 * DAY)
    promote.main(["--now", str(30 * DAY + 59 * DAY)])
    assert ledger(sandbox).count("### First look H5") == 1                       # day 59 of the new window: nothing
    promote.main(["--now", str(30 * DAY + 60 * DAY + 7200)])
    assert ledger(sandbox).count("### First look H5") == 2                       # its own first look, at its day 60
    assert slot.load("challenger1")["first_look"]["start"] == 30 * DAY


def test_a_test_between_its_looks_is_never_ruled_by_the_one_look_rule(sandbox):
    """If the rule is switched off in the rules file while a test is between its
    looks, that test still gets its second look, on the documented 60 days.
    THIN would be promoted by the one look rule; it must come out unproven."""
    start_test(sandbox, THIN)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    rules = set_rules(sandbox, confirm_days=None, two_looks_from_ruleset=False)
    assert promote.two_looks(slot.load("challenger1"), rules)                    # still a two look test
    assert not promote.two_looks({"ruleset": 7, "started_at": 0}, rules)         # a new one would not be
    assert promote.total_days(slot.load("challenger1"), rules) == 120
    promote.main(["--now", str(at(75))])
    assert "### Result H5" not in ledger(sandbox)                                # and not ruled early either
    promote.main(["--now", str(at(120))])
    text = ledger(sandbox)
    assert "### Result H5: unproven" in text and "### Result H5: promoted" not in text
    assert config.account_cfg("champion")["hypothesis"] == "H0"


def test_two_fast_passes_in_one_hour_promote_one_and_restart_the_other_without_the_fast_pass_wording(sandbox):
    start_test(sandbox, STRONG)
    config.dump_yaml(sandbox / "configs" / "challenger2.yaml",
                     {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox) + "\n## H6: another\n- Expected gross bps per round trip: 90\n"
                                                           "- Status: testing\n")
    slot.save("challenger2", {"status": "testing", "hypothesis": "H6", "started_at": 0, "ruleset": 7,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0}})
    equity(sandbox, "challenger2", [0.0050, -0.0020] * 60)                       # stronger still
    trades(sandbox, "challenger2")
    (sandbox / "state" / "challenger2" / "account.json").write_text(json.dumps({"cash": 1}))
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H6: promoted" in text and "### Result H5: restarted" in text
    restarted = text[text.index("### Result H5: restarted"):]
    assert "H6 won by more this hour" in restarted and "promoted without waiting" not in restarted
    meta = slot.load("challenger1")
    assert meta["status"] == "testing" and meta["started_at"] == at(60) and "first_look" not in meta
    assert meta["ruleset"] == 7 and promote.two_looks(meta, RULES)               # a restart begins under today's rules


def test_an_early_kill_of_an_old_test_says_the_new_rule_shares_it(sandbox):
    start_test(sandbox, [-0.02] * 10 + [0.0] * 110, ruleset=6)
    promote.main(["--now", str(at(12))])
    result = ledger(sandbox)[ledger(sandbox).index("### Result H5"):]
    assert "### Result H5: killed" in result and "early kill limit" in result
    assert "- Two look rule (measured, not applied to this test): the early kill is the same under both rules" in result
    assert "it would pass the first look" not in result and "it would fail the first look" not in result


# --- settings left blank or mistyped never stop the hour ----------------------------------------------

@pytest.mark.parametrize("changes", [
    {"min_skill_t": "", "fast_pass_skill_t": ""},
    {"confidence": 5},
    {"confidence": {"prior": "lots", "edge_sharpe": None}},
    {"confidence": "", "confirm_days": "sixty"},
    {"two_looks_from_ruleset": "seven"},
    # settings older than ruleset 7, which the rule reads too: each of these used to stop the hour, some
    # of them only once a test reached day 60
    {"early_kill_drawdown": "15%"},
    {"window_days": "sixty"},
    {"min_skill": ""},
    {"min_trades": None},
    {"max_dd_floor": "", "max_dd_ratio": "one and a half"},
    {"min_return_edge": ""},
    {"confirm_days": 10 ** 400},
    {"compare_on": 5, "min_trade_profit": "none"},
    {"treadmill_kill_multiple": "3x", "treadmill_min_days": ""},
])
def test_a_blank_or_mistyped_setting_does_not_stop_the_summary_or_the_verdicts(sandbox, changes):
    rules = dict(RULES)
    rules.update(changes)
    config.dump_yaml(sandbox / "configs" / "risk.yaml", {"ruleset": 7, "challenger": rules, "pairs": ["BTC"],
                                                          "initial_cash": 10000, "fee_bps": 10, "slippage_bps": 5})
    for stamp in (None, 7):
        start_test(sandbox, STEADY, ruleset=stamp)
        text = report.test_section(at(30))
        assert "confidence: " in text and "readings unavailable" not in text and "could not be read" not in text
        assert text.count("- SETTING NOT USED: challenger.") == len(promote.rule_settings(rules)[1]) >= 1
        assert slot.describe_one("challenger1", at(30)).startswith("challenger1: testing H5")
        assert promote.main(["--now", str(at(30))]) == 0
    assert promote.main(["--now", str(at(60))]) == 0 and promote.main(["--now", str(at(120))]) == 0
    assert "### First look H5" in ledger(sandbox) or "### Result H5" in ledger(sandbox)     # and the rule still ruled


def test_whatever_goes_wrong_in_the_new_summary_lines_the_summary_is_still_written(sandbox, monkeypatch):
    start_test(sandbox, STEADY)

    def boom(*a, **k):
        raise RuntimeError("no")
    monkeypatch.setattr(promote, "confidence_text", boom)
    text = report.test_section(at(30))
    assert "challenger1: testing H5" in text and "so far: champion" in text
    assert "confidence and rule readings unavailable (RuntimeError: no)" in text


def test_settings_that_are_set_are_used_and_blanks_fall_back_to_the_defaults():
    c = promote.confidence
    m = 3.0 * math.sqrt(120 / 365)
    odds = (0.3 / 0.7) * math.exp(m * (2 * 1.0 - m) / 2)
    assert c(1.0, 120, {"confidence": {"prior": 0.3, "edge_sharpe": 3.0}}) == pytest.approx(odds / (1 + odds))
    assert c(1.0, 120, {"confidence": {"prior": 0.3, "edge_sharpe": 3.0}}) != pytest.approx(c(1.0, 120, {}))
    for blank in ({"confidence": None}, {"confidence": 5}, {"confidence": {"prior": None, "edge_sharpe": ""}},
                  {"confidence": {"prior": True}}, {"confidence": {"edge_sharpe": -2}}):
        assert c(1.0, 120, blank) == pytest.approx(c(1.0, 120, {}))
    assert promote._num({"a": "2.5"}, "a", 9) == 2.5 and promote._num({"a": ""}, "a", 9) == 9
    assert promote._num({"a": None}, "a", 9) == 9 and promote._num({}, "a", None) is None
    assert promote._num({"a": float("nan")}, "a", 9) == 9 and promote._num(None, "a", 9) == 9


# --- when the champion changes -------------------------------------------------------------------------

def test_a_promotion_brings_every_idle_slot_into_line_with_the_new_champion(sandbox):
    """An idle slot mirrors the champion. Left on the old champion's config it
    differs from the new one, and the next hourly run would open a test of the
    old champion in it."""
    start_test(sandbox, STRONG)
    assert slot.load("challenger2")["status"] == "idle"
    assert config.account_cfg("challenger2")["hypothesis"] == "H0"
    promote.main(["--now", str(at(60))])                                         # H5 is promoted by the fast pass
    assert config.account_cfg("champion")["hypothesis"] == "H5"
    for name in ("challenger1", "challenger2"):
        assert config.account_cfg(name)["hypothesis"] == "H5" and not slot.configs_differ(name)
    started = slot.maybe_start(at(60) + 3600, {"champion": 1.0, "challenger1": 1.0, "challenger2": 1.0})
    assert all(m["status"] == "idle" for m in started.values())                  # nothing starts by itself
    changes = promote.champion_changes()
    assert len(changes) == 1 and changes[0]["from"] == "H0" and changes[0]["to"] == "H5"
    assert changes[0]["why"] == "promotion" and changes[0]["ts"] == at(60)


def test_an_idle_slot_holding_a_new_hypothesis_is_left_alone(sandbox):
    old = config.strategy_signature(config.account_cfg("champion"))
    config.dump_yaml(sandbox / "configs" / "challenger2.yaml",
                     {"hypothesis": "H8", "strategy": "mean_reversion", "params": {"window_hours": 99}})
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    slot.reset("challenger1")
    config.dump_yaml(sandbox / "configs" / "challenger1.yaml",
                     {"hypothesis": "H0", "strategy": "ts_momentum", "params": {"lookback_hours": 72}})
    assert promote.sync_idle_slots(old) == ["challenger1"]
    assert config.account_cfg("challenger1")["hypothesis"] == "H5"
    assert config.account_cfg("challenger2")["hypothesis"] == "H8"               # waiting for its first hour


def test_a_revert_also_brings_idle_slots_back_and_is_on_the_record(sandbox):
    now = 100
    slot.reset("challenger1")
    shadow.start(config.account_cfg("champion"), "H5", now, 10000.0, 10000.0)    # H0 deposed by H5
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    for name in ("challenger1", "challenger2"):
        config.write_challenger_from_champion(name)
    (sandbox / "LEDGER.md").write_text(ledger(sandbox).replace("- Status: testing", "- Status: promoted"))
    later = now + 60 * DAY + 100
    equity(sandbox, "champion", [-0.002, 0.0] * 31)
    equity(sandbox, "shadow", [0.004, -0.001] * 31)
    trades(sandbox, "shadow")
    promote.rule_on_shadow(later, RULES)
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    assert "### Result H5: reverted" in ledger(sandbox)
    for name in ("challenger1", "challenger2"):
        assert config.account_cfg(name)["hypothesis"] == "H0" and not slot.configs_differ(name)
    changes = promote.champion_changes()
    assert changes[-1]["why"] == "revert" and changes[-1]["from"] == "H5" and changes[-1]["to"] == "H0"


def falling_after(root, day, total_fall=-0.30, days=125):
    """A market that is flat until `day` and then falls by `total_fall` in equal daily steps to day 120."""
    step = (1 + total_fall) ** (1 / (120 - day)) - 1
    moving_market(root, [0.0] * day + [step] * (120 - day), days=days)


def test_the_champion_side_is_benchmarked_config_by_config_when_it_changes(sandbox):
    """The review's case. The champion goes from a config that usually holds
    50% to one that usually holds 10% on day 80, and the market then falls 30%.
    The new champion simply holds its 10%. That is no skill, and it must not
    read as any: scored against 50% for the whole window it read +12%, against
    the window's average +8%, and a good challenger was killed for it."""
    falling_after(sandbox, 80)
    start_test(sandbox, STEADY)
    step = 0.70 ** (1 / 40) - 1
    held = [1 + 0.10 * ((1 + step) ** k - 1) for k in range(41)]                 # 10% in the basket, bought once and held
    noise = [0.002, -0.002] * 60                                                  # plus day to day noise that sums to nothing
    equity_at_day_end(sandbox, "champion", [n + (held[k - 80] / held[k - 81] - 1 if k > 80 else 0.0)
                                            for k, n in zip(range(1, 121), noise)])
    equity_at_day_end(sandbox, "challenger1", STEADY)
    promote.record_champion_change(80 * DAY, "H0", "H7", "promotion", 0.10)
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)
    assert champ["skill_basis"] == "usual by config"
    assert champ["exposure_schedule"] == [(0, 0.5), (80 * DAY, 0.10)]
    assert abs(champ["skill"]) < 0.003                                            # no skill, as it should read
    assert champ["skill_exposure"] == pytest.approx((80 * 0.5 + 40 * 0.10) / 120, abs=0.01)
    assert chal["skill_basis"] == "usual" and "exposure_schedule" not in chal     # only the champion side changes
    assert abs(champ["skill_t"]) < 1.0                                            # and its daily skill is flat too
    one = promote.add_skill({"return": champ["return"]}, -0.30, 0.5)["skill"]
    assert one > 0.10                                                             # what one exposure made of it
    assert promote.decide_final(champ, chal, RULES)[0] == "promoted"              # the challenger is judged on its own merit
    line = promote._fmt(champ)
    assert "against the basket at each config's usual exposure (0.50 then 0.10)" in line
    assert "usual 0.50 then 0.10 by config" in report.test_section(at(120))


def test_a_change_late_in_the_window_leaves_the_days_before_it_alone(sandbox):
    """One change on day 119.5 used to move the champion's benchmark for all 120 days."""
    moving_market(sandbox, [0.002] * 120)                                         # a market up 27%
    start_test(sandbox, STEADY)
    equity_at_day_end(sandbox, "champion", [0.5 * 0.002 + c for c in CHAMP])
    equity_at_day_end(sandbox, "challenger1", [0.5 * 0.002 + x for x in STEADY])
    before = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)[0]
    promote.record_champion_change(int(119.5 * DAY), "H0", "H7", "promotion", 0.95)
    after = promote.paired_slot("challenger1", slot.load("challenger1"), at(120), RULES)[0]
    assert before["skill_basis"] == "usual" and after["skill_basis"] == "usual by config"
    assert after["skill"] == pytest.approx(before["skill"], abs=0.003)


def test_without_a_usual_exposure_on_record_the_window_average_stands_in_and_says_so(sandbox):
    start_test(sandbox, STEADY)
    promote.record_champion_change(40 * DAY, "H0", "H7", "promotion")            # no exposure known
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(90), RULES)
    assert champ["skill_basis"] == "window" and "exposure_schedule" not in champ and chal["skill_basis"] == "usual"
    note = promote.champion_note(0, at(90), bool(champ.get("exposure_schedule")))
    assert "H0 at the start, then H7 from 1970-02-10 (promotion)" in note
    assert "average exposure in the window, because a usual exposure is not on record" in note
    assert promote.champion_note(0, at(90)).endswith("across them")              # when the caller does not know how
    assert promote.champion_note(0, at(90), False, measured=False).endswith("across them")   # or nothing was measured
    text = report.test_section(at(90))
    assert "  champion change: the champion's config changed during this test" in text
    assert "which stands in for a usual exposure" in text
    # and the ledger says the same, not that it was measured stretch by stretch
    promote.main(["--now", str(at(60))])
    block = ledger(sandbox)[ledger(sandbox).index("### First look H5"):]
    assert "- Champion change: the champion's config changed during this test" in block
    assert "average exposure in the window, because a usual exposure is not on record" in block
    assert "stretch by stretch" not in block


def test_a_champion_change_is_said_in_every_block_of_a_test_it_touched(sandbox):
    start_test(sandbox, STEADY)
    promote.record_champion_change(40 * DAY, "H0", "H7", "promotion", 0.3)
    promote.main(["--now", str(at(60))])
    first = ledger(sandbox)[ledger(sandbox).index("### First look H5"):]
    assert "- Champion change: the champion's config changed during this test" in first
    assert "stretch by stretch, each against the usual exposure of the config that ran it" in first
    promote.main(["--now", str(at(120))])
    result = ledger(sandbox)[ledger(sandbox).index("### Result H5"):]
    assert "- Champion change: the champion's config changed during this test" in result
    assert "at each config's usual exposure (0.50 then 0.30)" in result


def test_a_voided_test_also_says_the_champion_changed(sandbox):
    start_test(sandbox, STEADY)
    promote.record_champion_change(10 * DAY, "H0", "H7", "promotion", 0.3)
    config.dump_yaml(sandbox / "configs" / "void.yaml",
                     {"requests": [{"slot": "challenger1", "hypothesis": "H5", "reason": "broken feed"}]})
    promote.main(["--now", str(at(20))])
    block = ledger(sandbox)[ledger(sandbox).index("### Result H5: voided"):]
    assert "- Champion change: the champion's config changed during this test" in block


def test_only_changes_inside_the_window_count_and_all_of_them_are_named(sandbox):
    start_test(sandbox, STEADY)
    meta = {**slot.load("challenger1"), "started_at": 30 * DAY}
    slot.save("challenger1", meta)
    promote.record_champion_change(50 * DAY, "H7", "H8", "promotion", 0.2)       # written out of order on purpose
    promote.record_champion_change(10 * DAY, "H0", "H7", "promotion", 0.9)       # before this test began
    promote.record_champion_change(70 * DAY, "H8", "H7", "revert", 0.9)
    assert [r["ts"] for r in promote.champion_changes()] == [10 * DAY, 50 * DAY, 70 * DAY]     # read back in order
    assert [r["ts"] for r in promote.champion_changed_in(30 * DAY, 100 * DAY)] == [50 * DAY, 70 * DAY]
    champ = promote.paired_slot("challenger1", meta, 100 * DAY, RULES)[0]
    assert champ["exposure_schedule"] == [(30 * DAY, 0.5), (50 * DAY, 0.2), (70 * DAY, 0.9)]
    note = promote.champion_note(30 * DAY, 100 * DAY)
    assert "H7 at the start, then H8 from 1970-02-20 (promotion), H7 from 1970-03-12 (revert)" in note
    earlier = promote.paired_slot("challenger1", {**meta, "started_at": 20 * DAY, "usual_exposure": {}},
                                  29 * DAY, RULES)[0]
    assert earlier["skill_basis"] == "usual" and "exposure_schedule" not in earlier   # a change before the window is not in it


def test_a_change_at_the_first_or_last_moment_of_a_window_is_not_inside_it(sandbox):
    promote.record_champion_change(1000, "H0", "H7", "promotion")
    assert promote.champion_changed_in(1000, 5000) == [] and promote.champion_changed_in(0, 1000) == []
    assert len(promote.champion_changed_in(999, 1001)) == 1


def test_a_changes_file_mended_by_hand_cannot_stop_the_hour_or_be_lost(sandbox):
    path = sandbox / "state" / "champion" / "changes.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('[{"ts": NaN, "to": "H1"}, {"ts": 1e400, "to": "H2"}, {"ts": "soon"}, 7, {"ts": true},'
                    ' {"ts": 5000.0, "from": "H0", "to": "H3", "why": "promotion", "exposure": "x"}]')
    assert [r["ts"] for r in promote.champion_changes()] == [5000]                # the one usable row
    assert promote.champion_changed_in(0, 9999)[0]["to"] == "H3"
    assert promote.champion_schedule(0.5, 0, 9999) is None                        # its exposure is not a number
    assert "average exposure in the window" in promote.champion_note(0, 9999, False)
    path.write_text("{not json")
    assert promote.champion_changes() == [] and promote.champion_note(0, 9999) is None    # never raises
    promote.record_champion_change(2000, "H7", "H0", "revert", 0.4)
    assert [r["ts"] for r in promote.champion_changes()] == [2000]
    kept = sandbox / "state" / "champion" / "changes.unreadable-2000.json"
    assert kept.exists() and kept.read_text() == "{not json"                      # what was there is kept for mending


def test_a_promotion_and_a_revert_put_the_new_champions_usual_exposure_on_record(sandbox):
    start_test(sandbox, STRONG)
    promote.main(["--now", str(at(60))])                                          # promoted by the fast pass
    change = promote.champion_changes()[-1]
    assert change["why"] == "promotion" and change["exposure"] == 0.5 and change["ts"] == at(60)
    later = at(60) + 60 * DAY + 100
    equity(sandbox, "champion", [-0.002, 0.0] * 62)
    eq = pd.read_csv(sandbox / "state" / "champion" / "equity.csv")
    eq.assign(equity=10_000 * (1 + 0.004) ** np.arange(len(eq))).to_csv(sandbox / "state" / "shadow" / "equity.csv",
                                                                         index=False)
    trades(sandbox, "shadow", n=124)
    promote.rule_on_shadow(later, RULES)
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    back = promote.champion_changes()[-1]
    assert back["why"] == "revert" and back["ts"] == later and back["exposure"] == 0.5
    assert back["from"] == "H5" and back["to"] == "H0"


# --- the ledger -------------------------------------------------------------------------------------------

def test_a_status_flip_stays_inside_its_own_ledger_entry(sandbox):
    """H0's entry says `champion`, not `testing`. The match used to run on past
    it and flip the next entry that did say testing."""
    m = {"return": 0.01, "max_drawdown": -0.01, "trades": 40, "fees": 1.0, "gross_pnl": 1.0, "realised_bps": None}
    promote.update_ledger("H0", "killed", "because", m, m, 0, DAY, "challenger1")
    text = ledger(sandbox)
    assert "## H0: base\n- Status: champion" in text
    assert "## H5: pick coins\n- Expected gross bps per round trip: 150\n- Status: testing" in text
    assert "### Result H0: killed" in text                                       # the block is still written
    promote.update_ledger("H5", "killed", "because", m, m, 0, DAY, "challenger1")
    assert "- Status: killed" in ledger(sandbox).split("## Results")[0].split("## H5:")[1]


def test_expected_bps_and_the_status_flip_tell_h1_from_h10(sandbox):
    (sandbox / "LEDGER.md").write_text(
        "# Ledger\n\n## H10: later\n- Expected gross bps per round trip: 310\n- Status: testing\n\n"
        "## H1: earlier, and its bps line is missing\n- Status: testing\n\n"
        "## H12: last\n- Expected gross bps per round trip: 120\n- Status: testing\n")
    assert promote.expected_bps("H10") == 310 and promote.expected_bps("H12") == 120
    assert promote.expected_bps("H1") is None                     # not H12's, the next entry down
    m = {"return": 0.01, "max_drawdown": -0.01, "trades": 40, "fees": 1.0, "gross_pnl": 1.0, "realised_bps": None}
    promote.update_ledger("H1", "killed", "because", m, m, 0, DAY, "challenger1")
    head = ledger(sandbox).split("## Results")[0]
    assert "## H10: later\n- Expected gross bps per round trip: 310\n- Status: testing" in head
    assert "## H1: earlier, and its bps line is missing\n- Status: killed" in head
    assert "## H12: last\n- Expected gross bps per round trip: 120\n- Status: testing" in head


# --- settings that cannot be used: the documented value stands in, and it is said out loud -------------

DOCUMENTED = {"two_from": 7, "window_days": 60.0, "confirm_days": 60.0, "min_skill_t": 1.0, "min_trades": 30,
              "max_dd_ratio": 1.5, "max_dd_floor": 0.10, "min_return_edge": 0.0, "min_skill": 0.0, "early_kill": 0.15,
              "treadmill_multiple": 3.0, "treadmill_min_days": 14.0, "min_trade_profit": 0.0, "fast_pass": 2.0,
              "compare_on": "skill", "prior": 0.10, "edge_sharpe": 1.5}
LINES = ("window_days", "confirm_days", "min_skill_t", "fast_pass_skill_t", "two_looks_from_ruleset", "confidence",
         "min_trades", "min_trade_profit", "max_dd_ratio", "max_dd_floor", "compare_on", "min_return_edge", "min_skill",
         "early_kill_drawdown", "treadmill_kill_multiple", "treadmill_min_days")


def test_rule_settings_reads_what_it_can_and_names_what_it_cannot():
    good, wrong = promote.rule_settings(RULES)
    assert wrong == [] and good == DOCUMENTED
    # Nothing set at all: every line is at its documented value and each is named as missing. A missing line
    # used to mean "off" for seven of them, so a slip in a line's name switched the thing off without a word.
    bare, wrong = promote.rule_settings({})
    assert bare == {**DOCUMENTED, "fast_pass": None}                 # for the fast pass, none is what stands in
    assert len(wrong) == len(LINES) and all(" is not in the file; " in w for w in wrong)
    assert {w.split(" ")[0] for w in wrong} == {f"challenger.{k}" for k in LINES}
    assert promote.rule_settings("not a dict") == (bare, wrong)
    for key in LINES:                                                 # one line lost: that one, and only that one
        st, wrong = promote.rule_settings({k: v for k, v in RULES.items() if k != key})
        assert len(wrong) == 1 and wrong[0].startswith(f"challenger.{key} is not in the file; "), key
        assert st == ({**DOCUMENTED, "fast_pass": None} if key == "fast_pass_skill_t" else DOCUMENTED), key
    # a slip in a line's name is a line this code does not read, and the setting it was meant for is missing
    st, wrong = promote.rule_settings({**{k: v for k, v in RULES.items() if k != "two_looks_from_ruleset"},
                                       "two_looks_from_rulset": 7})
    assert st["two_from"] == 7 and wrong == [
        "challenger.two_looks_from_rulset is not a setting this code reads; nothing uses it",
        "challenger.two_looks_from_ruleset is not in the file; ruleset 7 stands in (to switch the rule off, write `off`)"]
    for slip, meant, name in (("early_kill", "early_kill_drawdown", "early_kill"), ("min_skil", "min_skill", "min_skill"),
                              ("max_dd", "max_dd_floor", "max_dd_floor"), ("compare", "compare_on", "compare_on"),
                              ("treadmill", "treadmill_kill_multiple", "treadmill_multiple")):
        st, wrong = promote.rule_settings({**{k: v for k, v in RULES.items() if k != meant}, slip: RULES[meant]})
        assert st[name] == DOCUMENTED[name] and len(wrong) == 2, slip
    # to switch a thing off on purpose the file says `off`, which YAML reads as False; nothing is said then
    for key, name, value in (("two_looks_from_ruleset", "two_from", None), ("fast_pass_skill_t", "fast_pass", None),
                             ("min_skill_t", "min_skill_t", 0.0), ("min_skill", "min_skill", None),
                             ("max_dd_floor", "max_dd_floor", 0.0), ("early_kill_drawdown", "early_kill", 0.0),
                             ("treadmill_kill_multiple", "treadmill_multiple", 0.0)):
        assert promote.rule_settings({**RULES, key: False}) == ({**good, name: value}, []), key
    for key in ("window_days", "confirm_days", "min_trades", "max_dd_ratio", "min_return_edge", "min_trade_profit",
                "treadmill_min_days", "compare_on", "confidence"):       # these cannot be switched off
        st, wrong = promote.rule_settings({**RULES, key: False})
        assert st == good and len(wrong) == 1 and "cannot be used" in wrong[0], key
    assert yaml.safe_load("a: off\nb: Off\nc: OFF") == {"a": False, "b": False, "c": False}
    # every setting written in a way that cannot be used: the documented value stands in, and each is named
    slips = {"confirm_days": "60 days", "min_skill_t": -1, "fast_pass_skill_t": -2, "two_looks_from_ruleset": "seven",
             "confidence": {"prior": 10, "edge_sharpe": 0}, "min_trade_profit": "0.5%", "window_days": "sixty",
             "min_trades": "", "max_dd_ratio": None, "max_dd_floor": "10%", "min_return_edge": -0.01, "min_skill": "",
             "early_kill_drawdown": "15%", "treadmill_kill_multiple": "3x", "treadmill_min_days": [],
             "compare_on": "skil"}
    st, wrong = promote.rule_settings(slips)
    assert st == {**DOCUMENTED, "fast_pass": None}
    assert len(wrong) == 17 and all("cannot be used" in w for w in wrong)
    said = " | ".join(wrong)
    for piece in ("challenger.confirm_days is '60 days', which cannot be used; 60 days stand in",
                  "challenger.confidence.prior is 10", "challenger.min_trades is ''", "30 stands in",
                  "challenger.max_dd_ratio is None", "challenger.early_kill_drawdown is '15%', which cannot be used; "
                  "15% stands in", "challenger.compare_on is 'skil', which cannot be used; `skill` stands in",
                  "challenger.min_skill is '', which cannot be used; a floor of 0.0% stands in",
                  "challenger.fast_pass_skill_t is -2, which cannot be used; there is no fast pass until it is mended",
                  "challenger.min_return_edge is -0.01"):
        assert piece in said, piece
    # switches that are documented: these are choices, not slips
    assert promote.rule_settings({**RULES, "fast_pass_skill_t": 0}) == ({**good, "fast_pass": None}, [])
    assert promote.rule_settings({**RULES, "min_skill_t": 0}) == ({**good, "min_skill_t": 0.0}, [])
    assert promote.rule_settings({**RULES, "early_kill_drawdown": 0}) == ({**good, "early_kill": 0.0}, [])
    assert promote.rule_settings({**RULES, "treadmill_kill_multiple": 0})[1] == []
    assert promote.rule_settings({**RULES, "min_trade_profit": 0.01}) == ({**good, "min_trade_profit": 0.01}, [])
    assert promote.rule_settings({**RULES, "compare_on": " Skill "}) == (good, [])            # a capital is not a typo
    assert promote.rule_settings({**RULES, "compare_on": "return"})[0]["compare_on"] == "return"
    assert promote.rule_settings({**RULES, "confirm_days": 0})[1] != []                       # 0 days is not a choice
    assert promote.rule_settings({**RULES, "window_days": 0})[1] != []
    # a line that is there and blank is a slip everywhere, and each says so
    for key in ("window_days", "confirm_days", "min_skill_t", "min_trades", "max_dd_ratio", "max_dd_floor",
                "min_return_edge", "min_skill", "early_kill_drawdown", "min_trade_profit", "compare_on",
                "two_looks_from_ruleset", "fast_pass_skill_t", "confidence"):
        st, wrong = promote.rule_settings({**RULES, key: None})
        assert len(wrong) == 1 and f"challenger.{key} is None" in wrong[0], key
        assert st == ({**DOCUMENTED, "fast_pass": None} if key == "fast_pass_skill_t" else DOCUMENTED), key
    # settings that would switch a rule off or widen it by a slip of the hand keep it on, and say so
    for slip in ({"two_looks_from_ruleset": 0}, {"two_looks_from_ruleset": 6}, {"two_looks_from_ruleset": 7.5},
                 {"two_looks_from_ruleset": True}):
        st, wrong = promote.rule_settings({**RULES, **slip})
        assert st["two_from"] == 7 and len(wrong) == 1 and "ruleset 7 stands in" in wrong[0], slip
    for slip in ({"min_trade_profit": -0.05}, {"min_trade_profit": True}, {"min_trade_profit": 2}):
        st, wrong = promote.rule_settings({**RULES, **slip})
        assert st["min_trade_profit"] == 0.0 and len(wrong) == 1, slip
    assert promote.rule_settings({**RULES, "two_looks_from_ruleset": 9})[0]["two_from"] == 9     # a later ruleset is fine
    # a number too large to be one does not raise, and a long value is not printed in full
    st, wrong = promote.rule_settings({**RULES, "confirm_days": 10 ** 400})
    assert st["confirm_days"] == 60.0 and len(wrong) == 1 and len(wrong[0]) < 140


@pytest.mark.parametrize("word", ["skill", "Skill", " SKILL ", "skil", 7])
def test_a_mistyped_compare_on_does_not_fall_back_to_raw_return(sandbox, monkeypatch, word):
    """`compare_on: Skill` used to be read as "not skill", so the rule compared
    raw returns without a word, and a challenger that simply held 0.9 of a
    rising market against the champion's 0.3 was promoted."""
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: 0.9 if cfg["hypothesis"] == "H5" else 0.3)
    market = [0.004, -0.002] * 60                                                 # up 0.1% a day
    moving_market(sandbox, market)
    rules = set_rules(sandbox, compare_on=word)
    start_test(sandbox, STEADY, ruleset=6)
    equity_at_day_end(sandbox, "champion", [0.3 * m + 0.0005 for m in market], exposure=0.3)       # more skill
    equity_at_day_end(sandbox, "challenger1", [0.9 * m + 0.0002 for m in market], exposure=0.9)    # more money
    champ, chal, _ = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), rules)
    assert chal["return"] > champ["return"] and 0 < chal["skill"] < champ["skill"]
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H5: promoted" not in text and "net return" not in text
    assert "### First look H5: kept on value" in text and "did not beat champion skill" in text
    typo = word in ("skil", 7)
    assert ("- SETTING NOT USED: challenger.compare_on is" in report.test_section(at(61))) == typo


def test_with_compare_on_return_the_rule_reads_raw_return_and_needs_no_market_data(sandbox):
    """The rule from before 2026-09-25, when the rules file asks for it by name."""
    rules = set_rules(sandbox, compare_on="return")
    start_test(sandbox, STEADY, ruleset=6)
    (sandbox / "state" / "candles" / "BTC.csv").unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    assert promote.missing_market_data({"gap": "there are no candles for its window"}, rules) is None
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H5: promoted" in text and "challenger net return +" in text and "beat champion -" in text


def test_a_mistyped_confirmation_period_keeps_the_two_look_rule_and_says_so(sandbox, capsys):
    """`confirm_days: "60 days"` used to read as 0, and a new test was quietly promoted at day 60."""
    set_rules(sandbox, confirm_days="60 days")
    start_test(sandbox, THIN)
    promote.main(["--now", str(at(60))])
    out = capsys.readouterr().out
    assert "WARNING: challenger.confirm_days is '60 days', which cannot be used; 60 days stand in" in out
    text = ledger(sandbox)
    assert "### First look H5: passed" in text and "### Result H5" not in text
    assert config.account_cfg("champion")["hypothesis"] == "H0"
    assert "- SETTING NOT USED: challenger.confirm_days is '60 days'" in report.test_section(at(61))
    assert "of 120" in slot.describe_one("challenger1", at(61))


@pytest.mark.parametrize("bar", [0, -1, "", "high"])
def test_a_fast_pass_bar_of_zero_or_nonsense_means_no_fast_pass(sandbox, bar):
    set_rules(sandbox, fast_pass_skill_t=bar)
    start_test(sandbox, STRONG)                                   # t of about 2.6 at day 60
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox) and "### Result H5" not in ledger(sandbox)


def test_a_prior_outside_zero_to_one_falls_back_to_ten_percent():
    assert promote.confidence(1.0, 120, {"confidence": {"prior": 10}}) == pytest.approx(promote.confidence(1.0, 120, {}))
    assert promote.confidence(1.0, 120, {"confidence": {"prior": 0}}) == pytest.approx(promote.confidence(1.0, 120, {}))
    assert promote.confidence(1.0, 120, {"confidence": {"prior": 0.5}}) > promote.confidence(1.0, 120, {})


# --- values that are not numbers ---------------------------------------------------------------------

def test_a_blank_cell_in_the_record_is_not_a_reading_and_promotes_nothing(sandbox, capsys):
    """One blank equity cell at the end of the window made the return NaN, and
    every comparison with NaN is false, so a losing test passed. The engine
    never writes such a row, so it is also a sign of damage: nothing is ruled
    on the account until the file is mended."""
    start_test(sandbox, [-0.0030, 0.0010] * 60, ruleset=6)        # loses about 6% in 60 days
    trades(sandbox, "challenger1", sell_price=99.0)               # and its trades lost money
    p = sandbox / "state" / "challenger1" / "equity.csv"
    eq = pd.read_csv(p)
    eq["equity"] = eq["equity"].astype(object)
    eq.loc[eq["ts"] == 60 * DAY + 3600, "equity"] = ""            # the last row before the verdict
    eq.loc[eq["ts"] == 30 * DAY + 3600, "equity"] = "n/a"
    eq.to_csv(p, index=False)
    chal = promote.window_metrics("challenger1", 0, at(60), 10000.0)      # read by itself, the blank rows are left out
    assert math.isfinite(chal["return"]) and chal["return"] < -0.04 and math.isfinite(chal["max_drawdown"])
    promote.main(["--now", str(at(60))])
    assert "WARNING: challenger1: H5 could not be looked at this hour (Unreadable: challenger1/equity.csv has 2 rows " \
           "that are not a reading (a time, an equity, an exposure and costs, each a number))" in capsys.readouterr().out
    assert "### " not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    # with no account file to set the record against, the blank rows are simply left out: killed, never promoted
    (sandbox / "state" / "challenger1" / "account.json").unlink()
    promote.main(["--now", str(at(60))])
    assert "### Result H5: killed" in ledger(sandbox) and config.account_cfg("champion")["hypothesis"] == "H0"


def test_a_figure_that_is_not_a_number_is_no_data_and_kills(sandbox):
    champ = {"return": 0.0, "max_drawdown": -0.01, "trades": 40, "skill": 0.0, "skill_exposure": 0.5}
    good = {"return": 0.05, "max_drawdown": -0.01, "trades": 40, "skill": 0.05, "skill_exposure": 0.5, "edge_t": None}
    for key in ("return", "skill", "max_drawdown"):
        verdict, why = promote.decide(champ, {**good, key: float("nan")}, RULES)
        assert verdict == "killed" and "not a number" in why
        assert promote.decide({**champ, key: float("nan")}, good, RULES)[0] == "killed"
    assert promote.decide(champ, good, RULES)[0] == "promoted"
    assert "skill" not in promote.add_skill({"return": 0.1, "avg_exposure": 0.5}, float("nan"), 0.5)
    assert "skill" not in promote.add_skill({"return": float("nan"), "avg_exposure": 0.5}, 0.1, 0.5)


def test_a_blank_close_at_the_end_of_the_window_does_not_take_the_basket_with_it(sandbox):
    start_test(sandbox, STEADY)
    p = sandbox / "state" / "candles" / "BTC.csv"
    c = pd.read_csv(p)
    c["close"] = c["close"].astype(object)
    c.loc[c["time"] >= 60 * DAY, "close"] = ""                     # the feed wrote blanks for the last two hours
    c.to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    mc = promote.market_context(0, at(60), ["BTC"])
    assert mc["basket_return"] == pytest.approx(0.0) and math.isfinite(mc["basket_max_dd"])     # never a NaN
    # ... and a pair with no close for the hour that has just ended is behind: no skill is worked out on it
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert mc["gap"] == "the candles for BTC stop before the one that closed at the top of this hour"
    assert chal["skill"] is None


# --- more of the state machine ---------------------------------------------------------------------------

def test_a_start_time_typed_with_a_fraction_does_not_loop_the_first_look(sandbox):
    start_test(sandbox, STEADY)
    slot.save("challenger1", {**slot.load("challenger1"), "started_at": 0.5})
    for hour in range(5):
        promote.main(["--now", str(at(60) + hour * 3600)])
    assert ledger(sandbox).count("### First look H5") == 1 and "### Result H5" not in ledger(sandbox)
    assert promote.first_look_of(slot.load("challenger1")) is not None
    assert "first look passed" in slot.describe_one("challenger1", at(61))
    for odd in ({"first_look": True}, {"first_look": {"start": None}}, {"first_look": {"start": "x"}},
                {"first_look": {"at": 5}, "started_at": None}, {"first_look": [1]}):
        assert promote.first_look_of({"started_at": 0, **odd}) is None           # never a pass, never an error


def test_a_first_look_that_comes_after_day_120_says_the_verdict_is_next(sandbox):
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(121))])
    block = ledger(sandbox)[ledger(sandbox).index("### First look H5"):]
    assert "this look came on day 121.1, at or past day 120, so the verdict on the whole test follows at the next " \
           "run" in block
    assert "more days in the same slot" not in block and "more hours" not in block


def test_a_first_look_just_before_day_120_says_how_long_is_left_and_the_verdict_waits_for_it(sandbox):
    """It used to say "this look came on day 120, past day 120, so the verdict
    follows at the next run", and the next run then said "no verdict yet"."""
    start_test(sandbox, STEADY)
    late = int(119.5 * DAY)
    promote.main(["--now", str(late)])
    block = ledger(sandbox)[ledger(sandbox).index("### First look H5"):]
    assert "Not a promotion: 12 more hours in the same slot, then a verdict on all 120 days" in block
    assert "past day 120" not in block
    promote.main(["--now", str(late + 3600)])
    assert "### Result H5" not in ledger(sandbox)                                 # still inside the 120 days
    promote.main(["--now", str(at(120))])
    assert "### Result H5: promoted" in ledger(sandbox)
    assert promote._days_ahead(120, 60.04) == "60 more days in the same slot, then a verdict on all 120 days"
    assert promote._days_ahead(120, 118.4).startswith("2 more days in the same slot")
    assert promote._days_ahead(120, 119.99).startswith("1 more hour in the same slot")
    assert promote._days_ahead(120, 119.9).startswith("2 more hours in the same slot")


def test_an_old_test_that_is_restarted_begins_again_under_todays_rules(sandbox):
    """Two tests from before ruleset 7 win in the same hour. The weaker one is
    restarted against the new champion, and that fresh test is a ruleset 7 test."""
    start_test(sandbox, STEADY, ruleset=6)
    config.dump_yaml(sandbox / "configs" / "challenger2.yaml",
                     {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox) + "\n## H6: another\n- Expected gross bps per round trip: 90\n"
                                                           "- Status: testing\n")
    slot.save("challenger2", {"status": "testing", "hypothesis": "H6", "started_at": 0, "ruleset": 6,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0}})
    equity(sandbox, "challenger2", STRONG)
    trades(sandbox, "challenger2")
    (sandbox / "state" / "challenger2" / "account.json").write_text(json.dumps({"cash": 1}))
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H6: promoted" in text and "### Result H5: restarted" in text
    meta = slot.load("challenger1")
    assert meta["ruleset"] == 7 and meta["started_at"] == at(60) and promote.two_looks(meta, RULES)
    assert "of 120" in slot.describe_one("challenger1", at(61))


def test_one_slot_whose_config_cannot_be_read_does_not_stop_the_others_following(sandbox):
    old = config.strategy_signature(config.account_cfg("champion"))
    set_rules(sandbox, slots=3)
    for name in ("challenger1", "challenger2", "challenger3"):
        slot.reset(name)
        config.write_challenger_from_champion(name)
    (sandbox / "configs" / "challenger1.yaml").write_text("strategy: [unclosed")
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    assert promote.sync_idle_slots(old) == ["challenger2", "challenger3"]
    assert config.account_cfg("challenger3")["hypothesis"] == "H5"


# --- buying and holding is not a skill ---------------------------------------------------------------------

def held_with_top_ups_and_trims(sandbox, name="challenger1", n=40):
    """Fills of a bot that bought on day one and never left: ten units bought,
    then a small top up and a small trim in turn. Plenty of fills, no exit."""
    rows = [{"ts": DAY, "account": name, "pair": "BTC", "side": "buy", "qty": 10, "price": 100.0, "ref_price": 100.0,
             "notional": 1000.0, "fee": 0, "slippage_cost": 0, "reason": "", "equity_after": 0}]
    for i in range(1, n):
        rows.append({**rows[0], "ts": (i + 1) * DAY, "side": "buy" if i % 2 else "sell", "qty": 1, "notional": 100.0})
    pd.DataFrame(rows).to_csv(sandbox / "state" / name / "trades.csv", index=False)


def rising_and_held(sandbox, ruleset, market=None):
    """A market up 0.3% a day, and a challenger that usually holds half of it
    but sat fully invested from the first day and never changed its mind.
    Against its usual half it shows a fat skill figure."""
    market = market or [0.003] * 120
    moving_market(sandbox, market)
    start_test(sandbox, STEADY, ruleset=ruleset)
    equity_at_day_end(sandbox, "champion", [0.5 * m + c for m, c in zip(market, CHAMP)])
    equity_at_day_end(sandbox, "challenger1", [1.0 * m - 0.00001 for m in market], exposure=1.0)


@pytest.mark.parametrize("ruleset", [6, 7])
def test_a_bot_that_bought_and_held_through_a_rising_market_is_killed_not_promoted(sandbox, ruleset):
    """Fin, 2026-10-05: make sure to kill bots that are just buying and holding.
    It has its 40 fills, small top ups and trims, and it never left a position."""
    rising_and_held(sandbox, ruleset)
    held_with_top_ups_and_trims(sandbox)
    chal = chal_at(60)
    assert chal["trades"] >= 30 and chal["skill"] > 0.08 and chal["round_trips"] == 0      # a "skill" of +9%, no exit
    assert chal["avg_exposure"] == pytest.approx(1.0) and chal["skill_exposure"] == 0.5
    assert promote.decide(*promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[:2],
                          RULES)[0] == "promoted"                                 # the ordinary rule alone would pass it
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "First look H5" not in text
    assert "it has finished no trade of its own: none of its 40 fills closed a position it had bought or had chosen " \
           "to keep, so the +19." in text
    assert "It clears the rule's numbers all the same (challenger skill +9." in text
    assert "a test that has not left a position by its own choice is not promoted on them" in text
    assert ("first look:" in text) == (ruleset == 7)
    assert config.account_cfg("champion")["hypothesis"] == "H0"


def test_a_standing_tilt_is_said_on_the_confidence_line_and_earns_no_fast_pass(sandbox):
    """The same bot with real round trips beside its holding. It is not "just
    holding", so it is not killed, and its numbers pass the first look. But
    its daily skill t of 2.3 is half the market's own daily return, every day,
    for one decision it never went back to. The line says so, and there is no
    promotion on one look."""
    rising_and_held(sandbox, 7, market=[0.013, -0.007] * 60)                     # up 0.3% a day, with noise
    chal = chal_at(60)
    assert chal["skill_t"] > 2.0 and chal["round_trips"] == 20
    tilt = promote.standing_tilt(chal)
    assert tilt.startswith("+9.67% of its +9.60% skill comes from holding 1.00 of the market on average against its "
                           "usual 0.50 while the basket moved +19.33%") and tilt.endswith(": one bet, not one a day")
    assert promote.fast_pass(chal, RULES) is None
    line = promote.confidence_line(chal, RULES)
    assert line.startswith("27% that this is a real edge (every idea starts at 10%; the daily skill t is +2.29 over")
    assert ". Read it with care: +9." in line and line.endswith("one bet, not one a day")
    assert "Read it with care: +" in report.test_section(at(60))                 # in the summary too
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### First look H5: passed" in text and "### Result H5" not in text
    assert "at or above the 2.0 fast pass bar, but +9." in text and "so there is no fast pass on it. Not a promotion: " \
           "60 more days" in text
    assert "- Confidence: 27%" in text and "Read it with care" in text
    # a test without the tilt carries the plain figure, and so does one the figure already reads low for
    good = {"skill_t": 2.5, "skill_days": 60, "skill": 0.05, "basket_return": 0.20, "avg_exposure": 0.55,
            "skill_exposure": 0.50, "skill_basis": "usual", "trades": 40, "round_trips": 9}
    assert promote.standing_tilt(good) is None and "Read it with care" not in promote.confidence_line(good, RULES)
    assert promote.fast_pass(good, RULES) is not None
    assert promote.standing_tilt({**good, "avg_exposure": 0.625}) is not None     # exactly half of the skill is the tilt
    assert promote.standing_tilt({**good, "avg_exposure": 0.62}) is None
    assert "Read it with care" not in promote.confidence_line({**good, "skill_t": -1.0, "avg_exposure": 1.0}, RULES)
    assert "Read it with care" not in promote.confidence_line({**good, "skill_t": None, "avg_exposure": 1.0}, RULES)
    assert promote.standing_tilt({**good, "avg_exposure": 1.0, "skill_basis": "window"}) is None   # no usual to tilt from
    assert promote.standing_tilt({**good, "avg_exposure": 1.0, "skill": -0.01}) is None
    # out of a falling market for the whole window is a tilt too: one bet
    out = promote.standing_tilt({**good, "avg_exposure": 0.0, "basket_return": -0.30, "skill": 0.15})
    assert out.startswith("+15.00% of its +15.00% skill comes from holding 0.00 of the market")
    never = promote.confidence_line({**good, "round_trips": 0}, RULES)
    assert never.endswith("Read it with care: it has finished no trade of its own, so that skill rests on its "
                          "entries alone, a few bets and not one a day")
    assert "Read it with care" not in promote.confidence_line({**good, "round_trips": 0, "trades": 0}, RULES)


def test_riding_the_rise_and_selling_before_the_fall_is_what_the_rule_rewards(sandbox):
    """The skill Fin describes: in for the rise, out before the fall. The
    market ends where it began; the bot kept what the first half gave. Its
    average exposure is its usual one, so none of the skill is a tilt."""
    market = [0.005] * 30 + [-0.005] * 30 + [0.0] * 60
    moving_market(sandbox, market)
    start_test(sandbox, STEADY, ruleset=6)
    equity_at_day_end(sandbox, "champion", [0.5 * m + c for m, c in zip(market, CHAMP)])
    equity_at_day_end(sandbox, "challenger1", [m if k < 30 else 0.0 for k, m in enumerate(market)],
                      exposure=[1.0] * 30 + [0.0] * 90)
    chal = chal_at(60)
    assert abs(chal["avg_exposure"] - 0.5) < 0.02 and chal["skill"] == pytest.approx(0.16, abs=0.01)
    assert promote.standing_tilt(chal) is None
    promote.main(["--now", str(at(60))])
    assert "### Result H5: promoted" in ledger(sandbox) and "Read it with care" not in ledger(sandbox)


def test_average_exposure_counts_the_hours_the_bot_did_not_run(sandbox):
    """Fully invested for five days in which the bot wrote no rows, flat for
    the rest. A plain mean of the rows said it had held nothing; each row now
    stands for the time until the next one."""
    start_test(sandbox, STEADY)
    rows = []
    for h in range(60 * 24 + 1):
        if 20 * 24 < h < 25 * 24:
            continue                                                             # no rows for days 20 to 25
        invested = h == 20 * 24                                                  # the last row before the gap: all in
        rows.append({"ts": h * 3600, "equity": 10_000.0, "cash": 0.0 if invested else 10_000.0,
                     "gross_exposure": 10_000.0 if invested else 0.0, "n_positions": 1, "fees_paid": 0, "slippage_paid": 0})
    pd.DataFrame(rows).to_csv(sandbox / "state" / "challenger1" / "equity.csv", index=False)
    got = promote.window_metrics("challenger1", 0, 60 * DAY, 10000.0)
    assert got["avg_exposure"] == pytest.approx(5 / 60, abs=0.001)                # five days of sixty, not one row of 1,320
    # rows at even hours: the weighted mean is the plain mean
    equity(sandbox, "challenger1", STEADY)
    assert promote.window_metrics("challenger1", 0, at(60), 10000.0)["avg_exposure"] == pytest.approx(0.5)


def test_the_shadow_guard_asks_only_who_did_better_not_the_floor_under_skill():
    champ = {"return": -0.05, "max_drawdown": -0.01, "trades": 40, "skill": -0.03, "skill_exposure": 0.5}
    shad = {"return": -0.02, "max_drawdown": -0.01, "trades": 40, "skill": -0.01, "skill_exposure": 0.5,
            "skill_basis": "usual", "edge_t": None}
    assert promote.decide(champ, shad, RULES, absolute=False)[0] == "promoted"       # the deposed config did better
    verdict, why = promote.decide(champ, shad, RULES)
    assert verdict == "killed" and "but not the +0.00% floor: it did no better than holding the basket at its usual " \
                                   "exposure 0.50" in why
    # when no usual exposure is on record the sentence does not call the window's average "usual"
    why = promote.decide(champ, {**shad, "skill_basis": "window"}, RULES)[1]
    assert "holding the basket at its average exposure in the window 0.50 (no usual exposure is on record)" in why
    # and the guard asks for the fills the rule asks for: a deposed config that did better on 12 fills does not revert
    assert promote.decide(champ, {**shad, "trades": 12}, RULES, absolute=False)[0] == "killed"


def test_the_shadow_guard_waits_for_the_market_data_too(sandbox, capsys):
    """It used to rule on raw return when the candles were missing, and revert."""
    now = 100
    slot.reset("challenger1")
    shadow.start(config.account_cfg("champion"), "H5", now, 10000.0, 10000.0)    # H0 deposed by H5
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox).replace("- Status: testing", "- Status: promoted"))
    later = now + 60 * DAY + 100
    equity(sandbox, "champion", [-0.002, 0.0] * 31)
    equity(sandbox, "shadow", [0.004, -0.001] * 31)
    trades(sandbox, "shadow")
    candles = sandbox / "state" / "candles" / "BTC.csv"
    kept = candles.read_text()
    candles.unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    promote.rule_on_shadow(later, RULES)
    out = capsys.readouterr().out
    assert "WARNING: the guard on H5 is due a ruling on day 60.0 but there are no candles for its window; nothing " \
           "is ruled until the market data is whole" in out
    assert config.account_cfg("champion")["hypothesis"] == "H5" and shadow.load()["status"] == "active"
    assert "### Result H5" not in ledger(sandbox)
    candles.write_text(kept)
    getattr(data, "_READ_CACHE", {}).clear()
    promote.rule_on_shadow(later + 3600, RULES)
    assert config.account_cfg("champion")["hypothesis"] == "H0" and "### Result H5: reverted" in ledger(sandbox)


def test_the_basket_is_read_at_the_last_candle_that_had_closed_not_the_one_still_forming():
    path = pd.Series([1.00, 1.10, 1.21, 1.33], index=[0, 3600, 7200, 10800])      # by candle open; each closes an hour on
    level = promote._basket_level(path, [3600 + 1500, 7200, 7200 + 3599, 10800 + 1500, 14400, 99999, 100])
    assert list(level) == [1.00, 1.10, 1.10, 1.21, 1.33, 1.33, 1.00]              # before any close: the window's start
    times = pd.Series([3600 + 1500, 10800 + 1500], index=[0, 1])
    got = promote._basket_returns(path, 0, times)
    assert list(got.round(6)) == [0.0, 0.21]                                       # 1.00 to 1.00, then 1.00 to 1.21


@pytest.mark.parametrize("fills,stamp", [(12, 7), (40, 7), (40, 6)])
def test_nothing_is_ruled_in_an_hour_when_the_market_data_for_the_window_is_missing(sandbox, capsys, fills, stamp):
    """Without the basket there is no skill figure. The verdict used to fall
    back to raw return in that hour, and a bot that had only held through a
    rise was promoted on it."""
    start_test(sandbox, STRONG, ruleset=stamp)
    trades(sandbox, "challenger1", n=fills)
    candles = sandbox / "state" / "candles" / "BTC.csv"
    kept = candles.read_text()
    candles.unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    for day in (60, 61, 120, 123):
        assert promote.main(["--now", str(at(day))]) == 0
    out = capsys.readouterr().out
    assert "WARNING: challenger1: H5 is due a ruling on day 60.1 but there are no candles for its window; nothing " \
           "is ruled until the market data is whole" in out
    assert "### Result H5" not in ledger(sandbox) and "First look H5" not in ledger(sandbox)
    assert slot.load("challenger1")["status"] == "testing" and config.account_cfg("champion")["hypothesis"] == "H0"
    # the summary does not read the rule on raw return either, and says what it is waiting for
    text = report.test_section(at(61))
    assert "it passes the first look" not in text and "it would pass" not in text
    assert "  no skill figure this hour: there are no candles for its window. Nothing is ruled on a test until the " \
           "market data is whole" in text
    line = slot.describe_one("challenger1", at(61))
    if stamp == 6:
        assert "two look rule (measured, not applied to this test): nothing to read this hour (there are no candles " \
               "for its window); neither rule decides without the market data" in text
        assert "no reading this hour" not in text                    # those words are kept for a damaged record
        assert "one look at day 60 (due: taken at the next hourly run for which the market data and its record " \
               "are whole): promoted, killed, or kept" in line
    else:
        assert "first look at day 60 (due: taken at the next hourly run for which the market data and its record " \
               "are whole) (two look rule)" in line
    # the candles come back: the look that was due is taken, on the day it is taken
    candles.write_text(kept)
    getattr(data, "_READ_CACHE", {}).clear()
    promote.main(["--now", str(at(124))])
    assert "### First look H5" in ledger(sandbox) or "### Result H5" in ledger(sandbox)


def test_the_second_look_waits_for_the_market_data_as_well(sandbox, capsys):
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    candles = sandbox / "state" / "candles" / "BTC.csv"
    kept = candles.read_text()
    candles.unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    capsys.readouterr()
    for day in (120, 121):
        promote.main(["--now", str(at(day))])
    assert "### Result H5" not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    assert capsys.readouterr().out.count("is due a ruling on day 12") == 2
    candles.write_text(kept)
    getattr(data, "_READ_CACHE", {}).clear()
    promote.main(["--now", str(at(122))])
    assert "### Result H5: promoted" in ledger(sandbox)


def three_pairs(sandbox, days=125):
    """The sandbox with three pairs in its rules file, each with flat candles."""
    rules_file = config.load_yaml(sandbox / "configs" / "risk.yaml")
    rules_file["pairs"] = ["BTC", "ETH", "SOL"]
    config.dump_yaml(sandbox / "configs" / "risk.yaml", rules_file)
    flat = pd.read_csv(sandbox / "state" / "candles" / "BTC.csv")
    for pair in ("ETH", "SOL"):
        flat.to_csv(sandbox / "state" / "candles" / f"{pair}.csv", index=False)
    getattr(data, "_READ_CACHE", {}).clear()


def test_candles_missing_for_some_pairs_are_not_a_market_to_rule_on(sandbox, capsys):
    """Three pairs, two of them rising. With the two risers' files gone the
    basket was the one flat pair, a challenger that only held the market read
    +10% of skill, and a kill became a promotion with no warning."""
    three_pairs(sandbox)
    start_test(sandbox, STEADY)
    assert promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[2]["gap"] is None
    for pair in ("ETH", "SOL"):
        (sandbox / "state" / "candles" / f"{pair}.csv").unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert mc["gap"] == "there are no candles in its window for ETH, SOL" and mc["pairs"] == 1
    assert chal["skill"] is None and champ["skill"] is None and chal["skill_t"] is None    # nothing leans on that basket
    promote.main(["--now", str(at(60))])
    assert "### First look H5" not in ledger(sandbox) and "### Result H5" not in ledger(sandbox)
    assert "is due a ruling on day 60.1 but there are no candles in its window for ETH, SOL; nothing is ruled until " \
           "the market data is whole" in capsys.readouterr().out
    assert "no skill figure this hour: there are no candles in its window for ETH, SOL" in report.test_section(at(60))


def test_candles_that_stop_early_are_not_read_as_a_flat_market(sandbox, capsys):
    """One pair's file stops three days before the look. Carried forward flat,
    it read the days after as no move at all."""
    three_pairs(sandbox)
    start_test(sandbox, STEADY)
    p = sandbox / "state" / "candles" / "ETH.csv"
    eth = pd.read_csv(p)
    eth[eth["time"] < 57 * DAY].to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[2]
    assert mc["gap"] == "the candles for ETH stop before the one that closed at the top of this hour"
    promote.main(["--now", str(at(60))])
    assert "### First look H5" not in ledger(sandbox)
    assert "the candles for ETH stop before the one that closed at the top of this hour; nothing is ruled" \
           in capsys.readouterr().out
    # the candle that closed at the top of this hour is what the hourly run has just fetched: with it the pair
    # is current, however far into the hour the run comes; one fetch that failed leaves the pair behind
    eth[eth["time"] + 3600 <= at(60)].to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    for minutes in (0, 27, 59):
        assert promote.paired_slot("challenger1", slot.load("challenger1"), at(60) + 60 * minutes, RULES)[2]["gap"] is None
    assert promote.paired_slot("challenger1", slot.load("challenger1"), at(60) + 3600, RULES)[2]["gap"] is not None
    eth[eth["time"] + 3600 <= at(60) - 3600].to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    assert promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[2]["gap"] is not None


def test_the_early_kill_on_losses_is_measured_since_the_test_began_and_against_the_market(sandbox):
    """Down 21% in eight days. In a flat market that is the strategy's doing and
    it is ended. In a market that fell 30% over the same days it is not."""
    start_test(sandbox, [-0.03] * 8 + [0.0] * 112)
    promote.main(["--now", str(at(10))])
    text = ledger(sandbox)
    assert "### Result H5: killed" in text and "has lost 21.63% since its test began, past the 15% early kill limit, " \
           "and more than the market itself over the same days (the basket made 0.00%)" in text
    # the same account while the market fell further
    start_test(sandbox, [-0.03] * 8 + [0.0] * 112)
    (sandbox / "LEDGER.md").write_text(ledger(sandbox).split("## Results")[0].replace("- Status: killed", "- Status: testing"))
    moving_market(sandbox, [-0.045] * 8 + [0.0] * 112)
    promote.main(["--now", str(at(10))])
    assert "### Result H5" not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    # 16% under its high and still above where it began is not a loss since the test began
    start_test(sandbox, [0.02] * 15 + [-0.02] * 9 + [0.0] * 96)
    moving_market(sandbox, [0.0] * 120)
    chal = chal_at(26)
    assert chal["max_drawdown"] < -0.16 and chal["return"] > 0.10
    promote.main(["--now", str(at(26))])
    assert "### Result H5" not in ledger(sandbox)


def test_the_cost_kill_does_not_wait_for_market_data_and_the_loss_kill_does(sandbox, capsys):
    rules = {**RULES, "treadmill_kill_multiple": 3.0, "treadmill_min_days": 14}
    config.dump_yaml(sandbox / "configs" / "risk.yaml",
                     {"ruleset": 7, "challenger": rules, "pairs": ["BTC"], "initial_cash": 10000, "fee_bps": 10,
                      "slippage_bps": 5, "backtest_gate": {"max_cost_drag": 0.15}})
    start_test(sandbox, [-0.03] * 8 + [0.0] * 112)
    (sandbox / "state" / "candles" / "BTC.csv").unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    promote.main(["--now", str(at(10))])
    out = capsys.readouterr().out
    assert "### Result H5" not in ledger(sandbox)                                # no figure for the market: no loss kill
    assert "WARNING: challenger1: H5 has lost 21.63% since its test began, past the early kill limit, but there are " \
           "no candles for its window, so it cannot be said whether the market lost more; no early kill this hour" in out
    eq = pd.read_csv(sandbox / "state" / "challenger1" / "equity.csv")
    eq["fees_paid"] = 15.0 * np.arange(len(eq))                                  # 15 a day on 10,000 is 55% a year
    eq.to_csv(sandbox / "state" / "challenger1" / "equity.csv", index=False)
    promote.main(["--now", str(at(20))])
    assert "### Result H5: killed" in ledger(sandbox) and "fees treadmill" in ledger(sandbox)


def test_a_yes_or_no_typed_where_a_number_belongs_is_not_read_as_one():
    assert promote._num({"a": True}, "a", 9) == 9 and promote._num({"a": False}, "a", 9) == 9
    assert promote.rule_settings({**RULES, "min_skill_t": True})[0]["min_skill_t"] == 1.0


# --- pinned after the third review -----------------------------------------------------------------------

def test_exactly_thirty_fills_is_enough_and_fills_before_the_window_do_not_count(sandbox):
    start_test(sandbox, STRONG, ruleset=6)
    trades(sandbox, "challenger1", n=30)
    assert promote.too_few_fills(chal_at(60), RULES) is None
    m = promote.window_metrics("challenger1", 20 * DAY, at(60), 10000.0)          # a window that opens on day 20
    assert m["trades"] == 11 and m["round_trips"] == 5                            # only what is inside it
    promote.main(["--now", str(at(60))])
    assert "### Result H5: promoted" in ledger(sandbox)


def test_each_side_is_measured_against_its_own_usual_exposure_and_the_right_one_goes_on_record(sandbox, monkeypatch):
    """The challenger usually holds 80%, the champion 30%. After a promotion the
    record must hold the new champion's 80%, and a test that began under the
    old champion starts its champion side from 30%."""
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: 0.8 if cfg["hypothesis"] == "H5" else 0.3)
    start_test(sandbox, STRONG)
    promote.main(["--now", str(at(60))])                                          # H5 promoted by the fast pass
    change = promote.champion_changes()[-1]
    assert change["to"] == "H5" and change["exposure"] == 0.8
    # another test that had been running since day 10 under H0
    slot.save("challenger2", {"status": "testing", "hypothesis": "H9", "started_at": 10 * DAY, "ruleset": 7,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0},
                              "usual_exposure": {"start": 10 * DAY, "champion": 0.3, "challenger2": 0.6}})
    equity(sandbox, "challenger2", STEADY)
    champ = promote.paired_slot("challenger2", slot.load("challenger2"), at(90), RULES)[0]
    assert champ["exposure_schedule"] == [(10 * DAY, 0.3), (at(60), 0.8)]
    # the guard reverts: the restored config's own usual exposure goes on record, not the undone one's
    later = at(60) + 60 * DAY + 100
    equity(sandbox, "champion", [-0.002, 0.0] * 62)
    eq = pd.read_csv(sandbox / "state" / "champion" / "equity.csv")
    eq.assign(equity=10_000 * (1 + 0.004) ** np.arange(len(eq))).to_csv(sandbox / "state" / "shadow" / "equity.csv",
                                                                         index=False)
    trades(sandbox, "shadow", n=124)
    promote.rule_on_shadow(later, RULES)
    back = promote.champion_changes()[-1]
    assert back["why"] == "revert" and back["to"] == "H0" and back["exposure"] == 0.3


def test_two_winners_in_one_hour_are_ranked_on_skill_not_on_raw_return(sandbox, monkeypatch):
    """H5 made more money by holding more of a rising market; H6 made less
    money and more skill. The rule compares on skill, so H6 is the one promoted."""
    monkeypatch.setattr(promote, "design_exposure",
                        lambda cfg, before_ts, days=365: {"H5": 0.9, "H6": 0.2}.get(cfg["hypothesis"], 0.5))
    market = [0.004, -0.002] * 60                                                 # up 0.1% a day
    moving_market(sandbox, market)
    start_test(sandbox, STEADY, ruleset=6)
    config.dump_yaml(sandbox / "configs" / "challenger2.yaml",
                     {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox) + "\n## H6: another\n- Expected gross bps per round trip: 90\n"
                                                           "- Status: testing\n")
    slot.save("challenger2", {"status": "testing", "hypothesis": "H6", "started_at": 0, "ruleset": 6,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0}})
    equity_at_day_end(sandbox, "champion", [0.5 * m - 0.0005 for m in market])
    equity_at_day_end(sandbox, "challenger1", [0.9 * m + 0.0004 * (1 if k % 2 else 3) for k, m in enumerate(market)],
                      exposure=0.9)                                               # +0.08% a day of its own
    equity_at_day_end(sandbox, "challenger2", [0.2 * m + 0.0005 * (1 if k % 2 else 3) for k, m in enumerate(market)],
                      exposure=0.2)                                               # +0.10% a day of its own
    trades(sandbox, "challenger2")
    (sandbox / "state" / "challenger2" / "account.json").write_text(json.dumps({"cash": 1}))
    a = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[1]
    b = promote.paired_slot("challenger2", slot.load("challenger2"), at(60), RULES)[1]
    assert a["return"] > b["return"] and a["skill"] < b["skill"]
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### Result H6: promoted" in text and "### Result H5: restarted" in text
    assert config.account_cfg("champion")["hypothesis"] == "H6"


def test_the_start_price_is_only_read_between_closes_that_are_close_by():
    def closes(times_h, prices):
        return pd.DataFrame({"time": [int(h * 3600) for h in times_h], "close": prices})
    # an hourly record: the price 30 minutes into the hour is half way between the closes either side
    w = promote._window_closes(closes([0, 1, 2, 3], [100, 110, 120, 130]), int(2.5 * 3600), 4 * 3600)
    assert list(w.round(6)) == [115.0, 120.0, 130.0] and int(w.index[0]) == int(2.5 * 3600) - 3600
    # a hole of five hours around the start: no reading across it; the window starts at the first price inside
    w = promote._window_closes(closes([0, 6, 7], [100, 200, 210]), 4 * 3600, 8 * 3600)
    assert list(w) == [200.0, 210.0]
    # the last close before the start is under two hours old, and nothing follows it at once: it stands as the start
    w = promote._window_closes(closes([0, 1, 5, 6], [100, 110, 150, 160]), int(2.5 * 3600), 7 * 3600)
    assert list(w) == [110.0, 150.0, 160.0]
    # duplicates and rows out of order do not matter; one usable price is not a window
    w = promote._window_closes(closes([2, 0, 1, 1], [120, 100, 110, 110]), 3600, 3 * 3600)
    assert list(w)[0] == 100.0 and list(w)[-1] == 120.0
    assert promote._window_closes(closes([0], [100]), 0, 3600) is None
    assert promote._window_closes(closes([0, 1], [100, 110]), 5 * 3600, 4 * 3600) is None      # ends before it starts


# --- pinned after the fourth review -----------------------------------------------------------------------

def test_a_blank_equity_cell_in_the_hour_of_a_promotion_does_not_disarm_the_shadow_guard(sandbox):
    """The newest cell was taken as it was. Blank, it went into the guard's
    start equity as NaN, and sixty days on the guard could not tell a deposed
    config that was up 61% from one that was down."""
    start_test(sandbox, STRONG)
    for name in ("champion", "challenger1"):
        p = sandbox / "state" / name / "equity.csv"
        eq = pd.read_csv(p)
        eq["equity"] = eq["equity"].astype(object)
        eq.loc[eq["ts"] == 60 * DAY + 3600, "equity"] = ""                       # the row of the promotion hour
        eq.to_csv(p, index=False)
    now = at(60)
    got = promote.current_equities(now)
    assert all(math.isfinite(v) for v in got.values()) and set(got) >= {"champion", "challenger1"}
    # a blank row is damage, so with the account's own file there nothing is ruled at all
    promote.main(["--now", str(now)])
    assert "### " not in ledger(sandbox)
    # and without it (nothing to set the record against) the promotion still starts the guard from real figures
    (sandbox / "state" / "challenger1" / "account.json").unlink()
    promote.main(["--now", str(now)])
    assert "### Result H5: promoted" in ledger(sandbox)
    started = shadow.load()["start_equity"]
    assert started and all(isinstance(v, float) and math.isfinite(v) for v in started.values())


def test_a_start_equity_that_is_not_a_number_is_no_start_equity(sandbox, capsys):
    """Left in a slot's record it made every return NaN, and the test then
    waited for ever with a line in the log blaming the market data."""
    start_test(sandbox, STEADY)
    meta = slot.load("challenger1")
    meta["start_equity"] = {"champion": float("nan"), "challenger1": "ten thousand"}
    slot.save("challenger1", meta)
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert math.isfinite(champ["return"]) and math.isfinite(chal["return"]) and mc["gap"] is None
    assert chal["skill"] is not None
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    assert "market data" not in capsys.readouterr().out
    assert promote.window_metrics("challenger1", 0, at(60), -5.0)["return"] == pytest.approx(chal["return"], abs=0.01)


def test_a_record_that_cannot_be_read_stops_only_its_own_slot(sandbox, capsys):
    """A zero byte trades file in one slot. The other slot's look is still
    taken, the summary is still written, and the hour's commit still happens.
    Nothing is ruled for the slot whose record cannot be read: a damaged file
    is not a strategy with nothing to show."""
    start_test(sandbox, STEADY)
    config.dump_yaml(sandbox / "configs" / "challenger2.yaml",
                     {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox) + "\n## H6: another\n- Expected gross bps per round trip: 90\n"
                                                           "- Status: testing\n")
    slot.save("challenger2", {"status": "testing", "hypothesis": "H6", "started_at": 0, "ruleset": 7,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0}})
    equity(sandbox, "challenger2", STEADY)
    trades(sandbox, "challenger2")
    (sandbox / "state" / "challenger2" / "account.json").write_text(json.dumps({"cash": 1}))
    (sandbox / "state" / "challenger1" / "trades.csv").write_text("")              # cut to nothing
    assert promote.main(["--now", str(at(60))]) == 0
    out = capsys.readouterr().out
    assert "WARNING: challenger1: H5 could not be looked at this hour (Unreadable: challenger1/trades.csv cannot be " \
           "read" in out and "nothing is ruled for it until its record can be read" in out
    text = ledger(sandbox)
    assert "### First look H6: passed" in text and "H5:" not in text.split("## Results")[1]
    assert slot.load("challenger1")["status"] == "testing"
    summary = report.test_section(at(60))
    assert "its record could not be read this hour (Unreadable: challenger1/trades.csv" in summary
    assert "challenger2: testing H6" in summary and "confidence: " in summary
    # an equity file cut to nothing, the same; a file that is simply not there is no data
    equity_file = sandbox / "state" / "challenger1" / "equity.csv"
    kept = equity_file.read_text()
    trades(sandbox, "challenger1")
    equity_file.write_text("")
    assert promote.main(["--now", str(at(61))]) == 0 and "H5:" not in ledger(sandbox).split("## Results")[1]
    assert "challenger1" not in promote.current_equities(at(61))                   # and no figure is made up for it
    equity_file.write_text(kept)


def test_rows_under_the_wrong_header_are_a_damaged_file_and_not_an_account_with_nothing_to_show(sandbox, capsys):
    """A file whose first line has gone still parses: its rows sit under the
    wrong names. Read as "no fills" that was a kill for a test that had made
    forty, and read as "no equity" a kill for one with a full record."""
    start_test(sandbox, STEADY)
    equity_file, trades_file = (sandbox / "state" / "challenger1" / f for f in ("equity.csv", "trades.csv"))
    kept_equity, kept_trades = equity_file.read_text(), trades_file.read_text()
    for broken, lacking in (("ts\n5\n", "equity"), ("a,b\n1,2\n", "ts or equity"), (kept_equity.split("\n", 1)[1], "ts or equity")):
        equity_file.write_text(broken)
        with pytest.raises(promote.Unreadable, match=f"challenger1/equity.csv has rows and no {lacking} column"):
            promote.window_metrics("challenger1", 0, at(60), 10000.0)
    equity_file.write_text(kept_equity)
    for broken, lacking in (("ts,pair\n5,BTC\n", "side or qty"), (kept_trades.split("\n", 1)[1], "ts or side or pair or qty")):
        trades_file.write_text(broken)
        with pytest.raises(promote.Unreadable, match=f"challenger1/trades.csv has rows and no {lacking} column"):
            promote.window_metrics("challenger1", 0, at(60), 10000.0)
    # at the look: nothing is ruled, it is said, and the summary is still written
    assert promote.main(["--now", str(at(60))]) == 0
    assert "WARNING: challenger1: H5 could not be looked at this hour (Unreadable: challenger1/trades.csv has rows and " \
           "no ts or side or pair or qty column)" in capsys.readouterr().out
    assert "### " not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    assert "its record could not be read this hour (Unreadable: challenger1/trades.csv" in report.test_section(at(60))
    # a header with no rows under it is an account that has not traded, and a file that is not there the same
    trades_file.write_text(kept_trades.split("\n", 1)[0] + "\n")
    assert promote.window_metrics("challenger1", 0, at(60), 10000.0)["trades"] == 0
    trades_file.unlink()
    assert promote.window_metrics("challenger1", 0, at(60), 10000.0)["trades"] == 0


def test_no_look_is_taken_on_an_account_with_no_equity_reading_in_its_window(sandbox, capsys):
    """Every account is written every hour, so a window with no reading in it
    is a damaged record. It used to be ruled on as "no equity data for the
    window": a kill, for the file's fault and not the strategy's."""
    start_test(sandbox, STEADY)
    for who in ("challenger1", "champion"):
        equity_file = sandbox / "state" / who / "equity.csv"
        kept = equity_file.read_text()
        rows = kept.split("\n")
        for broken in (rows[0] + "\n",                                               # the header and no rows
                       "\n".join(rows[:1] + [r for r in rows[1:] if r and int(r.split(",")[0]) > at(60)]) + "\n"):
            equity_file.write_text(broken)                                            # (or none inside the window)
            assert promote.main(["--now", str(at(60))]) == 0
            assert (f"WARNING: challenger1: H5 is due a ruling on day 60.1 but there is no usable equity record for {who} "
                    f"in its window; nothing is ruled until that record is whole") in capsys.readouterr().out
            assert "### " not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
            text = report.test_section(at(60))
            assert f"  no reading this hour: there is no usable equity record for {who} in its window. Nothing is ruled " \
                   f"on a test until that record is whole" in text
            assert "it would be killed" not in text and "would also have ended it" not in text
        # text where the numbers belong is damage of the plainer kind: the record cannot be read
        equity_file.write_text(rows[0] + "\n" + "soon,lots,,,,,\n")
        assert promote.main(["--now", str(at(60))]) == 0
        said = capsys.readouterr().out
        if who == "challenger1":                                                      # (the sandbox gives it an account file)
            assert "could not be looked at this hour (Unreadable: challenger1/equity.csv has 1 row that is not a " \
                   "reading (a time, an equity, an exposure and costs, each a number))" in said
        else:
            assert "is due a ruling on day 60.1 but there is no usable equity record for champion" in said
        assert "### " not in ledger(sandbox)
        equity_file.write_text(kept)
    # before a look is due it is not said every hour by the verdict code; the summary still shows it
    equity_file = sandbox / "state" / "challenger1" / "equity.csv"
    kept = equity_file.read_text()
    equity_file.write_text(kept.split("\n", 1)[0] + "\n")
    assert promote.main(["--now", str(at(30))]) == 0 and "WARNING" not in capsys.readouterr().out
    assert "no reading this hour: there is no usable equity record for challenger1" in report.test_section(at(30))
    assert "trades: there is no usable equity record in its window to set them against" in report.test_section(at(30))
    # mended: the look is taken
    equity_file.write_text(kept)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)


def test_the_shadow_guard_waits_for_an_equity_record_too(sandbox, capsys):
    """With no reading for the deposed config the guard read "no equity data",
    which ended it as held: a promotion confirmed by a missing file."""
    now = 100
    slot.reset("challenger1")
    shadow.start(config.account_cfg("champion"), "H5", now, 10000.0, 10000.0)    # H0 deposed by H5
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox).replace("- Status: testing", "- Status: promoted"))
    later = now + 60 * DAY + 100
    equity(sandbox, "champion", [-0.002, 0.0] * 31)
    equity(sandbox, "shadow", [0.004, -0.001] * 31)
    trades(sandbox, "shadow")
    equity_file = sandbox / "state" / "shadow" / "equity.csv"
    kept = equity_file.read_text()
    equity_file.write_text(kept.split("\n", 1)[0] + "\n")
    promote.rule_on_shadow(later, RULES)
    assert "WARNING: the guard on H5 is due a ruling on day 60.0 but there is no usable equity record for shadow in its " \
           "window; nothing is ruled until that record is whole" in capsys.readouterr().out
    assert shadow.load()["status"] == "active" and "### Result H5" not in ledger(sandbox)
    equity_file.write_text(kept)
    promote.rule_on_shadow(later + 3600, RULES)
    assert config.account_cfg("champion")["hypothesis"] == "H0" and "### Result H5: reverted" in ledger(sandbox)


def test_one_account_whose_files_cannot_be_read_does_not_stop_the_summary(sandbox):
    """bot.report read every account's files with nothing around it, so the
    file that the verdict code had stepped round stopped the summary instead,
    and with it the commit of the hour."""
    start_test(sandbox, STEADY)
    first, last = (int(pd.read_csv(sandbox / "state" / "challenger1" / "equity.csv")["ts"].iloc[i]) for i in (0, -1))
    (sandbox / "state" / "challenger1" / "account.json").write_text(json.dumps(
        {"cash": 1, "initial_cash": 10000.0, "created_at": first, "fees_paid": 0.0, "slippage_paid": 0.0,
         "n_trades": 40, "positions": {}, "last_run_ts": last, "halted_day": None}))
    whole = report.build(at(60))
    assert "## challenger1: " in whole and "could not be read" not in whole
    (sandbox / "state" / "challenger1" / "trades.csv").write_text("")
    text = report.build(at(60))
    assert "## challenger1\n\nits record could not be read this hour (EmptyDataError" in text
    assert "## Challenger slots" in text and "## champion: " in text and "## Data" in text
    assert "its record could not be read this hour (Unreadable: challenger1/trades.csv" in text    # the slot's lines too


def test_any_error_in_one_slots_look_leaves_the_others_ruled(sandbox, monkeypatch, capsys):
    start_test(sandbox, STRONG)
    config.dump_yaml(sandbox / "configs" / "challenger2.yaml",
                     {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox) + "\n## H6: another\n- Expected gross bps per round trip: 90\n"
                                                           "- Status: testing\n")
    slot.save("challenger2", {"status": "testing", "hypothesis": "H6", "started_at": "soon", "ruleset": 7,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0}})    # a start that is not a time
    assert promote.main(["--now", str(at(60))]) == 0
    assert "WARNING: challenger2: H6 could not be looked at this hour (ValueError" in capsys.readouterr().out
    assert "### Result H5: promoted" in ledger(sandbox)
    assert "challenger2: its record could not be read this hour" in report.test_section(at(60) + 3600)


def test_a_t_bar_of_zero_means_no_t_bar():
    good = {"return": 0.05, "max_drawdown": -0.01, "trades": 40, "round_trips": 20, "skill": 0.05, "trade_profit": 0.02,
            "trade_wins": 20, "avg_exposure": 0.5, "skill_exposure": 0.5, "skill_basis": "usual", "skill_days": 120,
            "edge_t": None}
    champ = {"return": 0.0, "max_drawdown": -0.01, "trades": 40, "skill": 0.0, "skill_exposure": 0.5}
    none = {**RULES, "min_skill_t": 0}
    for t in (-0.30, 0.0, None, float("nan")):
        verdict, why = promote.decide_final(champ, {**good, "skill_t": t}, none)
        assert verdict == "promoted" and why.endswith("no t bar is set")
    verdict, why = promote.decide_final(champ, {**good, "skill_t": -0.30}, RULES)
    assert verdict == "unproven" and "the daily skill t is -0.30 over 120 days, under the 1.00 the rule asks for: its " \
                                     "skill is above zero in total and too thin day by day to tell from luck" in why
    assert "positive and too thin" not in why                                    # a t of -0.30 is not positive


def test_a_figure_beside_its_bar_is_printed_so_the_two_can_be_told_apart():
    assert promote._against(0.996, 1.0, percent=False) == ("+0.996", "1.000")
    assert promote._against(0.96, 1.0, percent=False) == ("+0.96", "1.00")
    assert promote._against(1.0, 1.0, percent=False) == ("+1.00", "1.00")
    assert promote._against(0.00996, 0.01) == ("+0.996%", "1.000%")
    assert promote._against(-0.014, 0.0) == ("-1.40%", "0.00%")
    good = {"return": 0.05, "max_drawdown": -0.01, "trades": 40, "round_trips": 20, "skill": 0.05, "trade_profit": 0.02,
            "trade_wins": 20, "avg_exposure": 0.5, "skill_exposure": 0.5, "skill_basis": "usual", "skill_days": 120,
            "edge_t": None, "skill_t": 0.996}
    champ = {"return": 0.0, "max_drawdown": -0.01, "trades": 40, "skill": 0.0, "skill_exposure": 0.5}
    why = promote.decide_final(champ, good, RULES)[1]
    assert "the daily skill t is +0.996 over 120 days, under the 1.000 the rule asks for" in why
    assert promote.confidence_text({"skill_t": 0.96, "skill_days": 120}, RULES).endswith("the daily skill t is +0.96 over 120 days)")
    assert "daily skill t +0.96 over 120 days" in promote._fmt({**good, "skill_t": 0.96, "fees": 1.0, "gross_pnl": 1.0,
                                                               "realised_bps": None})
    assert promote._n(1, "fill") == "1 fill" and promote._n(0, "fill") == "0 fills" and promote._n(2, "finished trade") == "2 finished trades"
    assert "1 fill (1 finished trade)" in promote._fmt({**good, "trades": 1, "round_trips": 1, "fees": 1.0,
                                                        "gross_pnl": 1.0, "realised_bps": None})


def test_the_slot_line_counts_the_days_to_the_verdict_it_names(sandbox):
    start_test(sandbox, STEADY)
    assert "day 30.1 of 120, 89.9 days until the verdict, first look at day 60 (two look rule)" in \
        slot.describe_one("challenger1", at(30))
    start_test(sandbox, STEADY, ruleset=6)
    assert "day 30.1 of 60, 29.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days " \
           "if its trades are of value and it does not pass)" in slot.describe_one("challenger1", at(30))


def test_fills_at_the_very_start_of_a_test_and_the_one_day_line(sandbox):
    """Every live test's first fills carry its start time. And a position the
    slot was handed is the strategy's own to leave from 24 hours on, to the second."""
    start_test(sandbox, STRONG)
    begin = 10 * DAY

    def left(rows, name="challenger1"):
        pd.DataFrame([{"ts": int(t), "account": name, "pair": p, "side": sd, "qty": q, "price": 100.0,
                       "ref_price": 100.0, "notional": 100.0 * q, "fee": 0, "slippage_cost": 0, "reason": "",
                       "equity_after": 0} for t, p, sd, q in rows]).to_csv(sandbox / "state" / name / "trades.csv", index=False)
        return promote.window_metrics(name, begin, at(60), 10000.0)["round_trips"]

    assert left([(begin, "BTC", "buy", 1.0), (begin + 6 * 3600, "BTC", "sell", 1.0)]) == 1     # bought in its first hour: its own
    assert left([(begin - DAY, "BTC", "buy", 1.0), (begin, "BTC", "sell", 1.0)]) == 0          # the slot's book, sold at once
    assert left([(begin - DAY, "BTC", "buy", 1.0), (begin + 86399, "BTC", "sell", 1.0)]) == 0
    assert left([(begin - DAY, "BTC", "buy", 1.0), (begin + 86400, "BTC", "sell", 1.0)]) == 1
    # rows out of time order, a negative quantity, and exactly a twentieth left
    assert left([(begin + 7200, "BTC", "sell", 1.0), (begin + 3600, "BTC", "buy", 1.0)]) == 1
    assert left([(begin + 3600, "BTC", "buy", 1.0), (begin + 7200, "BTC", "sell", -1.0)]) == 0
    assert left([(begin + 3600, "BTC", "buy", 1.0), (begin + 7200, "BTC", "sell", -1.0),      # the row is left out:
                 (begin + 9000, "BTC", "sell", 1.0)]) == 1                                    # it does not add to the book
    assert left([(begin + 3600, "BTC", "buy", 1.0), (begin + 7200, "BTC", "sell", 0.95)]) == 1
    assert left([(begin + 3600, "BTC", "buy", 1.0), (begin + 7200, "BTC", "sell", 0.94)]) == 0
    # The champion's account is one long record and nothing is handed to it at a window's start, so a
    # position it leaves in a window's first day is its own (its count used to come out one short)
    rows = [(begin - DAY, "BTC", "buy", 1.0), (begin + 3600, "BTC", "sell", 1.0)]
    assert left(rows) == 0 and left(rows, name="champion") == 1
