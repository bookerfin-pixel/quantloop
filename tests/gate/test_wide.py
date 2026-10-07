"""PROTECTED. The wide data collector (bot/wide.py): which coins join the list, what is
written for them, what a failure costs, and that it stays apart from the hourly loop."""
import json
import os
import re
import shutil
import subprocess
import sys
import types
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pytest
import yaml

from bot import config, data, report, slot, wide
from tests.gate import hourly_driver

DAY = 86400
NOW = 1_791_072_000 + 40 * 60          # 2026-10-04 00:40 UTC, forty minutes after a UTC midnight
REPO = Path(__file__).resolve().parents[2]


def midnight(ts=NOW):
    return ts // DAY * DAY


class Exchange:
    """Kraken, Kraken Futures and Coinbase as far as the collector talks to them."""

    def __init__(self):
        self.pairs = {}        # AssetPairs
        self.ticker = {}       # Ticker
        self.ohlc = {}         # altname -> rows
        self.perps = []        # futures tickers
        self.funding = {}      # symbol -> rates
        self.coinbase = {}     # coin -> rows [time, low, high, open, close, volume]
        self.calls = []
        self.patience = []     # (url, tries, timeout) of every request
        self.broken = set()    # url fragments that answer with a server error
        self.refuse_whole_ticker = False
        self.coinbase_knows_nobody = False     # a bad day there: "no such product" for every coin
        self.coinbase_time_unit = 1            # 1000: it answers in milliseconds

    def coin(self, name, price=10.0, volume=1e6, spread=0.001, kraken=None, wsname=None, days=30, status="online",
             quote="ZUSD", aclass="currency", low=None, high=None, altname=None):
        key = kraken or f"{name}USD"
        alt = altname or key
        self.pairs[key] = {"altname": alt, "wsname": wsname or f"{name}/USD", "base": name, "quote": quote,
                           "aclass_base": aclass, "status": status}
        # in every pair of values the first is today's and the second the last 24 hours': only the second is ours
        self.ticker[key] = {"a": [str(price * (1 + spread)), "1", "1"], "b": [str(price * (1 - spread)), "1", "1"],
                            "c": [str(price), "1"], "v": ["7", str(volume / price)], "p": ["3", str(price)],
                            "t": [9, 500], "l": ["0.5", str(low if low is not None else price * 0.9)],
                            "h": ["99999", str(high if high is not None else price * 1.1)], "o": str(price)}
        first = midnight() - days * DAY
        rows = []
        for i in range(days + 1):                          # the last row is the day still forming
            rows.append([first + i * DAY, str(price), str(price * 1.02), str(price * 0.98), str(price), str(price), "100.5", 42 + i])
        self.ohlc[alt] = rows
        return alt

    def __call__(self, url, params=None, headers=None, tries=3, timeout=20.0):
        self.calls.append((url, dict(params or {})))
        self.patience.append((url, tries, timeout))
        if any(b in url for b in self.broken):
            return None, None, "http 503"
        params = params or {}
        # each venue at its whole address: an answer to a request sent anywhere else would hide a slip in one
        if url == "https://api.kraken.com/0/public/AssetPairs":
            return 200, {"error": [], "result": self.pairs}, ""
        if url == "https://api.kraken.com/0/public/Ticker":
            if "pair" not in params:
                if self.refuse_whole_ticker:
                    return 200, {"error": ["EGeneral:Invalid arguments"], "result": {}}, ""
                return 200, {"error": [], "result": self.ticker}, ""
            by_alt = {info["altname"]: key for key, info in self.pairs.items()}
            return 200, {"error": [], "result": {by_alt[a]: self.ticker[by_alt[a]] for a in params["pair"].split(",")}}, ""
        if url == "https://api.kraken.com/0/public/OHLC":
            if params.get("interval") != 1440:
                return 200, {"error": ["EGeneral:Invalid arguments:interval"]}, ""       # only the daily candle is ours
            if params["pair"] not in self.ohlc:
                return 200, {"error": ["EQuery:Unknown asset pair"]}, ""
            long_name = {info["altname"]: key for key, info in self.pairs.items()}.get(params["pair"], params["pair"])
            return 200, {"error": [], "result": {long_name: self.ohlc[params["pair"]], "last": 0}}, ""
        if url == "https://futures.kraken.com/derivatives/api/v3/tickers":
            return 200, {"result": "success", "tickers": self.perps}, ""
        if url == "https://futures.kraken.com/derivatives/api/v3/historical-funding-rates":
            if params["symbol"] not in self.funding:
                return 400, {"result": "error"}, ""
            return 200, {"result": "success", "rates": self.funding[params["symbol"]]}, ""
        if url.startswith("https://api.exchange.coinbase.com/products/") and url.endswith("-USD/candles"):
            coin = url.split("/products/")[1].split("-USD")[0]
            if coin not in self.coinbase or self.coinbase_knows_nobody:
                return 404, {"message": "NotFound"}, ""
            lo = datetime.fromisoformat(params["start"]).timestamp()
            hi = datetime.fromisoformat(params["end"]).timestamp()
            if (hi - lo) / params["granularity"] > 300:      # as the venue does: more than 300 candles is refused
                return 400, {"message": "granularity too small for the requested time range"}, ""
            return 200, [[r[0] * self.coinbase_time_unit] + r[1:] for r in reversed(self.coinbase[coin]) if lo <= r[0] <= hi], ""
        if url in ("https://data-api.binance.vision/api/v3/klines",
                   "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1d/BTCUSDT-1d-2026-08.zip.CHECKSUM"):
            return 451, None, "not JSON, 0 bytes"
        raise AssertionError(f"unexpected request {url}")


@pytest.fixture
def world(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STATE", tmp_path / "state")
    monkeypatch.setattr(config, "CONFIGS", tmp_path / "configs")
    (tmp_path / "configs").mkdir()
    (tmp_path / "state").mkdir()
    ex = Exchange()
    monkeypatch.setattr(wide, "fetch", ex)
    monkeypatch.setattr(wide, "_sleep", lambda s: None)
    monkeypatch.setattr(wide, "_now", lambda: NOW)
    write_settings()                                   # as in the repo: the file is there and says what the defaults say
    return ex


def write_settings(**kw):
    (config.CONFIGS / "wide.yaml").write_text(yaml.safe_dump({**wide.DEFAULTS, **kw}))


def rates(symbol_days, per_hour=0.0001, hours=24, start=None):
    start = midnight() - symbol_days * DAY if start is None else start
    out = []
    for h in range(symbol_days * 24):
        if h % 24 < hours:
            ts = datetime.fromtimestamp(start + h * 3600, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            out.append({"timestamp": ts, "fundingRate": per_hour * 100, "relativeFundingRate": per_hour})
    return out


# --- settings -------------------------------------------------------------------

def test_the_settings_file_in_the_repo_always_gives_settings_that_can_be_used(monkeypatch):
    """Whatever the file says, slip or no slip: a slip there must not turn this suite red, because the
    gate runs it on every agent PR and the note that reports the slip is one of them. The collector
    names a slip itself (SETTING NOT USED); what is held here is that it always has usable settings."""
    monkeypatch.setattr(config, "CONFIGS", REPO / "configs")
    st, notes = wide.settings()
    assert set(st) == set(wide.DEFAULTS) and isinstance(notes, list)
    assert st["top_n"] >= 1 and st["history_days"] >= 1 and st["funding_top_n"] >= 0 and st["deepen_budget_s"] >= 0
    assert isinstance(st["exclude"], list) and all(isinstance(x, str) and x == x.upper() for x in st["exclude"])


def test_a_missing_settings_file_means_the_defaults_and_says_so(world):
    (config.CONFIGS / "wide.yaml").unlink()
    st, notes = wide.settings()
    assert st["top_n"] == wide.DEFAULTS["top_n"] and st["exclude"] == wide.DEFAULTS["exclude"]
    assert notes == ["configs/wide.yaml is missing; the defaults are used"]


@pytest.mark.parametrize("key, bad", [("top_n", 0), ("top_n", 2.5), ("top_n", -3), ("top_n", "many"), ("top_n", True),
                                      ("top_n", float("inf")), ("top_n", float("nan")), ("top_n", None),
                                      ("history_days", 0), ("funding_top_n", 1.5), ("deepen_budget_s", -1),
                                      ("min_usd_volume", "none"), ("exclude", "USDT"), ("exclude", [1, 2]),
                                      ("top_n", 10 ** 400), ("min_usd_volume", 10 ** 400), ("deepen_budget_s", -10 ** 400),
                                      ("deepen_budget_s", 601), ("deepen_budget_s", 86400)])
def test_a_setting_that_cannot_be_used_falls_back_and_is_named(world, key, bad):
    write_settings(**{key: bad})
    st, notes = wide.settings()
    assert st[key] == wide.DEFAULTS[key]
    assert len(notes) == 1 and f"`{key}" in notes[0] and "is used" in notes[0]


def test_settings_that_can_be_used_are(world):
    write_settings(top_n=5, funding_top_n=0, history_days=900, deepen_budget_s=0, min_usd_volume=1.5, exclude=["usdt", " eur "])
    st, notes = wide.settings()
    assert notes == []
    assert (st["top_n"], st["funding_top_n"], st["history_days"], st["deepen_budget_s"], st["min_usd_volume"]) == (5, 0, 900, 0, 1.5)
    assert st["exclude"] == ["USDT", "EUR"]
    write_settings(deepen_budget_s=600, top_n=10 ** 9)                    # the most the older history may be given; and a list with no end
    st, notes = wide.settings()
    assert notes == [] and st["deepen_budget_s"] == 600 == wide.DEEPEN_BUDGET_MAX_S and st["top_n"] == 10 ** 9


def test_a_missing_line_and_an_unknown_line_are_both_named(world):
    kept = {k: v for k, v in wide.DEFAULTS.items() if k not in ("top_n", "exclude")}
    (config.CONFIGS / "wide.yaml").write_text(yaml.safe_dump({**kept, "top": 50}))
    st, notes = wide.settings()
    assert st["top_n"] == 100
    assert sorted(notes) == sorted(["`top_n` is not in configs/wide.yaml; 100 is used",
                                    "`exclude` is not in configs/wide.yaml; the default list is used",
                                    "`top` in configs/wide.yaml is not a setting this code reads"])


@pytest.mark.parametrize("text", ["- a\n- b\n", "top_n: [1\n", "just words"])
def test_a_settings_file_that_is_not_settings_means_the_defaults(world, text):
    (config.CONFIGS / "wide.yaml").write_text(text)
    st, notes = wide.settings()
    assert st["top_n"] == 100 and len(notes) == 1 and "the defaults are used" in notes[0]


def test_the_defaults_are_never_handed_out_to_be_changed(world):
    for case in ("no file", "a file with no `exclude` line"):
        (config.CONFIGS / "wide.yaml").unlink()
        if case != "no file":
            (config.CONFIGS / "wide.yaml").write_text(yaml.safe_dump({k: v for k, v in wide.DEFAULTS.items() if k != "exclude"}))
        st, _ = wide.settings()
        st["exclude"].append("ZZZ")
        assert "ZZZ" not in wide.DEFAULTS["exclude"] and "ZZZ" not in wide.settings()[0]["exclude"], case
        write_settings()


# --- one request ----------------------------------------------------------------

class Answer:
    def __init__(self, status, body=None, raw=b"x"):
        self.status_code, self._body, self.content = status, body, raw

    def json(self):
        if self._body is None:
            raise ValueError("not json")
        return self._body


def test_a_request_is_tried_again_only_when_that_can_help(monkeypatch):
    monkeypatch.setattr(wide, "_sleep", lambda s: None)
    script = []

    sent, waits = [], []

    def get(url, params=None, headers=None, timeout=None):
        sent.append((url, params, headers, timeout))
        step = script.pop(0)
        if isinstance(step, Exception):
            raise step
        return step
    monkeypatch.setattr(wide.requests, "get", get)
    monkeypatch.setattr(wide, "_sleep", waits.append)
    script[:] = [Answer(503), Answer(429), Answer(200, {"ok": 1})]
    assert wide.fetch("u", {"pair": "SOLUSD"}) == (200, {"ok": 1}, "") and script == []     # a failing server and a slow down are waited out
    assert [s[:2] for s in sent] == [("u", {"pair": "SOLUSD"})] * 3                         # what was asked goes out each time
    assert all(s[2] == {"User-Agent": "quantloop/1.0"} and 0 < s[3] <= 60 for s in sent)    # with a name, and a limit on the wait
    assert waits == [3.0, 6.0]                                                              # longer each time
    sent.clear()
    assert wide.fetch("u", headers={"X": "1"}, timeout=5)[0] is None and sent[0][2:] == ({"X": "1"}, 5)
    waits.clear()
    script[:] = [ConnectionError("down"), Answer(200, [1])]
    assert wide.fetch("u") == (200, [1], "") and script == []
    script[:] = [Answer(404, {"message": "NotFound"}), Answer(200, {})]
    assert wide.fetch("u") == (404, {"message": "NotFound"}, "") and len(script) == 1      # "no such thing" is an answer
    script[:] = [Answer(400, {"e": 1}), Answer(200, {})]
    assert wide.fetch("u")[0] == 400 and len(script) == 1
    script[:] = [Answer(200, None, b"abc"), Answer(200, {})]
    assert wide.fetch("u") == (200, None, "not JSON, 3 bytes") and len(script) == 1
    script[:] = [Answer(500), Answer(502), Answer(503), Answer(200, {})]
    assert wide.fetch("u") == (None, None, "http 503") and len(script) == 1          # three tries, no more
    script[:] = [TimeoutError("slow")] * 3
    waits.clear()
    status, body, note = wide.fetch("u")
    assert (status, body) == (None, None) and note.startswith("TimeoutError: slow") and waits == [2.0, 4.0, 6.0]
    script[:] = [Answer(503), Answer(200, {})]
    assert wide.fetch("u", tries=1) == (None, None, "http 503") and len(script) == 1
    # one request may hang for twenty seconds, three times: the allowances of time in bot/wide.py are sized on that
    script[:] = [Answer(200, {})]
    sent.clear()
    wide.fetch("u")
    assert sent[0][3] == 20.0


def test_kraken_slowing_us_down_is_waited_out_and_a_refusal_is_not(world, monkeypatch):
    answers = [(200, {"error": ["EGeneral:Too many requests"]}, ""), (200, {"error": ["EAPI:Rate limit exceeded"]}, ""),
               (200, {"error": [], "result": {"ok": 1}}, "")]
    asked, waits = [], []
    monkeypatch.setattr(wide, "fetch", lambda url, params=None, **k: (asked.append((url, params)), answers.pop(0))[1])
    monkeypatch.setattr(wide, "_sleep", waits.append)
    assert wide.kraken("OHLC", {"pair": "SOLUSD", "interval": 1440}) == {"ok": 1} and answers == []
    assert asked == [("https://api.kraken.com/0/public/OHLC", {"pair": "SOLUSD", "interval": 1440})] * 3
    assert waits == [6.0, 12.0, 1.0]                    # a longer wait each time it says slow down, and a pause after every answer
    answers, waits[:] = [(200, {"error": [], "result": {"ok": 2}}, "")], []
    assert wide.kraken("Ticker") == {"ok": 2} and waits == [1.0]    # one call a second is what Kraken says stays inside its limits
    answers = [(200, {"error": ["EQuery:Unknown asset pair"]}, ""), (200, {"error": [], "result": {}}, "")]
    monkeypatch.setattr(wide, "fetch", lambda *a, **k: answers.pop(0))
    waits.clear()
    with pytest.raises(wide.WideError, match="Unknown asset pair"):
        wide.kraken("OHLC", {"pair": "NOPE"})
    assert len(answers) == 1 and waits == [1.0]                                   # asked once, and a refusal is paused after too
    monkeypatch.setattr(wide, "fetch", lambda *a, **k: (None, None, "ConnectionError: down"))
    waits.clear()
    with pytest.raises(wide.WideError, match="kraken Ticker: ConnectionError: down"):
        wide.kraken("Ticker")
    assert waits == [1.0]
    monkeypatch.setattr(wide, "fetch", lambda *a, **k: (200, {"error": [], "result": ["a list"]}, ""))
    with pytest.raises(wide.WideError, match="kraken Ticker: no result"):
        wide.kraken("Ticker")
    # told to slow down three times running: it gives up, having waited longer each time and once more at the end
    monkeypatch.setattr(wide, "fetch", lambda *a, **k: (200, {"error": ["EGeneral:Too many requests"]}, ""))
    waits.clear()
    with pytest.raises(wide.WideError, match="Too many requests"):
        wide.kraken("OHLC", {"pair": "SOLUSD", "interval": 1440})
    assert waits == [6.0, 12.0, 18.0, 1.0]


# --- the list -------------------------------------------------------------------

def test_coin_names():
    assert wide.coin_name("XBT/USD", "XBTUSD") == "BTC"
    assert wide.coin_name("XDG/USD", "XDGUSD") == "DOGE"
    assert wide.coin_name("SOL/USD", "SOLUSD") == "SOL"
    assert wide.coin_name("sol/USD", None) == "SOL"
    assert wide.coin_name(None, "ADAUSD") == "ADA"
    assert wide.coin_name(None, "ADAEUR") is None
    assert wide.coin_name("../x/USD", None) is None           # nothing that is not a plain name becomes a file name
    assert wide.coin_name("A.B/USD", None) is None
    assert wide.coin_name("AVERYLONGCOINNAME1/USD", None) is None
    assert wide.coin_name("CON/USD", None) is None and wide.coin_name("nul/USD", None) is None and wide.coin_name("COM1/USD", None) is None
    assert wide.coin_name("LPT1/USD", None) is None and wide.coin_name("lpt9/USD", None) is None and wide.coin_name("PRN/USD", None) is None
    assert wide.coin_name("AUX/USD", None) is None and wide.coin_name("COM9/USD", None) is None
    assert wide.coin_name("LPT/USD", None) == "LPT" and wide.coin_name("COM10/USD", None) == "COM10" and wide.coin_name("NA/USD", None) == "NA"
    assert wide.coin_name(None, None) is None and wide.coin_name("/USD", None) is None


def test_only_coins_quoted_in_dollars_and_not_excluded_are_pairs(world):
    world.coin("SOL")
    world.coin("BTC", kraken="XXBTZUSD", wsname="XBT/USD", altname="XBTUSD")
    world.coin("ETH", quote="XXBT", kraken="ETHXBT", wsname="ETH/XBT")       # not quoted in dollars
    world.coin("USDT")                                                        # a dollar token
    world.coin("AAPLX", aclass="tokenized_asset")                             # a tokenised share
    world.coin("OLD", status="delisted")
    world.coin("ADA", quote="USD")
    pairs = wide.usd_pairs(world.pairs, ["usdt"])
    assert sorted(pairs) == ["ADA", "BTC", "SOL"]
    assert pairs["BTC"] == {"kraken": "XXBTZUSD", "altname": "XBTUSD", "wsname": "XBT/USD"}
    assert wide.usd_pairs({"X": "not a pair", "Y": {"quote": "ZUSD"}}, []) == {}


def test_a_pair_the_venue_has_only_slowed_is_still_listed(world):
    """Kraken puts a pair into post only, limit only, reduce only or cancel only for a while; it is not gone."""
    for i, status in enumerate(("online", "post_only", "limit_only", "reduce_only", "cancel_only")):
        world.coin(f"S{i}", status=status)
    world.coin("GONE", status="delisted")
    world.coin("ODD", status="work_in_progress")
    del world.pairs["S0USD"]["status"]                                              # no word on it: taken as open
    assert sorted(wide.usd_pairs(world.pairs, [])) == ["S0", "S1", "S2", "S3", "S4"]


def test_the_ticker_ranks_by_dollars_traded_and_drops_unusable_quotes(world):
    world.coin("SOL", price=100.0, volume=5e6, spread=0.0005)
    world.coin("ADA", price=0.5, volume=9e6, spread=0.002)
    world.coin("DEAD", volume=1e7)
    world.ticker["DEADUSD"]["b"] = ["0", "1", "1"]                            # no bid
    world.coin("CROSS", volume=1e7)
    world.ticker["CROSSUSD"]["b"], world.ticker["CROSSUSD"]["a"] = ["11", "1", "1"], ["10", "1", "1"]
    world.coin("GONE", volume=1e7)
    del world.ticker["GONEUSD"]
    world.coin("ODD", volume=1e7)
    world.ticker["ODDUSD"] = {"a": []}                                         # not a ticker entry
    rows = wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)
    assert [(r["pair"], r["rank"]) for r in rows] == [("ADA", 1), ("SOL", 2)]
    world.coin("ZED", price=2.0, volume=5e6)                                  # traded exactly as much as SOL, and sent before AAB
    world.coin("AAB", price=4.0, volume=5e6)
    again = wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)
    assert [(r["pair"], r["rank"]) for r in again] == [("ADA", 1), ("AAB", 2), ("SOL", 3), ("ZED", 4)]     # by name among equals
    assert rows[0]["usd_volume_24h"] == pytest.approx(9e6) and rows[1]["usd_volume_24h"] == pytest.approx(5e6)
    assert rows[0]["half_spread_bps"] == pytest.approx(20.0) and rows[1]["half_spread_bps"] == pytest.approx(5.0)
    assert not rows[0]["pegged"]
    # the 24 hour figures, not the ones for the UTC day so far
    assert rows[1]["volume_24h"] == pytest.approx(5e4) and rows[1]["vwap_24h"] == pytest.approx(100.0) and rows[1]["trades_24h"] == 500
    assert rows[1]["bid"] == pytest.approx(99.95) and rows[1]["ask"] == pytest.approx(100.05) and rows[1]["last"] == pytest.approx(100.0)


