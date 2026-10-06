"""Wide market data for research. PROTECTED.

A collector that runs once a day on its own workflow (.github/workflows/wide.yml),
apart from the hourly loop and never read by it. It exists to answer one
question on real data before any machinery is built around the answer: is
there anything in the many coins beyond the ten the bot trades?

What it writes, all under state/wide/:

  universe.json        every pair that has ever been among the most traded USD
                       pairs on Kraken on a day this ran, with the day it joined.
                       A pair that has joined is kept, also after it falls down
                       the ranking or is taken off the venue, so from the day
                       after a coin joined a study on this list is not a study
                       of the coins that did well. Candles from before that day
                       are a survivor's past (state/README.md).
  daily/<COIN>.csv     daily candles, one row per closed UTC day. Kraken serves
                       the newest 720 days; older days come from Coinbase where
                       it lists the coin and its prices agree with Kraken's on
                       the days both have (the `source` column says which).
  quotes/<YEAR>.csv    one reading a day of every listed pair's best bid and
                       ask and its 24 hour volume: what a coin costs to trade.
  funding/<SYMBOL>.csv funding of Kraken's perpetual futures, summed by UTC day.
                       On 2026-10-06 Kraken's public feed went back to October
                       2025 and no further, and nothing says how long it keeps
                       what it has, so it is logged from now on.
  status.json          what the last run did, what failed, and whether GitHub's
                       runners can reach Binance's public market data (the venue
                       the cost model assumes; its main API refuses US addresses).

Nothing here places an order, needs a key, or touches an account.

What a failure costs. The run stops, red, with nothing committed, when Kraken's
list or its ticker cannot be read, when the list file is damaged, when the
list is empty and no coin qualifies for it, when a large part of the list has
gone from Kraken's answer since the last run (a cut off answer), or when most
pairs fail. Anything smaller is named in status.json and the run goes on: a
pair whose candles could not be read or whose file is damaged, a quotes file
that cannot be added to, many listed coins with no bid and ask, a day on which
no coin qualified, funding, the older history, the probes. Each part has its
own allowance of time, so a venue that hangs costs that part and not the run.
`python -m bot.wide` prints the last run. Every line about something that went
wrong begins with the word FAILED, a last run that is old (or no run at all)
with STALE, a slip in the settings with SETTING NOT USED. Nobody is told any
other way, so the agent's daily note passes those lines on (CLAUDE.md).

`python -m bot.wide` only reads. Collecting takes `--collect`, which is the
workflow's business: it writes state/, and a pull request that carries a
change to state/ is refused by the gate. The schedule asks twice a day because
GitHub drops scheduled runs; the second ask finds the day done and does
nothing (`--collect --again` collects regardless).
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

from . import config

KRAKEN = "https://api.kraken.com/0/public"
KRAKEN_FUTURES = "https://futures.kraken.com/derivatives/api/v3"
COINBASE = "https://api.exchange.coinbase.com"
PROBES = {
    # Binance's market data only host, and its static archive. Read, never traded on.
    "binance_data_api": ("https://data-api.binance.vision/api/v3/klines", {"symbol": "BTCUSDT", "interval": "1d", "limit": 3}),
    "binance_archive": ("https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1d/BTCUSDT-1d-2026-08.zip.CHECKSUM", None),
}
DAY = 86400
FIRST_DAY = 1230940800                   # 2009-01-03, the day of bitcoin's first block: no candle is older
KRAKEN_DAILY = 1440                      # minutes: Kraken's daily candle
COINBASE_PAGE = 300                      # candles per request, the endpoint's maximum
KRAKEN_TO_COMMON = {"XBT": "BTC", "XDG": "DOGE"}
USD_QUOTES = ("ZUSD", "USD")
DAILY_COLUMNS = ["time", "open", "high", "low", "close", "vwap", "volume", "count", "source"]
QUOTE_COLUMNS = ["time", "pair", "bid", "ask", "last", "volume_24h", "vwap_24h", "trades_24h",
                 "usd_volume_24h", "half_spread_bps", "rank"]
FUNDING_COLUMNS = ["time", "hours", "relative_sum", "absolute_sum"]
COIN_NAME = re.compile(r"[A-Z0-9]{1,15}")
# names a Windows checkout cannot hold as files; a coin called one of these is left out
NOT_A_FILE_NAME = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
# The schedule asks at 00:40 and 12:40 UTC and the agent reads at 22:00. A day on which both asks failed is
# then 33 hours or more from the last good run, and a good day at most 22: thirty hours tells the two apart.
STALE_AFTER_S = 30 * 3600
SYMBOL_NAME = re.compile(r"[A-Z0-9_]{3,30}")
SETTINGS_FILE = "wide.yaml"
DEFAULTS = {
    "top_n": 100,
    "funding_top_n": 30,
    "history_days": 1825,
    "deepen_budget_s": 240,
    "min_usd_volume": 50000,
    "exclude": ["USDT", "USDC", "DAI", "PYUSD", "TUSD", "USDD", "USDE", "USDS", "FDUSD", "RLUSD", "USDG", "USD1",
                "USDQ", "USDR", "GUSD", "BUSD", "EURT", "EURC", "EURR", "EURQ", "EUR", "GBP", "AUD", "CAD", "CHF",
                "JPY", "AED", "PAXG", "XAUT", "WBTC", "TBTC", "CBETH", "STETH", "WSTETH", "MSOL", "JITOSOL"],
}
# A coin whose last price is within 3% of one dollar and whose whole day's range is inside 2% is
# taken for a dollar token, whatever it is called, and does not join the list that day.
PEG_BAND, PEG_RANGE = 0.03, 0.02
# Coinbase's older candles are taken only when the two venues agree on the days both have.
OVERLAP_DAYS, MIN_OVERLAP, MAX_MEDIAN_GAP, MAX_P90_GAP = 30, 10, 0.01, 0.05
RETRY_DEEPEN_DAYS = 90
# A first "no such product" or "no candles" from Coinbase is not yet believed: on one bad day there every coin
# gets that answer. It is asked once more on a later run, the next day's and not one minutes after.
ONCE_MORE = "to be asked once more"
ASK_AGAIN_AFTER_S = 20 * 3600
# Time each part of a run may take, so that a venue that hangs costs its own part and never the whole
# run: GitHub cancels the job at its time limit (wide.yml), and a cancelled job commits nothing. The older
# history has its allowance in configs/wide.yaml (`deepen_budget_s`). The candles get twelve minutes, or
# two and a half seconds for each pair on a long list, so that a healthy run is never cut short.
CANDLES_BUDGET_S = 12 * 60
CANDLES_S_PER_PAIR = 2.5
MOST_PAIRS = 700                         # more US dollar pairs than Kraken lists; the job's limit is sized for a list this long
FUNDING_BUDGET_S = 120
DEEPEN_BUDGET_MAX_S = 600                # the most `deepen_budget_s` may be set to
EXTRA = {"tries": 2, "timeout": 15.0}    # funding, older history: asked less patiently than the candles
# More than this share of the coins on the list gone from Kraken's answer since a run in the last week,
# or with no bid and ask, is not the venue changing: it is an answer that was cut off.
BAD_ANSWER_SHARE = 0.25


class WideError(RuntimeError):
    pass


def _now() -> int:
    return int(time.time())


def _sleep(seconds: float) -> None:
    time.sleep(seconds)


def _clock() -> float:
    return time.monotonic()


# --- paths ---------------------------------------------------------------------

def root() -> Path:
    return config.STATE / "wide"


def daily_path(coin: str) -> Path:
    return root() / "daily" / f"{coin}.csv"


def funding_path(symbol: str) -> Path:
    return root() / "funding" / f"{symbol}.csv"


def quotes_path(year: int) -> Path:
    return root() / "quotes" / f"{year}.csv"


def _day(ts: int) -> str:
    return datetime.fromtimestamp(int(ts), timezone.utc).strftime("%Y-%m-%d")


# --- settings ------------------------------------------------------------------

def _usable(key: str, value) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        size = float(value)
    except OverflowError:                        # a whole number of hundreds of digits is not a number of anything
        return False
    if size != size or size in (float("inf"), float("-inf")) or value < 0:
        return False
    if key in ("top_n", "funding_top_n", "history_days") and size != int(value):
        return False
    if key == "deepen_budget_s" and value > DEEPEN_BUDGET_MAX_S:
        return False                             # the job's time limit is sized for no more than this
    return not (key in ("top_n", "history_days") and value < 1)


def settings() -> tuple[dict, list[str]]:
    """configs/wide.yaml over the defaults. A line that is missing or cannot be
    used falls back to the default written here and is named in the notes, so
    a slip in the file never stops the collector and never goes unsaid."""
    notes: list[str] = []
    name = f"configs/{SETTINGS_FILE}"
    path = config.CONFIGS / SETTINGS_FILE
    raw: dict = {}
    readable = False
    if not path.exists():
        notes.append(f"{name} is missing; the defaults are used")
    else:
        try:
            loaded = config.load_yaml(path)
        except Exception as e:  # noqa: BLE001
            notes.append(f"{name} cannot be read ({type(e).__name__}); the defaults are used")
        else:
            if isinstance(loaded, dict):
                raw, readable = loaded, True
            else:
                notes.append(f"{name} is not a list of settings; the defaults are used")
    out = {k: (list(v) if isinstance(v, list) else v) for k, v in DEFAULTS.items()}
    for key, default in DEFAULTS.items():
        shown = "the default list" if key == "exclude" else repr(default)
        if key not in raw:
            if readable:
                notes.append(f"`{key}` is not in {name}; {shown} is used")
            continue
        value = raw[key]
        if key == "exclude":
            if isinstance(value, list) and all(isinstance(v, str) for v in value):
                out[key] = [v.strip().upper() for v in value if v.strip()]
            else:
                notes.append(f"`exclude` in {name} is not a list of names; {shown} is used")
        elif _usable(key, value):
            out[key] = int(value) if float(value) == int(value) else float(value)
        else:
            notes.append(f"`{key}: {value!r}` in {name} cannot be used; {shown} is used")
    for key in raw:
        if key not in DEFAULTS:
            notes.append(f"`{key}` in {name} is not a setting this code reads")
    return out, notes


# --- http ----------------------------------------------------------------------

def fetch(url: str, params: dict | None = None, headers: dict | None = None, tries: int = 3,
          timeout: float = 20.0) -> tuple[int | None, object, str]:
    """One GET. Returns (http status or None, the parsed JSON or None, a note).
    Tried again only when the request could not be made, the server failed or
    it said to slow down; an answer of 'no such thing' is returned at once."""
    note = ""
    for attempt in range(tries):
        try:
            r = requests.get(url, params=params, headers=headers or {"User-Agent": "quantloop/1.0"}, timeout=timeout)
        except Exception as e:  # noqa: BLE001
            note = f"{type(e).__name__}: {e}"[:200]
            _sleep(2.0 * (attempt + 1))
            continue
        if r.status_code == 429 or r.status_code >= 500:
            note = f"http {r.status_code}"
            _sleep(3.0 * (attempt + 1))
            continue
        try:
            body = r.json()
        except Exception:  # noqa: BLE001
            body = None
        return r.status_code, body, ("" if body is not None else f"not JSON, {len(r.content)} bytes")
    return None, None, note or "no answer"


def kraken(path: str, params: dict | None = None, pause: float = 1.0) -> dict:
    """Kraken's public API. It answers 200 with an `error` list when it refuses.
    A second's pause after every answer, a refusal included: Kraken's own word
    is that public calls at one a second or fewer stay inside its limits, and
    nobody is waiting."""
    last = ""
    for attempt in range(3):
        status, body, note = fetch(f"{KRAKEN}/{path}", params)
        if status == 200 and isinstance(body, dict):
            errors = body.get("error") or []
            if not errors and isinstance(body.get("result"), dict):
                _sleep(pause)
                return body["result"]
            last = "; ".join(str(e) for e in errors) or "no result"
            if any("limit" in str(e).lower() or "too many" in str(e).lower() for e in errors):
                _sleep(6.0 * (attempt + 1))
                continue
            break
        last = note or f"http {status}"
        break
    _sleep(pause)
    raise WideError(f"kraken {path}: {last}")


# --- the list ------------------------------------------------------------------

def coin_name(wsname: str | None, altname: str | None) -> str | None:
    """The common name of a pair's base coin: BTC for Kraken's XBT, DOGE for XDG."""
    base = None
    if isinstance(wsname, str) and "/" in wsname:
        base = wsname.split("/", 1)[0]
    elif isinstance(altname, str) and altname.endswith("USD"):
        base = altname[:-3]
    if not base:
        return None
    base = KRAKEN_TO_COMMON.get(base.upper(), base.upper())
    return base if COIN_NAME.fullmatch(base) and base not in NOT_A_FILE_NAME else None


def usd_pairs(asset_pairs: dict, exclude: list[str]) -> dict[str, dict]:
    """Kraken's tradable pairs quoted in US dollars, by the common name of the coin."""
    out: dict[str, dict] = {}
    skip = {e.upper() for e in exclude}
    for key, info in asset_pairs.items():
        if not isinstance(info, dict) or info.get("quote") not in USD_QUOTES:
            continue
        if info.get("aclass_base", "currency") != "currency":
            continue                                    # tokenised shares are not coins
        if str(info.get("status", "online")) not in ("online", "post_only", "limit_only", "reduce_only", "cancel_only"):
            continue
        coin = coin_name(info.get("wsname"), info.get("altname"))
        if not coin or coin in skip:
            continue
        altname = info.get("altname") or key
        if coin in out and len(str(key)) >= len(str(out[coin]["kraken"])):
            continue                                    # two pairs for one coin: keep the plainer name
        out[coin] = {"kraken": str(key), "altname": str(altname), "wsname": info.get("wsname")}
    return out


