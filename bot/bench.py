"""The bench: what a strategy shows on history, set against its own twins. PROTECTED.

    python -m bot.bench --config configs/challenger3.yaml --quick   # the replay and its twins
    python -m bot.bench --config configs/challenger3.yaml           # the whole reading
    python -m bot.bench --all                                       # the champion and every slot, side by side

A backtest's return says little. Over five years in which the market fell by
half, anything that held coins lost money and anything that sat in cash looks
clever. The bench asks a narrower question, one that has an answer: did *when*
the strategy held what it held add anything? And then: could that be luck, or
one lucky setting?

What it does, in order.

1. Replays the config through the real engine (bot.backtest, the same `step`
   the hourly loop runs) over all the history on file, and keeps the book hour
   by hour.
2. Twins. A twin is the same book slid later in time: the same positions in
   the same order on the same coins, held for as long, with nothing left of
   when they were taken. A thousand are made. A book with no timing lands
   anywhere among its twins and beats about half of them. The share it beats,
   before costs, is the bench's main figure.
3. What the timing is worth: the book as it last traded each pair, less its
   average twin, before costs, a year. Then what letting positions run
   between trades added to that, what the costs took, and what is left.
4. By calendar year, at double costs, on each half of the coins, and at
   settings near its own. An edge that lives in one year, one coin or one
   setting is a bet on that year, coin or setting.
5. The clock. If the strategy's decisions can depend on the hour or the
   weekday, it is replayed with the clock moved, because a rule with a rhythm
   can look like skill on one phase of it alone (FINDINGS, Overturned,
   2026-10-06).
6. The live rule. Had a test begun on each day of this history, how often
   would it have had the counts a promotion asks for (PROMOTION.md)?

How a twin is made, and why that way. `series` has the particulars.

- A twin holds each pair at the weight the book last *traded* it to, not the
  weight the book then drifted to. A held position's weight moves with its
  price, so the weights a book ends each hour with carry the market's own
  path, and a book that bought once and never traded again would be told
  apart from its twins by that alone. What letting positions run added is
  shown apart.
- A twin is slid 30 days or more, and never so far round that it would hold
  positions the book took soon after the hour in hand: within the 90 days of
  candles a strategy is handed, and then within the longest the book stayed
  in any one pair, or 90 days more if that is longer. Those were chosen with
  that hour in view. A trend follower's twin slid that way has seen the rise
  it rides, and one that holds what a book was still sitting on months later
  has seen that the price had not come back. A strategy is told what it
  holds, so a book that is never out of a pair leaves no room at all: it has
  no twins, and the bench cannot read its timing, which is not to say it has
  none. (A book that never leaves any position it takes finishes no trade of
  its own, and the live rule ends such a test at its look. One that keeps
  one position for good and trades the rest is not ended by that. Nor is one
  that sells down to a crumb and never to nothing: the rule counts a
  position as left at a twentieth of its size, the bench only at nothing.
  Neither is read here. Reading such books by their trades alone was tried
  and taken out again: FINDINGS, 2026-10-07.)
- A pair that was listed late is slid inside the stretch it has prices for,
  so a twin holds as much of it as the book does.
- Twins are ranked before costs, on the t of each one's daily gap to the
  average twin. Costs are the same for all of them, and a shared cost divided
  by each one's own noise would rank the noisier book higher.
- A thousand twins are not a thousand chances for luck to match the book:
  twins slid a few days apart are nearly one book. The reading says how many
  separate twins they are worth (`separate`) and, from that, how often a book
  with no timing does as well (`chance`). A slow book on a short run has
  twins worth a handful, and then no share of them is saying much.

How far to trust it, measured (FINDINGS, 2026-10-07). On markets made from
the ten pairs' own hours with every hour's direction tossed, so that the past
says nothing, books that decide on that past all the same (trend followers,
dip buyers, breakouts, books that sit on a position until its price comes
back) and blind ones were read. On five years the chance came out at one in
ten or less for seven in a hundred of the books that could be read, and for
no kind of book clearly more than ten: from none for the slowest to twelve
in a hundred, give or take two, for blind books. On shorter runs it is more
cautious still. The share of twins beaten alone is not that honest: a slow
dip buyer, whose wins are many and small and whose losses are few and large,
beat 90% of its twins 18 times in 100 on five years; and a book whose twins
are worth fewer than nine separate ones beats nine in ten of them about one
time in ten with nothing in it, and is given no chance of one in ten however
many it beats. (Books sized by how quiet each coin has been were made as
well. They are never out of a pair, and not one of them could be read.)

What it is not. Every number here is in sample: the config was written by
someone who had seen this history. The bench can show that an idea has
nothing; it cannot show that it has something. Only the prospective test does
that (PROMOTION.md). It ranks ideas for a slot and no rule leans on it.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import copy
import hashlib
import inspect
import json
import math
import multiprocessing
import multiprocessing.connection
import os
import re
import sys
import textwrap
import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import backtest, config, strategy

VERSION = 1                 # goes up when a reading would come out differently on the same data
TWINS = 1000                # twins made for a config's own replay
SUB_TWINS = 200             # ... and for each nearby setting, each half of the coins and each phase of the clock
MIN_SLIDE_DAYS = 30         # a twin is slid by at least this
MIN_ROOM_DAYS = 90          # slides are drawn from a stretch at least this long, or there are no twins
NEARBY = 6                  # settings near the config's own that are replayed
NEARBY_SPREAD = 0.25        # each number in params is moved by up to this share, up or down
CLOCK_SHIFTS_H = (27, 54, 81, 108, 135, 162)    # every other weekday, and six other hours of the day
PROBE_SHIFTS_H = (27, 81, 135)
PROBE_HOURS = 24            # hours of history on which the strategy is asked whether the clock matters to it
SEED = 20261007             # fixed, so the same config on the same history always reads the same
MIN_DAYS = 30               # fewer daily readings than this and a Sharpe ratio or a t is not given
STALE_AFTER_S = 7 * 86400   # a saved reading older than this is taken again
DAYS_PER_YEAR = 365
TAIL_SHARE = 0.005          # the best and the worst days a reading shows apart: this share of them, each end
EPS = 1e-9
MOST_COST = 0.999           # an hour's fills cannot cost more of the book than this

# Where the words at the end of a reading change. A reading aid and no more. `chance` is how often a book
# with no timing does as well among its twins as this one did; measured on markets with no memory it is
# LUCK_ABOVE or under about one time in ten for the kinds of book that get there most often, and less
# often than that for slow books and short runs (FINDINGS, 2026-10-07). How often an idea that somebody
# has tuned on this history gets under it has not been measured, and is more often than that.
NO_TIMING_BELOW = 0.5       # share of twins beaten under which there is no sign of timing at all
LUCK_ABOVE = 0.10           # a chance of doing as well with no timing above which it cannot be told from luck
HOLDS_UP = 0.75             # share of its own twins a nearby setting, a half of the coins or a phase of the clock
                            # has to beat for the result to count as still there. A book with no timing beats
                            # half; one that beats nine in ten at its own setting and barely half a quarter
                            # away from it has most of its result in the setting

STOPPED = "not run: the bench's time ran out"
DROPPED = "not run: its config's own replay had failed"
GRACE_S = 5.0               # what a process that has answered, or closed its pipe, is given to end by itself
START_TRIES = 3             # times a replay's process is tried for when the machine has none to give


# --- the book, hour by hour -------------------------------------------------

def series(path: dict) -> dict:
    """A recorded run (bot.backtest.run_backtest(..., record=True)["path"]) as
    hourly and daily series.

    Hour t runs from one recorded step to the next. `held[t]` is the share of
    equity in each pair just after step t's fills, `r[t]` each pair's move from
    its price at t to its price at t+1, and `c[t]` the costs of the fills at
    t+1 as a share of equity. Then equity[t+1] = equity[t] * (1 + sum(held*r))
    * (1 - c), and that is exact: the record prices a held pair that has no
    candle in some hour at the mark the account itself valued it at. `gap_bps`
    is how far the days rebuilt this way are from the engine's own, at the
    worst, in basis points. It should be nothing; anything else is a fault in
    the record, and the reading says so.

    `w[t]` is what twins are made of: each pair at the weight the book last
    traded it to. A trade is an hour in which the number of coins held
    changed; between trades `w` stands still while `held` moves with the
    price. `valid` marks the hours a pair can be held in, from its first price
    to its last, and `stretches` groups the pairs by those hours: a twin
    slides each group inside its own. `hold` is the longest the book was in
    any one pair without a break, in hours, and `hold_pair` the pair that was
    (`lead` says what it is for).

    The hours before the strategy could first decide on anything (every
    decision said it had too few candles) are left out: a book that is flat
    because it has no data is not a view on the market."""
    ts = np.asarray(path["ts"], dtype="int64")
    starved = np.asarray(path["starved"], dtype=bool)
    live = np.flatnonzero(~starved)
    if not len(live) or len(ts) - int(live[0]) < 48:
        raise ValueError("the strategy never had the candles it needs, or had them for under two days")
    first = int(live[0])
    ts, eq = ts[first:], np.asarray(path["equity"], dtype=float)[first:]
    costs = np.asarray(path["costs"], dtype=float)[first:]
    weights = np.asarray(path["weights"], dtype=float)[first:]
    fills = np.asarray(path["fills"], dtype="int64")[first:]
    raw = np.asarray(path["opens"], dtype=float)[first:]
    raw = np.where(raw > 0, raw, np.nan)                    # a price of nothing is no price
    opens = pd.DataFrame(raw).ffill().to_numpy()
    with np.errstate(invalid="ignore", divide="ignore"):
        r = opens[1:] / opens[:-1] - 1.0
        coins = weights * eq[:, None] / opens
    r = np.where(np.isfinite(r), r, 0.0)                    # nothing until a pair's first price
    coins = np.where(np.isfinite(coins), coins, 0.0)
    n, pairs = r.shape
    hour = np.arange(n + 1)[:, None]
    has = np.isfinite(raw)
    began = np.where(has, hour, n + 1).min(axis=0)          # each pair's first hour with a price of its own
    ended = np.where(has, hour, -1).max(axis=0)             # ... and its last
    valid = (hour[:-1] >= began) & (hour[:-1] < ended)
    # the weight each pair was last traded to
    changed = np.abs(np.diff(coins, axis=0)) > 1e-9 * np.maximum(np.abs(coins[1:]), np.abs(coins[:-1]))
    traded = np.vstack([np.ones((1, pairs), dtype=bool), changed])
    as_traded = np.take_along_axis(weights, np.maximum.accumulate(np.where(traded, hour, 0), axis=0), axis=0)
    held, w = weights[:-1], np.where(valid, as_traded[:-1], 0.0)
    paid = np.diff(costs)
    c = np.clip(paid / np.maximum(eq[1:] + paid, EPS), 0.0, MOST_COST)
    day = ts[:-1] // 86400
    starts = np.flatnonzero(np.r_[True, day[1:] != day[:-1]])
    by_pair = np.expm1(np.add.reduceat(np.log1p(np.maximum(r, -0.999999)), starts, axis=0))
    listed = np.add.reduceat(valid.astype(float), starts, axis=0) > 0
    n_listed = listed.sum(axis=1)
    basket = np.where(n_listed > 0, (by_pair * listed).sum(axis=1) / np.maximum(n_listed, 1), 0.0)
    groups: dict[tuple[int, int], list[int]] = {}
    for p in range(pairs):
        if ended[p] > began[p]:
            groups.setdefault((int(began[p]), int(ended[p])), []).append(p)
    stretches = [((a, b), np.ascontiguousarray(w[a:b][:, cols]), np.ascontiguousarray(r[a:b][:, cols]))
                 for (a, b), cols in sorted(groups.items())]
    names = [[str(path["pairs"][p]) for p in cols] for _, cols in sorted(groups.items())]
    invested = held.sum(axis=1)
    hold, where = _longest(w > 0)
    s = {"ts": ts[:-1], "pairs": list(path["pairs"]), "held": held, "w": w, "r": r, "valid": valid, "c": c,
         "starts": starts, "days": day[starts], "by_pair": by_pair, "listed": listed, "basket": basket,
         "stretches": stretches, "stretch_pairs": names, "memory": int(path["memory_hours"]),
         "hold": hold, "hold_pair": None if where is None else str(path["pairs"][where]),
         "hourly": (held * r).sum(axis=1),
         "fills": np.add.reduceat(fills[1:], starts), "exposure": float(invested.mean()),
         "exposure_daily": np.add.reduceat(invested, starts) / np.diff(np.r_[starts, n]),
         "exits": np.asarray(path.get("exits", ()), dtype="int64"),
         "span": tuple(path.get("span") or (int(ts[0]), int(ts[-1])))}
    s["gross"] = _days(s, s["hourly"])
    s["daily"] = _days(s, _after(s["hourly"], c))
    engine_daily = np.multiply.reduceat(eq[1:] / eq[:-1], starts) - 1.0
    gap = float(np.max(np.abs(engine_daily - s["daily"])) * 1e4)
    s["gap_bps"] = gap if math.isfinite(gap) else float("inf")     # a record with a hole in it does not rebuild at all
    return s


def _longest(on: np.ndarray) -> tuple[int, int | None]:
    """The longest run of True down any one column, and which column it is in
    (the first, when two are as long)."""
    best, where = 0, None
    for j in range(on.shape[1]):
        edges = np.flatnonzero(np.diff(np.r_[0, on[:, j].astype(np.int8), 0]))
        if len(edges) and int((edges[1::2] - edges[::2]).max()) > best:
            best, where = int((edges[1::2] - edges[::2]).max()), j
    return best, where


def _days(s: dict, hourly: np.ndarray) -> np.ndarray:
    """An hourly series of returns, compounded into days."""
    return np.expm1(np.add.reduceat(np.log1p(np.maximum(hourly, -0.999999)), s["starts"]))


def _after(hourly: np.ndarray, c: np.ndarray) -> np.ndarray:
    """Hourly returns after each hour's costs: (1 + hourly) * (1 - c) - 1, written so that an hour
    with no costs comes out as it went in, to the last digit."""
    return hourly - c * (1.0 + hourly)


def with_costs(s: dict, multiple: float) -> dict:
    """The same book had every fill cost `multiple` times what it did: 0 for a
    book that trades for nothing, 2 for double costs. The positions are left as
    they were; a strategy does not decide differently because trading costs more."""
    out = dict(s, c=np.clip(s["c"] * float(multiple), 0.0, MOST_COST))
    out["daily"] = _days(out, _after(out["hourly"], out["c"]))
    return out


# --- twins --------------------------------------------------------------------

def lead(s: dict) -> int:
    """Hours a twin's slide stops short of the whole way round. Slid by all
    but k hours, a twin holds in each hour the positions the book took k hours
    *later*, and those were chosen with that hour in view for as long as the
    strategy's memory reaches. Its memory is the candles it is handed and what
    it holds. A strategy is told its positions, so one that is still in a pair
    can be saying something about every hour since it went in (a stop that has
    not been hit, a price that has not come back), however often it has traded
    the pair meanwhile. So: the candles it is handed, and then the longest it
    was in any one pair, or as long again as the candles if that is longer. A
    book whose longest stay is most of the run leaves no room, and has no
    twins.

    This is a rule of thumb, held to what was measured (FINDINGS, 2026-10-07).
    A strategy that enters on one thing and leaves on another carries
    something through its flat stretches too. And every strategy is taken to
    use what it is told it holds: reading the ones that do not by their
    trades instead, so that a book which is never out of a pair could still
    be set against twins, was built and taken out again, because no reading
    of a strategy's code could be made sure that it keeps nothing of its own
    between hours."""
    return int(s["memory"]) + max(int(s["memory"]), int(s["hold"]))


def least_hours(s: dict) -> int:
    """The shortest stretch a book can be slid inside."""
    return MIN_SLIDE_DAYS * 24 + lead(s) + MIN_ROOM_DAYS * 24


def _held(s: dict) -> list[tuple[int, list[str]]]:
    """Each stretch the book holds something in: its length in hours, and the
    pairs of it that are held."""
    out = []
    for ((a, b), w, _), names in zip(s["stretches"], s["stretch_pairs"]):
        held = [name for j, name in enumerate(names) if w[:, j].any()]
        if held:
            out.append((b - a, held))
    return out


def no_twins(s: dict) -> str | None:
    """Why a book cannot be set against twins, or None when it can. "idle":
    it never held a position. "short": the run is too short for any book, one
    that stays in nothing for long included. "hold": the run would do for
    such a book and not for this one, with the stay it has. Where the run is
    long enough, the same two of the pairs it holds: "new" when none of them
    has prices for long enough for any book, "pairs" when they would do for a
    book that stays in nothing for long and not for this one."""
    hours, least = len(s["c"]), least_hours(s)
    any_book = (MIN_SLIDE_DAYS + MIN_ROOM_DAYS) * 24 + 2 * int(s["memory"])
    held = [m for m, _ in _held(s)]
    if not held:
        return "idle"
    if hours < least:
        return "short" if hours < any_book else "hold"
    if max(held) < least:
        return "new" if max(held) < any_book else "pairs"
    return None


def left_in_place(s: dict) -> list[str]:
    """The pairs the book holds whose prices cover too short a stretch to
    slide a book inside. Their positions stay where they were in every twin,
    so what their timing added is in the book and in every twin alike: it is
    neither counted nor tested."""
    least = least_hours(s)
    return sorted(name for m, names in _held(s) if m < least for name in names)


def slid(s: dict, hours: int) -> tuple[np.ndarray, np.ndarray]:
    """The book as last traded, slid `hours` later: its daily returns before
    costs and after them. The market stays where it was. Each group of pairs
    is slid inside the stretch it has prices for, round the end of that
    stretch and back in at its start; a stretch too short to slide a book
    inside is left where it is. The costs slide with the positions. Slid by
    nothing it is the book as last traded.

    Where the end of a stretch meets its start a twin changes position once
    without the book ever having done so, and that change is not charged.
    Against five years of fills it is nothing. A twin that holds a late pair
    and the others from different hours can hold more than the book ever did
    at one time; on average it holds exactly as much."""
    n = len(s["c"])
    least = least_hours(s)
    hourly = np.zeros(n)
    for (a, b), w, r in s["stretches"]:
        m = b - a
        k = int(hours) % m if m >= least else 0
        if k:
            hourly[a + k: b] += np.einsum("ij,ij->i", w[: m - k], r[k:])
            hourly[a: a + k] += np.einsum("ij,ij->i", w[m - k:], r[:k])
        else:
            hourly[a:b] += np.einsum("ij,ij->i", w, r)
    c = np.roll(s["c"], int(hours) % n)
    return _days(s, hourly), _days(s, _after(hourly, c))


def slides(s: dict, n: int = TWINS, seed: int = SEED) -> np.ndarray | None:
    """How far each of n twins is slid, in hours: drawn evenly from
    MIN_SLIDE_DAYS up to `lead` short of the whole way round, and such that
    every stretch the book holds something in, and that is long enough to
    slide a book inside, is slid by as much inside itself. None when the book
    cannot be set against twins (`no_twins` says why), and never otherwise:
    a slide of MIN_SLIDE_DAYS and a little fits every such stretch."""
    hours, least, front, back = len(s["c"]), least_hours(s), MIN_SLIDE_DAYS * 24, lead(s)
    if n < 1 or no_twins(s):
        return None
    own = [m for m, _ in _held(s) if least <= m < hours]
    rng = np.random.default_rng(seed)
    out: list[int] = []
    for _ in range(1000):
        draw = rng.integers(front, hours - back + 1, size=n)
        ok = np.ones(n, dtype=bool)
        for m in own:
            ok &= (draw % m >= front) & (draw % m <= m - back)
        out.extend(int(x) for x in draw[ok])
        if len(out) >= n:
            break
    else:       # so few slides fit that a thousand rounds did not find enough: the rest from those that fit them all
        out.extend(int(x) for x in rng.integers(front, min([hours] + own) - back + 1, size=n - len(out)))
    return np.array(out[:n], dtype="int64")


def _scores(gaps: np.ndarray) -> np.ndarray | None:
    """The t of each row of daily gaps: its mean over its standard error. A
    row that is nothing every day scores nothing, so a book that never trades
    ties with its twins. None on too few days."""
    gaps = np.atleast_2d(gaps)
    days = gaps.shape[1]
    if days < MIN_DAYS:
        return None
    mean, sd = gaps.mean(axis=1), gaps.std(axis=1, ddof=1)
    still = ~(sd > 1e-12)
    t = mean / np.where(still, 1.0, sd / math.sqrt(days))
    return np.where(still, np.where(np.abs(mean) <= 1e-12, 0.0, np.where(mean > 0, np.inf, -np.inf)), t)


def separate(by: np.ndarray, gaps: np.ndarray, around: float | None = None) -> float:
    """How many separate twins a set of twins is worth. Two twins slid a day
    apart are nearly the same book, so a thousand twins are far fewer than a
    thousand chances for luck to match the book, and it is the number of
    chances that says how far a book can stand out among them.

    by: how far each twin is slid, in hours. gaps: each twin's days, a row
    each. around: the hours in the whole way round, so that a twin slid
    nearly all the way and one slid hardly at all count as near each other.

    Each twin's days are taken to the average twin's, which is how a book is
    ranked among them, then put in units of that twin's own spread, so that
    a loud twin counts as one and no more, and taken to the average once
    again. The likeness of two twins is their days multiplied together and
    summed, over what a twin's own days come to on average. Taken to their
    average like this, twins with nothing in common are not unlike each
    other but opposed, a little: what one has above the average the rest
    must have below it, and over all pairs the likenesses add up to nothing.
    Among k separate twins any two are alike by -1/(k-1).

    Two counts are made, and the smaller is the answer. The first looks at
    likeness by distance: the pairs are sorted by how far apart they are
    slid and averaged in groups, the place is found where likeness has
    stopped falling with distance (the first group at or under the average
    of all the groups after it), and the level p it has settled at from
    there on gives k = 1 - 1/p. Twins that are k blocks, each block one
    book, read k. Twins whose likeness dies away with distance read about
    the number of separate twins whose average would vary as much as theirs
    does. But it takes likeness to end where it first ends, and for a book
    that keeps to the clock it comes back: slid a week further, a book that
    holds at weekends is the same book again, and the first count read 888
    for twins worth three or four (found in review, 2026-10-07). The second
    takes likeness wherever it is: one more than the square of the summed
    likeness of each twin with itself over the summed squares of all the
    likenesses, less what twins with nothing in common show by chance. That
    last is reckoned day by day: a market's days are not of a size, a few
    wild ones carry most of what any twin's days come to, and two twins
    with nothing else in common are alike in having been through them.
    Reckoned as if every day weighed the same, the allowance was a fifth of
    what it should be and the cap cut the live books' twins by up to half
    (found in review, 2026-10-07). Blocks read k by the second count too,
    wherever they lie; twins whose likeness dies away read about twice what
    the first count gives, which is why it is the cap and not the count. On
    under a few hundred days it reads low, the allowance being a little
    short there; that errs to caution. Never more than the twins there are,
    never fewer than one (FINDINGS, 2026-10-07)."""
    n = len(by)
    if n < 2:
        return 1.0
    z = gaps - gaps.mean(axis=0, keepdims=True)
    z = z - z.mean(axis=1, keepdims=True)
    spread = np.sqrt((z ** 2).sum(axis=1, keepdims=True))
    if not (spread > 1e-12).all():
        return 1.0                      # twins that do not differ at all are one twin
    z = z / spread
    z = z - z.mean(axis=0, keepdims=True)
    like = z @ z.T
    size = float(np.trace(like)) / n
    by_day = (z ** 2).mean(axis=0)      # what each day carries of a twin's days: a few wild days carry most of them
    by_chance = n * (n - 1) * float((by_day ** 2).sum())
    cap = 1.0 + (n * size) ** 2 / max(float((like ** 2).sum()) - by_chance, 1e-300)
    pick = np.triu_indices(n, 1)
    far = np.abs(by[:, None] - by[None, :])[pick].astype(float)
    if around:
        far = np.minimum(far, float(around) - far)
    alike = (like / size)[pick][np.argsort(far, kind="stable")]
    group = max(20, len(alike) // 250)
    groups = len(alike) // group
    count = float(n)                    # with too few pairs of twins to see where likeness ends, as many as there are
    if groups >= 2:
        level = alike[: groups * group].reshape(groups, group).mean(axis=1)
        after = (level[::-1].cumsum()[::-1] - level)[:-1] / np.arange(groups - 1, 0, -1)    # the average of the groups after each
        settled = np.flatnonzero(level[:-1] <= after)
        stop = int(settled[0]) if len(settled) else groups - 1
        p = float(alike[stop * group:].mean())
        if p < 0:
            count = 1.0 - 1.0 / p
    return float(max(1.0, min(n, count, cap)))


def chance(beaten: float | None, worth: float | None) -> float | None:
    """How often a book with no timing lands as high among its twins as this
    one did: the share of the separate twins that did as well or better,
    counting the book itself as one more of them. Among 9 separate twins the
    best a book can do is to beat all 9, and luck does that one time in 10."""
    if beaten is None or worth is None:
        return None
    return float(((1.0 - beaten) * worth + 1.0) / (worth + 1.0))


def judge(s: dict, n: int = TWINS, seed: int = SEED) -> dict | None:
    """The book set against n twins. `beaten`: over each stretch in `spans`,
    the share of twins whose t the book's is above, a tie counting as half.
    The t is that of the daily gap to the average twin, before costs, the
    book's taken as last traded like theirs. `gross`: the average twin's daily
    return before costs, which is what the book's positions made wherever in
    time they were put. `own`: the book's, as last traded. `net_middle`: what
    the middle twin made over the whole run after the book's costs. `worth`:
    how many separate twins the n are worth (`separate`). `in_place`: the
    pairs that could not be slid (`left_in_place`). None when the book cannot
    be set against twins."""
    by = slides(s, n, seed)
    if by is None:
        return None
    own = slid(s, 0)[0]
    theirs = np.empty((len(by), len(own)))
    nets = np.empty(len(by))
    for i, hours in enumerate(by):
        theirs[i], net = slid(s, int(hours))
        nets[i] = compounded(net)
    mean = theirs.mean(axis=0)
    beaten = {}
    for name, mask in spans(s["days"]).items():
        mine = _scores((own - mean)[mask])
        if mine is None:
            beaten[name] = None
            continue
        others = _scores(theirs[:, mask] - mean[mask])
        level = (others == mine[0]) | (np.abs(others - mine[0]) <= EPS)
        beaten[name] = float(((others < mine[0]) & ~level).sum() + 0.5 * level.sum()) / len(others)
    return {"n": int(len(by)), "beaten": beaten, "gross": mean, "own": own, "net_middle": float(np.median(nets)),
            "slides": by, "worth": separate(by, theirs - mean, around=len(s["c"])), "in_place": left_in_place(s)}


def measure(x: np.ndarray) -> dict | None:
    """Yearly Sharpe ratio and t of a daily series; None when there are too
    few days or the series does not vary."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) < MIN_DAYS:
        return None
    sd = float(x.std(ddof=1))
    if not math.isfinite(sd) or sd < 1e-12:
        return None
    mean = float(x.mean())
    return {"sharpe": mean / sd * math.sqrt(DAYS_PER_YEAR), "t": mean / (sd / math.sqrt(len(x))), "days": int(len(x))}