def test_a_locked_book_is_a_quote_and_dollars_traded_go_by_the_days_average_price(world):
    world.coin("LOCK", price=10.0, volume=1e6)
    world.ticker["LOCKUSD"]["b"] = world.ticker["LOCKUSD"]["a"] = ["10.0", "1", "1"]          # bid and ask the same
    world.coin("MOVED", price=10.0, volume=1e6)
    world.ticker["MOVEDUSD"]["c"] = ["20.0", "1"]                                             # it ended the day at twice its average
    world.coin("NOAVG", price=10.0, volume=1e6)
    world.ticker["NOAVGUSD"]["p"] = ["3", "0"]                                                # no 24 hour average on offer
    world.ticker["NOAVGUSD"]["c"] = ["8.0", "1"]
    world.coin("NOLAST", price=10.0, volume=1e6)
    world.ticker["NOLASTUSD"]["p"], world.ticker["NOLASTUSD"]["c"] = ["3", "0"], ["0", "1"]   # nor a last trade: the mid stands in
    rows = {r["pair"]: r for r in wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)}
    assert rows["LOCK"]["half_spread_bps"] == 0.0 and rows["LOCK"]["bid"] == rows["LOCK"]["ask"] == 10.0
    assert rows["MOVED"]["usd_volume_24h"] == pytest.approx(1e6)                               # 100,000 coins at 10, not at 20
    assert rows["NOAVG"]["usd_volume_24h"] == pytest.approx(8e5) and rows["NOLAST"]["usd_volume_24h"] == pytest.approx(1e6)


def test_two_pairs_for_one_coin_the_plainer_name_is_kept_whichever_comes_first(world):
    a = {"altname": "XBTUSD", "wsname": "XBT/USD", "quote": "ZUSD", "status": "online"}
    b = {"altname": "BTCUSD", "wsname": "BTC/USD", "quote": "ZUSD", "status": "online"}
    for pairs in ({"XXBTZUSD": a, "BTCUSD": b}, {"BTCUSD": b, "XXBTZUSD": a}):
        assert wide.usd_pairs(pairs, []) == {"BTC": {"kraken": "BTCUSD", "altname": "BTCUSD", "wsname": "BTC/USD"}}


def test_a_coin_that_sits_at_a_dollar_all_day_is_taken_for_a_dollar_token(world):
    world.coin("NEWUSD", price=1.001, low=0.999, high=1.004, volume=5e7)
    world.coin("REAL", price=1.01, low=0.93, high=1.06, volume=1e6)            # near a dollar, but it moves
    world.coin("FAR", price=1.2, low=1.199, high=1.201, volume=1e6)            # quiet, but not at a dollar
    world.coin("EDGE", price=1.029, low=1.02, high=1.035, volume=1e6)          # just inside the price band: a dollar token
    world.coin("OVER", price=1.031, low=1.03, high=1.035, volume=1e6)          # just past it: not one
    world.coin("UNDER", price=0.969, low=0.968, high=0.970, volume=1e6)        # nor just below it
    world.coin("CALM", price=1.0, low=0.9905, high=1.0095, volume=1e6)         # a day's range just inside 2%: one
    world.coin("LIVELY", price=1.0, low=0.9895, high=1.0105, volume=1e6)       # just outside: not one
    rows = {r["pair"]: r for r in wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)}
    assert rows["NEWUSD"]["pegged"] and not rows["REAL"]["pegged"] and not rows["FAR"]["pegged"]
    assert rows["EDGE"]["pegged"] and not rows["OVER"]["pegged"] and not rows["UNDER"]["pegged"]
    assert rows["CALM"]["pegged"] and not rows["LIVELY"]["pegged"]


def test_the_most_traded_join_the_list_and_none_leaves(world):
    for i, name in enumerate(["AAA", "BBB", "CCC", "DDD"]):
        world.coin(name, volume=1e6 * (10 - i))
    world.coin("THIN", volume=100.0)
    world.coin("PEG", price=1.0, low=1.0, high=1.0, volume=1e9)
    st = {**wide.DEFAULTS, "top_n": 2}
    pairs = wide.usd_pairs(world.pairs, [])
    uni = {"pairs": {}}
    assert wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW) == ["AAA", "BBB"]
    a = uni["pairs"]["AAA"]
    assert a["since"] == "2026-10-04" and a["joined_at"] == NOW and a["listed"] and a["rank"] == 2
    assert a["kraken"] == "AAAUSD" and a["altname"] == "AAAUSD" and a["usd_volume_24h"] == pytest.approx(1e7)
    assert uni["updated"] == NOW
    # the next day the ranking turns over: the new leaders join, the old ones stay
    for name, v in [("AAA", 1.0), ("BBB", 2.0), ("CCC", 9e6), ("DDD", 8e6)]:
        world.coin(name, volume=v)
    pairs = wide.usd_pairs(world.pairs, [])
    assert wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + DAY) == ["CCC", "DDD"]
    assert sorted(uni["pairs"]) == ["AAA", "BBB", "CCC", "DDD"]
    assert uni["pairs"]["AAA"]["since"] == "2026-10-04" and uni["pairs"]["AAA"]["joined_at"] == NOW
    assert uni["pairs"]["CCC"]["since"] == "2026-10-05" and uni["pairs"]["CCC"]["joined_at"] == NOW + DAY
    assert "THIN" not in uni["pairs"] and "PEG" not in uni["pairs"]
    # a coin on the list has its rank and its dollars traded brought up to date every day
    assert uni["pairs"]["AAA"]["rank"] == 6 and uni["pairs"]["AAA"]["usd_volume_24h"] == pytest.approx(1.0)
    assert uni["pairs"]["CCC"]["rank"] == 2 and uni["pairs"]["AAA"]["last_seen"] == "2026-10-05" and uni["updated"] == NOW + DAY


def test_a_coin_that_trades_too_little_does_not_join_whatever_its_rank(world):
    world.coin("BIG", volume=60_000.0)
    world.coin("SMALL", volume=40_000.0)
    world.coin("EXACT", volume=50_000.0)
    pairs = wide.usd_pairs(world.pairs, [])
    uni = {"pairs": {}}
    assert wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), dict(wide.DEFAULTS), NOW) == ["BIG", "EXACT"]
    uni = {"pairs": {}}
    assert wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), {**wide.DEFAULTS, "min_usd_volume": 0}, NOW) == \
        ["BIG", "EXACT", "SMALL"]


def test_a_coin_taken_off_the_venue_stays_on_the_list_marked(world):
    world.coin("AAA")
    world.coin("BBB")
    st = {**wide.DEFAULTS}
    pairs = wide.usd_pairs(world.pairs, [])
    uni = {"pairs": {}}
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW)
    del world.pairs["BBBUSD"], world.ticker["BBBUSD"]
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + DAY)
    assert uni["pairs"]["BBB"]["listed"] is False and uni["pairs"]["BBB"]["unlisted_since"] == "2026-10-05"
    assert uni["pairs"]["BBB"]["last_seen"] == "2026-10-04"
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 2 * DAY)
    assert uni["pairs"]["BBB"]["unlisted_since"] == "2026-10-05"                # the first day it was gone, kept
    assert "gaps" not in uni["pairs"]["BBB"] and "gaps" not in uni["pairs"]["AAA"]
    world.coin("BBB")                                                           # and it can come back
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 3 * DAY)
    assert uni["pairs"]["BBB"]["listed"] is True and "unlisted_since" not in uni["pairs"]["BBB"]
    assert uni["pairs"]["BBB"]["since"] == "2026-10-04"
    # the time it was away is kept: a name that returns may not be the coin that left
    assert uni["pairs"]["BBB"]["gaps"] == [["2026-10-05", "2026-10-07"]] and "gaps" not in uni["pairs"]["AAA"]
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 4 * DAY)
    assert uni["pairs"]["BBB"]["gaps"] == [["2026-10-05", "2026-10-07"]]        # written once
    del world.pairs["BBBUSD"]
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 5 * DAY)
    world.coin("BBB")
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 9 * DAY)
    assert uni["pairs"]["BBB"]["gaps"] == [["2026-10-05", "2026-10-07"], ["2026-10-09", "2026-10-13"]]
    del world.pairs["BBBUSD"]                                                   # gone from one answer and back in the next, the same day
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 10 * DAY)
    world.coin("BBB")
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), st, NOW + 10 * DAY + 3600)
    assert uni["pairs"]["BBB"]["gaps"][2:] == [["2026-10-14", "2026-10-14"]]    # is on record too


def test_a_pair_the_venue_renames_is_followed(world):
    world.coin("AAA", kraken="XAAAZUSD", altname="AAAUSD")
    pairs = wide.usd_pairs(world.pairs, [])
    uni = {"pairs": {}}
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), dict(wide.DEFAULTS), NOW)
    assert (uni["pairs"]["AAA"]["kraken"], uni["pairs"]["AAA"]["altname"]) == ("XAAAZUSD", "AAAUSD")
    world.pairs, world.ticker, world.ohlc = {}, {}, {}
    world.coin("AAA", kraken="AAA2USD", altname="AAA2USD", wsname="AAA/USD", days=3)
    pairs = wide.usd_pairs(world.pairs, [])
    wide.update_universe(uni, pairs, wide.read_ticker(pairs, world.ticker), dict(wide.DEFAULTS), NOW + DAY)
    assert (uni["pairs"]["AAA"]["kraken"], uni["pairs"]["AAA"]["altname"]) == ("AAA2USD", "AAA2USD")
    assert uni["pairs"]["AAA"]["listed"] is True and uni["pairs"]["AAA"]["since"] == "2026-10-04"
    read, added, failed = wide.collect_daily(uni, NOW)
    assert (read, added, failed) == (1, 3, [])                                  # and its candles are asked for by the new name


def test_a_damaged_list_is_never_started_again_over(world):
    wide.root().mkdir(parents=True)
    (wide.root() / "universe.json").write_text('{"pairs": {"AAA": ')
    with pytest.raises(wide.WideError, match="universe.json cannot be read"):
        wide.load_universe()
    for text in ('["AAA"]', '{"pairs": ["AAA"]}', '{"pairs": {"AAA": null}}', '{"pairs": {"AAA": "since yesterday"}}'):
        (wide.root() / "universe.json").write_text(text)
        with pytest.raises(wide.WideError, match="not a list of pairs"):
            wide.load_universe()
    world.coin("AAA")
    with pytest.raises(wide.WideError):
        wide.collect(NOW)
    assert (wide.root() / "universe.json").read_text() == '{"pairs": {"AAA": "since yesterday"}}'      # left as it was found
    assert not (wide.root() / "status.json").exists()


# --- candles --------------------------------------------------------------------

def test_only_closed_utc_days_are_candles(world):
    alt = world.coin("SOL", days=5)
    world.ohlc[alt].append([midnight() - 2 * DAY + 3600, "1", "1", "1", "1", "1", "1", 1])    # two days ago, but not a midnight
    world.ohlc[alt].append([midnight() - 40 * DAY, "1", "1", "1", "0", "1", "1", 1])          # no close
    world.ohlc[alt].append([midnight() - 41 * DAY, "1", "1", "1", "junk", "1", "1", 1])       # not a number
    world.ohlc[alt].append(["when", "1", "1", "1", "1", "1", "1", 1])                         # no time
    world.ohlc[alt].append([None, "1", "1", "1", "1", "1", "1", None])
    world.ohlc[alt].append([0, "1", "1", "1", "1", "1", "1", 1])                              # a midnight, in 1970
    world.ohlc[alt].append([wide.FIRST_DAY - DAY, "1", "1", "1", "1", "1", "1", 1])           # the day before there was a coin
    world.ohlc[alt][0][7] = None                                                              # a candle with no trade count
    df = wide.kraken_daily(alt, NOW)
    assert len(df) == 5 and int(df["count"].iloc[0]) == 0 and str(df["count"].dtype) == "int64"
    world.ohlc[alt][0][7] = 42
    df = wide.kraken_daily(alt, NOW)
    assert int(df["time"].max()) == midnight() - DAY                    # yesterday is the newest closed day
    assert (df["time"] % DAY == 0).all() and (df["source"] == "kraken").all()
    assert list(df.columns) == wide.DAILY_COLUMNS
    assert list(df["count"]) == [42, 43, 44, 45, 46]                    # the venue's trade count is kept
    row = df.iloc[0]
    assert (row["open"], row["high"], row["low"], row["close"], row["vwap"], row["volume"]) == \
        (pytest.approx(10.0), pytest.approx(10.2), pytest.approx(9.8), pytest.approx(10.0), pytest.approx(10.0), pytest.approx(100.5))
    # the day is closed the second it ends, and not a second before
    assert int(wide.kraken_daily(alt, midnight())["time"].max()) == midnight() - DAY
    assert int(wide.kraken_daily(alt, midnight() - 1)["time"].max()) == midnight() - 2 * DAY
    assert int(wide.kraken_daily(alt, midnight() + DAY)["time"].max()) == midnight()


def test_an_answer_whose_rows_are_no_daily_candles_is_a_failure_and_a_day_with_nothing_closed_is_not(world):
    alt = world.coin("SOL", days=5)
    world.ohlc[alt] = [[r[0] * 1000] + r[1:] for r in world.ohlc[alt]]               # times in another unit
    with pytest.raises(wide.WideError, match="kraken OHLC SOLUSD: 6 rows and none is a daily candle"):
        wide.kraken_daily(alt, NOW)
    world.ohlc[alt] = [[d * DAY, "10", "10", "10", "10", "10", "1", 1] for d in (0, 1, 365)]     # days counted from 1970, or no times at all
    with pytest.raises(wide.WideError, match="kraken OHLC SOLUSD: 3 rows and none is a daily candle"):
        wide.kraken_daily(alt, NOW)
    world.ohlc[alt] = [[wide.FIRST_DAY, "10", "10", "10", "10", "10", "1", 1]]       # the first day there was a coin is a day
    assert list(wide.kraken_daily(alt, NOW)["time"]) == [wide.FIRST_DAY] and wide.FIRST_DAY == 14247 * DAY
    world.ohlc[alt] = [[midnight(), "10", "10", "10", "10", "10", "1", 1]]           # listed today: only the day still forming
    assert len(wide.kraken_daily(alt, NOW)) == 0
    world.ohlc[alt] = []
    assert len(wide.kraken_daily(alt, NOW)) == 0                                     # and no rows at all is nothing new
    uni = {"pairs": {"SOL": {"listed": True, "altname": alt}}}
    world.ohlc[alt] = [[(midnight() - DAY) * 1000, "10", "10", "10", "10", "10", "1", 1]]
    read, added, failed = wide.collect_daily(uni, NOW)
    assert (read, added) == (0, 0) and failed == ["SOL: kraken OHLC SOLUSD: 1 rows and none is a daily candle"]


def test_candles_are_added_once_and_kraken_stands_over_coinbase(world):
    alt = world.coin("SOL", days=5)
    assert wide.merge_daily("SOL", wide.kraken_daily(alt, NOW)) == 5
    assert wide.merge_daily("SOL", wide.kraken_daily(alt, NOW)) == 0
    before = wide.daily_path("SOL").read_text()
    wide.merge_daily("SOL", wide.kraken_daily(alt, NOW))
    assert wide.daily_path("SOL").read_text() == before                 # nothing rewritten differently
    other = wide.load_daily("SOL").tail(2).copy()
    other["close"], other["source"] = 999.0, "coinbase"
    older = other.head(1).copy()
    older["time"] = midnight() - 9 * DAY
    assert wide.merge_daily("SOL", pd.concat([other, older])) == 1
    df = wide.load_daily("SOL")
    assert df["time"].is_monotonic_increasing and df["time"].is_unique and len(df) == 6
    assert list(df["source"]) == ["coinbase"] + ["kraken"] * 5
    assert (df.loc[df["source"] == "kraken", "close"] != 999.0).all()
    # and the other way round: a Kraken row replaces a Coinbase row for the same day
    fix = df.head(1).copy()
    fix["close"], fix["source"] = 5.0, "kraken"
    assert wide.merge_daily("SOL", fix) == 0
    assert wide.load_daily("SOL").iloc[0]["close"] == 5.0 and wide.load_daily("SOL").iloc[0]["source"] == "kraken"
    # of two readings of a day from one venue, the newer stands
    again = fix.copy()
    again["close"] = 6.0
    assert wide.merge_daily("SOL", again) == 0 and wide.load_daily("SOL").iloc[0]["close"] == 6.0


