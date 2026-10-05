"""PROTECTED. Pinned after the fifth review (2026-10-05): a record that has lost
rows, files the engine must not rewrite, the guard and a slot's own record not
stopping the hour, a void on a record that cannot be read, names of settings
with a slip in them, candles that lag or begin late, and the finer points of
what a finished trade made."""
import json
import math

import numpy as np
import pandas as pd
import pytest

from bot import config, data, paper, promote, report, shadow, slot

from .test_two_looks import (CHAMP, DAY, LOSING, RULES, STEADY, STRONG, at, equity, ledger,  # noqa: F401
                             sandbox, set_rules, start_test, trades)


def whole(root, name):
    """Give an account the file the engine keeps beside its records, agreeing with them."""
    adir = root / "state" / name
    eq = pd.read_csv(adir / "equity.csv")
    made = len(pd.read_csv(adir / "trades.csv")) if (adir / "trades.csv").exists() else 0
    (adir / "account.json").write_text(json.dumps({"cash": 1, "n_trades": made, "created_at": int(eq["ts"].iloc[0]),
                                                   "last_run_ts": int(eq["ts"].iloc[-1])}))


def fills(rows, columns=("ts", "pair", "side", "qty", "price", "notional", "fee", "reason")):
    """Fills as a frame. Each row: (ts, pair, side, qty, price), with notional = qty * price and no fee."""
    out = [{"ts": ts, "pair": pair, "side": side, "qty": qty, "price": price,
            "notional": qty * price if price is not None else None, "fee": 0.0, "reason": ""}
           for ts, pair, side, qty, price in rows]
    return pd.DataFrame(out)[list(columns)]


# --- the engine does not rewrite what it did not write -------------------------------------------------------

def test_the_engine_does_not_rewrite_a_file_that_has_lost_its_header(tmp_path):
    """The schema migration rewrote any file whose first line was not today's
    header. For a file that had lost its header that blanked every row, and
    what the verdict code then read was an account with one hour of record."""
    p = tmp_path / "acct" / "equity.csv"
    row = {"ts": 1, "equity": 100.0, "cash": 50.0, "gross_exposure": 50.0, "n_positions": 1, "fees_paid": 0.1,
           "slippage_paid": 0.0}
    paper.append_rows(p, paper.EQUITY_FIELDS, [row, {**row, "ts": 2, "equity": 101.0}])
    text = p.read_text()
    for damaged in (text.split("\n", 1)[1], "", "ts,ts,equity\n1,1,100\n", "when,worth\n1,100\n"):
        p.write_text(damaged)
        with pytest.raises(ValueError, match="acct/equity.csv does not begin with a header this code wrote"):
            paper.append_rows(p, paper.EQUITY_FIELDS, [{**row, "ts": 3}])
        assert p.read_text() == damaged                                  # left exactly as it was found
    # a header from an older version of this code is still brought up to date, its rows kept
    p.write_text("ts,equity\n1,100.0\n2,101.0\n")
    paper.append_rows(p, paper.EQUITY_FIELDS, [{**row, "ts": 3, "equity": 102.0}])
    got = pd.read_csv(p)
    assert list(got.columns) == paper.EQUITY_FIELDS and list(got["equity"]) == [100.0, 101.0, 102.0]


# --- a record that has lost rows --------------------------------------------------------------------------------

def test_an_accounts_files_are_set_against_its_own_counts(sandbox):
    start_test(sandbox, STEADY)
    adir = sandbox / "state" / "challenger1"
    whole(sandbox, "challenger1")
    assert promote.record_fault("challenger1") is None
    eq_text, tr_text = (adir / "equity.csv").read_text(), (adir / "trades.csv").read_text()
    eq_rows, tr_rows = eq_text.strip().split("\n"), tr_text.strip().split("\n")

    def with_files(eq=None, tr=None):
        (adir / "equity.csv").write_text(eq_text if eq is None else "\n".join(eq) + "\n")
        (adir / "trades.csv").write_text(tr_text if tr is None else "\n".join(tr) + "\n")
        return promote.record_fault("challenger1")

    assert with_files(tr=tr_rows[:-3]) == ("challenger1/trades.csv has 37 rows and the account has made 40 fills: "
                                           "rows have been lost or added")
    assert with_files(tr=tr_rows[:2]) == ("challenger1/trades.csv has 1 row and the account has made 40 fills: "
                                          "rows have been lost or added")
    assert with_files(tr=tr_rows + tr_rows[-1:]).startswith("challenger1/trades.csv has 41 rows and")
    assert with_files(eq=eq_rows[:1] + eq_rows[2:]) == ("challenger1/equity.csv does not begin at the account's "
                                                        "first run: rows have been lost from its start")
    assert with_files(eq=eq_rows[:-1]) == "challenger1/equity.csv does not end at the account's last run"
    assert with_files(eq=eq_rows + eq_rows[5:6]) == "challenger1/equity.csv is not in time order"
    blank = eq_rows[7].split(",")
    blank[1] = ""
    one = "challenger1/equity.csv has 1 row that is not a reading (a time, an equity, an exposure and costs, each a number)"
    assert with_files(eq=eq_rows[:7] + [",".join(blank)] + eq_rows[8:]) == one
    # A row cut short that still ends its line: "2595600,101" has a time and an equity that are numbers (the
    # equity was 10,100 and reads 101, a fall of 99%), and the count of rows is right. Its other cells are blank.
    cut = ",".join(eq_rows[7].split(",")[:2])[:-3]
    assert with_files(eq=eq_rows[:7] + [cut] + eq_rows[8:]) == one
    for cell in (3, 5, 6):                                               # the exposure, the fees, the slippage
        cells = eq_rows[7].split(",")
        cells[cell] = ""
        assert with_files(eq=eq_rows[:7] + [",".join(cells)] + eq_rows[8:]) == one, cell
    for cell in (2, 4):                                                  # cash and the count of positions are not read
        cells = eq_rows[7].split(",")
        cells[cell] = ""
        assert with_files(eq=eq_rows[:7] + [",".join(cells)] + eq_rows[8:]) is None, cell
    assert with_files(eq=eq_rows[:7] + [",".join(blank)] + eq_rows[8:10] + [",".join(blank)] + eq_rows[11:]).startswith(
        "challenger1/equity.csv has 2 rows that are not a reading (")
    assert with_files(eq=eq_rows[:1]) == "challenger1/equity.csv has no rows and the account has run"
    assert with_files(eq=eq_rows[:5] + eq_rows[60:]) is None             # hours the bot did not run are not damage
    with pytest.raises(promote.Unreadable, match="has rows and no ts or equity column"):
        with_files(eq=eq_rows[1:])
    assert with_files() is None
    (adir / "account.json").write_text("{not json")
    assert promote.record_fault("challenger1") == "challenger1/account.json cannot be read (JSONDecodeError)"
    (adir / "account.json").write_text("[1, 2]")
    assert promote.record_fault("challenger1") == "challenger1/account.json is not an account record"
    (adir / "account.json").write_text(json.dumps({"cash": 1}))          # no counts: nothing to set the files against
    assert with_files(tr=tr_rows[:2], eq=eq_rows[:1] + eq_rows[9:]) is None
    (adir / "account.json").unlink()
    assert with_files(tr=tr_rows[:2], eq=eq_rows[:1] + eq_rows[9:]) is None