def spans(days: np.ndarray) -> dict[str, np.ndarray]:
    """The stretches a book is set against its twins over: the whole run, its
    last 365 days when the run is longer than that, and each calendar year
    with enough days in it."""
    out = {"all": np.ones(len(days), dtype=bool)}
    if len(days) > DAYS_PER_YEAR:
        out["last"] = days > days[-1] - DAYS_PER_YEAR
    years = pd.to_datetime(days * 86400, unit="s").year.to_numpy()
    for y in sorted(set(years.tolist())):
        if int((years == y).sum()) >= MIN_DAYS:
            out[str(y)] = years == y
    return out


def compounded(x: np.ndarray) -> float:
    return float(np.prod(1.0 + x) - 1.0)


def a_year(x: np.ndarray) -> float | None:
    """A daily series as a yearly figure: its average day times 365."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    return float(x.mean() * DAYS_PER_YEAR) if len(x) else None


def tails(x: np.ndarray) -> dict:
    """What the best and the worst of a daily series carry, a year: TAIL_SHARE
    of its days at each end, and at least one. Shown so that a result made on
    a handful of days can be seen to be one; nothing is ruled on it, because
    taking the best days away from any series leaves less."""
    x = np.asarray(x, dtype=float)
    k = max(1, int(round(len(x) * TAIL_SHARE))) if len(x) >= MIN_DAYS else 0
    if not k:
        return {"days": 0, "best": 0.0, "worst": 0.0}
    ordered = np.sort(x)
    return {"days": k, "best": float(ordered[len(x) - k:].sum() / len(x) * DAYS_PER_YEAR),
            "worst": float(ordered[:k].sum() / len(x) * DAYS_PER_YEAR)}


def reading_of(s: dict, tw: dict | None) -> dict:
    """What one run shows over its whole length; tw is `judge(s)`.

    Timing is the book as it last traded each pair, less its average twin,
    before costs, a year: what taking its positions when it did was worth
    over taking the same positions at other times. It is what the twins are
    ranked on. Drift is what letting positions run between trades added to
    that, which a twin does not do: the book's own return before costs less
    the same book as last traded. Costs are what the fills took from its
    daily returns. What is left is timing plus drift less costs: the book's
    return after costs less its average twin's before any. The four add up
    exactly."""
    out = {"days": int(len(s["daily"])), "start": _date(int(s["ts"][0])), "end": _date(int(s["ts"][-1]) + 3600),
           "pairs": list(s["pairs"]), "net": compounded(s["daily"]), "basket": compounded(s["basket"]),
           "exposure": s["exposure"], "costs_per_year": a_year(s["gross"] - s["daily"]),
           "rebuilt_within_bps": s["gap_bps"],
           "slide": {"candles_days": s["memory"] / 24.0, "longest_hold_days": s["hold"] / 24.0,
                     "longest_hold_pair": s["hold_pair"], "wrote_params": bool(s.get("wrote_params")),
                     "lead_days": lead(s) / 24.0, "least_days": least_hours(s) / 24.0,
                     "history_days": max([m for m, _ in _held(s)] or [0]) / 24.0},
           "no_twins": None if tw is not None else no_twins(s),
           "twins": None, "timing_per_year": None, "drift_per_year": None, "left_per_year": None,
           "sharpe": None, "t": None, "twin_gross_per_year": None, "tails": None}
    if tw is not None:
        left = s["daily"] - tw["gross"]
        m = measure(left) or {"sharpe": None, "t": None}
        out.update(twins={"n": tw["n"], "beaten": tw["beaten"]["all"], "beaten_last_365": tw["beaten"].get("last"),
                          "net_middle": tw["net_middle"], "worth": tw["worth"],
                          "chance": chance(tw["beaten"]["all"], tw["worth"]), "in_place": list(tw["in_place"])},
                   timing_per_year=a_year(tw["own"] - tw["gross"]), drift_per_year=a_year(s["gross"] - tw["own"]),
                   left_per_year=a_year(left), sharpe=m["sharpe"], t=m["t"],
                   twin_gross_per_year=a_year(tw["gross"]), tails=tails(left))
    return out


def by_year(s: dict, tw: dict | None) -> list[dict]:
    """Each calendar year with enough days in it. A year's timing, drift,
    costs and what is left are the sums of its days', so the years add up to
    the whole, and in each year timing plus drift less costs is what is left."""
    rows = []
    for name, mask in spans(s["days"]).items():
        if name in ("all", "last"):
            continue
        costs = float((s["gross"] - s["daily"])[mask].sum())
        timing = None if tw is None else float((tw["own"] - tw["gross"])[mask].sum())
        drift = None if tw is None else float((s["gross"] - tw["own"])[mask].sum())
        rows.append({"year": int(name), "days": int(mask.sum()), "net": compounded(s["daily"][mask]),
                     "basket": compounded(s["basket"][mask]), "exposure": float(s["exposure_daily"][mask].mean()),
                     "costs": costs, "timing": timing, "drift": drift,
                     "left": None if tw is None else float((s["daily"] - tw["gross"])[mask].sum()),
                     "twins_beaten": None if tw is None else tw["beaten"].get(name)})
    return rows


# --- the live rule, on history --------------------------------------------------

def live_rules(rcfg: dict) -> dict:
    """The counts a promotion asks for, as the hourly loop reads them."""
    from .promote import rule_settings          # the one place the rules file is read into usable values
    st = rule_settings(rcfg.get("challenger"))[0]
    first = max(2, int(round(float(st["window_days"]))))
    return {"first_days": first, "total_days": first + max(0, int(round(float(st["confirm_days"])))),
            "min_fills": int(st["min_trades"]), "min_t": float(st["min_skill_t"]),
            "fast_t": None if st["fast_pass"] is None else float(st["fast_pass"])}


def windows(s: dict, rules: dict) -> dict | None:
    """A test of this config begun on each day of the run, from a year in:
    what each would have had at its looks, window by window. `begin`: the
    day each opens on. `usual`: the exposure the config usually held, its
    average over the 365 days before. `t_first`, `t_total`: the t of its
    daily skill at the first look and at the verdict, skill being each day's
    return less the basket's at that exposure, and the basket the pairs
    listed on the window's first day in equal parts, never set back.
    `left_one`: whether it left a position of its own by the first look.
    `fills_first`, `fills_total`: its fills by each look. None when the run
    has no whole window after its first year."""
    first, total, days = int(rules["first_days"]), int(rules["total_days"]), len(s["daily"])
    begin = np.arange(DAYS_PER_YEAR, days - total + 1)
    if not len(begin):
        return None
    held = np.r_[0.0, np.cumsum(s["exposure_daily"])]
    usual = (held[begin] - held[begin - DAYS_PER_YEAR]) / DAYS_PER_YEAR
    grown = np.vstack([np.zeros((1, s["by_pair"].shape[1])),
                       np.cumsum(np.log1p(np.maximum(s["by_pair"], -0.999999)), axis=0)])
    t_first, t_total = np.full(len(begin), np.nan), np.full(len(begin), np.nan)
    for i, d in enumerate(begin):
        there = s["listed"][d]
        if not there.any():
            continue
        level = np.exp(grown[d: d + total + 1][:, there] - grown[d, there]).mean(axis=1)
        skill = s["daily"][d: d + total] - usual[i] * (level[1:] / level[:-1] - 1.0)
        t_first[i], t_total[i] = _t(skill[:first]), _t(skill)
    fills = np.r_[0, np.cumsum(s["fills"])]
    opened = s["days"][begin] * 86400
    exits = np.sort(s["exits"])
    left_one = (np.searchsorted(exits, opened + first * 86400, side="right")
                - np.searchsorted(exits, opened, side="right")) > 0
    return {"begin": begin, "usual": usual, "t_first": t_first, "t_total": t_total, "left_one": left_one,
            "fills_first": fills[begin + first] - fills[begin], "fills_total": fills[begin + total] - fills[begin]}


def looks(s: dict, rules: dict) -> dict | None:
    """Had a test of this config begun on each day of the run, from a year
    in: how often would it have had what a promotion asks for at its looks?
    Three counts, each as the live rule takes it (PROMOTION.md): a trade of
    its own finished by the first look; `min_fills` fills by the verdict; and
    a daily skill t of `min_t` at the verdict (`windows` has how each is
    taken).

    It is the replay's own days that are cut into windows, so a window opens
    on the book the replay then held, where a live test opens on the slot's,
    and a day here is a UTC day where the live rule counts days from the
    hour a test began. The windows overlap: `apart` is how many would fit
    end to end. In sample, all of it. None when the run has no whole window
    after its first year."""
    w = windows(s, rules)
    if w is None:
        return None
    total, days = int(rules["total_days"]), len(s["daily"])
    enough = w["fills_total"] >= rules["min_fills"]
    with np.errstate(invalid="ignore"):
        reached = w["t_total"] >= rules["min_t"]
        fast = None if rules["fast_t"] is None else \
            w["left_one"] & (w["fills_first"] >= rules["min_fills"]) & (w["t_first"] >= rules["fast_t"])
    read = np.isfinite(w["t_total"])
    return {"windows": int(len(w["begin"])), "apart": int(max(1, (days - DAYS_PER_YEAR) // total)),
            "no_trade": float((~w["left_one"]).mean()), "few_fills": float((~enough).mean()),
            "t_middle": float(np.median(w["t_total"][read])) if read.any() else None, "t_reached": float(reached.mean()),
            "all_counts": float((w["left_one"] & enough & reached).mean()),
            "fast_pass": None if fast is None else float(fast.mean())}


def _t(x: np.ndarray) -> float:
    sd = float(x.std(ddof=1)) if len(x) > 1 else 0.0
    return float(x.mean() / (sd / math.sqrt(len(x)))) if sd > 1e-12 else float("nan")


# --- the settings and the coins either side ----------------------------------

def nearby(params: dict, k: int = NEARBY, spread: float = NEARBY_SPREAD, seed: int = SEED) -> list[dict]:
    """k copies of params with every number in it moved by up to `spread`, up
    or down, all at once. Whole numbers stay whole and at least 1, a zero
    stays zero, and anything that is not a number (a switch, a name) is left
    alone. Copies that come out the same as params or as each other are
    dropped, so there may be fewer than k."""
    names = sorted(n for n, v in params.items()
                   if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) and v != 0)
    rng = np.random.default_rng(seed)
    reach = math.log(1.0 + spread)
    out, seen = [], {json.dumps(params, sort_keys=True, default=str)}
    for _ in range(k * 4):
        if len(out) >= k or not names:
            break
        p = dict(params)
        for n in names:
            v = params[n] * math.exp(rng.uniform(-reach, reach))
            p[n] = (max(1, int(round(v))) if params[n] > 0 else min(-1, int(round(v)))) if isinstance(params[n], int) \
                else float(f"{v:.6g}")
        key = json.dumps(p, sort_keys=True, default=str)
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


def halves(pairs: list[str]) -> list[list[str]]:
    """The pairs halved two ways: every other one, and the first half against
    the second, in alphabetical order. Four lists, or none when there are
    fewer than four pairs."""
    names = sorted(pairs)
    if len(names) < 4:
        return []
    mid = (len(names) + 1) // 2
    return [names[0::2], names[1::2], names[:mid], names[mid:]]


CLOCK_WORDS = ("time", "now", "utcnow", "today", "gmtime", "localtime", "ctime", "strftime", "time_ns", "monotonic",
               "monotonic_ns", "perf_counter", "perf_counter_ns", "process_time")
CODE_NAMES_IT = "its code names the candles' time column or asks the time"
TARGETS_MOVE = "its targets change when the clock is moved"
COULD_NOT_ASK = "it could not be asked"


def names_the_clock(fn) -> bool:
    """Does the strategy's code name the candles' `time` column (`"time"`,
    `.time`, or a name its module has set to something with `"time"` in it:
    a word, a list, a pair of names set at once) or ask what time it is
    (`.now`, `.today`, `.gmtime`, a bare `time()` and the like)? Its own
    code and that of every function of its module it reaches are read as
    code, so a comment or a docstring that happens to hold the word is not a
    finding. Naming the column is not yet a rhythm: a strategy that only
    lines two pairs up by it is replayed with the clock moved and shows no
    difference. What this cannot see is a column read by where it stands and
    not by its name; asking the strategy (`reads_clock`) catches that unless
    the rhythm is a rare one."""
    try:
        tree = ast.parse(inspect.getsource(inspect.getmodule(fn)))
        defs = {node.name: node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
        stands_for = set()

        def given(target, value) -> None:
            """The names a module level assignment gives to something with "time" in it."""
            both = (ast.Tuple, ast.List)
            if isinstance(target, both) and isinstance(value, both) and len(target.elts) == len(value.elts):
                for t, v in zip(target.elts, value.elts):       # two names set at once: each to its own
                    given(t, v)
            elif any(isinstance(v, ast.Constant) and v.value == "time" for v in ast.walk(value)):
                stands_for.update(t.id for t in ast.walk(target) if isinstance(t, ast.Name))
        for node in tree.body:
            if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None:
                for target in (node.targets if isinstance(node, ast.Assign) else [node.target]):
                    given(target, node.value)
    except Exception:  # noqa: BLE001 - whatever stops the code being read: it is then asked instead (`reads_clock`)
        defs, stands_for = {}, set()

    def named(node) -> bool:
        return (isinstance(node, ast.Constant) and node.value == "time") or \
            (isinstance(node, ast.Attribute) and node.attr in CLOCK_WORDS) or \
            (isinstance(node, ast.Name) and (node.id in stands_for or node.id in CLOCK_WORDS))
    if getattr(fn, "__name__", None) not in defs:
        try:
            return any(named(node) for node in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(fn)))))
        except Exception:  # noqa: BLE001
            return False
    todo, seen = [fn.__name__], set()
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        seen.add(name)
        for node in ast.walk(defs[name]):
            if named(node):
                return True
            if isinstance(node, ast.Name) and node.id in defs:
                todo.append(node.id)
    return False


def reads_clock(cfg: dict, rcfg: dict, candles: dict[str, pd.DataFrame]) -> str | None:
    """Can the clock matter to this strategy? None, or why it can. Two ways
    of asking, and either is enough. Its code is read (`names_the_clock`).
    And it is asked for its targets at PROBE_HOURS hours spread over the
    history, flat and holding, and asked again with every candle's time moved
    by a day and three hours, by three days and nine, and by five days and
    fifteen: if any target moves, the clock matters. The first catches a
    rhythm too rare for the second to land on (the first hour of a month),
    the second one that hides behind something the first cannot read. A
    strategy that fails here is taken to read the clock, so that it is looked
    at harder, not less."""
    fn = strategy.get(cfg["strategy"])
    if names_the_clock(fn):
        return CODE_NAMES_IT
    hist = int(rcfg.get("history_hours", 720))
    frames = {p: df.sort_values("time").drop_duplicates("time").reset_index(drop=True)
              for p, df in candles.items() if len(df)}
    if not frames:
        return None
    times = sorted(set.union(*[set(df["time"].astype("int64")) for df in frames.values()]))
    if len(times) < 4:
        return None
    picks = [times[int(i)] for i in np.linspace(len(times) // 3, len(times) - 1, PROBE_HOURS)]
    try:
        for at in picks:
            window = {}
            for p, df in frames.items():
                upto = int(np.searchsorted(df["time"].to_numpy().astype("int64"), at, side="right"))
                if upto:
                    window[p] = df.iloc[max(0, upto - hist): upto]
            for held in ({}, {p: 0.1 for p in window}):
                base = _targets(fn, window, cfg["params"], held)
                for hours in PROBE_SHIFTS_H:
                    moved = {p: df.assign(time=df["time"] + hours * 3600) for p, df in window.items()}
                    if _targets(fn, moved, cfg["params"], held) != base:
                        return TARGETS_MOVE
    except KeyboardInterrupt:
        raise
    except BaseException as e:  # noqa: BLE001
        return f"{COULD_NOT_ASK} ({type(e).__name__}: {e})"
    return None


def _targets(fn, window: dict, params: dict, held: dict) -> dict:
    asked = strategy.normalise(fn({p: df.copy() for p, df in window.items()}, copy.deepcopy(params), dict(held)))
    return {p: round(float(t.weight), 9) for p, t in asked.items()}


# --- one replay, and all of them ---------------------------------------------

def replay(candles: dict[str, pd.DataFrame], rcfg: dict, cfg: dict, days: int | None = None,
           pairs: list[str] | None = None, shift_hours: int = 0) -> tuple[dict, dict]:
    """One run through the engine. Returns (series, the engine's own metrics).
    The strategy is handed a copy of the config, so nothing it does to its
    params reaches the caller's; whether they are, at the end, as they were
    handed in is kept (`wrote_params`), because live a strategy is handed its
    params afresh every hour and would not have what it kept there. That is
    one look, at the end: what a strategy wrote and put back is not seen, nor
    what it keeps anywhere else. A run in which the strategy failed on any
    hour is not a reading of it and raises: the engine goes flat on such an
    hour, live as here, and what comes out is that and not the strategy."""
    use = {p: df for p, df in candles.items() if pairs is None or p in pairs}
    if shift_hours:
        use = {p: df.assign(time=df["time"] + int(shift_hours) * 3600) for p, df in use.items()}
    handed = copy.deepcopy(cfg)
    m = backtest.run_backtest(use, handed, rcfg, max_days=days, record=True)
    path = m.pop("path")
    m.pop("equity_curve", None)
    if path.get("errors"):
        raise RuntimeError(f"the strategy failed on {path['errors']:,} of the {len(path['ts']):,} hours replayed "
                           f"(the first time: {path.get('first_error')}); a run with such hours in it is not a "
                           f"reading of the strategy")
    s = series(path)
    try:        # as plain text, so that a list or a number is itself whatever kind of object holds it
        s["wrote_params"] = json.dumps(_plain(handed.get("params")), sort_keys=True) != json.dumps(_plain(cfg.get("params")), sort_keys=True)
    except Exception:  # noqa: BLE001 - params that cannot even be set side by side are not as they were
        s["wrote_params"] = True
    return s, m


def _task(task: dict, shared: dict) -> dict:
    """One replay and everything read from it, or one strategy asked about
    the clock. Never raises: what fails comes back as its error, and the
    reading says so."""
    began = time.time()
    said = {k: task[k] for k in ("config", "kind", "params", "pairs", "shift_hours") if k in task}
    try:
        cfg = shared["configs"][task["config"]]
        if task["kind"] == "probe":
            return {**said, "ok": True, "clock": reads_clock(cfg, shared["rcfg"], shared["candles"]),
                    "took_s": round(time.time() - began, 1)}
        use = {**cfg, "params": task["params"]} if "params" in task else cfg
        s, m = replay(shared["candles"], shared["rcfg"], use, days=shared["days"], pairs=task.get("pairs"),
                      shift_hours=task.get("shift_hours", 0))
        tw = judge(s, int(task["twins"]))
        out = {**said, "ok": True, **reading_of(s, tw)}
        if task["kind"] == "own":
            rules = shared["rules"]
            twice = with_costs(s, 2.0)
            left = None if tw is None else twice["daily"] - tw["gross"]
            out.update(
                years=by_year(s, tw),
                double_costs={"left_per_year": None if left is None else a_year(left),
                              **{k: (measure(left) or {}).get(k) if left is not None else None for k in ("sharpe", "t")}},
                rule_one={**rules, "fills_by_first": float(m["n_trades"]) / max(float(m["days"]), EPS) * rules["first_days"],
                          "finished_trades": m["finished_trades"], "closed_by_halt_or_error": m["closed_by_halt_or_error"],
                          "no_trade_by_first": backtest.windows_with_no_exit(s["exits"], *s["span"], rules["first_days"]),
                          "no_trade_by_total": backtest.windows_with_no_exit(s["exits"], *s["span"], rules["total_days"]),
                          "windows": looks(s, rules)},
                engine={k: m[k] for k in ("total_return", "max_drawdown", "n_trades", "trades_per_pair_per_day_avg",
                                          "pair_days_at_fill_cap", "starved_share", "avg_gross_exposure", "days")})
        out["took_s"] = round(time.time() - began, 1)
        return out
    except KeyboardInterrupt:
        raise
    except BaseException as e:  # noqa: BLE001
        return {**said, "ok": False, "error": f"{type(e).__name__}: {e}", "took_s": round(time.time() - began, 1)}


def _in_a_process(task: dict, shared: dict, send) -> None:
    sys.stdout = sys.stderr         # what a strategy prints is no part of a reading, and must not land in one
    try:
        try:
            out = _task(task, shared)
        except BaseException as e:  # noqa: BLE001
            out = {"config": task.get("config"), "kind": task.get("kind"), "ok": False, "error": f"{type(e).__name__}: {e}"}
        send.send(out)
    finally:
        send.close()


def run(tasks: list[dict], shared: dict, jobs: int | None = None, deadline: float | None = None) -> list[dict]:
    """Every task, each in a process of its own, `jobs` of them at a time; the
    answers come back in the order of `tasks`. A process of its own means
    that nothing a strategy keeps or breaks in one replay is there in the
    next, so a reading is the same however many run at once, and that a
    strategy which takes its process down with it has cost one replay: it
    comes back as failed.

    Past `deadline` (a time.time()) nothing more is started, what is running
    is stopped, and what was not done comes back saying so. When a config's
    own replay fails, nothing else of that config is worth having: what is
    waiting is not started and what is running is stopped. A process that
    has answered and does not end, or that closes its pipe and carries on,
    is given GRACE_S seconds, or until `deadline` if that is sooner, and then
    stopped. One that ends without an answer has died, whether or not
    something it started still holds its pipe open. One that cannot be
    started, because the machine has no process or memory to give, is tried
    again when another has finished, START_TRIES times in all, and nothing
    else is started until then. Where processes cannot be forked the tasks
    run one after another in this one."""
    out: list[dict | None] = [None] * len(tasks)
    if not tasks:
        return []
    dead: set = set()               # the configs whose own replay has failed

    def late() -> bool:
        return deadline is not None and time.time() >= deadline

    def not_done(i: int, why: str, **more) -> dict:
        t = tasks[i]
        return {**{k: t[k] for k in ("config", "kind", "params", "pairs", "shift_hours") if k in t}, "ok": False,
                "error": why, "took_s": 0.0, **more}

    def settle(i: int, answer: dict) -> None:
        out[i] = answer
        if tasks[i].get("kind") == "own" and not answer.get("ok"):
            dead.add(tasks[i].get("config"))

    if "fork" not in multiprocessing.get_all_start_methods():
        for i, t in enumerate(tasks):
            if late():
                out[i] = not_done(i, STOPPED, stopped=True)
            elif t.get("config") in dead:
                out[i] = not_done(i, DROPPED)
            else:
                with contextlib.redirect_stdout(sys.stderr):
                    settle(i, _task(t, shared))
        return out      # type: ignore[return-value]
    ctx = multiprocessing.get_context("fork")
    jobs = max(1, min(int(jobs or os.cpu_count() or 1), len(tasks)))
    waiting, running, tries = list(range(len(tasks))), {}, {}
    room = jobs                     # how many may run at once: fewer than `jobs` from a refused start until the next that works

    def end(proc) -> None:
        """Wait for a process that should be ending, GRACE_S at the most, then stop it. Not with `join`: that
        takes a process for ended once it has closed what it had open, and then waits for it without limit."""
        until = time.time() + GRACE_S if deadline is None else min(time.time() + GRACE_S, deadline)
        while proc.exitcode is None and time.time() < until:
            time.sleep(0.005)
        if proc.exitcode is None:
            proc.kill()
        proc.join()

    try:
        while waiting or running:
            while waiting and len(running) < min(jobs, room) and not late():
                i = waiting.pop(0)
                if tasks[i].get("config") in dead:
                    out[i] = not_done(i, DROPPED)
                    continue
                recv, send = ctx.Pipe(duplex=False)
                try:
                    # not a daemon: a strategy may start processes of its own, and a daemon may not
                    proc = ctx.Process(target=_in_a_process, args=(tasks[i], shared, send), daemon=False)
                    proc.start()
                except OSError as e:
                    recv.close()
                    send.close()
                    tries[i] = tries.get(i, 0) + 1
                    if running and tries[i] < START_TRIES:
                        waiting.insert(0, i)
                        room = len(running)         # not before one of those has finished: with a deadline this loop
                    else:                           # comes round every second, and three tries were gone in three seconds
                        settle(i, not_done(i, f"no process could be started to replay it ({type(e).__name__}: {e})"))
                    break
                send.close()
                running[recv] = (i, proc)
                room = jobs
            if late():
                for i in waiting + [i for i, _ in running.values()]:
                    out[i] = not_done(i, STOPPED, stopped=True)
                waiting = []
                break
            if not running:
                continue
            for recv in multiprocessing.connection.wait(list(running), timeout=1.0):
                i, proc = running[recv]         # it stays in `running` until it has ended: whatever interrupts the
                try:                            # wait for that, the `finally` below still knows of it and stops it
                    answer = recv.recv()
                    end(proc)
                except Exception:  # noqa: BLE001
                    end(proc)
                    answer = not_done(i, f"the process replaying it died before it could answer (exit code {proc.exitcode})")
                recv.close()
                del running[recv]
                settle(i, answer)
            # One that has ended and left nothing to read has died. Its pipe need not say so: a process the strategy
            # started holds the same pipe open for as long as it lives, and the bench waited that long (found in review)
            for recv, (i, proc) in list(running.items()):
                if proc.exitcode is not None and not recv.poll():
                    proc.join()
                    recv.close()
                    del running[recv]
                    settle(i, not_done(i, f"the process replaying it died before it could answer (exit code {proc.exitcode})"))
            for recv, (i, proc) in list(running.items()):
                if tasks[i].get("config") in dead:
                    proc.kill()
                    proc.join()
                    recv.close()
                    del running[recv]
                    out[i] = not_done(i, DROPPED)
    finally:
        for recv, (_, proc) in running.items():
            proc.kill()
            proc.join()
            recv.close()
    return out      # type: ignore[return-value]


def plan(cfg: dict, candles: dict[str, pd.DataFrame], quick: bool, index: int = 0, clock: str | None = None,
         n_twins: int | None = None) -> list[dict]:
    """The replays one reading needs. index: which of the configs handed to
    `run` this one is. clock: why the clock can matter to the strategy, if it
    can."""
    own, sub = (TWINS, SUB_TWINS) if n_twins is None else (max(1, int(n_twins)), max(1, min(int(n_twins), SUB_TWINS)))
    tasks = [{"config": index, "kind": "own", "twins": own}]
    if quick:
        return tasks
    tasks += [{"config": index, "kind": "nearby", "params": p, "twins": sub} for p in nearby(cfg["params"])]
    tasks += [{"config": index, "kind": "half", "pairs": h, "twins": sub} for h in halves(list(candles))]
    if clock:
        tasks += [{"config": index, "kind": "clock", "shift_hours": h, "twins": sub} for h in CLOCK_SHIFTS_H]
    return tasks


OWN = ("pairs", "start", "end", "days", "net", "basket", "exposure", "slide", "no_twins", "twins", "timing_per_year",
       "drift_per_year", "costs_per_year", "left_per_year", "sharpe", "t", "twin_gross_per_year", "tails",
       "double_costs", "years", "rule_one", "rebuilt_within_bps", "engine")


def assemble(cfg: dict, signed: str, done: list[dict], clock: str | None, quick: bool) -> dict:
    """One config's reading from its replays."""
    own = next((d for d in done if d["kind"] == "own"), None)
    if own is None or not own["ok"]:
        raise RuntimeError("its replay failed: " + (own["error"] if own else "it was never run"))
    cut = [d for d in done if d.get("stopped")]
    if cut:
        raise RuntimeError(f"the bench's time ran out with {len(cut)} of its {len(done)} replays not done")
    return {"version": VERSION, "made_at": int(time.time()), "quick": bool(quick), "signature": signed,
            "hypothesis": cfg.get("hypothesis"), "strategy": cfg["strategy"], "params": cfg["params"],
            **{k: own[k] for k in OWN},
            "nearby": [_light(d) for d in done if d["kind"] == "nearby"],
            "halves": [_light(d) for d in done if d["kind"] == "half"],
            "clock": None if quick else {"why": clock, "shifts": [_light(d) for d in done if d["kind"] == "clock"]},
            "took_s": round(sum(float(d.get("took_s") or 0.0) for d in done), 1)}


def _light(d: dict) -> dict:
    keep = ("ok", "error", "params", "pairs", "shift_hours", "days", "net", "exposure", "timing_per_year",
            "drift_per_year", "costs_per_year", "left_per_year", "t", "no_twins")
    out = {k: d[k] for k in keep if k in d}
    if d.get("ok"):
        out["beaten"] = (d.get("twins") or {}).get("beaten")
    return out


def read_many(configs: list[dict], rcfg: dict, candles: dict[str, pd.DataFrame], days: int | None = None,
              quick: bool = False, jobs: int | None = None, n_twins: int | None = None,
              deadline: float | None = None) -> list[dict]:
    """A reading of each config, their replays sharing the processors. A
    config that cannot be read, for whatever reason, comes back as
    {"failed": why} and costs the others nothing."""
    signed: dict[int, str] = {}
    failed: dict[int, str] = {}
    for i, cfg in enumerate(configs):
        try:
            strategy.get(cfg["strategy"])
            if not isinstance(cfg["params"], dict):
                raise ValueError("params must be a mapping")
            signed[i] = signature(cfg, rcfg)        # of the config as it was handed in, before any of its code has run
        except Exception as e:  # noqa: BLE001
            failed[i] = f"{type(e).__name__}: {e}"
    shared = {"configs": configs, "rcfg": rcfg, "candles": candles, "days": days, "rules": live_rules(rcfg)}
    clock: dict[int, str | None] = {}
    if not quick:
        asked = run([{"config": i, "kind": "probe"} for i in signed], shared, jobs, deadline)
        for d in asked:
            clock[d["config"]] = d["clock"] if d["ok"] else f"{COULD_NOT_ASK} ({d['error']})"
    tasks: list[dict] = []
    for i in signed:
        try:
            tasks += plan(configs[i], candles, quick, i, clock.get(i), n_twins)
        except Exception as e:  # noqa: BLE001
            failed[i] = f"{type(e).__name__}: {e}"
    done = run([t for t in tasks if t["config"] not in failed], shared, jobs, deadline)
    out = []
    for i, cfg in enumerate(configs):
        try:
            if i in failed:
                raise RuntimeError(failed[i])
            out.append(assemble(cfg, signed[i], [d for d in done if d["config"] == i], clock.get(i), quick))
        except Exception as e:  # noqa: BLE001
            out.append({"failed": str(e) if isinstance(e, RuntimeError) else f"{type(e).__name__}: {e}"})
    return out


def read(cfg: dict, rcfg: dict, candles: dict[str, pd.DataFrame], days: int | None = None, quick: bool = False,
         jobs: int | None = None, n_twins: int | None = None) -> dict:
    """The whole reading of one config. quick: the replay and its twins only."""
    r = read_many([cfg], rcfg, candles, days=days, quick=quick, jobs=jobs, n_twins=n_twins)[0]
    if "failed" in r:
        raise RuntimeError(r["failed"])
    return r


NO_REPLAY_RUNS = ("wide", "report", "slot", "shadow")     # the modules of bot/ that no replay runs
RESTS_ON = ("fee_bps", "slippage_bps", "impact_bps", "initial_cash", "history_hours", "max_weight_per_pair",
            "max_gross_weight", "min_trade_notional", "rebalance_threshold", "daily_loss_halt",
            "max_fills_per_pair_per_day", "pairs")


def strategy_code(name: str) -> bytes:
    """bot/strategy.py as the strategy `name` runs it: the whole file as code,
    so with comments and layout left out, less every other registered
    strategy it does not name. A change to another slot's strategy, or to a
    comment, then leaves this one's reading current."""
    src = config.ROOT / "bot" / "strategy.py"
    if not src.exists():
        return b""
    text = src.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text.encode()

    def registered(node) -> list[str]:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return []
        return [str(d.args[0].value) for d in node.decorator_list
                if isinstance(d, ast.Call) and getattr(d.func, "id", getattr(d.func, "attr", None)) == "register"
                and d.args and isinstance(d.args[0], ast.Constant)]

    others = [node for node in tree.body if registered(node) and name not in registered(node)]
    kept = [node for node in tree.body if node not in others]
    while True:         # ... unless this strategy, or something it reaches, calls one of them
        used = {n.id for node in kept for n in ast.walk(node) if isinstance(n, ast.Name)}
        back = [fn for fn in others if fn.name in used and fn not in kept]
        if not back:
            break
        kept += back
    tree.body = [node for node in tree.body if node in kept]
    return ast.dump(tree).encode()


def signature(cfg: dict, rcfg: dict) -> str:
    """Changes when a saved reading no longer describes the config: its
    strategy or params, the code of that strategy or of anything in bot/ a
    replay runs, the cost model, the limits, the pairs, the counts the live
    rule asks for, or the bench itself."""
    code = strategy_code(str(cfg["strategy"]))
    for src in sorted((config.ROOT / "bot").glob("*.py")):
        if src.stem != "strategy" and src.stem not in NO_REPLAY_RUNS:
            code += src.name.encode() + src.read_bytes()
    rests = {k: rcfg.get(k) for k in RESTS_ON}
    text = config.strategy_signature(cfg) + json.dumps([rests, live_rules(rcfg)], sort_keys=True, default=str) \
        + f"bench {VERSION}"
    return hashlib.sha256(text.encode() + code).hexdigest()[:16]


# --- words -------------------------------------------------------------------

def _date(ts: int) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")


def _pct(x, digits: int = 0) -> str:
    return "n/a" if x is None else f"{x:+.{digits}%}"


def _share(x, short: bool = False) -> str:
    """A share as a whole percentage. One that is not all is never shown as
    all, nor one that is not nothing as nothing: 995 twins beaten of 1,000
    read `100%` (found in review, 2026-10-07). short: for a table or a list."""
    if x is None:
        return "n/a"
    text = f"{x:.0%}"
    if text == "100%" and x < 1.0:
        return ">99%" if short else "over 99%"
    if text == "0%" and x > 0.0:
        return "<1%" if short else "under 1%"
    return text


def _about(x) -> str:
    """A share that is an estimate: `about 28%`, and with no `about` where it is already `over 99%` or `under 1%`."""
    text = _share(x)
    return text if x is None or " " in text else "about " + text


def _num(x, digits: int = 2) -> str:
    return "n/a" if x is None else f"{x:+.{digits}f}"


def _cost(x) -> str:
    return "n/a" if x is None else f"{x:.1%}"


def _counts(rows: list[dict]) -> tuple[int, int]:
    """Of the replays that were to be set against twins, how many beat
    HOLDS_UP of theirs, and how many there are. One that could not be
    replayed at all is one that did not; one too short for twins is not
    counted either way."""
    counted = [r for r in rows if not r.get("ok") or r.get("beaten") is not None]
    return sum(1 for r in counted if r.get("ok") and r["beaten"] >= HOLDS_UP), len(counted)


def _spread(rows: list[dict]) -> str:
    vals = sorted(r["beaten"] for r in rows if r.get("ok") and r.get("beaten") is not None)
    failed = sum(1 for r in rows if not r.get("ok"))
    short = len(rows) - len(vals) - failed
    text = ", ".join(_share(v, short=True) for v in vals) if vals else "no reading"
    return text + (f" ({failed} could not be replayed)" if failed else "") \
        + (f" ({short} could not be set against twins)" if short else "")


def _years_ahead(r: dict) -> tuple[int, int]:
    years = [y for y in r.get("years") or [] if y.get("left") is not None]
    return sum(1 for y in years if y["left"] > 0), len(years)


def _subs(r: dict) -> list[tuple[str, list[dict]]]:
    """The replays either side of a config's own, by kind."""
    return [("halves of the coins", r["halves"]), ("nearby settings", r["nearby"]),
            ("phases of the clock", (r.get("clock") or {}).get("shifts") or [])]


def weak_spots(r: dict) -> list[str]:
    """Where a reading that beats most of its twins, with something left
    after costs, is thin."""
    out = []
    up, n = _years_ahead(r)
    if n and up * 2 <= n:
        out.append(f"ahead of its average twin after costs in only {up} of {n} years")
    last = (r.get("twins") or {}).get("beaten_last_365")
    if last is not None and last < NO_TIMING_BELOW:
        out.append(f"over the last 365 days it beats {'only ' if ' ' not in _share(last) else ''}{_share(last)} of its twins")
    dc = (r.get("double_costs") or {}).get("left_per_year")
    if dc is not None and dc <= 0:
        out.append("at double costs nothing is left")
    if not r["quick"]:
        for what, rows in _subs(r):
            up, n = _counts(rows)
            failed = sum(1 for x in rows if not x.get("ok"))
            if rows and not n:
                out.append(f"none of the {len(rows)} {what} could be set against twins")
            elif n and up * 2 <= n:
                out.append(f"only {up} of {n} {what} beat {HOLDS_UP:.0%} of their twins"
                           + (f" ({failed} of them could not be replayed at all)" if failed else ""))
            elif failed:
                out.append(f"{failed} of the {n} {what} could not be replayed")
    ro = r.get("rule_one") or {}
    none = (ro.get("windows") or {}).get("no_trade", ro.get("no_trade_by_first"))
    if none is not None and none >= 0.5:
        out.append(f"it finishes no trade of its own in {_share(none)} of {ro.get('first_days', 60)} day windows, so a live "
                   f"test would likely be killed at its look")
    return out


def _stay(sl: dict) -> tuple[str, str]:
    """The stay a reading's lead was taken from, as a clause and as a few words."""
    days, pair = sl.get("longest_hold_days") or 0.0, sl.get("longest_hold_pair") or "one pair"
    return f"it was never out of {pair} for {days:,.0f} days on end", f"never out of {pair} for {days:,.0f} days"


def no_twins_words(r: dict, short: bool = False) -> str:
    """Why a reading has no twins: in a sentence, or (short) in a few words
    for the one line. A book the bench cannot set against twins has not been
    shown to have no timing, and but for one that never held anything the
    words say so."""
    why, sl = r.get("no_twins"), r.get("slide") or {}
    if why == "idle":
        return "it never held a position" + ("" if short else ", so there is no timing to read.")
    if why == "hold":
        return (f"{_stay(sl)[1]}, too long for a run of {r['days']:,}" if short else
                f"{_stay(sl)[0]}, which leaves too little of a run of {r['days']:,} days to set it against twins. The bench "
                f"cannot read its timing; that is not to say it has none.")
    if why == "pairs":
        return (f"{_stay(sl)[1]}, too long for the history of the pairs it holds" if short else
                f"{_stay(sl)[0]}, and no pair it holds has prices for long enough to set such a book against twins. The "
                f"bench cannot read its timing; that is not to say it has none.")
    if why == "new":
        return ("the pairs it holds have too short a history" if short else
                "no pair it holds has prices for long enough to set a book against twins, so nothing is said of its timing.")
    return "too short a run" if short else "the run is too short to set a book against twins, so nothing is said of its timing."


def words(r: dict) -> str:
    """The reading in a sentence or two. An aid to reading the figures, not a
    rule: the lines it draws are NO_TIMING_BELOW, LUCK_ABOVE and HOLDS_UP."""
    tw = r.get("twins") or {}
    beaten, luck, worth = tw.get("beaten"), tw.get("chance"), tw.get("worth")
    if beaten is None:
        return "Reading: " + no_twins_words(r)
    if beaten < NO_TIMING_BELOW:
        return ("Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken "
                "at other times.")
    if luck is None or luck > LUCK_ABOVE:
        few = worth is not None and 1.0 / (worth + 1.0) > LUCK_ABOVE
        return ("Reading: cannot be told from luck. A book with no timing at all does as well "
                + _about(luck) + " of the time"
                + (f"; its twins are worth only about {worth:.0f} separate ones, and no book can stand out among so few. "
                   f"A longer run gives a slow book more of them; a book that keeps to the clock has only so many"
                   if few else "") + ".")
    timing, drift, left = r.get("timing_per_year"), r.get("drift_per_year"), r.get("left_per_year")
    if left is None or left <= 0:
        if timing is None or timing <= 0:
            return ("Reading: day by day it stands above most of its twins, and over the whole run its timing made no "
                    "more than its average twin did. What it lost or kept came from letting positions run and from "
                    "costs, not from when it traded.")
        if timing + (drift or 0.0) > 0:
            return ("Reading: its timing beats most of its twins, and its costs take more than the book made over its "
                    "average twin before them, so nothing is left. The costs are the thing to mend: fewer or larger "
                    "trades, not a new signal.")
        return ("Reading: as last traded it beats most of its twins, and before any costs the book itself made no "
                "more than they did: what its timing adds is lost again in letting positions run between trades.")
    weak = weak_spots(r)
    rest = " The halves of the coins and the nearby settings are not in a quick reading." if r["quick"] else ""
    if weak:
        return ("Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: "
                + "; ".join(weak) + "." + rest)
    twice = (r.get("double_costs") or {}).get("left_per_year") is not None
    also = [w for w, there in (("in most years", _years_ahead(r)[1] > 0), ("at double costs", twice)) if there]
    said = "Reading: it beats most of its twins, with something left after costs" + (", " + " and ".join(also) if also else "")
    if r["quick"]:
        return said + "." + rest
    held = [f"{up} of {n} {what}" for what, (up, n) in ((what, _counts(rows)) for what, rows in _subs(r)) if n]
    lacking = [w for w, rows in (("There were too few coins to halve.", r["halves"]),
                                 ("It has no settings to move.", r["nearby"])) if not rows]
    return (said + (f"; {_listed(held)} beat {HOLDS_UP:.0%} of their own twins or more" if held else "") + "."
            + "".join(" " + w for w in lacking) + " Worth a slot on this evidence, all of which is in sample.")


def _listed(items: list[str]) -> str:
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def ledger_line(r: dict) -> str:
    """The reading in one line, for a ledger entry."""
    tw = r.get("twins") or {}
    if tw.get("beaten") is None:
        return (f"Bench: {_pct(r['net'], 1)} after costs over {r['days']:,} days; not set against twins "
                f"({no_twins_words(r, short=True)}). In sample.")
    last, drift = tw.get("beaten_last_365"), r.get("drift_per_year") or 0.0
    parts = [f"timing {_pct(r['timing_per_year'], 1)} a year before costs over {r['days']:,} days, which beats "
             f"{_share(tw['beaten'])} of its twins" + ("" if last is None else f" ({_share(last)} of them over the last 365 days)")
             + ("" if tw.get("chance") is None else f", and a book with no timing does as well {_share(tw['chance'])} of the time"),
             f"letting positions run {'added' if drift >= 0 else 'took'} {_cost(abs(drift))} and costs took "
             f"{_cost(r['costs_per_year'])} a year, so {_pct(r['left_per_year'], 1)} is left "
             f"(Sharpe {_num(r['sharpe'])}, t {_num(r['t'], 1)})"]
    up, n = _years_ahead(r)
    if n:
        parts.append(f"ahead after costs in {up} of {n} years")
    if not r["quick"]:
        parts.append(f"nearby settings beat {_spread(r['nearby'])} of their twins")
        parts.append(f"halves of the coins {_spread(r['halves'])}")
    return "Bench: " + "; ".join(parts) + ". In sample."


def _d(days: float) -> str:
    """A length in days: to a tenth of one where it is not whole, so that the days in a sentence add up as written."""
    return f"{days:,.0f}" if abs(days - round(days)) < 0.05 else f"{days:,.1f}"


def _why_none(r: dict) -> str:
    """Why this reading has no twins, with the days that go into it."""
    sl, why = r["slide"], r.get("no_twins")
    candles, least = sl["candles_days"], sl["least_days"]
    drawn = f"{MIN_SLIDE_DAYS} days to slide it by and {MIN_ROOM_DAYS} more to draw the slides from"
    history = sl.get("history_days") or 0.0
    if why == "idle":
        return "the book never held a position"
    # What there is falls short of what it takes by hours, and both are given in days: where the two would read the
    # same, the words say that it is short and not by how much (a run of 122 days against the 122 it takes)
    if why in ("hold", "pairs"):
        has = ((f"the run is {r['days']:,}" if r["days"] < round(least) else "the run is a few hours short of that")
               if why == "hold" else
               f"no pair it holds has prices for more than {history:,.0f}" if round(history) < round(least) else
               "no pair it holds has prices for quite that long")
        return (f"{_stay(sl)[0]}. A strategy that is told what it holds can carry what it has seen for as long as it "
                f"stays in a pair, so a twin may not hold what the book took within that long after the hour in hand, "
                f"nor within the {_d(candles)} days of candles a strategy is handed. With {drawn}, sliding it takes "
                f"{least:,.0f} days, and {has}. The bench cannot read this book's timing; that is not to say it has none")
    any_book = MIN_SLIDE_DAYS + MIN_ROOM_DAYS + 2 * candles      # what it takes for a book that stays in nothing for long
    takes = (f"That takes {drawn}, and twice the {_d(candles)} days of candles a strategy is handed, {_d(any_book)} days "
             f"in all")
    if why == "new":
        return (f"no pair the book holds has prices for long enough to slide a book inside. {takes}, and "
                + (f"none of them has more than {history:,.0f}" if round(history) < round(any_book) else
                   "none of them has quite that many"))
    return (f"the run is too short to slide a book inside. {takes}, and the run is "
            + (f"{r['days']:,} days" if r["days"] < round(any_book) else "a few hours short of that"))


def format_reading(r: dict) -> str:
    tw, ro, dc, tl, sl = r.get("twins") or {}, r["rule_one"], r.get("double_costs") or {}, r.get("tails") or {}, r["slide"]
    lines = [f"bench: {r['hypothesis']} ({r['strategy']}), {r['days']:,} days from {r['start']} to {r['end']}, "
             f"{len(r['pairs'])} pairs",
             f"  what it made: {_pct(r['net'], 1)} after costs, with {r['exposure']:.2f} of its equity invested on "
             f"average. The basket (the pairs in equal parts) made {_pct(r['basket'], 1)}"
             + ("" if tw.get("net_middle") is None else
                f", and the middle one of its twins {_pct(tw['net_middle'], 1)} after the same costs")]
    if tw.get("beaten") is not None:
        last, still, drift = tw.get("beaten_last_365"), tw.get("in_place") or [], r["drift_per_year"]
        lines.append(f"  twins: before costs it beats {_share(tw['beaten'])} of {tw['n']:,} twins over the whole run"
                     + ("" if last is None else f" and {_share(last)} over the last 365 days")
                     + f". A twin is the same book slid {MIN_SLIDE_DAYS} days or more later: the same positions on the "
                       f"same coins for as long, with nothing left of when they were taken. A book with no timing beats "
                       f"about half"
                     + ("" if tw.get("chance") is None else
                        f". Twins slid a few days apart are nearly one book: these are worth about {tw['worth']:.0f} separate "
                        f"ones, and among that many a book with no timing does as well as this {_about(tw['chance'])} "
                        f"of the time")
                     + f". No twin holds what the book took in the {sl['lead_days']:,.0f} days after the hour in hand: "
                       f"the {sl['candles_days']:.0f} days of candles a strategy is handed, and then "
                     + f"the longest it was in any one pair ({sl['longest_hold_days']:,.0f} days, {sl.get('longest_hold_pair')})"
                     + " or as long again as the candles, whichever is longer"
                     + ("" if sl["least_days"] * 4 <= r["days"] * 3 else
                        f". Sliding this book takes {sl['least_days']:,.0f} days of the run's {r['days']:,}: on a run "
                        f"so little longer than that, the books that can be set against twins at all are the ones that "
                        f"let go of their positions early, which is not a fair draw of them, and the share says less "
                        f"than it would on a longer one")
                     + ("" if not still else
                        f". Not slid: {', '.join(still)}, whose prices cover too short a stretch to slide a book inside. "
                        f"Those positions are the same in every twin, so their timing is neither counted nor tested"))
        lines.append(f"  what the timing is worth: {_pct(r['timing_per_year'], 1)} a year before costs, the book as it "
                     f"last traded each pair less its average twin. Letting positions run between trades, which a twin "
                     f"does not, {'added' if drift >= 0 else 'took'} {_cost(abs(drift))}. Costs take "
                     f"{_cost(r['costs_per_year'])} a year, so {_pct(r['left_per_year'], 1)} a year is left: a yearly "
                     f"Sharpe ratio of {_num(r['sharpe'])} and a t of {_num(r['t'], 1)}, where a t under about 2 either "
                     f"way cannot be told from noise. At double costs {_pct(dc.get('left_per_year'), 1)} is left")
    else:
        lines.append("  twins: none. " + _why_none(r)[0].upper() + _why_none(r)[1:])
    if r["years"]:
        timed = any(y.get("timing") is not None for y in r["years"])
        lines.append(("  by year (timing before costs, what is left after them, the basket, twins beaten): " if timed
                      else "  by year (what it made, the basket): ") + "; ".join(
            f"{y['year']}{'' if y['days'] >= 300 else f' ({y_days(y)})'} "
            + (f"{_pct(y['timing'], 1)}, {_pct(y['left'], 1)}, {_pct(y['basket'])}, {_share(y['twins_beaten'])}" if timed
               else f"{_pct(y['net'], 1)}, {_pct(y['basket'])}") for y in r["years"]))
    if tl.get("days"):
        lines.append(f"  its best and worst days: of what is left, its {tl['days']} best days carry "
                     f"{_pct(tl['best'], 1)} a year and its {tl['days']} worst {_pct(tl['worst'], 1)}")
    if not r["quick"]:
        own = "" if tw.get("beaten") is None else f", against its own {_share(tw['beaten'])}"
        lines.append(f"  half the coins (twins beaten on each half, halved two ways): {_spread(r['halves'])}")
        lines.append(f"  nearby settings (twins beaten with every number in params moved by up to {NEARBY_SPREAD:.0%}): "
                     f"{_spread(r['nearby'])}{own}")
        clock = r.get("clock") or {}
        if clock.get("why"):
            lines.append(f"  the clock: {clock['why']}. With the clock moved (by {', '.join(str(h) for h in CLOCK_SHIFTS_H)} "
                         f"hours) it beats {_spread(clock.get('shifts') or [])} of its twins{own}")
        else:
            lines.append(f"  the clock: nothing in its code names it, and its targets do not move with it (asked at "
                         f"{PROBE_HOURS} hours of the history, with the clock moved three ways)")
    first, total = ro["first_days"], ro["total_days"]
    none, later = ro.get("no_trade_by_first"), ro.get("no_trade_by_total")
    lines.append(f"  under rule 1: about {ro['fills_by_first']:.0f} fills in {first} days (a promotion needs "
                 f"{ro['min_fills']})"
                 + ("" if none is None else f"; it finished a trade of its own in every {first} day window" if none <= 0
                    else f"; in {_share(none)} of {first} day windows it finished no trade of its own, and a test that "
                         f"began in one of those is killed at its look"
                         + ("" if later is None else f" ({_share(later)} of {total} day windows)")))
    lk = ro.get("windows")
    if lk:
        lines.append(f"  had a test begun on each day from a year into the run ({lk['windows']:,} windows of {total} "
                     f"days, which overlap: about {lk['apart']} fit end to end): its daily skill t, as the live rule "
                     f"takes it, was {ro['min_t']:.1f} or more at day {total} in {_share(lk['t_reached'])} of them"
                     + ("" if lk.get("t_middle") is None else f" (the middle one: {_num(lk['t_middle'], 1)})")
                     + f", and it had all three counts a promotion asks for (a trade of its own by day {first}, "
                       f"{ro['min_fills']} fills, that t) in {_share(lk['all_counts'])}"
                     + ("" if lk.get("fast_pass") is None else f"; a fast pass at day {first} in {_share(lk['fast_pass'])}"))
    if sl.get("wrote_params"):
        lines.append("  NOTE: the strategy's params were not, at the end of the run, as they were handed to it. Live it is "
                     "handed them afresh every hour, so what it kept there it would not have: if it decides on that, this "
                     "replay is not what it would do")
    gap = r.get("rebuilt_within_bps")
    if gap is None or not gap <= 0.01:
        lines.append("  FAULT: the hour by hour record does not rebuild the engine's own daily returns ("
                     + ("it has a hole in it" if gap is None or not math.isfinite(gap) else f"it is off by {gap:.2f} bps at the worst")
                     + "). The figures above cannot be relied on until that is found")
    lines.append("  " + words(r))
    lines.append("  " + ledger_line(r))
    return "\n".join(lines)


def y_days(y: dict) -> str:
    return f"{y['days']} days"


def format_league(readings: list[tuple[str, dict]]) -> str:
    wide = max([28] + [len(label) for label, _ in readings])
    head = (f"{'config':<{wide}} {'days':>6} {'net':>8} {'timing/yr':>10} {'run/yr':>7} {'costs/yr':>9} {'left/yr':>8} "
            f"{'t':>6} {'twins':>6} {'luck':>5} {'last 365':>9} {'read on':>11}")
    rows = [head]
    for label, r in readings:
        tw = r.get("twins") or {}
        rows.append(f"{label:<{wide}} {r['days']:>6,} {_pct(r['net'], 1):>8} {_pct(r['timing_per_year'], 1):>10} "
                    f"{_pct(r['drift_per_year'], 1):>7} {_cost(r['costs_per_year']):>9} {_pct(r['left_per_year'], 1):>8} "
                    f"{_num(r['t'], 1):>6} {_share(tw.get('beaten'), True):>6} {_share(tw.get('chance'), True):>5} "
                    f"{_share(tw.get('beaten_last_365'), True):>9} {_date(int(r['made_at'])):>11}")
    if not readings:
        return "\n".join(rows + ["no reading"])
    r0 = readings[0][1]
    rows.append(f"Each config is read from the first hour it could decide to the end of the history on file when it was "
                f"read; days is how long that is. Over the first row's {r0['days']:,} days the basket made "
                f"{_pct(r0['basket'], 1)}. net: what the config made after costs. timing/yr: the book as it last traded "
                f"each pair, less its average twin, before costs, a year. run/yr: what letting positions run between "
                f"trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less "
                f"costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the "
                f"share of its twins it beats before costs (a book with no timing beats about half), over the whole run "
                f"and over the last 365 days. luck: how often a book with no timing does as well among its twins as "
                f"this one did; over {LUCK_ABOVE:.0%}, it cannot be told from luck. n/a: the book could not be set "
                f"against twins. In sample, all of it.")
    return "\n".join(rows)


# --- saved readings ----------------------------------------------------------

def bench_dir():
    return config.STATE / "bench"


def _plain_name(name) -> bool:
    return isinstance(name, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,39}", name) is not None


def saved(hyp) -> dict | None:
    """The reading on file for a hypothesis, or None when there is none or it
    cannot be read (it is then simply taken again)."""
    if not _plain_name(hyp):
        return None
    p = bench_dir() / f"{hyp}.json"
    try:
        rec = json.loads(p.read_text()) if p.exists() else None
        return rec if isinstance(rec, dict) else None
    except Exception:  # noqa: BLE001
        return None


def describes(rec: dict | None, cfg: dict, rcfg: dict) -> bool:
    """Is a saved reading one of this config, on this code and these costs?"""
    try:
        return bool(rec) and rec.get("signature") == signature(cfg, rcfg) and rec.get("version") == VERSION
    except Exception:  # noqa: BLE001
        return False


def current(rec: dict | None, cfg: dict, rcfg: dict, quick: bool, now: int | None = None) -> bool:
    """Is a saved reading still good: of this config, code and costs, taken in
    the last week, and whole unless only a quick one is wanted?"""
    now = int(time.time()) if now is None else int(now)
    try:
        return describes(rec, cfg, rcfg) and 0 <= now - int(rec.get("made_at", 0)) < STALE_AFTER_S \
            and (quick or not rec.get("quick"))
    except (TypeError, ValueError, OverflowError):
        return False


def save(r: dict) -> None:
    """Keep a reading under its hypothesis's name. A name that is not a plain
    one is refused: it comes from a config file, and it becomes a file name."""
    name = r.get("hypothesis")
    if not _plain_name(name):
        raise ValueError(f"a reading for hypothesis {name!r} is not kept: that is not a name a file can safely have")
    d = bench_dir()
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{name}.json").write_text(json.dumps(_plain(r), indent=1, sort_keys=True) + "\n")


def _plain(x):
    """A reading as plain JSON anywhere: numpy numbers as Python's, what is
    not a number (NaN, infinity) as null, and anything else a config can hold
    (YAML reads `2024-01-01` as a date) as its text."""
    if isinstance(x, dict):
        return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, np.ndarray)):
        return [_plain(v) for v in x]
    if x is None or isinstance(x, str):
        return x
    if isinstance(x, (np.bool_, bool)):
        return bool(x)
    if isinstance(x, (int, np.integer)):
        return int(x)
    if isinstance(x, (float, np.floating)):
        return float(x) if math.isfinite(float(x)) else None
    return str(x)


