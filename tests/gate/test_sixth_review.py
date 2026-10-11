"""PROTECTED. Pinned after the sixth review (2026-10-05): rows lost from the
middle of a record and rows that are not fills, a `slots` line that is not a
count, a slot the count no longer covers, what stops the hour and what is only
waited for, a guard that is superseded or overdue, a window in its first hour,
and sentences that set two figures against each other."""
import json
from pathlib import Path

import pandas as pd
import pytest

from bot import config, data, promote, report, shadow, slot

from .test_fifth_review import fills, two_tests, whole
from .test_two_looks import (CHAMP, DAY, GATE, RULES, STEADY, STRONG, at, equity, ledger,  # noqa: F401
                             sandbox, set_rules, start_test, trades)

TRADE_COLUMNS = ["ts", "account", "pair", "side", "qty", "price", "ref_price", "notional", "fee", "slippage_cost",
                 "reason", "equity_after"]


def no_candles(root):
    """Take the candle file away; returns the call that puts it back."""
    p = root / "state" / "candles" / "BTC.csv"
    text = p.read_text()
    p.unlink()
    getattr(data, "_READ_CACHE", {}).clear()

    def back():
        p.write_text(text)
        getattr(data, "_READ_CACHE", {}).clear()
    return back


# --- a record set against its own counts ------------------------------------------------------------------------

def test_a_trades_row_that_is_not_a_fill_is_a_fault(sandbox, capsys):
    """A fill whose quantity had gone blank was left out of the count of fills
    and of the walk through the positions, and the count of rows still agreed
    with the account's own: a test with twenty finished trades read as having
    finished none and was killed for it. The engine writes no row that is not
    a fill, so one that is not is damage, and nothing is ruled on it."""
    start_test(sandbox, STEADY)
    whole(sandbox, "challenger1")
    tr_file = sandbox / "state" / "challenger1" / "trades.csv"
    text = tr_file.read_text()
    rows = text.strip().split("\n")

    def with_cell(k, column, value):
        cells = rows[k].split(",")
        cells[TRADE_COLUMNS.index(column)] = value
        tr_file.write_text("\n".join(rows[:k] + [",".join(cells)] + rows[k + 1:]) + "\n")
        return promote.record_fault("challenger1")

    one = ("challenger1/trades.csv has 1 row that is not a fill (a time, a pair, buy or sell, and a quantity and a "
           "price above zero)")
    for column, value in (("qty", ""), ("qty", "lots"), ("qty", "0"), ("qty", "-10"), ("ts", ""), ("ts", "then"),
                          ("side", "hold"), ("side", ""), ("pair", ""), ("pair", "  "), ("price", ""), ("price", "0"),
                          ("notional", ""), ("notional", "-1000")):
        assert with_cell(5, column, value) == one, (column, value)
    assert with_cell(5, "reason", "anything at all") is None             # the cells a fill is not read from are free
    assert with_cell(5, "fee", "") is None
    cells = rows[7].split(",")
    cells[TRADE_COLUMNS.index("qty")] = ""
    with_cell(5, "qty", "")
    tr_file.write_text(tr_file.read_text().replace(rows[7], ",".join(cells)))
    assert promote.record_fault("challenger1").startswith("challenger1/trades.csv has 2 rows that are not a fill (")
    whole(sandbox, "champion")
    assert promote.main(["--now", str(at(60))]) == 0
    assert "H5 could not be looked at this hour (Unreadable: challenger1/trades.csv has 2 rows that are not a fill" \
        in capsys.readouterr().out
    assert "### " not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    tr_file.write_text(text)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)                # mended: the look that was due is taken


def test_rows_lost_from_the_middle_of_an_equity_record_are_a_fault(sandbox, capsys):
    """The checks on an equity file were its first row, its last row and its
    order, so rows cut from the middle left a file that passed them all. The
    champion's drawdown then read shallower than it had been, which tightens
    the guard on every challenger. The account now counts its readings as it
    counts its fills (bot/run.py), and the file is set against the count."""
    start_test(sandbox, STRONG, champion_returns=[-0.012, 0.011] * 60)
    for name in ("champion", "challenger1"):
        whole(sandbox, name)
    adir = sandbox / "state" / "champion"
    st = json.loads((adir / "account.json").read_text())
    eq_text = (adir / "equity.csv").read_text()
    rows = eq_text.strip().split("\n")
    (adir / "equity.csv").write_text("\n".join(rows[:3] + rows[50:]) + "\n")
    assert promote.record_fault("champion") is None                      # an account that keeps no count: not seen
    (adir / "account.json").write_text(json.dumps({**st, "equity_rows": len(rows) - 1}))
    assert promote.record_fault("champion") == ("champion/equity.csv has 73 rows and the account has taken 120 "
                                                "readings: rows have been lost or added")
    assert promote.main(["--now", str(at(60))]) == 0
    assert "(Unreadable: champion/equity.csv has 73 rows and the account has taken 120 readings" in capsys.readouterr().out
    assert "### " not in ledger(sandbox)
    (adir / "equity.csv").write_text(eq_text + rows[-1] + "\n")          # a row too many is not this account's file either
    assert promote.record_fault("champion").startswith("champion/equity.csv has 121 rows and the account has taken 120")
    (adir / "account.json").write_text(json.dumps({**st, "equity_rows": 1}))
    (adir / "equity.csv").write_text(rows[0] + "\n" + rows[1] + "\n")
    assert promote.record_fault("champion") == "champion/equity.csv does not end at the account's last run"
    (adir / "equity.csv").write_text(eq_text)
    (adir / "account.json").write_text(json.dumps({**st, "equity_rows": len(rows) - 1}))
    assert promote.record_fault("champion") is None
    # a blank line is not a row, to the count or to the check (the two count the same way)
    (adir / "equity.csv").write_text(eq_text.replace(rows[9] + "\n", rows[9] + "\n\n"))
    assert promote.record_fault("champion") is None


