"""The bench on daily bars across many coins. PROTECTED.

bot/bench.py reads a config of the hourly engine on the ten pairs. This reads
a book that chooses among many coins, day by day, on the history that keeps
the dead coins (bot/binance.py): the question step 2b of the plan asks, which
is whether choosing among many coins holds anything once the coins that died
are counted. No account trades on it and no rule leans on it. All of it is in
sample: it can show that an idea has nothing, never that it has something.

The market (market()). Every coin's daily closes and returns from the Binance
history, the list of the most traded coins on each day as it began
(binance.listing), and a cost for each coin and day. A book for day t is
decided on closes up to day t-1 and on the list for day t, which is itself
judged on days up to t-1, and earns the coin's return from the close of t-1
to the close of t. A coin with no candle on day t-1, inside its life, cannot
be traded on day t: it keeps what it held, and bears whatever the price did
(a suspension). A coin whose candles have ended is sold at its last close
(it died, or was swapped for another).

Costs. Per side, a fee of FEE_BPS plus the larger of FLOOR_BPS and the coin's
half spread plus IMPACT_BPS, the hourly engine's own model. Binance's
archive has no spreads, so the half spread is read off the dollars a coin
traded, by the line fitted to Kraken's daily quotes (SPREAD_FIT): a coin
that trades a million dollars a day has a half spread of about 3 bps there,
one that trades a hundred thousand about 9. For most coins the floor is what
counts. The reading is taken at double costs as well.

Two yardsticks, both before costs.
- Twins (as in bot/bench.py): the book's positions in each coin, as it last
  traded them, slid later in time over the days that coin could have been
  chosen (or was held), by a draw of their own for each coin, at least
  MIN_SLIDE_DAYS and stopping short of the lead (what the book's choices
  could have seen of the days they are slid over), and scored on what the
  coin made over the average of the coins that could be chosen that day, so
  that a twin holding more or less of the market than the book does on some
  day is not counted for or against it. The same coins held as long, at other
  times they could have been held: the share of its twins the book beats
  says whether it held each coin at better times than chance.
- Picks: on each day the book trades, as many coins as it holds drawn at
  random from the coins it could have chosen (the list's coins with the
  history its rule needs), at equal weight, held until its next trade.
  The share of such books it beats says whether it chose better than a
  random pick from the coins it could have chosen from, on the same days.
  This is the plainer question for a book that chooses among many.
For each, how often a book with no skill does as well: the chance, counted
over the separate twins or picks they are worth (bench.separate, bench.chance).

The checks a whole reading adds: each calendar year; double costs; nearby
settings; each half of the coins; every phase of a rhythm (a weekly
rebalance on each of the seven days); and four markets made from the history
with every day's direction tossed, one toss a day for every coin alike, where
the past says nothing of the day to come, so a book there has no skill: if a
yardstick finds some, it is finding skill where there is none (the null check).

The survivors' market (market(survivors=True)) is the same history with only
the SURVIVORS_TOP coins most traded as it ends, their whole past kept: what
the Kraken list is. A rule read on both shows how much of what it seemed to
have was the dead coins left out, in what it made (set against the list's
coins at equal weight) and in how it stood against its picks. A coin swapped
for another (MATIC for POL, say) ends where the swap was on both markets.

Beating random picks says a book chose well among the coins it could choose
from; it says nothing of whether choosing among them was worth doing. So a
whole reading sets what the book made, after costs, beside two plain books
on BTC alone (timed()): BTC held throughout, and BTC held only while it rose
over the TIMED_DAYS days before (the book's own filter length when it has
one), on the book's own rhythm and at the same costs. Each with its Sharpe
ratio and its worst fall, over the whole history and over its last
LAST_DAYS days alone. A book of many coins that does not beat the second of
those has found nothing a bot of one coin would not have.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import bench, binance

FEE_BPS = 10.0
FLOOR_BPS = 5.0
IMPACT_BPS = 2.0
SPREAD_FIT = (7.317, -0.446)    # log half spread in bps = a + b log dollars traded in 24 hours: Kraken's daily quotes,
                                # 6,341 readings of about 180 coins, 2026-10-07 to 2026-11-10 (state/wide/quotes)
MOST_SPREAD_BPS = 100.0
VOLUME_DAYS = 30                # the half spread goes by the median of dollars traded over this many days before
MIN_SLIDE_DAYS = bench.MIN_SLIDE_DAYS
MIN_ROOM_DAYS = bench.MIN_ROOM_DAYS
TWINS = 1000
PICKS = 1000
SEED = bench.SEED
NULL_MARKETS = bench.NULL_MARKETS
NULL_SEED = bench.NULL_SEED
LIST_MEMORY = binance.LIST_WINDOW + binance.LIST_MIN_DAYS    # what the list itself has seen of the days before
SURVIVORS_TOP = 100             # the survivors' market: this many coins, the most traded as the history ends
TIMED_COIN = "BTC"              # the plain books a whole reading sets a book beside
TIMED_DAYS = 30                 # BTC held only while it rose over this many days before (or the book's own filter)
LAST_DAYS = 1095                # the last three years, read on their own: the market has not been the same throughout


# --- the market --------------------------------------------------------------------

def half_spread_bps(dollars: np.ndarray) -> np.ndarray:
    a, b = SPREAD_FIT
    with np.errstate(divide="ignore", invalid="ignore"):
        hs = np.exp(a + b * np.log(np.maximum(dollars, 1.0)))
    return np.minimum(np.where(np.isfinite(hs), hs, MOST_SPREAD_BPS), MOST_SPREAD_BPS)


def cost_per_side(dollars: np.ndarray) -> np.ndarray:
    """What a fill costs, as a share of what is traded, for a coin that trades `dollars` a day."""
    return (FEE_BPS + np.maximum(FLOOR_BPS, half_spread_bps(dollars) + IMPACT_BPS)) / 1e4


def market(df: pd.DataFrame | None = None, survivors: bool = False, n_list: int = 100) -> dict:
    """What a book is run on, as arrays of one row a day and one column a coin: `close` (no value outside a
    coin's life, the last close carried over a suspension), `r` (the return from one close to the next;
    nothing outside a coin's life), `tradable` (a candle the day before with something traded in it),
    `gone` (its candles have ended), `cost` (a fill's cost per side), `listed` (binance.listing(n_list)).
    `days` and `coins` name them."""
    df = binance.load() if df is None else df
    df = df[df["close"] > 0]                              # a price of nothing is no candle (the collector keeps none)
    if survivors:
        top = binance.listing(SURVIVORS_TOP, df)
        alive = top.iloc[-1]
        df = df[df["coin"].isin(alive[alive].index)]
    close = binance.panel("close", df)
    r = binance.returns(df).reindex(index=close.index, columns=close.columns)
    qv = binance.panel("quote_volume", df).reindex(index=close.index, columns=close.columns)
    listed = binance.listing(n_list, df).reindex(index=close.index, columns=close.columns, fill_value=False)
    has = close.notna().to_numpy()
    dealt = has & (qv.fillna(0.0).to_numpy() > 0)        # a candle with something traded in it
    idx = np.arange(len(close))[:, None]
    first = np.where(has, idx, len(close)).min(axis=0)
    last = np.where(has, idx, -1).max(axis=0)
    life = (idx >= first) & (idx <= last)
    dollars = qv.fillna(0.0).rolling(VOLUME_DAYS, min_periods=1).median().shift(1).to_numpy()
    return {"days": close.index, "coins": list(close.columns), "first": first, "last": last,
            "close": close.ffill().where(life).to_numpy(), "r": np.nan_to_num(r.to_numpy(), nan=0.0),
            "tradable": np.vstack([np.zeros((1, has.shape[1]), dtype=bool), dealt[:-1]]) & life,
            "gone": idx > last, "life": life, "cost": cost_per_side(np.nan_to_num(dollars, nan=0.0)),
            "listed": listed.to_numpy(dtype=bool), "n_list": n_list}


def tossed(m: dict, seed: int) -> dict:
    """The same market with every day's direction tossed, one toss a day for every coin alike: each day's
    move from one close to the next kept in size, turned or not, and taken down by the log of its cosh, so
    that what a coin makes in a day is nothing on average (as bench.tossed does by the hour). The list and
    the costs stay as they were: they go by dollars traded, which no toss touches."""
    rng = np.random.default_rng(seed)
    sign = rng.choice([-1.0, 1.0], size=len(m["days"]))[:, None]
    with np.errstate(invalid="ignore", divide="ignore"):
        move = np.log1p(np.maximum(m["r"], -0.999999))
    step = np.where(m["life"], sign * move - np.log(np.cosh(move)), 0.0)
    r = np.where(m["life"], np.expm1(step), 0.0)
    level = np.exp(np.cumsum(step, axis=0))
    return dict(m, r=r, close=np.where(m["life"], level, np.nan))


def subset(m: dict, keep: np.ndarray) -> dict:
    """The market with only the coins in `keep` (a boolean mask over its coins)."""
    cols = np.flatnonzero(keep)
    out = {k: (v[:, cols] if isinstance(v, np.ndarray) and v.ndim == 2 else v) for k, v in m.items()}
    out.update(coins=[m["coins"][j] for j in cols], first=m["first"][cols], last=m["last"][cols])
    return out


# --- books -----------------------------------------------------------------------

def strongest(m: dict, n: int, lookback: int, every: int = 7, phase: int = 0,
              filter_days: int = 0) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """The n coins of the list with the highest return over the `lookback` days before, at equal weights,
    chosen again every `every` days (on the days whose number since the first is `phase` more than a
    multiple of `every`). With `filter_days`, it holds them only when the list's own coins at equal weight
    (listed_basket) made something over that many days before, and cash otherwise. Returns (targets,
    rebalance, eligible): the weights wanted on each rebalance day, which days those are, and the coins it
    could have chosen on each day. A coin needs a close `lookback` days before, inside its life, to be ranked."""
    close = m["close"]
    days, coins = close.shape
    past = np.full_like(close, np.nan)
    past[lookback + 1:] = close[: days - lookback - 1]          # the close lookback days before the day before
    before = np.vstack([np.full((1, coins), np.nan), close[:-1]])  # the close of the day before
    with np.errstate(invalid="ignore", divide="ignore"):
        score = before / past - 1.0
    eligible = m["listed"] & np.isfinite(score)
    score = np.where(eligible, score, -np.inf)
    rebalance = (np.arange(days) % every) == (phase % every)
    targets = np.zeros_like(close)
    top = np.argsort(-score, axis=1, kind="stable")[:, :n]
    rows = np.arange(days)[:, None]
    chosen = np.isfinite(score[rows, top])
    targets[rows, top] = np.where(chosen, 1.0 / n, 0.0)
    if filter_days:
        targets[~(trailing(listed_basket(m), filter_days) > 0)] = 0.0
    targets[~rebalance] = 0.0
    return targets, rebalance, eligible


def trailing(x: np.ndarray, days: int) -> np.ndarray:
    """For each day, what a daily return series made (in log) over the `days` days before it, up to the close
    of the day before: nothing of the day itself. No value until there are that many days behind it."""
    level = np.cumsum(np.log1p(np.maximum(x, -0.999999)))
    out = np.full(len(x), np.nan)
    out[days + 1:] = level[days:-1] - level[: len(x) - days - 1]
    return out


def timed(m: dict, coin: str = TIMED_COIN, days: int = TIMED_DAYS, every: int = 1, phase: int = 0) -> dict | None:
    """One coin held only while it rose over the `days` days before, cash otherwise, decided on the rhythm
    given and run like any book (costs, halts). None when the market does not have the coin."""
    if coin not in m["coins"]:
        return None
    j = m["coins"].index(coin)
    rebalance = (np.arange(len(m["days"])) % every) == (phase % every)
    targets = np.zeros_like(m["r"])
    targets[(trailing(m["r"][:, j], days) > 0) & rebalance, j] = 1.0
    return run(m, targets, rebalance)


def worst_fall(daily: np.ndarray) -> float:
    """The deepest fall from a high, of a book that earns `daily` each day."""
    value = np.cumprod(1.0 + np.asarray(daily, dtype=float))
    return float((value / np.maximum.accumulate(value) - 1.0).min()) if len(value) else 0.0


def run(m: dict, targets: np.ndarray, rebalance: np.ndarray) -> dict:
    """The book through the history. On a rebalance day it trades to its targets in the coins it can trade;
    a coin it cannot trade keeps what it held, and the rest is scaled to fit inside the book. A coin whose
    candles have ended is sold at its last close, on any day. Between trades positions move with their prices.
    Returns the weights held each day (`held`), the weights as last traded (`w`, what twins are made of),
    each day's return before costs (`gross`) and after them (`daily`), the costs as a share of the book, and
    what it held in coins it could not trade (`stuck_share`, the average share of the book, and
    `stuck_per_year`, what those days made: a result that rests on them rests on halts)."""
    days, coins = targets.shape
    held = np.zeros((days, coins))
    traded = np.zeros((days, coins))
    gross = np.zeros(days)
    paid = np.zeros(days)
    w = np.zeros(coins)
    last = np.zeros(coins)
    r, cost, can, gone = m["r"], m["cost"], m["tradable"], m["gone"]
    exit_cost = np.zeros(coins)
    caught_share = np.zeros(days)
    caught_made = np.zeros(days)
    for t in range(days):
        dead = gone[t] & (w > 0)
        if dead.any():                                   # sold at the last close, at what a fill there cost
            paid[t] += float((w[dead] * exit_cost[dead]).sum())
            w = np.where(dead, 0.0, w)
            last = np.where(gone[t], 0.0, last)
        if rebalance[t]:
            new = np.where(can[t], targets[t], w)
            stuck = float(new[~can[t]].sum())
            free = float(new[can[t]].sum())
            if free > max(0.0, 1.0 - stuck) + 1e-12:
                new = np.where(can[t], new * max(0.0, 1.0 - stuck) / free, new)
            paid[t] += float((np.abs(new - w) * np.where(can[t], cost[t], 0.0)).sum())
            last = np.where(can[t], new, last)
            w = new
        exit_cost = np.where(can[t], cost[t], exit_cost)
        held[t] = w
        traded[t] = last
        gross[t] = float(w @ r[t])
        caught = ~can[t] & ~gone[t]
        caught_share[t] = float(w[caught].sum())
        caught_made[t] = float(w[caught] @ r[t][caught])
        grown = w * (1.0 + r[t])
        w = grown / max(1.0 + gross[t], 1e-12)
    paid = np.minimum(paid, bench.MOST_COST)
    daily = gross - paid * (1.0 + gross)
    return {"held": held, "w": traded, "gross": gross, "daily": daily, "costs": paid,
            "own": (traded * r).sum(axis=1), "exposure": float(held.sum(axis=1).mean()),
            "stuck_share": float(caught_share.mean()), "stuck_per_year": bench.a_year(caught_made)}


# --- twins ---------------------------------------------------------------------------

def _longest_hold(w: np.ndarray) -> int:
    return bench._longest(w > 0)[0]


def lead_days(book: dict, memory: int) -> int:
    """How short of the whole way round a coin's slide stops: a twin slid by all but k days holds on each day
    the positions the book took k days later, chosen with that day in view for as long as the book's memory
    reaches (its lookback and the list's own), and then as long as it ever stayed in one coin (bench.lead)."""
    return int(memory) + max(int(memory), _longest_hold(book["w"]))


def pool_average(m: dict, eligible: np.ndarray) -> np.ndarray:
    """Each day's return of the coins a book could have chosen that day, at equal weights."""
    on = eligible & m["tradable"]
    count = on.sum(axis=1)
    return np.where(count > 0, (m["r"] * on).sum(axis=1) / np.maximum(count, 1), 0.0)


def twins(m: dict, book: dict, memory: int, n: int = TWINS, seed: int = SEED) -> dict | None:
    """The book against n twins: each coin's positions, as last traded, slid later over the days the coin
    could have been chosen or was held, by a draw of their own, from MIN_SLIDE_DAYS up to the lead short of
    the whole way round of those days. Book and twins are scored on what each coin made over the average of
    the coins that could be chosen that day. A coin with too few such days stays where it was in every twin
    (`in_place`). None when no coin the book held can be slid."""
    w = book["w"]
    x = m["r"] - pool_average(m, book["eligible"])[:, None]
    front, back = MIN_SLIDE_DAYS, lead_days(book, memory)
    least = front + back + MIN_ROOM_DAYS
    rng = np.random.default_rng(seed)
    held = np.flatnonzero(w.any(axis=0))
    theirs = np.zeros((n, len(x)))
    in_place, slid = [], 0
    for j in held:
        dom = np.flatnonzero((book["eligible"][:, j] | (w[:, j] > 0)) & m["life"][:, j])
        size = len(dom)
        if size < least:
            theirs[:, dom] += w[dom, j] * x[dom, j]
            in_place.append(m["coins"][j])
            continue
        k = rng.integers(front, size - back + 1, size=n)
        idx = (np.arange(size)[None, :] - k[:, None]) % size          # which of those days each twin's position is from
        theirs[:, dom] += w[dom, j][idx] * x[dom, j][None, :]
        slid += 1
    if not slid:
        return None
    return _ranked((w * x).sum(axis=1), theirs, m["days"], in_place=in_place)


def picks(m: dict, book: dict, rebalance: np.ndarray, n: int = PICKS, seed: int = SEED) -> dict | None:
    """The book against n books that, on each day it trades, hold as many coins as it does, drawn at random
    from the coins it could have chosen that day, at equal weights, until its next trade. A coin that dies
    is sold at its last close, as the book's are. Before costs. A pick does not carry a coin through a halt
    that spans one of the book's trades, where the book can be caught in one: `stuck_share` in the book's
    reading says how much that can matter. None when the book never held anything."""
    rng = np.random.default_rng(seed)
    days = np.flatnonzero(rebalance)
    count = (book["held"] > 0).sum(axis=1)
    theirs = np.zeros((n, len(m["r"])))
    ends = list(days[1:]) + [len(m["r"])]
    any_held = False
    for d, e in zip(days, ends):
        k = int(count[d])
        pool = np.flatnonzero(book["eligible"][d] & m["tradable"][d])
        if k == 0 or len(pool) == 0:
            continue
        any_held = True
        k = min(k, len(pool))
        size = float(book["held"][d].sum())                 # the book's own exposure that day
        growth = np.cumprod(1.0 + m["r"][d:e][:, pool], axis=0)          # each coin's value through the stretch
        start = np.vstack([np.ones((1, len(pool))), growth[:-1]])
        choice = np.argpartition(rng.random((n, len(pool))), k - 1, axis=1)[:, :k]   # k coins, none twice, per book
        value = growth[:, choice].mean(axis=2).T            # (n, days): what the coins held are worth at each close
        before = start[:, choice].mean(axis=2).T            # ... and at the close before
        # the book's own share of itself in coins that day, the rest in cash: a day's return on the whole
        theirs[:, d:e] = size * (value - before) / (1.0 - size + size * before)
    if not any_held:
        return None
    return _ranked(book["gross"], theirs, m["days"])


def day_numbers(days) -> np.ndarray:
    """Days as whole days since 1970-01-01, the form bench.spans takes, whatever the index's resolution."""
    idx = pd.DatetimeIndex(days)
    idx = idx.tz_convert("UTC") if idx.tz is not None else idx.tz_localize("UTC")
    return np.asarray((idx - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(days=1), dtype="int64")


def _ranked(own: np.ndarray, theirs: np.ndarray, days, in_place: list[str] | None = None) -> dict:
    """Where a book's daily returns stand among others': the share of them whose t of the daily gap to the
    average of them the book's is above, a tie counting as half, over the whole run, the last 365 days and
    each calendar year; how many separate books they are worth; the chance."""
    mean = theirs.mean(axis=0)
    beaten = {}
    for name, mask in bench.spans(day_numbers(days)).items():
        mine = bench._scores((own - mean)[mask])
        if mine is None:
            beaten[name] = None
            continue
        others = bench._scores(theirs[:, mask] - mean[mask])
        level = (others == mine[0]) | (np.abs(others - mine[0]) <= bench.EPS)
        beaten[name] = float(((others < mine[0]) & ~level).sum() + 0.5 * level.sum()) / len(others)
    worth = bench.separate(np.arange(len(theirs)), theirs - mean)
    return {"n": int(len(theirs)), "beaten": beaten, "mean": mean, "own": own, "worth": worth,
            "chance": bench.chance(beaten["all"], worth), "in_place": sorted(in_place or [])}


# --- a reading -----------------------------------------------------------------------

STRATEGIES = {"strongest": strongest}
NEARBY_SHARES = (0.75, 1.25)    # the lookback moved by a quarter either way, and n by one
LUCK_ABOVE = bench.LUCK_ABOVE
NO_SKILL_BELOW = bench.NO_TIMING_BELOW


def spec_name(spec: dict) -> str:
    rhythm = "daily" if int(spec.get("every", 7)) == 1 else f"every {spec['every']} days, phase {spec.get('phase', 0)}"
    held = f", held only while the list rose over the {spec['filter']} days before" if spec.get("filter") else ""
    return (f"{spec['strategy']} {spec['n']} of the top {spec['list']} by {spec['lookback']} day return, {rhythm}{held}")


def memory_of(spec: dict) -> int:
    """What a book's choices on a day can have seen of the days before it: its lookback and the list's own."""
    return max(int(spec["lookback"]) + 1, LIST_MEMORY)


def book_of(m: dict, spec: dict) -> tuple[dict, np.ndarray]:
    fn = STRATEGIES[spec["strategy"]]
    targets, rebalance, eligible = fn(m, n=int(spec["n"]), lookback=int(spec["lookback"]),
                                      every=int(spec.get("every", 7)), phase=int(spec.get("phase", 0)),
                                      filter_days=int(spec.get("filter", 0)))
    book = run(m, targets, rebalance)
    book["eligible"] = eligible
    return book, rebalance


def listed_basket(m: dict) -> np.ndarray:
    """Every coin of the list at equal weight, chosen again each day, before costs: the list's own market."""
    on = m["listed"] & m["tradable"]
    count = on.sum(axis=1)
    return np.where(count > 0, (m["r"] * on).sum(axis=1) / np.maximum(count, 1), 0.0)


def _plain(daily: np.ndarray) -> dict:
    """What a book that earns `daily` each day made, its Sharpe ratio and its worst fall."""
    return {"net": bench.compounded(daily), "sharpe": (bench.measure(daily) or {}).get("sharpe"), "worst": worst_fall(daily)}


def one(m: dict, spec: dict, n_twins: int = TWINS, n_picks: int = PICKS, seed: int = SEED,
        costs: float = 1.0, yardsticks: bool = False) -> dict:
    """One replay of a spec on one market, set against its twins and its picks; with `yardsticks`, beside
    BTC held and BTC timed (timed()) as well, over the whole history and over its last LAST_DAYS days."""
    book, rebalance = book_of(m, spec)
    if costs != 1.0:
        book = dict(book, costs=np.minimum(book["costs"] * costs, bench.MOST_COST))
        book["daily"] = book["gross"] - book["costs"] * (1.0 + book["gross"])
    tw = twins(m, book, memory_of(spec), n=n_twins, seed=seed) if n_twins else None
    pk = picks(m, book, rebalance, n=n_picks, seed=seed) if n_picks else None
    basket = listed_basket(m)
    btc = m["r"][:, m["coins"].index(TIMED_COIN)] if TIMED_COIN in m["coins"] else np.zeros(len(basket))
    out = {"days": int(len(book["gross"])), "net": bench.compounded(book["daily"]),
           "btc": bench.compounded(btc), "btc_per_year": bench.a_year(btc),
           "over_btc_per_year": bench.a_year(book["daily"] - btc), "over_btc_t": (bench.measure(book["daily"] - btc) or {}).get("t"),
           "basket": bench.compounded(basket), "exposure": book["exposure"],
           "net_per_year": bench.a_year(book["daily"]), "basket_per_year": bench.a_year(basket),
           "gross_per_year": bench.a_year(book["gross"]), "costs_per_year": bench.a_year(book["gross"] - book["daily"]),
           "stuck_share": book["stuck_share"], "stuck_per_year": book["stuck_per_year"],
           "twins": None, "picks": None, "against_btc": None}
    if yardsticks and TIMED_COIN in m["coins"]:
        f = int(spec.get("filter") or TIMED_DAYS)
        tb = timed(m, TIMED_COIN, f, every=int(spec.get("every", 7)), phase=int(spec.get("phase", 0)))
        if costs != 1.0:
            tb = dict(tb, daily=tb["gross"] - np.minimum(tb["costs"] * costs, bench.MOST_COST) * (1.0 + tb["gross"]))
        last = np.asarray(m["days"] >= m["days"][-1] - pd.Timedelta(days=LAST_DAYS))
        out["against_btc"] = {"timed_days": f, "book": _plain(book["daily"]), "held": _plain(btc),
                              "timed": _plain(tb["daily"]), "timed_exposure": tb["exposure"],
                              "last_days": int(last.sum()), "book_last": _plain(book["daily"][last]),
                              "held_last": _plain(btc[last]), "timed_last": _plain(tb["daily"][last])}
    if tw is not None:
        out["twins"] = {"n": tw["n"], "beaten": tw["beaten"]["all"], "beaten_last_365": tw["beaten"].get("last"),
                        "worth": tw["worth"], "chance": tw["chance"], "in_place": len(tw["in_place"]),
                        "timing_per_year": bench.a_year(tw["own"] - tw["mean"]),
                        "years": {k: v for k, v in tw["beaten"].items() if k not in ("all", "last")}}
    if pk is not None:
        left = book["daily"] - pk["mean"]
        m_left = bench.measure(left) or {"sharpe": None, "t": None}
        out["picks"] = {"n": pk["n"], "beaten": pk["beaten"]["all"], "beaten_last_365": pk["beaten"].get("last"),
                        "worth": pk["worth"], "chance": pk["chance"],
                        "choosing_per_year": bench.a_year(book["gross"] - pk["mean"]),
                        "left_per_year": bench.a_year(left), "left_t": m_left["t"],
                        "years": {k: v for k, v in pk["beaten"].items() if k not in ("all", "last")}}
    return out


def nearby(spec: dict) -> list[dict]:
    out = []
    for share in NEARBY_SHARES:
        lb = max(2, int(round(spec["lookback"] * share)))
        if lb != spec["lookback"]:
            out.append(dict(spec, lookback=lb))
    for dn in (-1, 1):
        if spec["n"] + dn >= 1:
            out.append(dict(spec, n=spec["n"] + dn))
    return out


def halves(m: dict, seed: int = SEED) -> list[np.ndarray]:
    """The coins in two halves, drawn once by a fixed seed."""
    rng = np.random.default_rng(seed)
    side = rng.random(len(m["coins"])) < 0.5
    return [side, ~side]


def whole(m: dict, spec: dict, n_twins: int = TWINS, n_picks: int = PICKS, sub: int = 200) -> dict:
    """A spec's whole reading on one market: its own replay against TWINS twins and PICKS picks, then, against
    `sub` of each, double costs, the settings nearby, each half of the coins, every phase of its rhythm and
    NULL_MARKETS markets with every day's direction tossed."""
    out = {"spec": dict(spec), "name": spec_name(spec), "own": one(m, spec, n_twins, n_picks, yardsticks=True)}
    out["double_costs"] = one(m, spec, 0, sub, costs=2.0)["picks"]
    out["nearby"] = [{"spec": s, **_short(one(m, s, sub, sub))} for s in nearby(spec)]
    out["halves"] = [_short(one(subset(m, keep), spec, sub, sub)) for keep in halves(m)]
    every = int(spec.get("every", 7))
    out["phases"] = [] if every == 1 else [
        {"phase": p, **_short(one(m, dict(spec, phase=p), sub, sub))} for p in range(every) if p != spec.get("phase", 0)]
    out["null"] = [{"seed": NULL_SEED + k, **_short(one(tossed(m, NULL_SEED + k), spec, sub, sub))}
                   for k in range(NULL_MARKETS)]
    return out


def _short(r: dict) -> dict:
    t, p = r.get("twins") or {}, r.get("picks") or {}
    return {"twins_beaten": t.get("beaten"), "twins_chance": t.get("chance"),
            "picks_beaten": p.get("beaten"), "picks_chance": p.get("chance"), "left_per_year": p.get("left_per_year")}


def _pct(x) -> str:
    return "?" if x is None else f"{x:.0%}"


def _signed(x) -> str:
    return "?" if x is None else f"{x:+.1%}"


def _num(x) -> str:
    return "?" if x is None else f"{x:.2f}"


def _plainly(p: dict) -> str:
    return f"{_signed(p['net'])} (Sharpe {_num(p['sharpe'])}, worst fall {_pct(p['worst'])})"


def words(rd: dict) -> list[str]:
    """A whole reading in plain lines."""
    o = rd["own"]
    t, p = o.get("twins") or {}, o.get("picks") or {}
    lines = [f"{rd['name']}: made {_signed(o['net'])} over {o['days']} days, where the list's coins at equal weight "
             f"made {_signed(o['basket'])} and BTC {_signed(o.get('btc'))} ({_signed(o['net_per_year'])} a year after "
             f"costs against {_signed(o['basket_per_year'])} and {_signed(o.get('btc_per_year'))}); average exposure "
             f"{o['exposure']:.2f}"]
    a = o.get("against_btc")
    if a:
        lines.append(f"  against BTC alone, at the same costs: this book {_plainly(a['book'])}; BTC held "
                     f"{_plainly(a['held'])}; BTC held only while it rose over the {a['timed_days']} days before, on the "
                     f"book's rhythm, {_plainly(a['timed'])}, in BTC {a['timed_exposure']:.0%} of the time")
        lines.append(f"  the last three years alone ({a['last_days']} days): this book {_plainly(a['book_last'])}; BTC held "
                     f"{_plainly(a['held_last'])}; BTC timed {_plainly(a['timed_last'])}")
    lines.append(f"  against random picks from the same list on the same days: beats {_pct(p.get('beaten'))} of them, "
                 f"and a book with no skill does as well {_pct(p.get('chance'))} of the time; choosing was worth "
                 f"{_signed(p.get('choosing_per_year'))} a year before costs, costs took {_pct(o['costs_per_year'])} a year, "
                 f"and {_signed(p.get('left_per_year'))} a year is left after them "
                 f"(t {'?' if p.get('left_t') is None else format(p['left_t'], '+.1f')}); "
                 f"at double costs {_signed((rd.get('double_costs') or {}).get('left_per_year'))}")
    lines.append(f"  against its twins (the same coins held as long at other times they could have been): beats "
                 f"{_pct(t.get('beaten'))}, chance {_pct(t.get('chance'))}; timing worth {_signed(t.get('timing_per_year'))} "
                 f"a year before costs" + (f"; {t['in_place']} of the coins it held had too few days to slide and are "
                                           f"in every twin as they are" if t.get("in_place") else ""))
    if o.get("stuck_share", 0) > 0.001:
        lines.append(f"  halts: {_pct(o['stuck_share'])} of the book on average sat in coins that could not be traded, "
                     f"and those days made {_signed(o['stuck_per_year'])} a year")
    years = p.get("years") or {}
    if years:
        lines.append("  share of picks beaten by year: " + ", ".join(f"{y} {_pct(v)}" for y, v in sorted(years.items())))
    for label, rows in (("nearby", rd.get("nearby") or []), ("halves", rd.get("halves") or []),
                        ("phases", rd.get("phases") or []), ("null", rd.get("null") or [])):
        if rows:
            lines.append(f"  {label}: picks beaten " + ", ".join(_pct(r["picks_beaten"]) for r in rows)
                         + "; twins beaten " + ", ".join(_pct(r["twins_beaten"]) for r in rows))
    return lines


# --- the study and the command -----------------------------------------------------

STUDY_LISTS = (30, 50, 100)
STUDY_NS = (3, 5, 10)
STUDY_LOOKBACKS = (7, 14, 30, 60, 90)
STUDY_RHYTHMS = ((1, 0),) + tuple((7, p) for p in range(7))


def study(df: pd.DataFrame, lists=STUDY_LISTS, ns=STUDY_NS, lookbacks=STUDY_LOOKBACKS, rhythms=STUDY_RHYTHMS,
          sub: int = 200, strategy: str = "strongest", progress=None) -> pd.DataFrame:
    """Every setting on both markets, each against `sub` twins and picks: one row a replay."""
    rows = []
    for survivors in (False, True):
        for size in lists:
            m = market(df, survivors=survivors, n_list=size)
            for n in ns:
                for lb in lookbacks:
                    for every, phase in rhythms:
                        spec = {"strategy": strategy, "n": n, "lookback": lb, "every": every, "phase": phase, "list": size}
                        r = one(m, spec, sub, sub)
                        rows.append({"market": "survivors" if survivors else "with the dead", "list": size, "n": n,
                                     "lookback": lb, "every": every, "phase": phase, "net": r["net"],
                                     "basket": r["basket"], "net_per_year": r["net_per_year"],
                                     "basket_per_year": r["basket_per_year"], "costs_per_year": r["costs_per_year"],
                                     "stuck_share": r["stuck_share"],
                                     **{f"twins_{k}": (r["twins"] or {}).get(k) for k in ("beaten", "chance", "timing_per_year")},
                                     **{f"picks_{k}": (r["picks"] or {}).get(k) for k in ("beaten", "chance", "choosing_per_year",
                                                                                            "left_per_year", "left_t")}})
                        if progress:
                            progress(len(rows))
    return pd.DataFrame(rows)


def summary_table(tab: pd.DataFrame) -> pd.DataFrame:
    """The study in one table, a row for each list, n and lookback with the two markets side by side: what
    the book made a year after costs over the list's coins at equal weight (`edge`), the share of its picks
    it beats and what is left a year after costs against them, for the daily rebalance and for the weekly
    one (the average of its seven phases, and the lowest phase's share), and twins for the weekly."""
    rows = []
    for (size, n, lb), g in tab.groupby(["list", "n", "lookback"], sort=True):
        row = {"list": size, "n": n, "lookback": lb}
        for market_, tag in (("with the dead", "dead"), ("survivors", "surv")):
            h = g[g["market"] == market_]
            daily, weekly = h[h["every"] == 1], h[h["every"] == 7]
            row[f"{tag}_edge_daily"] = float((daily["net_per_year"] - daily["basket_per_year"]).mean()) if len(daily) else None
            row[f"{tag}_edge_weekly"] = float((weekly["net_per_year"] - weekly["basket_per_year"]).mean()) if len(weekly) else None
            row[f"{tag}_picks_daily"] = float(daily["picks_beaten"].mean()) if len(daily) else None
            row[f"{tag}_picks_weekly"] = float(weekly["picks_beaten"].mean()) if len(weekly) else None
            row[f"{tag}_picks_weekly_lowest"] = float(weekly["picks_beaten"].min()) if len(weekly) else None
            row[f"{tag}_left_weekly"] = float(weekly["picks_left_per_year"].mean()) if len(weekly) else None
            row[f"{tag}_twins_weekly"] = float(weekly["twins_beaten"].mean()) if len(weekly) else None
        rows.append(row)
    return pd.DataFrame(rows)


def luck_count(tab: pd.DataFrame) -> dict:
    """On each market, how many replays a book with no skill would match one time in ten or less, against
    how many luck alone gives: with this many settings tried, some will."""
    out = {}
    for market_, g in tab.groupby("market"):
        chance = g["picks_chance"].dropna()
        out[market_] = {"replays": int(len(chance)), "one_in_ten_or_less": int((chance <= LUCK_ABOVE).sum()),
                        "luck_gives_about": round(LUCK_ABOVE * len(chance), 1)}
    return out


def main(argv: list[str] | None = None) -> int:
    import sys
    argv = sys.argv[1:] if argv is None else argv
    if "--spec" in argv:
        # --spec strongest,5,30,7,0,50[,30]: strategy, n, lookback, every, phase, list[, filter]
        spec = parse_spec(argv[argv.index("--spec") + 1])
        df = binance.load()
        for survivors in (False, True):
            print((f"on the survivors' market (the {SURVIVORS_TOP} coins most traded as it ends, their whole past kept)"
                   if survivors else "on the market with the dead coins"))
            print("\n".join(words(whole(market(df, survivors=survivors, n_list=spec["list"]), spec))))
        return 0
    if "--study" in argv:
        # every setting of strongest on both markets: about twenty minutes; --out FILE keeps the rows as CSV
        tab = study(binance.load(), progress=lambda k: print(f"[widebench] {k} replays", flush=True) if k % 40 == 0 else None)
        if "--out" in argv:
            tab.to_csv(argv[argv.index("--out") + 1], index=False)
        with pd.option_context("display.width", 250, "display.max_rows", 500, "display.max_columns", 50):
            print(summary_table(tab).round(3).to_string(index=False))
        for market_, c in luck_count(tab).items():
            print(f"{market_}: {c['one_in_ten_or_less']} of {c['replays']} replays beat their picks by as much as luck "
                  f"gives one time in ten or less; luck alone gives about {c['luck_gives_about']}")
        return 0
    print("python -m bot.widebench --spec strongest,5,30,7,0,50[,30]   (strategy, n, lookback, every, phase, list[, filter])\n"
          "python -m bot.widebench --study [--out FILE]               (every setting of strongest, on both markets)")
    return 0


def parse_spec(text: str) -> dict:
    """strategy,n,lookback,every,phase,list and, if given, the filter's days (0 or left out: no filter)."""
    parts = [p.strip() for p in text.split(",")]
    if len(parts) not in (6, 7) or parts[0] not in STRATEGIES:
        raise SystemExit(f"--spec wants strategy,n,lookback,every,phase,list[,filter] with a strategy among "
                         f"{sorted(STRATEGIES)}, not {text!r}")
    spec = {"strategy": parts[0], "n": int(parts[1]), "lookback": int(parts[2]), "every": int(parts[3]),
            "phase": int(parts[4]), "list": int(parts[5])}
    if len(parts) == 7 and int(parts[6]):
        spec["filter"] = int(parts[6])
    return spec


if __name__ == "__main__":
    raise SystemExit(main())