def test_rows_on_file_are_never_written_back_a_digit_off(world):
    """Long numbers (a mean of three prices, a sum of funding rates) must survive being read and written again."""
    alt = world.coin("SOL", days=3)
    wide.merge_daily("SOL", wide.kraken_daily(alt, NOW))
    cb = pd.DataFrame({"time": [midnight() - (300 - i) * DAY for i in range(200)]})
    cb["high"], cb["low"], cb["close"] = [103.09 + i * 0.37 for i in range(200)], [97.09 + i * 0.29 for i in range(200)], [100.09 + i * 0.31 for i in range(200)]
    cb["open"], cb["volume"], cb["count"], cb["source"] = cb["close"], 0.1 + 1 / 3, 0, "coinbase"
    cb["vwap"] = (cb["high"] + cb["low"] + cb["close"]) / 3
    wide.merge_daily("SOL", cb)
    first = wide.daily_path("SOL").read_text()
    assert any(len(cell) >= 17 for line in first.splitlines()[1:] for cell in line.split(","))      # the long numbers are there
    world.ohlc[alt].append([midnight() + DAY, "10", "10", "10", "10", "10", "1", 1])
    assert wide.merge_daily("SOL", wide.kraken_daily(alt, NOW + DAY)) == 1                            # the next day adds a row
    second = wide.daily_path("SOL").read_text()
    assert second.splitlines()[:len(first.splitlines())] == first.splitlines()                        # and changes no old one
    f = pd.DataFrame({"time": [midnight() - (9 - i) * DAY for i in range(8)], "hours": 24,
                      "relative_sum": [0.1 + i / 7 for i in range(8)], "absolute_sum": [1 / 3 + i / 9 for i in range(8)]})
    wide.merge_funding("PF_XBTUSD", f)
    first = wide.funding_path("PF_XBTUSD").read_text()
    wide.merge_funding("PF_XBTUSD", f.tail(1).assign(time=midnight() - DAY))
    assert wide.funding_path("PF_XBTUSD").read_text().splitlines()[:9] == first.splitlines()


def test_an_empty_cell_on_file_is_no_value_and_stays_one(world):
    alt = world.coin("SOL", days=3)
    wide.merge_daily("SOL", wide.kraken_daily(alt, NOW))
    lines = wide.daily_path("SOL").read_text().splitlines()
    cells = lines[2].split(",")
    cells[5] = ""                                                         # the second day has no vwap on file
    wide.daily_path("SOL").write_text("\n".join(lines[:2] + [",".join(cells)] + lines[3:]) + "\n")
    df = wide.load_daily("SOL")
    assert str(df["vwap"].dtype) == "float64" and df["vwap"].isna().tolist() == [False, True, False]
    world.ohlc[alt].append([midnight() + DAY, "10", "10", "10", "10", "10", "1", 1])
    served = world.ohlc[alt]
    world.ohlc[alt] = [r for r in served if r[0] != int(cells[0])]         # a day the venue no longer serves
    assert wide.merge_daily("SOL", wide.kraken_daily(alt, NOW + DAY)) == 1    # the next day is added all the same
    again = wide.daily_path("SOL").read_text().splitlines()
    assert again[2] == ",".join(cells) and len(again) == 5                 # and the cell is left empty
    assert wide.panel("vwap")["SOL"].isna().tolist() == [False, True, False, False]
    world.ohlc[alt] = served                                               # while the venue still serves the day, its reading mends it
    assert wide.merge_daily("SOL", wide.kraken_daily(alt, NOW + DAY)) == 0 and wide.load_daily("SOL")["vwap"].notna().all()


def test_candles_have_an_allowance_of_time(world, monkeypatch):
    """A venue that hangs on every request must stop the run with a reason, inside the job's time, not run it
    into GitHub's limit: a cancelled job commits nothing and says nothing."""
    names = ["AAA", "BBB", "CCC", "DDD", "EEE"]
    for name in names:
        world.coin(name, days=4)
    uni = {"pairs": {c: {"listed": True, "altname": f"{c}USD"} for c in names}}
    clock = iter(range(0, 10 ** 6, 300))                                  # each look at the clock is five minutes on
    monkeypatch.setattr(wide, "_clock", lambda: next(clock))
    read, added, failed = wide.collect_daily(uni, NOW)
    assert (read, added) == (2, 8) and wide.CANDLES_BUDGET_S == 720       # two pairs fit in twelve minutes at five minutes a look
    assert failed == [f"{c}: not asked, the time allowed for candles had run out" for c in ("CCC", "DDD", "EEE")]
    assert [p["pair"] for u, p in world.calls if u.endswith("/OHLC")] == ["AAAUSD", "BBBUSD"]      # the rest were not asked at all
    clock = iter([0] + [720] * 9)                                         # exactly the allowance is still inside it
    assert wide.collect_daily(uni, NOW)[0] == 5
    # a long list is given two and a half seconds a pair, so that a healthy run is never cut short;
    # the job's own limit (wide.yml) is sized for the longest list Kraken could give
    assert [wide.candles_budget(n) for n in (0, 100, 288, 289, 600, 700, 5000)] == [720, 720, 720, 722.5, 1500, 1750, 1750]
    names = [f"P{i:03d}" for i in range(400)]
    for name in names:
        world.coin(name, days=2)
    uni = {"pairs": {c: {"listed": True, "altname": f"{c}USD"} for c in names}}
    uni["pairs"]["GONE"] = {"listed": False, "altname": "GONEUSD"}        # a coin that left does not earn the others time
    clock = iter([0] + [1000] * 400)                                      # 1,000 seconds in: past twelve minutes, inside 400 pairs' worth
    assert wide.collect_daily(uni, NOW)[0] == 400
    clock = iter([0] + [1001] * 400)
    assert wide.collect_daily(uni, NOW)[0] == 0


@pytest.mark.parametrize("damage, says", [
    (lambda lines: "\n".join(lines[1:]) + "\n", "lost its header"),
    (lambda lines: "", "cannot be read (EmptyDataError)"),
    (lambda lines: "\n".join(lines + [",1,1,1,1,1,1,1,kraken"]) + "\n", "a row with no time"),
    (lambda lines: "\n".join(lines + ["soon,1,1,1,1,1,1,1,kraken"]) + "\n", "a row with no time"),
    (lambda lines: "\n".join(lines + ["1790000000.5,1,1,1,1,1,1,1,kraken"]) + "\n", "a row with no time"),
    (lambda lines: "\n".join([lines[0].replace("close", "shut")] + lines[1:]) + "\n", "lost its header or a column (close)"),
])
def test_a_damaged_candle_file_is_refused_and_left_as_it_is(world, damage, says):
    alt = world.coin("SOL", days=3)
    wide.merge_daily("SOL", wide.kraken_daily(alt, NOW))
    wide.daily_path("SOL").write_text(damage(wide.daily_path("SOL").read_text().splitlines()))
    as_found = wide.daily_path("SOL").read_text()
    with pytest.raises(wide.WideError, match=re.escape(says)):
        wide.merge_daily("SOL", wide.kraken_daily(alt, NOW))
    assert wide.daily_path("SOL").read_text() == as_found


def test_one_pair_that_fails_does_not_cost_the_rest(world):
    world.coin("AAA", days=4)
    world.coin("BBB", days=4)
    world.coin("CCC", days=4)
    world.coin("DDD", days=4)
    world.coin("EEE", days=4)
    del world.ohlc["BBBUSD"]                                             # the venue refuses the pair
    world.ohlc["DDDUSD"] = [[midnight() - DAY, "1", "1"]]                # an answer in a shape nobody expected
    wide.merge_daily("EEE", wide.kraken_daily("EEEUSD", NOW))
    wide.daily_path("EEE").write_text("")                                # a file that cannot be read
    uni = {"pairs": {c: {"listed": True, "altname": f"{c}USD"} for c in ("AAA", "BBB", "CCC", "DDD", "EEE")}}
    uni["pairs"]["OFF"] = {"listed": False, "altname": "OFFUSD"}
    uni["pairs"]["NONAME"] = {"listed": True}
    read, added, failed = wide.collect_daily(uni, NOW)
    assert (read, added) == (2, 8)
    assert [f.split(":")[0] for f in failed] == ["BBB", "DDD", "EEE"]
    assert "Unknown asset pair" in failed[0] and "cannot be read" in failed[2]
    assert not wide.daily_path("OFF").exists() and not wide.daily_path("NONAME").exists()
    assert not any("OFFUSD" in str(p) for _, p in world.calls)


# --- bid and ask ----------------------------------------------------------------

def test_one_bid_and_ask_reading_a_day_for_each_coin_on_the_list(world):
    world.coin("AAA", price=20.0, volume=4e6, spread=0.001)
    world.coin("BBB", volume=3e6)
    world.coin("OUT", volume=2e6)
    pairs = wide.usd_pairs(world.pairs, [])
    rows = wide.read_ticker(pairs, world.ticker)
    uni = {"pairs": {"AAA": {}, "BBB": {}}}
    assert wide.append_quotes(uni, rows, NOW) == 2
    assert wide.append_quotes(uni, rows, NOW + 3600) == 0               # a second run the same day
    uni["pairs"]["OUT"] = {}
    assert wide.append_quotes(uni, rows, NOW + 7200) == 1               # a coin that joined since is read once
    assert wide.append_quotes(uni, rows, midnight() + DAY - 1) == 0     # the last second of the day is the same day
    assert wide.append_quotes(uni, rows, midnight() + DAY) == 3         # the first second of the next is not
    assert wide.append_quotes(uni, rows, midnight() + DAY + 5) == 0     # and a reading taken in that first second counts for its day
    df = pd.read_csv(wide.quotes_path(2026))
    assert list(df.columns) == wide.QUOTE_COLUMNS and len(df) == 6
    a = df[df["pair"] == "AAA"].iloc[0]
    assert a["bid"] == pytest.approx(19.98) and a["ask"] == pytest.approx(20.02) and a["half_spread_bps"] == pytest.approx(10.0)
    assert a["usd_volume_24h"] == pytest.approx(4e6) and a["rank"] == 1 and a["time"] == NOW
    assert a["volume_24h"] == pytest.approx(2e5) and a["vwap_24h"] == pytest.approx(20.0) and a["trades_24h"] == 500 and a["last"] == pytest.approx(20.0)
    assert wide.quotes_path(2026).read_text().count("time,pair") == 1   # one header
    assert list(df["time"]) == sorted(df["time"])


def test_a_coin_called_na_or_null_keeps_its_name_on_file(world):
    for name in ("NA", "NULL", "NAN", "INF", "TRUE", "1E5"):
        world.coin(name)
    rows = wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)
    uni = {"pairs": {r["pair"]: {} for r in rows}}
    assert wide.append_quotes(uni, rows, NOW) == 6
    assert wide.append_quotes(uni, rows, NOW + 60) == 0                  # each is known to have its reading for the day
    back = wide._read_csv(wide.quotes_path(2026), wide.QUOTE_COLUMNS)
    assert sorted(back["pair"]) == ["1E5", "INF", "NA", "NAN", "NULL", "TRUE"]


def test_coins_whose_names_all_read_as_numbers_keep_them_as_names(world):
    """With one name among them that is plainly a word, a parser leaves the whole column as text. Without one it would not."""
    for name in ("1E5", "42", "007"):
        world.coin(name)
    rows = wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)
    uni = {"pairs": {r["pair"]: {} for r in rows}}
    assert wide.append_quotes(uni, rows, NOW) == 3
    assert wide.append_quotes(uni, rows, NOW + 60) == 0                  # each is known to have its reading for the day
    assert sorted(wide._read_csv(wide.quotes_path(2026), wide.QUOTE_COLUMNS)["pair"]) == ["007", "1E5", "42"]


def test_a_new_year_starts_a_new_file(world, monkeypatch):
    import time
    monkeypatch.setenv("TZ", "America/Los_Angeles")                       # a machine eight hours behind UTC
    time.tzset()
    try:
        _a_new_year_starts_a_new_file(world)
    finally:
        monkeypatch.undo()
        time.tzset()


def _a_new_year_starts_a_new_file(world):
    world.coin("AAA")
    rows = wide.read_ticker(wide.usd_pairs(world.pairs, []), world.ticker)
    uni = {"pairs": {"AAA": {}}}
    new_year = int(datetime(2027, 1, 1, 0, 40, tzinfo=timezone.utc).timestamp())
    assert wide.append_quotes(uni, rows, new_year - DAY) == 1 and wide.append_quotes(uni, rows, new_year) == 1
    assert len(pd.read_csv(wide.quotes_path(2026))) == 1 and len(pd.read_csv(wide.quotes_path(2027))) == 1


# --- funding --------------------------------------------------------------------

def test_funding_is_summed_by_utc_day_and_only_for_days_that_are_over(world):
    r = rates(2) + [{"timestamp": "2026-10-04T00:00:00.000Z", "fundingRate": 1.0, "relativeFundingRate": 0.5},   # today
                    {"timestamp": "not a time", "fundingRate": 1.0, "relativeFundingRate": 0.5},
                    {"timestamp": 1790985600, "fundingRate": 1.0, "relativeFundingRate": 0.5},                   # a bare number
                    {"timestamp": "2026-10-03T05:00:00.000Z", "fundingRate": None, "relativeFundingRate": 0.5},
                    {"timestamp": "2026-10-03T05:30:00.000Z", "fundingRate": float("nan"), "relativeFundingRate": 0.5},
                    {"timestamp": "2026-10-03T05:40:00.000Z", "fundingRate": 1.0, "relativeFundingRate": float("nan")},
                    {"timestamp": "2026-10-03T05:00:00.000Z"}, "junk", None]
    df = wide.funding_by_day(r, NOW)
    assert list(df.columns) == wide.FUNDING_COLUMNS
    assert list(df["time"]) == [midnight() - 2 * DAY, midnight() - DAY] and list(df["hours"]) == [24, 24]
    assert df["relative_sum"].tolist() == pytest.approx([0.0024, 0.0024]) and df["absolute_sum"].tolist() == pytest.approx([0.24, 0.24])
    assert len(wide.funding_by_day([], NOW)) == 0 and len(wide.funding_by_day(None, NOW)) == 0
    # the same reading sent twice counts once, and a reading belongs to the day its time stamp is in
    twice = rates(1) + rates(1)[:5]
    assert list(wide.funding_by_day(twice, NOW)["hours"]) == [24]
    edge = [{"timestamp": "2026-10-02T23:00:00Z", "fundingRate": 1.0, "relativeFundingRate": 0.1},
            {"timestamp": "2026-10-03T00:00:00Z", "fundingRate": 2.0, "relativeFundingRate": 0.2}]
    df = wide.funding_by_day(edge, NOW)
    assert list(df["time"]) == [midnight() - 2 * DAY, midnight() - DAY] and df["relative_sum"].tolist() == pytest.approx([0.1, 0.2])
    assert df["absolute_sum"].tolist() == pytest.approx([1.0, 2.0])