def test_nothing_is_ruled_on_a_record_that_has_lost_rows(sandbox, capsys):
    """A file that has lost rows still parses. A test that had made forty fills
    read as one that had made one and was killed for having "finished no trade
    of its own"; a champion whose equity rows had gone read as never having
    had a drawdown, and a challenger that passed on the whole record was
    killed on the guard that then tightened."""
    start_test(sandbox, STRONG, champion_returns=[-0.012, 0.011] * 60)
    for name in ("champion", "challenger1"):
        whole(sandbox, name)
    tr_file, champ_file = sandbox / "state" / "challenger1" / "trades.csv", sandbox / "state" / "champion" / "equity.csv"
    tr_text, champ_text = tr_file.read_text(), champ_file.read_text()
    tr_file.write_text("\n".join(tr_text.split("\n")[:1] + tr_text.strip().split("\n")[-1:]) + "\n")
    assert promote.main(["--now", str(at(60))]) == 0
    assert "WARNING: challenger1: H5 could not be looked at this hour (Unreadable: challenger1/trades.csv has 1 row and " \
           "the account has made 40 fills: rows have been lost or added); nothing is ruled for it until its record " \
           "can be read" in capsys.readouterr().out
    assert "### " not in ledger(sandbox) and slot.load("challenger1")["status"] == "testing"
    assert "its record could not be read this hour (Unreadable: challenger1/trades.csv has 1 row" in report.test_section(at(60))
    tr_file.write_text(tr_text)
    rows = champ_text.strip().split("\n")
    champ_file.write_text("\n".join(rows[:1] + rows[-70:]) + "\n")       # the champion's first fifty days are gone
    assert promote.main(["--now", str(at(60))]) == 0
    assert "(Unreadable: champion/equity.csv does not begin at the account's first run: rows have been lost from its " \
           "start)" in capsys.readouterr().out
    assert "### " not in ledger(sandbox)
    champ_file.write_text(champ_text)
    assert promote.main(["--now", str(at(60))]) == 0                     # mended: the look that was due is taken
    assert "### Result H5: promoted" in ledger(sandbox)


def test_the_newest_reading_is_the_latest_in_time_not_the_last_line(sandbox):
    """An old row copied to the end of the file was read as the newest
    reading: a test that was up read as down 20% and was ended early."""
    start_test(sandbox, STEADY)
    p = sandbox / "state" / "challenger1" / "equity.csv"
    true = promote.window_metrics("challenger1", 0, at(60), 10000.0)["return"]
    rows = p.read_text().strip().split("\n")
    old = rows[3].split(",")
    old[1] = "8000.0"
    p.write_text("\n".join(rows + [",".join(old)]) + "\n")
    (sandbox / "state" / "challenger1" / "account.json").unlink()        # with nothing to set the record against
    got = promote.window_metrics("challenger1", 0, at(60), 10000.0)
    assert got["return"] == pytest.approx(true) and got["max_drawdown"] < -0.19    # the low is still in the path
    assert promote.current_equities(at(60))["challenger1"] == pytest.approx(10000.0 * (1 + true))
    whole(sandbox, "challenger1")                                        # and with the account's file, it is a fault
    assert promote.record_fault("challenger1") == "challenger1/equity.csv is not in time order"


def test_the_newest_equity_is_the_last_cell_that_is_a_number_and_not_a_later_hour(sandbox):
    start_test(sandbox, STEADY)
    p = sandbox / "state" / "challenger1" / "equity.csv"
    eq = pd.read_csv(p)
    want = float(eq.loc[eq["ts"] == 59 * DAY + 3600, "equity"].iloc[0])
    eq["equity"] = eq["equity"].astype(object)
    eq.loc[eq["ts"] == 60 * DAY + 3600, "equity"] = ""                   # the hour's own cell is blank
    eq.to_csv(p, index=False)
    assert promote.current_equities(at(60))["challenger1"] == pytest.approx(want)   # not blank, and not day 120's


# --- what stops the hour, and what must not ---------------------------------------------------------------------

def two_tests(root):
    """H5 in slot 1 and H6 in slot 2, both under ruleset 7 with whole records."""
    start_test(root, STEADY)
    config.dump_yaml(root / "configs" / "challenger2.yaml",
                     {"hypothesis": "H6", "strategy": "mean_reversion", "params": {"window_hours": 240}})
    (root / "LEDGER.md").write_text(ledger(root) + "\n## H6: another\n- Expected gross bps per round trip: 90\n"
                                                   "- Status: testing\n")
    slot.save("challenger2", {"status": "testing", "hypothesis": "H6", "started_at": 0, "ruleset": 7,
                              "start_equity": {"champion": 10000.0, "challenger2": 10000.0}})
    equity(root, "challenger2", STEADY)
    trades(root, "challenger2")


def test_the_guards_own_record_does_not_stop_the_slots_rulings(sandbox, capsys):
    """rule_on_shadow ran with nothing round it. With the guard due and one of
    its files cut to nothing, the hour stopped there every hour: no look for
    any slot, no void, no summary and no commit."""
    start_test(sandbox, STEADY)
    shadow.start(config.account_cfg("champion"), "H9", 0, 10000.0, 10000.0)
    equity(sandbox, "shadow", STEADY)
    (sandbox / "state" / "shadow" / "trades.csv").write_text("")
    assert promote.main(["--now", str(at(60))]) == 0
    out = capsys.readouterr().out
    assert "WARNING: the shadow guard could not be ruled on this hour (Unreadable: shadow/trades.csv cannot be read" in out
    assert "### First look H5: passed" in ledger(sandbox)                # the slot's look was still taken
    assert shadow.load()["status"] == "active"                           # and the guard is still there to be ruled on
    (sandbox / "state" / "shadow" / "meta.json").write_text("{cut short")
    assert promote.main(["--now", str(at(61))]) == 0
    assert "the shadow guard could not be ruled on this hour (JSONDecodeError" in capsys.readouterr().out
    assert "shadow: its record could not be read this hour" in report.test_section(at(61))


