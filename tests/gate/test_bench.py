"""PROTECTED. The bench (bot/bench.py): what a strategy shows on history, set against its own twins.

The figures the bench prints decide which ideas get a slot, so each one is held here to a case
whose answer is known beforehand: a book made by hand, a strategy that sees the next hour, one
that is blind, one that decides on the past of a market with no memory, one that reads the clock."""
import json
import math
import multiprocessing
import os
import re
import subprocess
import sys
import threading
import time
import types
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from bot import backtest, bench, config, data, strategy

REPO = Path(__file__).resolve().parents[2]
T0 = 1_750_000_000 // 86400 * 86400            # a UTC midnight
HOUR, DAY = 3600, 86400
RCFG = {"fee_bps": 10, "slippage_bps": 5, "impact_bps": 2, "initial_cash": 10_000, "pairs": ["AAA", "BBB", "CCC", "DDD"],
        "history_hours": 200, "max_weight_per_pair": 0.25, "max_gross_weight": 1.0, "min_trade_notional": 50,
        "rebalance_threshold": 0.05, "daily_loss_halt": 0.05, "max_fills_per_pair_per_day": 4, "ruleset": 7,
        "challenger": {"slots": 2}}
FORKS = "fork" in multiprocessing.get_all_start_methods()


# --- books made by hand --------------------------------------------------------------------

def path_of(w, r, c=None, start=T0, starved=0, late=None, holes=None, gone=None, memory=24, runs=False):
    """A recorded run built from the sum the bench says holds: equity moves by sum(w * r) and then
    pays c. w: hours x pairs, the share in each pair after each hour's fills. r: one row fewer, each
    pair's move to the next hour. c: the costs of each hour's fills as a share of equity. late:
    {column: hours}, a pair with no price for its first hours. holes: {column: (from, to)}, hours in
    which a pair nobody holds has no price. gone: {column: hour}, a pair with no price from that hour
    on. memory: the hours of candles the strategy was handed. runs: w is what the book trades a pair
    to in the hours w changes; between those it keeps its coins, so the weight on record moves with
    the price, as an account's does."""
    w, r = np.array(w, dtype=float), np.asarray(r, dtype=float)
    hours, pairs = w.shape
    assert r.shape == (hours - 1, pairs)
    c = np.zeros(hours) if c is None else np.asarray(c, dtype=float)
    opens = np.vstack([np.full(pairs, 100.0), 100.0 * np.cumprod(1.0 + r, axis=0)])
    eq, costs = np.empty(hours), np.empty(hours)
    eq[0], costs[0] = 10_000.0 * (1.0 - c[0]), 10_000.0 * c[0]
    wanted = w.copy()
    for t in range(hours - 1):
        before = eq[t] * (1.0 + float((w[t] * r[t]).sum()))
        paid = before * c[t + 1]
        eq[t + 1], costs[t + 1] = before - paid, costs[t] + paid
        if runs:
            kept = w[t] * (1.0 + r[t]) * eq[t] / eq[t + 1]
            w[t + 1] = np.where(wanted[t + 1] == wanted[t], kept, wanted[t + 1])
    for col, n in (late or {}).items():
        assert not w[:n, col].any(), "a pair is not held before it has a price"
        opens[:n, col] = np.nan
    for col, (a, b) in (holes or {}).items():
        assert not w[max(a - 1, 0): b + 1, col].any(), "a held pair always has a price in the record"
        opens[a:b, col] = np.nan
    for col, n in (gone or {}).items():
        assert not w[n - 1:, col].any(), "a pair is not held once its prices have stopped"
        opens[n:, col] = np.nan
    return {"pairs": [f"P{i}" for i in range(pairs)], "ts": start + HOUR * np.arange(hours), "equity": eq, "costs": costs,
            "fills": (c > 0).astype("int64"), "starved": np.arange(hours) < starved, "weights": w, "opens": opens,
            "memory_hours": memory, "errors": 0, "first_error": None}


def market(hours, pairs=3, seed=1, vol=0.01):
    return np.random.default_rng(seed).normal(0.0, vol, (hours - 1, pairs))


def blind_book(hours, pairs, seed):
    """Positions that know nothing of the market: each pair is held or not for stretches of a day or
    two, and every change is paid for."""
    rng = np.random.default_rng(seed)
    w = np.zeros((hours, pairs))
    for p in range(pairs):
        t, on = 0, bool(rng.integers(0, 2))
        while t < hours:
            run = int(rng.integers(12, 72))
            w[t: t + run, p] = (1.0 / pairs) if on else 0.0
            t, on = t + run, not on
    c = np.r_[0.0, np.abs(np.diff(w, axis=0)).sum(axis=1) * 0.0015]
    return w, c


def longest_hold(w):
    """The longest run of hours any one pair is held for, counted the slow way."""
    best = 0
    for col in np.asarray(w).T:
        run = 0
        for x in col:
            run = run + 1 if x > 0 else 0
            best = max(best, run)
    return best


def by_days(s, hourly):
    """An hourly series compounded day by day, the long way round."""
    edges = list(s["starts"]) + [len(hourly)]
    return np.array([np.prod(1.0 + hourly[a:b]) - 1.0 for a, b in zip(edges[:-1], edges[1:])])


def t_of(x):
    return x.mean() / (x.std(ddof=1) / math.sqrt(len(x)))


