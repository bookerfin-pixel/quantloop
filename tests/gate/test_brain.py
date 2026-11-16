"""PROTECTED. The brain's sensors (bot/brain.py): that each source is read from its answer and nothing else,
that a day or a headline on file is never changed (the record is what was known then), that the markers follow
the regime read's thresholds of 16 November 2026, that one source failing stops no other, and that it stays apart
from the hourly loop and from every account."""
import csv
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from bot import brain, config

REPO = Path(__file__).resolve().parents[2]
DAY = 86400
NOW = int(datetime(2026, 11, 16, 4, 0, tzinfo=timezone.utc).timestamp())       # a Monday, 04:00 UTC


@pytest.fixture
def root(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    monkeypatch.setattr(config, "CANDLES", tmp_path / "state" / "candles")
    monkeypatch.setattr(brain, "_sleep", lambda s: None)
    return tmp_path


def ts(day: str, hour: int = 0) -> int:
    return int(datetime.fromisoformat(day).replace(tzinfo=timezone.utc).timestamp()) + hour * 3600


def rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def plant_prices(root: Path, last_daily: str, days: int, hourly_days: int = 2, start: float = 100.0, step: float = 1.0):
    """BTC and ETH daily candles for `days` days to `last_daily`, rising by `step` a day, then hourly candles for
    the next `hourly_days` days, each hour's close the day's close (the 23:00 one is the day's)."""
    for coin, scale in (("BTC", 1.0), ("ETH", 0.05)):
        d = config.STATE / "wide" / "daily"
        d.mkdir(parents=True, exist_ok=True)
        first = date.fromisoformat(last_daily) - timedelta(days=days - 1)
        with (d / f"{coin}.csv").open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["time", "open", "high", "low", "close", "vwap", "volume", "count", "source"])
            for i in range(days):
                c = (start + step * i) * scale
                w.writerow([ts((first + timedelta(days=i)).isoformat()), c, c, c, c, c, 1, 1, "kraken"])
        h = config.CANDLES
        h.mkdir(parents=True, exist_ok=True)
        with (h / f"{coin}.csv").open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["time", "open", "high", "low", "close", "vwap", "volume", "count"])
            for k in range(1, hourly_days + 1):
                day = (date.fromisoformat(last_daily) + timedelta(days=k)).isoformat()
                c = (start + step * (days - 1 + k)) * scale
                for hour in range(24):
                    w.writerow([ts(day, hour), c, c, c, c, c, 1, 1])


# --- the sources ----------------------------------------------------------------------

def test_fear_and_greed_and_stablecoins_are_read_from_their_answers():
    body = {"name": "Fear and Greed Index", "metadata": {"error": None}, "data": [
        {"value": "10", "value_classification": "Extreme Fear", "timestamp": str(ts("2026-11-16")), "time_until_update": "1"},
        {"value": "12", "value_classification": "Extreme Fear", "timestamp": str(ts("2026-11-15"))},
        {"value": "101", "value_classification": "Greed", "timestamp": str(ts("2026-11-14"))},        # not a reading
        {"value": "x", "timestamp": str(ts("2026-11-13"))},
        {"value": "50", "value_classification": "Neutral", "timestamp": str(ts("2026-11-17"))}]}     # dated after now
    assert brain.parse_fng(body, NOW) == {"2026-11-16": ("10", "Extreme Fear"), "2026-11-15": ("12", "Extreme Fear")}
    assert brain.parse_fng({**body, "metadata": {"error": "rate limited"}}, NOW) == {}
    assert brain.parse_fng(None, NOW) == {} and brain.parse_fng({"data": "nothing"}, NOW) == {}

    chart = [{"date": str(ts("2026-11-14")), "totalCirculating": {"peggedUSD": 1.0},
              "totalCirculatingUSD": {"peggedUSD": 280e9, "peggedEUR": 1.5e9}},
             {"date": str(ts("2026-11-15")), "totalCirculatingUSD": {"peggedUSD": 279e9}},
             {"date": str(ts("2026-11-16")), "totalCirculatingUSD": {"peggedUSD": 278e9}},             # still running
             {"date": "soon", "totalCirculatingUSD": {"peggedUSD": 1e9}}]
    assert brain.parse_stablecoins(chart, NOW) == {"2026-11-14": ("281500000000",), "2026-11-15": ("279000000000",)}
    assert brain.parse_stablecoins({"not": "a list"}, NOW) == {}


