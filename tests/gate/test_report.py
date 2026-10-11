"""PROTECTED. The summary says whether the hourly loop itself ran, and where the fill cap stopped a buy."""
import csv

import pytest

from bot import config, data, paper, report, slot, strategy
from bot.run import DECISION_FIELDS, REPLAYED, run_account

HOUR = 3600
T0 = 1_790_000_000 // HOUR * HOUR


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "ROOT", tmp_path)
    monkeypatch.setattr(config, "CONFIGS", tmp_path / "configs")
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    (tmp_path / "state" / "champion").mkdir(parents=True)
    return tmp_path


def record(root, hours, replayed=()):
    """One equity row per listed hour (hours after T0, at seven minutes past), replayed ones on the hour."""
    adir = root / "state" / "champion"
    rows = [{"ts": T0 + h * HOUR + (0 if h in replayed else 420), "equity": 10_000, "cash": 10_000,
             "gross_exposure": 0, "n_positions": 0, "fees_paid": 0, "slippage_paid": 0} for h in hours]
    with open(adir / "equity.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=paper.EQUITY_FIELDS)
        w.writeheader()
        w.writerows(rows)
    paper.append_rows(adir / "decisions.csv", DECISION_FIELDS, [
        {"ts": r["ts"], "account": "champion", "pair": "BTC", "price": 1, "signal_weight": 0, "target_weight": 0,
         "current_weight": 0, "action": "hold", "half_spread_bps": 1,
         "reason": (REPLAYED if h in replayed else "") + "flat"} for h, r in zip(hours, rows)])


def test_every_hour_on_record_reads_clean(sandbox):
    record(sandbox, range(0, 400))
    text = report.runs_section(T0 + 399 * HOUR + 500)
    assert "hours on record: 24 of the last 24, 168 of the last 168" in text
    assert "no hour in the last 7 days is without a decision" in text and "replayed" not in text.split("\n")[2]


def test_dropped_runs_show_even_though_no_candle_is_missing(sandbox):
    """The scheduler drops seven hours. The candle files would be complete; this section is the only place it shows."""
    hours = [h for h in range(0, 400) if not 380 <= h < 387]
    record(sandbox, hours)
    text = report.runs_section(T0 + 399 * HOUR + 500)
    assert "hours on record: 17 of the last 24, 161 of the last 168" in text
    assert "7 hours in the last 7 days have no decision at all" in text
    assert "longest gap 8.0 hours" in text


def test_replayed_hours_count_as_on_record_and_are_named(sandbox):
    record(sandbox, range(0, 400), replayed={390, 391, 392})
    text = report.runs_section(T0 + 399 * HOUR + 500)
    assert "24 of the last 24, 168 of the last 168 (3 of them replayed after a missed run)" in text
    assert "no hour in the last 7 days is without a decision" in text


def test_a_young_account_is_not_charged_for_hours_before_it_existed(sandbox):
    record(sandbox, range(0, 10))
    text = report.runs_section(T0 + 9 * HOUR + 500)
    assert "hours on record: 10 of the last 10, 10 of the last 10" in text
    assert "no hour in the last 7 days is without a decision" in text


def test_no_runs_yet_says_so(sandbox):
    assert "no hourly run on record yet" in report.runs_section(T0)


# --- the fill cap: what the summary says of it ---------------------------------------------------

RISK = {"fee_bps": 10, "slippage_bps": 5, "impact_bps": 2, "initial_cash": 10_000, "pairs": ["BTC", "ETH"],
        "history_hours": 720, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0, "min_trade_notional": 50,
        "rebalance_threshold": 0.05, "daily_loss_halt": 0.05, "max_fills_per_pair_per_day": 4,
        "challenger": {"slots": 2}}
FLIP = {"hypothesis": "HF", "strategy": "flip", "params": {"x_hours": 24}}
MIDNIGHT = T0 // 86400 * 86400 + 86400          # 2026-09-22 00:00 UTC, the first midnight after T0
NOW = MIDNIGHT + 30 * HOUR                      # 06:00 the day after, so the section reads from 2026-09-16
CAP4 = "(the cap is 4 fills in one pair in one UTC day)"
NOTES = ("- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go "
         "through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later "
         "is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is "
         "left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before "
         "a promotion, a revert or a retirement are the config it had then\n"
         "- how to read a line: that many fills in one coin in one day is in and out more than once, or one position "
         "built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy "
         "resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry "
         "from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry "
         "condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back "
         "within an hour or two of selling, the entry naming the same signal as the one before, often lower than it "
         "just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the "
         "old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and "
         "trades.csv show which. Every one of those fills paid costs\n")


def quiet(since="2026-09-16"):
    return (f"## Fill cap\n\n- since {since} (today and the 7 UTC days before it): no buy stopped by the cap and no "
            f"pair that filled 4 times or more in one UTC day, in any account read {CAP4}\n")


def stopped(pair, n=4, cap=4, said="enter"):
    """The reason the engine writes on a buy the cap stopped (pinned to the engine's own in test_replay.py)."""
    return (f"capped: {n} fills in {pair} today, the limit is {cap} a day, so no new buys until the next UTC day "
            f"(sells are never capped) | {said}")


@pytest.fixture
def book(sandbox, monkeypatch):
    """The sandbox with settings in it: a cap of four fills a day, two slots, and a champion that flips."""
    for name in ("CANDLES", "HISTORY", "ARCHIVE"):
        monkeypatch.setattr(config, name, sandbox / "state" / name.lower())
    monkeypatch.setattr(config, "LEDGER", sandbox / "LEDGER.md")
    (sandbox / "configs").mkdir()
    config.dump_yaml(sandbox / "configs" / "risk.yaml", RISK)
    for name in ("champion", "challenger1", "challenger2"):
        config.dump_yaml(sandbox / "configs" / f"{name}.yaml", FLIP)
    monkeypatch.setitem(strategy.STRATEGIES, "flip", lambda c, params, w: {
        "BTC": strategy.Target(0.0, "exit") if w.get("BTC", 0) > 0 else strategy.Target(0.2, "enter")})
    monkeypatch.setitem(strategy.STRATEGIES, "buyer", lambda c, params, w: {"BTC": strategy.Target(0.2, "enter")})
    return sandbox


def fills(root, name, *rows):
    """Rows for an account's trades.csv: (seconds after MIDNIGHT, pair, side)."""
    paper.append_rows(root / "state" / name / "trades.csv", paper.TRADE_FIELDS, [
        {"ts": MIDNIGHT + t, "account": name, "pair": pair, "side": side, "qty": 1, "price": 100, "ref_price": 100,
         "notional": 100, "fee": 0.1, "slippage_cost": 0.05, "reason": "x", "equity_after": 10_000,
         "half_spread_bps": 1, "slip_bps": 5} for t, pair, side in rows])


def decided(root, name, *rows):
    """Rows for an account's decisions.csv: (seconds after MIDNIGHT, pair, action, reason), each from flat, or with
    the weight held at the time as a fifth item."""
    paper.append_rows(root / "state" / name / "decisions.csv", DECISION_FIELDS, [
        {"ts": MIDNIGHT + row[0], "account": name, "pair": row[1], "price": 100, "signal_weight": 0.25,
         "target_weight": 0.25, "current_weight": row[4] if len(row) > 4 else 0, "action": row[2], "reason": row[3],
         "half_spread_bps": 1} for row in rows])


def in_and_out(root, name, pair, day=0, n=4, first=HOUR):
    """n fills in one pair on one UTC day, a buy and then a sell and so on, an hour apart from `first`."""
    fills(root, name, *[(day * 86400 + first + i * HOUR, pair, "sell" if i % 2 else "buy") for i in range(n)])


def under_test(root, name, started, hypothesis="H9"):
    slot.save(name, {"status": "testing", "hypothesis": hypothesis, "started_at": MIDNIGHT + started,
                     "start_equity": {}, "ruleset": 7})


def hourly(names, frames, at):
    """One hourly run of these accounts as bot/run.py makes it, slots started or ended after it."""
    prices = {p: float(df["close"].iloc[-1]) for p, df in frames.items()}
    equities = {name: run_account(name, frames, prices, at, RISK) for name in names}
    slot.maybe_start(at, equities)


def made_up(n=320):
    """Hourly candles for BTC and ETH whose 300th closes at MIDNIGHT."""
    full = {p: data.SyntheticSource(["BTC", "ETH"], n=n, seed=5, start=MIDNIGHT - 300 * HOUR).ohlc(p)
            for p in ("BTC", "ETH")}
    return lambda k: {p: df.iloc[:k].reset_index(drop=True) for p, df in full.items()}


def test_a_buy_the_cap_stopped_is_in_the_summary_with_its_pair_its_day_and_its_hours(book):
    """Through the engine itself, so that what it writes is what the summary finds: a strategy that goes in and
    out of BTC every hour from midnight fills four times, and its buy is stopped in the next four hours."""
    upto = made_up()
    for h in range(8):
        hourly(["champion"], upto(300 + h), MIDNIGHT + h * HOUR + 600)
    assert report.fill_cap_section(NOW) == (
        "## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before it): the cap stopped a buy in 4 hours, on "
        f"1 pair day; a pair filled 4 times or more in one UTC day on 1 pair day {CAP4}\n"
        "- champion, BTC, 2026-09-22: 4 fills (buy 00:10, sell 01:10, buy 02:10, sell 03:10); a buy stopped by the cap "
        "in 4 hours (04:10, 05:10, 06:10, 07:10), each an entry from flat\n" + NOTES)
    whole = report.build(NOW)
    assert whole.index("## Runs") < whole.index("## Fill cap") < whole.index("## Challenger slots")
    assert report.fill_cap_section(NOW) in whole


def test_a_buy_stopped_in_an_hour_that_was_replayed_is_counted_like_any_other(book):
    """The run drops seven hours and replays them. Those rows begin "replayed after a missed run", and the fills
    and the stopped buys among them are the account's all the same."""
    upto = made_up()
    hourly(["champion"], upto(300), MIDNIGHT + 600)
    hourly(["champion"], upto(308), MIDNIGHT + 8 * HOUR + 600)
    text = report.fill_cap_section(NOW)
    assert "): the cap stopped a buy in 5 hours, on 1 pair day; " in text
    assert ("- champion, BTC, 2026-09-22: 4 fills (buy 00:10, sell 01:00, buy 02:00, sell 03:00); a buy stopped by "
            "the cap in 5 hours (04:00, 05:00, 06:00, 07:00, 08:10), each an entry from flat\n") in text


def test_a_test_whose_first_buy_the_cap_stopped_shows_it_and_says_why_with_fewer_fills(book):
    """Through the engine and the slots: a slot runs the champion's config, fills BTC four times by 03:10, and is
    handed a new strategy at 05:10 that wants BTC. The cap counts the account's day, so the new test's very first
    buy is stopped, in the hour the test begins, and the line says why it shows no fill of the test's own."""
    upto = made_up()
    for h in range(5):
        hourly(["champion", "challenger1", "challenger2"], upto(300 + h), MIDNIGHT + h * HOUR + 600)
    config.dump_yaml(book / "configs" / "challenger1.yaml", {"hypothesis": "H9", "strategy": "buyer", "params": {}})
    hourly(["champion", "challenger1", "challenger2"], upto(305), MIDNIGHT + 5 * HOUR + 600)
    assert slot.load("challenger1")["started_at"] == MIDNIGHT + 5 * HOUR + 600
    text = report.fill_cap_section(NOW)
    assert ("- challenger1, BTC, 2026-09-22: no fill; a buy stopped by the cap in 1 hour (05:10), a new strategy's first "
            "buy, stopped by the old config's fills that day\n") in text
    assert "challenger2" not in text and "- champion, BTC, 2026-09-22: 4 fills" in text


def test_with_nothing_at_the_cap_the_section_is_one_line_that_says_so(book):
    in_and_out(book, "champion", "BTC", n=3)                    # three fills is under the cap
    decided(book, "champion", (HOUR, "BTC", "buy", "enter"), (2 * HOUR, "BTC", "hold", "hold: nothing to do | enter"))
    assert report.fill_cap_section(NOW) == quiet()


def test_no_account_with_a_record_yet_reads_as_quiet(book):
    assert report.fill_cap_section(NOW) == quiet()


def test_a_strategy_s_own_use_of_the_word_is_not_a_stopped_buy(book):
    """A reason is free text, and the engine puts its own words first only on a decision it did not fill. A
    strategy that says "capped:" for a reason of its own, on a buy that filled or a weight it holds, has had
    nothing stopped."""
    decided(book, "champion",
            (HOUR, "BTC", "buy", "capped: at my own limit of 0.2"),
            (2 * HOUR, "BTC", "hold", "capped: at my own limit of 0.2"),
            (3 * HOUR, "ETH", "none", "waits for cash: the book is fully invested | capped: at my own limit"),
            (4 * HOUR, "ETH", "hold", "hold: weight change +0.010 below threshold 0.05 | " + stopped("ETH")))
    assert report.fill_cap_section(NOW) == quiet()
    decided(book, "champion", (5 * HOUR, "ETH", "none", stopped("ETH")))
    assert report.fill_cap_section(NOW) == (
        "## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before it): the cap stopped a buy in 1 hour, on 1 "
        f"pair day; no pair filled 4 times or more in one UTC day {CAP4}\n"
        "- champion, ETH, 2026-09-22: no fill; a buy stopped by the cap in 1 hour (05:00), an entry from flat\n" + NOTES)


def test_each_line_says_whether_the_stopped_buys_were_entries_from_flat_or_top_ups(book):
    """The weight held when the buy was stopped tells a top up of a position the strategy keeps from an entry,
    which only a whipsaw or a loop can be."""
    decided(book, "champion", (5 * HOUR, "ETH", "none", stopped("ETH"), 0.0),
            (6 * HOUR, "ETH", "none", stopped("ETH"), 0.1312), (7 * HOUR, "ETH", "none", stopped("ETH"), 0.0),
            (5 * HOUR, "BTC", "none", stopped("BTC"), 0.25), (8 * HOUR, "DOT", "none", stopped("DOT"), ""),
            (9 * HOUR, "DOT", "none", stopped("DOT"), 0))
    text = report.fill_cap_section(NOW)
    assert "- champion, ETH, 2026-09-22: no fill; a buy stopped by the cap in 3 hours (05:00, 06:00, 07:00), 2 entries " \
           "from flat, 1 top up of a position it held\n" in text
    assert "- champion, BTC, 2026-09-22: no fill; a buy stopped by the cap in 1 hour (05:00), a top up of a position " \
           "it held\n" in text
    assert "- champion, DOT, 2026-09-22: no fill; a buy stopped by the cap in 2 hours (08:00, 09:00), 1 entry from " \
           "flat, 1 with no weight on record\n" in text
    decided(book, "champion", (10 * HOUR, "LTC", "none", stopped("LTC"), ""), (11 * HOUR, "LTC", "none", stopped("LTC"), ""),
            (12 * HOUR, "ADA", "none", stopped("ADA"), ""), (13 * HOUR, "SOL", "none", stopped("SOL"), 0.2),
            (14 * HOUR, "SOL", "none", stopped("SOL"), 0.1))
    text = report.fill_cap_section(NOW)
    assert "(10:00, 11:00), none with a weight on record\n" in text and "(12:00), with no weight on record\n" in text
    assert "(13:00, 14:00), each a top up of a position it held\n" in text


def test_a_new_strategy_s_first_buy_is_said_to_be_one_whatever_was_held(book):
    """A test's first hour, and the champion's after a promotion or a revert, decide as if flat; a pair held over
    from the config before is decided as if flat when it is first decided. A buy those words lead is the new
    strategy's first, stopped by what the old config filled that day: neither a top up, nor a whipsaw, nor a loop."""
    first = "first hour under a new strategy, decided as if flat | enter long"
    held_over = "held over from the previous strategy, decided as if flat | enter long"
    decided(book, "champion", (5 * HOUR, "BTC", "none", stopped("BTC", said=first), 0.1003),
            (6 * HOUR, "ETH", "none", REPLAYED + stopped("ETH", said=held_over), 0.0),
            (7 * HOUR, "ETH", "none", stopped("ETH", said="enter long"), 0.0))
    text = report.fill_cap_section(NOW)
    assert ("- champion, BTC, 2026-09-22: no fill; a buy stopped by the cap in 1 hour (05:00), a new strategy's first buy, "
            "stopped by the old config's fills that day\n") in text
    assert ("- champion, ETH, 2026-09-22: no fill; a buy stopped by the cap in 2 hours (06:00, 07:00), 1 entry from flat, "
            "1 first buy of a new strategy, stopped by the old config's fills that day\n") in text


def test_a_pair_at_the_cap_is_listed_though_no_buy_was_stopped(book):
    in_and_out(book, "champion", "ETH")
    fills(book, "champion", (9 * HOUR, "ETH", "sell"))          # a fifth fill is a sell: those are never stopped
    assert report.fill_cap_section(NOW) == (
        "## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before it): no buy stopped by the cap; a pair "
        f"filled 4 times or more in one UTC day on 1 pair day {CAP4}\n"
        "- champion, ETH, 2026-09-22: 5 fills (buy 01:00, sell 02:00, buy 03:00, sell 04:00, sell 09:00); no buy "
        "stopped\n" + NOTES)


def test_the_days_are_utc_days_and_the_window_is_today_and_seven_whole_days_before_it(book):
    in_and_out(book, "champion", "BTC", first=22 * HOUR)        # 22:00, 23:00, then 00:00 and 01:00 the next day
    assert report.fill_cap_section(NOW) == quiet()              # two and two: no UTC day has four
    in_and_out(book, "champion", "ETH", day=2, first=20 * HOUR)             # 20:00 to 23:00 on the 24th
    decided(book, "champion", (2 * 86400 + 23 * HOUR + 1800, "ETH", "none", stopped("ETH")))     # and 23:30
    line = ("- champion, ETH, 2026-09-24: 4 fills (buy 20:00, sell 21:00, buy 22:00, sell 23:00); a buy stopped by "
            "the cap in 1 hour (23:30), an entry from flat\n")
    last = MIDNIGHT + 10 * 86400 - 1                            # 2026-10-01 23:59:59: the 24th is seven days back
    assert line in report.fill_cap_section(last)                # the whole day, at every hour of the last day it shows
    assert line in report.fill_cap_section(MIDNIGHT + 9 * 86400 + 21 * HOUR)
    assert report.fill_cap_section(last + 1) == quiet("2026-09-25")         # and then none of it
    # rows after the hour the summary is written for are not in it (the hourly run never writes any)
    assert report.fill_cap_section(MIDNIGHT + 2 * 86400 + 22 * HOUR) == quiet("2026-09-17")
    assert report.fill_cap_section(MIDNIGHT + 2 * 86400 + 23 * HOUR) == (
        "## Fill cap\n\n- since 2026-09-17 (today and the 7 UTC days before it): no buy stopped by the cap; a pair "
        f"filled 4 times or more in one UTC day on 1 pair day {CAP4}\n"
        "- champion, ETH, 2026-09-24: 4 fills (buy 20:00, sell 21:00, buy 22:00, sell 23:00); no buy stopped\n" + NOTES)
    assert line in report.fill_cap_section(MIDNIGHT + 2 * 86400 + 23 * HOUR + 1800)     # a row of the very second is in
    # and the first second of the first day is in it as well: a replayed hour's rows sit exactly on the hour
    fills(book, "champion", *[(2 * 86400 + i * HOUR, "BTC", side) for i, side in enumerate(("sell", "buy", "sell", "buy"))])
    assert "- champion, BTC, 2026-09-24: 4 fills (sell 00:00, buy 01:00, sell 02:00, buy 03:00); no buy stopped" in \
        report.fill_cap_section(last)


def test_a_slot_is_read_from_the_hour_its_test_began_and_an_idle_slot_not_at_all(book):
    for name in ("challenger1", "challenger2"):                 # both made four fills and had a buy stopped
        in_and_out(book, name, "BTC")
        decided(book, name, (5 * HOUR, "BTC", "none", stopped("BTC")))
    assert report.fill_cap_section(NOW) == quiet()              # neither holds a test: it was the champion's config
    under_test(book, "challenger1", started=HOUR)               # its test began with the first of those fills
    text = report.fill_cap_section(NOW)
    assert ("- challenger1, BTC, 2026-09-22: 4 fills (buy 01:00, sell 02:00, buy 03:00, sell 04:00); a buy stopped "
            "by the cap in 1 hour (05:00), an entry from flat\n") in text and "challenger2" not in text
    under_test(book, "challenger1", started=HOUR + 1)           # a second later: the first fill was not its own
    text = report.fill_cap_section(NOW)
    assert ("- challenger1, BTC, 2026-09-22: 3 fills (sell 02:00, buy 03:00, sell 04:00); a buy stopped by the cap "
            "in 1 hour (05:00), an entry from flat; the cap counts the account's fills from earlier that day, before this test began, as "
            "well\n") in text
    under_test(book, "challenger1", started=5 * HOUR)           # it began in the hour the buy was stopped
    assert ("- challenger1, BTC, 2026-09-22: no fill; a buy stopped by the cap in 1 hour (05:00), an entry from flat; the cap counts the "
            "account's fills from earlier that day, before this test began, as well\n") in report.fill_cap_section(NOW)
    under_test(book, "challenger1", started=5 * HOUR + 1)       # and after it: nothing here is the test's
    assert report.fill_cap_section(NOW) == quiet()


def test_a_test_that_began_before_the_window_is_read_from_the_window(book):
    under_test(book, "challenger1", started=-10 * 86400)        # 2026-09-12, before the section's first day
    in_and_out(book, "challenger1", "BTC", day=-8)              # 2026-09-14: the test's, and too old to show
    in_and_out(book, "challenger1", "ETH", day=-6)              # 2026-09-16: the section's first day
    text = report.fill_cap_section(NOW)
    assert "- challenger1, ETH, 2026-09-16: 4 fills (" in text and "2026-09-14" not in text


def test_rows_out_of_time_order_are_put_in_order(book):
    fills(book, "champion", (4 * HOUR, "BTC", "sell"), (HOUR, "BTC", "buy"), (3 * HOUR, "BTC", "buy"),
          (2 * HOUR, "BTC", "sell"))
    decided(book, "champion", (7 * HOUR, "BTC", "none", stopped("BTC")), (6 * HOUR, "BTC", "none", stopped("BTC")))
    assert ("- champion, BTC, 2026-09-22: 4 fills (buy 01:00, sell 02:00, buy 03:00, sell 04:00); a buy stopped by "
            "the cap in 2 hours (06:00, 07:00), each an entry from flat\n") in report.fill_cap_section(NOW)


def test_the_columns_are_read_by_name_whatever_their_order_in_the_file(book):
    adir = book / "state" / "champion"
    adir.joinpath("trades.csv").write_text("side,ts,pair\n" + "".join(
        f"{'sell' if i % 2 else 'buy'},{MIDNIGHT + (i + 1) * HOUR},BTC\n" for i in range(4)))
    adir.joinpath("decisions.csv").write_text(f"current_weight,reason,pair,ts,action\n0,\"{stopped('BTC')}\",BTC,"
                                              f"{MIDNIGHT + 6 * HOUR},none\n")
    assert ("- champion, BTC, 2026-09-22: 4 fills (buy 01:00, sell 02:00, buy 03:00, sell 04:00); a buy stopped by "
            "the cap in 1 hour (06:00), an entry from flat\n") in report.fill_cap_section(NOW)


def test_the_note_on_a_test_s_first_day_is_only_for_that_day_and_only_when_it_explains_something(book):
    under_test(book, "challenger1", started=-86400 + 12 * HOUR)  # began at noon the day before
    in_and_out(book, "challenger1", "BTC", n=2)
    decided(book, "challenger1", (5 * HOUR, "BTC", "none", stopped("BTC", n=2, cap=2)))     # under an older cap
    text = report.fill_cap_section(NOW)
    assert ("- challenger1, BTC, 2026-09-22: 2 fills (buy 01:00, sell 02:00); a buy stopped by the cap in 1 hour "
            "(05:00), an entry from flat\n") in text
    under_test(book, "challenger1", started=HOUR)               # its first day, and four fills of its own on it
    in_and_out(book, "challenger1", "BTC", n=2, first=3 * HOUR)
    text = report.fill_cap_section(NOW)
    assert "sell 04:00); a buy stopped by the cap in 1 hour (05:00), an entry from flat\n" in text and "before this test began" not in text


def test_an_account_that_cannot_be_read_says_so_and_costs_the_others_nothing(book):
    in_and_out(book, "champion", "BTC")
    under_test(book, "challenger1", started=0)
    (book / "state" / "challenger1" / "trades.csv").write_text("")
    (book / "state" / "challenger2").mkdir()
    (book / "state" / "challenger2" / "meta.json").write_text("{not json")
    lines = report.fill_cap_section(NOW).split("\n")
    assert lines[2].startswith("- since 2026-09-16 (today and the 7 UTC days before it): no buy stopped by the cap; a "
                               "pair filled 4 times or more in one UTC day on 1 pair day ")
    assert lines[3].startswith("- challenger1: its record could not be read this hour (EmptyDataError: ")
    assert lines[3].endswith("), so it is not in the counts above")
    assert lines[4].startswith("- challenger2: its record could not be read this hour (JSONDecodeError: ")
    assert lines[5].startswith("- champion, BTC, 2026-09-22: 4 fills (")
    (book / "state" / "champion" / "trades.csv").unlink()       # and when the rest is quiet, the same lines
    lines = report.fill_cap_section(NOW).split("\n")
    assert lines[2] + "\n" == quiet().split("\n\n")[1] and lines[3].startswith("- challenger1: its record could not")
    assert lines[4].startswith("- challenger2: its record could not") and lines[5:] == [""]
    # a decisions file from before it had an action column cannot be read for stopped buys, and says so
    (book / "state" / "champion" / "decisions.csv").write_text("ts,pair,reason\n1,BTC,x\n")
    assert "- champion: its record could not be read this hour (ValueError: " in report.fill_cap_section(NOW)


def test_the_shadow_is_read_while_it_runs(book):
    in_and_out(book, "shadow", "ETH")
    assert report.fill_cap_section(NOW) == quiet()              # no shadow is running: the files are nobody's
    config.dump_yaml(book / "configs" / "shadow.yaml", FLIP)
    (book / "state" / "shadow" / "meta.json").write_text('{"status": "active", "started_at": 0}')
    assert "- shadow, ETH, 2026-09-22: 4 fills (" in report.fill_cap_section(NOW)


def test_with_no_cap_set_the_section_says_so_and_still_lists_what_an_older_cap_stopped(book):
    unset = ("no cap is set: `max_fills_per_pair_per_day` in configs/risk.yaml is missing, 0 or under 1, so a pair "
             "can fill any number of times in a day")
    for written in ("missing", 0, None, 0.5):
        body = dict(RISK)
        if written == "missing":
            del body["max_fills_per_pair_per_day"]
        else:
            body["max_fills_per_pair_per_day"] = written
        config.dump_yaml(book / "configs" / "risk.yaml", body)
        in_and_out(book, "champion", "BTC", n=9)                # nine fills in a day, and nothing to stop them
        assert report.fill_cap_section(NOW) == ("## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before "
                                                f"it): no buy stopped by the cap, in any account read ({unset})\n")
    decided(book, "champion", (86400 + HOUR, "ETH", "none", stopped("ETH")))
    assert report.fill_cap_section(NOW) == (
        "## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before it): the cap stopped a buy in 1 hour, on 1 "
        f"pair day ({unset})\n- champion, ETH, 2026-09-23: no fill; a buy stopped by the cap in 1 hour (01:00), an entry from flat\n" + NOTES)


def test_a_cap_of_one_and_a_cap_under_zero_are_said_as_they_are(book):
    config.dump_yaml(book / "configs" / "risk.yaml", {**RISK, "max_fills_per_pair_per_day": 1})
    assert report.fill_cap_section(NOW) == ("## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before it): "
                                            "no buy stopped by the cap and no pair that filled 1 time or more in one "
                                            "UTC day, in any account read (the cap is 1 fill in one pair in one UTC "
                                            "day)\n")
    fills(book, "champion", (HOUR, "BTC", "buy"))
    assert ("; a pair filled 1 time or more in one UTC day on 1 pair day (the cap is 1 fill in one pair in one UTC "
            "day)\n- champion, BTC, 2026-09-22: 1 fill (buy 01:00); no buy stopped\n") in report.fill_cap_section(NOW)
    config.dump_yaml(book / "configs" / "risk.yaml", {**RISK, "max_fills_per_pair_per_day": -1})
    decided(book, "champion", (2 * HOUR, "BTC", "none", stopped("BTC", n=1, cap=-1)))  # what the engine writes once a pair has filled
    fills(book, "champion", (3 * HOUR, "ETH", "sell"))          # a fill with no buy stopped: no line, whatever the cap
    assert report.fill_cap_section(NOW) == (
        "## Fill cap\n\n- since 2026-09-16 (today and the 7 UTC days before it): the cap stopped a buy in 1 hour, on 1 "
        "pair day (`max_fills_per_pair_per_day` in configs/risk.yaml is -1, under zero, which the engine cannot use: the "
        "hourly run stops with an error at the first buy of a UTC day in a pair that has not filled that day)\n"
        "- champion, BTC, 2026-09-22: 1 fill (buy 01:00); a buy stopped by the cap in 1 hour (02:00), an entry from "
        "flat\n" + NOTES)


def test_a_cap_that_cannot_be_read_costs_the_summary_one_section_and_no_more(book):
    config.dump_yaml(book / "configs" / "risk.yaml", {**RISK, "max_fills_per_pair_per_day": "four"})
    with pytest.raises(ValueError):
        report.fill_cap_section(NOW)
    whole = report.build(NOW)
    assert "## Fill cap\n\nits record could not be read this hour (ValueError: " in whole
    assert "## Runs" in whole and "## Challenger slots" in whole and "## champion: flip (HF)" in whole


def test_stopped_buys_come_first_then_the_newest_and_the_same_records_always_read_the_same(book):
    under_test(book, "challenger1", started=-86400)
    for name in ("challenger1", "champion"):                    # written slot first: the order is not the files'
        in_and_out(book, name, "ETH", day=1)
        in_and_out(book, name, "BTC", day=1)
        in_and_out(book, name, "ETH", day=0)
    decided(book, "champion", (6 * HOUR, "ETH", "none", stopped("ETH")), (7 * HOUR, "ETH", "none", stopped("ETH")))
    text = report.fill_cap_section(NOW)
    assert [line.split(":")[0] for line in text.split("\n")[2:10]] == [
        "- since 2026-09-16 (today and the 7 UTC days before it)",
        "- champion, ETH, 2026-09-22",                                      # the one with a buy stopped, though older
        "- champion, BTC, 2026-09-23", "- champion, ETH, 2026-09-23",       # then the newest day: the champion first,
        "- challenger1, BTC, 2026-09-23", "- challenger1, ETH, 2026-09-23",     # and a pair in the alphabet's order
        "- challenger1, ETH, 2026-09-22", "- times are UTC, and a pair day is one pair on one UTC day in one account. "
        "At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy "
        "still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a "
        "slot with no test is left out"]
    assert text.split("\n")[2].endswith("the cap stopped a buy in 2 hours, on 1 pair day; a pair filled 4 times or "
                                        f"more in one UTC day on 6 pair days {CAP4}")
    assert all(report.fill_cap_section(NOW) == text for _ in range(3))


def test_a_long_list_is_cut_to_twelve_lines_and_never_at_the_cost_of_a_stopped_buy(book, monkeypatch):
    monkeypatch.setattr(report, "CAP_DAYS", 30)
    for d in range(15):                                         # fifteen days at the cap, the oldest three with stops
        in_and_out(book, "champion", "BTC", day=d)
    for d in (0, 1, 2):
        decided(book, "champion", (d * 86400 + 6 * HOUR, "BTC", "none", stopped("BTC")))
    lines = report.fill_cap_section(MIDNIGHT + 15 * 86400).split("\n")
    assert lines[2].startswith("- since 2026-09-07 (today and the 30 UTC days before it): the cap stopped a buy in 3 "
                               "hours, on 3 pair days; a pair filled 4 times or more in one UTC day on 15 pair days ")
    listed = [line.split(":")[0] for line in lines[3:15]]
    assert listed[:4] == ["- champion, BTC, 2026-09-24", "- champion, BTC, 2026-09-23", "- champion, BTC, 2026-09-22",
                          "- champion, BTC, 2026-10-06"] and listed[-1] == "- champion, BTC, 2026-09-28"
    assert lines[15] == "- and 3 more pair days not listed, none of them with a buy stopped"
    assert lines[16].startswith("- times are UTC,")
    monkeypatch.setattr(report, "CAP_LINES", 2)                 # and when even the stopped ones do not fit, it says so
    lines = report.fill_cap_section(MIDNIGHT + 15 * 86400).split("\n")
    assert lines[5] == "- and 13 more pair days not listed, 1 of them with a buy stopped"
    monkeypatch.setattr(report, "CAP_LINES", 14)
    assert report.fill_cap_section(MIDNIGHT + 15 * 86400).split("\n")[17] == (
        "- and 1 more pair day not listed, none of them with a buy stopped")
    monkeypatch.setattr(report, "CAP_LINES", 15)                # all of them fit: no such line
    assert "not listed" not in report.fill_cap_section(MIDNIGHT + 15 * 86400)


def test_a_day_of_many_fills_or_many_stopped_buys_is_cut_to_eight_and_says_how_many_more(book):
    in_and_out(book, "champion", "BTC", n=11, first=0)
    decided(book, "champion", *[(12 * HOUR + i * 600, "BTC", "none", stopped("BTC", n=11)) for i in range(9)])
    assert ("- champion, BTC, 2026-09-22: 11 fills (buy 00:00, sell 01:00, buy 02:00, sell 03:00, buy 04:00, sell "
            "05:00, buy 06:00, sell 07:00, and 3 more); a buy stopped by the cap in 9 hours (12:00, 12:10, 12:20, "
            "12:30, 12:40, 12:50, 13:00, 13:10, and 1 more), each an entry from flat\n") in report.fill_cap_section(NOW)
    in_and_out(book, "champion", "ETH", n=8, first=0)           # eight is all of them: nothing more to speak of
    decided(book, "champion", *[(12 * HOUR + i * 600, "ETH", "none", stopped("ETH", n=8)) for i in range(8)])
    assert ("- champion, ETH, 2026-09-22: 8 fills (buy 00:00, sell 01:00, buy 02:00, sell 03:00, buy 04:00, sell "
            "05:00, buy 06:00, sell 07:00); a buy stopped by the cap in 8 hours (12:00, 12:10, 12:20, 12:30, 12:40, "
            "12:50, 13:00, 13:10), each an entry from flat\n") in report.fill_cap_section(NOW)
