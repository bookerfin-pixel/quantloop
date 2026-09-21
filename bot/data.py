"""Market data. PROTECTED.

Live: Kraken public OHLC and ticker (bid, ask), plus a growing local cache of
closed hourly candles at state/candles/<PAIR>.csv.

History: a one off backfill of older hourly candles at state/history/<PAIR>.csv
from Coinbase's public candles endpoint, written once and never touched by the
hourly loop, so the repo does not rewrite megabytes every hour. Backtests read
history plus live, merged on time, with live rows winning where they overlap.

Why two venues: Binance refuses US IP addresses and GitHub Actions runners
sit in the US. Kraken serves live data with no key; Coinbase serves deep
hourly history with no key. Costs are modelled on Binance fees regardless
(configs/risk.yaml). Prices across the two venues differ by a few basis
points at most for these pairs, which is far inside the modelled costs.

A synthetic source exists for tests and dry runs.
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import requests

from . import config

KRAKEN = "https://api.kraken.com/0/public"
KRAKEN_NAMES = {"BTC": "XBT", "DOGE": "XDG"}  # Kraken's own asset codes
COINBASE = "https://api.exchange.coinbase.com"
CANDLE_COLUMNS = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]
INTERVAL_MIN = 60
MAX_CACHE_ROWS = 24 * 366 * 2  # two years of hourly candles per pair
COINBASE_PAGE = 300            # candles per request, the endpoint's maximum


@dataclass
class Quote:
    bid: float
    ask: float
    last: float

    @property
    def mid(self) -> float:
        return (self.bid + self.ask) / 2

    @property
    def half_spread_bps(self) -> float:
        mid = self.mid
        return (self.ask - self.bid) / 2 / mid * 1e4 if mid > 0 else 0.0


def kraken_pair(pair: str, quote: str = "USD") -> str:
    return f"{KRAKEN_NAMES.get(pair, pair)}{quote}"


def _get_json(url: str, params: dict | None = None, retries: int = 3, headers: dict | None = None):
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, timeout=20, headers=headers or {})
            if r.status_code == 429:
                raise RuntimeError("rate limited")
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001 - retry anything transient
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"{url} failed after {retries} attempts: {last_err}")


def _kraken_get(path: str, params: dict) -> dict:
    body = _get_json(f"{KRAKEN}/{path}", params)
    if body.get("error"):
        raise RuntimeError(f"kraken {path} error: {body['error']}")
    return body["result"]


def _first_pair_key(result: dict) -> str:
    keys = [k for k in result if k != "last"]
    if not keys:
        raise RuntimeError("kraken returned no pair data")
    return keys[0]


class KrakenSource:
    def __init__(self, quote: str = "USD"):
        self.quote = quote

    def ohlc(self, pair: str, since: int | None = None) -> pd.DataFrame:
        params = {"pair": kraken_pair(pair, self.quote), "interval": INTERVAL_MIN}
        if since:
            params["since"] = int(since)
        result = _kraken_get("OHLC", params)
        rows = result[_first_pair_key(result)]
        df = pd.DataFrame(rows, columns=CANDLE_COLUMNS)
        for c in CANDLE_COLUMNS:
            df[c] = pd.to_numeric(df[c])
        df["time"] = df["time"].astype("int64")
        # The final row is the candle still forming. Only closed candles are usable.
        now = int(time.time())
        df = df[df["time"] + INTERVAL_MIN * 60 <= now]
        time.sleep(0.35)  # stay well inside Kraken's public rate limit
        return df.reset_index(drop=True)

    def quote_for(self, pair: str) -> Quote:
        result = _kraken_get("Ticker", {"pair": kraken_pair(pair, self.quote)})
        t = result[_first_pair_key(result)]
        time.sleep(0.35)
        return Quote(bid=float(t["b"][0]), ask=float(t["a"][0]), last=float(t["c"][0]))


class CoinbaseHistory:
    """Hourly candles from Coinbase Exchange, 300 per request, oldest first."""

    def __init__(self, quote: str = "USD"):
        self.quote = quote

    def candles(self, pair: str, start: int, end: int) -> pd.DataFrame:
        frames = []
        cursor = start
        while cursor < end:
            page_end = min(cursor + COINBASE_PAGE * 3600, end)
            params = {
                "granularity": 3600,
                "start": datetime.fromtimestamp(cursor, timezone.utc).isoformat(),
                "end": datetime.fromtimestamp(page_end, timezone.utc).isoformat(),
            }
            rows = _get_json(f"{COINBASE}/products/{pair}-{self.quote}/candles", params,
                             headers={"User-Agent": "quantloop/1.0"})
            if rows:
                # Coinbase order: [time, low, high, open, close, volume]
                df = pd.DataFrame(rows, columns=["time", "low", "high", "open", "close", "volume"])
                frames.append(df)
            cursor = page_end
            time.sleep(0.15)  # public limit is 10 requests a second
        if not frames:
            return pd.DataFrame(columns=CANDLE_COLUMNS)
        df = pd.concat(frames, ignore_index=True)
        df["time"] = df["time"].astype("int64")
        df["vwap"] = (df["high"] + df["low"] + df["close"]) / 3
        df["count"] = 0
        df = df[CANDLE_COLUMNS].drop_duplicates("time").sort_values("time")
        return df.reset_index(drop=True)


class SyntheticSource:
    """Geometric random walk with slow regime drift. Deterministic per seed so
    tests and dry runs are repeatable. Quotes are the last close with a spread.
    Doubles as a history source for backfill tests."""

    def __init__(self, pairs: list[str], n: int = 900, seed: int = 7, start: int | None = None,
                 spread_bps: float = 5.0):
        self.pairs = pairs
        self.n = n
        self.seed = seed
        self.start = start or (int(time.time()) // 3600 * 3600 - n * 3600)
        self.spread_bps = spread_bps
        self._frames = {p: self._make(i) for i, p in enumerate(pairs)}

    def _make(self, i: int) -> pd.DataFrame:
        rng = np.random.default_rng(self.seed + i)
        n = self.n
        drift = np.zeros(n)
        regime = 0.0
        for k in range(n):
            if k % 120 == 0:
                regime = rng.normal(0, 0.0006)
            drift[k] = regime
        rets = rng.normal(0, 0.006, n) + drift
        close = 100.0 * (1 + i) * np.exp(np.cumsum(rets))
        open_ = np.roll(close, 1)
        open_[0] = close[0]
        high = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, 0.002, n)))
        low = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, 0.002, n)))
        times = self.start + np.arange(n) * 3600
        return pd.DataFrame(
            {"time": times, "open": open_, "high": high, "low": low, "close": close,
             "vwap": (open_ + close) / 2, "volume": rng.uniform(10, 100, n), "count": 50}
        )

    def ohlc(self, pair: str, since: int | None = None) -> pd.DataFrame:
        df = self._frames[pair]
        if since:
            df = df[df["time"] > since]
        return df.reset_index(drop=True)

    def candles(self, pair: str, start: int, end: int) -> pd.DataFrame:
        df = self._frames[pair]
        return df[(df["time"] >= start) & (df["time"] < end)].reset_index(drop=True)

    def quote_for(self, pair: str) -> Quote:
        last = float(self._frames[pair]["close"].iloc[-1])
        half = self.spread_bps / 1e4
        return Quote(bid=last * (1 - half), ask=last * (1 + half), last=last)


def get_source(pairs: list[str], quote: str = "USD"):
    if os.environ.get("QUANTLOOP_FAKE_DATA"):
        return SyntheticSource(pairs, seed=int(os.environ.get("QUANTLOOP_FAKE_SEED", "7")))
    return KrakenSource(quote)


def get_history_source(pairs: list[str], quote: str = "USD"):
    if os.environ.get("QUANTLOOP_FAKE_DATA"):
        # a long synthetic past that ends where the live synthetic series begins
        live = get_source(pairs, quote)
        return SyntheticSource(pairs, n=int(os.environ.get("QUANTLOOP_FAKE_HISTORY_HOURS", "2000")),
                               seed=int(os.environ.get("QUANTLOOP_FAKE_SEED", "7")) + 100,
                               start=live.start - int(os.environ.get("QUANTLOOP_FAKE_HISTORY_HOURS", "2000")) * 3600)
    return CoinbaseHistory(quote)


# --- caches -------------------------------------------------------------------

def cache_path(pair: str):
    config.CANDLES.mkdir(parents=True, exist_ok=True)
    return config.CANDLES / f"{pair}.csv"


def history_path(pair: str):
    config.HISTORY.mkdir(parents=True, exist_ok=True)
    return config.HISTORY / f"{pair}.csv"


def _read(path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=CANDLE_COLUMNS)
    df = pd.read_csv(path)
    if not len(df):
        return pd.DataFrame(columns=CANDLE_COLUMNS)
    df["time"] = df["time"].astype("int64")
    return df


def load_candles(pair: str) -> pd.DataFrame:
    return _read(cache_path(pair))


def load_history(pair: str) -> pd.DataFrame:
    return _read(history_path(pair))


def load_all_candles(pair: str) -> pd.DataFrame:
    """History plus live, merged on time. Live rows win where they overlap."""
    hist, live = load_history(pair), load_candles(pair)
    if not len(hist):
        return live
    if not len(live):
        return hist
    merged = pd.concat([hist, live], ignore_index=True)
    merged = merged.drop_duplicates("time", keep="last").sort_values("time")
    return merged.reset_index(drop=True)


def strategy_frames(pairs: list[str], history_hours: int) -> dict[str, pd.DataFrame]:
    """What a strategy is shown each hour: the trailing history_hours of
    history plus live, per pair. The same merge the backtest replays, so a
    lookback that works in a backtest also works live."""
    out = {}
    for p in pairs:
        df = load_all_candles(p)
        out[p] = df.tail(history_hours).reset_index(drop=True)
    return out


def save_candles(pair: str, df: pd.DataFrame) -> None:
    df = df.drop_duplicates("time").sort_values("time").tail(MAX_CACHE_ROWS)
    df.to_csv(cache_path(pair), index=False)


def update_candles(pairs: list[str], source) -> dict[str, pd.DataFrame]:
    """Fetch new closed candles for every pair, merge into the live cache, and
    return the merged frames. A pair that fails to fetch keeps its cached data
    so one bad request does not stall the whole run."""
    out: dict[str, pd.DataFrame] = {}
    for pair in pairs:
        cached = load_candles(pair)
        since = int(cached["time"].max()) if len(cached) else None
        try:
            fresh = source.ohlc(pair, since=since)
        except Exception as e:  # noqa: BLE001
            print(f"[data] {pair}: fetch failed ({e}); using cached candles only")
            fresh = pd.DataFrame(columns=CANDLE_COLUMNS)
        merged = pd.concat([cached, fresh], ignore_index=True) if len(fresh) else cached
        merged = merged.drop_duplicates("time").sort_values("time").reset_index(drop=True)
        if len(merged):
            save_candles(pair, merged)
        out[pair] = merged
    return out


def backfill_if_short(pairs: list[str], target_hours: int, history_source, now: int | None = None) -> dict[str, int]:
    """Make sure history plus live covers about target_hours for every pair.
    Fetches only the span that is missing before the earliest candle we hold,
    so this is expensive once per pair and free afterwards. Returns rows added."""
    now = now or int(time.time())
    added: dict[str, int] = {}
    for pair in pairs:
        have = load_all_candles(pair)
        earliest = int(have["time"].min()) if len(have) else now
        want_from = (now // 3600) * 3600 - target_hours * 3600
        if earliest - want_from < 24 * 3600:   # within a day of the target: nothing to do
            continue
        try:
            fetched = history_source.candles(pair, want_from, earliest)
        except Exception as e:  # noqa: BLE001
            print(f"[data] {pair}: history backfill failed ({e}); backtests use what is cached")
            continue
        if not len(fetched):
            print(f"[data] {pair}: history source returned nothing for the missing span")
            continue
        fetched = fetched[fetched["time"] < earliest]
        hist = load_history(pair)
        merged = pd.concat([hist, fetched], ignore_index=True) if len(hist) else fetched
        merged = merged.drop_duplicates("time").sort_values("time").reset_index(drop=True)
        merged.to_csv(history_path(pair), index=False)
        added[pair] = int(len(fetched))
        print(f"[data] {pair}: backfilled {len(fetched)} hourly candles "
              f"({datetime.fromtimestamp(int(fetched['time'].min()), timezone.utc):%Y-%m-%d} to "
              f"{datetime.fromtimestamp(int(fetched['time'].max()), timezone.utc):%Y-%m-%d})")
    return added


def quotes(pairs: list[str], source) -> dict[str, Quote]:
    out = {}
    for pair in pairs:
        try:
            out[pair] = source.quote_for(pair)
        except Exception as e:  # noqa: BLE001
            print(f"[data] {pair}: quote failed ({e}); pair skipped this run")
    return out