def test_a_day_on_file_is_never_changed_and_a_rewrite_is_only_counted(root):
    path = brain.fng_path()
    first = brain.merge_days(path, ["value", "classification"], {"2026-11-13": ("20", "Fear"), "2026-11-15": ("12", "Extreme Fear")})
    assert first == {"added": 2, "revised": 0, "holes_left": 0, "last": "2026-11-15"}
    later = brain.merge_days(path, ["value", "classification"], {"2026-11-13": ("21", "Fear"), "2026-11-14": ("15", "Fear"),
                                                                  "2026-11-15": ("12", "Extreme Fear"), "2026-11-16": ("10", "Extreme Fear")})
    assert later == {"added": 1, "revised": 1, "holes_left": 1, "last": "2026-11-16"}
    on_file = rows(path)
    assert [(r["day"], r["value"]) for r in on_file] == [("2026-11-13", "20"), ("2026-11-15", "12"), ("2026-11-16", "10")]
    assert brain.load_days(path, "value") == {"2026-11-13": 20.0, "2026-11-15": 12.0, "2026-11-16": 10.0}


def test_the_perpetuals_watched_are_read_and_an_answer_in_another_shape_is_refused():
    body = {"result": "success", "tickers": [
        {"symbol": "PF_XBTUSD", "tag": "perpetual", "markPrice": 64500.5, "indexPrice": 64510, "fundingRate": 1.2,
         "openInterest": 1500.25, "suspended": False},
        {"symbol": "pf_nvdaxusd", "markPrice": "183.4", "fundingRate": None},
        {"symbol": "PF_DOGEUSD", "markPrice": 0.1},                                                      # not watched
        "not a ticker"]}
    got = brain.parse_perps(body, NOW)
    assert [r[1] for r in got] == ["PF_XBTUSD", "PF_NVDAXUSD"]
    assert got[0] == [NOW, "PF_XBTUSD", "64500.5", "64510", "1.2", "1500.25", "0"] and got[1][2:5] == ["183.4", "", ""]
    for bad in ({"tickers": "none"}, {"tickers": [{"symbol": "PF_DOGEUSD"}]}, {"tickers": [{"symbol": "PF_NVDAXUSD"}]}, None):
        with pytest.raises(brain.BrainError):
            brain.parse_perps(bad, NOW)


RSS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel>
<title>A feed</title><atom:link href="https://example.com/rss" rel="self"/>
<item><title><![CDATA[Bitcoin falls &amp; <b>funding</b> flips]]></title><link>https://example.com/a</link>
  <pubDate>Mon, 16 Nov 2026 03:30:00 +0000</pubDate><description>Article text that must not be kept</description></item>
<item><title>No link here</title><pubDate>Mon, 16 Nov 2026 03:00:00 +0000</pubDate></item>
<item><title>Bad link</title><link>javascript:alert(1)</link></item>
<item><title>Line\tone\n   line two\xe2\x80\xa8end</title><link> https://example.com/b </link><dc:date>2026-11-16T02:00:00Z</dc:date></item>
</channel></rss>"""

ATOM = b"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"><title>Atom</title>
<entry><title type="html">Fed holds &lt;i&gt;rates&lt;/i&gt;</title><link rel="enclosure" href="https://example.com/x.mp3"/>
  <link rel="alternate" href="https://example.gov/fed"/><updated>2026-11-16T03:00:00Z</updated>
  <published>2026-11-15T20:00:00-05:00</published></entry>
<entry><title>""" + b"y" * 400 + b"""</title><link href="https://example.gov/long"/></entry>
</feed>"""


def test_feeds_give_the_time_the_headline_and_the_link_and_no_article_text():
    got = brain.parse_feed(RSS)
    assert got == [(ts("2026-11-16", 3) + 1800, "Bitcoin falls & funding flips", "https://example.com/a"),
                   (ts("2026-11-16", 2), "Line one line two end", "https://example.com/b")]
    atom = brain.parse_feed(ATOM)
    assert atom[0] == (ts("2026-11-16", 1), "Fed holds rates", "https://example.gov/fed")        # published, in UTC
    assert atom[1][0] is None and len(atom[1][1]) == brain.TITLE_CHARS and atom[1][2] == "https://example.gov/long"
    with pytest.raises(Exception):
        brain.parse_feed(b"<html><body>a page, not a feed")