def test_a_days_return_is_the_books_hours_compounded_and_the_record_rebuilds_it():
    hours = 24 * 5
    r = market(hours)
    w = np.tile([0.2, 0.3, 0.0], (hours, 1))
    w[48:96] = [0.0, 0.5, 0.25]
    c = np.zeros(hours)
    c[25] = c[48] = c[96] = 0.002
    path = path_of(w, r, c)
    s = bench.series(path)
    eq = path["equity"]
    by_hand = [eq[min(24 * (d + 1), hours - 1)] / eq[24 * d] - 1.0 for d in range(5)]
    assert s["daily"] == pytest.approx(by_hand, abs=1e-12) and len(s["daily"]) == 5
    assert s["gap_bps"] < 1e-6                                          # the hour by hour sum is the engine's own equity
    assert s["gross"] == pytest.approx(by_days(s, (w[:-1] * r).sum(axis=1)), abs=1e-12)        # the same days with nothing paid
    assert s["exposure"] == pytest.approx(w[:-1].sum(axis=1).mean())
    assert s["exposure_daily"] == pytest.approx([w[:-1].sum(axis=1)[24 * d: 24 * (d + 1)].mean() for d in range(5)])
    assert list(s["days"]) == [T0 // DAY + d for d in range(5)]
    # The costs are those of the fills at the end of each hour, as a share of equity, and so are the fills: what is
    # filled in a day's first step ended the hour before it, and belongs to the day before
    assert s["c"][24] == pytest.approx(0.002) and s["c"][47] == pytest.approx(0.002) and s["c"][95] == pytest.approx(0.002)
    assert s["c"].sum() == pytest.approx(0.006) and list(s["fills"]) == [0, 2, 0, 1, 0] and s["memory"] == 24
    reading = bench.reading_of(s, None)
    assert reading["net"] == pytest.approx(eq[-1] / eq[0] - 1.0) and reading["rebuilt_within_bps"] < 1e-6
    # what the costs took is the gap between the days before costs and the days after, a year
    assert reading["costs_per_year"] == pytest.approx((s["gross"] - s["daily"]).sum() / 5 * 365)
    assert reading["costs_per_year"] == pytest.approx(0.006 / 5 * 365, rel=0.02)
    assert reading["start"] == "2025-06-15" and reading["end"] == "2025-06-19" and reading["days"] == 5
    assert reading["twins"] is None and reading["timing_per_year"] is None and reading["left_per_year"] is None
    # the longest it was in any one pair: the second pair, all through; and five days is no run to slide a book inside
    assert s["hold"] == hours - 1 and s["hold_pair"] == "P1" and reading["no_twins"] == "short"
    assert reading["slide"] == {"candles_days": 1.0, "longest_hold_days": pytest.approx((hours - 1) / 24), "longest_hold_pair": "P1",
                                "wrote_params": False, "lead_days": pytest.approx((24 + hours - 1) / 24),
                                "least_days": pytest.approx(30 + 90 + (24 + hours - 1) / 24), "history_days": pytest.approx((hours - 1) / 24)}
    short_holds = w.copy()
    short_holds[60:70, 1] = 0.0
    assert bench.series(path_of(short_holds, r, c))["hold"] == 60          # the first pair until hour 48 is shorter than the second until hour 60
    assert len(s["ts"]) == len(s["c"]) == len(s["hourly"]) == hours - 1
    never = bench.series(path_of(np.zeros((hours, 3)), r))
    assert never["hold"] == 0 and never["hold_pair"] is None and bench.reading_of(never, None)["slide"]["history_days"] == 0.0
    # the day a reading begins on is that of its first hour, and the day it ends on that of the end of its last
    late_start = bench.reading_of(bench.series(path_of(w, r, c, start=T0 + 23 * HOUR)), None)
    assert late_start["start"] == "2025-06-15" and late_start["end"] == "2025-06-20"
    to_midnight = bench.reading_of(bench.series(path_of(np.tile([0.2, 0.3, 0.0], (hours + 1, 1)), market(hours + 1))), None)
    assert to_midnight["start"] == "2025-06-15" and to_midnight["end"] == "2025-06-20" and reading["end"] == "2025-06-19"
    # a run that ends an hour into a day has that day, one hour long
    longer = 24 * 5 + 2
    r6, w6 = market(longer, seed=4), np.tile([0.2, 0.3, 0.0], (longer, 1))
    s6 = bench.series(path_of(w6, r6))
    assert list(s6["days"]) == [T0 // DAY + d for d in range(6)] and list(np.diff(np.r_[s6["starts"], len(s6["c"])])) == [24] * 5 + [1]
    assert s6["daily"][-1] == pytest.approx(float((w6[120] * r6[120]).sum()), abs=1e-12) and s6["exposure_daily"][-1] == pytest.approx(0.5)
    assert bench.reading_of(s6, None)["end"] == "2025-06-20" and bench.reading_of(s6, None)["days"] == 6


def test_the_basket_is_the_pairs_in_equal_parts_set_back_each_day():
    hours = 24 * 3 + 1
    r = np.zeros((hours - 1, 2))
    r[:, 0] = 0.001                                                      # one pair gains a tenth of a percent an hour, the other stands still
    s = bench.series(path_of(np.zeros((hours, 2)), r))
    one_day = 1.001 ** 24 - 1.0
    assert s["basket"] == pytest.approx([one_day / 2] * 3)               # not compounded across days as a held basket would be
    assert bench.reading_of(s, None)["basket"] == pytest.approx((1 + one_day / 2) ** 3 - 1)


def test_a_pair_is_in_the_basket_and_within_a_twins_reach_only_while_it_has_a_price():
    """Three pairs: one with prices throughout, one listed two days in, one whose prices stop a day
    before the end. Each is in the basket from its first price to its last, and those are the hours a
    twin can hold it in."""
    hours = 24 * 4 + 1
    r = np.zeros((hours - 1, 3))
    r[:, 0], r[:, 1], r[:, 2] = 0.001, -0.002, 0.0005
    w = np.full((hours, 3), 0.25)
    w[:48, 1] = 0.0
    w[71:, 2] = 0.0
    s = bench.series(path_of(w, r, late={1: 48}, gone={2: 72}))
    one, other, third = 1.001 ** 24 - 1.0, 0.998 ** 24 - 1.0, 1.0005 ** 24 - 1.0
    assert s["basket"][:2] == pytest.approx([(one + third) / 2] * 2)     # the second pair is not listed yet
    assert s["basket"][2] == pytest.approx((one + other + (1.0005 ** 23 - 1.0)) / 3)       # the third has its last price at hour 71
    assert s["basket"][3] == pytest.approx((one + other) / 2)            # and is out of the basket after it, not carried at nothing
    assert not s["valid"][:48, 1].any() and s["valid"][48:, 1].all() and s["valid"][:, 0].all()
    assert s["valid"][:71, 2].all() and not s["valid"][71:, 2].any()
    assert s["w"][:48, 1].sum() == 0.0 and s["w"][48:, 1] == pytest.approx(0.25) and s["w"][71:, 2].sum() == 0.0
    assert [(a, b) for (a, b), _, _ in s["stretches"]] == [(0, 71), (0, 96), (48, 96)]     # each pair's own stretch
    assert s["stretch_pairs"] == [["P2"], ["P0"], ["P1"]]
    assert [blk.shape for _, blk, _ in s["stretches"]] == [(71, 1), (96, 1), (48, 1)]
    assert s["gap_bps"] < 1e-6 and [bool(x) for x in s["listed"][2]] == [True, True, True]
    assert [bool(x) for x in s["listed"][0]] == [True, False, True] and [bool(x) for x in s["listed"][3]] == [True, True, False]
    # a pair with one price in the whole record, at its first step or at its last, has no hour it can be held in: it is in
    # no day's basket and has no stretch
    for only_at in (0, hours - 1):
        once = path_of(np.tile([0.25, 0.0], (hours, 1)), r[:, :2])
        once["opens"][:, 1] = np.nan
        once["opens"][only_at, 1] = 100.0
        lone = bench.series(once)
        assert not lone["valid"][:, 1].any() and not lone["listed"][:, 1].any() and lone["basket"] == pytest.approx([one] * 4), only_at
        assert [(a, b) for (a, b), _, _ in lone["stretches"]] == [(0, hours - 1)] and lone["stretch_pairs"] == [["P0"]]
    # on a day when no pair has a price at all, the basket made nothing
    empty = bench.series(path_of(np.zeros((hours, 2)), r[:, :2], gone={0: 24}, late={1: 72}))
    assert empty["basket"][1:3].tolist() == [0.0, 0.0] and not empty["listed"][1:3].any() and empty["basket"][0] > 0 > empty["basket"][3]
    # and a price is a price however small: a coin at a tenth of a cent is read as it would be at a hundred dollars
    cheap = path_of(w, r, late={1: 48}, gone={2: 72})
    cheap["opens"][:, 0] *= 1e-5
    small = bench.series(cheap)
    assert small["r"] == pytest.approx(s["r"], abs=1e-12) and (small["valid"] == s["valid"]).all() and small["w"] == pytest.approx(s["w"], abs=1e-12)
    assert small["basket"] == pytest.approx(s["basket"], abs=1e-12) and small["gap_bps"] < 1e-6 and len(small["stretches"]) == 3


def test_a_pair_with_hours_missing_keeps_its_whole_move_in_the_basket():
    """A pair nobody holds has no candle for five hours and comes back 8% higher. The basket had it all
    along: the move belongs to the day it comes back in, and is not lost."""
    hours = 24 * 2 + 1
    r = np.zeros((hours - 1, 2))
    r[:, 0] = 0.0002
    r[9, 1] = 0.08                                                        # the jump, inside the hole
    s = bench.series(path_of(np.zeros((hours, 2)), r, holes={1: (8, 13)}))
    assert s["basket"][0] == pytest.approx(((1.0002 ** 24 - 1) + 0.08) / 2) and s["basket"][1] == pytest.approx((1.0002 ** 24 - 1) / 2)
    assert s["valid"].all() and len(s["stretches"]) == 1                  # a hole is not a pair that is not listed
    nothing = path_of(np.zeros((hours, 2)), r, holes={1: (8, 13)})        # the same hole, written as a price of nothing
    nothing["opens"][8:13, 1] = 0.0
    zeroed = bench.series(nothing)
    assert zeroed["basket"] == pytest.approx(s["basket"], abs=0) and (zeroed["r"] == s["r"]).all() and zeroed["valid"].all()
    # a pair listed part way through a day is in the basket for the hours it has a price that day
    part = bench.series(path_of(np.zeros((hours, 2)), np.full((hours - 1, 2), 0.0002), late={1: 30}))
    assert part["basket"][0] == pytest.approx(1.0002 ** 24 - 1) and part["basket"][1] == pytest.approx(((1.0002 ** 24 - 1) + (1.0002 ** 18 - 1)) / 2)
    hour = bench.series(path_of(np.zeros((hours, 2)), np.full((hours - 1, 2), 0.0002), late={1: 23}))     # ... were it one hour of it
    assert hour["basket"][0] == pytest.approx(((1.0002 ** 24 - 1) + 0.0002) / 2) and [bool(v) for v in hour["listed"][0]] == [True, True]
    assert s["r"][7:12, 1].tolist() == [0.0, 0.0, 0.0, 0.0, 0.0] and s["r"][12, 1] == pytest.approx(0.08)      # carried, then the whole move at once


def test_a_record_that_does_not_add_up_is_said_to_be_one():
    hours = 24 * 5
    w, c = blind_book(hours, 3, seed=6)
    good = path_of(w, market(hours, seed=7), c)
    assert bench.series(good)["gap_bps"] < 1e-6
    bad = dict(good, equity=good["equity"] * np.where(np.arange(hours) >= 60, 1.01, 1.0))      # one hour's equity is 1% out
    s = bench.series(bad)
    assert 95 < s["gap_bps"] < 105 and bench.reading_of(s, None)["rebuilt_within_bps"] == s["gap_bps"]
    drifting = dict(good, weights=good["weights"] * 0.9)                  # the weights on record are not the weights held
    assert bench.series(drifting)["gap_bps"] > 1.0
    worst_day_only = dict(good, equity=good["equity"] * np.where(np.arange(hours) >= 60, 1.0004, 1.0))
    assert 3.5 < bench.series(worst_day_only)["gap_bps"] < 4.5            # the worst day, in basis points, not an average
    # a record with a hole in it rebuilds nothing, and that is a gap too, not a figure that compares as no gap
    for holed in (dict(good, equity=np.where(np.arange(hours) == 60, np.nan, good["equity"])),
                  dict(good, costs=np.where(np.arange(hours) == 60, np.nan, good["costs"])),
                  dict(good, weights=np.where(np.arange(hours)[:, None] == 60, np.nan, good["weights"]))):
        assert bench.series(holed)["gap_bps"] == float("inf")
    for gap, says in ((0.5, "it is off by 0.50 bps at the worst"), (float("inf"), "it has a hole in it"), (None, "it has a hole in it"),
                      (float("nan"), "it has a hole in it")):
        text = bench.format_reading(a_reading(rebuilt_within_bps=gap))
        assert "FAULT: the hour by hour record does not rebuild the engine's own daily returns (" + says in text, gap
    assert "FAULT" not in bench.format_reading(a_reading(rebuilt_within_bps=0.009))
    # a hundredth of a basis point is the line, and on it is within it
    assert "FAULT" not in bench.format_reading(a_reading(rebuilt_within_bps=0.01))
    assert "it is off by 0.01 bps at the worst" in bench.format_reading(a_reading(rebuilt_within_bps=0.0101))


def test_the_hours_before_a_strategy_could_decide_are_left_out():
    hours = 24 * 6
    r = market(hours)
    path = path_of(np.full((hours, 3), 0.1), r, starved=30)
    s = bench.series(path)
    assert s["ts"][0] == T0 + 30 * HOUR and len(s["c"]) == hours - 30 - 1
    assert bench.reading_of(s, None)["net"] == pytest.approx(path["equity"][-1] / path["equity"][30] - 1.0)
    with pytest.raises(ValueError, match="never had the candles"):
        bench.series(path_of(np.full((hours, 3), 0.1), r, starved=hours))
    with pytest.raises(ValueError, match="never had the candles"):
        bench.series(path_of(np.full((hours, 3), 0.1), r, starved=hours - 47))      # under two days of deciding
    assert len(bench.series(path_of(np.full((hours, 3), 0.1), r, starved=hours - 48))["c"]) == 47


def test_double_costs_take_each_fills_costs_twice():
    hours = 24 * 3
    w, c = blind_book(hours, 3, seed=4)
    path = path_of(w, market(hours), c)
    once = bench.series(path)
    twice, free = bench.with_costs(once, 2.0), bench.with_costs(once, 0.0)
    assert twice["c"] == pytest.approx(once["c"] * 2.0) and once["c"].sum() > 0 and free["c"].sum() == 0.0
    hourly = (1.0 + (once["held"] * once["r"]).sum(axis=1)) * (1.0 - 2.0 * once["c"]) - 1.0
    assert twice["daily"] == pytest.approx(by_days(once, hourly))
    assert (twice["daily"] <= once["daily"] + 1e-15).all() and twice["daily"].sum() < once["daily"].sum() < free["daily"].sum()
    assert free["daily"] == pytest.approx(once["gross"], abs=1e-15) and (twice["gross"] == once["gross"]).all()
    assert twice["exposure"] == once["exposure"] and (twice["w"] == once["w"]).all()        # the positions are as they were
    assert bench.with_costs(once, 1.0)["daily"] == pytest.approx(once["daily"], abs=1e-15) and once["c"].sum() == pytest.approx(c.sum(), rel=1e-9)
    # an hour's fills never cost more than the book, however often the costs are counted
    assert bench.with_costs(once, 1e6)["c"].max() == bench.MOST_COST == 0.999 and np.isfinite(bench.with_costs(once, 1e6)["daily"]).all()


def test_twins_are_made_of_the_weights_a_book_last_traded_to():
    """A held position's weight moves with its price, so the weights an account ends each hour with
    carry the market's own path. A twin is made of the weight each pair was last traded to: that
    stands still between trades, and a trade is an hour in which the number of coins changed."""
    hours = 24 * 6
    r = market(hours, pairs=2, seed=3, vol=0.02)
    w = np.zeros((hours, 2))
    w[10:, 0] = 0.4                                                       # bought in hour 10 and left to run,
    w[60:, 0] = 0.2                                                       # cut in hour 60, and left again
    w[30:90, 1] = 0.3                                                     # the other pair: in at hour 30, out at 90
    path = path_of(w, r, runs=True)
    held = path["weights"]
    assert held[10, 0] == 0.4 and held[60, 0] == 0.2 and np.abs(held[11:60, 0] - 0.4).max() > 0.02      # on record it moves with the price
    s = bench.series(path)
    as_traded = np.zeros((hours - 1, 2))
    as_traded[10:60, 0], as_traded[60:, 0], as_traded[30:90, 1] = 0.4, 0.2, 0.3
    assert s["w"] == pytest.approx(as_traded, abs=1e-12) and s["held"] == pytest.approx(held[:-1], abs=0)
    assert s["gap_bps"] < 1e-6                                            # the record itself adds up on the weights it holds
    # slid by nothing, the book as last traded made what those weights made; the book itself made what it held made
    own, _ = bench.slid(s, 0)
    assert own == pytest.approx(by_days(s, (as_traded * r).sum(axis=1)), abs=1e-12)
    assert s["gross"] == pytest.approx(by_days(s, (held[:-1] * r).sum(axis=1)), abs=1e-12) and not np.allclose(own, s["gross"])
    # a book that trades back to the same weights every hour holds what it last traded to: the two are one
    level = bench.series(path_of(w, r))
    assert level["w"] == pytest.approx(level["held"], abs=0) and bench.slid(level, 0)[0] == pytest.approx(level["gross"], abs=1e-15)
    # a change too small to be a trade is not one
    quiet = path_of(w, r, runs=True)
    quiet["weights"][20, 0] *= 1.0 + 1e-12
    assert bench.series(quiet)["w"] == pytest.approx(as_traded, abs=1e-9)
    # A pair that is held through a hole in its candles has not traded either. The record prices it at the mark the
    # account valued it at, so its price stands still for the hole and the whole move lands at once when the candles
    # come back; its weight on record moves all the while, with the rest of the book, and its coins do not
    marked = r.copy()
    marked[40:50, 1] = 0.0
    marked[50, 1] = 0.08
    back = bench.series(path_of(w, marked, runs=True))
    assert back["w"] == pytest.approx(as_traded, abs=1e-12) and np.ptp(back["held"][40:50, 1]) > 1e-4
    # and one nobody holds, with no price at all for those hours, is not held by a twin because of them
    holed = bench.series(path_of(np.where(np.arange(hours)[:, None] >= 100, w, 0.0), r, runs=True, holes={1: (40, 50)}))
    assert holed["w"][100:, 0] == pytest.approx(0.2, abs=1e-12) and holed["w"][:, 1].sum() == 0.0


def test_a_sharpe_ratio_and_a_t_are_what_they_say_and_are_not_given_on_too_little():
    x = np.array([0.01, -0.006] * 20)
    m = bench.measure(x)
    mean, sd = x.mean(), x.std(ddof=1)
    assert m["sharpe"] == pytest.approx(mean / sd * math.sqrt(365)) and m["t"] == pytest.approx(mean / (sd / math.sqrt(40)))
    assert m["days"] == 40 and m["t"] == pytest.approx(m["sharpe"] * math.sqrt(40 / 365))
    assert bench.measure(x[:29]) is None and bench.measure(x[:30]) is not None      # MIN_DAYS
    assert bench.MIN_DAYS == 30
    assert bench.measure(np.full(60, 0.001)) is None                    # a series that does not vary measures nothing
    assert bench.measure(np.r_[x, np.nan, np.inf])["days"] == 40          # and what is not a number is not a reading
    assert bench.a_year(np.array([0.001, 0.003])) == pytest.approx(0.002 * 365) and bench.a_year(np.array([])) is None
    assert bench.a_year(np.array([0.001, np.nan])) == pytest.approx(0.365)
    # the score twins are ranked on is that same t, row by row; a row that is nothing every day scores nothing
    rows = np.vstack([x, -x, np.zeros(40)])
    assert bench._scores(rows) == pytest.approx([m["t"], -m["t"], 0.0]) and bench._scores(rows[:, :29]) is None
    assert bench._scores(rows[:, :30]) == pytest.approx([t_of(x[:30]), -t_of(x[:30]), 0.0])
    assert bench._scores(x)[0] == pytest.approx(t_of(x))
    assert list(bench._scores(np.vstack([np.full(40, 0.01), np.full(40, -0.01)]))) == [float("inf"), float("-inf")]


def test_the_stretches_are_the_whole_run_its_last_365_days_and_each_year_with_enough_days():
    first = int(pd.Timestamp("2024-12-12").timestamp()) // DAY
    days = first + np.arange(20 + 365 + 40)                               # 20 days of 2024, all of 2025, 40 of 2026
    where = bench.spans(days)
    assert list(where) == ["all", "last", "2025", "2026"]                 # 2024 has under 30 days: no reading for it
    assert where["all"].sum() == len(days) and where["last"].sum() == 365 and where["last"][-365:].all()
    assert where["2025"].sum() == 365 and where["2026"].sum() == 40 and not where["2025"][:20].any()
    # a run of a year or less has no last 365 days apart from the whole of it
    assert list(bench.spans(first + 20 + np.arange(365))) == ["all", "2025"]
    assert list(bench.spans(first + 20 + np.arange(366))) == ["all", "last", "2025"]


# --- twins ---------------------------------------------------------------------------------

def test_a_book_that_never_lets_go_of_a_position_has_no_twins():
    """A twin may not hold what the book took within the book's own longest stay in a pair of the hour
    in hand, so a book that is never out of some pair leaves no room for one. Nor has a book that never
    took a position. And a book that trades now and then is ranked on the weights it traded to: on
    record its weights move with every price, and ranked on those a book that never traded read as far
    worse than its twins for no reason but the market's path (found in review, 2026-10-07)."""
    hours = 24 * 150
    r = market(hours)
    still = np.tile([0.25, 0.25, 0.1], (hours, 1))
    late = still.copy()
    late[: 24 * 20, 2] = 0.0
    for path in (path_of(still, r), path_of(still, r, runs=True), path_of(late, r, runs=True, late={2: 24 * 20})):
        s = bench.series(path)
        assert s["hold"] == hours - 1 and s["hold_pair"] == "P0" and bench.no_twins(s) == "hold"
        assert bench.slides(s, 50) is None and bench.judge(s, n=50) is None
        out = bench.reading_of(s, None)
        assert out["no_twins"] == "hold" and out["twins"] is None and out["slide"]["longest_hold_days"] == pytest.approx((hours - 1) / 24)
        assert out["slide"]["longest_hold_pair"] == "P0"
    idle = bench.series(path_of(np.zeros((hours, 3)), r))
    assert idle["hold"] == 0 and bench.no_twins(idle) == "idle" and bench.judge(idle, n=50) is None
    assert bench.reading_of(idle, None)["no_twins"] == "idle"
    # One pair held all through is enough, however busy the rest of the book, and whether it is traded or not: a strategy
    # is told what it holds, and what it does with the rest can turn on that. (Leaving out a position that never changes,
    # and reading a book by its trades when its strategy does not look at what it holds, were both built and taken out
    # again in review, 2026-10-07: neither could be made safe for every strategy)
    busy, c = blind_book(hours, 3, seed=2)
    assert bench.no_twins(bench.series(path_of(busy, r, c))) is None
    for kept in (0.1, np.where((np.arange(hours) // 24) % 2 == 0, 0.25, 0.10)):
        busy[:, 0] = kept
        cored = bench.series(path_of(busy, r, c, runs=True))
        assert bench.no_twins(cored) == "hold" and cored["hold"] == hours - 1 and cored["hold_pair"] == "P0" and bench.judge(cored, 20) is None
    # five days in every fourteen, a pair at a time: left to run between its trades, and set back to its weights every hour
    turns = np.zeros((hours, 3))
    for k, at in enumerate(range(0, hours, 24 * 14)):
        turns[at: at + 24 * 5, k % 3] = 0.3
    level, ran = bench.series(path_of(turns, r)), bench.series(path_of(turns, r, runs=True))
    assert np.abs(ran["held"] - turns[:-1]).max() > 0.01 and ran["hold"] == level["hold"] == 24 * 5      # the weights on record did move
    a, b = bench.judge(level, n=60), bench.judge(ran, n=60)
    assert a["beaten"] == b["beaten"] and 0.0 < a["beaten"]["all"] < 1.0 and a["own"] == pytest.approx(b["own"], abs=1e-12)
    assert a["gross"] == pytest.approx(b["gross"], abs=1e-12) and not np.allclose(ran["gross"], level["gross"])


def test_a_stay_in_a_pair_runs_until_the_book_is_out_of_it_however_it_trades_meanwhile(strategies, root, small):
    """A strategy is told what it holds. For as long as it is in a pair it can be acting on what it saw
    when it went in, however often it has traded the pair meanwhile, so the stay the lead is taken
    from runs from the hour it went in to the hour it was out, and selling part of the position does
    not end it. A book that is never out of a pair is told so, in those words: one that switched every
    pair between two weights at a cost of 81% a year was told that it sat in one position, which it did
    not, and that it had no timing, which nobody had measured (found in review, 2026-10-07)."""
    hours = 24 * 200
    r = market(hours, pairs=2, seed=21)
    w = np.zeros((hours, 2))
    w[100:1300, 0] = 0.4                                                  # in at hour 100,
    w[400:1300, 0] = 0.1                                                  # three quarters of it sold at hour 400,
    w[900:1300, 0] = 0.2                                                  # some bought back at hour 900, and out at 1300
    w[2000:2100, 1] = 0.3
    s = bench.series(path_of(w, r, runs=True))
    n = len(s["c"])
    assert s["hold"] == 1200 and s["hold_pair"] == "P0" and bench.lead(s) == 24 + 1200
    assert n - 1224 - 100 < bench.slides(s, 400).max() <= n - 1224
    # Which of the two a run is too short for: any book at all (the days to slide by and the days to draw from, five and
    # five in this test, and twice the candles), or only one that stays in a pair as long as this one does. To the hour
    edge = (5 + 5) * 24 + 2 * 24
    assert (bench.MIN_SLIDE_DAYS, bench.MIN_ROOM_DAYS) == (5, 5)
    for run, why in ((edge, "hold"), (edge - 1, "short")):
        sat = bench.series(path_of(np.full((run + 1, 1), 0.3), market(run + 1, pairs=1)))
        assert len(sat["c"]) == run and sat["hold"] == run and bench.no_twins(sat) == why, run
    # Through the engine: a strategy that is never out of a pair, each one at a tenth or a quarter of the book by the hour
    # of the day. It trades every twelve hours and has no twins, and its reading says which it is
    c = made_up(900)
    never_out = bench.replay(c, RCFG, cfg_of("turns_about"))[0]
    assert never_out["hold"] == len(never_out["c"]) and never_out["hold_pair"] == "AAA" and bench.no_twins(never_out) == "hold"
    assert never_out["fills"].sum() > 100 and never_out["wrote_params"] is False
    looks = bench.read(cfg_of("turns_about"), RCFG, c, jobs=1, quick=True, n_twins=20)
    days = looks["slide"]["longest_hold_days"]
    assert looks["twins"] is None and looks["no_twins"] == "hold" and looks["slide"]["longest_hold_pair"] == "AAA"
    assert days == pytest.approx(len(never_out["c"]) / 24)
    assert bench.words(looks) == (f"Reading: it was never out of AAA for {days:,.0f} days on end, which leaves too little of a run of {looks['days']:,} "
                                  f"days to set it against twins. The bench cannot read its timing; that is not to say it has none.")
    assert f"not set against twins (never out of AAA for {days:,.0f} days, too long for a run of {looks['days']:,}). In sample." in bench.ledger_line(looks)
    assert "NOTE:" not in bench.format_reading(looks)
    # A strategy whose params are not, at the end, as they were handed to it has kept something there that it would not
    # have live, where every hour starts afresh. The reading says so
    noted = bench.replay(c, RCFG, cfg_of("turns_about_and_notes", sizes=[0.25, 0.1], deep={"a": 1.0}))[0]
    assert noted["wrote_params"] is True and bench.replay(c, RCFG, cfg_of("turns_about", sizes=[0.25, 0.1], deep={"a": 1.0}))[0]["wrote_params"] is False
    # Params are set side by side as the plain text they come to. An array among them, which cannot simply be compared with
    # its copy, is not thereby taken to have been written to
    assert bench.replay(c, RCFG, cfg_of("turns_about", sizes=np.array([0.25, 0.1])))[0]["wrote_params"] is False
    assert bench.replay(c, RCFG, cfg_of("turns_about_and_notes", sizes=np.array([0.25, 0.1])))[0]["wrote_params"] is True
    # ... and params that can no longer be written out at all, a strategy having tied them in a knot, are not as they were
    assert bench.replay(c, RCFG, cfg_of("ties_a_knot"))[0]["wrote_params"] is True
    told = bench.read(cfg_of("turns_about_and_notes"), RCFG, c, jobs=1, quick=True, n_twins=5)
    assert told["slide"]["wrote_params"] is True and told["params"] == {}
    assert ("  NOTE: the strategy's params were not, at the end of the run, as they were handed to it. Live it is handed them afresh every "
            "hour, so what it kept there it would not have: if it decides on that, this replay is not what it would do\n") in bench.format_reading(told)


def test_a_book_that_sees_the_next_hour_beats_every_twin_and_its_mirror_beats_none():
    hours = 24 * 150
    r = market(hours, seed=3)
    sees = np.vstack([(r > 0) / 3.0, np.zeros((1, 3))])
    mirror = np.vstack([(r <= 0) / 3.0, np.zeros((1, 3))])
    assert bench.judge(bench.series(path_of(sees, r)), n=200)["beaten"]["all"] == 1.0
    assert bench.judge(bench.series(path_of(mirror, r)), n=200)["beaten"]["all"] == 0.0


def clustered(hours, pairs, seed):
    """A market with no memory of direction and plenty of everything else: quiet and wild spells, and
    pairs that move together."""
    rng = np.random.default_rng(seed)
    level = np.zeros(hours - 1)
    for t in range(1, hours - 1):
        level[t] = 0.97 * level[t - 1] + 0.25 * rng.normal()
    together = rng.normal(size=(hours - 1, 1))
    return 0.006 * np.exp(level)[:, None] * (0.7 * together + 0.7 * rng.normal(size=(hours - 1, pairs)))


def follower(r, look=48, band=0.02, sign=1.0, size=0.3):
    """Holds a pair from the hour its move over the last `look` hours passes `band` until it falls
    under minus that: a trend follower (sign 1) or a dip buyer (sign -1). It decides on the past alone."""
    grown = np.vstack([np.zeros((1, r.shape[1])), np.cumsum(np.log1p(r), axis=0)])
    w, on = np.zeros_like(grown), np.zeros(r.shape[1], dtype=bool)
    for t in range(look, len(grown)):
        x = sign * (grown[t] - grown[t - look])
        on = np.where(on, x > -band, x > band)
        w[t] = on * size
    return w, np.r_[0.0, np.abs(np.diff(w, axis=0)).sum(axis=1) * 0.0015]


def test_books_with_no_timing_land_anywhere_among_their_twins_and_on_average_in_the_middle(small):
    """The figure the bench leans on: for a book with no timing the share of twins beaten is as likely
    to be any number between 0 and 1 as any other. Two hundred blind books, each on a market of its
    own. The bounds are four standard errors and more from what such books give, so that they hold on
    any seeds and not only on these (they did not at first; found in review, 2026-10-07)."""
    hours, shares, luck = 24 * 40, [], []
    for seed in range(200):
        w, c = blind_book(hours, 3, seed=100 + seed)
        s = bench.series(path_of(w, clustered(hours, 3, 500 + seed), c))
        tw = bench.judge(s, n=60, seed=seed)
        shares.append(tw["beaten"]["all"])
        luck.append(bench.chance(tw["beaten"]["all"], tw["worth"]))
        assert 3.0 < tw["worth"] <= 60.0
    shares, luck = np.array(shares), np.array(luck)
    assert 0.41 < shares.mean() < 0.59                                    # 0.5 give or take 0.02
    assert (shares > 0.7).sum() >= 35 and (shares < 0.3).sum() >= 35      # spread out, not huddled at a half: 60 each, give or take 6
    assert (shares >= 0.95).mean() <= 0.14 and (shares <= 0.05).mean() <= 0.14
    # and the chance read off the share is one a book with no timing gets under no more often than it says
    assert (luck <= 0.10).mean() <= 0.19 and (luck <= 0.05).mean() <= 0.12 and luck.min() > 0.0 and luck.max() <= 1.0


def test_a_twin_that_had_seen_the_hours_it_trades_would_pile_trend_followers_up_at_the_bottom(small, monkeypatch):
    """The harder case: books that decide on the market's past when its past says nothing. A trend
    follower that looks twenty days back, on eighty markets. Among its real twins it lands where it
    lands. Let the twins be slid all the way round, so that some hold what the book took in the days
    just after, and those twins have seen the rise they ride: the book falls behind them, by ten points
    of share and more on average. If the bench ever made such twins this would show nothing, and fail."""
    hours, look = 24 * 87, 24 * 20
    real, seeing = [], []
    for seed in range(80):
        r = clustered(hours, 3, 500 + seed)
        w, _ = follower(r, look=look, band=0.0)
        s = bench.series(path_of(w, r, memory=look, starved=look))
        tw = bench.judge(s, n=60, seed=seed)
        if tw is None:                                                    # it held one pair too long to be slid at all
            continue
        with monkeypatch.context() as m:
            m.setattr(bench, "lead", lambda s_: 0)
            seeing.append(bench.judge(s, n=60, seed=seed)["beaten"]["all"])
        real.append(tw["beaten"]["all"])
    real, seeing = np.array(real), np.array(seeing)
    assert len(real) >= 40 and 0.3 < real.mean() < 0.7
    assert (seeing - real).mean() < -0.04                                 # -0.10 to -0.15 on six other sets of seeds, give or take 0.025


def test_among_twins_worth_only_a_few_no_book_reads_as_more_than_luck(small):
    """Blind books that turn over once in a fortnight or so, on runs of a hundred days: their twins
    are worth five separate ones or so. A book with no timing still beats nine in ten of such twins one
    time in ten, and nineteen in twenty about as often as that, because its few separate twins are all
    on one side of it together. Read off the share alone that would be one idea in ten with nothing in
    it passing for timing; the chance, which knows what the twins are worth, lets next to none through."""
    hours, shares, worth = 24 * 100, [], []
    for seed in range(150):
        w = np.repeat(blind_book(hours // 12 + 1, 3, seed=100 + seed)[0], 12, axis=0)[:hours]
        s = bench.series(path_of(w, clustered(hours, 3, 500 + seed)))
        tw = bench.judge(s, n=60, seed=seed)
        shares.append(tw["beaten"]["all"])
        worth.append(tw["worth"])
    shares, worth = np.array(shares), np.array(worth)
    luck = np.array([bench.chance(b, k) for b, k in zip(shares, worth)])
    assert 3.0 < np.median(worth) < 8.0 and worth.max() < 14.0
    assert (shares >= 0.9).sum() >= 6                                     # 12 to 19 on six other sets of seeds
    assert (luck <= 0.10).sum() <= 3 and (luck <= 0.05).sum() == 0        # none, on those six


def test_no_twin_holds_what_the_book_took_in_the_hours_just_after():
    """A book that holds the pair in each hour that follows a rising one decides on the past alone.
    Slid all the way round but one hour, a twin holds in each hour what the book took an hour later,
    which is to say it holds the pair in every hour that rises. No slide may come that close to the
    whole way round. It stops short by as far as the strategy's memory reaches: the hours of candles it
    is handed, and then the longest it kept any position or as long again as the candles, since a
    strategy is told what it holds and a position still held says something of every hour since it was
    taken (a twin that held what a book was still sitting on half a year later had seen that the price
    had not come back; found in review, 2026-10-07)."""
    hours = 24 * 150
    r = market(hours, pairs=1, seed=5)
    w = np.vstack([np.zeros((1, 1)), (r > 0) * 0.5])
    s = bench.series(path_of(w, r, memory=1))
    n = len(s["c"])
    assert bench.slid(s, n - 1)[0].sum() > bench.slid(s, 0)[0].sum() + 3.0       # the twin that has seen the hour it trades
    every_rise = 0.5 * np.maximum(r[:, 0], 0.0)
    every_rise[-1] = 0.0                                                  # but for the last hour, where the end of the run meets its start
    assert bench.slid(s, n - 1)[0] == pytest.approx(by_days(s, every_rise), abs=1e-12)
    runs = longest_hold(w[:-1])                                           # the longest run of rising hours
    assert s["hold"] == runs and 6 <= runs < 24 and bench.lead(s) == 1 + runs
    assert n - bench.lead(s) - 60 < bench.slides(s, 2000).max() <= n - bench.lead(s)
    for memory, short in ((24, 48), (100, 200), (720, 1440)):             # no hold is as long as these candles: twice the candles
        longer = bench.series(path_of(w, r, memory=memory))
        assert bench.lead(longer) == short and bench.least_hours(longer) == 30 * 24 + short + 90 * 24
        if bench.slides(longer, 500) is not None:
            assert n - short - 100 < bench.slides(longer, 2000).max() <= n - short and bench.slides(longer, 2000).min() >= 30 * 24
    too_long = bench.series(path_of(w, r, memory=720))
    assert bench.slides(too_long, 10) is None and bench.no_twins(too_long) == "short"      # 150 days is too short a run for a memory of 30
    # a book that sits on a position for longer than its candles reach: the candles, and then that hold
    sits = np.zeros((hours, 1))
    sits[100:700], sits[2000:2100] = 0.5, 0.5
    slow = bench.series(path_of(sits, r, memory=24))
    assert slow["hold"] == 600 and bench.lead(slow) == 624 and bench.least_hours(slow) == 30 * 24 + 624 + 90 * 24 <= n
    drawn = bench.slides(slow, 2000)
    assert n - 624 - 60 < drawn.max() <= n - 624 and drawn.min() >= 30 * 24
    assert bench.reading_of(slow, bench.judge(slow, 30))["slide"] == {
        "candles_days": 1.0, "longest_hold_days": 25.0, "longest_hold_pair": "P0", "wrote_params": False, "lead_days": 26.0,
        "least_days": 146.0, "history_days": pytest.approx(n / 24)}
    sits[100:1000] = 0.5                                                  # and one that sits so long that no room is left
    stuck = bench.series(path_of(sits, r, memory=24))
    assert stuck["hold"] == 900 and bench.least_hours(stuck) > n and bench.no_twins(stuck) == "hold" and bench.judge(stuck, 30) is None


def test_the_share_of_twins_beaten_is_what_counting_them_by_hand_gives():
    """Every twin made the long way round, with nothing borrowed from bot/bench.py but the series and
    how far each is slid: the pairs with prices throughout rolled over the whole run, the pair listed
    late rolled inside its own stretch, each twin's days set against the average twin's before any
    costs, its t by the textbook."""
    hours, late = 24 * 200, 24 * 60
    r = market(hours, pairs=3, seed=33, vol=0.02)
    w, c = blind_book(hours, 3, seed=34)
    w[:, 2] *= 2.5                                                        # the book leans on the pair that is listed late
    w[:late, 2] = 0.0
    s = bench.series(path_of(w, r, c, late={2: late}))
    n = len(s["c"])
    by = bench.slides(s, 90)
    back = bench.lead(s)
    assert back == 24 + longest_hold(w[:-1]) and 48 < back < 24 + 72      # the day of candles it is handed, and its longest hold
    assert len(by) == 90 and by.min() >= 720 and by.max() <= n - back and ((by % (n - late) >= 720) & (by % (n - late) <= n - late - back)).all()

    def twin(hours_later):
        w_ = np.zeros_like(s["w"])
        w_[:, :2] = np.roll(s["w"][:, :2], hours_later, axis=0)
        w_[late:, 2] = np.roll(s["w"][late:, 2], hours_later % (n - late))
        return by_days(s, (w_ * s["r"]).sum(axis=1))
    theirs = np.array([twin(int(h)) for h in by])
    usual = theirs.mean(axis=0)
    mine = t_of(twin(0) - usual)
    others = np.array([t_of(x - usual) for x in theirs])
    by_hand = ((others < mine - 1e-9).sum() + 0.5 * (np.abs(others - mine) <= 1e-9).sum()) / len(by)
    got = bench.judge(s, n=90)
    assert got["beaten"]["all"] == pytest.approx(by_hand, abs=1e-12) and 0.0 < by_hand < 1.0
    assert got["gross"] == pytest.approx(usual, abs=1e-12) and got["own"] == pytest.approx(twin(0), abs=1e-12) and (got["slides"] == by).all()

    def twin_net(hours_later):                                            # after the book's own costs, which slide with its positions
        w_ = np.zeros_like(s["w"])
        w_[:, :2] = np.roll(s["w"][:, :2], hours_later, axis=0)
        w_[late:, 2] = np.roll(s["w"][late:, 2], hours_later % (n - late))
        hourly = (1.0 + (w_ * s["r"]).sum(axis=1)) * (1.0 - np.roll(s["c"], hours_later)) - 1.0
        return float(np.prod(1.0 + hourly) - 1.0)
    assert got["net_middle"] == pytest.approx(np.median([twin_net(int(h)) for h in by]), abs=1e-12)
    # It is the t of each twin's gap that ranks it, not the gap: a twin that made more on wilder days is not ahead for
    # that. On this book the two orders happen to give one share, so here are six more, and on most of them they do not
    apart = 0
    for seed in range(40, 46):
        w_, c_ = blind_book(hours, 3, seed=seed)
        w_[:late, 2] = 0.0
        s_ = bench.series(path_of(w_, market(hours, pairs=3, seed=seed + 100, vol=0.02), c_, late={2: late}))
        got_ = bench.judge(s_, n=90)
        gaps = np.array([bench.slid(s_, int(h))[0] for h in got_["slides"]]) - got_["gross"]
        its = got_["own"] - got_["gross"]
        scores = np.array([t_of(g) for g in gaps])
        by_t = ((scores < t_of(its) - 1e-9).sum() + 0.5 * (np.abs(scores - t_of(its)) <= 1e-9).sum()) / 90
        by_gap = ((gaps.mean(axis=1) < its.mean() - 1e-15).sum() + 0.5 * (np.abs(gaps.mean(axis=1) - its.mean()) <= 1e-15).sum()) / 90
        assert got_["beaten"]["all"] == pytest.approx(by_t, abs=1e-12), seed
        apart += abs(by_t - by_gap) > 1e-9
    assert apart >= 3
    # the costs are not in the ranking: at twenty times the costs the share is the same, and the middle twin has paid them
    dear = bench.judge(bench.with_costs(s, 20.0), n=90)
    assert dear["beaten"] == got["beaten"] and dear["net_middle"] < got["net_middle"] - 0.05
    # and the costs slide with the positions: a twin's costly hours are the book's, as much later as the twin is slid
    k = int(by[0])
    assert bench.slid(s, k)[1] == pytest.approx(by_days(s, (1.0 + (np.roll(s["w"][:, :2], k, axis=0) * s["r"][:, :2]).sum(axis=1)
                                                           + np.r_[np.zeros(late), np.roll(s["w"][late:, 2], k % (n - late)) * s["r"][late:, 2]])
                                                      * (1.0 - np.roll(s["c"], k)) - 1.0), abs=1e-12)
    assert not np.allclose(bench.slid(s, k)[1], by_days(s, bench._after((np.roll(s["w"], k, axis=0) * s["r"]).sum(axis=1), s["c"])))


def test_a_pair_listed_late_is_slid_inside_the_stretch_it_has_prices_for():
    """So that a twin holds as much of it as the book does. Rolled over the whole run with the hours
    before its listing struck out, as it once was, twins held less of the late pair than the book and
    more cash, and a book that never traded it did not tie with them (found in review, 2026-10-07)."""
    hours, late = 24 * 220, 24 * 70
    r = np.zeros((hours - 1, 2))
    r[:, 1] = 1e-7                                                        # only the late pair moves, by the same sliver every hour it is listed
    w, _ = blind_book(hours, 2, seed=8)
    w[:late, 1] = 0.0
    s = bench.series(path_of(w, r, late={1: late}))
    n = len(s["c"])
    held = float(s["w"][:, 1].sum())                                      # pair hours of the late pair in the book
    for hours_later in (0, 720, 2000, 3111, n - 48):
        gross, _ = bench.slid(s, hours_later)
        assert gross.sum() == pytest.approx(held * 1e-7, rel=1e-6), hours_later       # every twin holds as much of it, inside its own hours
    struck = (np.roll(s["w"][:, 1], 2000) * s["valid"][:, 1]).sum()
    assert struck < 0.9 * held                                            # the old way lost a tenth of it and more
    assert [(a, b) for (a, b), _, _ in s["stretches"]] == [(0, n), (late, n)] and n - late >= bench.least_hours(s)
    assert bench.left_in_place(s) == [] and bench.judge(s, 20)["in_place"] == []
    # A stretch too short to slide a book inside is left where it is, in the book and in every twin, and the
    # reading says which pair that is: what its timing added is then in both, neither counted nor tested
    newer = w.copy()
    newer[: hours - 2000, 1] = 0.0
    short = bench.series(path_of(newer, r, late={1: hours - 2000}))
    assert 2000 < bench.least_hours(short) and short["w"][:, 1].sum() > 100
    assert bench.slid(short, 1000)[0] == pytest.approx(bench.slid(short, 0)[0], abs=1e-15)       # only the late pair moves, and it was not slid
    assert bench.slides(short, 50) is not None and bench.no_twins(short) is None      # and it does not stand in the way of sliding the rest
    tw = bench.judge(short, 20)
    assert bench.left_in_place(short) == ["P1"] == tw["in_place"] and bench.reading_of(short, tw)["twins"]["in_place"] == ["P1"]
    text = bench.format_reading(a_reading(twins=twins_of(0.97, in_place=["P1", "P3"])))
    assert ("Not slid: P1, P3, whose prices cover too short a stretch to slide a book inside. Those positions are the same in every twin, so "
            "their timing is neither counted nor tested") in text and "Not slid" not in bench.format_reading(a_reading())
    # a pair the book never holds is not in that list, however short its history
    never = newer.copy()
    never[:, 1] = 0.0
    assert bench.left_in_place(bench.series(path_of(never, r, late={1: hours - 2000}))) == []
    # ... and one it never holds does not narrow the slides either, late as it is listed: they are the ones drawn with that pair not there
    unheld = w.copy()
    unheld[:, 1] = 0.0
    with_it, without = bench.series(path_of(unheld, r, late={1: late})), bench.series(path_of(unheld[:, :1], r[:, :1]))
    assert (bench.slides(with_it, 300) == bench.slides(without, 300)).all() and not (bench.slides(s, 300) == bench.slides(without, 300)).all()
    # a stretch exactly long enough to slide a book inside is slid; an hour shorter, it is left where it is
    least = bench.least_hours(s)
    for stretch, slides_it in ((least, True), (least - 1, False)):
        edge = w.copy()
        edge[: hours - 1 - stretch, 1] = 0.0
        at_the_edge = bench.series(path_of(edge, r, late={1: hours - 1 - stretch}))
        assert bench.least_hours(at_the_edge) == least and [b - a for (a, b), _, _ in at_the_edge["stretches"]] == [n, stretch]
        assert np.allclose(bench.slid(at_the_edge, 1000)[0], bench.slid(at_the_edge, 0)[0], atol=1e-15) is not slides_it
        assert (bench.left_in_place(at_the_edge) == []) is slides_it
        inside = bench.slides(at_the_edge, 400) % stretch                 # where each slide leaves the late pair, inside its own stretch
        assert bool(((inside >= 720) & (inside <= stretch - bench.lead(at_the_edge))).all()) is slides_it and len(set(inside.tolist())) > 100
    # and a book that holds nothing but pairs too new to slide has no twin that differs from it: it has none
    only = newer.copy()
    only[:, 0] = 0.0
    alone = bench.series(path_of(only, r, late={1: hours - 2000}))
    assert bench.no_twins(alone) == "new" and bench.slides(alone, 50) is None and bench.judge(alone, 20) is None
    # Which of two things such a book is told. That no pair it holds has prices for long enough for any book: thirty days
    # to slide by, ninety to draw from and twice the candles. Or that they would do for a book that stays in nothing for
    # long and not for this one, with the stay it has: it was told the second of a book whose stays were six hours, which
    # no letting go would have mended (found in review, 2026-10-07). To the hour, for a book that is in the late pair a
    # hundred hours at a time
    def in_turns(stretch):
        book = np.zeros((hours, 2))
        book[:, 1] = np.where(np.arange(hours) % 150 < 100, 0.3, 0.0)
        book[: hours - 1 - stretch, 1] = 0.0
        return bench.series(path_of(book, r, late={1: hours - 1 - stretch}))
    any_book, this_book = (30 + 90) * 24 + 2 * 24, 30 * 24 + (24 + 100) + 90 * 24
    for stretch, why in ((any_book - 1, "new"), (any_book, "pairs"), (this_book - 1, "pairs"), (this_book, None)):
        turned = in_turns(stretch)
        assert turned["hold"] == 100 and bench.least_hours(turned) == this_book <= n and [b - a for (a, b), _, _ in turned["stretches"]] == [n, stretch]
        assert bench.no_twins(turned) == why and (bench.judge(turned, 20) is None) is (why is not None), stretch
        assert bench.reading_of(turned, None)["slide"]["history_days"] == pytest.approx(stretch / 24)


def test_slides_are_drawn_to_the_hour_at_the_edges_of_every_stretch(monkeypatch):
    """With no room asked for beyond the slide itself, a late pair whose stretch is exactly long enough
    to slide the book inside leaves one place for it there: slid by the least there is. Every slide then
    puts it in that place, and the slides are the ones that do, to the hour."""
    monkeypatch.setattr(bench, "MIN_SLIDE_DAYS", 2)
    monkeypatch.setattr(bench, "MIN_ROOM_DAYS", 0)

    def book(hours, stretch, held):
        w = np.zeros((hours, 2))
        for at in range(0, hours, 60):
            w[at: at + 30, 0] = 0.5                                       # thirty hours in the first pair, thirty out
        first = hours - 1 - stretch
        w[first + 5: first + 5 + held, 1] = 0.3                           # and one stay in the pair that is listed late
        return bench.series(path_of(w, market(hours, pairs=2, seed=3), late={1: first}))
    s = book(401, 102, 30)
    assert bench.lead(s) == 24 + 30 and bench.least_hours(s) == 48 + 54 == 102 and [b - a for (a, b), _, _ in s["stretches"]] == [400, 102]
    drawn = bench.slides(s, 300)
    assert sorted(set(drawn.tolist())) == [48, 150, 252] and len(drawn) == 300      # 48 inside the stretch each time; 354 would be within the lead of the whole way round
    assert min(np.bincount(drawn)[[48, 150, 252]]) > 60                   # each as likely as the others
    # Where so few slides fit that a thousand rounds of drawing do not find enough of them, the rest are made up from the
    # ones that fit every stretch as they stand. Never none: it used to be that a book could have no twins for that alone
    long = book(5001, 48 + 24 + 2400, 2400)
    assert bench.lead(long) == 2424 and bench.least_hours(long) == 2472 and bench.no_twins(long) is None
    rare = bench.slides(long, 200)
    assert sorted(set(rare.tolist())) == [48, 2520] and len(rare) == 200 and (rare == 2520).sum() >= 20
    assert bench.judge(long, 20)["n"] == 20


def test_twins_are_ranked_before_costs_and_the_costs_do_not_move_the_share():
    """Costs are the same for a book and every one of its twins. Left in the figure each is ranked on,
    a shared loss divided by each one's own noise ranked the noisier book higher: a book on the costs
    treadmill read 83% where its timing alone read 73% (found in review, 2026-10-07)."""
    hours = 24 * 150
    r = clustered(hours, 3, 77)
    w, c = follower(r)
    free, dear = bench.series(path_of(w, r, memory=48)), bench.series(path_of(w, r, c * 6.0, memory=48))
    a, b = bench.judge(free, n=150), bench.judge(dear, n=150)
    assert a["beaten"] == b["beaten"] and (a["slides"] == b["slides"]).all() and a["gross"] == pytest.approx(b["gross"], abs=1e-15)
    assert b["net_middle"] < a["net_middle"] - 0.05                       # the twins pay the book's costs all the same
    one, other = bench.reading_of(free, a), bench.reading_of(dear, b)
    assert one["timing_per_year"] == pytest.approx(other["timing_per_year"], abs=1e-12) and one["costs_per_year"] == 0.0
    assert other["costs_per_year"] > 0.3 and other["left_per_year"] == pytest.approx(one["left_per_year"] - other["costs_per_year"], abs=1e-12)
    # a market that goes nowhere: the book loses its costs and so does every twin, and nothing else is said of it
    flat = bench.series(path_of(w, np.zeros_like(r), c, memory=48))
    tw = bench.judge(flat, n=40)
    out = bench.reading_of(flat, tw)
    assert tw["beaten"]["all"] == 0.5 and out["timing_per_year"] == 0.0 and out["left_per_year"] == pytest.approx(-out["costs_per_year"])
    assert tw["net_middle"] == pytest.approx(out["net"], rel=1e-9) and out["net"] < -0.05


def test_every_twin_is_slid_by_thirty_days_or_more_and_the_same_book_always_reads_the_same(monkeypatch):
    hours = 24 * 150
    w, c = blind_book(hours, 3, seed=9)
    s = bench.series(path_of(w, market(hours, seed=10), c))
    seen, real = [], bench.slid

    def noting(s_, by):
        seen.append(int(by))
        return real(s_, by)
    monkeypatch.setattr(bench, "slid", noting)
    first = bench.judge(s, n=300)
    n = len(s["c"])
    back = bench.lead(s)
    assert back == 24 + longest_hold(w[:-1])
    assert len(seen) == 301 and seen[0] == 0 and min(seen[1:]) >= 30 * 24 and max(seen) <= n - back and len(set(seen)) > 200
    assert bench.MIN_SLIDE_DAYS == 30 and bench.MIN_ROOM_DAYS == 90 and bench.TWINS == 1000 and bench.SUB_TWINS == 200
    again = bench.judge(s, n=300)
    assert again["beaten"] == first["beaten"] and (again["slides"] == first["slides"]).all()      # nothing random is left to chance
    assert bench.judge(s, n=300, seed=1)["beaten"]["all"] != first["beaten"]["all"]
    assert bench.judge(s, n=0) is None and bench.slides(s, 0) is None and len(bench.slides(s, 1)) == 1
    drawn = bench.slides(s, 5000)
    tenths = np.histogram(drawn, bins=10, range=(720, n - back))[0]
    assert tenths.min() > 400 and tenths.max() < 600                      # drawn evenly over all the room there is
    assert drawn.min() < 720 + 5 and drawn.max() > n - back - 5           # from the first hour of it to the last


def test_a_thousand_twins_are_worth_far_fewer_separate_ones():
    """Two twins slid a day apart are nearly the same book. Here the twins are made to order, first
    as blocks: k groups of twins, each group one book. They are worth k."""
    room = 24_000
    by = np.random.default_rng(1).integers(720, 720 + room, size=400)

    def blocks(k, seed, loud=False):
        rng = np.random.default_rng(seed)
        books = rng.normal(size=(k, 600)) * (rng.uniform(0.5, 3.0, size=(k, 1)) if loud else 1.0)
        return books[np.minimum((by - 720) * k // room, k - 1)] + 0.05 * rng.normal(size=(len(by), 600))
    for k in (2, 3, 4, 8, 16, 30):
        got = [bench.separate(by, blocks(k, seed)) for seed in range(4)]
        assert k * 0.85 < np.mean(got) < k * 1.1, (k, got)
    # A loud twin counts as one and no more: blocks that differ in how much they move are still k, or a little under.
    # Without the step that puts each twin in units of its own spread, eight such blocks read five and sixteen read ten
    for k in (4, 8, 16):
        got = [bench.separate(by, blocks(k, seed, loud=True)) for seed in range(4)]
        assert k * 0.8 < np.mean(got) < k * 1.1, (k, got)

    # Books that keep to the clock. Slid a week further, a book that holds at weekends is the same book again: its twins
    # are a few books taking turns, and likeness comes back with distance. Counted only out to where likeness first ends,
    # two books taking turns every 84 hours read 246 and seven every 24 hours read 369 (found in review, 2026-10-07)
    def in_turns(k, every, seed):
        rng = np.random.default_rng(seed)
        books = rng.normal(size=(k, 600))
        return books[((by - 720) // every) % k] + 0.05 * rng.normal(size=(len(by), 600))
    for k, every in ((2, 84), (4, 42), (7, 24), (4, 500), (3, 2000)):
        got = [bench.separate(by, in_turns(k, every, seed)) for seed in range(3)]
        assert k * 0.9 < np.mean(got) < k * 1.1, (k, every, got)

    # Then as chains, in which two twins a distance d apart are alike by exp(-d / reach): what four hundred twins drawn
    # from such a chain are worth is what a set of that many separate twins would vary by on average, 1 / (1 / 400 +
    # the average likeness of two places in the room)
    def chained(reach, seed):
        rng = np.random.default_rng(seed)
        order = np.argsort(by)
        gaps = np.empty((len(by), 600))
        gaps[order[0]] = rng.normal(size=600)
        for a, b in zip(order[:-1], order[1:]):
            keep = math.exp(-(by[b] - by[a]) / reach)
            gaps[b] = keep * gaps[a] + math.sqrt(1.0 - keep * keep) * rng.normal(size=600)
        return gaps
    for reach in (100.0, 400.0, 1500.0):
        x = room / reach
        want = 1.0 / (1.0 / 400 + (2.0 / x) * (1.0 - (1.0 - math.exp(-x)) / x))
        got = [bench.separate(by, chained(reach, seed)) for seed in range(4)]
        assert want * 0.8 < np.mean(got) < want * 1.2, (reach, want, got)
    # the bench hands it each twin's days less the average twin's, and it is all one whether it does or not
    raw = chained(400.0, 0)
    assert bench.separate(by, raw - raw.mean(axis=0)) == pytest.approx(bench.separate(by, raw), rel=1e-9)
    # twins that do not differ at all are one twin, twins with nothing in common are as many as there are, and of
    # two or one there is nothing to work out
    same = np.tile(np.random.default_rng(2).normal(size=600), (400, 1))
    assert bench.separate(by, same) == 1.0 and bench.separate(by, np.zeros((400, 600))) == 1.0
    assert bench.separate(by, np.random.default_rng(4).normal(size=(400, 600))) > 380.0
    assert bench.separate(by[:2], raw[:2]) == pytest.approx(2.0, abs=0.02) and bench.separate(by[:1], raw[:1]) == 1.0
    assert bench.separate(by[:0], raw[:0]) == 1.0 and bench.separate(by[:2], np.vstack([raw[0], raw[0]])) == 1.0
    # A handful of twins is too few to see where likeness ends, and is counted by the likeness it has: six with nothing in
    # common are six, six that are two books are two. They used to be six whatever they were (found in review, 2026-10-07)
    assert bench.separate(by[:6], np.random.default_rng(5).normal(size=(6, 600))) == pytest.approx(6.0, abs=0.1)
    pair_of_books = np.random.default_rng(6).normal(size=(2, 600))
    assert bench.separate(by[:6], pair_of_books[[0, 1, 0, 1, 1, 0]] + 0.01 * np.random.default_rng(7).normal(size=(6, 600))) == pytest.approx(2.0, abs=0.05)
    assert bench.separate(by[:9], np.random.default_rng(8).normal(size=(9, 600))) == pytest.approx(9.0, abs=0.2)
    # likeness taken everywhere is the cap and not the count: where it dies away with distance it reads about double
    assert bench.separate(by, chained(400.0, 1)) < 0.7 * (1.0 + 400.0 ** 2 / ((np.corrcoef(chained(400.0, 1)) ** 2).sum() - 400.0 * 399.0 / 598.0))

    # The second count, step by step as its text has it, on six twins that are two books of unequal loudness with a little
    # of their own: each twin's days taken to the average twin's and to its own average, put in units of its own spread,
    # taken to the average once more; likeness is the product of two twins' days summed; the count is one more than the
    # square of the summed likeness of each with itself over the summed squares of all, less what chance alone gives,
    # which is n (n - 1) times the summed squares of what each day carries. Six twins are too few for the first count
    def by_the_book(g, again=True):
        z = g - g.mean(axis=0)
        z = z - z.mean(axis=1, keepdims=True)
        z = z / np.sqrt((z ** 2).sum(axis=1, keepdims=True))
        z = z - z.mean(axis=0) if again else z
        like = z @ z.T
        allowed = len(g) * (len(g) - 1) * float((((z ** 2).mean(axis=0)) ** 2).sum())
        return 1.0 + float(np.trace(like)) ** 2 / (float((like ** 2).sum()) - allowed)
    rng = np.random.default_rng(21)
    six = rng.normal(size=(2, 40))[[0, 1, 0, 0, 1, 0]] * np.array([1.0, 3.0, 1.0, 1.0, 3.0, 1.0])[:, None] + 0.3 * rng.normal(size=(6, 40))
    assert bench.separate(by[:6], six) == pytest.approx(by_the_book(six), rel=1e-9) and 1.5 < by_the_book(six) < 4.0
    assert abs(by_the_book(six, again=False) - by_the_book(six)) > 0.005     # each step is in it: without the last it is not the same number
    # A twin's own average is no part of its likeness to another: twins that are eight books, each twin with a level of
    # its own far wider than its days, are still eight (with the level left in they read two or three)
    for k in (4, 8):
        got = [bench.separate(by, blocks(k, seed) + 5.0 * np.random.default_rng(50 + seed).normal(size=(400, 1))) for seed in range(3)]
        assert k * 0.85 < np.mean(got) < k * 1.1, (k, got)
    # A market's days are not of a size, and twins with nothing else in common are alike in having been through the wild
    # ones. With the allowance for that reckoned as if every day weighed the same, four hundred such twins read forty,
    # and the live books' twins were cut by up to half (found in review, 2026-10-07)
    wild = np.exp(np.random.default_rng(0).normal(size=(1, 600)))
    for power in (1.0, 1.5):
        got = [bench.separate(by, np.random.default_rng(seed).normal(size=(400, 600)) * wild ** power) for seed in range(3)]
        assert np.mean(got) > 360.0, (power, got)
    # a twin slid nearly all the way round and one slid hardly at all are near each other: two groups of twins, one book each
    # way round the join, are two blocks only when the distance between them is taken round the circle
    ends = np.r_[np.random.default_rng(6).integers(0, 2000, 200), np.random.default_rng(7).integers(22_000, 24_000, 200)]
    middle = np.random.default_rng(8).integers(10_000, 14_000, 400)
    spots = np.r_[ends, middle]
    rng = np.random.default_rng(9)
    two = np.vstack([np.tile(rng.normal(size=600), (400, 1)), np.tile(rng.normal(size=600), (400, 1))]) + 0.05 * rng.normal(size=(800, 600))
    assert bench.separate(spots, two, around=24_000) == pytest.approx(2.0, abs=0.1)
    # The same for likeness that falls away slowly: twins made from each day's noise smoothed round the whole circle, so
    # that two of them are alike by how far apart they are slid the short way round. What they are worth is again what
    # that many separate twins would vary by. Measured the long way round, the farthest pairs are the nearest, and the
    # count comes out half as much again for the slowest of these
    def round_the_circle(reach, seed, places=240):
        rng = np.random.default_rng(seed)
        apart = np.minimum(np.arange(places), places - np.arange(places)) * (room / places)
        kernel = np.fft.fft(np.exp(-apart / reach))
        field = np.real(np.fft.ifft(np.fft.fft(rng.normal(size=(600, places)), axis=1) * kernel[None, :], axis=1))
        alike = np.real(np.fft.ifft(np.abs(kernel) ** 2))
        at = ((by - 720) * places // room) % places
        usual = ((alike / alike[0])[np.abs(at[:, None] - at[None, :])].sum() - len(by)) / (len(by) * (len(by) - 1))
        return field[:, at].T, 1.0 / (1.0 / len(by) + usual)
    for reach, margin in ((300.0, 0.15), (1000.0, 0.15), (2500.0, 0.25)):
        made = [round_the_circle(reach, seed) for seed in range(3)]
        got, want = np.mean([bench.separate(by - 720, g, around=room) for g, _ in made]), np.mean([w for _, w in made])
        assert want * (1 - margin) < got < want * (1 + margin), (reach, want, got)
    # how often luck does as well: the share of the separate twins at or above the book, the book counted as one more
    assert bench.chance(1.0, 9.0) == pytest.approx(0.1) and bench.chance(1.0, 99.0) == pytest.approx(0.01)       # the best there is: one in ten, one in a hundred
    assert bench.chance(0.5, 99.0) == pytest.approx(0.505) and bench.chance(0.0, 50.0) == 1.0 and bench.chance(0.9, 1000.0) == pytest.approx(101 / 1001)
    assert bench.chance(None, 9.0) is None and bench.chance(0.9, None) is None
    # on a book: the twins of one that trades every day or two are worth many, of one that turns over a few times a season few
    hours = 24 * 200
    r = market(hours, seed=11)
    quick_w, quick_c = blind_book(hours, 3, seed=12)
    slow = np.repeat(blind_book(hours // 8 + 1, 3, seed=13)[0], 8, axis=0)[:hours]       # the same kind of book, eight hours for one
    fast_tw = bench.judge(bench.series(path_of(quick_w, r, quick_c)), n=300)
    slow_tw = bench.judge(bench.series(path_of(slow, r)), n=300)
    assert fast_tw["worth"] > 3 * slow_tw["worth"] and 2.0 < slow_tw["worth"] < 40.0 and fast_tw["worth"] <= 300.0


def test_a_run_too_short_to_slide_a_book_inside_has_no_twins(monkeypatch):
    """Thirty days for the least slide, ninety more to draw the slides from, the day of candles the
    strategy is handed and the thirty hours this book holds a pair for: to the hour."""
    def turns(hours):
        w = np.zeros((hours, 2))
        for at in range(0, hours, 60):
            w[at: at + 30, 0], w[at + 30: at + 60, 1] = 0.5, 0.5          # thirty hours in one pair, thirty in the other
        return bench.series(path_of(w, market(hours, pairs=2)))
    least = 30 * 24 + (24 + 30) + 90 * 24
    for hours, has in ((least, False), (least + 1, True)):
        s = turns(hours)
        assert len(s["c"]) == hours - 1 and s["hold"] == 30 and bench.least_hours(s) == least
        assert (bench.judge(s, n=20) is not None) == has and (bench.no_twins(s) is None) == has, hours
    assert bench.reading_of(s, bench.judge(s, n=20))["twins"]["n"] == 20
    # with no room asked for beyond the slide itself, a run that is exactly long enough has one slide to draw, and draws it
    monkeypatch.setattr(bench, "MIN_ROOM_DAYS", 0)
    one = turns(30 * 24 + 54 + 1)
    assert bench.least_hours(one) == len(one["c"]) == 30 * 24 + 54 and (bench.slides(one, 50) == 30 * 24).all()
    two = turns(30 * 24 + 54 + 2)
    assert sorted(set(bench.slides(two, 200).tolist())) == [30 * 24, 30 * 24 + 1]


def test_twins_are_counted_stretch_by_stretch():
    """A book that sees ahead in its second year only: it beats every twin there, and in its first
    year it is one of them."""
    start = int(pd.Timestamp("2024-01-01").timestamp())
    hours = 24 * 730
    r = market(hours, pairs=2, seed=12)
    w, c = blind_book(hours, 2, seed=13)
    w[24 * 366:-1] = (r[24 * 366:] > 0) / 2.0
    s = bench.series(path_of(w, r, c, start=start, runs=True))
    tw = bench.judge(s, n=150)
    assert set(tw["beaten"]) == {"all", "last", "2024", "2025"}
    assert tw["beaten"]["2025"] == 1.0 and tw["beaten"]["last"] == 1.0
    assert 0.02 < tw["beaten"]["2024"] < 0.98
    rows = bench.by_year(s, tw)
    assert [y["year"] for y in rows] == [2024, 2025] and [y["days"] for y in rows] == [366, 364]
    assert rows[1]["twins_beaten"] == 1.0 and rows[1]["timing"] > 1.0 and rows[0]["twins_beaten"] == tw["beaten"]["2024"]
    timing, drift, costs = tw["own"] - tw["gross"], s["gross"] - tw["own"], s["gross"] - s["daily"]
    in_2025 = bench.spans(s["days"])["2025"]
    assert rows[1]["net"] == pytest.approx(np.prod(1 + s["daily"][in_2025]) - 1)
    assert rows[1]["basket"] == pytest.approx(np.prod(1 + s["basket"][in_2025]) - 1)
    assert rows[1]["exposure"] == pytest.approx(s["exposure_daily"][in_2025].mean())
    assert rows[1]["timing"] == pytest.approx(timing[in_2025].sum()) and rows[0]["timing"] == pytest.approx(timing[~in_2025].sum())
    assert rows[1]["drift"] == pytest.approx(drift[in_2025].sum()) and rows[0]["drift"] == pytest.approx(drift[~in_2025].sum())
    assert rows[1]["costs"] == pytest.approx(costs[in_2025].sum()) and rows[1]["costs"] > 0 and abs(rows[0]["drift"]) > 1e-5
    # a year's timing and drift less its costs is what is left of it, and the years add up to the whole
    assert all(y["left"] == pytest.approx(y["timing"] + y["drift"] - y["costs"], abs=1e-12) for y in rows)
    out = bench.reading_of(s, tw)
    assert sum(y["timing"] for y in rows) / 730 * 365 == pytest.approx(out["timing_per_year"])
    assert sum(y["drift"] for y in rows) / 730 * 365 == pytest.approx(out["drift_per_year"])
    assert sum(y["left"] for y in rows) / 730 * 365 == pytest.approx(out["left_per_year"])
    bare = bench.by_year(s, None)
    assert bare[0]["twins_beaten"] is None and bare[0]["timing"] is None and bare[0]["drift"] is None and bare[0]["left"] is None
    assert bare[0]["net"] == rows[0]["net"]
    # a year needs thirty days to be read by itself: one with twenty nine is not a row
    assert bench.MIN_DAYS == 30
    assert [y["year"] for y in bench.by_year(bench.series(path_of(w[: 24 * 396 + 1], r[: 24 * 396], c[: 24 * 396 + 1], start=start)), None)] == [2024, 2025]
    assert [y["year"] for y in bench.by_year(bench.series(path_of(w[: 24 * 395 + 1], r[: 24 * 395], c[: 24 * 395 + 1], start=start)), None)] == [2024]


def test_timing_and_drift_less_costs_is_what_is_left():
    """The four figures a reading turns on, each by hand. Timing: the book as it last traded each pair
    less its average twin, before costs, a year; it is the figure the twins are ranked on. Drift: what
    letting positions run between trades added to that, which no twin has. Costs: what its fills took
    from its days. Left: its return after costs less its average twin's before any. Timing used to be
    printed with the drift in it, and a book that bought once and sat read `timing +8.8% a year` beside
    a share of twins beaten of exactly a half (found in review, 2026-10-07)."""
    hours = 24 * 160
    r = clustered(hours, 3, 21)
    w, c = follower(r)
    s = bench.series(path_of(w, r, c, memory=48, runs=True))
    tw = bench.judge(s, n=200)
    out = bench.reading_of(s, tw)
    assert out["timing_per_year"] == pytest.approx((tw["own"] - tw["gross"]).mean() * 365)
    assert out["drift_per_year"] == pytest.approx((s["gross"] - tw["own"]).mean() * 365) and abs(out["drift_per_year"]) > 1e-4
    assert out["costs_per_year"] == pytest.approx((s["gross"] - s["daily"]).mean() * 365) and out["costs_per_year"] > 0.05
    assert out["left_per_year"] == pytest.approx((s["daily"] - tw["gross"]).mean() * 365)
    assert out["timing_per_year"] + out["drift_per_year"] - out["costs_per_year"] == pytest.approx(out["left_per_year"], abs=1e-12)      # to the last digit
    assert out["twin_gross_per_year"] == pytest.approx(tw["gross"].mean() * 365)
    left = s["daily"] - tw["gross"]
    assert out["sharpe"] == pytest.approx(left.mean() / left.std(ddof=1) * math.sqrt(365)) and out["t"] == pytest.approx(t_of(left))
    assert out["twins"] == {"n": 200, "beaten": tw["beaten"]["all"], "beaten_last_365": None, "net_middle": tw["net_middle"], "worth": tw["worth"],
                            "chance": bench.chance(tw["beaten"]["all"], tw["worth"]), "in_place": []}
    assert out["exposure"] == pytest.approx(s["held"].sum(axis=1).mean()) and out["pairs"] == ["P0", "P1", "P2"] and out["no_twins"] is None
    # the timing is that of the book as last traded: the same book set back to its weights every hour has the same, and no drift
    level = bench.series(path_of(w, r, c, memory=48))
    flat_out = bench.reading_of(level, bench.judge(level, n=200))
    assert flat_out["timing_per_year"] == pytest.approx(out["timing_per_year"], abs=1e-12) and flat_out["drift_per_year"] == pytest.approx(0.0, abs=1e-12)
    assert flat_out["twins"]["beaten"] == out["twins"]["beaten"]
    # the same book trading for nothing: the same timing and drift, nothing taken, and all of it left
    free = bench.series(path_of(w, r, memory=48, runs=True))
    alone = bench.reading_of(free, bench.judge(free, n=200))
    assert alone["costs_per_year"] == 0.0 and alone["left_per_year"] == pytest.approx(alone["timing_per_year"] + alone["drift_per_year"])


def test_a_reading_shows_what_its_best_and_worst_days_carry():
    """Half a percent of the days at each end, and at least one. It is shown and nothing is ruled on
    it: taking its ten best days away from five years of anything leaves less, and with a real edge
    worth a yearly Sharpe ratio of 1 the old line `without its 10 best days the skill is gone` came up
    in most samples (found in review, 2026-10-07)."""
    x = np.zeros(1000)
    x[[5, 6, 50, 700, 701, 702]] = [0.10, 0.05, -0.20, 0.03, 0.02, -0.01]
    got = bench.tails(x)
    assert got["days"] == 5 and bench.TAIL_SHARE == 0.005
    assert got["best"] == pytest.approx((0.10 + 0.05 + 0.03 + 0.02) / 1000 * 365) and got["worst"] == pytest.approx((-0.20 - 0.01) / 1000 * 365)
    assert bench.tails(np.arange(100.0))["days"] == 1 and bench.tails(np.arange(300.0))["days"] == 2 and bench.tails(np.arange(1825.0))["days"] == 9
    assert bench.tails(np.arange(30.0)) == {"days": 1, "best": pytest.approx(29 / 30 * 365), "worst": 0.0}
    assert bench.tails(np.arange(29.0)) == {"days": 0, "best": 0.0, "worst": 0.0}       # too few days to have ends
    text = bench.format_reading(a_reading(tails={"days": 9, "best": 0.148, "worst": -0.147}))
    assert "its best and worst days: of what is left, its 9 best days carry +14.8% a year and its 9 worst -14.7%" in text
    assert "its best and worst days" not in bench.format_reading(a_reading(tails={"days": 0, "best": 0.0, "worst": 0.0}))
    assert "best days" not in " ".join(bench.weak_spots(a_reading(tails={"days": 9, "best": 0.5, "worst": -0.01}, left_per_year=0.1)))


def test_the_live_rules_counts_are_taken_window_by_window():
    """Had a test begun on each day of the run from a year in: a trade of its own by day 60, 30 fills
    and a daily skill t of 1.0 by day 120, each counted here the long way round."""
    days = 520
    hours = 24 * days + 1
    r = market(hours, pairs=3, seed=41, vol=0.006)
    w, c = blind_book(hours, 3, seed=42)
    w[24 * 400: 24 * 470] = 0.0                                           # ten weeks in which it does nothing at all
    w[: 24 * 380, 2] = 0.0                                                # the third pair is listed in the run's second year
    c = np.r_[0.0, np.abs(np.diff(w, axis=0)).sum(axis=1) * 0.0015]
    path = path_of(w, r, c, late={2: 24 * 380})
    path["exits"] = np.array(sorted([T0 + DAY * d + 7 * HOUR for d in list(range(3, 395, 9)) + [471, 500]]
                                    + [T0 + DAY * 396 + HOUR, T0 + DAY * 460]), dtype="int64")      # one in a day's first hour, one on the stroke of a sixtieth day
    s = bench.series(path)
    rules = {"first_days": 60, "total_days": 120, "min_fills": 30, "min_t": 1.0, "fast_t": 0.5}
    got = bench.looks(s, rules)
    left_one, enough, t_first, t_total, quick = [], [], [], [], []
    for d in range(365, days - 120 + 1):
        usual = s["exposure_daily"][d - 365: d].mean()                    # what it usually held: the year before the test began
        listed = s["listed"][d]
        level = np.cumprod(1.0 + s["by_pair"][d: d + 120][:, listed], axis=0).mean(axis=1)      # equal parts on day one, never set back
        basket = level / np.r_[1.0, level[:-1]] - 1.0
        skill = s["daily"][d: d + 120] - usual * basket
        opened = int(s["days"][d]) * DAY
        left_one.append(any(opened < e <= opened + 60 * DAY for e in path["exits"]))
        enough.append(s["fills"][d: d + 120].sum() >= 30)
        t_first.append(t_of(skill[:60]))
        t_total.append(t_of(skill))
        quick.append(left_one[-1] and s["fills"][d: d + 60].sum() >= 30 and t_first[-1] >= 0.5)
    left_one, enough, t_total = np.array(left_one), np.array(enough), np.array(t_total)
    assert got["windows"] == len(t_total) == 36 and got["apart"] == 1
    # window by window first, then the counts over them
    each = bench.windows(s, rules)
    assert list(each["begin"]) == list(range(365, days - 120 + 1)) and (each["left_one"] == left_one).all()
    assert each["usual"] == pytest.approx([s["exposure_daily"][d - 365: d].mean() for d in range(365, days - 120 + 1)], abs=1e-12)
    assert each["t_total"] == pytest.approx(t_total, abs=1e-9) and each["t_first"] == pytest.approx(t_first, abs=1e-9)
    assert list(each["fills_total"]) == [s["fills"][d: d + 120].sum() for d in each["begin"]]
    assert list(each["fills_first"]) == [s["fills"][d: d + 60].sum() for d in each["begin"]]
    assert got["no_trade"] == pytest.approx((~left_one).mean()) and 0 < got["no_trade"] < 1
    assert got["few_fills"] == pytest.approx((~enough).mean())
    assert got["t_middle"] == pytest.approx(np.median(t_total)) and got["t_reached"] == pytest.approx((t_total >= 1.0).mean())
    assert got["all_counts"] == pytest.approx((left_one & enough & (t_total >= 1.0)).mean())
    assert got["fast_pass"] == pytest.approx(np.mean(quick))
    assert bench.looks(s, dict(rules, fast_t=None))["fast_pass"] is None
    assert bench.looks(s, dict(rules, min_fills=10 ** 6))["few_fills"] == 1.0 and bench.looks(s, dict(rules, min_fills=10 ** 6))["all_counts"] == 0.0
    assert bench.looks(s, dict(rules, min_t=-99.0))["t_reached"] == 1.0
    # each count to the letter: the fills a promotion needs are enough, the t it asks for is reached, and an exit on
    # the stroke of the first look counts where one an hour later does not
    most, best = int(each["fills_total"].max()), float(each["t_total"].max())
    assert bench.looks(s, dict(rules, min_fills=most))["few_fills"] == pytest.approx(1 - (each["fills_total"] == most).mean())
    assert bench.looks(s, dict(rules, min_fills=most))["few_fills"] < 1.0
    assert bench.looks(s, dict(rules, min_fills=most + 1))["few_fills"] == 1.0
    assert bench.looks(s, dict(rules, min_t=best))["t_reached"] == pytest.approx(1 / 36)
    first_best, first_most = float(each["t_first"].max()), int(each["fills_first"][np.argmax(each["t_first"])])
    one = bench.looks(s, dict(rules, min_fills=first_most, fast_t=first_best))["fast_pass"]
    assert one == pytest.approx(float(each["left_one"][np.argmax(each["t_first"])]) / 36)
    assert bench.looks(s, dict(rules, min_fills=first_most + 1, fast_t=first_best))["fast_pass"] == 0.0
    opens_on = {int(d): bool(x) for d, x in zip(each["begin"], each["left_one"])}
    assert opens_on[396] and not opens_on[397]                            # the exit an hour into day 396 is inside the window that opens that day, and no later one
    assert opens_on[400] and not opens_on[399]                            # the exit at midnight sixty days on is inside the window that ends there
    assert math.isnan(bench._t(np.array([0.01]))) and math.isnan(bench._t(np.full(40, 0.01))) and bench._t(np.array([0.01, 0.03])) == pytest.approx(t_of(np.array([0.01, 0.03])))
    # a run with no whole window after its first year has none
    short = bench.series(path_of(w[: 24 * 484 + 1], r[: 24 * 484], c[: 24 * 484 + 1]))
    assert bench.looks(short, rules) is None and bench.windows(short, rules) is None
    assert bench.looks(bench.series(path_of(w[: 24 * 485 + 1], r[: 24 * 485], c[: 24 * 485 + 1])), rules)["windows"] == 1
    # and the counts are the ones the hourly loop reads from configs/risk.yaml
    assert bench.live_rules(RCFG) == {"first_days": 60, "total_days": 120, "min_fills": 30, "min_t": 1.0, "fast_t": None}
    asked = bench.live_rules(dict(RCFG, challenger={"window_days": 45, "confirm_days": 30, "min_trades": 12, "min_skill_t": 1.5, "fast_pass_skill_t": 2.5}))
    assert asked == {"first_days": 45, "total_days": 75, "min_fills": 12, "min_t": 1.5, "fast_t": 2.5}


def test_a_windows_basket_and_its_daily_skill_t_are_the_live_rules_own(root, monkeypatch):
    """The bench says it takes a window's daily skill t as the live rule takes it. Here the live rule's
    own functions (bot/promote.py: `market_context` for the basket, `skill_t` for the t) are run on
    windows cut from the same record: the account's equity as the hourly loop writes it, the market's
    candles as it reads them. The basket is the same to the last digit. The t differs only by where a
    day ends: on the account's last reading of the day for the live rule, at midnight an hour later for
    the bench. (The earlier test of these counts set the bench against its own sum, and nothing tied
    either to the rule; found in review, 2026-10-07.)"""
    from bot import paper, promote
    days = 520
    hours = 24 * days + 1
    r = market(hours, pairs=3, seed=41, vol=0.006)
    w, _ = blind_book(hours, 3, seed=42)
    w[: 24 * 380, 2] = 0.0                                                # the third pair is listed in the run's second year
    c = np.r_[0.0, np.abs(np.diff(w, axis=0)).sum(axis=1) * 0.0015]
    path = path_of(w, r, c, late={2: 24 * 380})
    s = bench.series(path)
    rules = {"first_days": 60, "total_days": 120, "min_fills": 30, "min_t": 1.0, "fast_t": None}
    each = bench.windows(s, rules)
    paper.append_rows(config.account_dir("challenger1") / "equity.csv", paper.EQUITY_FIELDS,
                      [{"ts": int(t), "equity": float(e)} for t, e in zip(path["ts"], path["equity"])])
    ts, opens = path["ts"], path["opens"]
    candles = {}
    for j in range(3):                                                    # a candle is stamped with its open and closes at the next hour's price
        there = np.isfinite(opens[:-1, j]) & np.isfinite(opens[1:, j])
        candles[f"P{j}"] = pd.DataFrame({"time": ts[:-1][there], "close": opens[1:, j][there]})
    monkeypatch.setattr(data, "load_all_candles", lambda pair: candles[pair])
    apart = []
    for i in (0, 9, 20, 27, 35):
        d = int(each["begin"][i])
        start = int(s["days"][d]) * DAY
        mc = promote.market_context(start, start + 120 * DAY, ["P0", "P1", "P2"])
        listed = s["listed"][d]
        held = np.prod(1.0 + s["by_pair"][d: d + 120][:, listed], axis=0)  # each pair listed on day one, bought then and held
        assert mc["pairs"] == listed.sum() == (3 if d >= 380 else 2) and mc["basket_return"] == pytest.approx(held.mean() - 1.0, abs=1e-9)
        t, n = promote.skill_t("challenger1", start, start + 120 * DAY, None, {"skill_exposure": float(each["usual"][i])}, mc["basket_path"])
        assert n == 120
        apart.append(t - each["t_total"][i])
    assert np.abs(apart).max() < 0.1 and abs(np.mean(apart)) < 0.05, apart       # 0.03 at the most, on these
    # and that is not a bound anything would meet: at another exposure the same window's t is somewhere else
    other, _ = promote.skill_t("challenger1", start, start + 120 * DAY, None, {"skill_exposure": float(each["usual"][i]) + 1.0}, mc["basket_path"])
    assert abs(other - each["t_total"][i]) > 0.2


# --- the settings and the coins either side ------------------------------------------------

def test_nearby_settings_move_every_number_a_little_and_nothing_else():
    params = {"lookback_hours": 240, "entry_z": 2.0, "exit_return": -0.01, "fresh": True, "mode": "fast", "none": 0,
              "tiny_hours": 1, "share": 0.25, "floor": 0.0, "steps": -4}
    near = bench.nearby(params)
    assert len(near) == bench.NEARBY == 6 and bench.NEARBY_SPREAD == 0.25
    assert near == bench.nearby(params) and near != bench.nearby(params, seed=1)
    seen = set()
    for p in near:
        assert set(p) == set(params) and p != params
        assert p["fresh"] is True and p["mode"] == "fast" and p["none"] == 0 and p["floor"] == 0.0
        assert isinstance(p["lookback_hours"], int) and 240 / 1.25 - 1 <= p["lookback_hours"] <= 240 * 1.25 + 1
        assert isinstance(p["tiny_hours"], int) and p["tiny_hours"] >= 1          # never rounded away to nothing
        assert isinstance(p["steps"], int) and -5 <= p["steps"] <= -3
        assert 2.0 / 1.25 <= p["entry_z"] <= 2.0 * 1.25 and -0.0125 <= p["exit_return"] <= -0.008
        assert 0.2 <= p["share"] <= 0.3125
        seen.add(json.dumps(p, sort_keys=True))
    assert len(seen) == 6
    moved = [p["lookback_hours"] for seed in range(4) for p in bench.nearby(params, seed=seed)]
    assert min(moved) < 240 < max(moved)                                  # both ways (over four sets of them: one set of six can fall on one side)
    assert all(a["lookback_hours"] != b["lookback_hours"] or a["entry_z"] != b["entry_z"] for a in near for b in near if a is not b)
    assert bench.nearby({"mode": "fast", "on": True}) == [] and bench.nearby({}) == []
    assert bench.nearby({"n": 1}) == []                                   # a quarter either way of 1 is still 1: there is no setting near it
    threes = [p["n"] for p in bench.nearby({"n": 3})]                     # a quarter either way of 3 is 2 or 4, and copies that
    assert 1 <= len(threes) == len(set(threes)) and set(threes) <= {2, 4}     # come out alike are given once
    assert {p["n"] for seed in range(8) for p in bench.nearby({"n": 3}, seed=seed)} == {2, 4}
    assert all(isinstance(p["x"], float) for p in bench.nearby({"x": 3.0})) and len(bench.nearby({"x": 3.0})) == 6
    assert params["lookback_hours"] == 240 and params["entry_z"] == 2.0   # the config's own are left as they were


def test_the_pairs_are_halved_two_ways():
    assert bench.halves(["D", "B", "A", "C", "E"]) == [["A", "C", "E"], ["B", "D"], ["A", "B", "C"], ["D", "E"]]
    four = bench.halves(["b", "a", "d", "c"])
    assert four == [["a", "c"], ["b", "d"], ["a", "b"], ["c", "d"]]
    assert bench.halves(["a", "b", "c"]) == [] and bench.halves([]) == []


# --- strategies for the tests ---------------------------------------------------------------

def rising(candles, params, held):
    """Hold a pair while its close is above its close some hours back. Knows nothing of the clock."""
    look = int(params.get("look_hours", 12))
    need = int(params.get("need", look + 2))
    out = {}
    for pair, df in candles.items():
        close = df["close"].to_numpy()
        if len(close) < need:
            out[pair] = strategy.Target(0.0, f"flat: only {len(close)} candles, need {need}")
        else:
            up = close[-1] > close[-1 - look] * (1.0 + float(params.get("band", 0.0)) * (-1 if held.get(pair, 0) > 0 else 1))
            out[pair] = strategy.Target(float(params.get("size", 0.2)) if up else 0.0, "rising" if up else "flat: not rising")
    return out


def stamp(df):
    """When the newest candle opened. A helper, so that the strategies below do not name the column themselves."""
    return pd.Timestamp(int(df[STAMP].iloc[-1]), unit="s")


STAMP = "ti" + "me"
MEMORY = {"calls": 0}


def fridays(candles, params, held):
    """Buy on Fridays, sell on Mondays: a rule with a rhythm, read through a helper."""
    return {pair: strategy.Target(0.2 if stamp(df).dayofweek in (4, 5, 6) else 0.0, "the weekend") for pair, df in candles.items()}


def noon(candles, params, held):
    """Exits only: lets go of what it holds at noon. Its rhythm shows only while it holds."""
    return {pair: strategy.Target(0.2 if held.get(pair, 0) > 0 and stamp(df).hour != 12 else 0.0, "until noon")
            for pair, df in candles.items()}


def monthly(candles, params, held):
    """Holds for the first hour of each month: a rhythm too rare to land on by asking."""
    out = {}
    for pair, df in candles.items():
        at = pd.Timestamp(int(df["time"].iloc[-1]), unit="s")
        out[pair] = strategy.Target(0.2 if at.day == 1 and at.hour == 0 else 0.0, "the first hour of the month")
    return out


def broken(candles, params, held):
    raise RuntimeError("no")


def sometimes(candles, params, held):
    """Fails one hour in fifty, and is `rising` in the others."""
    if (int(next(iter(candles.values()))[STAMP].iloc[-1]) // HOUR) % 50 == 0:
        raise RuntimeError("not this hour")
    return rising(candles, params, held)


def quits(candles, params, held):
    """Asks the interpreter to stop, which is not an Exception."""
    raise SystemExit(0)


def dies(candles, params, held):
    """Takes its process down with it."""
    os._exit(7)


def fiddles(candles, params, held):
    """Writes to the params it is handed."""
    params.setdefault("look_hours", 12)
    params["calls"] = params.get("calls", 0) + 1
    return rising(candles, params, held)


def remembers(candles, params, held):
    """Keeps count of its calls in its module and trades smaller after the first three hundred: what it
    does depends on what else has run in its process."""
    MEMORY["calls"] += 1
    return rising(candles, dict(params, size=float(params.get("size", 0.2)) * (1.0 if MEMORY["calls"] <= 300 else 0.25)), held)


def slow(candles, params, held):
    time.sleep(0.2)
    return {pair: 0.0 for pair in candles}


def ambles(candles, params, held):
    """Takes three seconds and more over a replay of 900 hours."""
    time.sleep(0.004)
    return rising(candles, params, held)


def _nothing():
    pass


def forks(candles, params, held):
    """Starts a process of its own now and then, as a strategy that does its sums in a pool would."""
    MEMORY["calls"] += 1
    if MEMORY["calls"] % 100 == 1:
        child = multiprocessing.get_context("fork").Process(target=_nothing)
        child.start()
        child.join()
    return rising(candles, params, held)


def lingers(candles, params, held):
    """Leaves a thread behind it that outlives the replay: its process cannot end until the thread has."""
    if not MEMORY.get("left"):
        MEMORY["left"] = True
        threading.Thread(target=time.sleep, args=(60,)).start()
    return rising(candles, params, held)


def hides(candles, params, held):
    """Shuts everything its process has open, the way out included, and stays."""
    os.closerange(3, 256)
    time.sleep(60)
    return {}


def chatty(candles, params, held):
    """Prints as it goes."""
    print("the strategy says: still here")
    return rising(candles, params, held)


def sits(candles, params, held):
    """Buys a fifth of the book in every pair it is shown and never changes its mind: what it holds is what it wants."""
    return {pair: strategy.Target(held.get(pair) or 0.2, "what it has") for pair in candles}


def turns_about(candles, params, held):
    """Never out of a pair: a quarter of the book in each for twelve hours of the day and a tenth for the other
    twelve, the pairs taking it in turns."""
    out = {}
    for k, (pair, df) in enumerate(sorted(candles.items())):
        up = (int(df[STAMP].iloc[-1]) // HOUR // 12 + k) % 2 == 0
        out[pair] = strategy.Target(0.25 if up else 0.10, "its turn" if up else "not its turn")
    return out


def turns_about_and_notes(candles, params, held):
    """The same book, from a strategy that keeps a note in its params."""
    params["noted"] = True
    return turns_about(candles, params, held)


def ties_a_knot(candles, params, held):
    """The same book again, from a strategy that puts its params inside themselves."""
    params["me"] = params
    return turns_about(candles, params, held)


def orphans(candles, params, held):
    """Starts a process that outlives it, and dies: the process left behind holds its pipe open."""
    multiprocessing.get_context("fork").Process(target=time.sleep, args=(40,)).start()
    os._exit(3)


OURS = {"sits": sits, "turns_about": turns_about, "turns_about_and_notes": turns_about_and_notes, "ties_a_knot": ties_a_knot,
        "orphans": orphans, "ambles": ambles, "rising": rising, "fridays": fridays, "noon": noon, "monthly": monthly, "broken": broken, "sometimes": sometimes,
        "quits": quits, "dies": dies, "fiddles": fiddles, "remembers": remembers, "slow": slow, "forks": forks, "lingers": lingers,
        "hides": hides, "chatty": chatty}


@pytest.fixture
def strategies(monkeypatch):
    for name, fn in OURS.items():
        monkeypatch.setitem(strategy.STRATEGIES, name, fn)
    monkeypatch.setitem(MEMORY, "calls", 0)
    monkeypatch.setitem(MEMORY, "left", False)


@pytest.fixture
def small(monkeypatch):
    """Twins on a run of a few weeks, so that a test can go through the engine in a second or two: a
    slide of five days or more, drawn from five days of room or more."""
    monkeypatch.setattr(bench, "MIN_SLIDE_DAYS", 5)
    monkeypatch.setattr(bench, "MIN_ROOM_DAYS", 5)


def made_up(n=1500, pairs=("AAA", "BBB", "CCC", "DDD"), seed=5):
    src = data.SyntheticSource(list(pairs), n=n, seed=seed, start=T0)
    return {p: src.ohlc(p) for p in pairs}


def cfg_of(name, **params):
    return {"hypothesis": "H9", "strategy": name, "params": params}


def test_a_strategy_is_asked_whether_the_clock_can_matter_to_it(strategies):
    c = made_up(600)
    assert bench.reads_clock(cfg_of("rising", look_hours=12), RCFG, c) is None
    assert bench.reads_clock(cfg_of("fridays"), RCFG, c) == bench.TARGETS_MOVE == "its targets change when the clock is moved"
    assert bench.reads_clock(cfg_of("noon"), RCFG, c) == bench.TARGETS_MOVE            # seen only when it is asked while holding
    # a rhythm too rare for the asking to land on is found in the strategy's own code, and only there
    assert bench.reads_clock(cfg_of("monthly"), RCFG, c) == bench.CODE_NAMES_IT == "its code names the candles' time column or asks the time"
    assert bench.names_the_clock(monthly) and not any(bench.names_the_clock(fn) for fn in (rising, fridays, noon, broken, sometimes, stamp))
    # one that cannot answer is looked at harder, not less, whichever way it fails
    assert bench.reads_clock(cfg_of("broken"), RCFG, c) == "it could not be asked (RuntimeError: no)"
    assert bench.reads_clock(cfg_of("quits"), RCFG, c) == "it could not be asked (SystemExit: 0)"
    assert bench.reads_clock(cfg_of("rising"), RCFG, {}) is None and bench.reads_clock(cfg_of("fridays"), RCFG, {}) is None
    with pytest.raises(KeyError, match="unknown strategy"):
        bench.reads_clock(cfg_of("no_such_strategy"), RCFG, c)
    # the asking hands the strategy copies: what it does to its params or its candles reaches nobody
    cfg = cfg_of("fiddles", size=0.25)
    before = {p: df.copy() for p, df in c.items()}
    assert bench.reads_clock(cfg, RCFG, c) is None and cfg == cfg_of("fiddles", size=0.25)
    assert all(c[p].equals(before[p]) for p in c)
    # the clock is moved by other weekdays and other hours, never by a whole number of weeks or days
    assert all(h % 24 and (h // 24) % 7 for h in bench.PROBE_SHIFTS_H + bench.CLOCK_SHIFTS_H)
    assert sorted({(h // 24) % 7 for h in bench.CLOCK_SHIFTS_H}) == [1, 2, 3, 4, 5, 6]      # every other weekday
    assert bench.PROBE_HOURS == 24


def test_a_strategys_code_is_read_as_code_and_a_word_in_a_comment_is_not_a_finding(tmp_path, monkeypatch):
    """The reading used to be a search of the function's text, comments and all, for the word. A
    comment that said `"time"` then made a strategy out to read the clock, and a helper that did read
    it went unseen (found in review, 2026-10-07)."""
    (tmp_path / "made_up_strategies.py").write_text('''
import datetime

def newest(df):
    return df["time"].iloc[-1]


def close(df):
    return df["close"].iloc[-1]


def a(candles, params, held):      # the "time" of day matters here, says the comment, and df.time too
    """It names the time in its docstring, "time" and all, and nowhere else."""
    lifetime, times, word = 3, "timeout", "in time"
    return {p: close(df) * lifetime for p, df in candles.items()}


def b(candles, params, held):
    return {p: newest(df) for p, df in candles.items()}             # through a helper


def c(candles, params, held):
    return {p: df.time.iloc[-1] for p, df in candles.items()}


def d(candles, params, held):
    return {p: datetime.datetime.now().hour for p in candles}       # the clock on the wall


def e(candles, params, held):
    return {p: by_way_of(df) for p, df in candles.items()}


def by_way_of(df):
    return through(df)


def through(df):
    return newest(df)


def f(candles, params, held):
    lined_up = {p: df.set_index("time")["close"] for p, df in candles.items()}      # names it, and has no rhythm
    return {p: 0.2 for p in lined_up}


COLUMN = "time"
OTHER = "close"


def g(candles, params, held):
    return {p: df[COLUMN].iloc[-1] for p, df in candles.items()}      # by a name the module has given it


def h(candles, params, held):
    import time as clock
    return {p: clock.gmtime().tm_wday for p in candles}               # the clock on the wall, by another door


def i(candles, params, held):
    return {p: df[OTHER].iloc[-1] for p, df in candles.items()}       # a name the module has given another column


STAMPED: str = "time"
FIRST, SECOND = "time", "close"
COLUMNS = ["time", "close"]


def j(candles, params, held):
    return {p: df[STAMPED].iloc[-1] for p, df in candles.items()}     # a name given with its kind written out


def k(candles, params, held):
    return {p: df[FIRST].iloc[-1] for p, df in candles.items()}       # one of two names given at once


def l(candles, params, held):
    return {p: df[SECOND].iloc[-1] for p, df in candles.items()}      # the other of the two, which is another column


def m(candles, params, held):
    return {p: df[COLUMNS[0]].iloc[-1] for p, df in candles.items()}  # out of a list


def n(candles, params, held):
    from time import time
    return {p: time() for p in candles}                               # asked for with nothing before the word


def o(candles, params, held):
    import time as clock
    return {p: clock.monotonic() for p in candles}                    # a clock that only counts is a clock


def q(candles, params, held):
    return {p: df.iloc[-1, 0] for p, df in candles.items()}           # the column by where it stands: this the reading cannot see
''')
    monkeypatch.syspath_prepend(str(tmp_path))
    import importlib
    mod = importlib.import_module("made_up_strategies")
    try:
        assert [bench.names_the_clock(getattr(mod, name)) for name in "abcdefghi"] == [False, True, True, True, True, True, True, True, False]
        assert not bench.names_the_clock(mod.close) and bench.names_the_clock(mod.through)
        # the ways to it a second review found unread (2026-10-07), and the one that stays unread: asking the strategy
        # (`reads_clock`) is what catches a column read by where it stands
        assert [bench.names_the_clock(getattr(mod, name)) for name in "jklmnoq"] == [True, True, False, True, True, True, False]
    finally:
        sys.modules.pop("made_up_strategies", None)
    assert not bench.names_the_clock(lambda cs, ps, hs: {}) and not bench.names_the_clock(len)       # nothing to read is not a finding
    # Nor is a file that has changed under the function since it was loaded into something that cannot be read as code at
    # all. That is nothing to read, and it is not an error either: the strategy is then asked (it used to end the reading;
    # found in review, 2026-10-07)
    changed = tmp_path / "made_up_and_changed.py"
    changed.write_text("def s(candles, params, held):\n    return {}\n")
    importlib.invalidate_caches()
    mod = importlib.import_module("made_up_and_changed")
    try:
        assert bench.names_the_clock(mod.s) is False
        changed.write_text("def (:\n")
        os.utime(changed, (time.time() + 5, time.time() + 5))
        assert bench.names_the_clock(mod.s) is False
        # a module too deep to be read as a whole (a sum of twenty thousand terms), whose function can still be read by itself
        changed.write_text("def s(candles, params, held):\n    return {}\n\n\nMANY = " + " + ".join(["1"] * 20000) + "\n")
        os.utime(changed, (time.time() + 7, time.time() + 7))
        assert bench.names_the_clock(mod.s) is False
        changed.write_text("def s(candles, params, held):\n    return {p: df.time.iloc[-1] for p, df in candles.items()}\n")
        os.utime(changed, (time.time() + 9, time.time() + 9))
        assert bench.names_the_clock(mod.s) is True                       # what is read is the file as it stands
    finally:
        sys.modules.pop("made_up_and_changed", None)
    assert bench.CLOCK_WORDS == ("time", "now", "utcnow", "today", "gmtime", "localtime", "ctime", "strftime", "time_ns", "monotonic",
                                 "monotonic_ns", "perf_counter", "perf_counter_ns", "process_time")


# --- the engine's record --------------------------------------------------------------------

def holed(c):
    """A pair listed late, and a pair with two days of candles missing in the middle."""
    out = dict(c)
    out["DDD"] = c["DDD"].iloc[500:].reset_index(drop=True)
    gap = c["BBB"]
    out["BBB"] = pd.concat([gap.iloc[:700], gap.iloc[748:]]).reset_index(drop=True)
    return out


@pytest.mark.parametrize("make", [made_up, lambda: holed(made_up())], ids=["whole", "with holes"])
def test_keeping_the_record_changes_nothing_and_the_record_rebuilds_the_run(strategies, make):
    c = make()
    cfg = cfg_of("rising", look_hours=12, size=0.25)
    plain = backtest.run_backtest(c, cfg, RCFG)
    kept = backtest.run_backtest(c, cfg, RCFG, record=True)
    path = kept.pop("path")
    assert "path" not in plain and kept == plain and plain["n_trades"] > 50
    hours = len(path["ts"])
    assert path["pairs"] == ["AAA", "BBB", "CCC", "DDD"] and path["weights"].shape == path["opens"].shape == (hours, 4)
    assert (np.diff(path["ts"]) > 0).all() and hours == plain["bars"]
    assert path["fills"].sum() == plain["n_trades"] and path["costs"][-1] == pytest.approx(plain["fees"] + plain["slippage"], abs=0.02)
    assert (path["weights"] >= 0).all() and path["weights"].sum(axis=1).max() <= 1.0 + 1e-9
    assert path["memory_hours"] == RCFG["history_hours"] == 200 and path["errors"] == 0 and path["first_error"] is None
    eq, w, px, costs = path["equity"], path["weights"], pd.DataFrame(path["opens"]).ffill().to_numpy(), path["costs"]
    # hour by hour: what the book was worth, moved by the prices of what it held, less what its fills cost
    moved = np.nansum(w[:-1] * (px[1:] / px[:-1] - 1.0), axis=1)
    assert eq[1:] == pytest.approx(eq[:-1] * (1.0 + moved) - np.diff(costs), rel=1e-12)
    s = bench.series(path)
    assert s["gap_bps"] < 1e-6
    assert bench.reading_of(s, None)["net"] == pytest.approx(eq[-1] / eq[len(eq) - len(s["c"]) - 1] - 1.0)
    assert s["exposure"] == pytest.approx(plain["avg_gross_exposure"], abs=0.01)
    # the hours a pair's coins changed in are the hours the engine filled it in, so the weights twins are made of
    # are the ones it traded to
    coins = np.nan_to_num(w * eq[:, None] / px)
    changed = np.abs(np.diff(coins, axis=0)) > 1e-9 * np.maximum(np.abs(coins[1:]), np.abs(coins[:-1]))
    assert changed.sum() + (coins[0] != 0).sum() == plain["n_trades"]
    first = len(eq) - len(s["c"]) - 1
    last_trade = np.maximum.accumulate(np.where(np.vstack([np.ones((1, 4), dtype=bool), changed[first:]]), np.arange(len(s["c"]) + 1)[:, None], 0), axis=0)
    assert s["w"] == pytest.approx(np.take_along_axis(w[first:], last_trade, axis=0)[:-1] * s["valid"], abs=1e-12)


def test_a_pair_with_no_candle_has_no_price_in_the_record_unless_the_book_holds_it(strategies):
    c = holed(made_up())
    path = backtest.run_backtest(c, cfg_of("rising", look_hours=12), RCFG, record=True)["path"]
    d = path["pairs"].index("DDD")
    listed = np.flatnonzero(np.isfinite(path["opens"][:, d]))
    assert listed[0] > 300 and np.isnan(path["opens"][: listed[0], d]).all() and path["weights"][: listed[0], d].sum() == 0
    assert np.isfinite(path["opens"][:, path["pairs"].index("AAA")]).all()
    s = bench.series(path)
    assert not s["valid"][0, d] and s["valid"][-1, d] and len(s["stretches"]) == 2
    # its first price on record is its first candle's open, in that candle's own hour
    first = made_up()["DDD"].iloc[500]
    assert path["ts"][listed[0]] == int(first["time"]) and path["opens"][listed[0], d] == pytest.approx(float(first["open"]))
    # The pair with two days of candles missing. In those hours it has a price on record exactly where the
    # book holds it, and that price is the mark the account values it at: its last close before the hole. The
    # hour its candles come back it can be seen and not yet traded, so the book still holds it at that mark,
    # and the whole move over the hole lands in the hour after.
    b = path["pairs"].index("BBB")
    whole = made_up()["BBB"]
    gone = (path["ts"] > int(whole.iloc[699]["time"])) & (path["ts"] < int(whole.iloc[748]["time"]))
    assert gone.sum() == 48 and (np.isfinite(path["opens"][gone, b]) == (path["weights"][gone, b] > 0)).all()
    row = int(np.flatnonzero(path["ts"] == int(whole.iloc[748]["time"]))[0])
    # a book that buys every pair it is shown and never changes its mind holds it all through the hole, whatever the prices
    kept = backtest.run_backtest(c, cfg_of("sits"), RCFG, record=True)["path"]
    assert (kept["weights"][gone, b] > 0).all() and kept["weights"][row, b] > 0
    assert kept["opens"][gone, b] == pytest.approx(float(whole.iloc[699]["close"])) and kept["opens"][row, b] == pytest.approx(float(whole.iloc[699]["close"]))
    assert kept["opens"][row + 1, b] == pytest.approx(float(whole.iloc[749]["open"])) and bench.series(kept)["gap_bps"] < 1e-6
    # while the late pair still has too few candles the others decide as usual: those hours are not starved hours
    assert not path["starved"].any() and s["gap_bps"] < 1e-6
    # a book that holds nothing: no price in the hole at all, and the pair is back at its first candle's own open
    idle = backtest.run_backtest(c, cfg_of("rising", look_hours=12, size=0.0), RCFG, record=True)["path"]
    assert np.isnan(idle["opens"][gone, b]).all() and idle["weights"].sum() == 0.0
    assert idle["opens"][row, b] == pytest.approx(float(whole.iloc[748]["open"]))
    assert bench.series(idle)["valid"][:, b].all() and bench.series(idle)["gap_bps"] < 1e-6       # a hole is not a pair that is not listed


def test_the_strategys_first_starved_hours_are_marked(strategies):
    path = backtest.run_backtest(made_up(400), cfg_of("rising", look_hours=12, need=150), RCFG, record=True)["path"]
    assert path["starved"][:99].all() and not path["starved"][100:].any()        # the run begins at candle 50, and it needs 150
    assert bench.series(path)["ts"][0] == path["ts"][np.flatnonzero(~path["starved"])[0]] == T0 + 150 * HOUR


def test_the_record_says_when_the_strategy_left_each_position_and_the_bench_counts_the_windows_with_none(strategies):
    c = made_up(3400)                                                     # 141 days, so a window of 120 fits
    cfg = cfg_of("rising", look_hours=12, size=0.25, band=0.02)
    kept = backtest.run_backtest(c, cfg, RCFG, record=True)
    path = kept["path"]
    exits, span = path["exits"], path["span"]
    assert len(exits) == kept["finished_trades"] > 5 and (np.diff(exits) >= 0).all() and span == (T0 + 50 * HOUR, T0 + 3399 * HOUR)
    assert kept["windows_with_no_finished_trade"] == round(backtest.windows_with_no_exit(exits, *span, 60), 3)
    # by hand: a window starts each day; it has no exit when none falls after its start and by its end
    for days in (60, 120, 1):
        starts = range(span[0], span[1] - days * DAY + 1, DAY)
        by_hand = sum(1 for a in starts if not any(a < e <= a + days * DAY for e in exits)) / len(starts)
        assert backtest.windows_with_no_exit(exits, *span, days) == pytest.approx(by_hand), days
    assert 0 < backtest.windows_with_no_exit(exits, *span, 1) < 1 and backtest.windows_with_no_exit(exits, *span, 120) == 0.0
    assert backtest.windows_with_no_exit(exits, *span, 142) is None                           # the run is shorter than one window
    assert backtest.windows_with_no_exit(np.array([], dtype="int64"), *span, 60) == 1.0
    exits2, forced = backtest.own_exits([], span[0])
    assert len(exits2) == 0 and forced == 0
    r = bench.read(cfg, RCFG, c, jobs=1, quick=True, n_twins=5)
    ro = r["rule_one"]
    assert ro["no_trade_by_first"] == pytest.approx(backtest.windows_with_no_exit(exits, *span, 60))
    assert ro["no_trade_by_total"] == pytest.approx(backtest.windows_with_no_exit(exits, *span, 120))
    assert ro["finished_trades"] == len(exits) and ro["closed_by_halt_or_error"] == kept["closed_by_halt_or_error"]
    assert ro["windows"] is None and r["twins"]["n"] == 5                 # no window of 120 days after a first year, in 141 days
    assert {k: ro[k] for k in ("first_days", "total_days", "min_fills", "min_t", "fast_t")} == bench.live_rules(RCFG)
    s = bench.series(path)
    assert (s["exits"] == exits).all() and s["span"] == span
    assert bench.series({k: v for k, v in path.items() if k not in ("exits", "span")})["span"] == (int(path["ts"][0]), int(path["ts"][-1]))


def test_a_run_in_which_the_strategy_failed_is_counted_on_the_record_and_is_no_reading(strategies, root):
    """The engine goes flat on an hour the strategy fails in, live as in a replay. What such a run made
    is that and not the strategy, so the bench does not read it: it says how often and what was said the
    first time. A nearby setting that made the strategy raise on every hour used to come back as read,
    with no figure, and drop out of the line without a word (found in review, 2026-10-07)."""
    c = made_up(1300)
    path = backtest.run_backtest(c, cfg_of("sometimes", look_hours=12), RCFG, record=True)["path"]
    hours = len(path["ts"])
    assert path["errors"] == sum(1 for t in path["ts"] if ((int(t) - HOUR) // HOUR) % 50 == 0) and 20 < path["errors"] < 30
    assert path["first_error"] == "RuntimeError: not this hour"
    with pytest.raises(RuntimeError, match=rf"the strategy failed on {path['errors']} of the {hours:,} hours replayed "
                                           r"\(the first time: RuntimeError: not this hour\); a run with such hours in it is not a reading"):
        bench.replay(c, RCFG, cfg_of("sometimes", look_hours=12))
    for name, said in (("broken", "RuntimeError: no"), ("quits", "SystemExit: 0")):
        every = backtest.run_backtest(c, cfg_of(name), RCFG, record=True)["path"]
        assert every["errors"] == len(every["ts"]) and every["first_error"] == said
        with pytest.raises(RuntimeError, match=rf"its replay failed: RuntimeError: the strategy failed on {len(every['ts']):,} of the "
                                               rf"{len(every['ts']):,} hours replayed \(the first time: {said}\)"):
            bench.read(cfg_of(name), RCFG, c, jobs=1, quick=True)
    long_winded = backtest.run_backtest(c, cfg_of("broken"), RCFG, record=True)["path"]["first_error"]
    assert len(long_winded) <= 200


# --- the whole reading ----------------------------------------------------------------------

@pytest.fixture
def root(tmp_path, monkeypatch):
    """The bot's paths pointed at a folder of its own, with a strategy file and the configs in it."""
    for name, value in (("ROOT", tmp_path), ("CONFIGS", tmp_path / "configs"), ("STATE", tmp_path / "state"),
                        ("CANDLES", tmp_path / "state" / "candles"), ("HISTORY", tmp_path / "state" / "history"),
                        ("ARCHIVE", tmp_path / "state" / "archive"), ("LEDGER", tmp_path / "LEDGER.md")):
        monkeypatch.setattr(config, name, value)
    (tmp_path / "configs").mkdir()
    (tmp_path / "bot").mkdir()
    (tmp_path / "bot" / "strategy.py").write_text("# the strategies\n")
    config.dump_yaml(tmp_path / "configs" / "risk.yaml", RCFG)
    config.dump_yaml(tmp_path / "configs" / "champion.yaml", dict(cfg_of("rising", look_hours=24, size=0.2), hypothesis="H0"))
    config.dump_yaml(tmp_path / "configs" / "challenger1.yaml", cfg_of("rising", look_hours=12, size=0.25, band=0.01))
    config.dump_yaml(tmp_path / "configs" / "challenger2.yaml", dict(cfg_of("rising", look_hours=24, size=0.2), hypothesis="H0"))
    return tmp_path


def same(a, b):
    drop = lambda d: {k: v for k, v in d.items() if k not in ("made_at", "took_s")}        # noqa: E731
    return json.dumps(bench._plain(drop(a)), sort_keys=True) == json.dumps(bench._plain(drop(b)), sort_keys=True)


def test_the_whole_reading_has_every_part_and_is_the_same_however_many_run_at_once(strategies, root, small):
    c = holed(made_up(1900))
    cfg = cfg_of("rising", look_hours=12, size=0.25, band=0.01)
    r = bench.read(cfg, RCFG, c, jobs=1, n_twins=40)
    assert same(bench.read(cfg, RCFG, c, jobs=3, n_twins=40), r)
    assert r["hypothesis"] == "H9" and r["strategy"] == "rising" and r["params"] == cfg["params"] and r["quick"] is False
    assert r["version"] == bench.VERSION and r["pairs"] == ["AAA", "BBB", "CCC", "DDD"] and r["days"] > 70
    assert r["signature"] == bench.signature(cfg, RCFG)
    assert r["twins"]["n"] == 40 and 0.0 <= r["twins"]["beaten"] <= 1.0 and r["twins"]["beaten_last_365"] is None
    assert r["rebuilt_within_bps"] < 1e-6 and r["exposure"] > 0.05
    assert r["timing_per_year"] + r["drift_per_year"] - r["costs_per_year"] == pytest.approx(r["left_per_year"], abs=1e-12)      # timing and drift less costs
    assert r["no_twins"] is None and r["twins"]["in_place"] == [] and r["slide"]["candles_days"] == pytest.approx(200 / 24)
    assert r["slide"]["lead_days"] == pytest.approx((200 + max(200, round(r["slide"]["longest_hold_days"] * 24))) / 24)
    assert r["costs_per_year"] > 0 and r["double_costs"]["left_per_year"] == pytest.approx(r["left_per_year"] - r["costs_per_year"], abs=0.05 * r["costs_per_year"])
    assert r["double_costs"]["left_per_year"] < r["left_per_year"] and r["double_costs"]["t"] < r["t"]       # it trades, so costs twice over hurt
    assert r["tails"]["days"] == 1 and r["tails"]["worst"] < 0 < r["tails"]["best"]
    assert r["t"] == pytest.approx(r["sharpe"] * math.sqrt(r["days"] / 365))
    assert len(r["nearby"]) == 6 and all(n["ok"] and n["params"] != cfg["params"] and n["beaten"] is not None for n in r["nearby"])
    assert [n["params"] for n in r["nearby"]] == bench.nearby(cfg["params"])
    assert [h["pairs"] for h in r["halves"]] == bench.halves(list(c)) and all(h["ok"] and h["beaten"] is not None for h in r["halves"])
    assert r["clock"] == {"why": None, "shifts": []}
    ro = r["rule_one"]
    assert ro["fills_by_first"] == pytest.approx(r["engine"]["n_trades"] / r["engine"]["days"] * 60)
    assert ro["no_trade_by_first"] is not None and ro["finished_trades"] > 0 and ro["windows"] is None
    # a half is replayed on its own pairs and set against twins of its own
    half, _ = bench.replay(c, RCFG, cfg, pairs=["AAA", "CCC"])
    on_half = bench.reading_of(half, bench.judge(half, 40))
    assert half["pairs"] == ["AAA", "CCC"] and r["halves"][0]["beaten"] == on_half["twins"]["beaten"]
    assert r["halves"][0]["timing_per_year"] == pytest.approx(on_half["timing_per_year"]) and r["halves"][0]["left_per_year"] == pytest.approx(on_half["left_per_year"])
    assert r["halves"][0]["timing_per_year"] != pytest.approx(r["halves"][1]["timing_per_year"])
    # a nearby setting is the same strategy at those params
    near, _ = bench.replay(c, RCFG, dict(cfg, params=r["nearby"][2]["params"]))
    assert r["nearby"][2]["beaten"] == bench.judge(near, 40)["beaten"]["all"]
    assert r["nearby"][2]["net"] == pytest.approx(bench.reading_of(near, None)["net"])
    text = bench.format_reading(r)
    for words in ("bench: H9 (rising)", "what it made:", "twins: before costs it beats", "what the timing is worth:", "No twin holds what the book took in the ",
                  "by year (timing before costs, what is left after them, the basket, twins beaten): 2025 (", "its best and worst days",
                  "half the coins (twins beaten on each half, halved two ways)", "nearby settings (twins beaten with every number in params moved by up to 25%)",
                  "the clock: nothing in its code names it, and its targets do not move with it", "under rule 1:", "Reading: ", "Bench: timing ", "In sample."):
        assert words in text, words
    assert "nan" not in text.lower() and "None" not in text and "n/a" not in text and "FAULT" not in text
    assert text.splitlines()[-1].strip() == bench.ledger_line(r) and bench.ledger_line(r).count("\n") == 0
    assert text.splitlines()[-2].strip() == bench.words(r) and "had a test begun" not in text


def test_a_quick_reading_is_the_replay_and_its_twins(strategies, root, small, monkeypatch):
    c = made_up(1900)
    cfg = cfg_of("rising", look_hours=12, size=0.25)
    whole, quick = bench.read(cfg, RCFG, c, jobs=1, n_twins=40), bench.read(cfg, RCFG, c, jobs=1, n_twins=40, quick=True)
    assert quick["quick"] is True and quick["nearby"] == [] and quick["halves"] == [] and quick["clock"] is None
    for key in ("net", "timing_per_year", "drift_per_year", "left_per_year", "sharpe", "t", "twins", "years", "costs_per_year", "rule_one",
                "days", "double_costs", "tails", "slide", "no_twins", "engine", "pairs", "signature"):
        assert quick[key] == whole[key], key
    text = bench.format_reading(quick)
    assert "nearby settings" not in text and "half the coins" not in text and "the clock" not in text
    assert "nearby" not in bench.ledger_line(quick) and "twins" in bench.ledger_line(quick)
    days = bench.read(cfg, RCFG, c, jobs=1, n_twins=10, quick=True, days=40)
    assert 39 <= days["days"] <= 41 and days["twins"] is not None
    monkeypatch.setattr(bench, "MIN_ROOM_DAYS", 90)                       # as it is: 40 days is then too short a run to slide a book inside
    short = bench.read(cfg, RCFG, c, jobs=1, n_twins=10, quick=True, days=40)
    assert short["twins"] is None and short["timing_per_year"] is None and short["left_per_year"] is None and short["tails"] is None
    assert short["drift_per_year"] is None and short["no_twins"] == "short" and days["no_twins"] is None
    assert short["slide"] == dict(days["slide"], least_days=pytest.approx(days["slide"]["least_days"] + 85))
    assert short["years"][0]["timing"] is None and short["years"][0]["left"] is None and short["years"][0]["net"] == days["years"][0]["net"]
    assert short["double_costs"] == {"left_per_year": None, "sharpe": None, "t": None} and short["net"] == days["net"]
    text = bench.format_reading(short)
    assert ("twins: none. The run is too short to slide a book inside. That takes 5 days to slide it by and 90 more to draw the slides from, and "
            f"twice the 8.3 days of candles a strategy is handed, 111.7 days in all, and the run is {short['days']} days\n") in text
    assert "by year (what it made, the basket): 2025 (" in text and "n/a" not in text and "None" not in text
    assert bench.words(short) == "Reading: the run is too short to set a book against twins, so nothing is said of its timing."
    assert re.fullmatch(r"Bench: [+-]\d+\.\d% after costs over \d+ days; not set against twins \(too short a run\)\. In sample\.", bench.ledger_line(short))


def test_the_last_365_days_are_read_apart_from_the_whole_run(strategies, root):
    c = made_up(9900, seed=7)                                             # 412 days: the last 365 are not the whole of it
    cfg = cfg_of("fridays")                                               # no eye for the market, so it lands among its twins
    r = bench.read(cfg, RCFG, c, jobs=1, quick=True, n_twins=150)
    s = bench.replay(c, RCFG, cfg)[0]
    tw = bench.judge(s, 150)
    assert tw["beaten"]["all"] != tw["beaten"]["last"] and set(tw["beaten"]) == {"all", "last", "2025", "2026"}
    assert r["twins"] == {"n": 150, "beaten": tw["beaten"]["all"], "beaten_last_365": tw["beaten"]["last"], "net_middle": tw["net_middle"],
                          "worth": tw["worth"], "chance": bench.chance(tw["beaten"]["all"], tw["worth"]), "in_place": []}
    assert [(y["year"], y["twins_beaten"]) for y in r["years"]] == [(2025, tw["beaten"]["2025"]), (2026, tw["beaten"]["2026"])]
    assert r["days"] == len(s["daily"]) > 400 and sum(y["days"] for y in r["years"]) == r["days"]
    assert sum(y["timing"] for y in r["years"]) / r["days"] * 365 == pytest.approx(r["timing_per_year"])     # the years add up to the whole
    assert sum(y["left"] for y in r["years"]) / r["days"] * 365 == pytest.approx(r["left_per_year"])
    text = bench.format_reading(r)
    assert f"before costs it beats {tw['beaten']['all']:.0%} of 150 twins over the whole run and {tw['beaten']['last']:.0%} over the last 365 days" in text
    assert (f"which beats {tw['beaten']['all']:.0%} of its twins ({tw['beaten']['last']:.0%} of them over the last 365 days), and a book with "
            f"no timing does as well {r['twins']['chance']:.0%} of the time; letting positions run ") in bench.ledger_line(r)
    assert "2025 (" in text and "2026 (" in text                          # part years say how many days they have
    whole_year = dict(r, years=[dict(r["years"][0], days=365)])
    assert "2025 (" not in bench.format_reading(whole_year)


def test_each_config_gets_its_own_replays_when_several_are_read_at_once(strategies, root, small):
    c = made_up(900)
    one, two = cfg_of("rising", look_hours=12, size=0.25), dict(cfg_of("rising", look_hours=40, size=0.1, band=0.03), hypothesis="H10")
    both = bench.read_many([one, two], RCFG, c, jobs=2, n_twins=5)
    alone = [bench.read(cfg, RCFG, c, jobs=1, n_twins=5) for cfg in (one, two)]
    for got, want, cfg in zip(both, alone, (one, two)):
        assert got["hypothesis"] == cfg["hypothesis"] and got["params"] == cfg["params"]
        assert [n["params"] for n in got["nearby"]] == bench.nearby(cfg["params"]) and len(got["nearby"]) == 6 and len(got["halves"]) == 4
        assert same(got, want)
    assert both[0]["net"] != both[1]["net"] and both[0]["nearby"][0]["net"] != both[1]["nearby"][0]["net"]


def test_a_strategy_the_clock_can_matter_to_is_replayed_with_the_clock_moved(strategies, root, small):
    c = made_up(900)
    r = bench.read(cfg_of("fridays"), RCFG, c, jobs=2, n_twins=20)
    shifts = r["clock"]["shifts"]
    assert r["clock"]["why"] == bench.TARGETS_MOVE and [s["shift_hours"] for s in shifts] == list(bench.CLOCK_SHIFTS_H)
    assert all(s["ok"] and s["beaten"] is not None for s in shifts)
    assert len({round(s["net"], 9) for s in shifts}) == 6                  # each phase is a different book
    moved, _ = bench.replay(c, RCFG, cfg_of("fridays"), shift_hours=54)
    assert shifts[1]["beaten"] == bench.judge(moved, 20)["beaten"]["all"] and shifts[1]["net"] == pytest.approx(bench.reading_of(moved, None)["net"])
    assert moved["ts"][0] == bench.replay(c, RCFG, cfg_of("fridays"))[0]["ts"][0] + 54 * HOUR
    text = bench.format_reading(r)
    assert "the clock: its targets change when the clock is moved. With the clock moved (by 27, 54, 81, 108, 135, 162 hours) it beats " in text
    # one whose code only names the time column is replayed the same way: the six replays say whether it matters
    named = bench.read(cfg_of("monthly"), RCFG, c, jobs=2, n_twins=5)["clock"]
    assert named["why"] == bench.CODE_NAMES_IT and len(named["shifts"]) == 6
    assert bench.plan(cfg_of("rising"), c, quick=False, clock=None)[-1]["kind"] == "half"
    assert [t["kind"] for t in bench.plan(cfg_of("rising"), c, quick=False, clock="any reason")[-6:]] == ["clock"] * 6
    assert bench.plan(cfg_of("rising", look_hours=12), c, quick=True, clock="any reason") == [{"config": 0, "kind": "own", "twins": 1000}]
    tasks = bench.plan(cfg_of("rising", look_hours=12, size=0.2), c, quick=False, index=3, clock="any reason", n_twins=500)
    assert [(t["kind"], t["twins"]) for t in tasks] == [("own", 500)] + [("nearby", 200)] * 6 + [("half", 200)] * 4 + [("clock", 200)] * 6
    assert {t["config"] for t in tasks} == {3}                              # a setting, a half and a phase get fewer twins each
    assert [t["twins"] for t in bench.plan(cfg_of("rising", look_hours=12, size=0.2), c, quick=False)][:2] == [1000, 200]


def test_a_replay_that_fails_is_said_and_the_configs_own_failing_stops_its_reading_alone(strategies, root, small, monkeypatch):
    c = made_up(900)
    real = bench.replay

    def some_fail(candles_, rcfg, cfg, days=None, pairs=None, shift_hours=0):
        if pairs == ["BBB", "DDD"] or cfg["params"].get("look_hours") == 99:
            raise ValueError("no candle data")
        return real(candles_, rcfg, cfg, days=days, pairs=pairs, shift_hours=shift_hours)
    monkeypatch.setattr(bench, "replay", some_fail)
    r = bench.read(cfg_of("rising", look_hours=12), RCFG, c, jobs=1, n_twins=10)
    assert [h["ok"] for h in r["halves"]] == [True, False, True, True] and r["halves"][1]["error"] == "ValueError: no candle data"
    assert "beaten" not in r["halves"][1] and "(1 could not be replayed)" in bench.format_reading(r) and "(1 could not be replayed)" in bench.ledger_line(r)
    with pytest.raises(RuntimeError, match="its replay failed: ValueError: no candle data"):
        bench.read(cfg_of("rising", look_hours=99), RCFG, c, jobs=1)
    # one config's failure does not cost the next its reading, in a quick reading or a whole one, whatever
    # the failure: a replay that raises, a strategy nobody registered, params that are not a mapping
    good = cfg_of("rising", look_hours=12)
    bads = [(cfg_of("rising", look_hours=99), "its replay failed: ValueError: no candle data"),
            (cfg_of("no_such_strategy"), "KeyError: \"unknown strategy 'no_such_strategy'"),
            ({"hypothesis": "H9", "strategy": "rising", "params": [1, 2]}, "ValueError: params must be a mapping"),
            ({"hypothesis": "H9", "params": {}}, "KeyError: 'strategy'")]
    for quick, some in ((True, bads), (False, bads[:2])):
        for bad, why in some:
            many = bench.read_many([bad, good], RCFG, c, jobs=2, quick=quick, n_twins=5)
            assert set(many[0]) == {"failed"} and many[0]["failed"].startswith(why), (quick, many[0])
            assert many[1]["twins"]["n"] == 5 and (quick or len(many[1]["halves"]) == 4), (quick, bad)
    with pytest.raises(RuntimeError, match="unknown strategy"):
        bench.read(cfg_of("no_such_strategy"), RCFG, c)


@pytest.mark.skipif(not FORKS, reason="every replay runs in a process of its own only where processes can be forked")
def test_every_replay_runs_in_a_process_of_its_own(strategies, root, small):
    """So that nothing a strategy keeps or breaks in one replay is there in the next, and one that takes
    its process down has cost one replay. `remembers` trades on how often it has been called in its
    process: with every replay in the same one, as it used to be, its halves and nearby settings read
    differently by how many ran at once (found in review, 2026-10-07)."""
    c = made_up(900)
    cfg = cfg_of("remembers", look_hours=12, size=0.2)
    one = bench.read(cfg, RCFG, c, jobs=1, n_twins=5)
    assert MEMORY["calls"] == 0                                           # none of it ran in this process, the asking about the clock neither
    assert same(bench.read(cfg, RCFG, c, jobs=3, n_twins=5), one) and MEMORY["calls"] == 0
    alone, _ = bench.replay(c, RCFG, cfg, pairs=["AAA", "CCC"])           # in this process, from a count of nothing
    assert one["halves"][0]["net"] == pytest.approx(bench.reading_of(alone, None)["net"]) and MEMORY["calls"] > 600
    again, _ = bench.replay(c, RCFG, cfg, pairs=["AAA", "CCC"])           # and a second time in the same one: not the same book
    assert bench.reading_of(again, None)["net"] != pytest.approx(one["halves"][0]["net"])
    # a strategy that takes its process down with it
    with pytest.raises(RuntimeError, match=r"its replay failed: the process replaying it died before it could answer \(exit code 7\)"):
        bench.read(cfg_of("dies"), RCFG, c, jobs=1, quick=True)
    many = bench.read_many([cfg_of("dies"), cfg_of("rising", look_hours=12, size=0.2)], RCFG, c, jobs=2, n_twins=5)
    assert "died before it could answer" in many[0]["failed"] and many[1]["twins"]["n"] == 5 and len(many[1]["nearby"]) == 6
    assert multiprocessing.active_children() == []
    # a strategy that writes to its params: the reading is of the config as it was handed in, and is still its reading afterwards
    cfg = cfg_of("fiddles", size=0.25)
    r = bench.read(cfg, RCFG, c, jobs=1, quick=True, n_twins=5)
    assert cfg == cfg_of("fiddles", size=0.25) and r["params"] == {"size": 0.25} and r["signature"] == bench.signature(cfg, RCFG)
    bench.replay(c, RCFG, cfg)                                            # and in one process too: the strategy is handed a copy
    assert cfg == cfg_of("fiddles", size=0.25)


def test_when_a_configs_own_replay_fails_nothing_else_of_it_is_replayed(strategies, root, small, monkeypatch, tmp_path):
    """A config whose own replay fails has no reading whatever its settings and halves show, and it
    fails again every night until somebody mends it: seventeen replays of five years thrown away each
    time (found in review, 2026-10-07). What is waiting is not started and what is running is stopped."""
    c = made_up(900)
    real, log = bench.replay, tmp_path / "replays.txt"

    def noting(candles_, rcfg, cfg, days=None, pairs=None, shift_hours=0):
        with open(log, "a") as f:
            f.write(f"{cfg['hypothesis']}\n")
        if cfg["params"] == {"look_hours": 99, "size": 0.25} and pairs is None:      # the config's own replay, and only that one
            raise ValueError("no candle data")
        return real(candles_, rcfg, cfg, days=days, pairs=pairs, shift_hours=shift_hours)
    monkeypatch.setattr(bench, "replay", noting)
    bad, good = cfg_of("rising", look_hours=99, size=0.25), dict(cfg_of("rising", look_hours=12, size=0.2), hypothesis="H10")
    shared = {"configs": [bad], "rcfg": RCFG, "candles": c, "days": None, "rules": bench.live_rules(RCFG)}
    for jobs in ((1, 3) if FORKS else (1,)):
        log.write_text("")
        done = bench.run(bench.plan(bad, c, quick=False, n_twins=5), shared, jobs=jobs)
        assert len(done) == 11 and done[0]["error"] == "ValueError: no candle data"
        assert all(d == {"config": 0, "kind": d["kind"], **{k: d[k] for k in ("params", "pairs") if k in d}, "ok": False,
                         "error": bench.DROPPED, "took_s": 0.0} for d in done[1:])
        assert 1 <= len(log.read_text().split()) <= jobs, jobs           # its own, and at the most what had been started beside it
        assert multiprocessing.active_children() == []
    assert bench.DROPPED == "not run: its config's own replay had failed"
    log.write_text("")
    many = bench.read_many([bad, good], RCFG, c, jobs=1, n_twins=5)
    assert many[0] == {"failed": "its replay failed: ValueError: no candle data"} and len(many[1]["nearby"]) == 6 and len(many[1]["halves"]) == 4
    assert log.read_text().split() == ["H9"] + ["H10"] * 11              # the config after it is read in full


@pytest.mark.skipif(not FORKS, reason="only where processes can be forked")
def test_a_process_that_will_not_end_or_cannot_be_started_costs_its_own_replay_and_no_more(strategies, root, small, monkeypatch):
    """The time the bench is given held only while every process ended by itself. One that had answered
    and stayed (a thread left running), or that shut its own way out and stayed, was waited for without
    limit; one the machine would not start ended the whole run; and a strategy that starts processes of
    its own could not be replayed at all (all four found in review, 2026-10-07)."""
    c = made_up(900)
    monkeypatch.setattr(bench, "GRACE_S", 0.5)
    shared = lambda *names: {"configs": [dict(cfg_of(n, look_hours=12), hypothesis=f"H{k}") for k, n in enumerate(names)], "rcfg": RCFG,     # noqa: E731
                             "candles": c, "days": None, "rules": bench.live_rules(RCFG)}
    own = lambda *ks: [{"config": k, "kind": "own", "twins": 5} for k in ks]                              # noqa: E731
    began = time.time()
    stays, shut, fine = bench.run(own(0, 1, 2), shared("lingers", "hides", "rising"), jobs=3)
    assert stays["ok"] is True and stays["twins"]["n"] == 5              # it had answered: its reading is kept, and its process is ended for it
    assert shut["ok"] is False and shut["error"] == "the process replaying it died before it could answer (exit code -9)"
    assert fine["ok"] is True and time.time() - began < 30 and multiprocessing.active_children() == []
    # a strategy that starts processes of its own is replayed like any other
    forked = bench.run(own(0), shared("forks"), jobs=1)[0]
    assert forked["ok"] is True and forked["twins"]["n"] == 5, forked.get("error")
    assert forked["net"] == pytest.approx(bench.run(own(0), shared("rising"), jobs=1)[0]["net"])
    # the machine has no process to give: tried again when another has finished, and failed alone when none is running
    real = multiprocessing.get_context

    class Refusing:
        def __init__(self, refuse):
            self.ctx, self.asked, self.refuse = real("fork"), 0, set(refuse)

        def Pipe(self, duplex=True):
            return self.ctx.Pipe(duplex=duplex)

        def Process(self, **kw):
            proc, n = self.ctx.Process(**kw), self.asked
            self.asked += 1
            if n in self.refuse:
                def start():
                    raise BlockingIOError(11, "Resource temporarily unavailable")
                proc.start = start
            return proc
    for refuse, jobs, oks, asked in (((0,), 1, [False, True, True], 3), ((1,), 2, [True, True, True], 4), ((1, 2, 3), 2, [True, False, False], 4)):
        ctx = Refusing(refuse)
        monkeypatch.setattr(multiprocessing, "get_context", lambda method: ctx)
        done = bench.run(own(0, 1, 2), shared("rising", "rising", "rising"), jobs=jobs)
        assert [d["ok"] for d in done] == oks and ctx.asked == asked, (refuse, [d.get("error") for d in done])
        lost = [d for d in done if not d["ok"]]
        assert all(d["error"] == "no process could be started to replay it (BlockingIOError: [Errno 11] Resource temporarily unavailable)" for d in lost)
        assert bench.START_TRIES == 3 and multiprocessing.active_children() == []

    # With a time to stop by, the bench comes round once a second to look at it, and a start that had been refused was
    # tried again each time round: three tries were gone in two seconds and the replay lost, on the very path the nightly
    # run takes (found in review, 2026-10-07). After a refusal nothing is started until one of those running has finished.
    # A machine that will run one process at a time, and a first replay that takes three seconds
    class OneAtATime:
        def __init__(self):
            self.ctx, self.asked, self.refused = real("fork"), 0, 0

        def Pipe(self, duplex=True):
            return self.ctx.Pipe(duplex=duplex)

        def Process(self, **kw):
            proc = self.ctx.Process(**kw)
            go = proc.start

            def start():
                self.asked += 1
                if multiprocessing.active_children():
                    self.refused += 1
                    raise BlockingIOError(11, "Resource temporarily unavailable")
                go()
            proc.start = start
            return proc
    for deadline in (None, time.time() + 3600):
        ctx = OneAtATime()
        monkeypatch.setattr(multiprocessing, "get_context", lambda method: ctx)
        began = time.time()
        done = bench.run(own(0, 1), shared("ambles", "rising"), jobs=2, deadline=deadline)
        assert [d["ok"] for d in done] == [True, True] and (ctx.asked, ctx.refused) == (3, 1), (deadline, [d.get("error") for d in done])
        assert time.time() - began > 2.5 and multiprocessing.active_children() == []
    monkeypatch.setattr(multiprocessing, "get_context", real)
    # A replay's process that dies while something it started lives on. The process left behind holds the pipe open, so
    # the pipe did not say the replay was dead, and the bench waited for as long as that process lived: until the agent's
    # thirty minutes ran out, or, with a time to stop by, to report a death as time running out (found in review, 2026-10-07)
    for deadline in (None, time.time() + 600):
        began = time.time()
        died, fine = bench.run(own(0, 1), shared("orphans", "rising"), jobs=2, deadline=deadline)
        assert died["ok"] is False and died["error"] == "the process replaying it died before it could answer (exit code 3)", died
        assert fine["ok"] is True and time.time() - began < 25 and multiprocessing.active_children() == []       # the one it left sleeps for forty
    # ... and when it is the only replay, which is the reading the agent takes of one config: no other replay's ending
    # brings the bench round to look, so with no time to stop by it has to come round by itself
    began = time.time()
    alone = bench.run(own(0), shared("orphans"), jobs=1)[0]
    assert alone["ok"] is False and alone["error"] == "the process replaying it died before it could answer (exit code 3)", alone
    assert time.time() - began < 25 and multiprocessing.active_children() == []
    # ... and the wait for a process that has answered and will not end stops at the time to stop by, not after it
    monkeypatch.setattr(bench, "GRACE_S", 60.0)
    began = time.time()
    stays = bench.run(own(0), shared("lingers"), jobs=1, deadline=time.time() + 5.0)[0]
    assert (stays["ok"] is True or stays.get("stopped") is True) and time.time() - began < 25 and multiprocessing.active_children() == []
    # An interrupt while the bench waits for a process that has answered and will not end: that one is stopped with the
    # rest. It had been taken off the list of what was running before the wait began, so it was left behind, and the bench
    # could not end until it had (found in review, 2026-10-07)
    import signal
    monkeypatch.setattr(bench, "GRACE_S", 60.0)
    waited = multiprocessing.connection.wait

    def answered_then_interrupted(conns, timeout=None):
        ready = waited(conns, timeout)
        if ready:
            signal.setitimer(signal.ITIMER_REAL, 0.5)                     # half a second into the wait for it to end
        return ready

    def interrupt(signum, frame):
        raise KeyboardInterrupt
    before = signal.signal(signal.SIGALRM, interrupt)
    monkeypatch.setattr(multiprocessing.connection, "wait", answered_then_interrupted)
    began = time.time()
    try:
        with pytest.raises(KeyboardInterrupt):
            bench.run(own(0), shared("lingers"), jobs=1)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, before)
    assert multiprocessing.active_children() == [] and time.time() - began < 30


def test_where_processes_cannot_be_forked_the_replays_run_one_after_another_in_this_one(strategies, root, small, monkeypatch, capsys):
    c = made_up(900)
    monkeypatch.setattr(multiprocessing, "get_all_start_methods", lambda: ["spawn"])
    cfg = cfg_of("forks", look_hours=12) if FORKS else cfg_of("remembers", look_hours=12)
    shared = {"configs": [cfg, cfg_of("chatty", look_hours=12), cfg_of("broken")], "rcfg": RCFG, "candles": c, "days": None, "rules": bench.live_rules(RCFG)}
    tasks = [{"config": 0, "kind": "own", "twins": 5}, {"config": 1, "kind": "own", "twins": 5}, {"config": 2, "kind": "own", "twins": 5},
             {"config": 2, "kind": "half", "pairs": ["AAA", "CCC"], "twins": 5}]
    done = bench.run(tasks, shared, jobs=4)
    assert [d["ok"] for d in done] == [True, True, False, False] and MEMORY["calls"] > 600        # it ran here, in this process
    assert done[3]["error"] == bench.DROPPED and done[2]["error"].startswith("RuntimeError: the strategy failed on ")
    said = capsys.readouterr()
    assert said.out == "" and said.err.count("the strategy says: still here") > 600                # what a strategy prints is no part of a reading
    late = bench.run(tasks, shared, jobs=4, deadline=time.time() - 1.0)
    assert all(d["stopped"] is True and d["error"] == bench.STOPPED for d in late)


def test_past_its_time_the_bench_starts_nothing_more_and_says_what_it_did_not_do(strategies, root, small):
    c = made_up(900)
    cfg = cfg_of("rising", look_hours=12, size=0.25)
    shared = {"configs": [cfg], "rcfg": RCFG, "candles": c, "days": None, "rules": bench.live_rules(RCFG)}
    tasks = bench.plan(cfg, c, quick=False, n_twins=5)
    late = bench.run(tasks, shared, jobs=2, deadline=time.time() - 1.0)
    assert len(late) == 11 and all(d["ok"] is False and d["stopped"] is True and d["error"] == bench.STOPPED for d in late)
    assert [d["kind"] for d in late] == [t["kind"] for t in tasks] and late[1]["params"] == tasks[1]["params"]
    assert bench.STOPPED == "not run: the bench's time ran out" and bench.run([], shared) == []
    assert {t["twins"] for t in bench.plan(cfg, c, quick=False, n_twins=0)} == {1} and {t["twins"] for t in tasks} == {5}      # never no twins at all
    for quick in (True, False):
        assert bench.read_many([cfg], RCFG, c, quick=quick, n_twins=5, deadline=time.time() - 1.0) == \
            [{"failed": "its replay failed: not run: the bench's time ran out"}]
    # a reading that was cut short part way is no reading: its settings and halves would be fewer than they say
    done = bench.run(tasks[:2], shared, jobs=1) + [dict(late[2])]
    assert done[0]["ok"] and done[1]["ok"]
    with pytest.raises(RuntimeError, match="the bench's time ran out with 1 of its 3 replays not done"):
        bench.assemble(cfg, "signed", done, None, False)
    assert bench.assemble(cfg, "signed", done[:2], None, False)["signature"] == "signed"
    with pytest.raises(RuntimeError, match="its replay failed: it was never run"):
        bench.assemble(cfg, "signed", done[1:2], None, False)
    if FORKS:                                                             # what is running when the time runs out is stopped, not waited for
        began = time.time()
        cut = bench.run([{"config": 0, "kind": "own", "twins": 5}], dict(shared, configs=[cfg_of("slow")]), jobs=1, deadline=time.time() + 1.5)
        assert cut[0]["stopped"] is True and time.time() - began < 20 and multiprocessing.active_children() == []


# --- the words ------------------------------------------------------------------------------

def a_reading(**over):
    """A whole reading that could have come off the bench: timing and drift less costs is what is
    left, and nothing about it is thin. `over` replaces whole parts of it."""
    r = {"version": 1, "made_at": 1_790_000_000, "quick": False, "signature": "0123456789abcdef", "hypothesis": "H9", "strategy": "rising",
         "params": {"look_hours": 12}, "pairs": ["A", "B", "C", "D"], "start": "2021-10-13", "end": "2026-10-06", "days": 1800,
         "net": 0.5, "basket": -0.4, "exposure": 0.3, "twins": twins_of(0.97), "no_twins": None,
         "slide": slide_of(),
         "timing_per_year": 0.13, "drift_per_year": 0.01, "costs_per_year": 0.04, "left_per_year": 0.10, "sharpe": 0.8, "t": 1.8,
         "twin_gross_per_year": -0.05, "tails": {"days": 9, "best": 0.12, "worst": -0.10},
         "double_costs": {"left_per_year": 0.06, "sharpe": 0.5, "t": 1.0},
         "years": [{"year": y, "days": 365, "net": 0.1, "basket": 0.1, "exposure": 0.3, "costs": 0.04, "timing": 0.08, "drift": 0.01, "left": 0.05,
                    "twins_beaten": 0.9} for y in (2022, 2023, 2024, 2025)],
         "nearby": [{"ok": True, "beaten": v} for v in (0.7, 0.8, 0.85, 0.9, 0.95, 0.99)],
         "halves": [{"ok": True, "beaten": v} for v in (0.8, 0.85, 0.9, 0.95)], "clock": {"why": None, "shifts": []},
         "rule_one": {"first_days": 60, "total_days": 120, "min_fills": 30, "min_t": 1.0, "fast_t": 2.0, "fills_by_first": 40.0,
                      "finished_trades": 50, "closed_by_halt_or_error": 1, "no_trade_by_first": 0.1, "no_trade_by_total": 0.0,
                      "windows": {"windows": 1300, "apart": 12, "no_trade": 0.1, "few_fills": 0.0, "t_middle": 0.3, "t_reached": 0.2,
                                  "all_counts": 0.18, "fast_pass": 0.02}},
         "rebuilt_within_bps": 0.0, "engine": {}, "took_s": 1.0}
    r.update(over)
    return r


def slide_of(stay=12.0, pair="B", candles=90.0, history=1800.0):
    """What a reading says of how far its twins could be slid, for a book whose longest stay was `stay` days, in `pair`."""
    lead = candles + max(candles, stay)
    return {"candles_days": candles, "longest_hold_days": stay, "longest_hold_pair": pair, "wrote_params": False,
            "lead_days": lead, "least_days": 30.0 + lead + 90.0, "history_days": history}


def twins_of(beaten, last=0.8, worth=200.0, in_place=()):
    return {"n": 1000, "beaten": beaten, "beaten_last_365": last, "net_middle": -0.3, "worth": worth, "chance": bench.chance(beaten, worth),
            "in_place": list(in_place)}


def no_twins(why="short", **over):
    """A reading of a book that could not be set against twins."""
    return a_reading(twins=None, no_twins=why, timing_per_year=None, drift_per_year=None, left_per_year=None, sharpe=None, t=None, tails=None,
                     double_costs={"left_per_year": None, "sharpe": None, "t": None},
                     years=[dict(y, timing=None, drift=None, left=None, twins_beaten=None) for y in a_reading()["years"]], **over)


def test_the_words_at_the_end_say_what_the_figures_show():
    good = a_reading()
    assert bench.weak_spots(good) == [] and bench.NO_TIMING_BELOW == 0.5 and bench.LUCK_ABOVE == 0.10 and bench.HOLDS_UP == 0.75
    assert bench.words(good) == ("Reading: it beats most of its twins, with something left after costs, in most years and at double costs; 4 of 4 "
                                 "halves of the coins and 5 of 6 nearby settings beat 75% of their own twins or more. Worth a slot on this "
                                 "evidence, all of which is in sample.")
    # Fewer than half its twins. A book with no timing gets that half the time, so what the figures back is `no sign`
    # and nothing stronger (it used to say `nothing here`; found in review, 2026-10-07)
    assert bench.words(a_reading(twins=twins_of(0.49))) == ("Reading: no sign of timing. Before costs, most of its own twins did better: the "
                                                            "same positions, taken at other times.")
    assert bench.words(a_reading(twins=twins_of(0.05), timing_per_year=-0.2, left_per_year=-0.24)).startswith("Reading: no sign of timing.")
    # half or more, and luck does as well more than one time in ten: with how often
    assert bench.words(a_reading(twins=twins_of(0.5))) == "Reading: cannot be told from luck. A book with no timing at all does as well about 50% of the time."
    assert bench.words(a_reading(twins=twins_of(0.72))) == "Reading: cannot be told from luck. A book with no timing at all does as well about 28% of the time."
    # The line is drawn on the chance, not on the share: among 200 separate twins, beating 90% of them is a
    # chance of 21 in 201, a shade over one in ten
    assert bench.chance(0.90, 200.0) > 0.10 > bench.chance(0.91, 200.0)
    assert bench.words(a_reading(twins=twins_of(0.90))).startswith("Reading: cannot be told from luck.")
    assert bench.words(a_reading(twins=twins_of(0.91))).startswith("Reading: it beats most of its twins")
    # ... and among twins worth only a few separate ones, no share is enough, and the reading says why
    few = bench.words(a_reading(twins=twins_of(0.99, worth=4.0)))
    assert few == ("Reading: cannot be told from luck. A book with no timing at all does as well about 21% of the time; its twins are worth only "
                   "about 4 separate ones, and no book can stand out among so few. A longer run gives a slow book more of them; a book that "
                   "keeps to the clock has only so many.")
    assert "worth only" not in bench.words(a_reading(twins=twins_of(0.8, worth=9.0))) and "worth only" in bench.words(a_reading(twins=twins_of(0.8, worth=8.9)))
    assert bench.words(a_reading(twins=twins_of(1.0, worth=9.0))).startswith("Reading: it beats most of its twins")       # one in ten, to the letter
    assert bench.words(a_reading(twins=dict(twins_of(0.97), chance=None, worth=None))).startswith("Reading: cannot be told from luck. A book with no timing at all does as well n/a")
    # a share that is not all of them is not said to be all of them (995 of 1,000 read `100%`; found in review, 2026-10-07)
    assert bench.words(a_reading(twins=twins_of(0.004, worth=100.0))).startswith("Reading: no sign of timing.")
    assert bench.words(a_reading(twins=twins_of(0.004, worth=100.0), timing_per_year=0.1)).startswith("Reading: no sign of timing.")
    assert bench.words(a_reading(twins=twins_of(0.5, worth=0.004))).startswith("Reading: cannot be told from luck. A book with no timing at all does as "
                                                                               "well over 99% of the time; its twins are worth only")
    assert "does as well as this under 1% of the time" in bench.format_reading(a_reading(twins=twins_of(0.9999, worth=999.0)))
    assert [bench._about(v) for v in (None, 0.28, 0.999, 0.001, 1.0)] == ["n/a", "about 28%", "over 99%", "under 1%", "about 100%"]
    # luck does as well one time in ten or less, and nothing is left after costs
    costly = a_reading(twins=twins_of(0.93), timing_per_year=0.08, drift_per_year=0.01, costs_per_year=0.58, left_per_year=-0.49)
    assert bench.words(costly) == ("Reading: its timing beats most of its twins, and its costs take more than the book made over its average twin "
                                   "before them, so nothing is left. The costs are the thing to mend: fewer or larger trades, not a new signal.")
    assert "costs take more than the book made" in bench.words(a_reading(timing_per_year=0.03, drift_per_year=0.01, left_per_year=0.0))        # nothing left is nothing
    # ... and the costs are not blamed for what the book never made before them: as last traded it ranks high, and
    # letting its positions run lost what its timing added
    lost = a_reading(twins=twins_of(0.93), timing_per_year=0.02, drift_per_year=-0.03, costs_per_year=0.04, left_per_year=-0.05)
    assert "costs take more" not in bench.words(lost) and "lost again in letting positions run between trades" in bench.words(lost)
    assert "costs take more" in bench.words(dict(lost, drift_per_year=-0.01, left_per_year=-0.03))
    assert "lost again in letting positions run" in bench.words(dict(lost, drift_per_year=-0.02, left_per_year=-0.04))      # to the letter: nothing made is nothing
    # ... nor for a timing that made nothing itself. A book can stand above most of its twins day by day and make no more
    # than they do: with timing at -1% and three points from letting positions run, it was told that its costs took more
    # than its timing added (found in review, 2026-10-07)
    none = a_reading(twins=twins_of(0.93), timing_per_year=-0.01, drift_per_year=0.03, costs_per_year=0.04, left_per_year=-0.02)
    assert bench.words(none) == ("Reading: day by day it stands above most of its twins, and over the whole run its timing made no more than its "
                                 "average twin did. What it lost or kept came from letting positions run and from costs, not from when it traded.")
    assert bench.words(dict(none, timing_per_year=0.0)) == bench.words(none) == bench.words(dict(none, timing_per_year=None, drift_per_year=None, left_per_year=None))
    assert "costs take more" in bench.words(dict(none, timing_per_year=0.001, left_per_year=-0.009))
    # No twins, and each reason in its own words. A book the bench cannot set against twins has not been shown to have no
    # timing: `it sits in one position too long` was said of a book that switched between two weights at a cost of 81% a
    # year, of a 95 day hold on a run of 300 days, and of a pair with 1,181 days of prices (found in review, 2026-10-07)
    assert bench.words(no_twins("short")) == "Reading: the run is too short to set a book against twins, so nothing is said of its timing."
    assert bench.words(no_twins("new")) == "Reading: no pair it holds has prices for long enough to set a book against twins, so nothing is said of its timing."
    assert bench.words(no_twins("idle")) == "Reading: it never held a position, so there is no timing to read."
    sits = slide_of(stay=1700.0, pair="P0")
    assert bench.words(no_twins("hold", slide=sits)) == ("Reading: it was never out of P0 for 1,700 days on end, which leaves too little of a run of "
                                                         "1,800 days to set it against twins. The bench cannot read its timing; that is not to say "
                                                         "it has none.")
    assert bench.words(no_twins("pairs", slide=sits)) == ("Reading: it was never out of P0 for 1,700 days on end, and no pair it holds has prices for "
                                                          "long enough to set such a book against twins. The bench cannot read its timing; that is "
                                                          "not to say it has none.")
    late = slide_of(stay=1000.4, pair="P6")                               # the days to the nearest one, with the pair it was
    assert bench.words(no_twins("hold", slide=late)).startswith("Reading: it was never out of P6 for 1,000 days on end, which leaves too little of a run of 1,800 days")
    assert bench.words(no_twins("pairs", slide=late)).startswith("Reading: it was never out of P6 for 1,000 days on end, and no pair it holds has prices for long enough")
    # a reading with no stay on it, as one made before the stay was kept would be, still comes out in words
    assert bench.words(no_twins("hold", slide={})).startswith("Reading: it was never out of one pair for 0 days on end, which leaves too little")
    assert bench.words(no_twins(None)) == bench.words(no_twins("short")) and bench.words(no_twins("something else")) == bench.words(no_twins("short"))
    assert not hasattr(bench, "NO_TWINS") and "sits in one position" not in (REPO / "bot" / "bench.py").read_text()
    # a quick reading never says an idea is worth a slot: it has not looked at the halves or the settings
    quick = bench.words(a_reading(quick=True, nearby=[], halves=[], clock=None))
    assert quick == ("Reading: it beats most of its twins, with something left after costs, in most years and at double costs. The halves of the "
                     "coins and the nearby settings are not in a quick reading.")
    # nothing is said to hold that was not read
    assert "in most years" not in bench.words(a_reading(years=[])) and "at double costs" in bench.words(a_reading(years=[]))
    assert "at double costs" not in bench.words(a_reading(double_costs={"left_per_year": None, "sharpe": None, "t": None}))
    assert bench.words(a_reading(years=[], double_costs=None, quick=True)) == ("Reading: it beats most of its twins, with something left after "
                                                                               "costs. The halves of the coins and the nearby settings are not in a quick reading.")
    bare = bench.words(a_reading(nearby=[], halves=[]))
    assert bare == ("Reading: it beats most of its twins, with something left after costs, in most years and at double costs. There were too few "
                    "coins to halve. It has no settings to move. Worth a slot on this evidence, all of which is in sample.")
    one = bench.words(a_reading(nearby=[]))
    assert "; 4 of 4 halves of the coins beat 75% of their own twins or more. It has no settings to move. Worth a slot" in one
    phases = bench.words(a_reading(clock={"why": "x", "shifts": [{"ok": True, "beaten": 0.9}] * 6}))
    assert "; 4 of 4 halves of the coins, 5 of 6 nearby settings and 6 of 6 phases of the clock beat 75% of their own twins or more. Worth a slot" in phases
    # A setting a quarter away that beats barely half its own twins is not the result holding up, and a replay that
    # failed is not one that agreed: four of six failing and the other two at 51% and 55% used to read `the nearby
    # settings agree` and `Worth a slot` (found in review, 2026-10-07)
    thin = bench.words(a_reading(nearby=[{"ok": False, "error": "x"}] * 4 + [{"ok": True, "beaten": 0.51}, {"ok": True, "beaten": 0.55}]))
    assert "Worth a slot" not in thin and "Weak spots: only 0 of 6 nearby settings beat 75% of their twins (4 of them could not be replayed at all)." in thin
    for r in (good, costly, lost, a_reading(twins=twins_of(0.99, worth=4.0)), a_reading(twins=twins_of(0.3)), a_reading(quick=True), no_twins()):
        assert bench.words(r).startswith("Reading: ") and bench.words(r).count("\n") == 0


def test_each_weak_spot_is_named_and_only_when_it_is_one():
    year = lambda left: {"year": 2022, "days": 365, "net": 0.1, "basket": 0.1, "exposure": 0.3, "costs": 0.04, "timing": left + 0.04, "drift": 0.0,     # noqa: E731
                         "left": left, "twins_beaten": 0.9}
    read = lambda *shares: [{"ok": True, "beaten": v} for v in shares]                                # noqa: E731
    lost = [{"ok": False, "error": "x"}]
    rule = lambda **over: dict(a_reading()["rule_one"], **over)                                        # noqa: E731
    cases = [
        (dict(years=[year(0.1), year(-0.1), year(-0.1), year(-0.1)]), "ahead of its average twin after costs in only 1 of 4 years"),
        (dict(years=[year(0.1), year(0.1), year(-0.1), year(-0.1)]), "ahead of its average twin after costs in only 2 of 4 years"),     # half is not most
        (dict(twins=twins_of(0.97, 0.35)), "over the last 365 days it beats only 35% of its twins"),
        (dict(double_costs={"left_per_year": -0.01, "sharpe": -0.1, "t": -0.1}), "at double costs nothing is left"),
        (dict(double_costs={"left_per_year": 0.0, "sharpe": 0.0, "t": 0.0}), "at double costs nothing is left"),
        (dict(nearby=read(0.2, 0.3, 0.74, 0.75, 0.8, 0.9)), "only 3 of 6 nearby settings beat 75% of their twins"),
        (dict(nearby=read(0.51, 0.55, 0.6, 0.7, 0.72, 0.74)), "only 0 of 6 nearby settings beat 75% of their twins"),     # each beats half, and none holds up
        (dict(nearby=lost * 6), "only 0 of 6 nearby settings beat 75% of their twins (6 of them could not be replayed at all)"),
        (dict(nearby=lost * 4 + read(0.8, 0.9)), "only 2 of 6 nearby settings beat 75% of their twins (4 of them could not be replayed at all)"),
        (dict(nearby=lost + read(0.8, 0.8, 0.9, 0.9, 0.9)), "1 of the 6 nearby settings could not be replayed"),          # the rest hold up, and it is said all the same
        (dict(halves=read(0.3, 0.4, 0.8, 0.9)), "only 2 of 4 halves of the coins beat 75% of their twins"),
        (dict(halves=[{"ok": True, "beaten": None}] * 4), "none of the 4 halves of the coins could be set against twins"),       # replayed, and with no twins
        (dict(clock={"why": "it reads it", "shifts": read(0.3, 0.5, 0.8, 0.2, 0.0, 0.9)}), "only 2 of 6 phases of the clock beat 75% of their twins"),
        (dict(rule_one=rule(windows=dict(a_reading()["rule_one"]["windows"], no_trade=0.5))),
         "it finishes no trade of its own in 50% of 60 day windows, so a live test would likely be killed at its look"),
        (dict(rule_one=rule(windows=None, no_trade_by_first=0.7)),
         "it finishes no trade of its own in 70% of 60 day windows, so a live test would likely be killed at its look"),
    ]
    for over, says in cases:
        r = a_reading(**over)
        assert bench.weak_spots(r) == [says], over
        assert bench.words(r) == f"Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: {says}."
    assert len(bench.weak_spots(a_reading(**{k: v for i in (0, 2, 3, 5, 10, 12, 13) for k, v in cases[i][0].items()}))) == 7
    # and what is not one
    fine = [dict(years=[year(0.1), year(0.1), year(0.1), year(-0.1)]), dict(years=[]), dict(twins=twins_of(0.97, 0.5)), dict(twins=twins_of(0.97, None)),
            dict(double_costs={"left_per_year": 0.001, "sharpe": 0.1, "t": 0.1}), dict(double_costs=None),
            dict(nearby=read(0.2, 0.3, 0.75, 0.76, 0.8, 0.9)), dict(nearby=[{"ok": True, "beaten": None}] * 2 + read(0.8, 0.9, 0.3)), dict(nearby=[]),
            dict(halves=read(0.3, 0.8, 0.8, 0.9)), dict(halves=[]), dict(clock={"why": None, "shifts": []}), dict(clock=None),
            dict(rule_one=rule(windows=dict(a_reading()["rule_one"]["windows"], no_trade=0.49))), dict(rule_one=rule(windows=None, no_trade_by_first=None))]
    for over in fine:
        assert bench.weak_spots(a_reading(**over)) == [], over
    # a quick reading has no halves and no settings to be thin on
    assert bench.weak_spots(a_reading(quick=True, halves=read(0.1), nearby=read(0.1))) == []
    with_weak = bench.words(a_reading(quick=True, twins=twins_of(0.97, 0.35), nearby=[], halves=[]))
    assert "Weak spots: over the last 365 days" in with_weak and with_weak.endswith("are not in a quick reading.")


def test_the_reading_in_one_line_and_the_league_table_say_what_the_figures_say():
    r = a_reading()
    assert bench.ledger_line(r) == ("Bench: timing +13.0% a year before costs over 1,800 days, which beats 97% of its twins (80% of them over the last "
                                    "365 days), and a book with no timing does as well 3% of the time; letting positions run added 1.0% and costs took "
                                    "4.0% a year, so +10.0% is left (Sharpe +0.80, t +1.8); ahead after costs in 4 of 4 years; nearby settings beat "
                                    "70%, 80%, 85%, 90%, 95%, 99% of their twins; halves of the coins 80%, 85%, 90%, 95%. In sample.")
    lost = [{"ok": False, "error": "x"}]
    line = bench.ledger_line(a_reading(nearby=lost * 2 + r["nearby"][:3] + [{"ok": True, "beaten": None}], halves=lost * 4, twins=twins_of(0.6, None), years=[],
                                       drift_per_year=-0.004))
    # what stands in brackets after the share is a share, and how often luck does as well stands apart from it: side by
    # side in one bracket the second read as a second chance (found in review, 2026-10-07)
    assert "which beats 60% of its twins, and a book with no timing does as well 40% of the time; letting positions run took 0.4% and costs took" in line
    assert "years" not in line
    assert "which beats 60% of its twins; letting" in bench.ledger_line(a_reading(twins=dict(twins_of(0.6, None), chance=None, worth=None)))
    assert "nearby settings beat 70%, 80%, 85% (2 could not be replayed) (1 could not be set against twins) of their twins" in line
    assert "halves of the coins no reading (4 could not be replayed). In sample." in line
    sits, late = slide_of(stay=1700.0, pair="P0"), slide_of(stay=1000.4, pair="P6")
    for why, slide, says in (("short", sits, "too short a run"), ("idle", slide_of(stay=0.0, pair=None), "it never held a position"),
                             ("new", slide_of(stay=0.25, pair="P6", history=100.0), "the pairs it holds have too short a history"),
                             ("hold", sits, "never out of P0 for 1,700 days, too long for a run of 1,800"),
                             ("hold", late, "never out of P6 for 1,000 days, too long for a run of 1,800"),
                             ("pairs", sits, "never out of P0 for 1,700 days, too long for the history of the pairs it holds"),
                             ("pairs", late, "never out of P6 for 1,000 days, too long for the history of the pairs it holds")):
        assert bench.ledger_line(no_twins(why, slide=slide)) == f"Bench: +50.0% after costs over 1,800 days; not set against twins ({says}). In sample."
    text = bench.format_reading(r)
    for said in ("bench: H9 (rising), 1,800 days from 2021-10-13 to 2026-10-06, 4 pairs",
                 "what it made: +50.0% after costs, with 0.30 of its equity invested on average. The basket (the pairs in equal parts) made -40.0%, "
                 "and the middle one of its twins -30.0% after the same costs",
                 "twins: before costs it beats 97% of 1,000 twins over the whole run and 80% over the last 365 days. A twin is the same book slid "
                 "30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with "
                 "no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 200 separate ones, and among "
                 "that many a book with no timing does as well as this about 3% of the time. No twin holds what the book took in the 180 days "
                 "after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (12 days, B) "
                 "or as long again as the candles, whichever is longer\n",
                 "what the timing is worth: +13.0% a year before costs, the book as it last traded each pair less its average twin. Letting "
                 "positions run between trades, which a twin does not, added 1.0%. Costs take 4.0% a year, so +10.0% a year is left: a yearly "
                 "Sharpe ratio of +0.80 and a t of +1.8, where a t under about 2 either way cannot be told from noise. At double costs +6.0% is left",
                 "by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +8.0%, +5.0%, +10%, 90%; 2023 ",
                 "under rule 1: about 40 fills in 60 days (a promotion needs 30); in 10% of 60 day windows it finished no trade of its own, and a "
                 "test that began in one of those is killed at its look (0% of 120 day windows)",
                 "had a test begun on each day from a year into the run (1,300 windows of 120 days, which overlap: about 12 fit end to end): its "
                 "daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 20% of them (the middle one: +0.3), and it had all three "
                 "counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 18%; a fast pass at day 60 in 2%"):
        assert said in text, said
    assert "between trades, which a twin does not, took 2.0%." in bench.format_reading(a_reading(drift_per_year=-0.02))
    # a stay longer than the candles is what the twins stop short by, and the reading gives it with its pair
    long_stay = bench.format_reading(a_reading(slide=slide_of(stay=400.0, pair="C")))
    assert ("No twin holds what the book took in the 490 days after the hour in hand: the 90 days of candles a strategy is handed, and then the "
            "longest it was in any one pair (400 days, C) or as long again as the candles, whichever is longer\n") in long_stay
    # On a run not much longer than the least the book could be slid inside, which books have twins at all hangs on how
    # their trades went: of slow trend followers on 300 days of a market with no memory, the ones that could be read beat
    # 31% of their twins on average, and of slow dip buyers 69% (found in review, 2026-10-07). The reading says so
    tight = bench.format_reading(a_reading(days=399))
    assert ("whichever is longer. Sliding this book takes 300 days of the run's 399: on a run so little longer than that, the books that can be set "
            "against twins at all are the ones that let go of their positions early, which is not a fair draw of them, and the share says less "
            "than it would on a longer one\n") in tight
    # ... and only there: said whenever sliding took over half the run, it was said of books with a stay of two years on a
    # run of five, where every one of them is read and nothing has been picked (found in review, 2026-10-07)
    assert "Sliding this book takes" not in bench.format_reading(a_reading(days=400)) and "Sliding this book takes" not in text
    # a strategy whose params were not, when the run ended, what it was handed has kept something there that it would
    # not have live, and the reading says so
    wrote = bench.format_reading(a_reading(slide=dict(slide_of(), wrote_params=True)))
    assert ("  NOTE: the strategy's params were not, at the end of the run, as they were handed to it. Live it is handed them afresh every hour, "
            "so what it kept there it would not have: if it decides on that, this replay is not what it would do\n") in wrote and "NOTE:" not in text
    # a share that is not all of them is not shown as all of them, in a sentence or in a table
    most = a_reading(twins=dict(twins_of(0.9951, 0.0049), chance=0.0012), nearby=[{"ok": True, "beaten": v} for v in (0.004, 0.5, 0.995, 1.0, 0.0)])
    assert "it beats over 99% of 1,000 twins over the whole run and under 1% over the last 365 days" in bench.format_reading(most)
    assert "which beats over 99% of its twins (under 1% of them over the last 365 days), and a book with no timing does as well under 1% of the time" in bench.ledger_line(most)
    assert "nearby settings beat 0%, <1%, 50%, >99%, 100% of their twins" in bench.ledger_line(most)
    assert bench.format_league([("H9 rising", most)]).splitlines()[1].split()[-4:-1] == [">99%", "<1%", "<1%"]
    assert [bench._share(v) for v in (None, 0.0, 0.0049, 0.005, 0.0051, 0.5, 0.9949, 0.995, 0.99999, 1.0)] == \
        ["n/a", "0%", "under 1%", "under 1%", "1%", "50%", "99%", "over 99%", "over 99%", "100%"]      # one twin in 200 is not none of them
    assert bench.weak_spots(a_reading(twins=twins_of(0.97, 0.004))) == ["over the last 365 days it beats under 1% of its twins"]
    windows = bench.format_reading(a_reading(rule_one=dict(r["rule_one"], no_trade_by_first=0.999, no_trade_by_total=0.001, windows=dict(
        r["rule_one"]["windows"], t_reached=0.001, all_counts=0.0004, fast_pass=0.0))))
    assert "in over 99% of 60 day windows it finished no trade of its own" in windows and "(under 1% of 120 day windows)" in windows
    assert "at day 120 in under 1% of them" in windows and "that t) in under 1%; a fast pass at day 60 in 0%" in windows
    # a book that could not be set against twins says which of the reasons it was, with the days that go into it
    hold = bench.format_reading(no_twins("hold", slide=slide_of(stay=1700.0, pair="P0")))
    assert ("twins: none. It was never out of P0 for 1,700 days on end. A strategy that is told what it holds can carry what it has seen for as "
            "long as it stays in a pair, so a twin may not hold what the book took within that long after the hour in hand, nor within the 90 "
            "days of candles a strategy is handed. With 30 days to slide it by and 90 more to draw the slides from, sliding it takes 1,910 days, "
            "and the run is 1,800. The bench cannot read this book's timing; that is not to say it has none\n") in hold
    assert "what the timing is worth" not in hold and "by year (what it made, the basket): 2022 +10.0%, +10%; 2023 " in hold and "n/a" not in hold
    late = bench.format_reading(no_twins("pairs", slide=slide_of(stay=1000.0, pair="P6", history=1181.0)))
    assert ("twins: none. It was never out of P6 for 1,000 days on end. A strategy that is told what it holds can carry what it has seen for as "
            "long as it stays in a pair, so a twin may not hold what the book took within that long after the hour in hand, nor within the 90 "
            "days of candles a strategy is handed. With 30 days to slide it by and 90 more to draw the slides from, sliding it takes 1,210 days, "
            "and no pair it holds has prices for more than 1,181. The bench cannot read this book's timing; that is not to say it has none\n") in late
    assert "twins: none. The book never held a position\n" in bench.format_reading(no_twins("idle", slide=slide_of(stay=0.0, pair=None)))
    takes = ("That takes 30 days to slide it by and 90 more to draw the slides from, and twice the 90 days of candles a strategy is handed, 300 "
             "days in all, and ")
    assert f"twins: none. The run is too short to slide a book inside. {takes}the run is 250 days\n" in bench.format_reading(no_twins("short", days=250))
    # a pair with prices for too short a time for any book is not told that the book stays in it too long
    young = bench.format_reading(no_twins("new", slide=slide_of(stay=0.25, pair="P6", history=100.4)))
    assert f"twins: none. No pair the book holds has prices for long enough to slide a book inside. {takes}none of them has more than 100\n" in young
    assert "never out of" not in young and "The run is too short" not in young
    # What there is falls short by hours and is given in days. Where the two would read the same, the words say that it is
    # short and not by how much: a run of 2,927 hours against the 2,928 it took read `122 days` against 122 (found in
    # review, 2026-10-07)
    assert f"{takes}the run is a few hours short of that\n" in bench.format_reading(no_twins("short", days=300))
    assert f"{takes}the run is 299 days\n" in bench.format_reading(no_twins("short", days=299))
    assert f"{takes}none of them has quite that many\n" in bench.format_reading(no_twins("new", slide=slide_of(stay=0.25, pair="P6", history=299.6)))
    assert f"{takes}none of them has more than 299\n" in bench.format_reading(no_twins("new", slide=slide_of(stay=0.25, pair="P6", history=299.4)))
    # days are given whole where they are whole and to a tenth where they are not, so that a sentence's days add up
    assert [bench._d(v) for v in (300.0, 300.04, 300.06, 111.67, 1800.0, 8.33, 0.0)] == ["300", "300", "300.1", "111.7", "1,800", "8.3", "0"]
    edge = slide_of(stay=1590.0, pair="P0")                               # sliding it takes 30 + 90 + 1,590 + 90 = 1,800 days
    bare = {k: v for k, v in edge.items() if k != "history_days"}         # a reading that does not say how long its pairs have prices for
    assert "and no pair it holds has prices for more than 0. The bench" in bench.format_reading(no_twins("pairs", slide=bare))
    assert "sliding it takes 1,800 days, and the run is a few hours short of that. The bench" in bench.format_reading(no_twins("hold", slide=edge))
    assert "sliding it takes 1,800 days, and the run is 1,799. The bench" in bench.format_reading(no_twins("hold", slide=edge, days=1799))
    assert ("sliding it takes 1,800 days, and no pair it holds has prices for quite that long. The bench"
            in bench.format_reading(no_twins("pairs", slide=dict(edge, history_days=1799.5))))
    assert ("sliding it takes 1,800 days, and no pair it holds has prices for more than 1,799. The bench"
            in bench.format_reading(no_twins("pairs", slide=dict(edge, history_days=1799.4))))
    every = bench.format_reading(a_reading(rule_one=dict(r["rule_one"], no_trade_by_first=0.0, windows=None)))
    assert "it finished a trade of its own in every 60 day window" in every and "killed at its look" not in every and "had a test begun" not in every
    no_fast = bench.format_reading(a_reading(rule_one=dict(r["rule_one"], windows=dict(r["rule_one"]["windows"], fast_pass=None, t_middle=None))))
    assert "a fast pass" not in no_fast and "(the middle one:" not in no_fast and "in 20% of them, and it had all three counts" in no_fast
    reads = bench.format_reading(a_reading(clock={"why": bench.CODE_NAMES_IT, "shifts": [{"ok": True, "beaten": v} for v in (0.5, 0.6, 0.7, 0.8, 0.9, 0.95)]}))
    assert ("the clock: its code names the candles' time column or asks the time. With the clock moved (by 27, 54, 81, 108, 135, 162 hours) it "
            "beats 50%, 60%, 70%, 80%, 90%, 95% of its twins, against its own 97%") in reads
    table = bench.format_league([("H9 rising", r), ("H10 a strategy with a very long name indeed", no_twins())])
    rows = table.splitlines()
    assert rows[0].split() == ["config", "days", "net", "timing/yr", "run/yr", "costs/yr", "left/yr", "t", "twins", "luck", "last", "365", "read", "on"]
    assert rows[1].split() == ["H9", "rising", "1,800", "+50.0%", "+13.0%", "+1.0%", "4.0%", "+10.0%", "+1.8", "97%", "3%", "80%", "2026-09-21"]
    assert rows[2].split()[-10:] == ["+50.0%", "n/a", "n/a", "4.0%", "n/a", "n/a", "n/a", "n/a", "n/a", "2026-09-21"]
    assert "luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck." in rows[3]
    assert "left/yr: timing plus run less costs." in rows[3] and "n/a: the book could not be set against twins." in rows[3]
    assert len({len(row) for row in rows[:3]}) == 1                        # the columns line up, however long a name is
    assert rows[3].startswith("Each config is read from the first hour it could decide") and rows[3].endswith("In sample, all of it.") and len(rows) == 4
    assert bench.format_league([]).splitlines()[1] == "no reading"


# --- readings on file -----------------------------------------------------------------------

STRATEGY_FILE = '''"""The strategies."""
import numpy as np

SCALE = 2


def helper(x):
    return x * SCALE


@register("rising")
def rising(candles, params, held):
    return {p: helper(1) for p in candles}


@register("other")
def other(candles, params, held):
    return {}
'''


def test_a_saved_reading_is_good_for_a_week_and_for_the_config_and_code_it_was_taken_on(strategies, root, small):
    cfg = cfg_of("rising", look_hours=12, size=0.25)
    r = bench.read(cfg, RCFG, made_up(1300), jobs=1, quick=True, n_twins=5)
    bench.save(r)
    rec = bench.saved("H9")
    assert rec == json.loads(json.dumps(bench._plain(r))) and bench.saved("H404") is None
    now = r["made_at"]
    assert bench.current(rec, cfg, RCFG, quick=True, now=now) and bench.describes(rec, cfg, RCFG)
    assert not bench.current(rec, cfg, RCFG, quick=False, now=now)        # a quick one does not stand in for a whole one
    assert bench.current(dict(rec, quick=False), cfg, RCFG, quick=False, now=now) and bench.current(dict(rec, quick=False), cfg, RCFG, quick=True, now=now)
    assert bench.current(rec, cfg, RCFG, True, now=now + 7 * DAY - 1) and not bench.current(rec, cfg, RCFG, True, now=now + 7 * DAY)
    assert not bench.current(rec, cfg, RCFG, True, now=now - 1)           # a reading from the future is not believed
    assert bench.describes(rec, cfg, RCFG) and bench.STALE_AFTER_S == 7 * DAY      # it is still a reading of this config, a week on
    assert not bench.current(rec, dict(cfg, params={**cfg["params"], "size": 0.2}), RCFG, True, now=now)
    assert not bench.current(rec, dict(cfg, strategy="fridays"), RCFG, True, now=now)
    for key, other in (("fee_bps", 12), ("slippage_bps", 6), ("impact_bps", 3), ("initial_cash", 5_000), ("history_hours", 300),
                       ("max_weight_per_pair", 0.2), ("max_gross_weight", 0.9), ("min_trade_notional", 60), ("rebalance_threshold", 0.04),
                       ("daily_loss_halt", 0.06), ("max_fills_per_pair_per_day", 3), ("pairs", ["AAA"])):
        assert not bench.current(rec, cfg, dict(RCFG, **{key: other}), True, now=now), key      # the costs and limits it was taken under
        assert not bench.describes(rec, cfg, dict(RCFG, **{key: other})), key
    for key, other in (("window_days", 45), ("confirm_days", 30), ("min_trades", 12), ("min_skill_t", 1.5), ("fast_pass_skill_t", 2.0)):
        assert not bench.current(rec, cfg, dict(RCFG, challenger={"slots": 2, key: other}), True, now=now), key     # the counts the live rule asks for
    assert set(bench.RESTS_ON) == {"fee_bps", "slippage_bps", "impact_bps", "initial_cash", "history_hours", "max_weight_per_pair", "max_gross_weight",
                                   "min_trade_notional", "rebalance_threshold", "daily_loss_halt", "max_fills_per_pair_per_day", "pairs"}
    assert bench.current(rec, dict(cfg, hypothesis="H10"), dict(RCFG, ruleset=8, challenger={"slots": 4}), True, now=now)       # not what a reading rests on
    assert not bench.current(dict(rec, version=bench.VERSION + 1), cfg, RCFG, True, now=now)
    assert not bench.current(None, cfg, RCFG, True, now=now) and not bench.current({}, cfg, RCFG, True, now=now)
    for when in ("soon", None, float("inf"), float("nan"), [1]):
        assert not bench.current(dict(rec, made_at=when), cfg, RCFG, True, now=now), when
    assert not bench.current(rec, {"params": {}}, RCFG, True, now=now) and not bench.describes(rec, {}, RCFG)      # a config that cannot be signed
    (root / "state" / "bench" / "H9.json").write_text("{ not json")
    assert bench.saved("H9") is None


def test_a_reading_goes_stale_with_the_code_its_replays_run_and_with_no_other(strategies, root):
    """Its own strategy and what that reaches in bot/strategy.py, and every module of bot/ a replay can
    run. Not a comment, not the layout, and not another slot's strategy: with the whole of every file
    in the signature, an edit to any strategy sent all five configs to be read again, hours of replays,
    on eight days in the three weeks before this was written (found in review, 2026-10-07)."""
    cfg = cfg_of("rising", look_hours=12)
    code = root / "bot" / "strategy.py"
    code.write_text(STRATEGY_FILE)
    signed = bench.signature(cfg, RCFG)
    same_code = [STRATEGY_FILE.replace("    return {p: helper(1) for p in candles}", "    # a note to self\n    return {p: helper(1)\n            for p in candles}"),
                 STRATEGY_FILE.replace("SCALE = 2\n", "SCALE = 2          # twice\n\n\n"),
                 STRATEGY_FILE.replace("    return {}", "    return {'x': 1}"),                       # another slot's strategy
                 STRATEGY_FILE + '\n\n@register("third")\ndef third(candles, params, held):\n    return {}\n',
                 STRATEGY_FILE.replace('@register("other")\ndef other(candles, params, held):\n    return {}\n', "")]
    for text in same_code:
        code.write_text(text)
        assert bench.signature(cfg, RCFG) == signed, text
    other_code = [STRATEGY_FILE.replace("helper(1) for", "helper(2) for"), STRATEGY_FILE.replace("return x * SCALE", "return x + SCALE"),
                  STRATEGY_FILE.replace("SCALE = 2", "SCALE = 3"), STRATEGY_FILE.replace("import numpy as np", "import numpy as np\nimport math"),
                  STRATEGY_FILE + "\n\ndef helper(x):\n    return x\n", STRATEGY_FILE.replace('"""The strategies."""', '"""The strategies, as of today."""')]
    for text in other_code:
        code.write_text(text)
        assert bench.signature(cfg, RCFG) != signed, text
    # another registered strategy that this one calls is part of this one
    calls = STRATEGY_FILE.replace("{p: helper(1) for p in candles}", "other(candles, params, held)")
    code.write_text(calls)
    with_call = bench.signature(cfg, RCFG)
    code.write_text(calls.replace("    return {}", "    return {'x': 1}"))
    assert bench.signature(cfg, RCFG) != with_call != signed
    assert b"'other'" in bench.strategy_code("rising") and b"'rising'" not in bench.strategy_code("other")
    # the two configs of one file are apart, and a strategy registered under two names is in both
    code.write_text(STRATEGY_FILE)
    assert bench.strategy_code("rising") != bench.strategy_code("other")
    assert b"'other'" not in bench.strategy_code("rising") and b"'rising'" not in bench.strategy_code("other") and b"helper" in bench.strategy_code("other")
    code.write_text(STRATEGY_FILE.replace('@register("other")', '@register("other")\n@register("rising2")'))
    assert b"'other'" in bench.strategy_code("rising2") and b"'other'" not in bench.strategy_code("rising")
    # a file that cannot be read as code is taken as it stands
    code.write_text("def broken(:\n")
    whole = bench.signature(cfg, RCFG)
    code.write_text("def broken(:\n# and a comment\n")
    assert bench.signature(cfg, RCFG) != whole
    code.unlink()
    assert bench.strategy_code("rising") == b""
    code.write_text(STRATEGY_FILE)
    assert bench.signature(cfg, RCFG) == signed
    # the engine, and anything else in bot/ a replay may run: a module nobody has listed is taken to be one
    for name in ("run", "paper", "risk", "backtest", "bench", "promote", "data", "config", "a_new_helper"):
        (root / "bot" / f"{name}.py").write_text("# changed\n")
        assert bench.signature(cfg, RCFG) != signed, name
        (root / "bot" / f"{name}.py").unlink()
        assert bench.signature(cfg, RCFG) == signed
    assert bench.NO_REPLAY_RUNS == ("wide", "report", "slot", "shadow")    # no replay runs these
    for name in bench.NO_REPLAY_RUNS:
        (root / "bot" / f"{name}.py").write_text("# changed\n")
        assert bench.signature(cfg, RCFG) == signed, name
    assert all((REPO / "bot" / f"{name}.py").exists() for name in bench.NO_REPLAY_RUNS)
    assert len(signed) == 16 and bench.signature(cfg, RCFG) == bench.signature(dict(cfg, hypothesis="H77"), RCFG)


def test_a_reading_on_file_is_plain_json_under_a_plain_name(strategies, root, small):
    import datetime
    odd = {"a": np.float64(1.5), "b": np.int64(3), "c": float("nan"), "d": [np.bool_(True), float("inf")], "e": {1: None}, "f": (1, 2),
           "g": datetime.date(2024, 1, 1), "h": np.array([1.0, np.nan]), "i": {"x"}, "j": True, "k": "text", "l": 7}
    assert bench._plain(odd) == {"a": 1.5, "b": 3, "c": None, "d": [True, None], "e": {"1": None}, "f": [1, 2], "g": "2024-01-01", "h": [1.0, None],
                                 "i": "{'x'}", "j": True, "k": "text", "l": 7}
    assert type(bench._plain(np.bool_(True))) is bool and type(bench._plain(np.int64(3))) is int and type(bench._plain(True)) is bool
    bench.save({"hypothesis": "H7", **odd})
    text = (root / "state" / "bench" / "H7.json").read_text()
    assert "NaN" not in text and "Infinity" not in text and json.loads(text)["c"] is None
    # the name comes from a config file and becomes a file name
    for name in ("../H7", "a/b", "", ".hidden", "H 7", "H7.json", None, "x" * 41, 7):
        with pytest.raises(ValueError, match="not a name a file can safely have"):
            bench.save({"hypothesis": name})
        assert bench.saved(name) is None
    assert sorted(p.name for p in (root / "state").rglob("*") if p.is_file()) == ["H7.json"] and not (root / "H7.json").exists()
    bench.save({"hypothesis": "H12_b-2"})
    assert bench.saved("H12_b-2") == {"hypothesis": "H12_b-2"}
    (root / "state" / "bench" / "H7.json").write_text("[1, 2]")
    assert bench.saved("H7") is None                                        # a file that is not a reading is no reading
    # A config may hold what JSON cannot: YAML reads `not_before: 2024-01-01` as a date. Its reading is kept all
    # the same, and is still its reading the night after (it used to fail to save, every night, and be read again)
    cfg = yaml.safe_load("hypothesis: H13\nstrategy: rising\nparams:\n  look_hours: 12\n  not_before: 2024-01-01\n")
    assert isinstance(cfg["params"]["not_before"], datetime.date)
    r = bench.read(cfg, RCFG, made_up(1300), jobs=1, quick=True, n_twins=5)
    bench.save(r)
    rec = bench.saved("H13")
    assert rec["params"] == {"look_hours": 12, "not_before": "2024-01-01"} and bench.current(rec, cfg, RCFG, quick=True) and bench._shows("H13 rising", rec)
    assert not bench._shows("x", {"hypothesis": "H7"}) and not bench._shows("x", dict(rec, rule_one={})) and not bench._shows("x", dict(rec, made_at="soon"))


def run_main(*args):
    return bench.main(list(args))


@pytest.fixture
def league(strategies, root, small, monkeypatch):
    """The command line with made up candles behind it and a dozen twins."""
    c = made_up(900)
    monkeypatch.setattr(backtest, "load_cached_candles", lambda pairs: {p: c[p] for p in pairs})
    monkeypatch.setattr(bench, "TWINS", 12)
    monkeypatch.setattr(bench, "SUB_TWINS", 6)
    return root


def test_the_league_takes_each_config_in_use_once_and_keeps_what_it_is_told_to(league, monkeypatch, capsys):
    root = league
    use, problems = bench.configs_in_use()
    assert [label for label, _ in use] == ["H0 rising (champion)", "H9 rising"] and problems == []        # the idle slot is the champion again
    assert run_main("--all", "--quick", "--jobs", "1") == 0
    out = capsys.readouterr().out
    assert "[bench] H0 rising (champion): read, " in out and "[bench] H9 rising: read, " in out and "In sample, all of it." in out
    table = out[out.index("config "):].splitlines()
    assert table[0].split() == ["config", "days", "net", "timing/yr", "run/yr", "costs/yr", "left/yr", "t", "twins", "luck", "last", "365", "read", "on"]
    assert len(table) == 4 and table[1].startswith("H0 rising (champion)") and table[2].startswith("H9 rising")
    assert len({len(row) for row in table[:3]}) == 1 and "nan" not in out.lower() and "None" not in out      # the columns line up
    days = table[1].split()[3]
    assert 34 <= int(days) <= 37 and f"Over the first row's {days} days the basket made" in table[3]         # 900 hours, less the warm up
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", table[1].split()[-1])
    assert not (root / "state" / "bench").exists() and not (root / "configs" / "challenger3.yaml").exists()      # reading writes nothing, anywhere
    assert run_main("--all", "--quick", "--jobs", "1", "--save") == 0
    capsys.readouterr()
    assert sorted(p.name for p in (root / "state" / "bench").iterdir()) == ["H0.json", "H9.json", "README.md"]
    assert sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and "state" in p.parts) == \
        ["state/bench/H0.json", "state/bench/H9.json", "state/bench/README.md"]
    readme = (root / "state" / "bench" / "README.md").read_text()
    assert readme.startswith("# The bench's league table\n\nLast changed on 20") and " UTC. The bench workflow (`python -m bot.bench --all --save`) " in readme
    assert "each row says the day it was read on. bot/bench.py says how each figure is made.\n\n```\nconfig " in readme
    assert "## Not read" not in readme and "FAILED" not in readme
    assert "H0 rising (champion)" in readme and "bench: H9 (rising)" in readme and "bench: H0 (rising)" in readme and readme.count("Bench: timing ") == 2
    first = (root / "state" / "bench" / "H9.json").read_text()
    # the next run finds both current and replays nothing
    monkeypatch.setattr(bench, "read_many", lambda *a, **k: pytest.fail("a current reading was taken again"))
    assert run_main("--all", "--quick", "--jobs", "1", "--save") == 0
    out = capsys.readouterr().out
    assert out.count("the saved reading is current") == 2 and "H9 rising" in out
    assert (root / "state" / "bench" / "H9.json").read_text() == first
    table = root / "state" / "bench" / "README.md"
    assert table.read_text() == readme
    # A table that would differ only in when it was written is not written again, at whatever hour: the heading held the
    # time of writing, so every night was a commit of its own, and each of those one more push to land between the hourly
    # bot's (found in review, 2026-10-07). What does change it is a reading, or a line under Not read
    use, rcfg, later = bench.configs_in_use()[0], config.risk_cfg(), int(time.time()) + 3 * 3600
    stamp = lambda ts: time.strftime("Last changed on %Y-%m-%d at %H:%M UTC.", time.gmtime(ts))        # noqa: E731
    bench.write_table(use, {}, [], rcfg, now=later)
    assert table.read_text() == readme and stamp(later) not in readme
    bench.write_table(use, {}, ["H9 rising: it broke"], rcfg, now=later)
    broke = table.read_text()
    assert stamp(later) in broke and "\n## Not read\n\n- FAILED: H9 rising: it broke\n" in broke
    bench.write_table(use, {}, ["H9 rising: it broke"], rcfg, now=later + 3600)
    assert table.read_text() == broke                                     # the same line the night after: nothing new to say
    bench.write_table(use, {}, [], rcfg, now=later + 7200)
    mended = table.read_text()
    assert stamp(later + 7200) in mended and mended.split(" UTC.", 1)[1] == readme.split(" UTC.", 1)[1]
    table.write_text("not a table at all")                                # and a file that is not the table is simply written over
    bench.write_table(use, {}, [], rcfg, now=later)
    assert table.read_text() == mended.replace(stamp(later + 7200), stamp(later))


def test_stale_readings_are_taken_again_one_config_at_a_time_and_each_is_kept_as_it_is_done(league, monkeypatch, capsys):
    root = league
    assert run_main("--all", "--quick", "--jobs", "1", "--save") == 0
    capsys.readouterr()
    config.dump_yaml(root / "configs" / "challenger1.yaml", cfg_of("rising", look_hours=30, size=0.25))        # the slot's config changed
    asked, real = [], bench.read_many
    monkeypatch.setattr(bench, "read_many", lambda configs, *a, **k: asked.append([x["params"] for x in configs]) or real(configs, *a, **k))
    assert run_main("--all", "--quick", "--jobs", "1", "--save") == 0
    assert asked == [[{"look_hours": 30, "size": 0.25}]] and "H0 rising (champion): the saved reading is current" in capsys.readouterr().out
    assert json.loads((root / "state" / "bench" / "H9.json").read_text())["params"] == {"look_hours": 30, "size": 0.25}
    assert run_main("--all", "--quick", "--jobs", "1", "--save", "--again") == 0 and len(asked[-1]) == 2      # quick readings share the processors
    capsys.readouterr()
    # Whole readings are taken one config at a time. Each is kept, and the table written again, as soon as it is
    # done, so that a job stopped part way has lost one reading and not the night's work, and the table on file
    # is never one from before the run
    asked.clear()
    on_file, tables = [], []

    def one_at_a_time(configs, *a, **k):
        asked.append([x["params"] for x in configs])
        on_file.append(sorted(p.name for p in (root / "state" / "bench").glob("H*.json") if not json.loads(p.read_text())["quick"]))
        tables.append((root / "state" / "bench" / "README.md").read_text())
        return real(configs, *a, **k)
    monkeypatch.setattr(bench, "read_many", one_at_a_time)
    assert run_main("--all", "--jobs", "1", "--save") == 0                # the quick ones on file do not stand in for whole ones
    assert [len(a) for a in asked] == [1, 1] and on_file == [[], ["H0.json"]]
    assert all(not json.loads((root / "state" / "bench" / f"{h}.json").read_text())["quick"] for h in ("H0", "H9"))
    assert "half the coins" not in tables[0] and tables[0].count("bench: H") == 2       # at the start: the quick readings on file, with their dates
    assert tables[1].count("half the coins") == 1 and "bench: H0 (rising)" in tables[1] and "bench: H9 (rising)" in tables[1]
    assert (root / "state" / "bench" / "README.md").read_text().count("half the coins") == 2
    capsys.readouterr()
    monkeypatch.setattr(bench, "read_many", lambda configs, *a, **k: asked.append([x["params"] for x in configs]) or real(configs, *a, **k))
    # a reading on file that has lost a part cannot be put into words: it is taken again, not shown and not fatal
    rec = json.loads((root / "state" / "bench" / "H0.json").read_text())
    del rec["rule_one"]
    (root / "state" / "bench" / "H0.json").write_text(json.dumps(rec))
    asked.clear()
    assert run_main("--all", "--quick", "--jobs", "1", "--save") == 0 and [len(a) for a in asked] == [1]
    assert "rule_one" in json.loads((root / "state" / "bench" / "H0.json").read_text())


def test_a_config_that_cannot_be_read_turns_the_run_red_and_has_its_line_in_the_table(league, capsys):
    """Whatever the failure and whichever kind of reading: the others are still read, kept and shown, the
    table says which config it has no reading of, and the exit code is 1. On the path the workflow runs
    (whole readings, kept) a config with a strategy nobody had registered used to end the run where it
    stood: the configs after it were never read, that night or any other, and no table was written
    (found in review, 2026-10-07)."""
    root = league
    assert run_main("--all", "--jobs", "2", "--save") == 0
    capsys.readouterr()
    readme = root / "state" / "bench" / "README.md"
    for quick in ((), ("--quick",)):
        config.dump_yaml(root / "configs" / "champion.yaml", dict(cfg_of("no_such_strategy"), hypothesis="H0"))        # the first one in the order
        config.dump_yaml(root / "configs" / "challenger2.yaml", dict(cfg_of("no_such_strategy"), hypothesis="H0"))
        assert run_main("--all", "--jobs", "2", "--save", "--again", *quick) == 1
        out = capsys.readouterr().out
        assert "[bench] FAILED: H0 no_such_strategy (champion): KeyError: \"unknown strategy 'no_such_strategy'" in out
        assert "[bench] H9 rising: read, " in out and out.splitlines()[-2].startswith("H9 rising")      # the one after it is read and shown
        text = readme.read_text()
        assert "## Not read\n\n- H0 no_such_strategy (champion): no reading on file of this config as it now is\n- FAILED: H0 no_such_strategy (champion): KeyError" in text
        assert "bench: H0 (" not in text and "bench: H9 (rising)" in text                              # what is on file under H0 is of another config
        assert json.loads((root / "state" / "bench" / "H0.json").read_text())["strategy"] == "rising"  # and is left as it was
        config.dump_yaml(root / "configs" / "champion.yaml", dict(cfg_of("rising", look_hours=24, size=0.2), hypothesis="H0"))
        config.dump_yaml(root / "configs" / "challenger2.yaml", dict(cfg_of("rising", look_hours=24, size=0.2), hypothesis="H0"))
    # a strategy that fails on some hours, one that takes its process down, a name that cannot be a file's
    for bad, says in ((cfg_of("sometimes", look_hours=12), "its replay failed: RuntimeError: the strategy failed on "),
                      (cfg_of("dies"), "died before it could answer (exit code 7)" if FORKS else None),
                      (dict(cfg_of("rising", look_hours=30), hypothesis="../H9"), "not a name a file can safely have")):
        if says is None:
            continue
        config.dump_yaml(root / "configs" / "challenger1.yaml", bad)
        assert run_main("--all", "--jobs", "2", "--save") == 1
        out = capsys.readouterr().out
        assert f"[bench] FAILED: {bad['hypothesis']} {bad['strategy']}: " in out and says in out and "H0 rising (champion)" in out
        assert f"- FAILED: {bad['hypothesis']} {bad['strategy']}: " in readme.read_text() and "bench: H0 (rising)" in readme.read_text()
    assert not (root / "state" / "H9.json").exists() and sorted(p.name for p in (root / "state" / "bench").iterdir()) == ["H0.json", "H9.json", "README.md"]
    # every config failing is a failure too, with nothing shown
    config.dump_yaml(root / "configs" / "champion.yaml", dict(cfg_of("broken"), hypothesis="H0"))
    config.dump_yaml(root / "configs" / "challenger1.yaml", dict(cfg_of("broken"), hypothesis="H0"))
    config.dump_yaml(root / "configs" / "challenger2.yaml", dict(cfg_of("broken"), hypothesis="H0"))
    assert run_main("--all", "--quick", "--jobs", "1") == 1
    assert capsys.readouterr().out.splitlines()[-1] == "[bench] FAILED: no reading was taken this time"


def test_when_the_bench_itself_fails_on_one_config_the_next_is_still_read(league, monkeypatch, capsys):
    """Whatever goes wrong in the taking of one reading costs that reading. A machine that would not
    start a process used to end the run where it stood, with no line for the config it was on and
    nothing read after it (found in review, 2026-10-07)."""
    root, real, asked = league, bench.read_many, []

    def breaks_once(configs, *a, **k):
        asked.append(configs[0]["hypothesis"])
        if len(asked) == 1:
            raise BlockingIOError(11, "Resource temporarily unavailable")
        return real(configs, *a, **k)
    monkeypatch.setattr(bench, "read_many", breaks_once)
    assert run_main("--all", "--jobs", "1", "--save") == 1
    out = capsys.readouterr().out
    assert asked == ["H0", "H9"] and "[bench] H9 rising: read, " in out
    assert "[bench] FAILED: H0 rising (champion): the bench itself failed (BlockingIOError: [Errno 11] Resource temporarily unavailable)" in out
    text = (root / "state" / "bench" / "README.md").read_text()
    assert "- FAILED: H0 rising (champion): the bench itself failed (BlockingIOError" in text and "bench: H9 (rising)" in text
    assert sorted(p.name for p in (root / "state" / "bench").iterdir()) == ["H9.json", "README.md"]


def test_configs_that_cannot_be_taken_are_problems_and_not_left_out_in_silence(league, capsys):
    root = league
    (root / "configs" / "challenger2.yaml").unlink()                      # a slot the hourly loop has not made yet is idle, and no problem
    assert bench.configs_in_use()[1] == [] and len(bench.configs_in_use()[0]) == 2
    assert not (root / "configs" / "challenger2.yaml").exists()           # and the bench does not make it either
    (root / "configs" / "challenger2.yaml").write_text("hypothesis: H3\nstrategy: rising\n")          # no params
    use, problems = bench.configs_in_use()
    assert [label for label, _ in use] == ["H0 rising (champion)", "H9 rising"]
    assert problems == ["configs/challenger2.yaml cannot be read (configs/challenger2.yaml is missing required key 'params')"]
    assert run_main("--all", "--quick", "--jobs", "1", "--save") == 1     # red: until now it was left out with a line nobody read, and the run was green
    out = capsys.readouterr().out
    assert "[bench] FAILED: configs/challenger2.yaml cannot be read" in out and "H9 rising" in out.splitlines()[-2]
    assert "- FAILED: configs/challenger2.yaml cannot be read" in (root / "state" / "bench" / "README.md").read_text()
    # a file that is not YAML at all: what its parser says comes as several lines with this machine's paths in them, and
    # the line goes into a table that is committed (found in review, 2026-10-07)
    (root / "configs" / "challenger2.yaml").write_text("hypothesis: [unclosed\n")
    said = bench.configs_in_use()[1][0]
    assert said.startswith("configs/challenger2.yaml cannot be read (") and "\n" not in said and str(root) not in said and "  " not in said
    assert bench._line(f"a\n   b {root}/configs/x.yaml  c {root}") == "a b configs/x.yaml c ."
    # two different configs under one hypothesis name: their readings would be kept in one file, each night's over the other's
    config.dump_yaml(root / "configs" / "challenger2.yaml", cfg_of("rising", look_hours=40))
    use, problems = bench.configs_in_use()
    assert [label for label, _ in use] == ["H0 rising (champion)", "H9 rising"] and use[1][1]["params"]["look_hours"] == 12
    assert problems == ["configs/challenger2.yaml and configs/challenger1.yaml are different configs under one hypothesis name, H9; only the first is read"]
    # the same config in two slots is one config, under whichever name
    config.dump_yaml(root / "configs" / "challenger2.yaml", dict(cfg_of("rising", look_hours=12, size=0.25, band=0.01), hypothesis="H77"))
    assert bench.configs_in_use()[1] == [] and len(bench.configs_in_use()[0]) == 2
    # the number of slots cannot be read: nothing is run until that is mended (bot/config.py), and it is said
    config.dump_yaml(root / "configs" / "risk.yaml", dict(RCFG, challenger={"slots": 2.5}))
    use, problems = bench.configs_in_use()
    assert use == [] and "challenger.slots must be a whole number" in problems[0] and len(problems) == 2
    assert run_main("--all", "--quick", "--jobs", "1") == 1
    assert "[bench] FAILED: no reading was taken this time" in capsys.readouterr().out
    config.dump_yaml(root / "configs" / "risk.yaml", RCFG)
    (root / "configs" / "champion.yaml").unlink()
    use, problems = bench.configs_in_use()
    assert [label for label, _ in use] == ["H9 rising"] and len(problems) == 1 and problems[0].startswith("configs/champion.yaml cannot be read (")


def test_the_bench_stops_itself_when_its_time_is_up_and_says_what_it_has_not_read(league, capsys):
    root = league
    assert run_main("--all", "--quick", "--jobs", "1", "--save", "--minutes", "0") == 1
    out = capsys.readouterr().out
    assert out.count("[bench] FAILED: ") == 3 and "[bench] FAILED: H0 rising (champion): not run: the bench's time ran out" in out
    assert out.splitlines()[-1] == ("[bench] FAILED: no reading was taken this time, and none on file is current (state/bench/README.md shows "
                                    "the older ones that still describe their configs)")
    text = (root / "state" / "bench" / "README.md").read_text()
    assert sorted(p.name for p in (root / "state" / "bench").iterdir()) == ["README.md"] and "no reading\n" in text
    assert "- H9 rising: no reading on file of this config as it now is" in text and "- FAILED: H9 rising: not run: the bench's time ran out" in text
    # with whole readings the second config is not begun once the time is up
    assert run_main("--all", "--jobs", "2", "--save", "--minutes", "0") == 1
    assert "[bench] FAILED: H9 rising: not run: the bench's time ran out" in capsys.readouterr().out
    assert run_main("--all", "--quick", "--jobs", "1", "--save", "--minutes", "30") == 0
    capsys.readouterr()
    assert sorted(p.name for p in (root / "state" / "bench").iterdir()) == ["H0.json", "H9.json", "README.md"]


def test_one_config_is_read_from_its_file_and_what_is_asked_for_is_checked(league, capfd):
    root, capsys = league, capfd                                           # at the level of the process, so that what a replay's own process prints is seen
    config.dump_yaml(root / "configs" / "challenger1.yaml", cfg_of("rising", look_hours=12, size=0.25))
    assert run_main("--config", "configs/challenger1.yaml", "--quick", "--jobs", "1") == 0
    out = capsys.readouterr().out
    assert out.startswith("bench: H9 (rising)") and out.splitlines()[-1].startswith("  Bench: timing ") and out.splitlines()[-2].startswith("  Reading: ")
    assert run_main("--config", "configs/challenger1.yaml", "--quick", "--jobs", "1", "--json", "--days", "20") == 0
    said = capsys.readouterr()
    r = json.loads(said.out)
    assert r["hypothesis"] == "H9" and 19 <= r["days"] <= 21 and r["quick"] is True and r["twins"] is None
    assert not (root / "state" / "bench").exists()
    # the whole league as JSON: one document on the way out, and what is said along the way goes elsewhere
    assert run_main("--all", "--quick", "--jobs", "1", "--json") == 0
    said = capsys.readouterr()
    doc = json.loads(said.out)
    assert [x["label"] for x in doc["readings"]] == ["H0 rising (champion)", "H9 rising"] and doc["problems"] == []
    assert doc["readings"][1]["twins"]["n"] == 12 and "[bench] H9 rising: read, " in said.err and "[bench]" not in said.out
    # what a strategy prints is no part of a reading: it goes with the rest of what is said along the way
    config.dump_yaml(root / "configs" / "talks.yaml", cfg_of("chatty", look_hours=12, size=0.25))
    assert run_main("--config", "configs/talks.yaml", "--quick", "--jobs", "1", "--json") == 0
    said = capfd.readouterr()
    assert json.loads(said.out)["strategy"] == "chatty" and "the strategy says" not in said.out and "the strategy says: still here" in said.err
    # a file that is not there, one that is not a config, one whose strategy fails: said in a line, and red
    (root / "configs" / "half.yaml").write_text("hypothesis: H3\nparams: {}\n")
    config.dump_yaml(root / "configs" / "bad.yaml", cfg_of("broken"))
    for name, says in (("configs/none.yaml", "No such file"), ("configs/half.yaml", "configs/half.yaml is missing 'strategy'"),
                       ("configs/bad.yaml", "its replay failed: RuntimeError: the strategy failed on ")):
        assert run_main("--config", name, "--quick", "--jobs", "1") == 1
        out = capsys.readouterr().out
        assert out.startswith(f"[bench] FAILED: {name}: ") and says in out and out.count("\n") == 1, out
    # what cannot be meant is refused before anything is read
    for args in ((), ("--all", "--config", "configs/challenger1.yaml"), ("--config", "configs/challenger1.yaml", "--save"),
                 ("--all", "--save", "--days", "40"), ("--all", "--again"), ("--all", "--quick", "--days", "forty")):
        with pytest.raises(SystemExit) as stopped:
            run_main(*args)
        assert stopped.value.code == 2, args
    assert "--save keeps readings of all the history on file, so it does not go with --days" in capsys.readouterr().err
    assert not (root / "state" / "bench").exists()


# --- the repo around it ----------------------------------------------------------------------

def test_the_bench_is_protected_and_carries_nothing_the_gate_forbids():
    protected = (REPO / "PROTECTED.txt").read_text().split()
    assert "bot/bench.py" in protected and "state/**" in protected and "tests/gate/**" in protected
    r = subprocess.run([sys.executable, str(REPO / "gate" / "check_protected.py"), "--help"], capture_output=True, text=True)
    assert r.returncode == 0
    src = (REPO / "bot" / "bench.py").read_text()
    for word in ("requests", "urllib", "socket", "api_key", "secret", "create_order", "place_order", "withdraw"):
        assert word not in src.lower(), word


def names_the_bench(src: str) -> list[str]:
    """Where a module imports the bench or spells out its folder."""
    import ast
    found = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Import) and any(a.name.split(".")[-1] == "bench" for a in node.names):
            found.append(f"line {node.lineno}: an import of bench")
        if isinstance(node, ast.ImportFrom) and ((node.module or "").split(".")[-1] == "bench" or any(a.name == "bench" for a in node.names)):
            found.append(f"line {node.lineno}: an import of bench")
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if "state/bench" in node.value or "bot.bench" in node.value or node.value == "bench":
                found.append(f"line {node.lineno}: the text {node.value[:30]!r}")
    return found


def test_nothing_else_in_bot_reads_the_bench():
    """The bench ranks ideas for a slot; no rule leans on it. Until Fin decides otherwise it stays that
    way: no other module of bot/ imports it or spells out the folder it saves to. That is every module
    the hourly loop runs and the one file of the loop the agent may change, bot/strategy.py, which was
    not on the list at first (found in review, 2026-10-07): a strategy that read its own reading would
    be trading on the years it is about to be tested on. (The backtest is used by the bench, not the
    other way round.)"""
    modules = sorted(p for p in (REPO / "bot").glob("*.py") if p.name != "bench.py")
    assert {"strategy.py", "run.py", "promote.py", "report.py", "slot.py", "backtest.py", "wide.py"} <= {p.name for p in modules}
    for path in modules:
        assert names_the_bench(path.read_text(encoding="utf-8")) == [], path.name
    for leaning in ("from . import bench", "from .bench import saved", "import bot.bench as b", "from bot import config, bench",
                    'p = config.STATE / "bench" / "H5.json"', 'open("state/bench/README.md")', '__import__("importlib").import_module("bot.bench")'):
        assert names_the_bench(leaning), leaning                                              # the reading itself bites
    for innocent in ("x = 'the benchmark'", "from . import config, data", "import benchmarks", "bench = 3",
                     '"""Net return minus a benchmark at the usual exposure."""', '"""for bot/bench.py: what the book was worth"""'):
        assert names_the_bench(innocent) == [], innocent


def test_the_watch_on_the_hourly_loop_and_on_every_strategy_covers_the_benchs_folder(tmp_path):
    """Three hours of the real loop are driven, in tests/gate/test_wide.py, once with nothing beside it
    and once with the wide data and a reading that flatters the slot's test: the loop must print and
    leave the same both times, leave the readings as they were, and open none of them. And every
    strategy on the books is called beside a reading under every hypothesis the configs name. Those
    tests do the driving; this one holds that the watch they rely on does see a read of the bench's
    files, and that they still plant what they say they plant."""
    from tests.gate import hourly_driver
    assert "bench" in hourly_driver.WATCHED and set(hourly_driver.BENCH_FILES) == {"H9.json", "README.md"}
    hourly_driver.plant_bench(tmp_path, ["H0", "H4"])
    assert sorted(p.name for p in (tmp_path / "state" / "bench").iterdir()) == ["H0.json", "H4.json", "H9.json", "README.md"]
    assert json.loads((tmp_path / "state" / "bench" / "H4.json").read_text())["hypothesis"] == "H4"
    with hourly_driver.watching() as seen:
        (tmp_path / "state" / "bench" / "H9.json").read_text()
        sorted((tmp_path / "state" / "bench").iterdir())
        (tmp_path / "state" / "bench" / "README.md").exists()               # asking whether it is there is not reading it
        noted = list(seen)
    assert "open state/bench/H9.json" in noted and {"os.listdir state/bench", "os.scandir state/bench"} & set(noted)
    assert all(n.split(" ", 1)[1].startswith("state/bench") for n in noted)
    # the files under the watched folders are the ones compared before and after a run, and never among those compared across runs
    assert set(hourly_driver._files(tmp_path, inside=True)) == {"state/bench/", "state/bench/H0.json", "state/bench/H4.json", "state/bench/H9.json",
                                                                "state/bench/README.md"}
    (tmp_path / "state" / "summary.md").write_text("x")
    assert set(hourly_driver._files(tmp_path, inside=False)) == {"state/", "state/summary.md"}
    wide = (REPO / "tests" / "gate" / "test_wide.py").read_text()
    for said in ("hourly.BENCH_FILES.items()", "'bot.bench' not in sys.modules", "the bench must not be imported by the hourly loop",
                 "hourly.plant_bench(root, sorted(set(hypotheses) - {\"H9\"}))", 'touched == [f"open state/bench/{its_own}.json"] * 2',
                 "not any(\"bench\" in k for k in plain_files)"):
        assert said in wide, said
    driver = (REPO / "tests" / "gate" / "hourly_driver.py").read_text()
    assert "    if bait:\n        plant(root, feed)\n        plant_bench(root)\n" in driver       # beside the run with the bait, and only that one


def flat(text: str) -> str:
    return " ".join(text.split())


def test_the_agent_is_told_to_read_the_bench_before_spending_a_slot():
    manual, sheet = flat((REPO / "CLAUDE.md").read_text()), flat((REPO / ".github" / "agent_prompt.md").read_text())
    command = "python -m bot.bench --config configs/challenger<k>.yaml --quick"
    for text in (manual, sheet):
        assert command in text and "state/bench/README.md" in text and "`not taken:`" in text and "`Not read`" in text
        assert "`timeout` set to 1800000" in text and "30 minutes" in text      # in the unit the tool takes, not as a command of its own
        assert "`--save`" in text and text.count("--save") == 1           # named once, to say never
        assert "begins `Bench:`" in text
    assert "Never run the bench with `--save`" in manual and "never add `--save`" in sheet
    assert "can show that an idea has nothing, never that it has something" in manual
    assert "No rule leans on it" in manual and "Take no more than two such readings in one run" in manual
    assert "if one runs out of time do not take it again" in manual and "do not run it again" in sheet
    # the rule of thumb in the manual is the one the reading's own words go by
    assert "Beats fewer than half its twins: no sign of timing." in manual and bench.NO_TIMING_BELOW == 0.5
    assert "No timing does as well more than one time in ten: cannot be told from luck." in manual and bench.LUCK_ABOVE == 0.10
    assert "One in ten is not proof either" in manual and "mend it before the proposal" in manual
    assert "A strategy must not read `state/bench` itself" in manual
    # the costs are blamed only for what there was to take, as the reading's own words have it
    assert ("If its timing is above nothing and, with what letting positions run added, still comes to more than nothing, the costs take more than "
            "the book made before them") in manual and "if not, there was nothing there for the costs to take" in manual
    # a book the bench could not set against twins has not been shown to have no timing, and the manual does not say it has
    assert "A line that says the book was not set against twins is neither a pass nor a fail: the bench could not read its timing" in manual
    assert "it is the bench that cannot read the timing, not the book that has none" in manual and "has shown no timing" not in manual
    # ... nor that a book which is never out of a pair can be read some other way: that was built and taken out again
    assert "finishes no trade of its own, so it would be killed at its look in any case" in manual and "the bench still cannot read either" in manual
    assert "to the bench a position is left only when nothing of it is held" in manual
    assert "never names what it holds" not in manual and "from one trade to the next" not in manual
    # A strategy that keeps a memory of its own does in a backtest what it cannot do live. The manual says so, and does not
    # promise that the bench sees more of it than it does. (The contract at the top of bot/strategy.py says it too, but that
    # file is the agent's to edit, and a protected test that pinned a sentence there would turn the gate red on a proposal
    # that reworded it: found in review, 2026-10-07)
    assert "A strategy keeps nothing from one hour to the next." in manual
    assert "The bench says so when a strategy's params are not, at the end of a replay, what it was handed. The other two it cannot see." in manual
    # the words in brackets that the manual tells the agent to expect are the four the bench prints, and the remedy it
    # names is asked for only where a stay is the reason
    assert ("say why (it never held a position; the run is too short; the pairs it holds have too short a history; it was never out of some pair "
            "for too long, set against the run or against the history of the pairs it holds)") in manual
    assert "Where the reason is a stay, ask whether it could let go of its positions now and then, all the way to nothing: one that does can be read." in manual
    # the tests are given the time they take as well: a command gets ten minutes unless told otherwise, and they take over half of it
    assert "`python -m pytest tests -q` with the Bash tool's `timeout` set to 1200000" in manual
    assert "`python -m pytest tests -q` (with the Bash tool's `timeout` set to 1200000" in sheet
    # the whole reading is asked for by what is on file, not by which night it is, and once for a test, not once a week
    assert "holds the whole reading of a test in a slot and FINDINGS has no line yet on that test's whole reading, add one, once for each test" in manual
    # a config that could not be read is Fin's to hear of, the champion's as much as a slot's, on a day with no note too
    assert "If the table has a line under `Not read`, for the champion or for a config in a slot, copy the line to the top of the day's note" in manual
    assert "write the note for that alone" in manual and "for the champion or for a config in a slot" in sheet
    # both commands that replay five years are given the time for it, not the bench alone (found in review, 2026-10-07)
    long_one = next(b for b in manual.split(" - ") if "--days 1800 --gate" in b)
    assert "`timeout` set to 1800000" in long_one and "say why in a few words" in manual and "why in a few words" in sheet
    steps = [ln for ln in (REPO / ".github" / "agent_prompt.md").read_text().splitlines() if re.match(r"\d+\. ", ln)]
    free = [ln for ln in steps if ln.split(". ", 1)[1].startswith("If a slot is free")]
    assert len(free) == 1 and command in free[0] and "python -m bot.backtest" in free[0]       # in the step that spends the slot
    fmt = (REPO / "LEDGER_FORMAT.md").read_text()
    assert f"- Bench: the last line of `{command}`" in fmt and "begin this line `not taken:` and say why" in fmt
    state = flat((REPO / "state" / "README.md").read_text())
    assert "bench/" in state and "state/bench" in flat((REPO / "README.md").read_text())
    agent = yaml.safe_load((REPO / ".github" / "workflows" / "agent.yml").read_text())
    run = [s_ for s_ in agent["jobs"]["propose"]["steps"] if s_.get("name") == "Run the agent"][0]
    usual, most = int(run["env"]["BASH_DEFAULT_TIMEOUT_MS"]), int(run["env"]["BASH_MAX_TIMEOUT_MS"])
    limit = agent["jobs"]["propose"]["timeout-minutes"] * 60 * 1000
    # A replay of five years takes longer than the two minutes a command gets unless told otherwise, so the agent may
    # ask for the 30 the manual names. What a command gets without asking stays short, and the most it can ask for
    # well under the job's limit: a command that hangs must not be able to cost the run (found in review, 2026-10-07)
    assert most >= 1_800_000 and 300_000 <= usual <= 600_000 and most * 2 <= limit and limit >= 120 * 60 * 1000 and usual < 1_200_000 <= most


def test_the_agents_workflow_asks_for_the_bench_the_moment_it_has_merged():
    """The bench used to go by the clock alone, at an hour the agent's run could overrun: it then found
    nothing new and the whole reading of a new test waited a day (found in review, 2026-10-07)."""
    agent = yaml.safe_load((REPO / ".github" / "workflows" / "agent.yml").read_text())
    merge = agent["jobs"]["merge"]
    assert merge["permissions"] == {"contents": "write", "pull-requests": "write", "actions": "write"}
    assert all(job.get("permissions", {}).get("actions") != "write" for name, job in agent["jobs"].items() if name != "merge")
    assert agent["permissions"]["actions"] == "read"
    names = [s_["name"] for s_ in merge["steps"]]
    assert names == ["Merge", "Ask for the bench"]                        # after the merge, never before it
    ask = merge["steps"][1]["run"]
    assert 'gh workflow run bench.yml --repo "$GITHUB_REPOSITORY" --ref main' in ask
    assert ask.strip().startswith("if gh workflow run") and "::warning::" in ask and "exit 1" not in ask       # a lost request does not undo a merge
    assert "gh pr merge" in merge["steps"][0]["run"] and "workflow run" not in merge["steps"][0]["run"]
    wf = workflow()
    triggers = wf.get("on", wf.get(True))
    assert "workflow_dispatch" in triggers                                # a merge made by a workflow starts no other, but may ask for one by name
    # the clock is the fallback, and comes after the latest hour an agent run that began at 22:00 UTC can still be merging
    propose, gate = agent["jobs"]["propose"]["timeout-minutes"], yaml.safe_load((REPO / ".github" / "workflows" / "gate.yml").read_text())["jobs"]["gate"]["timeout-minutes"]
    minute, hour = (int(x) for x in triggers["schedule"][0]["cron"].split()[:2])
    assert (agent.get("on", agent.get(True))["schedule"][0]["cron"]) == "0 22 * * *"
    assert ((hour + 24 - 22) % 24) * 60 + minute >= propose + gate + 30


LEDGER_HEAD = "# Ledger\n\n## H1: an old one\n- Status: killed\n\n"
BENCH_LINE = ("Bench: timing +3.0% a year before costs over 1,820 days, which beats 62% of its twins, and a book with no timing does as well 38% "
              "of the time; letting positions run added 0.1% and costs took 4.0% a year, so -0.9% is left (Sharpe -0.10, t -0.2). In sample.")
ENTRY = f"""## H2: a new one
- Date: 2026-10-07
- Hypothesis: something about the market.
- Change: configs/challenger1.yaml runs it.
- Why it should work: a reason, with the cost arithmetic.
- Expected gross bps per round trip: 120, from the size of the move.
- Kill criteria: the standard rule.
- Backtest: total return and the rest.
- Bench: {BENCH_LINE} Not much.
- Status: testing

"""


def ledger_check(tmp_path, entry):
    """A repo with a ledger on main and, on a branch, one slot's config changed and `entry` added;
    then the gate's own check, run as the gate runs it."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"HOME": str(tmp_path), "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})
    me = ("-c", "user.name=somebody", "-c", "user.email=somebody@example.com")
    repo = tmp_path / "repo"
    (repo / "configs").mkdir(parents=True)
    git(tmp_path, "init", "-q", "-b", "main", str(repo), env=env)
    (repo / "LEDGER.md").write_text(LEDGER_HEAD + "## Results\n")
    (repo / "configs" / "challenger1.yaml").write_text("hypothesis: H0\nstrategy: a\nparams: {}\n")
    git(repo, "add", "-A", env=env)
    git(repo, *me, "commit", "-q", "-m", "base", env=env)
    git(repo, "checkout", "-q", "-b", "agent", env=env)
    (repo / "LEDGER.md").write_text(LEDGER_HEAD + entry + "## Results\n")
    (repo / "configs" / "challenger1.yaml").write_text("hypothesis: H2\nstrategy: b\nparams: {}\n")
    git(repo, "add", "-A", env=env)
    git(repo, *me, "commit", "-q", "-m", "H2: a new one", env=env)
    return subprocess.run([sys.executable, str(REPO / "gate" / "check_ledger.py"), "--base", "main", "--head", "HEAD"],
                          cwd=repo, env=env, capture_output=True, text=True)


def test_a_proposal_must_carry_its_bench_line(tmp_path):
    ok = ledger_check(tmp_path / "a", ENTRY)
    assert ok.returncode == 0 and "ledger check passed: new entry H2" in ok.stdout, ok.stdout + ok.stderr
    filled = f"- Bench: {BENCH_LINE} Not much."
    for n, broken in enumerate((ENTRY.replace(filled + "\n", ""), ENTRY.replace(filled, "- Bench: "), ENTRY.replace("- Bench:", "- Bench line:"))):
        r = ledger_check(tmp_path / f"b{n}", broken)
        assert r.returncode == 1 and "ledger entry H2 is missing a filled '- Bench:' line" in r.stdout, (n, r.stdout + r.stderr)
    # It carries the line the bench printed, or says why there is none: `n/a` is neither (it used to pass). A few
    # words of reason are enough, however they are set out, and the bench's own line may be wrapped by hand: the
    # agent cannot read why the gate said no, so every form it would naturally write has to pass (asking for twenty
    # characters of reason turned away `not taken: timed out`; found in review, 2026-10-07)
    wrapped = BENCH_LINE.replace(" its twins, and", " its twins,\n  and").replace("In sample.", "In\n  sample.")
    for n, (text, passes) in enumerate((("n/a", False), ("...", False), ("see the note", False), ("not taken", False), ("not taken:", False),
                                        ("not taken: x", False), ("skill +3.0% a year after costs. In sample.", False),
                                        ("not taken: timed out", True), ("not taken: no time", True), ("Not taken: strategy too heavy", True),
                                        ("`not taken:` it ran out of time", True), ("not taken: KeyError 'vwap'", True),
                                        ("not taken: the reading ran out of its 30 minutes on the first try.", True),
                                        ("Not taken, because the replay failed on a KeyError in my own helper; mended below.", True),
                                        ("+3.0% after costs over 200 days; not set against twins (too short a run). In sample.", True),
                                        (wrapped, True), (BENCH_LINE, True))):
        r = ledger_check(tmp_path / f"f{n}", ENTRY.replace(filled, f"- Bench: {text}"))
        assert (r.returncode == 0) is passes, (text, r.stdout + r.stderr)
        assert passes or "the '- Bench:' line must carry the line the bench printed" in r.stdout, text
    # every other line it asks for is held the same way: a line left blank is not filled by the line under it
    for n, field in enumerate(("Hypothesis", "Kill criteria", "Backtest", "Date")):
        line = next(ln for ln in ENTRY.splitlines() if ln.startswith(f"- {field}:"))
        r = ledger_check(tmp_path / f"c{n}", ENTRY.replace(line, f"- {field}:"))
        assert r.returncode == 1 and f"missing a filled '- {field}:' line" in r.stdout, (field, r.stdout + r.stderr)
    # ... and what is written straight under a field's name is that field's: the figures as a block, the bench's line on
    # the line below (the mend for the blank line turned these away for a day; found in review, 2026-10-07)
    for n, (line, block) in enumerate((("- Backtest: total return and the rest.", "- Backtest:\n  total_return 0.12\n  max_drawdown -0.2\n  skill +3%"),
                                       ("- Backtest: total return and the rest.", "- Backtest:\n- total_return: 0.12\n- max_drawdown: -0.2\n- skill +3%"),
                                       (filled, f"- Bench:\n  {BENCH_LINE}\n  Not much."),
                                       ("- Hypothesis: something about the market.", "- Hypothesis:\nsomething about the market, on a line of its own."))):
        r = ledger_check(tmp_path / f"g{n}", ENTRY.replace(line, block))
        assert r.returncode == 0, (block, r.stdout + r.stderr)
    blank_then_text = ledger_check(tmp_path / "h", ENTRY.replace("- Backtest: total return and the rest.", "- Backtest:\n\n  total_return 0.12"))
    assert blank_then_text.returncode == 1 and "missing a filled '- Backtest:' line" in blank_then_text.stdout      # a blank line ends a field
    # and so does the next field the format names, the one that need not be there included: a list under a field is its own, the field after it is not
    unfilled = ledger_check(tmp_path / "i", ENTRY.replace("- Kill criteria: the standard rule.", "- Kill criteria:\n- Differs from running tests: it is slower."))
    assert unfilled.returncode == 1 and "missing a filled '- Kill criteria:' line" in unfilled.stdout
    low = ledger_check(tmp_path / "d", ENTRY.replace("trip: 120,", "trip: 45,"))
    assert low.returncode == 1 and "expected gross bps per round trip is 45" in low.stdout
    done = ledger_check(tmp_path / "e", ENTRY.replace("- Status: testing", "- Status: promoted"))
    assert done.returncode == 1 and "must have 'Status: testing'" in done.stdout
    # the format the agent copies names every line the check asks for, and the bench's own line is one the check takes
    fmt = (REPO / "LEDGER_FORMAT.md").read_text()
    template = fmt.split("```")[1]
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_ledger", REPO / "gate" / "check_ledger.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert "Bench" in mod.REQUIRED_FIELDS
    for field in mod.REQUIRED_FIELDS:
        assert re.search(rf"^- {re.escape(field)}: \S", template, re.M), field
    assert "a blank line or the next field ends it" in flat(fmt) and "indented or as a list" in flat(fmt)
    assert mod.FIELDS == mod.REQUIRED_FIELDS + ["Differs from running tests"] and all(f"- {field}: " in template for field in mod.FIELDS)
    assert "in a few words" in flat(fmt) and "`not taken: it ran out of its 30 minutes`" in fmt
    for r in [a_reading(), a_reading(quick=True, nearby=[], halves=[]), a_reading(twins=twins_of(0.2, None))] + [no_twins(why) for why in ("idle", "short", "new", "hold", "pairs")]:
        assert mod.bench_line(bench.ledger_line(r)[len("Bench: "):]) and mod.bench_line(bench.ledger_line(r)), bench.ledger_line(r)


def workflow():
    return yaml.safe_load((REPO / ".github" / "workflows" / "bench.yml").read_text(encoding="utf-8"))


def step(wf, name):
    found = [s for s in wf["jobs"]["bench"]["steps"] if s.get("name") == name]
    assert len(found) == 1, name
    return found[0]


def test_the_workflow_commits_only_its_own_folder_and_never_queues_with_the_bot():
    wf = workflow()
    others = [yaml.safe_load(p.read_text(encoding="utf-8")) for p in sorted((REPO / ".github" / "workflows").glob("*.yml")) if p.name != "bench.yml"]
    groups = [str((o.get("concurrency") or {}).get("group")) for o in others if isinstance(o.get("concurrency"), dict)]
    assert wf["concurrency"] == {"group": "bench", "cancel-in-progress": False} and "bench" not in groups
    assert wf["permissions"] == {"contents": "write"} and set(wf["jobs"]) == {"bench"}
    triggers = wf.get("on", wf.get(True))
    assert set(triggers) == {"schedule", "workflow_dispatch"}             # never on a push or a pull request
    assert triggers["schedule"] == [{"cron": "37 1 * * *"}]
    steps = wf["jobs"]["bench"]["steps"]
    assert steps[0]["uses"].startswith("actions/checkout@") and steps[0]["with"]["ref"] == "main"
    assert [s.get("name") for s in steps if s.get("name")] == ["Install", "Read", "Summary", "Commit"]
    assert step(wf, "Install")["run"] == "pip install -q -r requirements.txt"
    read = step(wf, "Read")
    assert read["run"] == "python -m bot.bench --all --save --minutes 240 ${{ inputs.again && '--again' || '' }}"
    assert set(read) == {"name", "id", "run", "timeout-minutes"}
    # the bench stops itself first, then the step would be stopped, then the job: each with time left over for the next
    own = int(re.search(r"--minutes (\d+)", read["run"]).group(1))
    assert 180 <= own <= read["timeout-minutes"] - 20 and read["timeout-minutes"] <= wf["jobs"]["bench"]["timeout-minutes"] - 20
    assert wf["jobs"]["bench"]["timeout-minutes"] <= 350                  # GitHub stops any job at 360
    assert step(wf, "Summary")["if"] == "always()" and "state/bench/README.md" in step(wf, "Summary")["run"]
    commit = step(wf, "Commit")
    assert commit.get("if") == "always()"                                 # what was read is kept even when one config failed
    adds = [ln.strip() for ln in commit["run"].splitlines() if "git add" in ln]
    assert adds == ['if [ -e "$f" ]; then git add -- "$f"; fi'] and "for f in state/bench/README.md state/bench/*.json; do" in commit["run"]
    commits = [ln.strip() for ln in commit["run"].splitlines() if ln.strip().startswith("git commit")]
    assert len(commits) == 1 and commits[0].startswith('git commit -q -m "bench: ') and " -a" not in commits[0] and commits[0].endswith(" -- state/bench")
    assert "git pull --rebase" in commit["run"] and "--force" not in commit["run"] and "-f " not in commit["run"]
    pythons = [str((s.get("with") or {}).get("python-version", "")) for s in steps if str(s.get("uses", "")).startswith("actions/setup-python@")]
    for version in pythons:
        named = re.fullmatch(r"(\d+)\.(\d+)(\.\d+)?", version)
        assert not named or (int(named.group(1)), int(named.group(2))) >= (3, 11), version


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
    (tools / "sleep").write_text(f'#!/bin/sh\necho "$1" >> "{tmp_path}/slept"\n')
    (tools / "sleep").chmod(0o755)
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"HOME": str(home), "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1", "GIT_TERMINAL_PROMPT": "0",
                "PATH": f"{tools}{os.pathsep}{env.get('PATH', '')}"})
    me = ("-c", "user.name=somebody", "-c", "user.email=somebody@example.com")
    origin, seed, work = tmp_path / "origin.git", tmp_path / "seed", tmp_path / "work"
    git(tmp_path, "init", "-q", "--bare", "-b", "main", str(origin), env=env)
    git(tmp_path, "init", "-q", "-b", "main", str(seed), env=env)
    for rel, text in (("README.md", "a repo\n"), ("state/summary.md", "hour 1\n"), ("configs/challenger1.yaml", "a: 1\n")):
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

    def read(n):
        (work / "state" / "bench").mkdir(parents=True, exist_ok=True)
        (work / "state" / "bench" / "H9.json").write_text(f'{{"n": {n}}}\n')
        (work / "state" / "bench" / "README.md").write_text(f"table {n}\n")
        (work / "bot").mkdir(exist_ok=True)
        (work / "bot" / "left_by_the_run.pyc").write_text("what a run leaves beside its readings")
        (work / "scratch.txt").write_text("and a stray file")

    def meanwhile(rel, text, subject):
        """The bot, or anybody, pushes a commit while the bench is at work."""
        git(seed, "pull", "-q", str(origin), "main", env=env)
        (seed / rel).parent.mkdir(parents=True, exist_ok=True)
        (seed / rel).write_text(text)
        git(seed, "add", "-A", env=env)
        git(seed, *me, "commit", "-q", "-m", subject, env=env)
        git(seed, "push", "-q", str(origin), "main", env=env)
    return types.SimpleNamespace(work=work, origin=origin, seed=seed, env=env, me=me, commit_step=commit_step, read=read, meanwhile=meanwhile,
                                 slept=lambda: (tmp_path / "slept").read_text().split() if (tmp_path / "slept").exists() else [])


def test_the_commit_step_itself_commits_the_readings_and_only_those(checkout):
    c = checkout
    r = c.commit_step()                                                    # a run that read nothing and made no folder: green, and nothing committed
    assert r.returncode == 0 and "no readings to commit" in r.stdout and "fatal" not in r.stderr, (r.stdout, r.stderr)
    c.read(1)
    r = c.commit_step()
    assert r.returncode == 0 and "pushed on attempt 1" in r.stdout, (r.stdout, r.stderr)
    subject, author = git(c.origin, "log", "-1", "--format=%s%n%an <%ae>", "main", env=c.env).splitlines()
    assert re.fullmatch(r"bench: \d{4}-\d{2}-\d{2}", subject) and author == "quantloop-bot <quantloop-bot@users.noreply.github.com>"
    assert sorted(git(c.origin, "show", "--name-only", "--format=", "main", env=c.env).split()) == ["state/bench/H9.json", "state/bench/README.md"]
    head = git(c.origin, "rev-parse", "main", env=c.env)
    r = c.commit_step()                                                    # nothing new: green, and nothing committed
    assert r.returncode == 0 and "nothing to commit" in r.stdout and git(c.origin, "rev-parse", "main", env=c.env) == head
    # A file that is no reading, left in the readings' own folder, and a change somebody had staged before the step
    # began: neither goes into the commit (both did; found in review, 2026-10-07)
    c.read(2)
    (c.work / "state" / "bench" / "left_over.tmp").write_text("half a reading")
    (c.work / "README.md").write_text("staged by something earlier in the job\n")
    git(c.work, "add", "README.md", env=c.env)
    r = c.commit_step()
    assert r.returncode == 0 and "pushed on attempt 1" in r.stdout, (r.stdout, r.stderr)
    assert sorted(git(c.origin, "show", "--name-only", "--format=", "main", env=c.env).split()) == ["state/bench/H9.json", "state/bench/README.md"]
    assert git(c.origin, "show", "main:README.md", env=c.env) == "a repo\n" and git(c.origin, "show", "main:state/bench/H9.json", env=c.env) == '{"n": 2}\n'
    assert "left_over.tmp" not in git(c.origin, "ls-tree", "-r", "--name-only", "main", env=c.env)
    # a folder with no reading in it at all (the run made it and wrote nothing): green, nothing committed
    for p in (c.work / "state" / "bench").iterdir():
        p.unlink()
    git(c.work, "checkout", "-q", "--", "state/bench", env=c.env)
    head = git(c.origin, "rev-parse", "main", env=c.env)
    r = c.commit_step()
    assert r.returncode == 0 and "nothing to commit" in r.stdout and git(c.origin, "rev-parse", "main", env=c.env) == head


def test_the_commit_step_lands_on_top_of_whatever_was_pushed_meanwhile(checkout):
    c = checkout
    c.meanwhile("state/summary.md", "hour 2\n", "state: the second hour")
    c.read(2)
    r = c.commit_step()
    assert r.returncode == 0, (r.stdout, r.stderr)
    subjects = git(c.origin, "log", "--format=%s", "main", env=c.env).splitlines()
    assert len(subjects) == 3 and subjects[0].startswith("bench: ") and subjects[1] == "state: the second hour"
    assert git(c.origin, "show", "main:state/summary.md", env=c.env) == "hour 2\n"          # the bot's hour is not undone
    assert git(c.origin, "show", "main:state/bench/H9.json", env=c.env) == '{"n": 2}\n'
    # What else the run left in its checkout must not stand in the way: a tracked file it changed, and a file of its
    # own that somebody has since added upstream. Either used to fail all five tries, and the readings were lost
    # (found in review, 2026-10-07). Neither is committed.
    c.meanwhile("configs/challenger2.yaml", "from upstream\n", "a slot is added")
    c.meanwhile("state/summary.md", "hour 3\n", "state: the third hour")
    c.read(3)
    (c.work / "README.md").write_text("changed by the run\n")
    (c.work / "configs" / "challenger2.yaml").write_text("made by the run\n")
    r = c.commit_step()
    assert r.returncode == 0 and "pushed on attempt 1" in r.stdout, (r.stdout, r.stderr)
    assert git(c.origin, "show", "main:state/bench/H9.json", env=c.env) == '{"n": 3}\n'
    assert git(c.origin, "show", "main:README.md", env=c.env) == "a repo\n"
    assert git(c.origin, "show", "main:configs/challenger2.yaml", env=c.env) == "from upstream\n"
    assert sorted(git(c.origin, "show", "--name-only", "--format=", "main", env=c.env).split()) == ["state/bench/H9.json", "state/bench/README.md"]


def test_the_commit_step_fails_when_the_readings_cannot_be_pushed(checkout):
    c = checkout
    c.read(3)
    git(c.work, "remote", "set-url", "origin", str(c.origin) + ".gone", env=c.env)
    r = c.commit_step()
    assert r.returncode == 1 and "push failed after 5 attempts" in r.stdout
    assert c.slept() == ["20", "40", "60", "80", "100"]


def test_the_commit_step_gives_up_cleanly_when_its_readings_clash_with_what_is_upstream(checkout):
    """Two bench runs never work at once, so this should not happen; if it does, the step fails after its
    five tries and leaves no rebase half done behind it."""
    c = checkout
    c.read(4)
    c.meanwhile("state/bench/H9.json", '{"n": "from another run"}\n', "bench: somebody else's")
    r = c.commit_step()
    assert r.returncode == 1 and "push failed after 5 attempts" in r.stdout, (r.stdout, r.stderr)
    assert not (c.work / ".git" / "rebase-merge").exists() and not (c.work / ".git" / "rebase-apply").exists()
    assert git(c.origin, "show", "main:state/bench/H9.json", env=c.env) == '{"n": "from another run"}\n'      # and nothing was forced
    assert git(c.work, "status", "--porcelain", env=c.env) == ""