def ticker_all(pairs: dict[str, dict], batch: int = 20) -> dict:
    """Kraken's ticker for every pair: one call when it will give them all, else a batch at a time."""
    try:
        return kraken("Ticker")
    except WideError as e:
        print(f"[wide] the ticker for every pair at once was refused ({e}); asking {batch} pairs at a time")
    out: dict = {}
    names = sorted(info["altname"] for info in pairs.values())
    for i in range(0, len(names), batch):
        out.update(kraken("Ticker", {"pair": ",".join(names[i:i + batch])}))
    return out


def _f(x) -> float:
    try:
        v = float(x)
        return v if v == v else 0.0
    except (TypeError, ValueError):
        return 0.0


def read_ticker(pairs: dict[str, dict], ticker: dict) -> list[dict]:
    """One row a coin from Kraken's ticker, most traded first. A coin with no
    usable quote (no entry, a zero bid, a crossed book) has no row."""
    rows = []
    for coin, info in pairs.items():
        t = ticker.get(info["kraken"]) or ticker.get(info["altname"])
        if not isinstance(t, dict):
            continue
        try:
            bid, ask, last = _f(t["b"][0]), _f(t["a"][0]), _f(t["c"][0])
            volume, vwap, trades = _f(t["v"][1]), _f(t["p"][1]), _f(t["t"][1])
            low, high = _f(t["l"][1]), _f(t["h"][1])
        except (KeyError, IndexError, TypeError):
            continue
        if not (bid > 0 and ask >= bid):
            continue
        mid = (bid + ask) / 2
        price = vwap if vwap > 0 else (last if last > 0 else mid)
        pegged = last > 0 and abs(last - 1.0) <= PEG_BAND and (high - low) <= PEG_RANGE * last
        rows.append({"pair": coin, "bid": bid, "ask": ask, "last": last, "volume_24h": volume, "vwap_24h": vwap,
                     "trades_24h": int(trades), "usd_volume_24h": round(volume * price, 2),
                     "half_spread_bps": round((ask - bid) / 2 / mid * 1e4, 2), "pegged": bool(pegged)})
    rows.sort(key=lambda r: (-r["usd_volume_24h"], r["pair"]))
    for i, r in enumerate(rows, start=1):
        r["rank"] = i
    return rows