def test_a_headline_is_kept_once_with_the_time_first_seen_and_old_news_is_left_out(root):
    items = [(ts("2026-11-16", 3), "New one", "https://example.com/1"),
             (ts("2026-11-01"), "Old news the feed still carries", "https://example.com/old"),
             (NOW + 5 * DAY, "Dated in the future", "https://example.com/future"),
             (None, "No date", "https://example.com/nodate")]
    assert brain.add_headlines({"coindesk": items}, NOW) == {"coindesk": 3}
    again = brain.add_headlines({"coindesk": items + [(ts("2026-11-16", 5), "Newer", "https://example.com/2")],
                                 "fed": [(ts("2026-11-16", 4), "Same link, other feed", "https://example.com/1")]}, NOW + 3600)
    assert again == {"coindesk": 1, "fed": 0}
    kept = rows(brain.headline_path("2026-11"))
    assert [r["title"] for r in kept] == ["New one", "Dated in the future", "No date", "Newer"]
    assert kept[0]["seen"] == "2026-11-16T04:00Z" and kept[0]["published"] == "2026-11-16T03:00Z"
    assert kept[1]["published"] == "" and kept[3]["seen"] == "2026-11-16T05:00Z"
    assert set(kept[0]) == set(brain.HEADLINE_COLUMNS)
    # the next month's run still knows last month's links
    assert brain.add_headlines({"coindesk": [(ts("2026-11-30"), "New one", "https://example.com/1")]}, ts("2026-12-01", 1)) == {"coindesk": 0}
    # newest first, by the time the feed gives or else the time seen
    assert [r["title"] for r in brain.recent_headlines(NOW + 3600)] == ["Newer", "Dated in the future", "No date", "New one"]


# --- the markers ------------------------------------------------------------------------

BASE = {"btc_week_close": 65000.0, "btc_low_52w": 59500.0, "btc_200w": 68000.0, "btc_week_close_prev": 74000.0,
        "btc_200w_prev": 67800.0, "btc_30d": -0.2, "stable_30d": -0.05, "nvda_30d": None, "fng": 10.0,
        "btc_funding_7d": 0.0014, "btc_7d": -0.12}


def test_the_markers_follow_the_regime_reads_thresholds():
    m = brain.points(BASE)
    assert m == {"m1": "neither", "m2": "lower", "m3": "lower", "m4": "lower", "m5": "n/a", "m6": "n/a",
                 "m7": "n/a", "m8": "lower"}
    assert brain.points({**BASE, "btc_week_close": 59000.0})["m1"] == "lower"                    # under the 52 week low
    assert brain.points({**BASE, "btc_week_close": 69000.0})["m2"] == "turn"                     # two closes above
    assert brain.points({**BASE, "btc_week_close": 69000.0, "btc_week_close_prev": 67000.0})["m2"] == "neither"
    assert brain.points({**BASE, "btc_30d": 0.01, "stable_30d": 0.0, "nvda_30d": -0.03}) == \
        {**m, "m3": "turn", "m4": "turn", "m7": "lower"}
    assert brain.points({**BASE, "btc_7d": 0.01, "btc_funding_7d": -0.001})["m8"] == "turn"       # fear, price holding, shorts paying
    assert brain.points({**BASE, "btc_7d": 0.01, "btc_funding_7d": -0.001, "fng": 30.0})["m8"] == "neither"
    assert brain.points({**BASE, "fng": None})["m8"] == "n/a" and brain.points({**BASE, "btc_200w": None})["m2"] == "n/a"


