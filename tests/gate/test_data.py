"""PROTECTED. Candle caches, backfill and quotes."""
import pandas as pd
import pytest

from bot import config, data


@pytest.fixture
def caches(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "STATE", tmp_path)
    monkeypatch.setattr(config, "CANDLES", tmp_path / "candles")
    monkeypatch.setattr(config, "HISTORY", tmp_path / "history")
    return tmp_path


def test_quote_half_spread():
    q = data.Quote(bid=99.95, ask=100.05, last=100.0)
    assert q.mid == pytest.approx(100.0)
    assert q.half_spread_bps == pytest.approx(5.0)


def test_backfill_fills_only_before_the_earliest_live_candle(caches):
    pairs = ["BTC"]
    live = data.SyntheticSource(pairs, n=100, seed=1, start=1_700_000_000)
    data.update_candles(pairs, live)
    hist = data.SyntheticSource(pairs, n=1000, seed=2, start=1_700_000_000 - 1000 * 3600)
    added = data.backfill_if_short(pairs, target_hours=500, history_source=hist, now=1_700_000_000 + 100 * 3600)
    assert added["BTC"] > 0
    h = data.load_history("BTC")
    assert int(h["time"].max()) < 1_700_000_000                       # nothing overlapping the live cache
    assert int(h["time"].min()) >= 1_700_000_000 + 100 * 3600 - 500 * 3600
    merged = data.load_all_candles("BTC")
    assert merged["time"].is_monotonic_increasing and merged["time"].is_unique
    assert len(merged) == len(h) + 100
    # second call: within a day of target, so nothing more is fetched
    again = data.backfill_if_short(pairs, target_hours=500, history_source=hist, now=1_700_000_000 + 100 * 3600)
    assert again == {}


def test_live_rows_win_over_history_on_overlap(caches):
    data.config.HISTORY.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"time": [0, 3600], "open": [1, 1], "high": [1, 1], "low": [1, 1], "close": [1.0, 1.0],
                  "vwap": [1, 1], "volume": [1, 1], "count": [0, 0]}).to_csv(data.history_path("X"), index=False)
    data.save_candles("X", pd.DataFrame({"time": [3600, 7200], "open": [2, 2], "high": [2, 2], "low": [2, 2],
                                         "close": [2.0, 2.0], "vwap": [2, 2], "volume": [1, 1], "count": [1, 1]}))
    merged = data.load_all_candles("X")
    assert list(merged["time"]) == [0, 3600, 7200]
    assert float(merged.loc[merged["time"] == 3600, "close"].iloc[0]) == 2.0


def test_kraken_pair_names():
    assert data.kraken_pair("BTC") == "XBTUSD"
    assert data.kraken_pair("DOGE") == "XDGUSD"
    assert data.kraken_pair("XRP") == "XRPUSD"


def test_history_and_live_merge_into_one_series(caches):
    """What the hourly loop and the backtest both read. Before 2026-09-21 the
    loop read the live cache only, so a 1440 hour lookback could never fire
    live (tests/gate/test_replay.py checks the loop itself, through its entry point)."""
    pairs = ["BTC"]
    live = data.SyntheticSource(pairs, n=100, seed=1, start=1_700_000_000)
    data.update_candles(pairs, live)
    hist = data.SyntheticSource(pairs, n=3000, seed=2, start=1_700_000_000 - 3000 * 3600)
    data.backfill_if_short(pairs, target_hours=2500, history_source=hist, now=1_700_000_000 + 100 * 3600)
    merged = data.load_all_candles("BTC")
    assert len(merged) >= 2500 and merged["time"].is_monotonic_increasing and merged["time"].is_unique
    assert int(merged["time"].iloc[-1]) == int(data.load_candles("BTC")["time"].max())   # ends at the latest live candle


def test_a_zero_or_crossed_quote_is_no_quote():
    class Source:
        def quote_for(self, pair):
            return {"BTC": data.Quote(bid=0.0, ask=0.0, last=0.0), "ETH": data.Quote(bid=101.0, ask=100.0, last=100.0),
                    "SOL": data.Quote(bid=19.99, ask=20.01, last=20.0)}[pair]
    assert list(data.quotes(["BTC", "ETH", "SOL"], Source())) == ["SOL"]


def test_the_backfill_stops_starting_pairs_when_its_time_is_up(caches, monkeypatch):
    pairs = ["BTC", "ETH", "SOL"]
    live = data.SyntheticSource(pairs, n=100, seed=1, start=1_700_000_000)
    data.update_candles(pairs, live)
    hist = data.SyntheticSource(pairs, n=3000, seed=2, start=1_700_000_000 - 3000 * 3600)
    clock = {"now": 0.0}
    monkeypatch.setattr(data.time, "monotonic", lambda: clock["now"])
    fetch = hist.candles

    def a_minute_each(pair, start, end):
        clock["now"] += 60.0
        return fetch(pair, start, end)
    monkeypatch.setattr(hist, "candles", a_minute_each)
    added = data.backfill_if_short(pairs, 2500, hist, now=1_700_000_000 + 100 * 3600, budget_s=100)
    assert list(added) == ["BTC", "ETH"]                        # SOL waits for the next run
    again = data.backfill_if_short(pairs, 2500, hist, now=1_700_000_000 + 100 * 3600, budget_s=100)
    assert list(again) == ["SOL"]                               # and gets it, without refetching the others


def test_backfill_asks_once_for_a_span_the_venue_does_not_have(caches):
    """A pair the venue listed late has no candles for the old part of a longer
    target. Ask once, remember, and do not ask again every hour."""
    pairs = ["BTC"]
    live = data.SyntheticSource(pairs, n=100, seed=1, start=1_700_000_000)
    data.update_candles(pairs, live)
    calls = []

    class Late:
        def candles(self, pair, start, end):
            calls.append((start, end))
            hist = data.SyntheticSource(pairs, n=200, seed=2, start=1_700_000_000 - 200 * 3600)
            return hist.candles(pair, start, end)                 # only the last 200 hours exist

    now = 1_700_000_000 + 100 * 3600
    assert data.backfill_if_short(pairs, 5000, Late(), now=now)["BTC"] == 200
    assert data.backfill_if_short(pairs, 5000, Late(), now=now + 3600) == {}
    assert len(calls) == 1
    # a longer target later is a new question, asked once
    data.backfill_if_short(pairs, 9000, Late(), now=now + 7200)
    data.backfill_if_short(pairs, 9000, Late(), now=now + 10800)
    assert len(calls) == 2