def test_one_slots_own_record_does_not_stop_the_others_or_the_lines_printed_before_the_commit(sandbox, capsys):
    two_tests(sandbox)
    meta_file = sandbox / "state" / "challenger1" / "meta.json"
    for damaged, how in (("", "JSONDecodeError"), ("{cut", "JSONDecodeError"), ("[]", "ValueError: it is not a slot record"),
                         ("null", "ValueError: it is not a slot record"), ('"testing"', "ValueError: it is not a slot record")):
        meta_file.write_text(damaged)
        assert promote.main(["--now", str(at(60))]) == 0
        assert f"WARNING: challenger1: its slot record (meta.json) could not be read this hour ({how}" in capsys.readouterr().out
        text = report.test_section(at(60))
        assert "- challenger1: its record could not be read this hour" in text and "challenger2: testing H6" in text
        lines = slot.describe(at(60)).split("\n")                        # printed in the workflow's Summary step
        assert lines[0].startswith("challenger1: its slot record could not be read (") and "testing H6" in lines[1]
        assert slot.free_slots() == []                                   # a slot that cannot be read is not free
    assert "### First look H6: passed" in ledger(sandbox) and "H5:" not in ledger(sandbox).split("## Results")[1]
    # a start that is not a time: the slot line says so and does not raise
    meta_file.write_text(json.dumps({"status": "testing", "hypothesis": "H5", "started_at": "soon", "start_equity": {}}))
    assert slot.describe(at(60)).split("\n")[0].startswith("challenger1: its slot record could not be read (ValueError")


def test_between_the_looks_nothing_is_said_to_be_due(sandbox, capsys):
    """On day 75, with a pair's candles behind, the log said the test "is due
    a ruling". None is due between the looks."""
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox)
    capsys.readouterr()
    (sandbox / "state" / "candles" / "BTC.csv").unlink()
    getattr(data, "_READ_CACHE", {}).clear()
    promote.main(["--now", str(at(75))])
    out = capsys.readouterr().out
    assert "due a ruling" not in out and "on day 75.1 of 120, past its first look; no verdict yet" in out


# --- settings ---------------------------------------------------------------------------------------------------

def test_a_line_this_code_does_not_read_is_said_to_do_nothing():
    st, wrong = promote.rule_settings({**RULES, "min_active": 0.01, "confidence": {"prior": 0.1, "edge_sharpe": 1.5,
                                                                                  "prier": 0.5}})
    assert wrong == ["challenger.min_active is not a setting this code reads; nothing uses it",
                     "challenger.confidence.prier is not a setting this code reads; nothing uses it"]
    assert st["prior"] == 0.1


def test_a_slip_in_a_lines_name_does_not_switch_the_rule_off(sandbox, capsys):
    """`two_looks_from_rulset: 7` was a line this code did not know and a
    setting that was not there, and "not there" meant off: a new test went
    back on the one look rule with nothing said, and a thin pass (t of 0.4)
    was promoted at day 60. The same slip dropped the floor under skill,
    switched the early kill off, and made the rule compare raw return. A
    line that is not there now means its documented value."""
    set_rules(sandbox, two_looks_from_ruleset=None, two_looks_from_rulset=7)
    start_test(sandbox, [0.0062, -0.0058] * 60)                          # thin: passes, with a t of about 0.4
    rules = config.risk_cfg()["challenger"]
    assert promote.two_looks(slot.load("challenger1"), rules)
    promote.main(["--now", str(at(60))])
    assert "### First look H5: passed" in ledger(sandbox) and "### Result H5" not in ledger(sandbox)
    out = capsys.readouterr().out
    assert "WARNING: challenger.two_looks_from_rulset is not a setting this code reads; nothing uses it" in out
    assert "WARNING: challenger.two_looks_from_ruleset is not in the file; ruleset 7 stands in (to switch the rule " \
           "off, write `off`)" in out
    text = report.test_section(at(60))
    assert "- SETTING NOT USED: challenger.two_looks_from_rulset is not a setting this code reads" in text
    assert "- SETTING NOT USED: challenger.two_looks_from_ruleset is not in the file; ruleset 7 stands in" in text


def test_the_early_kill_is_not_switched_off_by_a_line_under_another_name(sandbox):
    set_rules(sandbox, early_kill_drawdown=None, early_kill=0.15)
    start_test(sandbox, [-0.02] * 10 + [0.0] * 110)                      # down 18% by day 10 in a flat market
    promote.main(["--now", str(at(20))])
    assert "### Result H5: killed" in ledger(sandbox) and "past the 15% early kill limit" in ledger(sandbox)


def test_off_is_how_a_rule_is_switched_off(sandbox):
    (sandbox / "configs" / "risk.yaml").write_text(
        (sandbox / "configs" / "risk.yaml").read_text().replace("early_kill_drawdown: 0.15", "early_kill_drawdown: off"))
    rules = config.risk_cfg()["challenger"]
    assert rules["early_kill_drawdown"] is False and promote.rule_settings(rules) == (
        {**promote.rule_settings(RULES)[0], "early_kill": 0.0}, [])
    start_test(sandbox, [-0.02] * 10 + [0.0] * 110)
    promote.main(["--now", str(at(20))])
    assert "### " not in ledger(sandbox)                                 # no early kill, and nothing said about it
    assert "SETTING NOT USED" not in report.test_section(at(20))