def load_universe() -> dict:
    p = root() / "universe.json"
    if not p.exists():
        return {"pairs": {}}
    try:
        u = json.loads(p.read_text())
    except Exception as e:  # noqa: BLE001
        # the list is the record of which coins were watched from when; never start it again over a damaged one
        raise WideError(f"state/wide/universe.json cannot be read ({type(e).__name__}); mend or remove it") from e
    if not isinstance(u, dict) or not isinstance(u.get("pairs"), dict) \
            or not all(isinstance(m, dict) for m in u["pairs"].values()):
        raise WideError("state/wide/universe.json is not a list of pairs; mend or remove it")
    return u


def qualifying(rows: list[dict], st: dict) -> list[dict]:
    """The coins that may join the list today, most traded first: not a dollar token, and traded enough."""
    return [r for r in rows if not r["pegged"] and r["usd_volume_24h"] >= st["min_usd_volume"]]


def missing_from_answer(universe: dict, pairs: dict[str, dict], st: dict, now: int) -> tuple[list[str], int]:
    """The coins that were listed at the last run and are not in Kraken's answer now, and how many
    were listed. Coins Fin has since named in `exclude` are not counted, and neither is anything when
    the last run is more than a week back: after a long pause many coins may really have gone."""
    members = universe.get("pairs", {})
    skip = {e.upper() for e in st["exclude"]}
    were = [c for c, m in members.items() if m.get("listed") and c not in skip]
    try:
        recent = 0 <= int(now) - int(universe.get("updated")) <= 7 * DAY
    except (TypeError, ValueError):
        recent = False
    return (sorted(c for c in were if c not in pairs) if recent else []), len(were)