# --- the `slots` line ---------------------------------------------------------------------------------------------

@pytest.mark.parametrize("written", [None, "", "three", 2.9, True, 0, -1, "3", [2], "missing", "no block"])
def test_a_slots_line_that_is_not_a_count_stops_the_run(sandbox, written):
    """With a wrong count some slots are simply not run. `slots: 2.9` ran two
    slots and a slip in the line's name ran one, the run going green each hour
    while a test stood still. Nothing is run or ruled until it is mended."""
    body = config.load_yaml(sandbox / "configs" / "risk.yaml")
    if written == "missing":
        del body["challenger"]["slots"]
        body["challenger"]["slot"] = 2
    elif written == "no block":
        body["challenger"] = None
    else:
        body["challenger"]["slots"] = written
    config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
    shown = None if written in ("missing", "no block") else written
    with pytest.raises(ValueError) as said:
        config.n_slots()
    assert str(said.value) == (f"configs/risk.yaml: challenger.slots must be a whole number of 1 or more, and it is "
                               f"{shown!r}; nothing is run until it is mended")
    for ask in (config.challengers, config.accounts, config.prepare, lambda: promote.main(["--now", str(at(30))]),
                lambda: report.build(at(30))):
        with pytest.raises(ValueError, match="challenger.slots must be a whole number of 1 or more"):
            ask()


def test_a_slots_line_that_is_a_count_is_that_many_slots(sandbox):
    body = config.load_yaml(sandbox / "configs" / "risk.yaml")
    for written, n in ((1, 1), (2, 2), (4, 4), (3.0, 3)):
        body["challenger"]["slots"] = written
        config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
        assert config.n_slots() == n and config.challengers() == [f"challenger{k}" for k in range(1, n + 1)]


def test_a_running_test_in_a_slot_the_count_no_longer_covers_is_said_every_hour(sandbox, capsys):
    """`slots` lowered from 2 to 1 while slot 2 held a test: that test was
    neither run nor ruled from then on, with nothing said anywhere."""
    two_tests(sandbox)
    assert promote.other_notes() == []
    set_rules(sandbox, slots=1)
    note = ("challenger.slots is 1, and challenger2 holds a running test (H6): that slot is neither run nor ruled "
            "until slots covers it")
    assert promote.other_notes() == [note]
    promote.main(["--now", str(at(30))])
    assert f"WARNING: {note}" in capsys.readouterr().out
    assert f"- SETTING NOT USED: {note}" in report.test_section(at(30))
    slot.reset("challenger2")                                            # an idle slot past the count is nothing to speak of
    assert promote.other_notes() == []
    (sandbox / "state" / "challenger2" / "meta.json").write_text("{cut")  # nor does one that cannot be read stop the notes
    assert promote.other_notes() == []


# --- the `ruleset` line -----------------------------------------------------------------------------------------

def test_a_ruleset_line_in_quotes_is_still_its_number(sandbox):
    """`ruleset: '7'` is text to the parser. Read as "cannot be used" it
    stamped new tests `unreadable` and wrote a warning every hour for a line
    that says what it means."""
    body = config.load_yaml(sandbox / "configs" / "risk.yaml")
    for written, want in (("7", 7), (7.0, 7), ("7.0", 7), (8, 8), ("7.5", 7.5), (" 9 ", 9)):
        body["ruleset"] = written
        config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
        assert config.ruleset_number() == want and config.ruleset_stamp() == want, written
        assert type(config.ruleset_stamp()) is type(want) and promote.other_notes() == []
    for written in ("inf", "-inf", "nan", "7 or so", [7], {"n": 7}, False):
        body["ruleset"] = written
        config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
        assert config.ruleset_number() is None and config.ruleset_stamp() == "unreadable", written
    del body["ruleset"]
    config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
    assert config.ruleset_number() is None and config.ruleset_stamp() == "unreadable"


# --- what stops the hour, and what is only waited for -------------------------------------------------------------