@pytest.mark.parametrize("line", [None, "", "seven", float("nan"), True])
def test_a_ruleset_line_that_cannot_be_read_does_not_put_a_new_test_on_the_old_rule(sandbox, capsys, line):
    """A test with no stamp is one from before rulesets existed and keeps its
    one look. With `ruleset:` left blank a test that began today was stamped
    with nothing, read as old, and promoted at day 60 on a t of 0.4."""
    body = config.load_yaml(sandbox / "configs" / "risk.yaml")
    body["ruleset"] = line
    config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
    assert config.ruleset_stamp() == "unreadable"
    equity(sandbox, "champion", CHAMP)
    equity(sandbox, "challenger1", [0.0062, -0.0058] * 60)
    trades(sandbox, "challenger1")
    started = slot.maybe_start(0, {"champion": 10000.0, "challenger1": 10000.0})["challenger1"]
    assert started["status"] == "testing" and started["ruleset"] == "unreadable"
    assert promote.two_looks(started, RULES)
    assert len(promote.other_notes()) == 1 and promote.other_notes()[0].endswith(
        "which cannot be used; a test that starts while it is so is stamped `unreadable` and is judged as one begun "
        "under the newest rules (two looks)")
    assert "- SETTING NOT USED: ruleset is " in report.test_section(at(30))
    promote.restart("challenger2", at(30), {"champion": 1.0, "challenger2": 1.0}, "H9")
    assert slot.load("challenger2")["ruleset"] == "unreadable"
    shadow.start(config.account_cfg("champion"), "H9", 0, 1.0, 1.0)
    assert shadow.load()["ruleset"] == "unreadable"
    shadow.stop("held")
    promote.main(["--now", str(at(60))])
    text = ledger(sandbox)
    assert "### First look H5: passed" in text and "### Result H5" not in text
    assert "- Rules: the ruleset line in configs/risk.yaml cannot be read, so the rules this ran under are not on record" in text
    assert "WARNING: ruleset is " in capsys.readouterr().out
    body["ruleset"] = 7                                                   # mended before the verdict
    config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
    promote.main(["--now", str(at(120))])
    assert "- Rules: the ruleset line could not be read when the test began; ruleset 7 at the verdict" in ledger(sandbox)


def test_a_ruleset_line_that_is_a_number_is_stamped_as_it_is(sandbox):
    assert config.ruleset_stamp() == 7 and promote.other_notes() == []