def update_universe(universe: dict, pairs: dict[str, dict], rows: list[dict], st: dict, now: int) -> list[str]:
    """The day's most traded coins join the list; none leaves. Returns the names that joined."""
    today = _day(now)
    members = universe.setdefault("pairs", {})
    eligible = qualifying(rows, st)
    joined = []
    for r in eligible[: int(st["top_n"])]:
        if r["pair"] not in members:
            # `since` is the UTC day it joined; that day's candle began before the moment it joined
            # (`joined_at`), so a study that wants no hindsight starts a coin the day after `since`
            members[r["pair"]] = {"since": today, "joined_at": int(now)}
            joined.append(r["pair"])
    by_coin = {r["pair"]: r for r in rows}
    for coin, m in members.items():
        info = pairs.get(coin)
        if info:
            if m.get("listed") is False and m.get("unlisted_since"):
                # back after a time away: the stretch is kept, because a name that returns may not be the same coin
                m.setdefault("gaps", []).append([m["unlisted_since"], today])
            m.update({"kraken": info["kraken"], "altname": info["altname"], "listed": True, "last_seen": today})
            m.pop("unlisted_since", None)
        elif m.get("listed", True):
            m["listed"] = False
            m["unlisted_since"] = today
        r = by_coin.get(coin)
        if r:
            m["rank"], m["usd_volume_24h"] = r["rank"], r["usd_volume_24h"]
    universe["updated"] = int(now)
    return joined


def save_universe(universe: dict) -> None:
    root().mkdir(parents=True, exist_ok=True)
    (root() / "universe.json").write_text(json.dumps(universe, indent=1, sort_keys=True) + "\n")


# --- files ---------------------------------------------------------------------

def _read_csv(path: Path, columns: list[str]) -> pd.DataFrame:
    """One of this module's files. Every one of them has a `time` column, and a
    file that cannot be read whole is refused, never read in part."""
    if not path.exists():
        return pd.DataFrame(columns=columns)
    try:
        # round_trip: the default parser reads back one long number in seven a digit off, and a
        # file that is read and written again every day would have its old rows drift
        # only an empty cell is "no value": a coin called NA or NULL is a name, and stays one
        df = pd.read_csv(path, float_precision="round_trip", keep_default_na=False, na_values=[""],
                         dtype={"pair": str, "source": str})
    except Exception as e:  # noqa: BLE001
        raise WideError(f"{path.name} cannot be read ({type(e).__name__}); mend or remove it") from e
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise WideError(f"{path.name} has lost its header or a column ({', '.join(missing)}); mend or remove it")
    df = df[columns].copy()
    when = pd.to_numeric(df["time"], errors="coerce")
    if when.isna().any() or (when != when.round()).any():
        raise WideError(f"{path.name} has a row with no time; mend or remove it")
    df["time"] = when.astype("int64")
    return df


def load_daily(coin: str) -> pd.DataFrame:
    """A coin's daily candles, oldest first."""
    return _read_csv(daily_path(coin), DAILY_COLUMNS)


def merge_daily(coin: str, fresh: pd.DataFrame) -> int:
    """Add candles to a coin's file. Where a day is in both, Kraken's row stands
    over Coinbase's and a newer reading over an older. Returns the days added."""
    have = load_daily(coin)
    if not len(fresh):
        return 0
    both = pd.concat([have, fresh[DAILY_COLUMNS]], ignore_index=True) if len(have) else fresh[DAILY_COLUMNS].copy()
    both["_order"] = range(len(both))
    both["_venue"] = (both["source"] == "kraken").astype(int)
    both = both.sort_values(["time", "_venue", "_order"]).drop_duplicates("time", keep="last")
    both = both.drop(columns=["_order", "_venue"]).sort_values("time").reset_index(drop=True)
    both["time"] = both["time"].astype("int64")
    both["count"] = both["count"].astype("int64")
    added = len(both) - len(have)
    if added or not both.equals(have.reset_index(drop=True)):
        daily_path(coin).parent.mkdir(parents=True, exist_ok=True)
        both.to_csv(daily_path(coin), index=False)
    return int(added)


def kraken_daily(altname: str, now: int) -> pd.DataFrame:
    """The newest closed daily candles Kraken holds for a pair (720 at most)."""
    result = kraken("OHLC", {"pair": altname, "interval": KRAKEN_DAILY})
    keys = [k for k in result if k != "last"]
    if not keys:
        raise WideError(f"kraken OHLC {altname}: no pair in the answer")
    rows = result[keys[0]]
    df = pd.DataFrame(rows, columns=DAILY_COLUMNS[:8])
    for c in DAILY_COLUMNS[:8]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["time", "close"])
    df["time"] = df["time"].astype("int64")
    # a daily candle begins on a UTC midnight, between the first day there was a bitcoin and now
    df = df[(df["time"] % DAY == 0) & (df["close"] > 0) & (df["time"] >= FIRST_DAY) & (df["time"] <= int(now))]
    if len(rows) and not len(df):
        # an answer whose rows are not daily candles (times in another unit, say) must not pass for a day with nothing new
        raise WideError(f"kraken OHLC {altname}: {len(rows)} rows and none is a daily candle")
    df = df[df["time"] + DAY <= int(now)]                               # closed days only
    df["count"] = df["count"].fillna(0).astype("int64")
    df["source"] = "kraken"
    return df.reset_index(drop=True)


def candles_budget(listed: int) -> float:
    """Seconds the candles may take for a list of this many pairs."""
    return max(CANDLES_BUDGET_S, CANDLES_S_PER_PAIR * min(int(listed), MOST_PAIRS))