def test_a_reading_with_a_rate_missing_is_left_out_and_the_order_of_the_feed_does_not_matter(world):
    day = midnight() - DAY
    stamp = lambda h: datetime.fromtimestamp(day + h * 3600, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")      # noqa: E731
    good = [{"timestamp": stamp(h), "fundingRate": 0.1 + h / 7, "relativeFundingRate": 0.01 + h / 300} for h in range(24)]
    holed = [dict(r) for r in good]
    holed[5]["relativeFundingRate"] = None                                # the venue has no relative rate for one hour
    holed[9]["fundingRate"] = None                                        # and no absolute one for another
    df = wide.funding_by_day(holed, NOW)
    assert list(df["hours"]) == [22]                                      # neither is counted as an hour, or summed as nothing
    assert df["relative_sum"].iloc[0] == pytest.approx(sum(0.01 + h / 300 for h in range(24) if h not in (5, 9)))
    # the same readings in any order are the same day: summed in time order, to the last digit. Rates of
    # both signs, as funding has: with these, three shuffles in four give another last digit when summed as they come
    random = __import__("random")
    draw = random.Random(11)
    good = [{"timestamp": stamp(h), "relativeFundingRate": (rate := draw.uniform(-1e-4, 1e-4)), "fundingRate": rate * 63211.7} for h in range(24)]
    ordered = wide.funding_by_day(good, NOW)
    for seed in range(12):
        mixed = list(good)
        random.Random(seed).shuffle(mixed)
        assert wide.funding_by_day(mixed, NOW).equals(ordered), seed
    assert wide.merge_funding("PF_XBTUSD", ordered) == 1
    first = wide.funding_path("PF_XBTUSD").read_bytes()
    assert wide.merge_funding("PF_XBTUSD", wide.funding_by_day(list(reversed(good)), NOW)) == 0
    assert wide.funding_path("PF_XBTUSD").read_bytes() == first           # so the row on file is not written again


def test_a_day_of_funding_gives_way_only_to_a_reading_that_is_as_full(world):
    assert wide.merge_funding("PF_XBTUSD", wide.funding_by_day(rates(2, hours=6), NOW)) == 2
    assert wide.merge_funding("PF_XBTUSD", wide.funding_by_day(rates(1, hours=3, per_hour=0.5), NOW)) == 0
    df = pd.read_csv(wide.funding_path("PF_XBTUSD"))
    assert list(df["hours"]) == [6, 6] and df["relative_sum"].tolist() == pytest.approx([0.0006, 0.0006])     # the thinner reading is not taken
    assert wide.merge_funding("PF_XBTUSD", wide.funding_by_day(rates(1, hours=6, per_hour=0.002), NOW)) == 0
    df = pd.read_csv(wide.funding_path("PF_XBTUSD"))
    assert df["relative_sum"].tolist() == pytest.approx([0.0006, 0.012])                                      # as full and newer: taken
    assert wide.merge_funding("PF_XBTUSD", wide.funding_by_day(rates(3), NOW)) == 1
    df = pd.read_csv(wide.funding_path("PF_XBTUSD"))
    assert list(df["hours"]) == [24, 24, 24] and df["time"].is_monotonic_increasing
    assert df["relative_sum"].tolist() == pytest.approx([0.0024] * 3)


def test_funding_follows_the_most_traded_perpetuals_and_keeps_the_ones_it_has(world):
    world.perps = [
        {"tag": "perpetual", "symbol": "PF_ETHUSD", "volumeQuote": 5e8, "suspended": False},
        {"tag": "perpetual", "symbol": "PF_XBTUSD", "volumeQuote": 9e8, "suspended": False},
        {"tag": "perpetual", "symbol": "PF_SOLUSD", "volumeQuote": 1e8, "suspended": False},
        {"tag": "perpetual", "symbol": "PF_OLDUSD", "volumeQuote": 5.0, "suspended": False},
        {"tag": "perpetual", "symbol": "PF_HALTUSD", "volumeQuote": 9e9, "suspended": True},
        {"tag": "perpetual", "symbol": "PI_XBTUSD", "volumeQuote": 9e9, "suspended": False},      # the inverse contract
        {"tag": "month", "symbol": "PF_XBTUSD_261030", "volumeQuote": 9e9},
        {"tag": "perpetual", "symbol": "PF_../UP", "volumeQuote": 9e12, "suspended": False},      # not a name for a file
        "junk",
    ]
    for s in ("PF_XBTUSD", "PF_SOLUSD", "PF_OLDUSD", "PF_GONEUSD"):
        world.funding[s] = rates(3)
    wide.merge_funding("PF_OLDUSD", wide.funding_by_day(rates(5)[:24], NOW))                     # logged on an earlier day
    wide.merge_funding("PF_GONEUSD", wide.funding_by_day(rates(5)[:24], NOW))                    # logged, and no longer listed
    out = wide.collect_funding({**wide.DEFAULTS, "funding_top_n": 3}, NOW)
    asked = [p["symbol"] for u, p in world.calls if u.endswith("/historical-funding-rates")]
    assert asked == ["PF_XBTUSD", "PF_ETHUSD", "PF_OLDUSD"]            # PF_../UP took a place among the three and was passed over
    assert out["symbols"] == 2 and out["days_added"] == 6
    assert len(out["failed"]) == 1 and out["failed"][0].startswith("PF_ETHUSD: ")
    assert len(pd.read_csv(wide.funding_path("PF_OLDUSD"))) == 4 and len(pd.read_csv(wide.funding_path("PF_GONEUSD"))) == 1
    assert sorted(p.name for p in (wide.root() / "funding").iterdir()) == ["PF_GONEUSD.csv", "PF_OLDUSD.csv", "PF_XBTUSD.csv"]


def test_readings_that_cannot_be_read_are_a_failure_and_no_readings_yet_are_not(world):
    world.perps = [{"tag": "perpetual", "symbol": s, "volumeQuote": v, "suspended": False}
                   for s, v in (("PF_AUSD", 4.0), ("PF_BUSD", 3.0), ("PF_CUSD", 2.0), ("PF_DUSD", 1.0))]
    world.funding = {"PF_AUSD": rates(2),
                     "PF_BUSD": [{"timestamp": 1790985600 + h * 3600, "fundingRate": 1.0, "relativeFundingRate": 0.1} for h in range(48)],
                     "PF_CUSD": [],                                                                  # listed today: nothing yet
                     "PF_DUSD": [{"timestamp": "2026-10-04T00:00:00Z", "fundingRate": 1.0, "relativeFundingRate": 0.1}]}   # only today so far
    out = wide.collect_funding(dict(wide.DEFAULTS), NOW)
    assert out["symbols"] == 3 and out["days_added"] == 2
    assert out["failed"] == ["PF_BUSD: 48 readings and none could be read"]
    assert not wide.funding_path("PF_BUSD").exists()
    assert len(wide.funding_readings(world.funding["PF_DUSD"])) == 1 and len(wide.funding_readings("junk")) == 0


def test_a_list_of_futures_with_no_perpetual_in_it_is_a_failure(world):
    """Kraken always has perpetuals. None in the answer means its shape has changed, and funding would stop without a word."""
    world.perps = [{"tag": "perp", "symbol": "PF_XBTUSD", "volumeQuote": 9e8, "suspended": False}, "junk"]
    assert wide.collect_funding(dict(wide.DEFAULTS), NOW) == {"symbols": 0, "days_added": 0, "failed": ["tickers: 2 tickers and no perpetual among them"]}
    world.perps = []
    assert wide.collect_funding(dict(wide.DEFAULTS), NOW)["failed"] == ["tickers: 0 tickers and no perpetual among them"]
    world.perps = [{"tag": "perpetual", "symbol": "PF_XBTUSD", "volumeQuote": 9e8, "suspended": True}]
    assert wide.collect_funding(dict(wide.DEFAULTS), NOW)["failed"] == ["tickers: 1 tickers and no perpetual among them"]


def test_funding_has_an_allowance_of_time_and_is_asked_less_patiently_than_the_candles(world, monkeypatch):
    """Funding is an extra. A futures venue that hangs must cost the funding, never the candles gathered before it."""
    world.perps = [{"tag": "perpetual", "symbol": s, "volumeQuote": v, "suspended": False}
                   for s, v in (("PF_AUSD", 4.0), ("PF_BUSD", 3.0), ("PF_CUSD", 2.0), ("PF_DUSD", 1.0))]
    world.funding = {s: rates(2) for s in ("PF_AUSD", "PF_BUSD", "PF_CUSD", "PF_DUSD")}
    waits = []
    monkeypatch.setattr(wide, "_sleep", waits.append)
    clock = iter(range(0, 10 ** 6, 50))                                   # each look at the clock is fifty seconds on
    monkeypatch.setattr(wide, "_clock", lambda: next(clock))
    out = wide.collect_funding(dict(wide.DEFAULTS), NOW)
    assert out["symbols"] == 2 and wide.FUNDING_BUDGET_S == 120           # two fit in two minutes at fifty seconds a look
    assert out["failed"] == ["PF_CUSD and any after it: not asked, the time allowed for funding had run out"]
    assert [p["symbol"] for u, p in world.calls if u.endswith("/historical-funding-rates")] == ["PF_AUSD", "PF_BUSD"]
    assert waits == [0.3, 0.3]                                            # a little apart
    assert {(tries, timeout) for _, tries, timeout in world.patience} == {(2, 15.0)}      # two tries of fifteen seconds, not three of twenty
    assert wide.EXTRA == {"tries": 2, "timeout": 15.0}


def test_funding_can_be_switched_off(world):
    world.perps = [{"tag": "perpetual", "symbol": "PF_XBTUSD", "volumeQuote": 9e8, "suspended": False}]
    world.funding["PF_XBTUSD"] = rates(3)
    wide.merge_funding("PF_XBTUSD", wide.funding_by_day(rates(5)[:24], NOW))          # even with a symbol on file
    out = wide.collect_funding({**wide.DEFAULTS, "funding_top_n": 0}, NOW)
    assert out == {"symbols": 0, "days_added": 0, "failed": []} and world.calls == []  # the futures venue is not asked at all


def test_no_futures_ticker_means_no_funding_and_no_error(world):
    world.broken.add("/tickers")
    out = wide.collect_funding(dict(wide.DEFAULTS), NOW)
    assert out["symbols"] == 0 and out["failed"] == ["tickers: http 503"]


def test_one_perpetual_with_an_odd_answer_does_not_cost_the_others(world):
    world.perps = [{"tag": "perpetual", "symbol": s, "volumeQuote": v, "suspended": False}
                   for s, v in (("PF_AUSD", 3.0), ("PF_BUSD", 2.0), ("PF_CUSD", 1.0))]
    world.funding = {"PF_AUSD": rates(2), "PF_BUSD": rates(2), "PF_CUSD": rates(2)}
    wide.funding_path("PF_BUSD").parent.mkdir(parents=True)
    wide.funding_path("PF_BUSD").write_text("time,hours\n1,2\n")                                # a file that has lost columns
    out = wide.collect_funding(dict(wide.DEFAULTS), NOW)
    assert out["symbols"] == 2 and out["days_added"] == 4
    assert len(out["failed"]) == 1 and out["failed"][0].startswith("PF_BUSD: ") and "lost its header" in out["failed"][0]


# --- older history --------------------------------------------------------------

def coinbase_rows(first_day, days, price=10.0, drift=0.0):
    """[time, low, high, open, close, volume], oldest first; the close is 1% above the open so the two cannot be mixed up."""
    out = []
    for i in range(days):
        p = price * (1 + drift) ** i
        out.append([first_day + i * DAY, p * 0.96, p * 1.03, p * 0.99, p, 55.5 + i])     # low further from the close than the high
    return out


def test_coinbase_candles_come_back_oldest_first_in_our_columns(world):
    world.coinbase["SOL"] = coinbase_rows(midnight() - 700 * DAY, 700)
    df, note = wide.coinbase_daily("SOL", midnight() - 650 * DAY, midnight() - 10 * DAY)
    assert note == "" and list(df.columns) == wide.DAILY_COLUMNS
    assert df["time"].is_monotonic_increasing and df["time"].is_unique and len(df) == 641
    assert int(df["time"].min()) == midnight() - 650 * DAY and int(df["time"].max()) == midnight() - 10 * DAY
    assert (df["source"] == "coinbase").all() and (df["count"] == 0).all()
    row = df.iloc[0]
    assert (row["low"], row["high"], row["open"], row["close"]) == (pytest.approx(9.6), pytest.approx(10.3), pytest.approx(9.9), pytest.approx(10.0))
    assert row["vwap"] == pytest.approx((10.3 + 9.6 + 10.0) / 3) and row["vwap"] != pytest.approx(10.0)      # the mean of three, not the close
    assert row["volume"] == pytest.approx(55.5 + 50)
    pages = [p for u, p in world.calls if "/products/SOL-USD/candles" in u]
    assert len(pages) == 3 and all(p["granularity"] == DAY for p in pages)       # 640 days at 300 a page
    df, note = wide.coinbase_daily("NOPE", midnight() - 50 * DAY, midnight())
    assert note == "not listed" and len(df) == 0
    world.broken.add("/products/SOL-USD")
    df, note = wide.coinbase_daily("SOL", midnight() - 50 * DAY, midnight())
    assert note == "http 503" and len(df) == 0
    world.broken.clear()
    world.coinbase["EMPTY"] = []
    df, note = wide.coinbase_daily("EMPTY", midnight() - 50 * DAY, midnight())
    assert note == "" and len(df) == 0 and list(df.columns) == wide.DAILY_COLUMNS
    # a start that is not a midnight is taken back to one
    df, _ = wide.coinbase_daily("SOL", midnight() - 5 * DAY + 3600, midnight() - 2 * DAY)
    assert int(df["time"].min()) == midnight() - 5 * DAY
    # a row that is not a UTC day, has no close, or comes twice is not a candle
    world.coinbase["ODD"] = coinbase_rows(midnight() - 20 * DAY, 10) + [[midnight() - 8 * DAY + 60, 1, 1, 1, 1, 1],
                                                                        [midnight() - 7 * DAY, 1, 1, 1, 0, 1], [midnight() - 6 * DAY, 1, 1, 1, None, 1],
                                                                        [midnight() - 20 * DAY, 9.6, 10.3, 9.9, 10.0, 55.5]]
    df, note = wide.coinbase_daily("ODD", midnight() - 30 * DAY, midnight())
    assert note == "" and len(df) == 10 and (df["time"] % DAY == 0).all() and (df["close"] > 0).all() and df["time"].is_unique
    # nor is a row from before there was a coin, whatever the venue sends for such a stretch
    world.coinbase["EARLY"] = [[0, 1, 1, 1, 1, 1], [DAY, 1, 1, 1, 1, 1], [wide.FIRST_DAY - DAY, 1, 1, 1, 1, 1], [wide.FIRST_DAY, 1, 1, 1, 1, 1]]
    df, note = wide.coinbase_daily("EARLY", 0, 2 * DAY)
    assert note == "2 rows and none is a daily candle" and len(df) == 0 and list(df.columns) == wide.DAILY_COLUMNS
    df, note = wide.coinbase_daily("EARLY", wide.FIRST_DAY - DAY, wide.FIRST_DAY + DAY)
    assert note == "" and list(df["time"]) == [wide.FIRST_DAY]
    # times in another unit: an answer that is all rows and no candles is a failure, not a coin with no past
    world.coinbase_time_unit = 1000
    df, note = wide.coinbase_daily("SOL", midnight() - 30 * DAY, midnight() - 10 * DAY)
    assert note == "21 rows and none is a daily candle" and len(df) == 0
    world.coinbase_time_unit = 1
    # and the pages are asked for a little apart, and less patiently than the candles Kraken is asked for
    waits = []
    wide._sleep = waits.append
    world.patience.clear()
    wide.coinbase_daily("SOL", midnight() - 650 * DAY, midnight() - 10 * DAY)
    assert waits == [0.15] * 3
    assert [(tries, timeout) for _, tries, timeout in world.patience] == [(2, 15.0)] * 3


def test_two_venues_agree_only_when_their_closes_do():
    days = [i * DAY for i in range(30)]
    a = pd.DataFrame({"time": days, "close": [100.0 + i for i in range(30)]})
    assert wide.venues_agree(a, a.assign(close=a["close"] * 1.004))[0]
    assert wide.venues_agree(a, a.assign(close=a["close"] * 1.0099))[0] and not wide.venues_agree(a, a.assign(close=a["close"] * 1.0101))[0]
    ok, why = wide.venues_agree(a, a.assign(close=a["close"] * 1.2))
    assert not ok and "differ by 20.00%" in why
    spiky = a.assign(close=[c * (1.5 if i % 5 == 0 else 1.0) for i, c in enumerate(a["close"])])
    assert not wide.venues_agree(a, spiky)[0]                                     # mostly the same is not the same coin
    ok, why = wide.venues_agree(a.head(9), a)
    assert not ok and why == "only 9 days in common"
    assert wide.venues_agree(a.head(10), a)[0]
    # one day in ten may be off by a lot (a bad print on one venue), not more, and not by more than a twentieth at the ninth decile
    tail = lambda k, by: a.assign(close=[c * (by if i < k else 1.0) for i, c in enumerate(a["close"])])       # noqa: E731
    assert wide.venues_agree(a, tail(2, 1.5))[0] and not wide.venues_agree(a, tail(4, 1.5))[0]
    assert wide.venues_agree(a, tail(4, 1.04))[0] and not wide.venues_agree(a, tail(4, 1.06))[0]


def deep_world(world, coins):
    """Coins with Kraken candles on file; rank 1 is the first named."""
    uni = {"pairs": {}}
    for rank, (coin, kdays) in enumerate(coins, start=1):
        alt = world.coin(coin, days=kdays)
        wide.merge_daily(coin, wide.kraken_daily(alt, NOW))
        uni["pairs"][coin] = {"listed": True, "altname": alt, "rank": rank}
    return uni


def test_older_days_come_from_coinbase_when_the_venues_agree(world):
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = coinbase_rows(midnight() - 400 * DAY, 400)
    st = {**wide.DEFAULTS, "history_days": 300}
    out = wide.deepen(uni, st, NOW)
    assert out["coins"] == 1 and out["days_added"] == 200 and out["mismatch"] == [] and out["failed"] == []
    df = wide.load_daily("SOL")
    assert len(df) == 300 and df["time"].is_monotonic_increasing and df["time"].is_unique
    assert int(df["time"].min()) == midnight() - 300 * DAY
    assert list(df["source"]) == ["coinbase"] * 200 + ["kraken"] * 100          # no Kraken day was replaced
    assert df.iloc[0]["open"] == pytest.approx(9.9) and df.iloc[0]["close"] == pytest.approx(10.0)
    marks = json.loads((wide.root() / "deepen.json").read_text())
    assert marks["SOL"]["result"].startswith("added 200 days; closes differ by 0.00%") and marks["SOL"]["at"] == NOW


def test_coinbase_is_checked_against_krakens_days_and_never_against_its_own(world):
    """With Coinbase rows already on file, a later answer must still agree with Kraken on the days Kraken has."""
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = coinbase_rows(midnight() - 520 * DAY, 520)
    assert wide.deepen(uni, {**wide.DEFAULTS, "history_days": 500}, NOW)["days_added"] == 400
    world.coinbase["SOL"] = coinbase_rows(midnight() - 950 * DAY, 950, price=30.0)               # now it answers for another coin
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 900}, NOW)
    assert out["coins"] == 0 and len(out["mismatch"]) == 1 and "over 31 days" in out["mismatch"][0]
    assert len(wide.load_daily("SOL")) == 500


def test_whatever_else_is_on_file_it_is_krakens_days_the_answer_is_held_against(world):
    uni = deep_world(world, [("SOL", 100)])
    planted = wide.load_daily("SOL").head(40).copy()                                # forty older rows of some other price, marked Coinbase's
    planted["time"] = [midnight() - (140 - i) * DAY for i in range(40)]
    planted["close"], planted["source"] = 30.0, "coinbase"
    wide.merge_daily("SOL", planted)
    world.coinbase["SOL"] = coinbase_rows(midnight() - 400 * DAY, 400)              # Coinbase agrees with Kraken, not with those rows
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)
    assert out["coins"] == 1 and out["mismatch"] == [] and out["days_added"] == 160
    assert len(wide.load_daily("SOL")) == 300


def test_a_coin_kraken_no_longer_lists_still_gets_its_older_days(world):
    """Its candles on file end where it left; its past is as much wanted as anyone's, a dead coin's most of all."""
    uni = deep_world(world, [("DEAD", 100)])
    uni["pairs"]["DEAD"].update({"listed": False, "unlisted_since": "2026-10-04"})
    world.coinbase["DEAD"] = coinbase_rows(midnight() - 400 * DAY, 400)
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)
    assert out["coins"] == 1 and out["days_added"] == 200 and len(wide.load_daily("DEAD")) == 300


def test_a_coin_coinbase_lists_but_has_no_candles_for_is_asked_about_once_more_and_then_not_every_day(world):
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = []
    st = {**wide.DEFAULTS, "history_days": 300}
    out = wide.deepen(uni, st, NOW)
    assert out == {"coins": 0, "days_added": 0, "not_listed": 0, "mismatch": [], "failed": []}
    assert json.loads((wide.root() / "deepen.json").read_text())["SOL"]["result"] == "no candles, to be asked once more"
    calls = len(world.calls)
    wide.deepen(uni, st, NOW + 19 * 3600)
    assert len(world.calls) == calls                                              # not the same day
    wide.deepen(uni, st, NOW + DAY)
    assert len(world.calls) > calls                                               # the next day, once more
    assert json.loads((wide.root() / "deepen.json").read_text())["SOL"]["result"] == "no candles"      # and then it is believed
    calls = len(world.calls)
    wide.deepen(uni, st, NOW + 2 * DAY)
    wide.deepen(uni, st, NOW + 80 * DAY)
    assert len(world.calls) == calls


def test_an_empty_answer_on_one_bad_day_does_not_cost_three_months(world):
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = []                                                    # the day Coinbase answers with nothing
    st = {**wide.DEFAULTS, "history_days": 300}
    wide.deepen(uni, st, NOW)
    world.coinbase["SOL"] = coinbase_rows(midnight() - 400 * DAY, 400)
    assert wide.deepen(uni, st, NOW + DAY)["coins"] == 1 and len(wide.load_daily("SOL")) == 299


def test_a_coin_that_is_deep_enough_is_not_asked_about(world):
    uni = deep_world(world, [("SOL", 290), ("ADA", 269)])                       # within 30 days of the 300 asked for, and not
    world.coinbase["SOL"] = coinbase_rows(midnight() - 400 * DAY, 400)
    world.coinbase["ADA"] = coinbase_rows(midnight() - 400 * DAY, 400)
    calls = len(world.calls)
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)
    asked = {u.split("/products/")[1].split("-")[0] for u, _ in world.calls[calls:]}
    assert asked == {"ADA"} and out["coins"] == 1
    assert "SOL" not in json.loads((wide.root() / "deepen.json").read_text())   # not asked, so not marked either