def guarded(root):
    """The champion is H5, promoted at second 100 over H0, which now runs as the shadow and has done better."""
    slot.reset("challenger1")
    shadow.start(config.account_cfg("champion"), "H5", 100, 10000.0, 10000.0)
    config.dump_yaml(root / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (root / "LEDGER.md").write_text(ledger(root).replace("- Status: testing", "- Status: promoted"))
    equity(root, "champion", [-0.004, 0.001] * 31)
    equity(root, "shadow", [-0.002, 0.001] * 31)
    trades(root, "shadow")
    return 100 + 60 * DAY + 100


def test_a_revert_that_fails_while_it_is_being_made_stops_the_hour(sandbox, monkeypatch, capsys):
    """The whole of the guard's ruling sat inside the catch that keeps a
    damaged record from stopping the hour. A revert that had written its
    ledger block and champion.yaml and then failed was swallowed with a
    warning, and the hour went on to commit half of it. Only the reading is
    waited for: a write that fails stops the hour, nothing of it is committed,
    and the next hour makes the ruling again from the last whole state."""
    now = guarded(sandbox)

    def fails(*a, **k):
        raise OSError("disk full")
    monkeypatch.setattr(shadow, "stop", fails)
    with pytest.raises(OSError, match="disk full"):
        promote.main(["--now", str(now)])
    assert "H5: reverted" in capsys.readouterr().out                     # the ruling had been made; it was the writing


def test_a_ruling_that_the_promotion_holds_stops_the_hour_too_when_it_cannot_be_written(sandbox, monkeypatch):
    now = guarded(sandbox)
    equity(sandbox, "shadow", [-0.006, 0.001] * 31)                      # the deposed config did worse: the promotion holds

    def fails(*a, **k):
        raise OSError("disk full")
    monkeypatch.setattr(promote, "update_ledger", fails)
    with pytest.raises(OSError, match="disk full"):
        promote.main(["--now", str(now)])
    assert shadow.load()["status"] == "active"                           # still there to be ruled on at the next hour


def test_a_guard_record_that_cannot_be_read_is_waited_for(sandbox, capsys):
    now = guarded(sandbox)
    meta_file = sandbox / "state" / "shadow" / "meta.json"
    good = json.loads(meta_file.read_text())
    for damaged, how in (("[]", "ValueError: it is not a shadow record"),
                         (json.dumps({**good, "started_at": "then"}), "ValueError: invalid literal"),
                         (json.dumps({**good, "replaced_by": None}), "ValueError: it does not name the promotion it guards"),
                         (json.dumps({k: v for k, v in good.items() if k != "started_at"}), "KeyError: 'started_at'")):
        meta_file.write_text(damaged)
        promote.rule_on_shadow(now, RULES)
        assert f"WARNING: the shadow guard could not be ruled on this hour ({how}" in capsys.readouterr().out
        assert "### " not in ledger(sandbox)
    meta_file.write_text(json.dumps(good))
    promote.rule_on_shadow(now, RULES)
    assert "### Result H5: reverted" in ledger(sandbox)


def test_a_slot_record_that_lacks_what_a_look_needs_is_waited_for(sandbox, capsys):
    two_tests(sandbox)
    meta_file = sandbox / "state" / "challenger1" / "meta.json"
    good = json.loads(meta_file.read_text())
    for damaged, how in (({**good, "hypothesis": None}, "ValueError: its slot record names no hypothesis"),
                         ({**good, "hypothesis": ""}, "ValueError: its slot record names no hypothesis"),
                         ({**good, "started_at": None}, "TypeError"),
                         ({k: v for k, v in good.items() if k != "start_equity"}, "KeyError: 'start_equity'")):
        meta_file.write_text(json.dumps(damaged))
        assert promote.main(["--now", str(at(60))]) == 0
        assert f"could not be looked at this hour ({how}" in capsys.readouterr().out
    assert "### First look H6: passed" in ledger(sandbox) and "H5:" not in ledger(sandbox).split("## Results")[1]
    # a start equity that is not a table of accounts: measured from its first reading, and no more than that
    meta_file.write_text(json.dumps({**good, "start_equity": [10000.0]}))
    assert promote.main(["--now", str(at(60))]) == 0
    assert "### First look H5: passed" in ledger(sandbox)


def test_two_winners_in_one_hour_are_ruled_on_from_the_reading_each_look_took(sandbox, monkeypatch):
    """The verdicts used to read every record again, twice, after the looks.
    They are ruled on from the reading the look itself took."""
    two_tests(sandbox)
    for name in ("challenger1", "challenger2"):
        meta = slot.load(name)
        meta["ruleset"] = 6                                              # old tests: promoted at their one look
        slot.save(name, meta)
    equity(sandbox, "challenger2", STRONG)
    asked = []
    real = promote.paired_slot

    def counted(name, *a, **k):
        asked.append(name)
        return real(name, *a, **k)
    monkeypatch.setattr(promote, "paired_slot", counted)
    promote.main(["--now", str(at(60))])
    assert asked == ["challenger1", "challenger2"]
    text = ledger(sandbox)
    assert "### Result H6: promoted" in text and "### Result H5: restarted" in text
    assert text.index("### Result H6: promoted") < text.index("### Result H5: restarted")
    assert config.account_cfg("champion")["hypothesis"] == "H6"
    assert slot.load("challenger1")["restarted_against"] == "H6"


# --- a guard that is superseded, or due and waiting ------------------------------------------------------------

def test_a_superseded_guard_is_on_record_even_when_its_numbers_cannot_be_read(sandbox, capsys):
    """With the old shadow's record damaged the `superseded` block was not
    written at all, and the earlier promotion was left looking confirmed."""
    start_test(sandbox, STRONG)
    shadow.start(config.account_cfg("champion"), "H9", 0, 10000.0, 10000.0)
    equity(sandbox, "shadow", STEADY)
    (sandbox / "state" / "shadow" / "trades.csv").write_text("")
    promote.note_superseded("H5", at(30))
    text = ledger(sandbox)
    assert "### Result H9: superseded" in text and "- Promoted champion: no data\n- Deposed config (shadow): no data" in text
    assert ("This promotion was neither confirmed nor reverted. The guard's numbers so far could not be read "
            "(Unreadable: shadow/trades.csv cannot be read") in text
    # and with a record that can be read, the numbers are there
    trades(sandbox, "shadow")
    promote.note_superseded("H5", at(30))
    block = ledger(sandbox).split("### Result H9: superseded")[2]
    assert "- Deposed config (shadow): return +1.85%" in block and "could not be read" not in block


def test_the_summary_says_why_a_guard_that_is_due_has_not_been_ruled_on(sandbox, capsys):
    """Past its window the shadow line said only that a ruling was due. What
    it was waiting for was in the hourly log and nowhere a reader looks."""
    start_test(sandbox, STEADY)
    shadow.start(config.account_cfg("champion"), "H9", 0, 10000.0, 10000.0)
    equity(sandbox, "shadow", STEADY)
    trades(sandbox, "shadow")
    assert promote.guard_waits(at(30), RULES) is None                    # not due
    assert "no ruling this hour" not in report.test_section(at(30))
    assert promote.guard_waits(at(61), RULES) is None                    # due, and nothing in its way
    back = no_candles(sandbox)
    assert promote.guard_waits(at(30), RULES) is None                    # not due: nothing is waited for, whatever is missing
    assert promote.guard_waits(at(61), RULES) == "there are no candles for its window"
    assert ("- shadow: H0 (deposed by H9) running since 1970-01-01 00:00Z, day 61.1 of 60 (its ruling is due: made at "
            "the next hourly run for which the market data and both records are whole); the promotion is reverted if "
            "it wins\n  no ruling this hour: there are no candles for its window. The guard is ruled on once that is "
            "whole") in report.test_section(at(61))
    promote.rule_on_shadow(at(61), RULES)                                # the hourly log says the same
    assert "the guard on H9 is due a ruling on day 61.1 but there are no candles for its window" in capsys.readouterr().out
    back()
    p = sandbox / "state" / "shadow" / "equity.csv"
    text = p.read_text()
    p.write_text(text.split("\n", 1)[0] + "\n")
    assert promote.guard_waits(at(61), RULES) == "there is no usable equity record for shadow in its window"
    p.write_text(text)
    (sandbox / "state" / "shadow" / "trades.csv").write_text("")
    assert promote.guard_waits(at(61), RULES).startswith("its record could not be read (Unreadable: shadow/trades.csv")
    assert "  no ruling this hour: its record could not be read (Unreadable: shadow/trades.csv" in report.test_section(at(61))
    shadow.stop("held")
    assert promote.guard_waits(at(61), RULES) is None                    # no guard, nothing to wait for


def test_a_verdict_that_is_due_and_waiting_is_marked_on_the_slot_line(sandbox, capsys):
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    assert "its verdict is due" not in slot.describe_one("challenger1", at(119))
    back = no_candles(sandbox)
    promote.main(["--now", str(at(120))])
    assert "is due a ruling on day 120.1 but there are no candles for its window" in capsys.readouterr().out
    assert slot.describe_one("challenger1", at(120)).endswith(
        "day 120.1 of 120, 0.0 days until the verdict, first look passed (two look rule) (its verdict is due: made at "
        "the next hourly run for which the market data and its record are whole)")
    back()
    promote.main(["--now", str(at(120))])
    assert "### Result H5: promoted" in ledger(sandbox)


# --- a window in its first hour ---------------------------------------------------------------------------------

def test_a_window_that_opened_this_hour_is_not_said_to_have_no_candles(sandbox):
    """In a test's first hour no candle that closes inside its window is on
    file yet. The summary read "no skill figure this hour: there are no
    candles for its window. Nothing is ruled on a test until the market data
    is whole", which is the line the daily agent passes on as damage."""
    start_test(sandbox, STEADY)
    opened = 30 * DAY + 3600                                             # the reading of day 30 is its first
    meta = slot.load("challenger1")
    meta["started_at"] = opened
    slot.save("challenger1", meta)
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), opened + 600, RULES)
    assert mc["gap"] == promote.JUST_OPENED == "its window opened within the hour and no candle in it is on file yet"
    assert chal["skill"] is None and chal["return"] is not None
    text = report.test_section(opened + 600)
    assert "  no skill figure yet: its window opened within the hour, and no candle in it is on file yet" in text
    assert "no candles for its window" not in text and "no skill figure this hour" not in text
    assert "  market over the window: nothing yet (no candle in it is on file)" in text and "no candle data" not in text
    # the same for an old test, whose summary also carries the two look reading: in its first hour there is
    # nothing to measure, and the words kept for a damaged record ("no reading this hour") are not used
    old_test = slot.load("challenger1")
    old_test["ruleset"] = 6
    slot.save("challenger1", old_test)
    text = report.test_section(opened + 600)
    assert "two look rule (measured" not in text and "no reading this hour" not in text
    assert "two look rule (measured, not applied to this test): " in report.test_section(opened + 3600 + 600)
    old_test["ruleset"] = 7
    slot.save("challenger1", old_test)
    # A run that straddles the top of an hour: the test begins seconds before it, and the verdict code runs
    # seconds after. A candle has closed inside the window by then and the run before it could not have fetched it.
    straddle = slot.load("challenger1")
    p = sandbox / "state" / "candles" / "BTC.csv"
    whole_file = p.read_text()
    candles = pd.read_csv(p)
    straddle["started_at"] = opened + 3570                               # thirty seconds before the hour
    slot.save("challenger1", straddle)
    eq = pd.read_csv(sandbox / "state" / "challenger1" / "equity.csv")
    for name in ("champion", "challenger1"):                             # each has a reading at the test's first moment
        f = sandbox / "state" / name / "equity.csv"
        rows = pd.read_csv(f)
        rows.loc[rows["ts"] == opened, "ts"] = opened + 3570
        rows.to_csv(f, index=False)
    candles[candles["time"] + 3600 <= opened + 3570].to_csv(p, index=False)     # as fetched before the hour turned
    getattr(data, "_READ_CACHE", {}).clear()
    mc = promote.paired_slot("challenger1", slot.load("challenger1"), opened + 3615, RULES)[2]
    assert mc["gap"] == promote.JUST_OPENED
    assert "no skill figure yet" in report.test_section(opened + 3615)
    # an hour later with still nothing on file for the window, it is a gap like any other
    mc = promote.paired_slot("challenger1", slot.load("challenger1"), opened + 3570 + 3700, RULES)[2]
    assert mc["gap"] == "there are no candles for its window"
    p.write_text(whole_file)
    getattr(data, "_READ_CACHE", {}).clear()
    for name in ("champion", "challenger1"):
        f = sandbox / "state" / name / "equity.csv"
        rows = pd.read_csv(f)
        rows.loc[rows["ts"] == opened + 3570, "ts"] = opened
        rows.to_csv(f, index=False)
    straddle["started_at"] = opened
    slot.save("challenger1", straddle)
    assert promote.main(["--now", str(opened + 600)]) == 0 and "### " not in ledger(sandbox)
    # an hour on, one candle has closed inside it, and there is a figure
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), opened + 3600 + 600, RULES)
    assert mc["gap"] is None and chal["skill"] is not None
    assert "no skill figure" not in report.test_section(opened + 3600 + 600)
    # candles that cannot be read are still said to be that, first hour or not
    (sandbox / "state" / "candles" / "BTC.csv").write_text("time,close\n\"cut")
    getattr(data, "_READ_CACHE", {}).clear()
    mc = promote.paired_slot("challenger1", slot.load("challenger1"), opened + 600, RULES)[2]
    assert mc["gap"].startswith("the candles for its window could not be read (")