def collect_daily(universe: dict, now: int) -> tuple[int, int, list[str]]:
    """Returns (pairs read, days added, the pairs that failed with why)."""
    read = added = 0
    failed = []
    todo = [(coin, m) for coin, m in sorted(universe.get("pairs", {}).items()) if m.get("listed") and m.get("altname")]
    allowed = candles_budget(len(todo))
    began = _clock()
    for coin, m in todo:
        if _clock() - began > allowed:
            failed.append(f"{coin}: not asked, the time allowed for candles had run out")
            continue
        try:
            added += merge_daily(coin, kraken_daily(m["altname"], now))
            read += 1
        except Exception as e:  # noqa: BLE001 - one pair must not cost the rest
            failed.append(f"{coin}: {e}"[:160])
    return read, added, failed


def append_quotes(universe: dict, rows: list[dict], now: int) -> int:
    """One reading a UTC day for every coin on the list that Kraken quoted."""
    members = universe.get("pairs", {})
    path = quotes_path(datetime.fromtimestamp(now, timezone.utc).year)
    have = _read_csv(path, QUOTE_COLUMNS)
    today = int(now) // DAY * DAY
    done = set(have.loc[have["time"].astype("int64") >= today, "pair"]) if len(have) else set()
    out = [{**{k: r[k] for k in QUOTE_COLUMNS if k in r}, "time": int(now)} for r in rows
           if r["pair"] in members and r["pair"] not in done]
    if not out:
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(out)[QUOTE_COLUMNS].to_csv(path, mode="a", header=not path.exists(), index=False)
    return len(out)


# --- funding -------------------------------------------------------------------

def funding_readings(rates: list) -> pd.DataFrame:
    """Kraken's hourly funding readings as rows of (ts, rel, abs); one that cannot be read is left out."""
    rows = []
    for r in rates if isinstance(rates, list) else []:
        try:
            stamp = r["timestamp"]
            if not isinstance(stamp, str):
                continue                                 # Kraken writes the time out; a bare number would be read as 1970
            ts = int(pd.Timestamp(stamp).timestamp())
            rows.append((ts, float(r["relativeFundingRate"]), float(r["fundingRate"])))
        except Exception:  # noqa: BLE001 - a reading that cannot be parsed is not a reading
            continue
    # in time order whatever order the feed sends them: a sum of the same readings must come out the same
    df = pd.DataFrame(rows, columns=["ts", "rel", "abs"]).sort_values(["ts", "rel", "abs"]).drop_duplicates("ts")
    return df[(df["rel"] == df["rel"]) & (df["abs"] == df["abs"])].reset_index(drop=True)


def funding_by_day(rates: list, now: int) -> pd.DataFrame:
    """Hourly funding readings summed by UTC day, complete days only. A reading
    counts in the day its time stamp, the start of its hour, falls in.
    relative_sum is the share of a position's value a long paid a short over
    the day (negative: the short paid); absolute_sum is the same in dollars per
    contract."""
    df = funding_readings(rates)
    if not len(df):
        return pd.DataFrame(columns=FUNDING_COLUMNS)
    df["time"] = df["ts"] // DAY * DAY
    g = df.groupby("time").agg(hours=("ts", "count"), relative_sum=("rel", "sum"), absolute_sum=("abs", "sum")).reset_index()
    g = g[g["time"] + DAY <= int(now)]
    return g[FUNDING_COLUMNS].reset_index(drop=True)


def merge_funding(symbol: str, fresh: pd.DataFrame) -> int:
    """A day already on file gives way to a newer reading built from as many hours or more,
    never to one built from fewer (the feed's oldest day arrives with its first hours cut off)."""
    path = funding_path(symbol)
    have = _read_csv(path, FUNDING_COLUMNS)
    if not len(fresh):
        return 0
    both = pd.concat([have, fresh], ignore_index=True) if len(have) else fresh.copy()
    both["_order"] = range(len(both))
    both = both.sort_values(["time", "hours", "_order"]).drop_duplicates("time", keep="last").drop(columns="_order")
    both = both.sort_values("time").reset_index(drop=True)
    both["time"], both["hours"] = both["time"].astype("int64"), both["hours"].astype("int64")
    added = len(both) - len(have)
    if added or not both.equals(have.reset_index(drop=True)):
        path.parent.mkdir(parents=True, exist_ok=True)
        both.to_csv(path, index=False)
    return int(added)


def collect_funding(st: dict, now: int) -> dict:
    out = {"symbols": 0, "days_added": 0, "failed": []}
    if int(st["funding_top_n"]) == 0:
        return out                                       # switched off: the futures venue is not asked at all
    began = _clock()
    status, body, note = fetch(f"{KRAKEN_FUTURES}/tickers", **EXTRA)
    if status != 200 or not isinstance(body, dict) or not isinstance(body.get("tickers"), list):
        out["failed"].append(f"tickers: {note or 'http ' + str(status)}")
        return out
    perps = [t for t in body["tickers"] if isinstance(t, dict) and t.get("tag") == "perpetual"
             and isinstance(t.get("symbol"), str) and t["symbol"].upper().startswith("PF_") and not t.get("suspended")]
    if not perps:
        # the venue always has perpetuals: none in the answer means it is not in the shape this reads
        out["failed"].append(f"tickers: {len(body['tickers'])} tickers and no perpetual among them")
        return out
    perps.sort(key=lambda t: -_f(t.get("volumeQuote")))
    wanted = [t["symbol"].upper() for t in perps[: int(st["funding_top_n"])]]
    live = {t["symbol"].upper() for t in perps}
    folder = root() / "funding"
    kept = sorted(p.stem for p in folder.glob("*.csv")) if folder.exists() else []
    for symbol in dict.fromkeys(wanted + [s for s in kept if s in live]):     # the day's most traded, and any already logged
        if not SYMBOL_NAME.fullmatch(symbol):
            continue
        if _clock() - began > FUNDING_BUDGET_S:
            out["failed"].append(f"{symbol} and any after it: not asked, the time allowed for funding had run out")
            break
        status, body, note = fetch(f"{KRAKEN_FUTURES}/historical-funding-rates", {"symbol": symbol}, **EXTRA)
        if status != 200 or not isinstance(body, dict) or not isinstance(body.get("rates"), list):
            out["failed"].append(f"{symbol}: {note or 'http ' + str(status)}"[:160])
            continue
        try:
            if body["rates"] and not len(funding_readings(body["rates"])):
                # readings in a shape this cannot read must not pass for a symbol with nothing new
                raise WideError(f"{len(body['rates'])} readings and none could be read")
            out["days_added"] += merge_funding(symbol, funding_by_day(body["rates"], now))
            out["symbols"] += 1
        except Exception as e:  # noqa: BLE001
            out["failed"].append(f"{symbol}: {e}"[:160])
        _sleep(0.3)
    return out