def test_another_coin_with_the_same_name_is_not_taken(world):
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = coinbase_rows(midnight() - 400 * DAY, 400, price=3.0)
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)
    assert out["coins"] == 0 and out["days_added"] == 0
    assert len(out["mismatch"]) == 1 and out["mismatch"][0].startswith("SOL: closes differ by 70.00%")
    assert len(wide.load_daily("SOL")) == 100
    marks = json.loads((wide.root() / "deepen.json").read_text())
    assert marks["SOL"]["result"].startswith("not used: closes differ")
    calls = len(world.calls)
    wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW + DAY)
    assert len(world.calls) == calls                                             # and it is not asked for again the next day
    wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW + 89 * DAY)
    assert len(world.calls) == calls
    wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW + 91 * DAY)
    assert len(world.calls) > calls                                              # only after three months


def test_asking_for_a_much_longer_history_asks_again_at_once_and_a_little_longer_waits(world):
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = coinbase_rows(midnight() - 250 * DAY, 250)           # Coinbase has 250 days and no more
    assert wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)["days_added"] == 150
    calls = len(world.calls)
    assert wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW + DAY)["coins"] == 0 and len(world.calls) == calls
    world.coinbase["SOL"] = coinbase_rows(midnight() - 900 * DAY, 900)
    wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300 + 90}, NOW + DAY)      # Fin raises history_days by three months or less:
    assert len(world.calls) == calls                                              # not asked again until the 90 days are up
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 800}, NOW + DAY)     # by more: asked at once
    assert out["coins"] == 1 and len(wide.load_daily("SOL")) == 800 - 1


def test_a_coin_coinbase_does_not_list_is_asked_about_once_more_and_a_failed_request_is_not_an_answer(world):
    uni = deep_world(world, [("AAA", 100), ("BBB", 100)])
    world.coinbase["BBB"] = coinbase_rows(midnight() - 400 * DAY, 400)
    world.broken.add("/products/BBB-USD")
    st = {**wide.DEFAULTS, "history_days": 300}
    out = wide.deepen(uni, st, NOW)
    assert out["not_listed"] == 1 and out["coins"] == 0
    assert len(out["failed"]) == 1 and out["failed"][0].startswith("BBB: coinbase http 503")
    marks = json.loads((wide.root() / "deepen.json").read_text())
    assert marks["AAA"]["result"] == "not listed, to be asked once more" and "BBB" not in marks
    world.broken.clear()
    asked = lambda since: [u.split("/products/")[1].split("-")[0] for u, _ in world.calls[since:]]       # noqa: E731
    n = len(world.calls)
    out = wide.deepen(uni, st, NOW + 20 * 3600 - 1)                       # a run later the same day, or just past midnight: BBB again, AAA not
    assert out["coins"] == 1 and out["days_added"] == 200 and out["not_listed"] == 0 and set(asked(n)) == {"BBB"}
    n = len(world.calls)
    out = wide.deepen(uni, st, NOW + 20 * 3600)                           # twenty hours on, which the next day's run always is: once more
    assert out["not_listed"] == 1 and out["coins"] == 0 and set(asked(n)) == {"AAA"} and wide.ASK_AGAIN_AFTER_S == 20 * 3600
    assert json.loads((wide.root() / "deepen.json").read_text())["AAA"]["result"] == "not listed"         # and now it is believed
    n = len(world.calls)
    wide.deepen(uni, st, NOW + 2 * DAY)
    wide.deepen(uni, st, NOW + 89 * DAY)
    assert len(world.calls) == n                                          # for three months
    wide.deepen(uni, st, NOW + 92 * DAY)
    assert set(asked(n)) == {"AAA"}


def test_one_bad_day_at_coinbase_does_not_cost_three_months_of_older_history(world):
    """On a day Coinbase answers "no such product" for everything, every coin would be written off for 90 days."""
    uni = deep_world(world, [("AAA", 100), ("BBB", 100)])
    for coin in ("AAA", "BBB"):
        world.coinbase[coin] = coinbase_rows(midnight() - 400 * DAY, 400)
    world.coinbase_knows_nobody = True
    st = {**wide.DEFAULTS, "history_days": 300}
    out = wide.deepen(uni, st, NOW)
    assert out["not_listed"] == 2 and out["coins"] == 0 and out["failed"] == []
    world.coinbase_knows_nobody = False
    out = wide.deepen(uni, st, NOW + DAY)
    assert out["coins"] == 2 and out["not_listed"] == 0 and len(wide.load_daily("AAA")) == 299 and len(wide.load_daily("BBB")) == 299


def test_one_kind_of_no_does_not_stand_in_for_the_other(world):
    uni = deep_world(world, [("AAA", 100)])
    st = {**wide.DEFAULTS, "history_days": 300}
    mark = lambda: json.loads((wide.root() / "deepen.json").read_text())["AAA"]["result"]      # noqa: E731
    wide.deepen(uni, st, NOW)                                             # no such product, the first time
    assert mark() == "not listed, to be asked once more"
    world.coinbase["AAA"] = []
    wide.deepen(uni, st, NOW + DAY)                                       # the next day it is a product, with nothing in it
    assert mark() == "no candles, to be asked once more"                  # the first answer of its kind: not believed yet
    wide.deepen(uni, st, NOW + 2 * DAY)
    assert mark() == "no candles"                                         # the same answer again: believed
    # and a coin whose older days were added once is not written off by one "no" when it is asked about again
    world.coinbase["AAA"] = coinbase_rows(midnight() - 400 * DAY, 400)
    assert wide.deepen(uni, st, NOW + 100 * DAY)["coins"] == 1 and mark().startswith("added ")
    del world.coinbase["AAA"]
    wide.deepen(uni, {**st, "history_days": 900}, NOW + 101 * DAY)        # Fin asks for a much longer history, and Coinbase says no
    assert mark() == "not listed, to be asked once more"


def test_a_mark_from_before_the_second_ask_was_asked_for_is_believed_as_it_stands(world):
    uni = deep_world(world, [("AAA", 100)])
    st = {**wide.DEFAULTS, "history_days": 300}
    want_from = (NOW // DAY - 300) * DAY
    (wide.root() / "deepen.json").write_text(json.dumps({"AAA": {"at": NOW - 5 * DAY, "want_from": want_from, "result": "not listed"}}))
    n = len(world.calls)
    wide.deepen(uni, st, NOW)
    assert len(world.calls) == n
    out = wide.deepen(uni, st, NOW + 90 * DAY)                            # and when its three months are up, one more "no" is enough
    assert out["not_listed"] == 1
    assert json.loads((wide.root() / "deepen.json").read_text())["AAA"]["result"] == "not listed"


def test_an_answer_from_coinbase_that_is_no_candles_is_a_failure_and_is_asked_for_again(world):
    uni = deep_world(world, [("SOL", 100)])
    world.coinbase["SOL"] = coinbase_rows(midnight() - 400 * DAY, 400)
    world.coinbase_time_unit = 1000                                       # it answers in milliseconds
    st = {**wide.DEFAULTS, "history_days": 300}
    out = wide.deepen(uni, st, NOW)
    assert out["coins"] == 0 and out["mismatch"] == [] and len(out["failed"]) == 1
    assert out["failed"][0].startswith("SOL: coinbase ") and out["failed"][0].endswith(" rows and none is a daily candle")
    assert not (wide.root() / "deepen.json").exists() and len(wide.load_daily("SOL")) == 100       # not marked as asked
    world.coinbase_time_unit = 1
    assert wide.deepen(uni, st, NOW + 3600)["coins"] == 1                 # so the next run asks again


def test_a_coin_with_no_rank_waits_behind_those_that_have_one(world, monkeypatch):
    uni = deep_world(world, [("ZZZ", 100), ("AAA", 100)])
    del uni["pairs"]["AAA"]["rank"]                                       # Kraken gave no quote for it: it has no rank today
    uni["pairs"]["ZZZ"]["rank"] = 57
    for c in ("AAA", "ZZZ"):
        world.coinbase[c] = coinbase_rows(midnight() - 400 * DAY, 400)
    clock = iter(range(0, 10_000, 100))
    monkeypatch.setattr(wide, "_clock", lambda: next(clock))
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300, "deepen_budget_s": 150}, NOW)
    assert out["coins"] == 1 and len(wide.load_daily("ZZZ")) == 300 and len(wide.load_daily("AAA")) == 100


def test_a_coin_too_new_to_compare_is_asked_about_once_it_can_be(world):
    uni = deep_world(world, [("NEW", 6)])
    world.coinbase["NEW"] = coinbase_rows(midnight() - 400 * DAY, 400)
    st = {**wide.DEFAULTS, "history_days": 300}
    calls = len(world.calls)
    out = wide.deepen(uni, st, NOW)
    assert out == {"coins": 0, "days_added": 0, "not_listed": 0, "mismatch": [], "failed": []}
    assert len(world.calls) == calls and not (wide.root() / "deepen.json").exists()       # not asked, and not marked as asked
    for i in range(7, 11):                                                                # four more days of Kraken candles
        world.ohlc["NEWUSD"].append([midnight() + (i - 6) * DAY, "10", "10.2", "9.8", "10", "10", "1", 1])
    later = NOW + 4 * DAY
    wide.merge_daily("NEW", wide.kraken_daily("NEWUSD", later))
    world.coinbase["NEW"] += coinbase_rows(midnight(), 40)
    out = wide.deepen(uni, st, later)
    assert out["coins"] == 1 and out["days_added"] == 300 - 4 - 6


def test_one_coin_with_an_odd_answer_does_not_cost_the_coins_after_it(world):
    uni = deep_world(world, [("AAA", 100), ("BBB", 100), ("CCC", 100)])
    world.coinbase["AAA"] = [r + ["a seventh field"] for r in coinbase_rows(midnight() - 400 * DAY, 400)]
    world.coinbase["BBB"] = coinbase_rows(midnight() - 400 * DAY, 400)
    world.coinbase["CCC"] = coinbase_rows(midnight() - 400 * DAY, 400)
    wide.daily_path("CCC").write_text("")
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)
    assert out["coins"] == 1 and len(wide.load_daily("BBB")) == 300
    assert [f.split(":")[0] for f in out["failed"]] == ["AAA", "CCC"]
    marks = json.loads((wide.root() / "deepen.json").read_text())
    assert sorted(marks) == ["BBB"]                                               # what failed is asked again next run
    (wide.root() / "deepen.json").write_text('{"BBB": "a note", "AAA": {"want_from": "long ago", "at": []}}')
    world.coinbase["AAA"] = coinbase_rows(midnight() - 400 * DAY, 400)
    assert wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)["coins"] == 1      # marks that cannot be read are no marks
    (wide.root() / "deepen.json").write_text("[1, 2")
    assert wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300}, NOW)["coins"] == 0      # nor is a file that cannot be


def test_the_older_history_stops_when_its_time_is_up_and_goes_by_rank(world, monkeypatch):
    uni = deep_world(world, [("ZZZ", 100), ("MMM", 100), ("AAA", 100)])             # the most traded is last by name
    for c in ("AAA", "MMM", "ZZZ"):
        world.coinbase[c] = coinbase_rows(midnight() - 400 * DAY, 400)
    clock = iter(range(0, 10_000, 60))                                           # each look at the clock is a minute on
    monkeypatch.setattr(wide, "_clock", lambda: next(clock))
    out = wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300, "deepen_budget_s": 150}, NOW)
    assert out["coins"] == 2                                                     # most traded first; the third waits
    assert len(wide.load_daily("ZZZ")) == 300 and len(wide.load_daily("MMM")) == 300 and len(wide.load_daily("AAA")) == 100
    clock = iter(range(0, 10_000, 60))
    assert wide.deepen(uni, {**wide.DEFAULTS, "history_days": 300, "deepen_budget_s": 0}, NOW)["coins"] == 0       # no time: nothing asked


# --- a whole run ----------------------------------------------------------------

def stock_world(world, n=6):
    for i in range(n):
        world.coin(f"C{i}", price=5.0 + i, volume=1e6 * (n - i), days=40)
    world.coin("BTC", kraken="XXBTZUSD", wsname="XBT/USD", altname="XBTUSD", price=60000.0, volume=5e8, days=40)
    world.coin("USDT", price=1.0, low=1.0, high=1.0, volume=9e9)
    world.perps = [{"tag": "perpetual", "symbol": "PF_XBTUSD", "volumeQuote": 9e8, "suspended": False}]
    world.funding["PF_XBTUSD"] = rates(10)
    world.coinbase["BTC"] = coinbase_rows(midnight() - 200 * DAY, 200, price=60000.0)


def test_a_run_writes_the_list_the_candles_the_quotes_the_funding_and_what_it_did(world):
    stock_world(world)
    write_settings(top_n=4, history_days=150)
    status = wide.collect(NOW)
    uni = json.loads((wide.root() / "universe.json").read_text())
    assert sorted(uni["pairs"]) == ["BTC", "C0", "C1", "C2"]
    assert all((wide.daily_path(c)).exists() for c in uni["pairs"])
    assert len(wide.load_daily("C0")) == 40 and len(wide.load_daily("BTC")) == 150
    assert len(pd.read_csv(wide.quotes_path(2026))) == 4
    assert len(pd.read_csv(wide.funding_path("PF_XBTUSD"))) == 10
    on_disk = json.loads((wide.root() / "status.json").read_text())
    assert on_disk == json.loads(json.dumps(status))
    k = status["kraken"]
    assert (k["usd_pairs"], k["quoted"], k["on_the_list"], k["listed"], k["pairs_read"], k["days_added"], k["quotes_written"]) == \
        (7, 7, 4, 4, 4, 160, 4)
    assert k["joined_today"] == ["BTC", "C0", "C1", "C2"] and k["failed"] == [] and k["pegged_skipped"] == [] and k["quotes_failed"] == ""
    assert k["unquoted"] == []
    assert k["qualified_today"] == 7                                             # every coin but the dollar token could have joined
    assert status["funding"] == {"symbols": 1, "days_added": 10, "failed": []}
    assert status["coinbase"]["coins"] == 1 and status["coinbase"]["days_added"] == 110 and status["coinbase"]["not_listed"] == 3
    assert status["probes"] == {"binance_data_api": {"http": 451, "ok": False, "note": "not JSON, 0 bytes"},
                                "binance_archive": {"http": 451, "ok": False, "note": "not JSON, 0 bytes"}}
    assert status["settings_not_used"] == [] and status["ran_utc"] == "2026-10-04 00:40Z" and status["ok"] is True
    files = sorted(str(p.relative_to(config.STATE)) for p in config.STATE.rglob("*") if p.is_file())
    assert all(f.startswith("wide/") for f in files)                              # it writes nowhere else
    # the BTC pair goes by three names on Kraken: its candles are asked for by the short one
    assert [p["pair"] for u, p in world.calls if u.endswith("/OHLC")] == ["XBTUSD", "C0USD", "C1USD", "C2USD"]


def test_a_dollar_token_that_is_not_on_the_exclude_list_is_named_and_left_out(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30, exclude=[])
    status = wide.collect(NOW)
    assert status["kraken"]["pegged_skipped"] == ["USDT"] and "USDT" not in json.loads((wide.root() / "universe.json").read_text())["pairs"]
    assert status["kraken"]["usd_pairs"] == 8


def test_a_second_run_the_same_day_changes_no_data_file(world):
    stock_world(world)
    write_settings(top_n=4, history_days=150)
    wide.collect(NOW)
    before = {p: p.read_bytes() for p in wide.root().rglob("*.csv")}
    uni = (wide.root() / "universe.json").read_text()
    status = wide.collect(NOW + 3600)
    assert {p: p.read_bytes() for p in wide.root().rglob("*.csv")} == before
    assert json.loads((wide.root() / "universe.json").read_text())["pairs"] == json.loads(uni)["pairs"]
    assert status["kraken"]["days_added"] == 0 and status["kraken"]["quotes_written"] == 0 and status["kraken"]["joined_today"] == []


def test_the_next_day_adds_one_day_to_every_coin(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)
    for alt, rows in world.ohlc.items():                                          # a day passes on the venue
        rows.append([rows[-1][0] + DAY] + rows[-1][1:])
    status = wide.collect(NOW + DAY)
    assert status["kraken"]["days_added"] == 4 and status["kraken"]["quotes_written"] == 4
    assert int(wide.load_daily("C0")["time"].max()) == midnight()
    assert len(pd.read_csv(wide.quotes_path(2026))) == 8


def test_no_list_or_no_ticker_stops_the_run_with_nothing_written(world):
    stock_world(world)
    world.broken.add("/AssetPairs")
    with pytest.raises(wide.WideError, match="kraken AssetPairs"):
        wide.collect(NOW)
    world.broken = {"/Ticker"}
    with pytest.raises(wide.WideError, match="kraken Ticker"):
        wide.collect(NOW)
    assert not wide.root().exists()
    world.broken = set()
    saved = dict(world.ticker)
    world.ticker = {k: {**v, "b": ["0", "1", "1"]} for k, v in world.ticker.items()}
    with pytest.raises(wide.WideError, match="no usable quote for any US dollar pair"):
        wide.collect(NOW)
    world.ticker = saved
    world.pairs = {k: {**v, "quote": "ZEUR"} for k, v in world.pairs.items()}
    with pytest.raises(wide.WideError, match="no pair quoted in US dollars"):
        wide.collect(NOW)
    assert not wide.root().exists()


def test_a_setting_that_leaves_nobody_on_the_list_stops_the_run_and_says_which(world):
    stock_world(world)
    write_settings(min_usd_volume=5_000_000_000_000)
    with pytest.raises(wide.WideError, match="none of the 7 coins quoted qualifies for the list; look at `top_n` and `min_usd_volume`"):
        wide.collect(NOW)
    assert not wide.root().exists()
    # a list that already has coins is not emptied by the same slip: the run goes on with the coins it has,
    # and says every day that nobody can join
    write_settings(top_n=2, history_days=30)
    wide.collect(NOW)
    assert "FAILED" not in wide.summary(NOW)
    write_settings(min_usd_volume=5_000_000_000_000, history_days=30)
    world.coin("NEWBIG", volume=9e10)                                              # the most traded coin of the day
    status = wide.collect(NOW + DAY)
    assert status["kraken"]["on_the_list"] == 2 and status["kraken"]["joined_today"] == [] and status["kraken"]["qualified_today"] == 0
    assert status["ok"] is True
    assert ("\nFAILED: not one coin qualified for the list today, so none can join; look at `top_n` and `min_usd_volume` "
            "in configs/wide.yaml") in wide.summary(NOW + DAY)


def big_list(world, n=31):
    """A list of n coins on its second day: BTC and C0 to C<n-2>."""
    stock_world(world, n=n - 1)
    write_settings(top_n=n, history_days=30, deepen_budget_s=0, funding_top_n=0)
    wide.collect(NOW)
    assert len(json.loads((wide.root() / "universe.json").read_text())["pairs"]) == n