def test_the_words_for_a_gap_in_the_order_they_are_asked():
    mc = {"pairs": 2, "basket_return": 0.0, "basket_path": pd.Series([1.0, 1.0]), "missing": [], "late": [],
          "last_close": {"BTC": 7200, "ETH": 7200}}
    assert promote.market_gap(mc, 7200 + 900, 100) is None
    assert promote.market_gap(mc, 7200 + 900) is None                    # asked without a start: nothing to say of it
    assert promote.market_gap(mc, 7200 + 900, 7200 - 600) is None        # under an hour old, with its first candle on file
    assert promote.market_gap(mc, 10800, 7200 + 300) == "the candles for BTC, ETH stop before the one that closed at " \
                                                         "the top of this hour"
    none = {"pairs": 0, "basket_return": None, "basket_path": None, "missing": ["BTC", "ETH"], "late": [], "last_close": {}}
    assert promote.market_gap(none, 7200 + 900, 7200) == promote.JUST_OPENED     # opened on the hour, fifteen minutes ago
    assert promote.market_gap(none, 7200 + 900, 7200 + 300) == promote.JUST_OPENED
    assert promote.market_gap(none, 7200 + 15, 7200 - 30) == promote.JUST_OPENED     # a run that straddles the hour
    assert promote.market_gap(none, 7200 + 3599, 7200) == promote.JUST_OPENED
    assert promote.market_gap(none, 7200 + 3600, 7200) == "there are no candles for its window"    # an hour old: a gap
    assert promote.market_gap(none, 7200 + 900) == "there are no candles for its window"
    assert promote.market_gap({**none, "unread": "ParserError: cut"}, 7200 + 900, 7200) == \
        "the candles for its window could not be read (ParserError: cut)"