def _line(text: str) -> str:
    """A message as one line, with nothing of where the checkout happens to be: it goes into a table that is
    committed, and an error from a config file comes as several lines with the machine's own paths in them."""
    return " ".join(str(text).replace(str(config.ROOT) + os.sep, "").replace(str(config.ROOT), ".").split())


def _shows(label: str, r: dict) -> bool:
    """Can this reading be put into words? One on file that cannot (cut
    short, or mended by hand) is not current, whatever else it says."""
    try:
        format_reading(r), format_league([(label, r)])
        return True
    except Exception:  # noqa: BLE001
        return False


def configs_in_use() -> tuple[list[tuple[str, dict]], list[str]]:
    """The champion and every slot that holds a test, once each, and what is
    wrong with the configs that could not be taken: one that cannot be read,
    and two different ones under one hypothesis name (their readings would be
    kept in one file, each night's over the other's). A slot with the
    champion's own strategy and params is idle and is not a second config; a
    slot whose file the hourly loop has not made yet is idle too."""
    out, problems, seen, named = [], [], set(), {}
    try:
        names = [config.CHAMPION] + config.challengers()
    except Exception as e:  # noqa: BLE001
        names, problems = [config.CHAMPION], [_line(str(e))]
    for name in names:
        if name != config.CHAMPION and not (config.CONFIGS / f"{name}.yaml").exists():
            continue
        try:
            cfg = config.account_cfg(name)
            sig = config.strategy_signature(cfg)
        except Exception as e:  # noqa: BLE001
            problems.append(_line(f"configs/{name}.yaml cannot be read ({e})"))
            continue
        if sig in seen:
            continue
        seen.add(sig)
        hyp = str(cfg["hypothesis"])
        if hyp in named:
            problems.append(f"configs/{name}.yaml and configs/{named[hyp]}.yaml are different configs under one "
                            f"hypothesis name, {hyp}; only the first is read")
            continue
        named[hyp] = name
        out.append((f"{hyp} {cfg['strategy']}" + (" (champion)" if name == config.CHAMPION else ""), cfg))
    return out, problems