def test_a_list_from_kraken_that_was_cut_off_stops_the_run_and_marks_nobody_as_gone(world):
    """Coins leave a venue a few at a time. A quarter of the list missing from one answer is the answer's
    fault; taken at its word it would mark them all as gone and skip their day."""
    big_list(world)
    as_it_was = {p: p.read_bytes() for p in wide.root().rglob("*") if p.is_file()}
    whole = dict(world.pairs)
    for i in range(8):                                                    # 8 of 31: more than a quarter
        del world.pairs[f"C{i}USD"]
    with pytest.raises(wide.WideError, match=r"kraken AssetPairs: 8 of the 31 coins on the list are not in the answer "
                                             r"\(C0, C1, C2, C3, C4, \.\.\.\); taken for a cut off answer"):
        wide.collect(NOW + DAY)
    assert {p: p.read_bytes() for p in wide.root().rglob("*") if p.is_file()} == as_it_was       # nothing written, nobody marked
    world.pairs = dict(whole)
    for i in range(7):                                                    # 7 of 31: under a quarter, so it is believed
        del world.pairs[f"C{i}USD"]
    status = wide.collect(NOW + DAY)
    uni = json.loads((wide.root() / "universe.json").read_text())["pairs"]
    assert status["kraken"]["listed"] == 24 and uni["C0"]["listed"] is False and uni["C0"]["unlisted_since"] == "2026-10-05"


def test_a_short_list_may_lose_five_and_coins_fin_excludes_are_not_counted_as_missing(world):
    big_list(world, n=7)                                                  # BTC and C0 to C5
    for i in range(5):
        del world.pairs[f"C{i}USD"]
    assert wide.collect(NOW + DAY)["kraken"]["listed"] == 2               # five of seven: allowed, a short list can
    world.pairs, world.ticker, world.ohlc = {}, {}, {}
    (wide.root() / "universe.json").unlink()
    big_list(world)
    write_settings(top_n=31, history_days=30, deepen_budget_s=0, funding_top_n=0,
                   exclude=wide.DEFAULTS["exclude"] + [f"C{i}" for i in range(12)])
    status = wide.collect(NOW + DAY)                                      # twelve of 31 named in `exclude` at once: that is Fin's doing
    assert status["kraken"]["listed"] == 19 and status["ok"] is True


def test_after_a_long_pause_many_coins_may_really_have_gone(world):
    big_list(world)
    for i in range(12):
        del world.pairs[f"C{i}USD"]
    with pytest.raises(wide.WideError, match="12 of the 31 coins on the list are not in the answer"):
        wide.collect(NOW + 7 * DAY)                                       # a week since the last run: still an answer to doubt
    assert wide.collect(NOW + 7 * DAY + 1)["kraken"]["listed"] == 19      # longer than that: taken as it is
    uni = {"pairs": {f"C{i}": {"listed": True} for i in range(20)}, "updated": "last week"}
    assert wide.missing_from_answer(uni, {}, dict(wide.DEFAULTS), NOW) == ([], 20)      # no date of the last run to go by
    uni["updated"] = NOW + 5
    assert wide.missing_from_answer(uni, {}, dict(wide.DEFAULTS), NOW) == ([], 20)      # nor one from the future


def test_many_listed_coins_with_no_bid_and_ask_are_said(world):
    big_list(world)
    for i in range(7):                                                    # 7 of 31 with no bid: thin coins, not a fault
        world.ticker[f"C{i}USD"]["b"] = ["0", "1", "1"]
    status = wide.collect(NOW + DAY)
    assert status["kraken"]["unquoted"] == [f"C{i}" for i in range(7)] and "FAILED" not in wide.summary(NOW + DAY)
    world.ticker["C7USD"]["b"] = ["0", "1", "1"]                          # 8 of 31: the ticker was cut off
    status = wide.collect(NOW + 2 * DAY)
    assert len(status["kraken"]["unquoted"]) == 8 and status["ok"] is True
    assert "\nFAILED: no bid and ask for 8 of 31 listed coins (C0, C1, C2, C3, C4, ...)" in wide.summary(NOW + 2 * DAY)
    assert status["kraken"]["quotes_written"] == 23


def test_when_most_pairs_fail_the_run_fails_and_says_which(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    for alt in ("C0USD", "C1USD", "C2USD"):
        del world.ohlc[alt]
    with pytest.raises(wide.WideError, match="3 of 4 pairs could not be read; first: C0: "):
        wide.collect(NOW)
    status = json.loads((wide.root() / "status.json").read_text())                # what happened is still on record
    assert len(status["kraken"]["failed"]) == 3 and status["kraken"]["pairs_read"] == 1 and status["ok"] is False
    assert wide.ran_today(NOW) is None                                            # and it is not a day done
    assert "FAILED: the run stopped because most pairs could not be read" in wide.summary(NOW)
    del world.ohlc["XBTUSD"]                                                      # and when not one pair could be read
    with pytest.raises(wide.WideError, match="4 of 4 pairs could not be read"):
        wide.collect(NOW)
    assert json.loads((wide.root() / "status.json").read_text())["kraken"]["pairs_read"] == 0
    assert "FAILED: the run stopped because most pairs could not be read; nothing of it was committed" in wide.summary(NOW).splitlines()


def test_coins_that_left_the_venue_do_not_water_down_the_failure_rule(world):
    stock_world(world)
    write_settings(top_n=6, history_days=30)
    wide.collect(NOW)
    for name in ("C3", "C4"):                                                     # two of the six leave the venue
        del world.pairs[f"{name}USD"], world.ticker[f"{name}USD"]
    for alt in ("C0USD", "C1USD", "C2USD"):                                       # and three of the five now listed fail
        del world.ohlc[alt]                                                       # (C5 joins in their place: seven on the list in all)
    with pytest.raises(wide.WideError, match="3 of 5 pairs could not be read"):
        wide.collect(NOW + DAY)
    status = json.loads((wide.root() / "status.json").read_text())
    assert status["kraken"]["on_the_list"] == 7 and status["kraken"]["listed"] == 5


def test_half_the_pairs_failing_is_named_and_the_run_goes_green(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    del world.ohlc["C2USD"], world.ohlc["C1USD"]
    status = wide.collect(NOW)
    assert status["kraken"]["pairs_read"] == 2 and len(status["kraken"]["failed"]) == 2 and status["ok"] is True
    assert "\nFAILED: candles for 2 of 4 pairs: C1: " in wide.summary(NOW)


def test_a_quotes_file_that_cannot_be_added_to_does_not_cost_the_candles(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.quotes_path(2026).parent.mkdir(parents=True)
    wide.quotes_path(2026).write_text("")
    status = wide.collect(NOW)
    assert status["kraken"]["days_added"] == 160 and status["kraken"]["quotes_written"] == 0 and status["ok"] is True
    assert status["kraken"]["quotes_failed"] == "WideError: 2026.csv cannot be read (EmptyDataError); mend or remove it"
    assert wide.quotes_path(2026).read_text() == ""                               # left as it was found
    assert "\nFAILED: the day's bid and ask readings were not written: WideError: 2026.csv cannot be read" in wide.summary(NOW)


def test_the_extras_never_cost_the_candles(world, monkeypatch):
    stock_world(world)
    write_settings(top_n=4, history_days=30)

    def boom(*a, **k):
        raise ValueError("an answer in a shape nobody expected")
    monkeypatch.setattr(wide, "collect_funding", boom)
    monkeypatch.setattr(wide, "deepen", boom)
    monkeypatch.setattr(wide, "probes", boom)
    status = wide.collect(NOW)
    assert status["kraken"]["days_added"] == 160 and status["ok"] is True
    assert status["funding"]["failed"] == ["ValueError: an answer in a shape nobody expected"]
    assert status["coinbase"]["failed"] == ["ValueError: an answer in a shape nobody expected"]
    assert status["probes"] == {"error": "ValueError: an answer in a shape nobody expected"}
    text = wide.summary(NOW)
    assert "\nFAILED: funding for 1: ValueError" in text and "\nFAILED: older history for 1: ValueError" in text
    assert "\nFAILED: the probes: ValueError" in text


def test_a_probe_says_readable_only_for_an_answer_it_could_read(monkeypatch):
    answers = {"data-api": (200, [[1, 2]], ""), "data.binance": (200, None, "not JSON, 90 bytes")}
    monkeypatch.setattr(wide, "fetch", lambda url, params=None, tries=3, timeout=30.0: next(v for k, v in answers.items() if k in url))
    assert wide.probes() == {"binance_data_api": {"http": 200, "ok": True, "note": ""},
                             "binance_archive": {"http": 200, "ok": True, "note": ""}}       # the archive file is text, not JSON
    answers = {"data-api": (200, None, "not JSON, 9 bytes"), "data.binance": (403, None, "not JSON, 0 bytes")}
    assert wide.probes() == {"binance_data_api": {"http": 200, "ok": False, "note": "not JSON, 9 bytes"},
                             "binance_archive": {"http": 403, "ok": False, "note": "not JSON, 0 bytes"}}
    answers = {"data-api": (451, {"msg": "restricted location"}, ""), "data.binance": (None, None, "ConnectionError: refused")}
    assert wide.probes() == {"binance_data_api": {"http": 451, "ok": False, "note": "refused"},
                             "binance_archive": {"http": None, "ok": False, "note": "ConnectionError: refused"}}


def test_the_ticker_is_asked_in_batches_when_it_will_not_give_every_pair_at_once(world):
    stock_world(world, n=30)
    world.refuse_whole_ticker = True
    write_settings(top_n=5, history_days=30)
    status = wide.collect(NOW)
    asked = [p for u, p in world.calls if u.endswith("/Ticker")]
    assert asked[0] == {} and len(asked) == 1 + 2 and all(len(p["pair"].split(",")) <= 20 for p in asked[1:])
    assert "XBTUSD" in asked[1]["pair"].split(",") + asked[2]["pair"].split(",")             # by the short names
    assert status["kraken"]["quoted"] == 31 and status["kraken"]["on_the_list"] == 5       # the dollar token is not a pair to ask about
    assert "BTC" in json.loads((wide.root() / "universe.json").read_text())["pairs"]


def test_a_slip_in_the_settings_is_said_in_the_status_and_the_summary(world, capsys):
    stock_world(world)
    write_settings(top_n="lots", history_days=30)
    status = wide.collect(NOW)
    assert status["settings_not_used"] == ["`top_n: 'lots'` in configs/wide.yaml cannot be used; 100 is used"]
    assert "[wide] SETTING NOT USED: `top_n: 'lots'`" in capsys.readouterr().out
    assert "\nSETTING NOT USED: `top_n: 'lots'`" in wide.summary(NOW)


ALARMS = ("FAILED", "STALE", "SETTING NOT USED")


def test_the_summary_says_what_the_run_did(world):
    assert wide.summary() == "wide data\n" + wide.NO_RUN and wide.NO_RUN.startswith("STALE: no run on record")
    stock_world(world)
    write_settings(top_n=4, history_days=150)
    del world.ohlc["C2USD"]
    world.coinbase["C0"] = coinbase_rows(midnight() - 200 * DAY, 200, price=77.0)
    wide.collect(NOW)
    text = wide.summary()
    assert text.splitlines()[0] == "wide data, run of 2026-10-04 00:40Z"
    assert "- Kraken: 7 US dollar pairs, 4 on the list (4 still listed), 4 joined today; 3 read, 120 days of candles added, 4 bid and ask readings" in text
    assert "\nFAILED: candles for 1 of 4 pairs: C2: " in text
    assert "- funding: 1 perpetuals, 10 days added" in text
    assert ("- older history from Coinbase: 1 coins deepened by 110 days, 1 not listed there; prices did not match for 1 "
            "and theirs were not used: C0: closes differ by") in text
    assert "- binance_data_api: not readable from here (http 451, not JSON, 0 bytes)" in text
    assert "STALE" not in text and "SETTING NOT USED" not in text
    (wide.root() / "status.json").write_text("{")
    assert wide.summary() == "wide data\nFAILED: status.json cannot be read (JSONDecodeError)"
    for junk in ('{"kraken": []}', "[]", '"words"', "null", '{"ran": "soon"}', '{"ran": 5, "kraken": {"failed": 7}}',
                 '{"ran": 5, "funding": {"failed": 3}}', '{"ran": 5, "coinbase": {"mismatch": 1}}', '{"ran": 5, "kraken": {"joined_today": 1}}'):
        (wide.root() / "status.json").write_text(junk)
        assert wide.summary().startswith("wide data\nFAILED: status.json cannot be read"), junk


def test_a_record_that_does_not_say_how_the_run_went_is_a_fault(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)
    whole = json.loads((wide.root() / "status.json").read_text())
    for missing, says in (("ok", "FAILED: status.json does not say that the run went through"),
                          ("ran", "FAILED: status.json cannot be read (KeyError)")):
        (wide.root() / "status.json").write_text(json.dumps({k: v for k, v in whole.items() if k != missing}))
        assert says in wide.summary(NOW).splitlines(), missing
    (wide.root() / "status.json").write_text(json.dumps({"ran": NOW}))             # a record of nothing but the time
    assert "FAILED: status.json does not say that the run went through" in wide.summary(NOW).splitlines()
    (wide.root() / "status.json").write_text(json.dumps({**whole, "ok": "yes"}))
    assert "FAILED: status.json does not say that the run went through" in wide.summary(NOW).splitlines()


def test_the_settings_are_reported_as_the_file_stands_now(world):
    """Not as the last run found them: a slip made since shows at once, and goes the moment it is mended."""
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)
    assert "SETTING NOT USED" not in wide.summary(NOW)
    write_settings(top_n="lots", history_days=-1)                                  # two slips, made after the run
    lines = wide.summary(NOW).splitlines()
    assert "SETTING NOT USED: `top_n: 'lots'` in configs/wide.yaml cannot be used; 100 is used" in lines
    assert "SETTING NOT USED: `history_days: -1` in configs/wide.yaml cannot be used; 1825 is used" in lines
    write_settings(top_n=4, history_days=30)                                       # mended, and no run since
    assert "SETTING NOT USED" not in wide.summary(NOW)
    (config.CONFIGS / "wide.yaml").unlink()
    assert "SETTING NOT USED: configs/wide.yaml is missing; the defaults are used" in wide.summary(NOW).splitlines()
    (wide.root() / "status.json").unlink()                                         # and with no run on record it is said as well
    assert wide.summary(NOW).splitlines() == ["wide data", wide.NO_RUN, "SETTING NOT USED: configs/wide.yaml is missing; the defaults are used"]
    (wide.root() / "status.json").write_text("{")
    assert wide.summary(NOW).splitlines()[1:] == ["FAILED: status.json cannot be read (JSONDecodeError)",
                                                  "SETTING NOT USED: configs/wide.yaml is missing; the defaults are used"]


def test_the_report_comes_out_whatever_reading_the_settings_does(world, monkeypatch):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)

    def boom():
        raise ValueError("a file in a shape nobody expected")
    monkeypatch.setattr(wide, "settings", boom)
    lines = wide.summary(NOW).splitlines()
    assert lines[0] == "wide data, run of 2026-10-04 00:40Z" and len(lines) >= 6
    assert "SETTING NOT USED: configs/wide.yaml could not be read (ValueError); the defaults are used" in lines


def test_whatever_a_venue_or_an_error_said_stays_on_its_own_line(world):
    """A line break inside a failure's text must not start a line of its own: it could begin with one of the
    three words, or with none of them, and the agent is told to go by how a line begins."""
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)
    clean = wide.summary(NOW).splitlines()
    record = json.loads((wide.root() / "status.json").read_text())
    nasty = "X: boom\nSTALE: not really\r\nFAILED: nor this\n\nan orphan line"
    record["kraken"]["failed"] = [nasty] * 7
    record["kraken"]["quotes_failed"] = nasty
    record["funding"]["failed"] = [nasty]
    record["coinbase"]["failed"], record["coinbase"]["mismatch"] = [nasty], [nasty]
    record["probes"] = {"error": nasty, "binance_data_api": {"http": 451, "ok": False, "note": nasty}}
    record["ran_utc"] = "2026-10-04 00:40Z\nSTALE: forged"
    (wide.root() / "status.json").write_text(json.dumps(record))
    lines = wide.summary(NOW).splitlines()
    assert len(lines) == len(clean) + 5 - 1                                        # five lines of faults more, one probe line fewer
    assert not any(ln.startswith("STALE") for ln in lines) and "an orphan line" not in lines
    assert [ln.split(":")[0] for ln in lines if ln.startswith("FAILED")] == ["FAILED"] * 5
    for ln in lines:
        assert ln.startswith(ALARMS) or ln.startswith(("wide data", "- "))
    assert "FAILED: candles for 7 of 4 pairs: X: boom STALE: not really FAILED: nor this an orphan line; X: boom" in "\n".join(lines)
    assert lines[0] == "wide data, run of 2026-10-04 00:40Z STALE: forged"
    # all seven failed pairs are counted, though five are shown
    assert [ln for ln in lines if ln.startswith("FAILED: candles")][0].count("X: boom") == 5


def test_a_last_run_that_is_old_is_said_and_one_dropped_ask_is_not(world):
    """The asks are at 00:40 and 12:40 UTC and the agent reads at 22:00."""
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)                                                              # 00:40 on day one
    at = lambda day, hour: midnight() + day * DAY + hour * 3600                    # noqa: E731
    assert "STALE" not in wide.summary(at(0, 22))                                  # read that evening
    assert "STALE" not in wide.summary(at(1, 0))                                   # and before the next day's first ask
    assert "STALE" not in wide.summary(NOW + 29 * 3600) and "\nSTALE: the last run is 1.3 days old" in wide.summary(NOW + 31 * 3600)
    assert "\nSTALE: the last run is 1.9 days old" in wide.summary(at(1, 22))      # both asks of day two failed
    wide.collect(at(0, 12) + 40 * 60)                                              # the last good run was the 12:40 one
    assert "STALE" not in wide.summary(at(0, 22)) and "\nSTALE: the last run is 1.4 days old" in wide.summary(at(1, 22))
    assert wide.STALE_AFTER_S == 30 * 3600


def test_every_line_about_a_fault_begins_with_its_word_and_no_other_line_does(world, monkeypatch):
    """CLAUDE.md and the agent's run sheet tell the agent to look for lines that BEGIN with one of three
    words. Everything that can go wrong at once, and before it the same run with nothing wrong."""
    stock_world(world)
    write_settings(top_n=4, history_days=150)
    wide.collect(NOW)
    clean = wide.summary(NOW).splitlines()
    assert len(clean) >= 5 and not any(a in ln for ln in clean for a in ALARMS)

    def boom(*a, **k):
        raise ValueError("FAILED to parse a STALE answer")                         # even with the words inside a message
    write_settings(top_n="lots", history_days=400, min_usd_volume=5e12)
    del world.ohlc["C2USD"]
    wide.quotes_path(2026).write_text("")
    world.broken.add("/tickers")
    monkeypatch.setattr(wide, "probes", boom)
    world.coinbase["C0"] = [r + ["odd"] for r in coinbase_rows(midnight() - 500 * DAY, 500)]
    wide.collect(NOW + DAY)
    lines = wide.summary(NOW + 3 * DAY).splitlines()
    alarms = [ln for ln in lines if ln.startswith(ALARMS)]
    assert sorted(ln.split(":")[0] for ln in alarms) == ["FAILED"] * 6 + ["SETTING NOT USED", "STALE"]
    said = " ".join(alarms)
    for what in ("candles for 1 of 4 pairs", "bid and ask readings were not written", "funding for 1", "older history for",
                 "the probes", "not one coin qualified", "`top_n: 'lots'`", "the last run is 2.0 days old"):
        assert what in said, what
    for ln in lines:                                                               # and the words begin no other line
        assert ln.startswith(ALARMS) or ln.startswith(("wide data", "- "))
    # a run that stopped, a record that cannot be read, and no record at all each say so in a line that begins the same way
    for alt in ("C0USD", "C1USD"):
        del world.ohlc[alt]
    with pytest.raises(wide.WideError):
        wide.collect(NOW + 4 * DAY)
    assert "FAILED: the run stopped because most pairs could not be read; nothing of it was committed" in wide.summary(NOW + 4 * DAY).splitlines()
    (wide.root() / "status.json").write_text("{")
    assert wide.summary().splitlines()[1].startswith("FAILED: status.json cannot be read")
    (wide.root() / "status.json").unlink()
    assert wide.summary().splitlines()[1].startswith("STALE: no run on record")


