"""PROTECTED. The summary says whether the hourly loop itself ran."""
import csv

import pytest

from bot import config, paper, report
from bot.run import DECISION_FIELDS, REPLAYED

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