def write_table(use: list[tuple[str, dict]], taken: dict[int, dict], problems: list[str], rcfg: dict,
                now: int | None = None) -> None:
    """state/bench/README.md: the league table, what could not be read, and
    each config's whole reading. Written at the start of a run and after each
    reading, so it is never a table from before a run that died part way.
    Every row says the day it was read on. A config that could not be read
    this time is shown as it was last read only if that reading is of the
    config as it now is; otherwise it has a line saying there is none. The
    file is left alone when nothing under its heading would change."""
    now = int(time.time()) if now is None else int(now)
    shown, missing = [], []
    for i, (label, cfg) in enumerate(use):
        r = taken.get(i)
        if r is None:
            rec = saved(cfg.get("hypothesis"))
            r = rec if describes(rec, cfg, rcfg) and _shows(label, rec) else None
        if r is None:
            missing.append(label)
        else:
            shown.append((label, r))
    head = ("# The bench's league table\n\nLast changed on "
            f"{datetime.fromtimestamp(now, timezone.utc).strftime('%Y-%m-%d at %H:%M UTC')}. The bench workflow (`python -m "
            "bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row "
            "says the day it was read on. bot/bench.py says how each figure is made.\n")
    text = "\n```\n" + format_league(shown) + "\n```\n"
    if missing or problems:
        text += "\n## Not read\n\n" + "".join(f"- {label}: no reading on file of this config as it now is\n" for label in missing) \
            + "".join(f"- FAILED: {p}\n" for p in problems)
    text += "".join("\n```\n" + format_reading(r) + "\n```\n" for _, r in shown)
    bench_dir().mkdir(parents=True, exist_ok=True)
    table = bench_dir() / "README.md"
    try:
        was = table.read_text() if table.exists() else ""
    except Exception:  # noqa: BLE001
        was = ""
    if was.startswith("# The bench's league table\n") and was.partition("\n```\n")[1:] == ("\n```\n", text[5:]):
        return          # nothing under the heading has changed: a table that differed only in when it was written
    table.write_text(head + text)       # would be a commit every night for the life of the repo (found in review, 2026-10-07)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="What a strategy shows on history, set against its own twins.")
    ap.add_argument("--config", help="a config file, for one reading")
    ap.add_argument("--all", action="store_true", help="the champion and every slot, side by side")
    ap.add_argument("--quick", action="store_true", help="the replay and its twins only")
    ap.add_argument("--days", type=int, default=None,
                    help="only the last N days of history (default: all of it). For trying things out: on a run of a "
                         "year or two the books that can be set against twins are the ones that let go of their "
                         "positions early, which is not a fair draw, so go by the whole history")
    ap.add_argument("--jobs", type=int, default=None, help="replays to run at once (default: one per processor)")
    ap.add_argument("--json", action="store_true", help="print the readings as JSON; what is said along the way goes to stderr")
    ap.add_argument("--save", action="store_true",
                    help="with --all: keep each reading under state/bench/, and take only those that are missing or "
                         "stale. Only the bench workflow uses this: a pull request may not change state/")
    ap.add_argument("--again", action="store_true", help="with --save: take every reading again")
    ap.add_argument("--minutes", type=float, default=None,
                    help="stop after this long: what is running is ended, what was read is kept, and the exit code says so")
    args = ap.parse_args(argv)
    if bool(args.config) == bool(args.all):
        ap.error("give --config <file> or --all")
    if args.save and not args.all:
        ap.error("--save goes with --all: one config's reading is printed, not kept")
    if args.save and args.days:
        ap.error("--save keeps readings of all the history on file, so it does not go with --days")
    if args.again and not args.save:
        ap.error("--again goes with --save")

    def say(text: str) -> None:
        print(text, file=sys.stderr if args.json else sys.stdout, flush=True)

    deadline = None if args.minutes is None else time.time() + float(args.minutes) * 60.0
    rcfg = config.risk_cfg()
    candles = backtest.load_cached_candles(list(rcfg["pairs"]))
    if args.config:
        try:
            cfg = config.load_yaml(config.ROOT / args.config)
            for key in ("strategy", "params"):
                if key not in cfg:
                    raise ValueError(f"{args.config} is missing {key!r}")
            r = read_many([cfg], rcfg, candles, days=args.days, quick=args.quick, jobs=args.jobs, deadline=deadline)[0]
            if "failed" in r:
                raise RuntimeError(r["failed"])
            text = json.dumps(_plain(r), indent=1, sort_keys=True) if args.json else format_reading(_plain(r))
        except Exception as e:  # noqa: BLE001
            say(_line(f"[bench] FAILED: {args.config}: {e}"))
            return 1
        print(text)
        return 0
    use, problems = configs_in_use()
    for p in problems:
        say(f"[bench] FAILED: {p}")
    taken: dict[int, dict] = {}
    todo = []
    for i, (label, cfg) in enumerate(use):
        rec = saved(cfg["hypothesis"]) if args.save else None
        if args.save and not args.again and current(rec, cfg, rcfg, args.quick) and _shows(label, rec):
            say(f"[bench] {label}: the saved reading is current")
            taken[i] = rec
        else:
            todo.append(i)
    if args.save:
        write_table(use, taken, problems, rcfg)
    # Quick readings are one replay each and share the processors. A whole reading is a dozen replays and
    # fills them by itself, so those are taken one config at a time, and each is kept and the table written
    # again as soon as it is done: a job that is stopped part way has lost one reading, not the night's work.
    for group in ([todo] if args.quick else [[i] for i in todo]):
        if not group:
            continue
        if deadline is not None and time.time() >= deadline:
            fresh = [{"failed": STOPPED} for _ in group]
        else:
            try:
                fresh = read_many([use[i][1] for i in group], rcfg, candles, days=args.days, quick=args.quick,
                                  jobs=args.jobs, deadline=deadline)
            except Exception as e:  # noqa: BLE001 - whatever went wrong cost these readings and no others
                fresh = [{"failed": f"the bench itself failed ({type(e).__name__}: {e})"} for _ in group]
        for i, r in zip(group, fresh):
            label = use[i][0]
            try:
                if "failed" in r:
                    raise RuntimeError(r["failed"])
                r = _plain(r)
                if not _shows(label, r):
                    raise RuntimeError("its reading cannot be put into words; that is a fault in bot/bench.py")
                if args.save:
                    save(r)
                taken[i] = r
                say(f"[bench] {label}: read, {r['took_s']:.0f} s of replays")
            except Exception as e:  # noqa: BLE001
                problems.append(_line(f"{label}: {e}"))
                say(f"[bench] FAILED: {problems[-1]}")
        if args.save:
            write_table(use, taken, problems, rcfg)
    readings = [(use[i][0], taken[i]) for i in sorted(taken)]
    if args.json:
        print(json.dumps({"readings": [{"label": label, **r} for label, r in readings], "problems": problems},
                         indent=1, sort_keys=True))
    elif readings:
        print(format_league(readings))
    if not readings:
        say("[bench] FAILED: no reading was taken this time"
            + (", and none on file is current (state/bench/README.md shows the older ones that still describe "
               "their configs)" if args.save else ""))
        return 1
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