def sheet_steps(sheet: str) -> list[tuple[int, str]]:
    """The numbered steps of the agent's run sheet, each on one line however the file wraps it."""
    steps, open_step = [], False
    for ln in sheet.splitlines():
        m = re.match(r"(\d+)\. (.*)", ln)
        if m:
            steps.append([int(m.group(1)), m.group(2).strip()])
            open_step = True
        elif open_step and ln.strip():
            steps[-1][1] += " " + ln.strip()
        else:
            open_step = False
    return [(n, body) for n, body in steps]


def test_the_agent_is_told_to_run_the_report_and_which_words_to_look_for():
    """What is held is the shape, not the wording: the step is there, before anything is committed, it names
    the three words, and the command is nowhere given with the flag that collects."""
    sheet = (REPO / ".github" / "agent_prompt.md").read_text(encoding="utf-8")
    manual = " ".join((REPO / "CLAUDE.md").read_text(encoding="utf-8").split())
    for text in (" ".join(sheet.split()), manual):
        assert "python -m bot.wide" in text and "FAILED, STALE or SETTING NOT USED" in text and "--collect" in text
        assert "bot.wide --collect" not in text and "bot.wide` --collect" not in text
    steps = sheet_steps(sheet)
    assert [n for n, _ in steps] == list(range(1, len(steps) + 1)) and len(steps) >= 5     # numbered in order
    ours = [i for i, (_, body) in enumerate(steps) if "python -m bot.wide" in body]
    assert len(ours) == 1
    body = steps[ours[0]][1]
    assert "never add `--collect`" in body and "FAILED, STALE or SETTING NOT USED" in body
    commits = [i for i, (_, body) in enumerate(steps) if re.search(r"\bcommit", body, re.I)]
    assert commits and ours[0] < commits[0]                                                # before anything is committed
    # the same sheet wrapped at 72 columns reads the same
    import textwrap
    wrapped = "\n".join(textwrap.fill(ln, 72, subsequent_indent="   ") if re.match(r"\d+\. ", ln) else ln for ln in sheet.splitlines())
    assert wrapped != sheet and sheet_steps(wrapped) == steps


def test_a_clean_run_has_no_line_that_asks_for_anyones_time(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)
    text = wide.summary(NOW + DAY)
    assert "FAILED" not in text and "STALE" not in text and "SETTING NOT USED" not in text
    record = json.loads((wide.root() / "status.json").read_text())
    assert record["kraken"].pop("qualified_today") == 7
    (wide.root() / "status.json").write_text(json.dumps(record))
    assert "FAILED" not in wide.summary(NOW + DAY)                                 # a record with no count of who qualified is not one that says nobody did


def test_reading_is_the_default_and_collecting_takes_a_flag(world, capsys):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    for argv in ([], ["--summary"], ["--again"], ["collect"], ["-collect"], ["--COLLECT"]):
        assert wide.main(argv) == 0
        assert "no run on record" in capsys.readouterr().out
    assert world.calls == [] and not wide.root().exists()                          # nobody was asked and nothing was written
    assert wide.main(["--collect"]) == 0
    assert "wide data, run of 2026-10-04 00:40Z" in capsys.readouterr().out and wide.root().exists()
    world.broken.add("/AssetPairs")
    assert wide.main(["--collect", "--again"]) == 1
    assert "[wide] stopped: kraken AssetPairs: http 503" in capsys.readouterr().out


def test_the_second_ask_of_a_day_does_nothing_and_a_run_by_hand_collects_again(world, capsys, monkeypatch):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    assert wide.ran_today() is None
    assert wide.main(["--collect"]) == 0
    assert wide.ran_today() == "2026-10-04 00:40Z"
    files = {p: p.read_bytes() for p in wide.root().rglob("*") if p.is_file()}
    calls = len(world.calls)
    capsys.readouterr()
    monkeypatch.setattr(wide, "_now", lambda: NOW + 12 * 3600)
    assert wide.main(["--collect"]) == 0
    out = capsys.readouterr().out
    assert "already collected today (run of 2026-10-04 00:40Z); nothing to do" in out and "--again" not in out
    assert len(world.calls) == calls                                               # nobody was asked anything
    assert {p: p.read_bytes() for p in wide.root().rglob("*") if p.is_file()} == files     # and nothing was written
    assert wide.main(["--collect", "--again"]) == 0 and len(world.calls) > calls
    assert wide.ran_today() == "2026-10-04 12:40Z"
    monkeypatch.setattr(wide, "_now", lambda: midnight() + DAY - 1)
    assert wide.ran_today() == "2026-10-04 12:40Z"                                 # the last second of the day
    monkeypatch.setattr(wide, "_now", lambda: midnight() + DAY)
    assert wide.ran_today() is None                                                # a new day


def test_a_run_that_failed_or_read_no_pair_or_left_no_record_is_not_a_day_done(world):
    wide.root().mkdir(parents=True)
    good = {"ran": NOW - 60, "ok": True, "kraken": {"pairs_read": 5}}
    for text in ("", "{", "[]", json.dumps({"ran": NOW, "ok": True}), json.dumps({**good, "kraken": {"pairs_read": 0}}),
                 json.dumps({**good, "ran": "soon"}), json.dumps({**good, "ok": False}), json.dumps({**good, "ok": "yes"}),
                 json.dumps({k: v for k, v in good.items() if k != "ok"})):
        (wide.root() / "status.json").write_text(text)
        assert wide.ran_today() is None, text
    (wide.root() / "status.json").write_text(json.dumps(good))
    assert wide.ran_today() == "2026-10-04"                                        # no ran_utc on record: the day stands in


def test_the_panel_puts_every_coin_side_by_side(world):
    stock_world(world)
    write_settings(top_n=4, history_days=30)
    wide.collect(NOW)
    px = wide.panel()
    assert sorted(px.columns) == ["BTC", "C0", "C1", "C2"] and len(px) == 40
    assert px.index.is_monotonic_increasing and str(px.index.tz) == "UTC"
    assert px["C0"].iloc[-1] == pytest.approx(5.0) and px.index[-1] == pd.Timestamp("2026-10-03", tz="UTC")
    assert sorted(wide.panel(min_days=41).columns) == [] and sorted(wide.panel(min_days=40).columns) == ["BTC", "C0", "C1", "C2"]
    assert list(wide.panel("volume")["C1"].unique()) == [100.5]


# --- it stays apart -------------------------------------------------------------

def test_the_collector_carries_nothing_the_gate_forbids():
    """The code only. The settings file is Fin's to write in, and a word in one of his comments there
    (a coin that has "withdrawn" its delisting, say) must not turn this suite red."""
    from gate import check_protected
    src = (REPO / "bot" / "wide.py").read_text(encoding="utf-8")
    for pat in check_protected.FORBIDDEN:
        assert not re.search(pat, src), pat
    assert "/0/private" not in src and "/public" in src


def test_the_collector_and_its_settings_are_protected():
    from gate import check_protected
    patterns = check_protected.load_patterns(REPO / "PROTECTED.txt")
    for path in ("bot/wide.py", "configs/wide.yaml", "state/wide/universe.json", ".github/workflows/wide.yml", "tests/gate/test_wide.py"):
        assert any(check_protected.matches(path, p) for p in patterns), path


def test_no_strategy_is_handed_the_wide_data():
    src = (REPO / "bot" / "strategy.py").read_text(encoding="utf-8")
    assert not re.search(r"^\s*(from\s+\S*\s+import\s+[^\n]*\bwide\b|import\s+[^\n]*\bwide\b)", src, re.M)
    assert "state/wide" not in src and "bot.wide" not in src
    assert names_the_collector(src, folder_name=False) == []


LOOP = ("__init__", "run", "promote", "report", "slot", "config", "data", "paper", "risk", "shadow", "backtest")


def names_the_collector(src: str, folder_name: bool = True) -> list[str]:
    """Where a module imports the collector or spells out its folder. `folder_name`: the bare word "wide"
    as a piece of text counts too (as in `config.STATE / "wide"`); not asked of bot/strategy.py, where the
    agent may well call a band or a stop wide."""
    import ast
    found = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Import) and any(a.name.split(".")[-1] == "wide" for a in node.names):
            found.append(f"line {node.lineno}: an import of wide")
        if isinstance(node, ast.ImportFrom) and ((node.module or "").split(".")[-1] == "wide" or any(a.name == "wide" for a in node.names)):
            found.append(f"line {node.lineno}: an import of wide")
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if "state/wide" in node.value or "bot.wide" in node.value or (folder_name and node.value == "wide"):
                found.append(f"line {node.lineno}: the text {node.value[:30]!r}")
    return found


def test_no_module_of_the_hourly_loop_names_the_collector():
    """The driven tests below see only the lines three hours of the loop happen to run, about three in
    five. This reads every line of every module, for the plain ways of leaning on the collector: an
    import of it, or its folder spelled out. A way that is neither plain nor run is seen by nothing."""
    for module in LOOP:
        assert names_the_collector((REPO / "bot" / f"{module}.py").read_text(encoding="utf-8")) == [], module
    for leaning in ("from . import wide", "from .wide import panel", "import bot.wide as w", "from bot import config, wide",
                    'p = config.STATE / "wide" / "status.json"', 'open("state/wide/universe.json")',
                    '__import__("importlib").import_module("bot.wide")'):
        assert names_the_collector(leaning), leaning                                         # the reading itself bites
    for innocent in ("x = 'a wide band'", "from . import config, data", "import widening", "wide = 3", "reason = f'{pair}: spread too wide'"):
        assert names_the_collector(innocent) == [], innocent
    assert names_the_collector('band = "wide"') and names_the_collector('band = "wide"', folder_name=False) == []


def switches_of(fn) -> list[str]:
    """The settings a strategy's code reads as switches: `params.get("x")`, or with True, False or None to fall back on."""
    import inspect
    try:
        src = inspect.getsource(getattr(fn, "func", fn))
    except (TypeError, OSError):                      # no source to read (a strategy made out of another, say): nothing to turn on
        return []
    return sorted(set(re.findall(r"""params\.get\(\s*["'](\w+)["']\s*(?:,\s*(?:True|False|None)\s*)?\)""", src)))


def within(seconds: float, fn, *args):
    """One call, stopped if it has not come back in this many seconds: a strategy that never returns on
    made up settings must not hang the suite, and with it the gate."""
    import signal
    if not hasattr(signal, "setitimer"):
        return fn(*args)

    def out_of_time(signum, frame):
        raise TimeoutError(f"still running after {seconds:.0f} seconds")
    try:
        before = signal.signal(signal.SIGALRM, out_of_time)
    except ValueError:                                # not the main thread: no alarm to be had
        return fn(*args)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return fn(*args)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, before)


def test_the_helpers_of_the_strategy_check_do_what_they_say():
    import functools

    def reads(candles, params, current_weights):
        a = params.get("market_filter")
        b = params.get("fresh_cross", False)
        c = params.get( 'again' , None )
        d = params.get("step", 2)
        e = params["lookback_hours"]
        f = params.get("ratio", 0.5)
        return a, b, c, d, e, f
    assert switches_of(reads) == ["again", "fresh_cross", "market_filter"]           # the switches, and no number
    assert switches_of(functools.partial(reads, {})) == ["again", "fresh_cross", "market_filter"]
    assert switches_of(len) == [] and switches_of(functools.partial(len)) == []        # nothing to read: nothing to turn on

    def never_returns(step):
        h = 100
        while h > 0:
            h //= step                                # with a step of True this goes round for ever
        return h
    assert within(5.0, never_returns, 3) == 0
    with pytest.raises(TimeoutError, match="still running after 0 seconds"):
        within(0.2, never_returns, True)
    assert within(5.0, never_returns, 7) == 0                                         # and the alarm is put away afterwards


def what_strategies_open(strategies: dict, candles: dict, repo_configs: list, watching) -> tuple[list, int]:
    """Calls every one of these strategies on these candles: with no settings, with the settings of each
    repo config that names it, and with every switch its own code asks for turned on, one at a time (a
    read that waits behind a setting no config uses yet is still a read; only settings read as switches,
    because a number set to True could send a strategy round for ever), each time holding nothing and
    holding something. Returns what was opened or listed under a state/wide, and how many calls ran through."""
    asked = [(name, {}) for name in sorted(strategies)]
    asked += [(name, params) for name, params in repo_configs if name in strategies]
    for name, fn in sorted(strategies.items()):
        base = next((params for n, params in asked if n == name and params), {})
        for key in switches_of(fn):
            asked.append((name, {**base, key: True}))
    ran = 0
    with watching() as seen:
        for name, params in asked:
            for held in (0.0, 0.1):
                try:
                    within(10.0, strategies[name], {p: df.copy() for p, df in candles.items()}, dict(params), {p: held for p in candles})
                    ran += 1
                except Exception:  # noqa: BLE001 - whether it copes with these candles and settings is not what is asked here
                    pass
        touched = list(seen)
    return touched, ran


def test_no_strategy_opens_the_wide_data_when_it_is_called(tmp_path, hourly):
    """bot/strategy.py is the one file of the loop the agent may change, and a strategy that read the
    collector's files would see days its backtest had not reached yet. Every strategy on the books is
    called on made up candles beside a full state/wide. Not one may open a file or list a folder under a
    state/wide, in the root the candles are in or in the checkout itself."""
    from bot import strategy
    root = tmp_path / "root"
    feed = hourly.Feed()
    hourly.plant(root, feed)
    config.STATE = root / "state"                       # put back by the `hourly` fixture
    source = data.SyntheticSource(hourly.RISK["pairs"], n=2160, seed=7, start=hourly.HOUR0 - 2160 * 3600)
    candles = {pair: source.ohlc(pair) for pair in hourly.RISK["pairs"]}
    repo_configs, hypotheses = [], []
    for path in sorted((REPO / "configs").glob("*.yaml")):
        try:
            cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001 - a config that cannot be read is another test's business
            continue
        if isinstance(cfg, dict) and isinstance(cfg.get("strategy"), str):
            repo_configs.append((cfg["strategy"], cfg.get("params") if isinstance(cfg.get("params"), dict) else {}))
            if re.fullmatch(r"[A-Za-z0-9_-]{1,40}", str(cfg.get("hypothesis"))):
                hypotheses.append(str(cfg["hypothesis"]))
    # The bench's readings are there as well, one under every hypothesis the repo's configs name: a strategy
    # that read its own reading would be trading on five years it is about to be tested on. The same watch
    # sees a state/bench, here and in the checkout itself (tests/gate/test_bench.py holds that it does).
    hourly.plant_bench(root, sorted(set(hypotheses) - {"H9"}))
    assert len(strategy.STRATEGIES) >= 1 and any(name in strategy.STRATEGIES for name, _ in repo_configs)
    touched, ran = what_strategies_open(strategy.STRATEGIES, candles, repo_configs, hourly.watching)
    assert touched == [], touched
    assert ran >= 2                                     # the repo's own configs, at the least, ran through

    # Whichever names the repo's configs go by on the day this runs: the first of them, or the one that is
    # always planted. A name written out here would turn the gate red on the day a promotion retired it.
    its_own = (sorted(set(hypotheses)) or ["H9"])[0]

    def reads_its_reading(candles, params, current_weights):
        on_file = config.STATE / "bench" / f"{its_own}.json"    # only when there is one: asking whether a file is there is not seen
        return {"BTC": 0.2} if on_file.exists() and "beaten" in on_file.read_text() else {}
    touched, ran = what_strategies_open({"r": reads_its_reading}, candles, [], hourly.watching)
    assert touched == [f"open state/bench/{its_own}.json"] * 2 and ran == 2

    # and the check itself bites, on the kinds of read that are easiest to miss
    def behind_a_switch(candles, params, current_weights):
        if params.get("market_filter"):                 # a setting no config in the repo uses
            (config.STATE / "wide" / "universe.json").read_text()
        return {}

    def only_when_holding(candles, params, current_weights):
        if any(w > 0 for w in current_weights.values()):
            try:                                        # the checkout's own folder, its name put together so no search finds it
                (REPO / "state" / ("wi" + "de") / "daily" / "BTC.csv").read_text()
            except OSError:
                pass
        return {}

    def with_its_settings_only(candles, params, current_weights):
        return sorted((config.STATE / "wide" / "daily").iterdir()) if params.get("lookback_hours") == 99 else {}
    touched, ran = what_strategies_open({"a": behind_a_switch}, candles, [], hourly.watching)
    assert touched == ["open state/wide/universe.json"] * 2 and ran == 4            # no settings twice, the switch on twice
    touched, ran = what_strategies_open({"b": only_when_holding}, candles, [], hourly.watching)
    assert touched == ["open state/wide/daily/BTC.csv"] and ran == 2
    touched, ran = what_strategies_open({"c": with_its_settings_only}, candles, [("c", {"lookback_hours": 99}), ("zzz", {})], hourly.watching)
    assert len(touched) == 2 and all(x.endswith("state/wide/daily") for x in touched)       # with the repo's settings for it, and only then
    assert ran == 6                                     # no settings, the repo's settings, and its one switch on: twice each


@pytest.fixture
def hourly(monkeypatch):
    """hourly_driver points the bot's paths and its candle sources somewhere else; put them back afterwards."""
    for name in hourly_driver.PATHS:
        monkeypatch.setattr(config, name, getattr(config, name))
    monkeypatch.setattr(data, "get_source", data.get_source)
    monkeypatch.setattr(data, "get_history_source", data.get_history_source)
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)
    return hourly_driver


def files_only(tree: dict) -> dict:
    return {k: v for k, v in tree.items() if not k.endswith("/")}


def workflow():
    return yaml.safe_load((REPO / ".github" / "workflows" / "wide.yml").read_text(encoding="utf-8"))


def step(wf, name):
    found = [s for s in wf["jobs"]["collect"]["steps"] if s.get("name") == name]
    assert len(found) == 1, name
    return found[0]