def test_the_cost_kill_keeps_working_when_the_gates_cost_line_cannot_be_read(sandbox):
    """`max_cost_drag: 15%` is text. The cost kill multiplies that line, so it
    was simply off, and nothing said so."""
    body = config.load_yaml(sandbox / "configs" / "risk.yaml")
    assert promote.gate_cost_drag() == (0.15, None) and promote.other_notes() == []
    for written, limit, note in ((0.15, 0.15, None), (0.2, 0.2, None), (1, 1.0, None),
                                 ("15%", 0.15, "backtest_gate.max_cost_drag is '15%', which cannot be used; 15% stands "
                                               "in for the cost kill"),
                                 (None, 0.15, "backtest_gate.max_cost_drag is None, which cannot be used; 15% stands in "
                                              "for the cost kill"),
                                 (15, 0.15, "backtest_gate.max_cost_drag is 15, which cannot be used; 15% stands in for "
                                            "the cost kill"),              # a share of equity: 15 would be 1,500%
                                 (0, 0.15, "backtest_gate.max_cost_drag is 0, which cannot be used; 15% stands in for "
                                           "the cost kill"),
                                 (-1, 0.15, "backtest_gate.max_cost_drag is -1, which cannot be used; 15% stands in for "
                                            "the cost kill")):
        body["backtest_gate"] = {"max_cost_drag": written}
        config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
        assert promote.gate_cost_drag() == (limit, note)
        assert promote.other_notes() == ([note] if note else [])
    missing = "backtest_gate.max_cost_drag is not in the file; 15% stands in for the cost kill"
    for block in ({"max_cost_drg": 0.15}, None, "text"):                 # a slip in its name, no block, not a block
        body["backtest_gate"] = block
        config.dump_yaml(sandbox / "configs" / "risk.yaml", body)
        assert promote.gate_cost_drag() == (0.15, missing) and promote.other_notes() == [missing]
    # and the kill is made on it: costs at 60% of equity a year, four times the 15% that stands in
    start_test(sandbox, STEADY)
    p = sandbox / "state" / "challenger1" / "equity.csv"
    eq = pd.read_csv(p)
    eq["fees_paid"] = 16.5 * (eq["ts"] // DAY)
    eq.to_csv(p, index=False)
    promote.main(["--now", str(at(20))])
    assert "### Result H5: killed" in ledger(sandbox) and "a fees treadmill" in ledger(sandbox)


def test_the_shadow_line_reads_the_window_through_the_checked_settings(sandbox):
    """shadow.describe read window_days with a bare float(). Written "sixty",
    it took the whole slots section of the summary with it."""
    set_rules(sandbox, window_days="sixty")
    start_test(sandbox, STEADY)
    shadow.start(config.account_cfg("champion"), "H9", 0, 10000.0, 10000.0)
    assert "day 30.1 of 60; the promotion is reverted if it wins" in shadow.describe(at(30))
    text = report.test_section(at(30))
    assert "challenger1: testing H5" in text and "- shadow: H0 (deposed by H9)" in text
    assert "- SETTING NOT USED: challenger.window_days is 'sixty', which cannot be used; 60 days stand in" in text
    # and when the guard's ruling is due and has not come, the line says so
    assert "day 61.1 of 60 (its ruling is due: made at the next hourly run for which the market data and both records " \
           "are whole); the promotion is reverted if it wins" in shadow.describe(at(61))


@pytest.mark.parametrize("key,written,name,stands_in", [
    ("min_trades", 30.5, "min_trades", 30), ("early_kill_drawdown", 1.5, "early_kill", 0.15),
    ("early_kill_drawdown", -0.1, "early_kill", 0.15), ("treadmill_kill_multiple", -3, "treadmill_multiple", 3.0),
    ("max_dd_floor", 1.2, "max_dd_floor", 0.10), ("max_dd_floor", -0.1, "max_dd_floor", 0.10),
    ("max_dd_ratio", -1, "max_dd_ratio", 1.5), ("window_days", -60, "window_days", 60.0),
    ("confirm_days", -60, "confirm_days", 60.0),
])
def test_a_number_outside_what_a_setting_can_be_is_not_used(key, written, name, stands_in):
    st, wrong = promote.rule_settings({**RULES, key: written})
    assert st[name] == stands_in and len(wrong) == 1 and wrong[0].startswith(f"challenger.{key} is {written!r}, which")


# --- candles ------------------------------------------------------------------------------------------------------

def three_pairs(root):
    body = config.load_yaml(root / "configs" / "risk.yaml")
    body["pairs"] = ["BTC", "ETH", "SOL"]
    config.dump_yaml(root / "configs" / "risk.yaml", body)
    flat = pd.read_csv(root / "state" / "candles" / "BTC.csv")
    for pair in ("ETH", "SOL"):
        flat.to_csv(root / "state" / "candles" / f"{pair}.csv", index=False)
    getattr(data, "_READ_CACHE", {}).clear()


def test_pairs_whose_candles_begin_late_are_not_left_out_of_the_market_without_a_word(sandbox, capsys):
    """A pair whose candles begin more than a day into the window is left out
    of the basket. That was done after the missing pairs had been listed, so
    two rising pairs with their first two days gone left a basket of the one
    flat pair, with no gap reported, and a kill became a promotion."""
    three_pairs(sandbox)
    start_test(sandbox, STEADY)
    for pair in ("ETH", "SOL"):
        p = sandbox / "state" / "candles" / f"{pair}.csv"
        c = pd.read_csv(p)
        c[c["time"] >= 49 * 3600].to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert mc["late"] == ["ETH", "SOL"] and mc["missing"] == [] and mc["pairs"] == 1
    assert mc["gap"] == "the candles for ETH, SOL begin more than a day into its window" and chal["skill"] is None
    promote.main(["--now", str(at(60))])
    assert "### " not in ledger(sandbox)
    assert "is due a ruling on day 60.1 but the candles for ETH, SOL begin more than a day into its window" \
           in capsys.readouterr().out
    # a pair that begins a few hours in is still measured, from where it begins
    for pair in ("ETH", "SOL"):
        c = pd.read_csv(sandbox / "state" / "candles" / "BTC.csv")
        c[c["time"] >= 5 * 3600].to_csv(sandbox / "state" / "candles" / f"{pair}.csv", index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[2]
    assert mc["late"] == [] and mc["gap"] is None and mc["pairs"] == 3


def test_a_candle_file_that_cannot_be_read_is_said_to_be_that(sandbox, capsys):
    start_test(sandbox, STEADY)
    (sandbox / "state" / "candles" / "BTC.csv").write_text("time,close\n\"cut")
    getattr(data, "_READ_CACHE", {}).clear()
    mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)[2]
    assert mc["gap"].startswith("the candles for its window could not be read (")
    promote.main(["--now", str(at(60))])
    assert "### " not in ledger(sandbox) and "the candles for its window could not be read" in capsys.readouterr().out


def test_the_early_kill_waits_when_a_pair_is_one_failed_fetch_behind(sandbox, capsys):
    """The account is valued at this hour's quotes. Set against a basket in
    which two of three pairs were one failed fetch behind in a market falling
    3% an hour, a test that had lost less than the market was ended for
    losing more (the limit was six hours, then two; one fetch is 1.4)."""
    three_pairs(sandbox)
    start_test(sandbox, [-0.02] * 10 + [0.0] * 110)                      # down 18% by day 10
    p = sandbox / "state" / "candles" / "ETH.csv"
    eth = pd.read_csv(p)
    eth[eth["time"] + 3600 <= at(20) - 3600].to_csv(p, index=False)      # its newest close is the hour before
    getattr(data, "_READ_CACHE", {}).clear()
    promote.main(["--now", str(at(20) + 25 * 60)])
    out = capsys.readouterr().out
    assert "### " not in ledger(sandbox)
    assert "WARNING: challenger1: H5 has lost 18.29% since its test began, past the early kill limit, but the candles " \
           "for ETH stop before the one that closed at the top of this hour, so it cannot be said whether the market " \
           "lost more; no early kill this hour" in out
    eth.to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    promote.main(["--now", str(at(20) + 25 * 60)])
    assert "### Result H5: killed" in ledger(sandbox) and "past the 15% early kill limit" in ledger(sandbox)


def test_candles_that_begin_late_for_every_pair_are_a_gap_too(sandbox, capsys):
    """"Late" was measured from the earliest pair, so when every pair began
    ten days in, none was late: the basket covered only the end of the window
    and a test that should have been killed passed its first look. That is
    what a candle cache that has been lost and fetched again looks like."""
    three_pairs(sandbox)
    start_test(sandbox, STEADY)
    for pair in ("BTC", "ETH", "SOL"):
        p = sandbox / "state" / "candles" / f"{pair}.csv"
        c = pd.read_csv(p)
        c[c["time"] >= 10 * DAY].to_csv(p, index=False)
    getattr(data, "_READ_CACHE", {}).clear()
    champ, chal, mc = promote.paired_slot("challenger1", slot.load("challenger1"), at(60), RULES)
    assert mc["late"] == ["BTC", "ETH", "SOL"] and chal["skill"] is None
    assert mc["gap"] == "the candles for BTC, ETH, SOL begin more than a day into its window"
    promote.main(["--now", str(at(60))])
    assert "### " not in ledger(sandbox) and "begin more than a day into its window" in capsys.readouterr().out
    # a window that opened less than a day ago cannot have a pair that is a day late
    assert promote.market_context(59 * DAY + 3600, at(60), ["BTC", "ETH", "SOL"])["late"] == []


# --- sentences ------------------------------------------------------------------------------------------------------

def test_bars_and_limits_are_printed_as_they_are_written():
    assert [promote._bar(x) for x in (1.0, 2.0, 1.25, 0.5, 1.05)] == ["1.0", "2.0", "1.25", "0.5", "1.05"]
    assert [promote._bar(x, percent=True) for x in (0.15, 0.125, 0.1, 0.0)] == ["15%", "12.5%", "10%", "0%"]
    chal = {"return": -0.16, "skill": 0.05, "skill_t": 1.3, "skill_days": 60}
    assert "past the 12.5% early kill limit" in promote.early_kill(chal, {**RULES, "early_kill_drawdown": 0.125},
                                                                   basket_return=-0.05)
    assert "at or above the 1.25 fast pass bar" in promote.fast_pass({**chal, "skill_t": 1.3},
                                                                     {**RULES, "fast_pass_skill_t": 1.25})
    champ = {"return": 0.0, "max_drawdown": -0.01, "trades": 40, "round_trips": 5, "skill": 0.0, "skill_exposure": 0.5}
    good = {"return": 0.05, "max_drawdown": -0.01, "trades": 40, "round_trips": 5, "skill": 0.05, "skill_exposure": 0.5,
            "skill_basis": "usual", "edge_t": None, "skill_t": 1.3, "skill_days": 120, "trade_profit": 0.01}
    assert promote.decide_final(champ, good, {**RULES, "min_skill_t": 1.25})[1].endswith("at or above the 1.25 bar")


def test_a_figure_next_to_its_bar_is_printed_with_enough_decimals_to_tell_them_apart():
    champ = {"return": 0.0, "max_drawdown": -0.01}
    said = promote.drawdown_guard(champ, {"max_drawdown": -0.100004}, RULES)
    assert said.startswith("challenger max drawdown 10.0004% exceeded the limit 10.0000% (the larger of 1.5x the "
                           "champion's 1.00% and the 10% floor)")
    assert promote.drawdown_guard(champ, {"max_drawdown": -0.10}, RULES) is None              # at the limit is inside it
    assert promote.drawdown_guard(champ, {"max_drawdown": -0.25}, RULES).startswith("challenger max drawdown 25.00% "
                                                                                    "exceeded the limit 10.00%")
    kill = promote.early_kill({"return": -0.150004}, RULES, basket_return=-0.02)
    assert kill.startswith("challenger has lost 15.0004% since its test began, past the 15% early kill limit")
    kill = promote.early_kill({"return": -0.2000004}, RULES, basket_return=-0.2)
    assert "has lost 20.00004% since its test began" in kill and "(the basket lost 20.00000%)" in kill
    kill = promote.early_kill({"return": -0.2}, RULES, basket_return=0.031)
    assert "has lost 20.00% since" in kill and "(the basket made 3.10%)" in kill
    assert promote.early_kill({"return": -0.15}, RULES, basket_return=-0.02) is None           # at the limit is not past it
    assert promote.early_kill({"return": -0.2}, RULES, basket_return=-0.2) is None             # level with the market


def test_an_edge_equal_to_the_bar_is_not_more_than_it():
    # in numbers a float holds exactly: 0.03 - 0.01 comes out a hair under 0.02 and proves nothing
    champ = {"return": 0.25, "max_drawdown": -0.01, "trades": 40, "skill": 0.25, "skill_exposure": 0.5}
    chal = {"return": 0.5, "max_drawdown": -0.01, "trades": 40, "skill": 0.5, "skill_exposure": 0.5,
            "skill_basis": "usual", "edge_t": None}
    rules = {**RULES, "min_return_edge": 0.25}
    assert promote.decide(champ, chal, rules)[0] == "killed"
    assert promote.decide(champ, {**chal, "skill": 0.5001}, rules)[0] == "promoted"
    by_return = {**rules, "compare_on": "return"}
    assert promote.decide(champ, chal, by_return)[0] == "killed"
    assert promote.decide(champ, {**chal, "return": 0.5001}, by_return)[0] == "promoted"
    # and level with the champion is not ahead of it when no edge is asked for
    level = {**chal, "skill": 0.25, "return": 0.25}
    assert promote.decide(champ, level, RULES)[0] == "killed"
    assert promote.decide(champ, level, {**RULES, "compare_on": "return"})[0] == "killed"


def test_what_one_word_says_for_one_and_for_many(sandbox):
    start_test(sandbox, STEADY)
    trades(sandbox, "challenger1", n=1, sides=("buy",))
    text = report.test_section(at(30))
    assert "vs challenger1 +1.85% (max drawdown -0.25%, 1 fill)" in text and "none of its 1 fill closed" in text
    assert "champion -0.64% (max drawdown -0.64%, 0 fills)" in text
    assert "equal weight basket of 1 pair +0.00%" in text


def test_a_first_look_block_does_not_speak_of_a_verdict(sandbox):
    start_test(sandbox, STEADY)
    promote.main(["--now", str(at(60))])
    block = ledger(sandbox)[ledger(sandbox).index("### First look H5"):]
    assert "- Rules: ruleset 7 so far\n" in block
    promote.main(["--now", str(at(120))])
    assert "- Rules: ruleset 7 throughout\n" in ledger(sandbox)[ledger(sandbox).index("### Result H5"):]
    start_test(sandbox, STEADY, ruleset=None)
    (sandbox / "LEDGER.md").write_text("# Ledger\n\n## H5: again\n- Expected gross bps per round trip: 150\n"
                                       "- Status: testing\n")
    trades(sandbox, "challenger1", n=6)                                  # an old test, kept on value at its one look
    promote.main(["--now", str(at(60))])
    assert "- Rules: ruleset 7 at this look; the test began before rulesets were stamped" in ledger(sandbox)


def test_the_summary_in_the_hour_of_a_restart_does_not_call_a_new_window_damaged(sandbox):
    """A test restarted against a new champion begins its window after the
    hour's readings were written. The summary called that "no usable equity
    record", which is the line the daily agent passes on as damage."""
    start_test(sandbox, STEADY)
    now = at(40)
    promote.restart("challenger1", now, {"champion": 10000.0, "challenger1": 10000.0}, "H9")
    text = report.test_section(now)
    assert "  no reading yet: its window opened this hour, and the first reading in it is written at the next run" in text
    assert "no reading this hour" not in text
    # two hours on with still no reading in the window (this sandbox writes one a day), it is said as damage
    assert "no reading this hour: there is no usable equity record for challenger1" in report.test_section(now + 7200)
    later = report.test_section(at(42))                                  # and once readings are there, nothing is said
    assert "no reading this hour" not in later and "no reading yet" not in later and "  confidence: " in later


def test_the_measured_reading_is_left_out_when_there_is_nothing_to_measure(sandbox):
    start_test(sandbox, STEADY, ruleset=6)
    assert "two look rule (measured, not applied to this test): " in report.test_section(at(30))
    set_rules(sandbox, two_looks_from_ruleset=False)                     # the two look rule switched off: no reading of it
    assert "two look rule (measured" not in report.test_section(at(30))
    set_rules(sandbox)
    p = sandbox / "state" / "challenger1" / "equity.csv"
    p.write_text(p.read_text().split("\n", 1)[0] + "\n")                 # no equity reading: nothing to read the rule on
    text = report.test_section(at(30))
    assert "two look rule (measured" not in text and "no reading this hour: there is no usable equity record" in text


def test_the_measured_reading_for_an_old_test_whose_look_is_overdue(sandbox):
    champ = {"return": 0.0, "max_drawdown": -0.01, "trades": 40, "round_trips": 9, "skill": 0.0, "skill_exposure": 0.5}
    value = {"return": -0.01, "max_drawdown": -0.02, "trades": 12, "round_trips": 6, "skill": -0.01, "skill_exposure": 0.5,
             "skill_basis": "usual", "edge_t": None, "trade_profit": 0.01, "trade_wins": 6}
    assert promote.other_rule_reading(champ, value, RULES, 61.0) == \
        "the two look rule would also have kept it on the value of its trades for a second look"
    assert promote.other_rule_reading(champ, {**value, "trade_profit": -0.01}, RULES, 61.0) == \
        "the two look rule would also have ended it here, for the same reason"


# --- finished trades, the finer points ------------------------------------------------------------------------------

def test_a_sell_of_more_than_the_file_shows_held_has_no_profit_figure():
    """Buy 1 on record, sell 10: the nine units it did not show buying were
    priced as pure profit (+910)."""
    done = promote.finished_trades(fills([(DAY, "BTC", "buy", 1, 100.0), (2 * DAY, "BTC", "sell", 10, 101.0)]))
    assert [(t["pair"], t["pnl"], t["chosen"]) for t in done] == [("BTC", None, True)]

    def sold(bought, qty):
        return promote.finished_trades(fills([(DAY, "BTC", "buy", bought, 100.0), (2 * DAY, "BTC", "sell", qty, 101.0)]))[0]["pnl"]
    # The engine never sells more than an account holds and writes quantities to eight decimals, so only a hair
    # over is still the same sell. (The slack was 5%: a sell of 10.2 against 10 on record was given a figure.)
    assert sold(10, 10.000001) == pytest.approx(10.000001 * 101 - 1000)
    assert sold(10, 10.2) is None and sold(10, 10.001) is None and sold(10, 10.00002) is None
    assert sold(10000, 10000.005) == pytest.approx(10000.005 * 101 - 1000000)    # a large holding: a millionth of it
    assert sold(10000, 10000.02) is None
    assert sold(0.001, 0.0010005) == pytest.approx(0.0010005 * 101 - 0.1)       # half a millionth of a coin: rounding
    assert sold(0.001, 0.001002) is None                                          # two millionths: not rounding
    # (eight decimal rounding on four hundred adds and trims of one position came to 1e-7 of a coin in review)
    assert sold(0.03, 0.0300005) == pytest.approx(0.0300005 * 101 - 3.0)
    # a sell of more than the crumb an exit left is a sell of something the file does not show: no figure either
    rows = [(DAY, "BTC", "buy", 10, 100.0), (2 * DAY, "BTC", "sell", 9.6, 110.0)]
    assert len(promote.finished_trades(fills(rows + [(3 * DAY, "BTC", "sell", 0.4, 110.0)]))) == 1      # the crumb itself
    more = promote.finished_trades(fills(rows + [(3 * DAY, "BTC", "sell", 0.41, 110.0)]))
    assert [(t["ts"], t["pnl"]) for t in more] == [(2 * DAY, pytest.approx(9.6 * 110 + 0.4 * 110 - 1000)), (3 * DAY, None)]


def test_a_crumb_is_valued_at_what_the_closing_sell_went_for():
    rows = [(DAY, "BTC", "buy", 10, 100.0), (2 * DAY, "BTC", "sell", 9.6, 110.0)]
    assert promote.finished_trades(fills(rows))[0]["pnl"] == pytest.approx(9.6 * 110 + 0.4 * 110 - 1000)
    no_price = fills(rows, columns=("ts", "pair", "side", "qty", "notional", "fee"))   # no price or reason column at all
    assert promote.finished_trades(no_price)[0]["pnl"] == pytest.approx(9.6 * 110 + 0.4 * 110 - 1000)
    no_value = fills(rows, columns=("ts", "pair", "side", "qty", "price", "fee"))      # valued from quantity and price
    assert promote.finished_trades(no_value)[0]["pnl"] == pytest.approx(9.6 * 110 + 0.4 * 110 - 1000)
    neither = fills(rows, columns=("ts", "pair", "side", "qty", "fee"))
    assert [t["pnl"] for t in promote.finished_trades(neither)] == [None]
    # the crumb an exit left is carried into the next position at that position's first price
    again = rows + [(3 * DAY, "BTC", "buy", 10, 110.0), (4 * DAY, "BTC", "sell", 10.4, 120.0)]
    assert promote.finished_trades(fills(again))[1]["pnl"] == pytest.approx(10.4 * 120 - (0.4 * 110 + 1100))


def test_rows_that_are_not_fills_are_left_out_of_the_count_of_finished_trades():
    """A quantity that is text, below zero or blank, or a row with no time. Read
    as a sell of everything it would close the position a day early."""
    good = fills([(DAY, "BTC", "buy", 10, 100.0), (2 * DAY, "BTC", "sell", 4, 100.0), (4 * DAY, "BTC", "sell", 6, 110.0)])
    row = {"pair": "BTC", "side": "sell", "price": 100.0, "notional": 0.0, "fee": 0.0, "reason": ""}
    odd = pd.DataFrame([{**row, "ts": 3 * DAY, "qty": "lots"}, {**row, "ts": 3 * DAY, "qty": -5}, {**row, "ts": 3 * DAY, "qty": None},
                        {**row, "ts": None, "qty": 10}, {**row, "ts": 3 * DAY, "qty": 0}])
    done = promote.finished_trades(pd.concat([good, odd], ignore_index=True))
    assert [(t["ts"], t["pnl"]) for t in done] == [(4 * DAY, pytest.approx(4 * 100 + 6 * 110 - 1000))]


def test_a_fill_with_no_figure_leaves_its_trade_without_one():
    buy_blank = fills([(DAY, "BTC", "buy", 10, None), (2 * DAY, "BTC", "sell", 10, 110.0)])
    assert [t["pnl"] for t in promote.finished_trades(buy_blank)] == [None]
    sell_blank = fills([(DAY, "BTC", "buy", 10, 100.0), (2 * DAY, "BTC", "sell", 5, None), (3 * DAY, "BTC", "sell", 5, 110.0)])
    assert [t["pnl"] for t in promote.finished_trades(sell_blank)] == [None]


def test_a_position_is_measured_against_its_largest_size_and_trades_come_back_in_time_order():
    rows = [(1 * DAY, "ETH", "buy", 10, 100.0), (2 * DAY, "ETH", "sell", 6, 100.0), (3 * DAY, "ETH", "buy", 1, 100.0),
            (9 * DAY, "ETH", "sell", 4.6, 100.0),                        # 0.4 left of a largest size of 10: closed
            (4 * DAY, "BTC", "buy", 1, 100.0), (5 * DAY, "BTC", "sell", 1, 100.0),
            (6 * DAY, "ADA", "buy", 1, 100.0), (11 * DAY, "ADA", "sell", 1, 100.0)]    # first by name, last to close
    done = promote.finished_trades(fills(rows))
    assert [(t["pair"], t["ts"]) for t in done] == [("BTC", 5 * DAY), ("ETH", 9 * DAY), ("ADA", 11 * DAY)]


def test_what_the_window_counts_as_a_fill_a_win_and_a_cost(sandbox):
    start_test(sandbox, STEADY)
    tr_file = sandbox / "state" / "challenger1" / "trades.csv"
    text = tr_file.read_text().strip().split("\n")
    head, rows = text[0], text[1:30]                                     # 29 fills...
    odd = ["%d,challenger1,BTC,sell,-1,100,100,100,0,0,,0" % (31 * DAY), "%d,challenger1,BTC,hold,1,100,100,100,0,0,,0" % (32 * DAY),
           "%d,challenger1,,buy,1,100,100,100,0,0,,0" % (33 * DAY), "%d,challenger1,BTC,buy,lots,100,100,100,0,0,,0" % (34 * DAY)]
    tr_file.write_text("\n".join([head] + rows + odd) + "\n")            # ...and four rows that are not fills
    m = promote.window_metrics("challenger1", 0, at(60), 10000.0)
    assert m["trades"] == 29
    # a trade that made exactly nothing is not a win
    trades(sandbox, "challenger1", n=4, sell_price=100.0)
    m = promote.window_metrics("challenger1", 0, at(60), 10000.0)
    assert (m["trade_wins"], m["trade_losses"], m["trade_profit"]) == (0, 2, 0.0)
    # a blank cost cell is no cost, not a figure that is not a number
    p = sandbox / "state" / "challenger1" / "equity.csv"
    eq = pd.read_csv(p)
    eq["fees_paid"] = eq["fees_paid"].astype(object)
    eq.loc[eq["ts"] == 60 * DAY + 3600, "fees_paid"] = ""
    eq.to_csv(p, index=False)
    assert math.isfinite(promote.window_metrics("challenger1", 0, at(60), 10000.0)["fees"])


def test_a_tests_costs_include_the_fills_of_its_first_hour(sandbox):
    """The fills of a test's first hour are made before the window's first
    reading is written, and costs were counted from that reading: H4, all of
    whose 10 fills came in its first hour, read "10 fills, costs 0.00"."""
    rows = [(k * 3600, 10000.0 + k, 2.0 * (k + 1)) for k in range(5)]    # (ts, equity, fees paid so far)
    p = sandbox / "state" / "challenger1" / "equity.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"ts": ts, "equity": e, "cash": e, "gross_exposure": 0, "n_positions": 0, "fees_paid": f,
                   "slippage_paid": f / 2} for ts, e, f in rows]).to_csv(p, index=False)
    # costs on record after each reading: 3, 6, 9, 12, 15
    m = promote.window_metrics("challenger1", 2 * 3600, 4 * 3600, 10002.0)      # the test begins at the third reading
    assert m["fees"] == pytest.approx(15.0 - 6.0)                        # from the reading before it began: 3 hours' costs
    assert m["gross_pnl"] == pytest.approx(2.0 + (15.0 - 9.0))           # gross is over the return's own span
    assert m["fees_first_hour"] == pytest.approx(3.0)                    # and the difference is said, not left to puzzle
    assert ("costs 9.00 (3.00 of that on fills in the hour the test began, which the return and gross pnl here do not "
            "include: both run from the equity after them), gross pnl 8.00") in promote._fmt(m)
    m = promote.window_metrics("challenger1", 0, 4 * 3600, 10000.0)      # an account that began with the test
    assert (m["fees"], m["gross_pnl"], m["fees_first_hour"]) == pytest.approx((15.0, 4.0 + 12.0, 3.0))
    # An account whose return runs from before its first reading (the shadow starts from cash at a promotion and
    # first trades an hour later): every cost is in its return, so every cost is in its gross, and nothing is said.
    m = promote.window_metrics("challenger1", 1800, 4 * 3600, 10000.5)
    assert (m["fees"], m["gross_pnl"], m["fees_first_hour"]) == pytest.approx((15.0 - 3.0, 3.5 + 12.0, 0.0))
    assert "costs 12.00, gross pnl 15.50" in promote._fmt(m)
    m = promote.window_metrics("challenger1", 1800, 4 * 3600, None)      # no start equity on record: from its first reading
    assert (m["fees"], m["gross_pnl"], m["fees_first_hour"]) == pytest.approx((12.0, 3.0 + 9.0, 3.0))