# --- sentences ----------------------------------------------------------------------------------------------------

def test_two_figures_set_against_each_other_can_be_told_apart():
    """"challenger skill +0.00% ... beat champion skill +0.00%" is a sentence
    nobody can check. Figures are printed with as many decimals, two to six,
    as it takes to tell apart any two of them that differ."""
    assert promote._apart(0.05, 0.01) == ["+5.00%", "+1.00%"]
    assert promote._apart(0.00004, 0.00001) == ["+0.004%", "+0.001%"]
    assert promote._apart(-0.00004, 0.00003) == ["-0.004%", "+0.003%"]   # a zero reads the same whatever its sign
    assert promote._apart(0.0, 0.0) == ["+0.00%", "+0.00%"] and promote._apart(0.0123, 0.0123) == ["+1.23%", "+1.23%"]
    assert promote._apart(0.012, 0.01204, 0.0) == ["+1.200%", "+1.204%", "+0.000%"]
    assert promote._apart(1.004, 1.0, percent=False) == ["+1.004", "+1.000"]
    assert promote._against(0.996, 1.0, percent=False) == ("+0.996", "1.000")
    assert promote._against(-0.00004, 0.0) == ("-0.004%", "0.000%")
    champ = {"return": 0.00001, "max_drawdown": -0.01, "trades": 40, "skill": 0.00001, "skill_exposure": 0.5}
    chal = {"return": 0.00004, "max_drawdown": -0.01, "trades": 40, "skill": 0.00004, "skill_exposure": 0.5,
            "skill_basis": "usual", "edge_t": None}
    assert promote.decide(champ, chal, RULES) == ("promoted", (
        "challenger skill +0.004% (net +0.00%, benchmark exposure 0.50) beat champion skill +0.001% (net +0.00%, "
        "benchmark exposure 0.50) with max drawdown 1.00% vs 1.00%"))
    assert promote.decide({**champ, "skill": 0.00004}, {**chal, "skill": 0.00001}, RULES) == ("killed", (
        "challenger skill +0.001% (net +0.00%, benchmark exposure 0.50) did not beat champion skill +0.004% (net "
        "+0.00%, benchmark exposure 0.50) by more than 0.00%"))
    by_return = {**RULES, "compare_on": "return"}
    assert promote.decide(champ, chal, by_return)[1].startswith("challenger net return +0.004% beat champion +0.001% with")
    assert promote.decide(chal, champ, by_return)[1] == ("challenger net return +0.001% did not beat champion +0.004% "
                                                         "by more than 0.00%")
    under = promote.decide({**champ, "skill": -0.00005}, {**chal, "skill": -0.00003}, RULES)
    assert under[0] == "killed" and under[1].startswith("challenger skill -0.003% beat the champion's -0.005% but not "
                                                        "the +0.000% floor: it did no better than holding the basket")
    past = promote.decide(champ, {**chal, "max_drawdown": -0.2}, RULES)
    assert past[0] == "killed" and past[1].endswith("although its skill was +0.003% ahead of the champion's")
    # figures that are plainly apart keep their two decimals
    plain = promote.decide({**champ, "skill": 0.01}, {**chal, "skill": 0.05}, RULES)[1]
    assert plain.startswith("challenger skill +5.00% (net +0.00%, benchmark exposure 0.50) beat champion skill +1.00% (")


