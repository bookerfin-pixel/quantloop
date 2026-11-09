"""PROTECTED. The history of every pair Binance has quoted in USDT (bot/binance.py): that it keeps
the pairs that died, leaves out what it should, settles a month only when it is whole, stops loudly
rather than keep the survivors alone, and reads back as coins on the days they were what they were."""
import gzip
import io
import json
import re
import threading
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from bot import binance, config, wide

REPO = Path(__file__).resolve().parents[2]
DAY = 86400
MONTHLY = binance.MONTHLY


def at(year, month, day, hour=3):
    return int(datetime(year, month, day, hour, 17, tzinfo=timezone.utc).timestamp())


NOW = at(2026, 10, 10)                 # the 10th: September is the newest month, and can be settled


def days_of(month):
    y, m = int(month[:4]), int(month[5:])
    first = datetime(y, m, 1, tzinfo=timezone.utc)
    nxt = datetime(y + (m == 12), 1 if m == 12 else m + 1, 1, tzinfo=timezone.utc)
    return [int(first.timestamp()) + i * DAY for i in range((nxt - first).days)]


def zip_of(symbol, month, rows, header=False):
    text = ("open_time,open,high,low,close,volume,close_time,quote_volume,count,taker_buy_volume,"
            "taker_buy_quote_volume,ignore\n" if header else "") + "".join(",".join(map(str, r)) + "\n" for r in rows)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr(f"{symbol}-1d-{month}.csv", text)
    return buf.getvalue()


class Archive:
    """data.binance.vision, the S3 bucket behind it and Binance's market data host, as far as bot/binance.py asks them."""

    def __init__(self):
        self.files = {}          # (symbol, month) -> rows
        self.info = {}           # symbol -> (base, status) on Binance's list of symbols
        self.page = 1000         # names a listing page holds
        self.listing_down = False
        self.info_down = False
        self.files_down = False
        self.broken = set()      # (symbol, month) that answer 503
        self.headers = set()     # (symbol, month) whose file starts with a header line
        self.calls = []
        self.lock = threading.Lock()

    def pair(self, symbol, first, last, price=10.0, volume=1000.0, status="TRADING", base=None, skip=(), in_info=True):
        for month in binance.months_from(first, last):
            rows = []
            for t in days_of(month):
                day = datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%d")
                if day in skip:
                    continue
                ms = t * 1000
                stamp = ms * 1000 if month >= "2025-01" else ms          # microseconds from 2025, as Binance writes them
                p = price(day) if callable(price) else price
                rows.append([stamp, f"{p:.8f}", f"{p * 1.02:.8f}", f"{p * 0.98:.8f}", f"{p:.8f}", f"{volume:.8f}",
                             stamp + DAY * 1000 - 1, f"{volume * p:.8f}", 57, f"{volume / 2:.8f}", f"{volume * p / 2:.8f}", 0])
            if rows:
                self.files[(symbol, month)] = rows
        if in_info:
            self.info[symbol] = (base or symbol[:-4], status)

    def names(self):
        out = []
        for (sym, month) in self.files:
            out += [f"{MONTHLY}{sym}/1d/{sym}-1d-{month}.zip", f"{MONTHLY}{sym}/1d/{sym}-1d-{month}.zip.CHECKSUM"]
        # other quotes and other candle lengths, which the job must not take for USDT pairs or daily files
        out += [f"{MONTHLY}BTCBUSD/1d/BTCBUSD-1d-2026-09.zip", f"{MONTHLY}BTCUSDT/1h/BTCUSDT-1h-2026-09.zip"]
        return sorted(set(out))

    def listing(self, params):
        prefix, delim, marker = params["prefix"], params.get("delimiter"), params.get("marker", "")
        names = [n for n in self.names() if n.startswith(prefix)]
        if delim:
            names = sorted({prefix + n[len(prefix):].split(delim)[0] + delim if delim in n[len(prefix):] else n for n in names})
        names = [n for n in names if n > marker]
        page, more = names[:self.page], len(names) > self.page
        tag = "CommonPrefixes><Prefix" if delim else "Contents><Key"
        close = "Prefix></CommonPrefixes" if delim else "Key></Contents"
        body = "".join(f"<{tag}>{n}</{close}>" for n in page)
        nxt = f"<NextMarker>{page[-1]}</NextMarker>" if (more and delim) else ""      # S3 gives NextMarker only with a delimiter
        return (f'<?xml version="1.0" encoding="UTF-8"?><ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">'
                f"<Name>data.binance.vision</Name><Prefix>{prefix}</Prefix><Marker>{marker}</Marker>"
                f"<IsTruncated>{'true' if more else 'false'}</IsTruncated>{nxt}{body}</ListBucketResult>").encode()

    def __call__(self, url, params=None, tries=3, timeout=30.0):
        params = dict(params or {})
        with self.lock:
            self.calls.append((url, params))
        if url == binance.LISTING:
            return (None, None, "http 503") if self.listing_down else (200, self.listing(params), "")
        if url == f"{binance.API}/exchangeInfo":
            if self.info_down:
                return None, None, "http 503"
            symbols = [{"symbol": s, "baseAsset": b, "quoteAsset": "USDT", "status": st} for s, (b, st) in self.info.items()]
            symbols.append({"symbol": "BTCBUSD", "baseAsset": "BTC", "quoteAsset": "BUSD", "status": "BREAK"})
            return 200, json.dumps({"symbols": symbols}).encode(), ""
        if url == f"{binance.API}/klines":
            sym = params["symbol"]
            if sym not in self.info:
                return 400, None, "http 400"
            assert params["interval"] == "1M"
            rows = [[binance._month_ms(m), "1", "1", "1", "1", "1"] for (s, m) in sorted(self.files) if s == sym
                    and binance._month_ms(m) >= int(params["startTime"])]
            return 200, json.dumps(rows).encode(), ""
        if url.startswith(binance.ARCHIVE + "/"):
            m = re.fullmatch(rf"{re.escape(binance.ARCHIVE)}/{MONTHLY}(\w+)/1d/(\w+)-1d-(\d{{4}}-\d{{2}})\.zip", url)
            assert m and m.group(1) == m.group(2), url
            key = (m.group(1), m.group(3))
            if self.files_down or key in self.broken:
                return None, None, "http 503"
            if key not in self.files:
                return 404, None, "http 404"
            return 200, zip_of(key[0], key[1], self.files[key], header=key in self.headers), ""
        raise AssertionError(f"a request to an address the job has no business with: {url}")

    def asked(self, what):
        return [c for c in self.calls if what in c[0]]