# --- older history from Coinbase -----------------------------------------------

def coinbase_daily(coin: str, start: int, end: int) -> tuple[pd.DataFrame, str]:
    """Daily candles for <COIN>-USD between two times, oldest first, and a note
    ('' when it answered, 'not listed' when Coinbase has no such product)."""
    frames = []
    first = cursor = int(start) // DAY * DAY
    while cursor < end:
        page_end = min(cursor + COINBASE_PAGE * DAY, int(end))
        params = {"granularity": DAY, "start": datetime.fromtimestamp(cursor, timezone.utc).isoformat(),
                  "end": datetime.fromtimestamp(page_end, timezone.utc).isoformat()}
        status, body, note = fetch(f"{COINBASE}/products/{coin}-USD/candles", params, **EXTRA)
        if status == 404:
            return pd.DataFrame(columns=DAILY_COLUMNS), "not listed"
        if status != 200 or not isinstance(body, list):
            return pd.DataFrame(columns=DAILY_COLUMNS), note or f"http {status}"
        if body:
            # Coinbase order: [time, low, high, open, close, volume]
            frames.append(pd.DataFrame(body, columns=["time", "low", "high", "open", "close", "volume"]))
        cursor = page_end
        _sleep(0.15)
    if not frames:
        return pd.DataFrame(columns=DAILY_COLUMNS), ""
    df = pd.concat(frames, ignore_index=True)
    came = len(df)
    for c in ("time", "low", "high", "open", "close", "volume"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["time", "close"])
    df["time"] = df["time"].astype("int64")
    # a daily candle begins on a UTC midnight, no earlier than the first day there was a bitcoin, inside the days asked for
    df = df[(df["time"] % DAY == 0) & (df["close"] > 0) & (df["time"] >= max(FIRST_DAY, first)) & (df["time"] <= int(end))]
    df = df.drop_duplicates("time").sort_values("time")
    if not len(df):
        # as with Kraken's: rows that are not daily candles must not pass for a coin with no older history
        return pd.DataFrame(columns=DAILY_COLUMNS), f"{came} rows and none is a daily candle"
    df["vwap"] = (df["high"] + df["low"] + df["close"]) / 3
    df["count"] = 0
    df["source"] = "coinbase"
    return df[DAILY_COLUMNS].reset_index(drop=True), ""


def venues_agree(ours: pd.DataFrame, theirs: pd.DataFrame) -> tuple[bool, str]:
    """Do two venues' daily closes describe the same coin on the days both have?"""
    both = ours[["time", "close"]].merge(theirs[["time", "close"]], on="time", suffixes=("_a", "_b"))
    if len(both) < MIN_OVERLAP:
        return False, f"only {len(both)} days in common"
    gap = (both["close_b"] / both["close_a"] - 1).abs()
    median, p90 = float(gap.median()), float(gap.quantile(0.9))
    ok = median <= MAX_MEDIAN_GAP and p90 <= MAX_P90_GAP
    return ok, f"closes differ by {median:.2%} at the median and {p90:.2%} at the ninth decile over {len(both)} days"


def _believed(answer: str, before) -> str:
    """Coinbase's "no" for a coin, as it goes on file: the first time to be asked once more, and believed
    (for three months) when the same answer comes again."""
    again = isinstance(before, dict) and str(before.get("result", "")).startswith(answer)
    return answer if again else f"{answer}, {ONCE_MORE}"


def _asked_lately(mark, want_from: int, now: int) -> bool:
    """Was Coinbase asked for this coin's older days, back at least this far, within the last three months?
    A first "no" stands only until the next day's run."""
    try:
        if str(mark.get("result", "")).endswith(ONCE_MORE):
            return int(now) - int(mark["at"]) < ASK_AGAIN_AFTER_S
        return int(mark["want_from"]) <= want_from + RETRY_DEEPEN_DAYS * DAY and int(now) - int(mark["at"]) < RETRY_DEEPEN_DAYS * DAY
    except Exception:  # noqa: BLE001 - no mark, or one that cannot be read: ask
        return False