def test_a_bar_is_written_out_in_full_however_small():
    assert promote._bar(1e-7, percent=True) == "0.00001%" and promote._bar(0.0000125) == "0.0000125"
    assert promote._bar(0.07, percent=True) == "7%" and promote._bar(0.999999, percent=True) == "99.9999%"
    assert promote._bar(0.0) == "0.0" and promote._bar(0.0, percent=True) == "0%"
    assert "e-" not in promote.early_kill({"return": -0.16}, {**RULES, "early_kill_drawdown": 1e-7}, basket_return=-0.05)


def test_one_fill_in_a_pair_is_one_fill(sandbox):
    tr = pd.DataFrame([{"ts": DAY, "pair": "BTC", "side": "buy", "qty": 1.0, "ref_price": 100.0, "notional": 100.0},
                       {"ts": DAY, "pair": "ETH", "side": "buy", "qty": 1.0, "ref_price": 100.0, "notional": 100.0},
                       {"ts": 2 * DAY, "pair": "ETH", "side": "sell", "qty": 1.0, "ref_price": 101.0, "notional": 101.0}])
    lines = report.per_pair_lines(tr, {"name": "champion", "positions": {"BTC": 1.0}})
    assert lines[0].startswith("- BTC: 1 fill (1 buy / 0 sell), traded 100, ")
    assert lines[1].startswith("- ETH: 2 fills (1 buy / 1 sell), traded 201, gross pnl +1.00, ")


def test_a_figure_too_small_to_show_is_not_printed_as_minus_nothing(sandbox):
    """In H5's first hour its return was the rounding of one equity cell, and
    the summary read "challenger3 -0.00% (max drawdown -0.00%"."""
    assert report._pct(-4e-10) == "+0.00%" and report._pct(4e-10) == "+0.00%" and report._pct(None) == "n/a"
    assert report._pct(-0.0001) == "-0.01%" and report._pct(0.0409) == "+4.09%"
    assert report._dd(-4e-10) == "0.00%" and report._dd(None) == "0.00%" and report._dd(-0.0512) == "-5.12%"
    said = promote.no_trade_of_its_own({"return": -4e-10, "trades": 8})
    assert said.endswith("so the +0.00% it shows is not from an exit it chose") and "-0.00%" not in said
    assert promote.no_trade_of_its_own({"return": -0.0008, "trades": 2}).endswith("so the -0.08% it shows is not from "
                                                                                 "an exit it chose")
    start_test(sandbox, STEADY)
    opened = 30 * DAY + 3600
    meta = slot.load("challenger1")
    first = float(pd.read_csv(sandbox / "state" / "champion" / "equity.csv").query("ts == @opened")["equity"].iloc[0])
    meta["started_at"], meta["start_equity"] = opened, {"champion": first + 4e-7, "challenger1": 10186.0}
    slot.save("challenger1", meta)
    champ = promote.paired_slot("challenger1", slot.load("challenger1"), opened + 600, RULES)[0]
    assert -1e-9 < champ["return"] < 0 and -1e-9 < champ["max_drawdown"] < 0     # a hair under nothing, as H5's was
    text = report.test_section(opened + 600)
    assert "-0.00%" not in text and "so far: champion +0.00% (max drawdown 0.00%, 0 fills)" in text