@pytest.fixture
def archive(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    (tmp_path / "state").mkdir()
    a = Archive()
    monkeypatch.setattr(binance, "get", a)
    monkeypatch.setattr(binance, "_sleep", lambda s: None)
    monkeypatch.setattr(binance, "_now", lambda: NOW + DAY)            # main() and the report: the day after the first run
    monkeypatch.setattr(binance, "FIRST_MONTH", "2026-05")
    monkeypatch.setattr(binance, "MIN_ENDED", 2)
    return a


def world(a):
    """Two coins alive, two that died, one leveraged token, one dollar token, and two coins whose names a careless
    rule would take for leveraged tokens."""
    a.pair("BTCUSDT", "2026-05", "2026-09", price=60000.0, volume=50.0)
    a.pair("ETHUSDT", "2026-05", "2026-09", price=3000.0, volume=400.0)
    a.pair("LUNAUSDT", "2026-05", "2026-07", price=lambda d: 80.0 if d < "2026-07-10" else 0.0001, volume=1e6, status="BREAK")
    a.pair("OLDUSDT", "2026-05", "2026-06", price=2.0, in_info=False)                 # delisted long ago: only the archive knows it
    a.pair("BTCUPUSDT", "2026-05", "2026-06", price=12.0, status="BREAK")
    a.pair("USDCUSDT", "2026-05", "2026-09", price=1.0, volume=1e7)
    a.pair("JUPUSDT", "2026-05", "2026-09", price=0.8)
    a.pair("SYRUPUSDT", "2026-07", "2026-09", price=0.3)


def rows_of(month):
    with gzip.open(binance.month_path(month), "rt") as f:
        return list(csv_rows(f.read()))


def csv_rows(text):
    lines = text.splitlines()
    assert lines[0] == binance.HEADER
    return [ln.split(",") for ln in lines[1:]]


# --- a first run ------------------------------------------------------------------

def test_a_first_run_keeps_the_pairs_that_died_and_leaves_out_what_it_should(archive):
    world(archive)
    status = binance.collect(NOW)
    assert status["ok"] is True and status["newest_month"] == "2026-09"
    assert status["settled"] == ["2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
    may = {r[0] for r in rows_of("2026-05")}
    assert may == {"BTCUSDT", "ETHUSDT", "LUNAUSDT", "OLDUSDT", "JUPUSDT"}                  # the dead are in
    assert {r[0] for r in rows_of("2026-07")} == {"BTCUSDT", "ETHUSDT", "LUNAUSDT", "JUPUSDT", "SYRUPUSDT"}
    assert {r[0] for r in rows_of("2026-09")} == {"BTCUSDT", "ETHUSDT", "JUPUSDT", "SYRUPUSDT"}
    pairs = json.loads((binance.root() / "pairs.json").read_text())
    assert pairs["BTCUPUSDT"]["left_out"] == "leveraged token" and pairs["USDCUSDT"]["left_out"] == "pegged"
    assert pairs["JUPUSDT"]["left_out"] == "" and pairs["SYRUPUSDT"]["left_out"] == ""
    assert pairs["OLDUSDT"]["found_in"] == ["archive"] and pairs["OLDUSDT"]["binance_status"] == "not in Binance's list"
    assert pairs["LUNAUSDT"]["binance_status"] == "BREAK" and pairs["LUNAUSDT"]["last_month"] == "2026-07"
    assert "BTCBUSD" not in pairs
    assert status["pairs"]["kept"] == 6 and status["pairs"]["ended_before_newest"] == 2
    # nothing left out is ever asked for
    assert not [c for c in archive.asked(binance.ARCHIVE + "/") if "BTCUP" in c[0] or "USDCUSDT" in c[0]]


def test_the_rows_are_the_archives_figures_with_their_trailing_zeros_dropped(archive):
    world(archive)
    archive.headers.add(("ETHUSDT", "2026-06"))
    binance.collect(NOW)
    btc = [r for r in rows_of("2026-05") if r[0] == "BTCUSDT"]
    assert len(btc) == 31 and btc[0] == ["BTCUSDT", "2026-05-01", "60000", "61200", "58800", "60000", "50", "3000000", "57", "1500000"]
    eth = [r for r in rows_of("2026-06") if r[0] == "ETHUSDT"]
    assert [r[1] for r in eth] == [f"2026-06-{d:02d}" for d in range(1, 31)]          # the header line was not a candle


def test_microsecond_and_millisecond_stamps_both_give_the_right_day():
    for month, unit in (("2024-12", 1), ("2025-01", 1000)):
        t = days_of(month)[4] * 1000 * unit
        rows, bad = binance.read_zip(zip_of("XUSDT", month, [[t, "1.50000000", "2", "1", "1.5", "10", t + 1, "15", 3, "5", "7.5", 0]]),
                                     "XUSDT", month)
        assert rows == [["XUSDT", f"{month}-05", "1.5", "2", "1", "1.5", "10", "15", "3", "8"]] and bad == 0


def test_a_file_that_is_not_what_it_should_be_is_refused():
    t = days_of("2026-05")[0] * 1000
    good = [t, "1", "1", "1", "1", "1", t, "1", 1, "1", "1", 0]
    cases = {
        "a candle of another month": [[days_of("2026-06")[0] * 1000] + good[1:]],
        "not at midnight": [[t + 3600_000] + good[1:]],
        "two candles for one day": [good, good],
        "too few fields": [good[:6]],
        "not a number": [[t, "x"] + good[2:]],
        "a header among the candles": [good, ["open_time"] + good[1:]],
    }
    for name, rows in cases.items():
        with pytest.raises(ValueError):
            binance.read_zip(zip_of("XUSDT", "2026-05", rows), "XUSDT", "2026-05")
    zero = [t, "0", "0", "0", "0", "0", t, "0", 0, "0", "0", 0]
    assert binance.read_zip(zip_of("XUSDT", "2026-05", [zero]), "XUSDT", "2026-05") == ([], 1)   # a price of nothing is left out and counted
    blob = bytearray(zip_of("XUSDT", "2026-05", [good]))
    blob[60] ^= 0xFF
    with pytest.raises(Exception):
        binance.read_zip(bytes(blob), "XUSDT", "2026-05")


def test_volumes_are_rounded_and_prices_are_not():
    assert binance._coins("12345.67891234") == "12345.679" and binance._coins("0.00012345678912") == "0.00012345679"
    assert binance._coins("123456789123.5") == "123456790000" and binance._coins("0.00000000") == "0"
    assert binance._dollars("3021457.98765432") == "3021458" and binance._dollars("0.4") == "0"
    assert binance._num("0.00001234") == "0.00001234" and binance._num("61234.56000000") == "61234.56"
    for bad in ("-1", "nan", "inf", "x"):
        with pytest.raises(ValueError):
            binance._coins(bad)


def test_the_name_rules():
    coins = {"BTC", "ETH", "EOS", "XRP", "BNB", "1INCH", "S", "J", "SUPER", "JUP", "SYRUP", "LINK"}
    for name in ("BTCUP", "BTCDOWN", "ETHBULL", "EOSBEAR", "BULL", "BEAR", "1INCHUP", "LINKDOWN"):
        assert binance.leave_out(name, coins) == "leveraged token", name
    for name in ("JUP", "SYRUP", "SUPER", "SUP", "BTC", "S", "PUMP", "SETUP", "LINK"):
        assert binance.leave_out(name, coins) == "", name
    for name in ("USDC", "BUSD", "TUSD", "FDUSD", "PAXG", "WBTC", "WBETH", "EUR", "UST", "USD1"):
        assert binance.leave_out(name, coins) == "pegged", name
    wide_list = yaml.safe_load((REPO / "configs" / "wide.yaml").read_text())["exclude"]
    assert set(wide_list) <= binance.PEGGED                                  # whatever Kraken's list leaves out, this does


# --- the days after -----------------------------------------------------------------

def test_a_run_with_nothing_to_do_asks_nothing_and_writes_nothing(archive):
    world(archive)
    binance.collect(NOW)
    before = {p: p.read_bytes() for p in binance.root().rglob("*") if p.is_file()}
    archive.calls.clear()
    assert binance.collect(NOW + DAY) == {} and archive.calls == []
    assert {p: p.read_bytes() for p in binance.root().rglob("*") if p.is_file()} == before
    assert binance.main(["--collect"]) == 0 and archive.calls == []


def test_the_newest_month_waits_for_the_8th_and_for_its_files(archive):
    world(archive)
    late = {k: archive.files.pop(k) for k in [("JUPUSDT", "2026-09"), ("SYRUPUSDT", "2026-09")]}
    s = binance.collect(at(2026, 10, 4))                                        # the 4th: September is sought, not settled
    assert "2026-09" not in s["settled"] and "2026-08" in s["settled"]
    assert {r[0] for r in rows_of("2026-09")} == {"BTCUSDT", "ETHUSDT"}
    archive.calls.clear()
    s = binance.collect(at(2026, 10, 8))                                        # the 8th: only half the pairs have a file
    assert "2026-09" not in s["settled"]
    assert not archive.asked(binance.ARCHIVE + "/")                              # what it holds is not asked for again
    archive.files.update(late)
    archive.calls.clear()
    s = binance.collect(at(2026, 10, 9))
    assert "2026-09" in s["settled"] and {r[0] for r in rows_of("2026-09")} == {"BTCUSDT", "ETHUSDT", "JUPUSDT", "SYRUPUSDT"}
    assert sorted(c[0].rsplit("/", 1)[1] for c in archive.asked(binance.ARCHIVE + "/")) == \
        ["JUPUSDT-1d-2026-09.zip", "SYRUPUSDT-1d-2026-09.zip"]
    assert binance.collect(at(2026, 10, 10)) == {}


def test_the_newest_month_waits_for_every_pair_binance_still_trades(archive, monkeypatch):
    world(archive)
    for i in range(20):                                                       # enough pairs that one missing is under a tenth
        archive.pair(f"C{i}USDT", "2026-05", "2026-09")
    monkeypatch.setattr(binance, "MIN_ENDED", 2)
    late = archive.files.pop(("C3USDT", "2026-09"))
    s = binance.collect(NOW)
    assert "2026-09" not in s["settled"] and s["months"]["newest_waiting_for"] == ["C3USDT"]
    assert "- Binance history: 2026-09 waits for the files of 1 pairs Binance still trades (C3USDT) before it is settled" in binance.summary_lines(NOW)
    archive.files[("C3USDT", "2026-09")] = late
    assert "2026-09" in binance.collect(NOW + DAY)["settled"]


def test_a_new_month_is_sought_from_the_3rd(archive):
    world(archive)
    binance.collect(NOW)
    archive.pair("BTCUSDT", "2026-10", "2026-10", price=61000.0)
    archive.calls.clear()
    assert binance.collect(at(2026, 11, 2)) == {} and archive.calls == []        # the 2nd: October's files may not be up
    s = binance.collect(at(2026, 11, 3))
    assert s["newest_month"] == "2026-10" and "2026-10" not in s["settled"] and binance.month_path("2026-10").exists()


def test_a_file_that_fails_is_asked_for_again_and_its_month_waits(archive):
    world(archive)
    archive.broken.add(("ETHUSDT", "2026-06"))
    s = binance.collect(NOW)
    assert s["ok"] is True and "2026-06" not in s["settled"] and "2026-07" in s["settled"]
    assert s["files"]["failed"] == 1 and s["files"]["failed_first"] == ["2026-06 ETHUSDT: http 503"]
    assert any(ln.startswith("FAILED: Binance history: 1 files could not be fetched") for ln in binance.summary_lines(NOW))
    archive.broken.clear()
    archive.calls.clear()
    s = binance.collect(NOW + DAY)
    assert "2026-06" in s["settled"] and [c[0].rsplit("/", 1)[1] for c in archive.asked(binance.ARCHIVE + "/")] == ["ETHUSDT-1d-2026-06.zip"]
    assert "ETHUSDT" in {r[0] for r in rows_of("2026-06")}
    assert not [ln for ln in binance.summary_lines(NOW + DAY) if ln.startswith(("FAILED", "STALE"))]


def test_a_month_file_is_the_same_bytes_for_the_same_rows(archive):
    rows = [["BUSDT", "2026-05-02", "1", "1", "1", "1", "1", "1", "1", "1"], ["AUSDT", "2026-05-01", "2", "2", "2", "2", "2", "2", "2", "2"]]
    assert binance.write_month("2026-05", rows) is True
    first = binance.month_path("2026-05").read_bytes()
    assert binance.write_month("2026-05", list(reversed(rows))) is False and binance.month_path("2026-05").read_bytes() == first
    assert binance.read_month("2026-05")[0][0] == "AUSDT"


def test_a_listing_over_many_pages_is_read_whole(archive):
    world(archive)
    archive.page = 2
    s = binance.collect(NOW)
    assert s["pairs"]["kept"] == 6 and s["settled"][-1] == "2026-09"
    assert len(archive.asked(binance.LISTING)) > 10


def test_the_budget_is_looked_at_before_every_file_and_leaves_the_rest_for_the_next_run(archive, monkeypatch):
    world(archive)
    served = lambda: len(archive.asked(binance.ARCHIVE + "/"))
    monkeypatch.setattr(binance, "_clock", lambda: 0.0 if served() < 7 else binance.BUDGET_S + 1.0)
    s = binance.collect(NOW)
    assert s["ok"] is True and s["settled"][0] == "2026-05" and "2026-09" not in s["settled"]
    assert s["months"]["left_for_next_run"] and served() <= 7 + binance.WORKERS
    assert "the run's time being up" in "\n".join(binance.summary_lines(NOW))
    monkeypatch.setattr(binance, "_clock", lambda: 0.0)
    s = binance.collect(NOW)
    assert s["settled"] == binance.months_from("2026-05", "2026-09") and not s["months"]["left_for_next_run"]
    assert len({(c[0]) for c in archive.asked(binance.ARCHIVE + "/")}) == len(archive.asked(binance.ARCHIVE + "/"))  # none asked twice


# --- stopping loudly ----------------------------------------------------------------

def test_a_history_of_survivors_alone_stops_the_run(archive, monkeypatch):
    world(archive)
    monkeypatch.setattr(binance, "MIN_ENDED", 3)
    with pytest.raises(binance.BinanceError, match="survivors"):
        binance.collect(NOW)
    s = json.loads((binance.root() / "status.json").read_text())
    assert s["ok"] is False and "only 2 of the 6 pairs" in s["stopped"] and s["settled"] == []
    assert not (binance.root() / "months").exists() and not (binance.root() / "pairs.json").exists()
    assert binance.main(["--collect"]) == 1
    assert binance.summary_lines(NOW)[1].startswith("FAILED: Binance history: the run stopped: only 2 of the 6 pairs")


def test_the_archive_list_failing_falls_back_on_binances_list_and_says_so(archive, monkeypatch):
    world(archive)
    archive.listing_down = True
    with pytest.raises(binance.BinanceError, match="only 1 of the 5 pairs found .from Binance's list of symbols alone"):
        binance.collect(NOW)                                                   # it finds fewer of the dead, and says so
    monkeypatch.setattr(binance, "MIN_ENDED", 1)
    s = binance.collect(NOW)
    assert s["sources"]["fallback"] is True and s["ok"] is True
    assert "LUNAUSDT" in {r[0] for r in rows_of("2026-05")}                      # BREAK pairs are on Binance's list
    assert "OLDUSDT" not in {r[0] for r in rows_of("2026-05")}                   # one delisted long ago is not
    assert s["settled"] == []                                                    # so nothing it wrote is taken as whole
    assert any(ln.startswith("FAILED: Binance history: the archive's list of pairs could not be read") for ln in binance.summary_lines(NOW))
    archive.listing_down = False
    archive.calls.clear()
    s = binance.collect(NOW + DAY)
    assert s["settled"] == binance.months_from("2026-05", "2026-09") and "OLDUSDT" in {r[0] for r in rows_of("2026-05")}
    assert sorted(c[0].rsplit("/", 1)[1] for c in archive.asked(binance.ARCHIVE + "/")) == \
        ["OLDUSDT-1d-2026-05.zip", "OLDUSDT-1d-2026-06.zip"]                    # and only what it lacked is asked for


def test_neither_list_stops_the_run(archive):
    world(archive)
    archive.listing_down = archive.info_down = True
    with pytest.raises(binance.BinanceError, match="neither"):
        binance.collect(NOW)


def test_binances_list_failing_alone_is_said_and_the_run_goes_on(archive):
    world(archive)
    archive.info_down = True
    s = binance.collect(NOW)
    assert s["ok"] is True and s["pairs"]["kept"] == 6
    assert any(ln.startswith("FAILED: Binance history: Binance's list of symbols could not be read") for ln in binance.summary_lines(NOW))


def test_a_list_that_was_cut_off_stops_the_run(archive):
    world(archive)
    for i in range(11):
        archive.info[f"NEW{i}USDT"] = (f"NEW{i}", "TRADING")
    with pytest.raises(binance.BinanceError, match="cut off"):
        binance.collect(NOW)


def test_an_archive_that_serves_no_file_stops_the_run_at_the_first_month(archive):
    world(archive)
    archive.files_down = True
    with pytest.raises(binance.BinanceError, match="not one of the 5 files of 2026-05"):
        binance.collect(NOW)
    assert len(archive.asked(binance.ARCHIVE + "/")) == 5


# --- reading it back ----------------------------------------------------------------

def frame(rows):
    df = pd.DataFrame(rows, columns=["symbol", "day", "open", "close", "quote_volume"])
    df["day"] = pd.to_datetime(df["day"], utc=True)
    for c in ("high", "low", "volume", "trades", "taker_buy_quote_volume"):
        df[c] = 1.0
    df = df.sort_values(["symbol", "day"]).reset_index(drop=True)
    df["coin"] = binance.coins(df)
    return df


def run(symbol, start, prices, skip=()):
    out, day = [], pd.Timestamp(start)
    for p in prices:
        while day.strftime("%Y-%m-%d") in skip:
            day += pd.Timedelta(days=1)
        out.append([symbol, day.strftime("%Y-%m-%d"), p, p, 1000.0])
        day += pd.Timedelta(days=1)
    return out


def test_a_pair_that_came_back_as_another_coin_is_two_coins():
    gap = [f"2022-05-{d:02d}" for d in range(13, 31)]
    away = [d.strftime("%Y-%m-%d") for d in pd.date_range("2021-01-06", periods=40)]
    rows = (run("LUNAUSDT", "2022-05-01", [80.0] * 10 + [0.0002] * 2 + [6.0] * 10, skip=gap)    # 18 days away, then LUNA 2.0
            + run("COCOSUSDT", "2021-01-01", [0.001] * 5 + [1.2] * 5, skip=["2021-01-06", "2021-01-07", "2021-01-08"])
            + run("DROPUSDT", "2021-01-01", [10.0] * 5 + [1.0] * 5, skip=["2021-01-06", "2021-01-07"])  # suspended, then far lower
            + run("CRASHUSDT", "2021-01-01", [10.0] * 5 + [0.05] * 5)                              # no gap at all
            + run("LONGUSDT", "2021-01-01", [3.0] * 10, skip=away)                                 # 40 days away, back where it was
            + run("HALTUSDT", "2021-01-01", [3.0] * 5 + [1.8] * 5, skip=away[:12]))                # 12 days, back 40% lower
    df = frame(rows)
    got = {s: sorted(set(g["coin"])) for s, g in df.groupby("symbol")}
    assert got == {"LUNAUSDT": ["LUNA", "LUNA#2"], "COCOSUSDT": ["COCOS", "COCOS#2"], "DROPUSDT": ["DROP"], "CRASHUSDT": ["CRASH"],
                   "LONGUSDT": ["LONG", "LONG#2"], "HALTUSDT": ["HALT"]}
    cut = binance.breaks(df)
    assert [(b["coin"], b["split"], b["left"], b["back"], b["missing_days"]) for b in cut] == [
        ("COCOS#2", True, "2021-01-05", "2021-01-09", 3), ("DROP", False, "2021-01-05", "2021-01-08", 2),
        ("LONG#2", True, "2021-01-05", "2021-02-15", 40), ("LUNA#2", True, "2022-05-12", "2022-05-31", 18)]
    p = binance.panel("close", df)
    assert list(p.columns) == ["COCOS", "COCOS#2", "CRASH", "DROP", "HALT", "LONG", "LONG#2", "LUNA", "LUNA#2"]
    assert (p.index[1:] - p.index[:-1]).max() == pd.Timedelta(days=1)


def test_returns_book_a_suspension_on_the_day_trading_comes_back_and_nothing_outside_a_coins_life():
    df = frame(run("HALTUSDT", "2021-01-01", [10.0, 10.0, 2.0, 3.0], skip=["2021-01-03", "2021-01-04"])
               + run("LATEUSDT", "2021-01-04", [5.0, 5.5]))
    r = binance.returns(df)
    assert r["HALT"].tolist()[1:] == [0.0, 0.0, 0.0, -0.8, 0.5] and np.isnan(r["HALT"].iloc[0])
    assert r["LATE"].isna().tolist() == [True, True, True, True, False, True] and r["LATE"].iloc[4] == pytest.approx(0.1)


def test_the_list_is_judged_on_the_days_before_and_keeps_the_coins_that_die():
    big = run("BIGUSDT", "2024-01-01", [5.0] * 200)
    small = run("SMALLUSDT", "2024-01-01", [3.0] * 200)
    for r in small:
        r[4] = 10.0
    late = run("LATEUSDT", "2024-03-01", [2.0] * 140)                      # trades more than anyone, from 1 March
    for r in late:
        r[4] = 1e9
    dies = run("DIESUSDT", "2024-01-01", [8.0] * 100)                      # last candle on 9 April
    for r in dies:
        r[4] = 1e6
    peg = run("PEGUSDT", "2024-01-01", [1.0 + 0.001 * (i % 3) for i in range(200)])
    for r in peg:
        r[4] = 1e12
    df = frame(big + small + late + dies + peg)
    top = binance.listing(2, df)
    day = lambda d: pd.Timestamp(d, tz="UTC")
    assert not top.loc[day("2024-02-29")].any()                            # nobody has 60 days behind them yet
    assert top.loc[day("2024-03-01")][["DIES", "BIG"]].all() and top.loc[day("2024-03-01")].sum() == 2
    assert not top["PEG"].any()                                            # a dollar token never ranks, whatever it trades
    assert not top.loc[:day("2024-04-29"), "LATE"].any() and top.loc[day("2024-04-30"), "LATE"]  # 60 days behind it on 30 April
    assert top.loc[day("2024-04-10"), "DIES"] and not top.loc[day("2024-04-11"), "DIES"]  # in as the day after its last began
    # what a day holds says nothing of that day's list; half a window of it says something of the days after
    later = df.copy()
    later.loc[(later["coin"] == "SMALL") & (later["day"] >= day("2024-03-05")), "quote_volume"] = 1e15
    moved = binance.listing(2, later)
    assert moved.loc[:day("2024-03-05")].equals(top.loc[:day("2024-03-05")])
    assert moved["SMALL"].idxmax() == day("2024-03-20")                     # fifteen days of the thirty: the median has moved
    one = df.copy()
    one.loc[(one["coin"] == "SMALL") & (one["day"] == day("2024-03-05")), "quote_volume"] = 1e15
    assert binance.listing(2, one).equals(top)                              # and one day's burst buys no place at all


def test_load_works_out_the_coins_on_the_whole_history_whatever_months_it_is_asked_for(archive, monkeypatch):
    world(archive)
    archive.pair("LUNAUSDT", "2026-09", "2026-09", price=6.0, status="TRADING")              # listed again in September
    monkeypatch.setattr(binance, "MIN_ENDED", 1)                                            # LUNA no longer ends
    binance.collect(NOW)
    assert set(binance.load()["coin"]) >= {"LUNA", "LUNA#2"}
    assert set(binance.load(first="2026-09")["coin"]) == {"BTC", "ETH", "JUP", "SYRUP", "LUNA#2"}


def test_load_reads_the_files_back_as_coins(archive):
    world(archive)
    binance.collect(NOW)
    df = binance.load()
    assert set(df["coin"]) == {"BTC", "ETH", "LUNA", "OLD", "JUP", "SYRUP"}
    assert df["close"].dtype == float and str(df["day"].dt.tz) == "UTC"
    luna = df[df["coin"] == "LUNA"]
    assert luna["day"].max() == pd.Timestamp("2026-07-31", tz="UTC") and luna["close"].iloc[-1] == 0.0001
    assert binance.panel("close", df).shape[1] == 6 and binance.load(first="2026-09")["day"].min() == pd.Timestamp("2026-09-01", tz="UTC")


# --- the report ---------------------------------------------------------------------

def test_the_report(archive):
    assert binance.summary_lines(NOW) == ["- Binance history: no run on record yet; the job's first run fills it (bot/binance.py)"]
    assert binance.summary_lines(at(2026, 11, 25))[0].startswith("STALE: Binance history: no run on record")
    world(archive)
    binance.collect(NOW)
    lines = binance.summary_lines(NOW)
    assert lines == ["- Binance history, run of 2026-10-10 03:17Z: 5 months on file (2026-05 to 2026-09), settled to 2026-09; "
                     "6 pairs kept, 2 of them ending before 2026-09, 2 left out (pegged or leveraged)"]
    stale = binance.summary_lines(at(2026, 11, 21))                         # October should be in by the 20th of November
    assert stale[-1].startswith("STALE: Binance history: 2026-10 is not settled")
    assert not [ln for ln in binance.summary_lines(at(2026, 11, 19)) if ln.startswith("STALE")]
    (binance.root() / "status.json").write_text("{not json")
    assert binance.summary_lines(NOW) == ["FAILED: Binance history: status.json cannot be read (JSONDecodeError)"]


def test_python_m_bot_wide_prints_the_binance_lines_too(archive, capsys, monkeypatch):
    monkeypatch.setattr(config, "CONFIGS", REPO / "configs")
    assert wide.main([]) == 0
    out = capsys.readouterr().out.splitlines()
    assert out[-1] == "- Binance history: no run on record yet; the job's first run fills it (bot/binance.py)"
    monkeypatch.setattr(binance, "summary_lines", lambda now=None: (_ for _ in ()).throw(ValueError("broken")))
    assert wide.main([]) == 0
    assert capsys.readouterr().out.splitlines()[-1] == "FAILED: Binance history: its report could not be made (ValueError)"


def test_a_run_that_fails_unforeseen_says_so_and_keeps_what_was_settled(archive, monkeypatch):
    world(archive)
    binance.collect(NOW)
    monkeypatch.setattr(binance, "collect", lambda now=None: 1 / 0)
    assert binance.main(["--collect"]) == 1
    s = json.loads((binance.root() / "status.json").read_text())
    assert s["ok"] is False and s["stopped"] == "the run failed: ZeroDivisionError: division by zero"
    assert s["settled"] == binance.months_from("2026-05", "2026-09") and s["months"]["on_file"] == 5
    assert binance.summary_lines()[1] == "FAILED: Binance history: the run stopped: the run failed: ZeroDivisionError: division by zero"


# --- asking politely ----------------------------------------------------------------

def test_get_asks_again_only_when_it_is_worth_it(monkeypatch):
    answers, waits = [], []

    class Session:
        headers = {}

        def get(self, url, params=None, timeout=None):
            a = answers.pop(0)
            if isinstance(a, Exception):
                raise a
            return type("R", (), {"status_code": a, "content": b"ok"})()

    monkeypatch.setattr(binance, "_session", lambda: Session())
    monkeypatch.setattr(binance, "_sleep", waits.append)
    answers[:] = [429, 503, 200]
    assert binance.get("https://data.binance.vision/x") == (200, b"ok", "") and len(waits) == 2
    answers[:] = [404]
    assert binance.get("https://data.binance.vision/x") == (404, None, "http 404")
    answers[:] = [ConnectionError("down")] * 3
    assert binance.get("https://data.binance.vision/x")[0] is None and not answers


# --- the job's place ----------------------------------------------------------------

def test_the_job_is_protected_and_writes_only_its_own_folder():
    from gate import check_protected
    patterns = check_protected.load_patterns(REPO / "PROTECTED.txt")
    for path in ("bot/binance.py", ".github/workflows/binance.yml", "tests/gate/test_binance.py", "state/wide/binance/status.json"):
        assert any(check_protected.matches(path, p) for p in patterns), path
    src = (REPO / "bot" / "binance.py").read_text(encoding="utf-8")
    for pat in check_protected.FORBIDDEN:
        assert not re.search(pat, src), pat
    job = yaml.safe_load((REPO / ".github" / "workflows" / "binance.yml").read_text())
    steps = job["jobs"]["collect"]["steps"]
    collect = next(s for s in steps if s.get("id") == "collect")
    assert collect["run"].strip() == "python -m bot.binance --collect"
    # a failed or stopped collect step does not stop the job: what it wrote is committed, and then the job goes red
    assert collect["continue-on-error"] is True and binance.BUDGET_S + 120 < collect["timeout-minutes"] * 60
    assert collect["timeout-minutes"] * 60 + 600 <= job["jobs"]["collect"]["timeout-minutes"] * 60
    commit = next(s for s in steps if "git commit" in s.get("run", ""))
    red = next(s for s in steps if "outcome" in str(s.get("if", "")))
    assert "if" not in commit and steps.index(collect) < steps.index(commit) < steps.index(red)
    assert red["if"].strip() == "steps.collect.outcome == 'failure'" and "exit 1" in red["run"]
    assert [ln.strip() for ln in commit["run"].splitlines() if ln.strip().startswith("git add")] == ["git add -A state/wide/binance"]
    assert "-name '*.tmp' -delete" in commit["run"].split("git add")[0]
    assert job["concurrency"]["cancel-in-progress"] is False and job["concurrency"]["group"] not in ("wide-data", "bot")


def test_nothing_in_the_hourly_loop_or_a_strategy_reads_it():
    loop = ("__init__", "run", "promote", "report", "slot", "config", "data", "paper", "risk", "shadow", "backtest", "strategy")
    for module in loop:
        src = (REPO / "bot" / f"{module}.py").read_text(encoding="utf-8")
        assert not re.search(r"\bbinance\b", src.replace("Binance", "").replace("binance.vision", "")), module