def test_the_workflow_commits_only_its_own_folder_and_never_queues_with_the_bot():
    wf = workflow()
    others = [yaml.safe_load(p.read_text(encoding="utf-8")) for p in sorted((REPO / ".github" / "workflows").glob("*.yml")) if p.name != "wide.yml"]
    groups = [str((o.get("concurrency") or {}).get("group")) for o in others if isinstance(o.get("concurrency"), dict)]
    groups += [str(o["concurrency"]) for o in others if isinstance(o.get("concurrency"), str)]
    assert wf["concurrency"]["group"] == "wide-data" and "wide-data" not in " ".join(groups)       # a group of its own
    assert wf["concurrency"]["cancel-in-progress"] is False
    assert wf["permissions"] == {"contents": "write"}
    assert set(wf["jobs"]) == {"collect"} and "defaults" not in wf and "defaults" not in wf["jobs"]["collect"]
    # GitHub cancels the job at this many minutes, and a cancelled job commits nothing: it must be longer
    # than all the time the collector allows itself (bot/wide.py) on the longest list Kraken could give,
    # with ten minutes over for what has no allowance (the list and the ticker, the last request of each
    # part, the probes, setting the job up)
    limit = wf["jobs"]["collect"]["timeout-minutes"] * 60
    assert wide.candles_budget(wide.MOST_PAIRS) + wide.FUNDING_BUDGET_S + wide.DEEPEN_BUDGET_MAX_S + 600 <= limit <= 3600
    steps = wf["jobs"]["collect"]["steps"]
    checkout = steps[0]
    assert checkout["uses"].startswith("actions/checkout@") and checkout["with"]["ref"] == "main"       # the tip, so the day's work lands on it
    commit = step(wf, "Commit")["run"]
    adds = [ln.strip() for ln in commit.splitlines() if ln.strip().startswith("git add")]
    assert adds == ["git add -A state/wide"]
    commits = [ln.strip() for ln in commit.splitlines() if ln.strip().startswith("git commit")]
    assert len(commits) == 1 and " -a" not in commits[0] and "--all" not in commits[0] and commits[0].startswith('git commit -q -m "wide: ')
    assert "git pull --rebase" in commit and "git push" in commit and "--force" not in commit and "-f " not in commit
    assert step(wf, "Install")["run"] == "pip install -q -r requirements.txt"         # what the hourly bot runs on
    pythons = [str((s.get("with") or {}).get("python-version", "")) for s in steps if str(s.get("uses", "")).startswith("actions/setup-python@")]
    for version in pythons:                                                           # a Python the code runs on, where one is named
        named = re.fullmatch(r"(\d+)\.(\d+)(\.\d+)?", version)
        assert not named or (int(named.group(1)), int(named.group(2))) >= (3, 11), version
    run_step = step(wf, "Collect")
    assert run_step["id"] == "collect"
    assert run_step["run"] == "python -m bot.wide --collect ${{ github.event_name == 'workflow_dispatch' && '--again' || '' }}"
    assert set(run_step) == {"name", "id", "run"}                                     # no `if`, no other folder, no carrying on after an error
    assert set(step(wf, "Commit")) == {"name", "run"}                                 # a failed run commits nothing
    summary = step(wf, "Summary")
    assert "python -m bot.wide >>" in summary["run"] and "--collect" not in summary["run"]
    assert summary["if"] == "always()"                                               # a red run still says what went wrong
    assert "${{ steps.collect.outcome }}" in summary["run"]                          # and that it is this run that went wrong
    triggers = wf.get("on", wf.get(True))
    assert set(triggers) == {"schedule", "workflow_dispatch"}                         # never on a push or a pull request
    assert triggers["schedule"] == [{"cron": "40 0,12 * * *"}]
    assert [s.get("name") for s in steps if s.get("name")] == ["Install", "Collect", "Summary", "Commit"]


def git(cwd, *args, env=None):
    r = subprocess.run(["git", *args], cwd=cwd, env=env, capture_output=True, text=True)
    assert r.returncode == 0, (args, r.stderr[-300:])
    return r.stdout


@pytest.fixture
def checkout(tmp_path):
    """A bare `origin` with one commit, a checkout of it as the job has it, and a way to run the
    workflow's own Commit step in that checkout the way GitHub runs it (`bash -e`), with no waiting."""
    home, tools = tmp_path / "home", tmp_path / "tools"
    home.mkdir()
    tools.mkdir()
    (tools / "sleep").write_text(f'#!/bin/sh\necho "$1" >> "{tmp_path}/slept"\n')        # the script's waits are noted, not waited
    (tools / "sleep").chmod(0o755)
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"HOME": str(home), "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1", "GIT_TERMINAL_PROMPT": "0",
                "PATH": f"{tools}{os.pathsep}{env.get('PATH', '')}"})
    me = ("-c", "user.name=somebody", "-c", "user.email=somebody@example.com")
    origin, seed, work = tmp_path / "origin.git", tmp_path / "seed", tmp_path / "work"
    git(tmp_path, "init", "-q", "--bare", "-b", "main", str(origin), env=env)
    git(tmp_path, "init", "-q", "-b", "main", str(seed), env=env)
    for rel, text in (("README.md", "a repo\n"), ("state/summary.md", "hour 1\n"), ("state/wide/status.json", "{}\n"), ("bot/wide.py", "pass\n")):
        (seed / rel).parent.mkdir(parents=True, exist_ok=True)
        (seed / rel).write_text(text)
    git(seed, "add", "-A", env=env)
    git(seed, *me, "commit", "-q", "-m", "state: the first hour", env=env)
    git(seed, "push", "-q", str(origin), "main", env=env)
    git(tmp_path, "clone", "-q", str(origin), str(work), env=env)
    script = tmp_path / "commit.sh"
    script.write_text(step(workflow(), "Commit")["run"])

    def commit_step():
        return subprocess.run(["bash", "-e", str(script)], cwd=work, env=env, capture_output=True, text=True)

    def collected(day):
        (work / "state" / "wide" / "daily").mkdir(parents=True, exist_ok=True)
        (work / "state" / "wide" / "status.json").write_text(f'{{"day": {day}}}\n')
        (work / "state" / "wide" / "daily" / "BTC.csv").write_text("time,close\n" + "".join(f"{d},1\n" for d in range(day + 1)))
        (work / "bot" / "__pycache__").mkdir(exist_ok=True)
        (work / "bot" / "__pycache__" / "wide.pyc").write_text("left by the run")           # what a run leaves beside its data
        (work / "scratch.txt").write_text("and a stray file")
    return types.SimpleNamespace(work=work, origin=origin, seed=seed, env=env, me=me, commit_step=commit_step, collected=collected,
                                 slept=lambda: (tmp_path / "slept").read_text().split() if (tmp_path / "slept").exists() else [])


def test_the_commit_step_itself_commits_the_days_work_and_only_that(checkout):
    """The step is the one part of the job that makes the data last, and it is a shell script nobody
    runs until the first night. Here it is run, as written in the workflow, against a real repo."""
    c = checkout
    c.collected(1)
    r = c.commit_step()
    assert r.returncode == 0 and "pushed on attempt 1" in r.stdout, (r.stdout, r.stderr)
    subject, author = git(c.origin, "log", "-1", "--format=%s%n%an <%ae>", "main", env=c.env).splitlines()
    assert re.fullmatch(r"wide: \d{4}-\d{2}-\d{2}", subject) and author == "quantloop-bot <quantloop-bot@users.noreply.github.com>"
    changed = git(c.origin, "show", "--name-only", "--format=", "main", env=c.env).split()
    assert sorted(changed) == ["state/wide/daily/BTC.csv", "state/wide/status.json"]         # the data, and nothing a run leaves beside it
    assert git(c.origin, "rev-list", "--count", "main", env=c.env).strip() == "2"
    # the second ask of a day finds nothing new: green, and nothing committed
    head = git(c.origin, "rev-parse", "main", env=c.env)
    r = c.commit_step()
    assert r.returncode == 0 and "nothing to commit" in r.stdout and git(c.origin, "rev-parse", "main", env=c.env) == head
    assert c.slept() == []


def test_the_commit_step_lands_on_top_of_an_hour_the_bot_recorded_meanwhile(checkout):
    c = checkout
    (c.seed / "state" / "summary.md").write_text("hour 2\n")                 # the hourly bot commits while the collector is at work
    git(c.seed, "add", "-A", env=c.env)
    git(c.seed, *c.me, "commit", "-q", "-m", "state: the second hour", env=c.env)
    git(c.seed, "push", "-q", str(c.origin), "main", env=c.env)
    c.collected(2)
    r = c.commit_step()
    assert r.returncode == 0 and "pushed on attempt 1" in r.stdout, (r.stdout, r.stderr)
    subjects = git(c.origin, "log", "--format=%s", "main", env=c.env).splitlines()
    assert len(subjects) == 3 and subjects[0].startswith("wide: ") and subjects[1:] == ["state: the second hour", "state: the first hour"]
    assert git(c.origin, "show", "main:state/summary.md", env=c.env) == "hour 2\n"          # the bot's hour is not undone
    assert git(c.origin, "show", "main:state/wide/status.json", env=c.env) == '{"day": 2}\n'


def test_the_commit_step_fails_when_the_days_work_cannot_be_pushed(checkout):
    c = checkout
    c.collected(3)
    git(c.work, "remote", "set-url", "origin", str(c.origin) + ".gone", env=c.env)
    r = c.commit_step()
    assert r.returncode == 1 and "push failed after 5 attempts" in r.stdout          # red, so that somebody is told
    assert c.slept() == ["20", "40", "60", "80", "100"]                              # having tried five times, further apart each time
    assert git(c.origin, "rev-list", "--count", "main", env=c.env).strip() == "1"


# --- the hourly loop itself, driven: the slow tests, kept last so that a quicker failure shows first ------

def test_the_hourly_loop_is_the_same_with_and_without_the_wide_data(tmp_path, hourly):
    """Not a search of the source for a word: the loop itself, run both ways, as the hourly workflow runs
    it. Beside it sits a state/wide holding every kind of file the collector writes, and folders that
    look like accounts, candle caches, an archive and a summary. What the loop prints and says, and every
    file and folder it leaves, must come out the same, and everything under state/wide must be as it was."""
    plain_said, plain_files, none_before, none_after, _ = hourly.drive(tmp_path / "plain", bait=False)
    bait_said, bait_files, wide_before, wide_after, touched = hourly.drive(tmp_path / "bait", bait=True)
    assert none_before == {} and none_after == {}                                  # the loop makes no state/wide and no state/bench of its own
    assert len(plain_said) == 9 and plain_said == bait_said                        # what it printed, the slots and the free slots, three hours
    assert sorted(plain_files) == sorted(bait_files) and plain_files == bait_files
    assert len(files_only(wide_before)) == 24 and wide_after == wide_before        # all that was planted, untouched, and no folder added
    assert "state/wide/daily/" in wide_before and "state/candles/" in plain_files  # folders are part of what is compared
    for kind in ("universe.json", "status.json", "deepen.json", "daily/BTC.csv", "quotes/2026.csv", "funding/PF_XBTUSD.csv",
                 "champion/account.json", "challenger9/meta.json", "candles/BTC.csv", "history/ETH.csv", "archive/H1/trades.csv", "summary.md"):
        assert f"state/wide/{kind}" in wide_before, kind
    # it was the whole hourly job that ran, each of the three hours: the accounts, the history backfill
    # (which the repo's own risk.yaml has switched on), the rulings, the report written to file
    for hour in (0, 1, 2):
        printed = plain_said[3 * hour]
        assert "[champion] ts_momentum (H0)" in printed and "[challenger1] ts_momentum (H9)" in printed
        assert "[promote] challenger1: H9 on day" in printed and "[report] wrote <root>/state/summary.md" in printed
    assert "[data] BTC: backfilled 1100 hourly candles" in plain_said[0] and "state/history/BTC.csv" in plain_files
    assert "state/summary.md" in plain_files and "state/challenger1/account.json" in plain_files and "state/champion/equity.csv" in plain_files
    # The bench's readings sit beside the second run only, one of them flattering the test in the slot, and
    # the loop leaves them as they were. So everything compared above was compared with the readings there
    # and without them: a loop that so much as printed whether one was on file would have failed here.
    for name, content in hourly.BENCH_FILES.items():
        assert wide_before[f"state/bench/{name}"] == content == wide_after[f"state/bench/{name}"]
    assert sorted(k for k in wide_before if k.startswith("state/bench")) == ["state/bench/", "state/bench/H9.json", "state/bench/README.md"]
    assert not any("bench" in k for k in plain_files) and not any("bench" in k for k in bait_files)
    assert plain_files["state/champion/equity.csv"].count(b"\n") == 4              # a header and three hours
    assert "2026-09-21 22:10Z" in plain_said[0] and "2026-09-22 00:10Z" in plain_said[6]      # across a UTC midnight
    assert b"generated 2026-09-22 00:10Z" in plain_files["state/summary.md"]                  # and the report is the hour's, not the wall clock's
    # "never reads" is meant to the letter: in three hours the loop opened none of those files and listed
    # none of those folders (a read that is thrown away changes nothing above, and can still stop an hour)
    assert touched == []
    with hourly.watching() as seen:                                                # and the watch itself bites
        (tmp_path / "bait" / "state" / "wide" / "status.json").read_text()
        sorted((tmp_path / "bait" / "state" / "wide" / "daily").iterdir())
        pd.read_csv(tmp_path / "bait" / "state" / "wide" / "daily" / "BTC.csv")
        (tmp_path / "bait" / "state" / "champion" / "equity.csv").read_text()      # not under state/wide: not noted
        fd = os.open(tmp_path / "bait" / "state" / "wide" / "funding", os.O_RDONLY)    # a folder listed by file descriptor
        try:
            by_descriptor = len(os.listdir(fd))
        finally:
            os.close(fd)
        try:
            (REPO / "state" / "wide" / "no such file").read_text()                 # the checkout's own state/wide is watched too
        except OSError:
            pass
        (tmp_path / "another name").symlink_to(tmp_path / "bait" / "state" / "wide", target_is_directory=True)
        (tmp_path / "another name" / "deepen.json").read_text()                    # and a road to it under another name
        noted = list(seen)
    assert {"open state/wide/status.json", "open state/wide/daily/BTC.csv", "open state/wide/no such file",
            "open state/wide/deepen.json"} <= set(noted)
    assert {"os.listdir state/wide/daily", "os.scandir state/wide/daily"} & set(noted)          # a listing, however this Python does it
    assert all(n.split(" ", 1)[1].startswith("state/wide/") for n in noted)                     # and nothing from anywhere else
    assert by_descriptor == 1 and (not Path("/proc/self/fd").exists() or "os.listdir state/wide/funding" in noted)
    (tmp_path / "bait" / "state" / "wide" / "status.json").read_text()
    assert seen == noted                                                           # and it notes nothing once it is closed


def loop_in_a_copy(tmp_path, name, edits=()):
    """Three hours of the hourly loop in a process of its own, on a copy of bot/ in which the collector
    cannot be imported, with a full state/wide beside it. `edits` are (file, old, new) changes made to
    the copy first."""
    code = tmp_path / name
    shutil.copytree(REPO / "bot", code / "bot", ignore=shutil.ignore_patterns("__pycache__"))
    (code / "bot" / "wide.py").write_text('raise RuntimeError("the collector must not be imported by the hourly loop")\n')
    (code / "bot" / "bench.py").write_text('raise RuntimeError("the bench must not be imported by the hourly loop")\n')
    shutil.copy(REPO / "tests" / "gate" / "hourly_driver.py", code / "hourly_driver.py")
    for file, old, new in edits:
        src = (code / "bot" / file).read_text(encoding="utf-8")
        assert src.count(old) == 1, (file, old)
        (code / "bot" / file).write_text(src.replace(old, new), encoding="utf-8")
    env = {k: v for k, v in os.environ.items() if k not in ("GITHUB_OUTPUT", "QUANTLOOP_FAKE_DATA")}
    env.update({"QUANTLOOP_ROOT": str(code / "unused"), "PYTHONDONTWRITEBYTECODE": "1"})
    script = ("import sys, pathlib, hourly_driver\n"
              "import bot.backtest, bot.shadow, bot.strategy, bot.risk, bot.paper\n"
              f"said, files, before, after, touched = hourly_driver.drive(pathlib.Path({str(code / 'root')!r}), bait=True)\n"
              "assert 'bot.wide' not in sys.modules and before == after and len([k for k in before if not k.endswith('/')]) == 24\n"
              "assert 'bot.bench' not in sys.modules and before['state/bench/H9.json'] == hourly_driver.BENCH_FILES['H9.json']\n"
              "assert touched == [], ('the loop read the wide data or the bench', touched)\n"
              "print('ok', len(said), len(files) > 10)\n")
    return subprocess.run([sys.executable, "-c", script], cwd=code, env=env, capture_output=True, text=True)


def test_the_hourly_loop_runs_where_the_collector_cannot_even_be_imported(tmp_path):
    """Wherever an import of the collector sat in the hourly loop, at the top of a module or inside a
    function that runs, a slip in the collector could stop the hourly run. Three hours of the loop, with
    bot/wide.py made unimportable and a full state/wide beside it, must go through, and must not open
    one file of the collector's on the way."""
    r = loop_in_a_copy(tmp_path, "as_it_is")
    assert r.returncode == 0 and r.stdout.strip().splitlines()[-1] == "ok 9 True", (r.stdout[-300:], r.stderr[-600:])
    # and the check itself bites: the same run fails the moment something in the loop does import it,
    # here from a corner of the hour that is easy to leave out, the history backfill
    backfill = "    target = int(rcfg.get(\"history_target_hours\", 0))\n    if not target:\n        return\n"
    r = loop_in_a_copy(tmp_path, "imports", [("run.py", backfill, backfill + "    from . import wide  # noqa: F401\n")])
    assert r.returncode != 0 and "the collector must not be imported by the hourly loop" in r.stderr


def test_the_watch_on_the_loop_sees_one_read_in_one_hour(tmp_path, hourly, monkeypatch):
    """The watch must not pass because it looked away. A step of the loop is made to read one file of the
    collector's and throw the reading away: the report's own main (which the workflow runs, and a drive of
    `build` alone would miss), and the slots in the first hour of a UTC day only, the third of the three."""
    real_main, real_describe = report.main, slot.describe

    def main_that_peeks():
        json.loads((config.STATE / "wide" / "universe.json").read_text())
        return real_main()

    def describe_that_peeks(now=None):
        if now and int(now) % 86400 < 3600:
            (config.STATE / "wide" / "status.json").read_text()
        return real_describe(now)
    monkeypatch.setattr(report, "main", main_that_peeks)
    said, _, before, after, touched = hourly.drive(tmp_path / "report", bait=True)
    assert touched == ["open state/wide/universe.json"] * 3 and before == after and len(said) == 9
    monkeypatch.setattr(report, "main", real_main)
    monkeypatch.setattr(slot, "describe", describe_that_peeks)
    said, _, before, after, touched = hourly.drive(tmp_path / "slots", bait=True)
    assert touched == ["open state/wide/status.json"] and before == after and len(said) == 9