def test_a_trade_with_no_figure_does_not_leave_the_next_one_without(sandbox):
    """What is not known of one position says nothing of the next in the same pair."""
    rows = [(DAY, "BTC", "buy", 10, None), (2 * DAY, "BTC", "sell", 10, 110.0),
            (3 * DAY, "BTC", "buy", 10, 100.0), (4 * DAY, "BTC", "sell", 10, 105.0)]
    assert [t["pnl"] for t in promote.finished_trades(fills(rows))] == [None, pytest.approx(50.0)]
    # a crumb left by the first is carried into the second at the second's first price, known or not
    crumb = [(DAY, "BTC", "buy", 10, None), (2 * DAY, "BTC", "sell", 9.6, 110.0),
             (3 * DAY, "BTC", "buy", 10, 100.0), (4 * DAY, "BTC", "sell", 10.4, 105.0)]
    assert [t["pnl"] for t in promote.finished_trades(fills(crumb))] == [None, pytest.approx(10.4 * 105 - 10.4 * 100)]


# --- the rules file this repo ships -----------------------------------------------------------------------------

def test_the_rules_file_as_it_ships_is_read_without_a_word():
    """Every line of the real `challenger:` block is one the code reads and
    can use, no line is missing, and the values are the documented ones. A
    slip made while editing configs/risk.yaml fails here, before it ships."""
    body = config.load_yaml(Path(__file__).resolve().parents[2] / "configs" / "risk.yaml")
    st, wrong = promote.rule_settings(body["challenger"])
    assert wrong == []
    assert st == {**promote.DEFAULTS, "fast_pass": 2.0}                  # the one default that is "none" is set in the file
    assert set(body["challenger"]) == set(promote.KNOWN_SETTINGS)
    assert body["ruleset"] == 8 and st["two_from"] == promote.TWO_LOOKS_SINCE == 7 and st["retired"] == ("H0",)
    slots = body["challenger"]["slots"]
    assert isinstance(slots, int) and not isinstance(slots, bool) and slots >= 1
    assert body["backtest_gate"]["max_cost_drag"] == promote.GATE_COST_DRAG


# --- the seventh pass (2026-10-06): what the sixth round's fixes opened ------------------------------------------

def test_a_ruleset_in_quotes_did_not_change_during_the_test(sandbox):
    """The stamp on a test (7) was compared with the raw line ('7'), so under
    `ruleset: '7'` every block said "ruleset 7 at the start, 7 at this look:
    protected rules changed during the window"."""
    body = config.load_yaml(sandbox / "configs" / "risk.yaml")
    body["ruleset"] = "7"
    config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    assert "- Rules: ruleset 7 so far\n" in ledger(sandbox)
    assert promote._ruleset_note("challenger1") == "ruleset 7 throughout"
    meta = slot.load("challenger1")
    for stamp, said in (("7", "ruleset 7 throughout"), (7.0, "ruleset 7 throughout"),
                        (6, "ruleset 6 at the start, 7 at the verdict: protected rules changed during the window (see "
                            "the ruleset list in configs/risk.yaml)"),
                        ("seven", "the ruleset line could not be read when the test began; ruleset 7 at the verdict")):
        slot.save("challenger1", {**meta, "ruleset": stamp})
        assert promote._ruleset_note("challenger1") == said, stamp
    (sandbox / "state" / "challenger1" / "meta.json").write_text("{cut")
    assert promote._ruleset_note("challenger1", "at this look") == (
        "ruleset 7 at this look; the test's own record could not be read, so the ruleset it began under is not on record")


def test_a_test_whose_slot_record_cannot_be_read_can_still_be_voided(sandbox, capsys):
    """Once a slot record that cannot be read no longer stopped the run, a
    void request for that slot reached the verdict code, failed on the same
    file and was dropped: the request gone, nothing in the ledger, and the
    test still in its slot. That is a state a void is for. What runs in the
    slot is read from its config, and the void writes its record afresh."""
    two_tests(sandbox)
    meta1 = sandbox / "state" / "challenger1" / "meta.json"
    meta2 = sandbox / "state" / "challenger2" / "meta.json"
    meta1.write_text("{cut")
    meta2.write_text("{cut")
    config.dump_yaml(sandbox / "configs" / "void.yaml", {"requests": [
        {"slot": "challenger1", "hypothesis": "H5", "reason": "its slot record is beyond mending"},
        {"slot": "challenger2", "hypothesis": "H9", "reason": "the wrong name"}]})
    assert promote.main(["--now", str(at(30))]) == 0
    out, text = capsys.readouterr().out, ledger(sandbox)
    assert "challenger1: H5: voided" in out and "### Result H5: voided" in text
    assert ("- Rule: voided by Fin, not a verdict on the idea: its slot record is beyond mending. Its numbers so far could "
            "not be read (Unreadable: challenger1/meta.json cannot be read (JSONDecodeError") in text
    assert ("- Rules: ruleset 7 at the verdict; the test's own record could not be read, so the ruleset it began under is "
            "not on record") in text
    assert "- Status: voided" in text.split("## H5:")[1].split("\n## ")[0]
    assert slot.load("challenger1")["status"] == "idle" and not slot.configs_differ("challenger1")      # mended by the void
    # a request that does not name what the slot's config tests is dropped, and that record is left for a person
    assert ("void request H9 in challenger2: its slot record could not be read (JSONDecodeError) and its config tests H6; "
            "dropped") in out
    assert meta2.read_text() == "{cut" and "H9" not in text and "H6: voided" not in text
    # and a slot whose config is the champion's holds no test to void
    meta1.write_text("{cut")
    config.dump_yaml(sandbox / "configs" / "void.yaml", {"requests": [{"slot": "challenger1", "hypothesis": "H5", "reason": "again"}]})
    promote.main(["--now", str(at(31))])
    assert "its config is cash or the champion config; dropped" in capsys.readouterr().out
    assert ledger(sandbox).count("### Result H5: voided") == 1