def test_weeks_end_on_sunday_and_the_52_week_low_and_200_week_average_are_of_whole_weeks():
    first = date(2022, 1, 2)                                                       # a Sunday
    btc = {(first + timedelta(days=i)).isoformat(): 1000.0 + i for i in range(1600)}
    day = "2026-05-20"                                                             # a Wednesday
    r = brain.measure(day, btc, {}, {}, {}, {}, [])
    sundays = [d for d in sorted(btc) if d <= day and date.fromisoformat(d).weekday() == 6]
    assert r["btc_week_end"] == "2026-05-17" == sundays[-1] and r["btc_week_close"] == btc["2026-05-17"]
    assert r["btc_low_52w"] == btc[sundays[-53]] and r["btc_week_close_prev"] == btc[sundays[-2]]
    assert r["btc_200w"] == pytest.approx(sum(btc[d] for d in sundays[-200:]) / 200)
    assert r["btc_200w_prev"] == pytest.approx(sum(btc[d] for d in sundays[-201:-1]) / 200)
    assert r["btc_30d"] == pytest.approx(btc[day] / btc["2026-04-20"] - 1) and r["btc_7d"] == pytest.approx(btc[day] / btc["2026-05-13"] - 1)
    short = {d: c for d, c in btc.items() if d >= "2025-01-01"}
    assert brain.measure(day, short, {}, {}, {}, {}, [])["btc_200w"] is None


def test_funding_and_the_ai_perpetual_are_read_over_their_own_windows():
    day = "2026-11-15"
    funding = {(date(2026, 11, 15) - timedelta(days=i)).isoformat(): 0.001 for i in range(10)}
    marks = [(ts("2026-10-16", 20), 200.0), (ts("2026-11-15", 6), 190.0), (ts("2026-11-15", 22), 180.0),
             (ts("2026-11-16", 1), 170.0)]                                           # after the day: not its reading
    r = brain.measure(day, {day: 1.0}, {}, {}, {}, funding, marks)
    assert r["btc_funding_7d"] == pytest.approx(0.007) and r["nvda_mark"] == 180.0 and r["nvda_30d"] == pytest.approx(-0.1)
    gappy = {d: v for d, v in funding.items() if d not in ("2026-11-15", "2026-11-14", "2026-11-13")}
    assert brain.measure(day, {day: 1.0}, {}, {}, {}, gappy, marks[1:])["btc_funding_7d"] is None   # 4 of 7 days
    assert brain.measure(day, {day: 1.0}, {}, {}, {}, {}, marks[1:])["nvda_30d"] is None           # nothing 30 days back


def test_a_closed_day_is_written_once_never_again_and_at_most_a_week_late(root):
    plant_prices(root, "2026-11-13", days=1500, hourly_days=2)       # daily to the 13th, then hourly for the 14th and 15th
    brain.merge_days(brain.stable_path(), ["dollars"], {(date(2026, 11, 15) - timedelta(days=i)).isoformat(): (str(300e9 - i * 1e9),)
                                                         for i in range(40)})
    first = brain.write_markers(NOW)
    assert first == {"written": [f"2026-11-{d:02d}" for d in range(9, 16)], "newest_close": "2026-11-15"}
    on_file = rows(brain.markers_path())
    assert list(on_file[0]) == brain.MARKER_COLUMNS and len(on_file) == 7
    last = on_file[-1]
    assert last["day"] == "2026-11-15" and last["written"] == "2026-11-16T04:00Z" and float(last["btc_close"]) == 100.0 + 1501
    assert last["m3"] == "turn" and last["m4"] == "turn" and last["m5"] == "n/a" and last["version"] == "1"
    assert float(last["stable_30d"]) == pytest.approx(300e9 / 270e9 - 1)
    assert brain.write_markers(NOW + 6 * 3600)["written"] == []                                      # the same day: nothing
    assert len(rows(brain.markers_path())) == 7
    # nine days on with the 23:00 hours there: only the newest seven are written, the two before them skipped
    plant_prices(root, "2026-11-13", days=1500, hourly_days=11)
    later = brain.write_markers(NOW + 10 * DAY)
    assert later["written"] == [f"2026-11-{d}" for d in range(18, 25)]
    assert [r["day"] for r in rows(brain.markers_path())][6:8] == ["2026-11-15", "2026-11-18"]


# --- a run ------------------------------------------------------------------------------

def answers(url, params=None, **kw):
    if "alternative.me" in url:
        return None, b"", "ConnectionError: refused"
    if "llama" in url:
        return 200, json.dumps([{"date": str(ts("2026-11-15")), "totalCirculatingUSD": {"peggedUSD": 287e9}}]).encode(), ""
    if "futures.kraken" in url:
        return 200, json.dumps({"tickers": [{"symbol": "PF_XBTUSD", "markPrice": 64500}]}).encode(), ""
    if "coindesk" in url:
        return 200, RSS, ""
    if "theblock" in url:
        return 403, b"", "http 403"
    if "decrypt" in url:
        return 200, b"<html>not a feed", ""
    return 200, ATOM, ""