def test_the_tally_says_which_trades_have_no_figure():
    chal = {"trade_wins": 1, "trade_losses": 1, "trade_unknown": 2, "forced_exits": 1, "trade_profit": 0.012}
    assert promote.trade_tally(chal) == ("its 4 finished trades made +1.20% of its starting equity after costs (1 won, "
                                         "1 lost, 2 with no figure in the record, 1 of them closed by the daily loss "
                                         "halt or a strategy error)")
    assert promote.trade_tally({"trade_unknown": 1}) == ("its 1 finished trade (0 won, 0 lost, 1 with no figure in the "
                                                         "record) cannot be put a figure on from the record")


# --- order of writing, and the guard's own rule ---------------------------------------------------------------------

def test_a_first_look_is_on_record_only_once_its_block_is_written(sandbox, monkeypatch, capsys):
    start_test(sandbox, STEADY)
    real = promote.update_ledger

    def fails(*a, **k):
        raise OSError("ledger not writable")
    monkeypatch.setattr(promote, "update_ledger", fails)
    with pytest.raises(OSError, match="ledger not writable"):            # the hour stops: nothing of it is committed
        promote.main(["--now", str(at(60))])
    assert promote.first_look_of(slot.load("challenger1")) is None       # so the look is simply taken again
    monkeypatch.setattr(promote, "update_ledger", real)
    promote.main(["--now", str(at(60) + 3600)])
    assert "### First look H5: passed" in ledger(sandbox) and promote.first_look_of(slot.load("challenger1"))


def test_the_guard_asks_only_whether_the_deposed_config_did_better(sandbox):
    """Both lost to the market, the deposed config by less. The floor under
    skill is a bar for promotions; the guard reverts all the same."""
    slot.reset("challenger1")
    shadow.start(config.account_cfg("champion"), "H5", 100, 10000.0, 10000.0)
    config.dump_yaml(sandbox / "configs" / "champion.yaml",
                     {"hypothesis": "H5", "strategy": "ts_momentum", "params": {"lookback_hours": 168}})
    (sandbox / "LEDGER.md").write_text(ledger(sandbox).replace("- Status: testing", "- Status: promoted"))
    equity(sandbox, "champion", [-0.004, 0.001] * 31)
    equity(sandbox, "shadow", [-0.002, 0.001] * 31)                      # skill below zero, and above the champion's
    trades(sandbox, "shadow")
    promote.rule_on_shadow(100 + 60 * DAY + 100, RULES)
    assert "### Result H5: reverted" in ledger(sandbox) and config.account_cfg("champion")["hypothesis"] == "H0"