def test_an_idle_slot_whose_record_cannot_be_read_is_still_moved_to_cash(sandbox, capsys):
    """Left with the old champion's config, it would open a "test" of the old
    champion as soon as its record was mended. A slot whose config is the
    champion's holds no test, whatever its record says or cannot say, and from
    ruleset 8 an idle slot holds cash."""
    start_test(sandbox, STRONG, ruleset=6)                               # an old test: promoted at its one look
    (sandbox / "state" / "challenger2").mkdir(parents=True, exist_ok=True)
    (sandbox / "state" / "challenger2" / "meta.json").write_text("{cut")
    assert not slot.configs_differ("challenger2")
    assert promote.main(["--now", str(at(60))]) == 0
    out = capsys.readouterr().out
    assert "### Result H5: promoted" in ledger(sandbox) and config.account_cfg("champion")["hypothesis"] == "H5"
    assert "idle slots moved to cash: challenger2" in out
    assert config.account_cfg("challenger2") == config.CASH_CFG and not slot.configs_differ("challenger2")
    # a slot with a config of its own is a test, and is never touched
    two_tests(sandbox)
    (sandbox / "state" / "challenger2" / "meta.json").write_text("{cut")
    assert promote.sync_idle_slots(config.strategy_signature(config.account_cfg("champion"))) == []
    assert config.account_cfg("challenger2")["hypothesis"] == "H6"


def test_read_it_with_care_is_said_only_when_the_figure_reads_above_its_start():
    """H4 on day 10: a daily skill t of +0.24 is 10.26%, above the starting
    10% by a hair and printed "10%". The line then read "10% ... (every idea
    starts at 10% ...). Read it with care"."""
    chal = {"skill_t": 0.24, "skill_days": 10, "trades": 10, "round_trips": 0, "return": 0.01}
    assert 0.10 < promote.confidence(0.24, 10, RULES) < 0.105
    line = promote.confidence_line(chal, RULES)
    assert line.startswith("10% that this is a real edge") and "Read it with care" not in line
    more = promote.confidence_line({**chal, "skill_t": 1.44, "skill_days": 30}, RULES)
    assert more.startswith("16% that this is a real edge") and "Read it with care: it has finished no trade of its own" in more


def test_the_fills_of_a_tests_first_hour_are_not_a_pace(sandbox):
    """H4 made ten fills in the hour it began and none after. Ten in ten days
    read as on course for sixty, so the summary said nothing of its fills
    until about day twenty."""
    said = report.fills_pace({"trades": 10, "trades_first_hour": 10}, RULES, 10.2, 120.0, one_look=True)
    assert said.startswith("10 in 10.2 days, all of them in the hour it began; at this pace about 10 by day 120, under "
                           "the 30 a promotion needs. ")
    said = report.fills_pace({"trades": 16, "trades_first_hour": 10}, RULES, 20.0, 120.0)
    assert said.startswith("16 in 20.0 days, 10 of them in the hour it began; at this pace about 28 by day 60, under the "
                           "30 a pass at the first look needs, and about 46 by day 120. ")
    assert report.fills_pace({"trades": 16, "trades_first_hour": 0}, RULES, 20.0, 120.0) is None       # 48 by day 60
    assert report.fills_pace({"trades": 16}, RULES, 20.0, 120.0) is None
    # and the count comes from the record: fills made in the run that began the test
    start_test(sandbox, STEADY)
    trades(sandbox, "challenger1", n=6)                                  # one fill a day, days 1 to 6
    meta = slot.load("challenger1")
    meta["started_at"] = 3 * DAY                                         # the third of them is made at that moment
    slot.save("challenger1", meta)
    chal = promote.paired_slot("challenger1", slot.load("challenger1"), at(30), RULES)[1]
    assert (chal["trades"], chal["trades_first_hour"]) == (4, 1)
    assert promote.window_metrics("champion", 3 * DAY, at(30), 10000.0)["trades_first_hour"] == 0
    assert "  fills: 4 in 27.1 days, 1 of them in the hour it began; at this pace about 14 by day 120, under the 30" \
        in report.test_section(at(30))