def deepen(universe: dict, st: dict, now: int) -> dict:
    """Reach back past Kraken's 720 days with Coinbase's candles, a coin at a
    time, until the time allowed for one run is used. Returns what was done."""
    out = {"coins": 0, "days_added": 0, "not_listed": 0, "mismatch": [], "failed": []}
    marks_path = root() / "deepen.json"
    try:
        marks = json.loads(marks_path.read_text()) if marks_path.exists() else {}
        if not isinstance(marks, dict):
            marks = {}
    except Exception:  # noqa: BLE001
        marks = {}
    want_from = (int(now) // DAY - int(st["history_days"])) * DAY
    began = _clock()
    changed = False
    for coin, m in sorted(universe.get("pairs", {}).items(), key=lambda kv: kv[1].get("rank", 10 ** 9)):
        if _clock() - began > float(st["deepen_budget_s"]):
            break
        try:
            have = load_daily(coin)
        except Exception as e:  # noqa: BLE001
            out["failed"].append(f"{coin}: {e}"[:160])
            continue
        ours = have[have["source"] == "kraken"]
        if len(ours) < MIN_OVERLAP:
            continue                                     # too new on Kraken to compare yet; not marked, so it is asked once it can be
        earliest = int(have["time"].min())
        if earliest - want_from < 30 * DAY:
            continue                                     # already about as deep as asked
        if _asked_lately(marks.get(coin), want_from, now):
            continue                                     # asked not long ago for the same stretch
        first_ours = int(ours["time"].min())
        mark = {"at": int(now), "want_from": int(want_from)}
        try:
            theirs, note = coinbase_daily(coin, want_from, first_ours + OVERLAP_DAYS * DAY)
            if note == "not listed":
                out["not_listed"] += 1
                mark["result"] = _believed("not listed", marks.get(coin))
            elif note:
                out["failed"].append(f"{coin}: coinbase {note}"[:160])
                continue                                 # a failed request is not an answer; ask again next run
            elif not len(theirs):
                mark["result"] = _believed("no candles", marks.get(coin))
            else:
                ok, why = venues_agree(ours, theirs)
                if not ok:
                    out["mismatch"].append(f"{coin}: {why}")
                    mark["result"] = f"not used: {why}"
                else:
                    older = theirs[theirs["time"] < earliest]
                    added = merge_daily(coin, older) if len(older) else 0
                    out["coins"] += 1
                    out["days_added"] += added
                    mark["result"] = f"added {added} days; {why}"
        except Exception as e:  # noqa: BLE001 - one coin's odd answer must not cost the coins after it
            out["failed"].append(f"{coin}: {type(e).__name__}: {e}"[:160])
            continue
        marks[coin] = mark
        changed = True
    if changed:
        root().mkdir(parents=True, exist_ok=True)
        marks_path.write_text(json.dumps(marks, indent=1, sort_keys=True) + "\n")
    return out


# --- other sources -------------------------------------------------------------

def probes() -> dict:
    """Can this machine read Binance's public market data? One small request each."""
    out = {}
    for name, (url, params) in PROBES.items():
        status, body, note = fetch(url, params, tries=1, timeout=15.0)
        ok = status == 200 and (body is not None or name == "binance_archive")
        out[name] = {"http": status, "ok": bool(ok), "note": "" if ok else (note or "refused")}
    return out


# --- the run -------------------------------------------------------------------

def collect(now: int | None = None) -> dict:
    now = int(now or _now())
    st, notes = settings()
    for n in notes:
        print(f"[wide] SETTING NOT USED: {n}")
    pairs = usd_pairs(kraken("AssetPairs"), st["exclude"])
    if not pairs:
        raise WideError("kraken AssetPairs: no pair quoted in US dollars in the answer")
    rows = read_ticker(pairs, ticker_all(pairs))
    if not rows:
        raise WideError("kraken Ticker: no usable quote for any US dollar pair")
    universe = load_universe()
    gone, were = missing_from_answer(universe, pairs, st, now)
    if len(gone) > max(5, BAD_ANSWER_SHARE * were):
        # coins leave the venue a few at a time; this many at once is an answer that was cut off, and taking
        # it at its word would mark them all as gone and skip their day
        raise WideError(f"kraken AssetPairs: {len(gone)} of the {were} coins on the list are not in the answer "
                        f"({', '.join(gone[:5])}{', ...' if len(gone) > 5 else ''}); taken for a cut off answer")
    joined = update_universe(universe, pairs, rows, st, now)
    members = universe["pairs"]
    if not members:
        # a green run that gathers nothing would look like a quiet day: say what is wrong instead
        raise WideError(f"none of the {len(rows)} coins quoted qualifies for the list; look at `top_n` and "
                        f"`min_usd_volume` in configs/{SETTINGS_FILE}")
    save_universe(universe)
    quotes_failed = ""
    try:
        quoted = append_quotes(universe, rows, now)
    except Exception as e:  # noqa: BLE001 - a quotes file that cannot be added to must not cost the candles
        quoted, quotes_failed = 0, f"{type(e).__name__}: {e}"[:200]
    read, days, failed = collect_daily(universe, now)
    listed = sum(1 for m in members.values() if m.get("listed"))
    most_failed = bool(listed) and len(failed) * 2 > listed
    quoted_today = {r["pair"] for r in rows}
    unquoted = sorted(c for c, m in members.items() if m.get("listed") and c not in quoted_today)
    status = {
        "ran": now, "ran_utc": datetime.fromtimestamp(now, timezone.utc).strftime("%Y-%m-%d %H:%MZ"),
        "ok": not most_failed,
        "settings_not_used": notes,
        "kraken": {"usd_pairs": len(pairs), "quoted": len(rows), "pegged_skipped": sorted(r["pair"] for r in rows if r["pegged"]),
                   "on_the_list": len(members), "listed": listed, "joined_today": joined,
                   "qualified_today": len(qualifying(rows, st)), "quotes_written": quoted,
                   "quotes_failed": quotes_failed, "unquoted": unquoted, "pairs_read": read, "days_added": days,
                   "failed": failed},
    }
    try:
        status["funding"] = collect_funding(st, now)
    except Exception as e:  # noqa: BLE001 - research extras never cost the candles
        status["funding"] = {"symbols": 0, "days_added": 0, "failed": [f"{type(e).__name__}: {e}"[:160]]}
    try:
        status["coinbase"] = deepen(universe, st, now)
    except Exception as e:  # noqa: BLE001
        status["coinbase"] = {"coins": 0, "days_added": 0, "failed": [f"{type(e).__name__}: {e}"[:160]]}
    try:
        status["probes"] = probes()
    except Exception as e:  # noqa: BLE001
        status["probes"] = {"error": f"{type(e).__name__}: {e}"[:160]}
    (root() / "status.json").write_text(json.dumps(status, indent=1, sort_keys=True) + "\n")
    if most_failed:
        raise WideError(f"{len(failed)} of {listed} pairs could not be read; first: {failed[0]}")
    return status


def ran_today(now: int | None = None) -> str | None:
    """When the list and the candles have already been collected this UTC day: the time of that run."""
    p = root() / "status.json"
    try:
        s = json.loads(p.read_text())
        if s.get("ok") is True and int(s["ran"]) // DAY == int(now or _now()) // DAY \
                and int(s["kraken"]["pairs_read"]) > 0:
            return str(s.get("ran_utc") or _day(s["ran"]))
    except Exception:  # noqa: BLE001 - no record, or one that cannot be read, is no run
        return None
    return None


NO_RUN = ("STALE: no run on record. That is as it should be until the first run after the collector is installed "
          "(00:40 or 12:40 UTC); after that it means no run has been able to commit")


def _flat(text) -> str:
    """On one line. Whatever a venue, a file or an error said goes into the report through this, so a
    line break inside it can never start a line of its own."""
    return " ".join(str(text).split())


def summary(now: int | None = None) -> str:
    """The last run in a few lines. A line about something that went wrong begins
    with FAILED, a slip in the settings with SETTING NOT USED, and a last run
    that is old, or no run at all, with STALE: three words to look for at the
    start of a line, and no other line begins with them. The settings are read
    as the file stands now, so a slip shows at once and goes when it is mended."""
    try:
        slips = [f"SETTING NOT USED: {n}" for n in settings()[1]]
    except Exception as e:  # noqa: BLE001 - the report must come out whatever the file holds
        slips = [f"SETTING NOT USED: configs/{SETTINGS_FILE} could not be read ({type(e).__name__}); the defaults are used"]
    p = root() / "status.json"
    if not p.exists():
        return "\n".join(_flat(ln) for ln in ["wide data", NO_RUN] + slips)
    try:
        s = json.loads(p.read_text())
        k, f, c, pr = s.get("kraken", {}), s.get("funding", {}), s.get("coinbase", {}), s.get("probes", {})
        lines = [f"wide data, run of {s.get('ran_utc', '?')}"]
        age = int(now or _now()) - int(s["ran"])
        if age > STALE_AFTER_S:
            lines.append(f"STALE: the last run is {age / DAY:.1f} days old; the collector has not run or has not been able to commit")
        if s.get("ok") is False:
            lines.append("FAILED: the run stopped because most pairs could not be read; nothing of it was committed")
        elif s.get("ok") is not True:
            lines.append("FAILED: status.json does not say that the run went through")
        lines += slips
        lines.append(f"- Kraken: {k.get('usd_pairs', 0)} US dollar pairs, {k.get('on_the_list', 0)} on the list "
                     f"({k.get('listed', 0)} still listed), {len(k.get('joined_today', []))} joined today; "
                     f"{k.get('pairs_read', 0)} read, {k.get('days_added', 0)} days of candles added, "
                     f"{k.get('quotes_written', 0)} bid and ask readings")
        if k.get("qualified_today") == 0:
            lines.append(f"FAILED: not one coin qualified for the list today, so none can join; look at `top_n` and "
                         f"`min_usd_volume` in configs/{SETTINGS_FILE}")
        if k.get("failed"):
            lines.append(f"FAILED: candles for {len(k['failed'])} of {k.get('listed', 0)} pairs: " + "; ".join(k["failed"][:5]))
        if k.get("quotes_failed"):
            lines.append(f"FAILED: the day's bid and ask readings were not written: {k['quotes_failed']}")
        unquoted = k.get("unquoted") or []
        if len(unquoted) > max(5, BAD_ANSWER_SHARE * int(k.get("listed", 0))):
            # a thin coin or two with no bid is ordinary; this many is a ticker that was cut off
            lines.append(f"FAILED: no bid and ask for {len(unquoted)} of {k.get('listed', 0)} listed coins "
                         f"({', '.join(unquoted[:5])}{', ...' if len(unquoted) > 5 else ''})")
        lines.append(f"- funding: {f.get('symbols', 0)} perpetuals, {f.get('days_added', 0)} days added")
        if f.get("failed"):
            lines.append(f"FAILED: funding for {len(f['failed'])}: " + "; ".join(f["failed"][:3]))
        lines.append(f"- older history from Coinbase: {c.get('coins', 0)} coins deepened by {c.get('days_added', 0)} days, "
                     f"{c.get('not_listed', 0)} not listed there"
                     + (f"; prices did not match for {len(c['mismatch'])} and theirs were not used: {'; '.join(c['mismatch'][:3])}"
                        if c.get("mismatch") else ""))
        if c.get("failed"):
            lines.append(f"FAILED: older history for {len(c['failed'])}: " + "; ".join(c["failed"][:3]))
        if isinstance(pr, dict) and pr.get("error"):
            lines.append(f"FAILED: the probes: {pr['error']}")
        for name, r in sorted(pr.items()) if isinstance(pr, dict) else []:
            if isinstance(r, dict):
                lines.append(f"- {name}: {'readable from here' if r.get('ok') else 'not readable from here'} "
                             f"(http {r.get('http')}{', ' + r['note'] if r.get('note') else ''})")
        return "\n".join(_flat(ln) for ln in lines)
    except Exception as e:  # noqa: BLE001
        return "\n".join(_flat(ln) for ln in ["wide data", f"FAILED: status.json cannot be read ({type(e).__name__})"] + slips)


# --- reading it back (for studies) ---------------------------------------------

def panel(column: str = "close", min_days: int = 0) -> pd.DataFrame:
    """Every coin on the list side by side: one row a UTC day, one column a coin."""
    out = {}
    folder = root() / "daily"
    for path in sorted(folder.glob("*.csv")) if folder.exists() else []:
        df = load_daily(path.stem)
        if len(df) >= min_days and column in df.columns:
            out[path.stem] = pd.Series(df[column].to_numpy(dtype=float), index=df["time"].to_numpy())
    frame = pd.DataFrame(out).sort_index()
    frame.index = pd.to_datetime(frame.index, unit="s", utc=True)
    return frame


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--collect" not in argv:
        print(summary())
        return 0
    done = ran_today()
    if done and "--again" not in argv:
        # the schedule asks twice a day because GitHub drops runs; the second ask has nothing to do
        print(f"[wide] already collected today (run of {done}); nothing to do")
        return 0
    try:
        collect()
    except WideError as e:
        print(f"[wide] stopped: {e}")
        return 1
    print(summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