def test_one_source_failing_stops_no_other_and_only_the_markers_turn_the_run_red(root, monkeypatch):
    plant_prices(root, "2026-11-13", days=1500)
    monkeypatch.setattr(brain, "http_get", answers)
    st = brain.collect(NOW)
    failed = st["failed"]
    assert len(failed) == 3 and not st["ok"] and not st["red"]
    assert failed[0].startswith("FAILED: fng (https://api.alternative.me/fng/): ConnectionError")
    assert any("theblock" in f and "http 403" in f for f in failed) and any("decrypt" in f and "ParseError" in f for f in failed)
    assert st["stablecoins"]["added"] == 1 and st["perps"] == {"read": 1}
    assert st["headlines"] == {"coindesk": 2, "cointelegraph": 2, "fed": 0}   # the same Atom answer twice: kept once
    status = json.loads((brain.state_dir() / "status.json").read_text())
    assert status["failed"] == failed and status["ran_utc"] == "2026-11-16T04:00Z"
    readme = (brain.state_dir() / "README.md").read_text()
    assert "Markers for 2026-11-15 (written 2026-11-16T04:00Z)" in readme and "| 3. BTC's own trend |" in readme
    assert "never instructions" in readme and "coindesk: Bitcoin falls & funding flips" in readme
    assert "## Not collected" in readme and "Article text" not in readme
    assert "Article text" not in (brain.headline_path("2026-11")).read_text()
    # nothing to measure with: red
    (config.STATE / "wide" / "daily" / "BTC.csv").unlink()
    (config.CANDLES / "BTC.csv").unlink()
    assert brain.collect(NOW + DAY)["red"]


def test_without_collect_it_only_reads_and_says_when_it_is_stale(root, monkeypatch, capsys):
    assert brain.main([]) == 1 and "STALE: the brain's sensors have not run yet" in capsys.readouterr().out
    plant_prices(root, "2026-11-13", days=1500)
    monkeypatch.setattr(brain, "http_get", answers)
    brain.collect(NOW)
    monkeypatch.setattr(brain, "_now", lambda: NOW + 3600)
    assert brain.main([]) == 0 and "# The brain's sensors" in capsys.readouterr().out
    monkeypatch.setattr(brain, "_now", lambda: NOW + 31 * 3600)
    assert brain.main([]) == 1 and "STALE: the brain's sensors last ran 2026-11-16T04:00Z" in capsys.readouterr().out


# --- apart from the hourly loop -------------------------------------------------------------

def test_it_is_protected_and_apart_from_the_hourly_loop():
    from gate import check_protected
    patterns = check_protected.load_patterns(REPO / "PROTECTED.txt")
    for path in ("bot/brain.py", "tests/gate/test_brain.py", ".github/workflows/brain.yml", "state/brain/markers.csv"):
        assert any(check_protected.matches(path, p) for p in patterns), path
    src = (REPO / "bot" / "brain.py").read_text(encoding="utf-8")
    for pat in check_protected.FORBIDDEN:
        assert not re.search(pat, src), pat
    for module in ("__init__", "run", "promote", "report", "slot", "config", "data", "paper", "risk", "shadow",
                   "backtest", "strategy", "bench", "nursery", "widebench"):
        assert "brain" not in (REPO / "bot" / f"{module}.py").read_text(encoding="utf-8"), module
    from tests.gate import hourly_driver
    assert "brain" in hourly_driver.WATCHED              # a strategy that opened state/brain would be seen doing it


def test_the_job_commits_only_state_brain_under_the_benchs_word():
    job = (REPO / ".github" / "workflows" / "brain.yml").read_text(encoding="utf-8")
    assert "python -m bot.brain --collect" in job and "git add -A state/brain" in job
    assert 'git commit -q -m "bench: brain $(date -u +%Y-%m-%dT%H:%MZ)"' in job
    assert "group: brain" in job and "cancel-in-progress: false" in job and 'cron: "23 */6 * * *"' in job
    assert "secrets." not in job                         # it needs no key
