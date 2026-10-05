"""Rule on challenger tests. PROTECTED.

    python -m bot.promote [--now <unix ts>]

Runs every hour after the accounts. The rules are set out for a reader in
PROMOTION.md; this is the code that applies rule 1. It uses only data from
the test window, which the hypothesis could not have been fitted to because
it did not exist yet.

The ordinary rule (`decide`) says a challenger did better than the champion:

  on challenger.compare_on:
      skill    net return minus the equal weight basket held at the
               strategy's usual exposure, its average over the year before
               the test (beta removed, timing at any horizon kept)
      return   raw net return over the window
  it beat the champion by more than min_return_edge
  AND, on skill, its skill is above challenger.min_skill when that is set
      (it beat holding the market at its own exposure, not just a weak champion)
  AND its max drawdown <= max(max_dd_ratio * champion max drawdown, max_dd_floor)
  AND it placed >= min_trades fills

Two things come before it, from Fin's steers of 2026-10-05, for every test:

  it must have finished a trade of its own   it left a position it had bought,
      or one it had chosen to keep (`finished_trades`). A test that only bought
      and held is killed, whatever its numbers: selling at the right time is the
      skill, and a bot that never sells has shown none.
  trading little does not kill by itself     a test that does not pass the rule
      is kept all the same when its trades are of value (`of_value`): it has
      finished a trade, those finished trades made money after costs, and its
      drawdown is inside the guard. Kept is not promoted.

When a test is looked at:

  every hour   the early kills: it has lost more than early_kill_drawdown since
               the test began AND more than the market itself over the same
               days; or its live costs are a fees treadmill. Either ends it.
  day 60       the first look (challenger.window_days)
                 never finished a trade, or the drawdown guard is broken: killed
                 passes the ordinary rule: a test from before ruleset 7 is
                   promoted here (the one look rule it began under). A test
                   that began under ruleset 7 or later is promoted here only if
                   its daily skill t is already challenger.fast_pass_skill_t
                   (the fast pass); otherwise `First look: passed` and
                   challenger.confirm_days more in the same slot
                 does not pass, trades of value: `First look: kept on value`,
                   the same days more (for an old test too)
                 otherwise: killed
  day 120      the verdict on the whole test (`decide_final`)
                 never finished a trade, or the guard is broken: killed
                 passes the ordinary rule with min_trades fills and a daily
                   skill t of at least challenger.min_skill_t: promoted
                 passes it without the t or the fills, or does not pass it and
                   its trades are of value: `unproven` (the slot is freed; the
                   result does not count against the idea's family)
                 otherwise: killed

When the rules compare on skill and the candles for a window are missing,
incomplete, late to begin or stale, no look is taken that hour, and the early
kill on losses waits too whatever the rules compare on; nothing is ever ruled
on raw return because the market data was not there. Nor is anything ruled on a record that cannot be read or has no
equity reading in the window: that is a damaged file, said every hour until
it is mended, and not a strategy with nothing to show. Every verdict on a
test, every first look and the hourly summary carry a confidence figure (see
`confidence`).

When the champion's config changes (a promotion, or a revert by the shadow
guard) the change is written to state/champion/changes.json, every idle slot
is brought into line with the new champion, and a test still running in
another slot carries on with its champion side measured stretch by stretch,
each against the usual exposure of the config that ran it (see `paired_slot`).

Every verdict also records each side's average exposure, skill, the t of its
own daily skill and the t of the daily edge over the champion, so a reader
can tell a real difference from a coin flip.

A test Fin voids (configs/void.yaml, for broken code or data only) is
recorded as `voided` with its numbers so far and frees its slot. If two slots
win in the same hour only the stronger one is promoted; the other is
restarted against the new champion with a fresh window.

Promotion copies the winning slot's config into configs/champion.yaml and
starts the shadow (bot/shadow.py): the deposed config keeps running for one
more window and the promotion is reverted if it beats the new champion by the
ordinary rule. Either way the slot's config is reset to the champion's, its
account is archived and restarted with fresh cash, and LEDGER.md gets the
verdict with the realised gross bps per round trip next to what the ledger
entry predicted, plus what the market did over the window (BTC, an equal
weight basket of all pairs, and the basket's realised vol) so a result can be
read in context. The champion account is never reset, so its equity curve is
the one long record of what this system has actually done.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import config, data, paper, shadow, slot

CHAMPION_HEADER = "# PROTECTED. Written only by bot/promote.py when a challenger wins.\n"


class Unreadable(Exception):
    """A record that is there and cannot be parsed. Not the same as no data: nothing is ruled on it."""


def _read_csv(path) -> pd.DataFrame:
    """A record as a frame; an empty frame when the file is not there. A file
    that is there and cannot be parsed (cut short, zero bytes) raises
    Unreadable: the hour goes on for every other account, and the slot whose
    record it is gets no ruling until it is mended (`main`, `_look_at`)."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        return pd.DataFrame()
    except Exception as e:  # noqa: BLE001
        raise Unreadable(f"{path.parent.name}/{path.name} cannot be read ({type(e).__name__}: {e})") from e


def _need_columns(df: pd.DataFrame, path, names: tuple[str, ...]) -> None:
    """Raise Unreadable when a record that has rows lacks a column it cannot be
    read without. Rows under the wrong header are a damaged file, and reading
    them as "no fills" or "no equity" would rule on the damage."""
    lacking = [c for c in names if c not in df.columns]
    if len(df) and lacking:
        raise Unreadable(f"{path.parent.name}/{path.name} has rows and no {' or '.join(lacking)} column")


def _column(df: pd.DataFrame, name: str, default: float = np.nan) -> pd.Series:
    """A column as numbers (text and blanks become NaN), or `default` when the column is not there."""
    if name in df.columns:
        return pd.to_numeric(df[name], errors="coerce")
    return pd.Series(default, index=df.index, dtype=float)


def _equity_rows(path, start_ts: int, end_ts: int) -> pd.DataFrame:
    """An account's equity rows inside a window. A row whose time or equity is
    blank or not a number is not a reading and is left out: one such cell at
    the end of a window used to make the whole return NaN, and every
    comparison with NaN is false, so a losing test walked through the rule as
    a pass (found in review, 2026-10-05). The cost and exposure columns come
    back as numbers too, with a blank read as zero. A file that has rows and
    no `ts` or `equity` column has lost its header: Unreadable, like a file
    that cannot be parsed, and not the same as an account with no rows yet."""
    eq = _read_csv(path)
    if not len(eq):
        return pd.DataFrame(columns=["ts", "equity", "gross_exposure", "fees_paid", "slippage_paid"])
    _need_columns(eq, path, ("ts", "equity"))
    ts, value = _column(eq, "ts"), _column(eq, "equity")
    ok = np.isfinite(ts) & np.isfinite(value) & (ts >= start_ts) & (ts <= end_ts)
    out = eq[ok].assign(ts=ts[ok].astype("int64"), equity=value[ok])
    for col in ("gross_exposure", "fees_paid", "slippage_paid"):
        out[col] = _column(eq, col, 0.0)[ok].fillna(0.0)
    return out.sort_values("ts", kind="stable")      # the newest reading is the latest in time, not the last line


def record_fault(name: str) -> str | None:
    """What is wrong with an account's record taken as a whole, or None.

    The engine keeps an account's files in step every hour (bot/run.py): the
    account's own file counts every fill it has made and every reading it has
    taken; trades.csv has one row for each fill, every one of them a fill;
    equity.csv has one row for each reading, from the account's first run to
    its last, in time order. A file that has lost rows still parses, and read
    as it stands it is simply a shorter record: a test that had made forty
    fills read as one that had made none and was killed for it, and a
    champion whose equity rows had gone read as never having had a drawdown,
    which tightened the guard on every challenger. A fill whose quantity had
    gone blank was dropped, and a test with twenty finished trades read as
    having finished none (all found in review, 2026-10-05). So before
    anything is read from an account, its files are set against its own
    counts. Where account.json is not there, or does not carry a count,
    there is nothing to set them against and nothing is said.

    What it cannot see: a row whose figures were changed and still read as
    numbers, every cell of it."""
    adir = config.account_dir(name)
    path = adir / "account.json"
    if not path.exists():
        return None
    try:
        st = json.loads(path.read_text())
    except Exception as e:  # noqa: BLE001
        return f"{name}/account.json cannot be read ({type(e).__name__})"
    if not isinstance(st, dict):
        return f"{name}/account.json is not an account record"
    made, runs = _reading(st.get("n_trades")), _reading(st.get("equity_rows"))
    first, last = _reading(st.get("created_at")), _reading(st.get("last_run_ts"))
    tr = _read_csv(adir / "trades.csv")
    if made is not None and len(tr) != int(made):
        return (f"{name}/trades.csv has {_n(len(tr), 'row')} and the account has made {_n(int(made), 'fill')}: "
                f"rows have been lost or added")
    if len(tr):
        _need_columns(tr, adir / "trades.csv", ("ts", "side", "pair", "qty"))
        amount = _column(tr, "qty")
        a_fill = (np.isfinite(_column(tr, "ts")) & tr["side"].isin(["buy", "sell"]) & np.isfinite(amount) & (amount > 0)
                  & tr["pair"].notna() & tr["pair"].astype(str).str.strip().ne(""))
        for col in ("price", "notional"):                   # the engine writes both on every fill
            if col in tr.columns:
                a_fill &= np.isfinite(_column(tr, col)) & (_column(tr, col) > 0)
        odd = int((~a_fill).sum())
        if odd:
            return (f"{name}/trades.csv has {_n(odd, 'row')} that {'is' if odd == 1 else 'are'} not a fill (a time, a "
                    f"pair, buy or sell, and a quantity and a price above zero)")
    eq = _read_csv(adir / "equity.csv")
    if runs is not None:
        try:
            # counted as the engine counted them when it began the count (bot/run.py), so the two cannot differ
            # over what a blank line is
            on_file = paper.rows_in(adir / "equity.csv")
        except Exception as e:  # noqa: BLE001
            raise Unreadable(f"{name}/equity.csv cannot be read ({type(e).__name__}: {e})") from e
        if on_file != int(runs):
            return (f"{name}/equity.csv has {_n(on_file, 'row')} and the account has taken "
                    f"{_n(int(runs), 'reading')}: rows have been lost or added")
    if not len(eq):
        return f"{name}/equity.csv has no rows and the account has run" if last is not None else None
    _need_columns(eq, adir / "equity.csv", ("ts", "equity"))
    ts, value = _column(eq, "ts"), _column(eq, "equity")
    a_reading = np.isfinite(ts) & np.isfinite(value)
    for col in ("gross_exposure", "fees_paid", "slippage_paid"):        # the engine writes each on every row, and
        if col in eq.columns:                                           # the rule reads each: a row cut short has
            a_reading &= np.isfinite(_column(eq, col))                  # them blank ("2595600,101" read as equity 101)
    blank = int((~a_reading).sum())
    if blank:
        return (f"{name}/equity.csv has {_n(blank, 'row')} that {'is' if blank == 1 else 'are'} not a reading (a "
                f"time, an equity, an exposure and costs, each a number)")
    if not ts.is_monotonic_increasing:
        return f"{name}/equity.csv is not in time order"
    if first is not None and int(ts.iloc[0]) != int(first):
        return f"{name}/equity.csv does not begin at the account's first run: rows have been lost from its start"
    if last is not None and int(ts.iloc[-1]) != int(last):
        return f"{name}/equity.csv does not end at the account's last run"
    return None


ADOPTED_AFTER = 86400      # a position held from before a test, left this long into it, is this strategy's own exit
EXIT_SHARE = 0.05          # a position counts as closed when this share of its largest size or less is left
# The engine never sells more than an account holds. Quantities are written to eight decimals, so the file can
# show a sell a hair above what its rows add up to (a position added to and trimmed four hundred times came out
# 1e-7 over in review); anything past this is a sell the file has lost the buys for. The smallest fill the
# engine makes is 50 dollars, about 0.0006 of a bitcoin.
QTY_SLACK = (1e-6, 1e-6)   # (in units of the coin, as a share of the sell)
# What bot.run may put before a fill's reason, in the order it puts them: a replayed hour, then a position
# decided on as if the account were flat (the first hour under a new strategy, or one held over from the last).
REPLAYED = "replayed after a missed run | "
AS_IF_FLAT = ("first hour under a new strategy, decided as if flat | ",
              "held over from the previous strategy, decided as if flat | ")
FORCED_SELL = ("daily halt", "strategy error")     # how the reason itself begins when the risk layer made the sell


def _forced(reason) -> bool:
    """Whether a sell was made by the risk layer and not by the strategy: the
    daily loss halt sells the whole book, and so does a strategy that raises.
    Neither is an exit the strategy chose (in the gate's replay of the last
    year 31 of H4's 101 closed positions and 19 of H2's 146 were halt sells)."""
    r = reason if isinstance(reason, str) else ""
    for lead in (REPLAYED, *AS_IF_FLAT):
        if r.startswith(lead):
            r = r[len(lead):]
    return r.startswith(FORCED_SELL)


def _oversold(held: float, qty: float) -> bool:
    """A sell of more than the file shows the account holding."""
    return qty - held > QTY_SLACK[0] + QTY_SLACK[1] * qty


def finished_trades(tr: pd.DataFrame, start_ts: int = 0, start_prices: dict | None = None,
                    adopted_after: int = ADOPTED_AFTER) -> list[dict]:
    """The positions an account left inside a test, oldest first. Each is
    {"ts": when it was closed, "pair", "pnl": what it made after costs in
    quote currency (None when that cannot be worked out), "chosen": False
    when the daily loss halt or a strategy error closed it}.

    `tr` is the account's fills up to the end of the window, those from before
    the test included. The file begins when the account was last given fresh
    cash, so the earlier fills say what the account held when the test began
    (a slot runs the champion's config while idle, and H4 began holding five
    positions that config had bought).

    By pair, in time order. A position is closed when sells have brought it
    down to EXIT_SHARE of its largest size or less: a trim is not an exit, and
    a position sold in pieces counts once. For a position held when the test
    began, the size at that moment is the one that counts. A close is a
    finished trade of this test when it falls inside the window and the
    strategy bought into the position during the test, or, for a position it
    only kept, when the close comes `adopted_after` seconds or more into the
    test: in the first day that is the unwinding of what the last config
    left, later it is a position this strategy chose to keep and then chose
    to leave. A sell of something the file does not show the account holding
    (rows lost from the file) is read the same way, as leaving a holding from
    before, with no profit figure.

    What a finished trade made: what its sells brought in minus what its buys
    cost, the fee taken off on both sides; slippage is already in the fill
    prices. A position held when the test began is costed at its price then
    (`start_prices`, read from the candles; failing that, the price of its
    first fill in the test), so only what happened during the test counts. A
    crumb left behind is valued at the price of the closing sell. A trade has
    no figure (None) when a number it needs is not in the record, or when one
    of its sells is of more than the file shows the account holding."""
    need = {"ts", "side", "pair", "qty"}
    if not len(tr) or not need.issubset(tr.columns):
        return []
    start_ts = int(start_ts)
    start_prices = start_prices or {}
    tr = tr.assign(ts=_column(tr, "ts"), qty=_column(tr, "qty"), _value=_column(tr, "notional"),
                   _fee=_column(tr, "fee", 0.0).fillna(0.0), _price=_column(tr, "price"),
                   _reason=tr["reason"] if "reason" in tr.columns else "")
    tr = tr[np.isfinite(tr["ts"]) & np.isfinite(tr["qty"]) & (tr["qty"] > 0)]
    out: list[dict] = []
    for pair, fills in tr.sort_values("ts", kind="stable").groupby("pair"):
        held = peak = 0.0          # peak 0: no position open (held may still be the crumb an exit left)
        own = False                # the strategy under test bought into the open position
        inside = False             # the walk has reached the test's start
        cost = proceeds = 0.0      # money into and out of the open position since the test began
        known = True               # False once a figure the profit needs is missing
        for ts, side, qty, value, fee, price, reason in zip(fills["ts"], fills["side"], fills["qty"], fills["_value"],
                                                           fills["_fee"], fills["_price"], fills["_reason"]):
            ts, qty = int(ts), float(qty)
            price = float(price) if np.isfinite(price) and price > 0 else None
            value = float(value) if np.isfinite(value) else (qty * price if price is not None else None)
            unit = price if price is not None else (value / qty if value is not None else None)   # what one unit went for
            if ts >= start_ts and not inside:
                inside = True
                if peak > 0:                         # held from before: its size, and its worth, as the test begins
                    peak = held
                    p0 = _reading(start_prices.get(pair))
                    p0 = p0 if p0 is not None and p0 > 0 else unit
                    known = p0 is not None
                    cost, proceeds = held * (p0 or 0.0), 0.0
            if side == "buy":
                if peak == 0:                        # a new position: its sums start here, a crumb carried in at this price
                    cost, proceeds, known = (held * unit if held > 0 and unit is not None else 0.0), 0.0, True
                held += qty
                peak = max(peak, held)
                own = own or inside
                if inside:
                    known = known and value is not None
                    cost += (value or 0.0) + float(fee)
            elif side == "sell":
                if peak > 0:
                    if _oversold(held, qty):                             # it sells more than the file shows it holding:
                        known = False                                    # rows are missing, so no figure for this one
                    held = max(held - qty, 0.0)
                    if inside:
                        known = known and value is not None
                        proceeds += (value or 0.0) - float(fee)
                    if held <= EXIT_SHARE * peak * (1 + 1e-9):          # "or less", to the last float
                        if own or ts - start_ts >= adopted_after:      # (neither can hold before the test)
                            crumb = held * unit if held > 0 and unit is not None else 0.0
                            out.append({"ts": ts, "pair": pair, "chosen": not _forced(reason),
                                        "pnl": float(proceeds + crumb - cost) if known else None})
                        peak, own = 0.0, False
                else:
                    unrecorded = _oversold(held, qty)                   # more than the crumb the file shows it holding
                    held = max(held - qty, 0.0)
                    if unrecorded and ts - start_ts >= adopted_after:
                        out.append({"ts": ts, "pair": pair, "chosen": not _forced(reason), "pnl": None})
    return sorted(out, key=lambda t: t["ts"])


def _price_at(pair: str, ts: int) -> float | None:
    """A pair's price at a moment, read between the hourly closes either side
    of it; None when there is no close within two hours of it."""
    try:
        df = data.load_all_candles(pair)
        if not len(df):
            return None
        t, c = _closes(df)
        return _start_price(t, c, int(ts))
    except Exception:  # noqa: BLE001
        return None


def window_metrics(name: str, start_ts: int, end_ts: int, start_equity: float | None) -> dict:
    adir = config.account_dir(name)
    eq_path, tr_path = adir / "equity.csv", adir / "trades.csv"
    out = {"return": None, "max_drawdown": None, "trades": 0, "trades_first_hour": 0, "round_trips": 0,
           "forced_exits": 0, "bars": 0,
           "fees": 0.0, "fees_first_hour": 0.0, "gross_pnl": None, "traded_notional": 0.0, "realised_bps": None,
           "avg_exposure": None,
           "skill": None, "trade_profit": None, "trade_wins": 0, "trade_losses": 0, "trade_unknown": 0,
           "edge_t": None, "edge_days": 0, "skill_t": None, "skill_days": 0}
    base = _reading(start_equity)
    base = base if base is not None and base > 0 else None      # a start equity that is not a number is no start equity
    so_far_eq = _equity_rows(eq_path, -10 ** 15, end_ts)
    eq, earlier = so_far_eq[so_far_eq["ts"] >= start_ts], so_far_eq[so_far_eq["ts"] < start_ts]
    if len(eq):
        # Where the return runs from: the start equity on record, which for a test is its equity at the
        # window's first reading (after the fills of that hour); failing that, the first reading itself.
        from_first = base is None or int(eq["ts"].iloc[0]) == int(start_ts)
        base = base if base is not None else float(eq["equity"].iloc[0])
        series = eq["equity"].astype(float)
        out["return"] = float(series.iloc[-1] / base - 1)
        path = pd.concat([pd.Series([base]), series], ignore_index=True)
        out["max_drawdown"] = float((path / path.cummax() - 1).min())
        out["bars"] = int(len(eq))
        paid = eq["fees_paid"] + eq["slippage_paid"]
        # The costs shown, and the cost kill's, are those of every fill in the window. The fills of a test's
        # first hour are made before the window's first reading is written, so the count starts from the
        # reading before that one (from nothing, for an account that began inside the window). It used to
        # start at the first reading: H4, all of whose 10 fills came in its first hour, read "10 fills,
        # costs 0.00" (found in review, 2026-10-05).
        before = float((earlier["fees_paid"] + earlier["slippage_paid"]).iloc[-1]) if len(earlier) else 0.0
        out["fees"] = float(paid.iloc[-1] - before)
        # Gross is net plus costs over the same span as the return. The fills of a test's first hour come
        # before the equity its return runs from, so their costs are in neither; `fees_first_hour` says how
        # much that is. An account whose return runs from before its first reading (the shadow, which
        # starts from cash at a promotion) has every cost in both.
        since = float(paid.iloc[0]) if from_first else before
        out["gross_pnl"] = float(series.iloc[-1] - base) + float(paid.iloc[-1] - since)
        out["fees_first_hour"] = float(since - before)
        # Each row's exposure stands until the next row, so it is weighted by that time. A plain mean of the
        # rows left out whatever was held through hours the bot did not run (found in review, 2026-10-05).
        share = (eq["gross_exposure"].astype(float) / series.where(series > 0)).fillna(0.0).to_numpy()
        held_for = np.diff(np.append(eq["ts"].to_numpy("int64"), max(int(end_ts), int(eq["ts"].iloc[-1])))).clip(min=0)
        out["avg_exposure"] = float(np.average(share, weights=held_for)) if held_for.sum() > 0 else float(share.mean())
    so_far = _read_csv(tr_path)
    _need_columns(so_far, tr_path, ("ts", "side", "pair", "qty"))
    if len(so_far):
        # A fill has a time, a side, a pair and a quantity above zero. The engine writes no other kind of row,
        # and one that is none of these is not counted towards the fills a promotion needs.
        amount = _column(so_far, "qty")
        a_fill = (np.isfinite(_column(so_far, "ts")) & so_far["side"].isin(["buy", "sell"]) & np.isfinite(amount)
                  & (amount > 0) & so_far["pair"].notna() & so_far["pair"].astype(str).str.strip().ne(""))
        so_far = so_far[a_fill & (_column(so_far, "ts") <= end_ts)]
        tr = so_far[_column(so_far, "ts") >= start_ts]
        out["trades"] = int(len(tr))
        out["trades_first_hour"] = int((_column(tr, "ts") == start_ts).sum())     # made in the run that began the test
        out["traded_notional"] = float(_column(tr, "notional", 0.0).fillna(0.0).sum())
        # the earlier fills say what it held at the start; only a challenger slot inherits a book it did not choose
        inherited = so_far[_column(so_far, "ts") < start_ts]
        prices = {p: _price_at(p, start_ts) for p in inherited["pair"].unique()} \
            if len(inherited) and "pair" in inherited.columns else {}
        fin = finished_trades(so_far, start_ts, prices, ADOPTED_AFTER if name in config.challengers() else 0)
        made = [t["pnl"] for t in fin if t["pnl"] is not None]
        out["round_trips"] = sum(1 for t in fin if t["chosen"])
        out["forced_exits"] = sum(1 for t in fin if not t["chosen"])
        out["trade_wins"], out["trade_losses"] = sum(1 for x in made if x > 0), sum(1 for x in made if x <= 0)
        out["trade_unknown"] = len(fin) - len(made)
        if base and made:
            out["trade_profit"] = float(sum(made) / base)
    if out["gross_pnl"] is not None and out["traded_notional"] > 0:
        # one round trip is a buy plus a sell, so half the traded notional
        out["realised_bps"] = out["gross_pnl"] / (out["traded_notional"] / 2) * 1e4
    return out


def add_skill(m: dict, basket_return: float | None, usual_exposure: float | None = None) -> dict:
    """Net return minus a constant position in the equal weight basket at the
    strategy's usual exposure: what it made beyond simply holding that much of
    the market. "Usual" is its average exposure over the year before the test
    began (usual_exposures), fixed before the window opens, so being more or
    less invested than usual during the window counts as skill at any horizon.
    Without it the window's own average exposure stands in, which removes the
    market's direction just as well but also hands the benchmark any timing
    slower than the window: a slow trend follower that sat out a whole falling
    window scores zero for it (in sample its 60 day skill was positive in 25%
    of windows that way and 54% on the usual basis, 2026-09-25)."""
    if m.get("return") is None or basket_return is None or not math.isfinite(float(basket_return)):
        return m
    if usual_exposure is not None and math.isfinite(float(usual_exposure)):
        m["skill_exposure"], m["skill_basis"] = float(usual_exposure), "usual"
    elif m.get("avg_exposure") is not None:
        m["skill_exposure"], m["skill_basis"] = float(m["avg_exposure"]), "window"
    else:
        return m
    skill = float(m["return"] - m["skill_exposure"] * basket_return)
    if math.isfinite(skill):
        m["skill"], m["basket_return"] = skill, float(basket_return)
    return m


def _basket_level(basket_path, times) -> np.ndarray:
    """The basket's level at each of `times`: the close of the last candle that
    had closed by then (the path is indexed by candle open, one hour earlier).
    Before the first candle it is the path's first level, the window's start."""
    closed_at = basket_path.index.to_numpy("int64") + 3600
    vals = basket_path.to_numpy(float)
    pos = np.searchsorted(closed_at, np.asarray(times, dtype="int64"), side="right") - 1
    return np.where(pos >= 0, vals[np.clip(pos, 0, len(vals) - 1)], vals[0])


def add_skill_by_config(m: dict, basket_path, schedule: list[tuple[int, float]], end_ts: int) -> dict:
    """Skill for an account whose config changed inside the window (only the
    champion's can). schedule: (from_ts, usual exposure of the config that ran
    from then), oldest first. The benchmark holds the basket at each config's
    own usual exposure for the stretch that config ran, so a change does not
    alter the benchmark for the days before it, and a new champion that
    usually holds less is not credited with skill for a fall it merely held
    less of (both happened with one exposure for the whole window; found in
    review, 2026-10-05)."""
    if m.get("return") is None or basket_path is None or len(basket_path) < 2 or not schedule:
        return m
    edges = [int(ts) for ts, _ in schedule] + [int(end_ts)]
    level = _basket_level(basket_path, edges)
    bench, weighted = 1.0, 0.0
    for i, (_, e) in enumerate(schedule):
        bench *= 1.0 + float(e) * (level[i + 1] / level[i] - 1.0)
        weighted += float(e) * (edges[i + 1] - edges[i])
    skill = float(m["return"] - (bench - 1.0))
    if not math.isfinite(skill):
        return m
    m["skill"], m["skill_basis"] = skill, "usual by config"
    m["skill_exposure"] = weighted / max(edges[-1] - edges[0], 1)      # time weighted, for the reader
    m["exposure_schedule"] = [(int(ts), float(e)) for ts, e in schedule]
    return m


def _exposure_at(m: dict, times) -> np.ndarray | float | None:
    """An account's benchmark exposure at each of `times`: one number, or the
    config in force half a day before each reading when it changed."""
    sched = m.get("exposure_schedule")
    if not sched:
        return m.get("skill_exposure")
    starts = np.array([ts for ts, _ in sched], dtype="int64")
    pos = np.clip(np.searchsorted(starts, np.asarray(times, dtype="int64") - 43200, side="right") - 1, 0, len(sched) - 1)
    return np.array([e for _, e in sched], dtype=float)[pos]


def design_exposure(cfg: dict, before_ts: int, days: int = 365) -> float | None:
    """Average exposure of a config over the `days` before `before_ts`, from the
    backtest engine on data that ends before the test starts."""
    from . import backtest
    try:
        rcfg = config.risk_cfg()
        candles = {p: df[df["time"] < before_ts].reset_index(drop=True)
                   for p, df in backtest.load_cached_candles(list(rcfg["pairs"])).items()}
        m = backtest.run_backtest(candles, cfg, rcfg, max_days=days)
        return float(m["avg_gross_exposure"])
    except Exception as e:  # noqa: BLE001
        print(f"[promote] usual exposure for {cfg.get('hypothesis')} unavailable ({e}); the window average stands in")
        return None


def usual_exposures(meta: dict, champ_name: str, chal_name: str, start_ts: int) -> tuple[dict, bool]:
    """Each side's usual exposure for the test that started at start_ts,
    computed once (two backtests) and kept in the test's meta. Returns
    (exposures, changed): the caller saves the meta when changed."""
    ue = meta.get("usual_exposure") or {}
    if ue.get("start") == int(start_ts) and champ_name in ue and chal_name in ue:
        return ue, False
    ue = {"start": int(start_ts),
          champ_name: design_exposure(config.account_cfg(champ_name), int(start_ts)),
          chal_name: design_exposure(config.account_cfg(chal_name), int(start_ts))}
    meta["usual_exposure"] = ue
    return ue, True


def _changes_path():
    return config.account_dir(config.CHAMPION) / "changes.json"


def champion_changes() -> list[dict]:
    """Every change of the champion's config, oldest first: when, from which
    hypothesis to which, why (promotion or revert) and the new config's usual
    exposure. Kept in state/champion/changes.json from ruleset 7 on. A row
    without a usable time is left out. Never raises."""
    p = _changes_path()
    try:
        rows = json.loads(p.read_text()) if p.exists() else []
        good = []
        for r in rows if isinstance(rows, list) else []:
            ts = r.get("ts") if isinstance(r, dict) else None
            if isinstance(ts, (int, float)) and not isinstance(ts, bool) and math.isfinite(ts) and 0 <= ts < 1e11:
                good.append({**r, "ts": int(ts)})
        return sorted(good, key=lambda r: r["ts"])
    except Exception as e:  # noqa: BLE001
        print(f"[promote] state/champion/changes.json is not readable ({e}); treated as empty")
        return []


def record_champion_change(now: int, old_hyp, new_hyp, why: str, exposure: float | None = None) -> None:
    """exposure: the new champion config's usual exposure, when it is known
    (a promoted challenger's from its own test, a restored champion's from the
    shadow guard). Never raises: this runs inside a promotion or a revert."""
    try:
        p = _changes_path()
        if p.exists():
            try:
                json.loads(p.read_text())
            except Exception:  # noqa: BLE001
                # keep what a person may want to mend; do not write over it
                shutil.copy(str(p), str(p.with_name(f"changes.unreadable-{int(now)}.json")))
        ok = exposure is not None and not isinstance(exposure, bool) and math.isfinite(float(exposure))
        rows = champion_changes() + [{"ts": int(now), "from": old_hyp, "to": new_hyp, "why": why,
                                      "exposure": float(exposure) if ok else None}]
        p.write_text(json.dumps(rows, indent=2))
    except Exception as e:  # noqa: BLE001
        print(f"[promote] could not record the champion change ({type(e).__name__}: {e})")


def champion_changed_in(start_ts: int, end_ts: int) -> list[dict]:
    """Champion changes strictly inside a window. One at the window's first or
    last moment is not inside it: every hour in between ran one config."""
    return [r for r in champion_changes() if int(start_ts) < int(r["ts"]) < int(end_ts)]


def champion_schedule(first_exposure, start_ts: int, end_ts: int) -> list[tuple[int, float]] | None:
    """The champion side's benchmark exposure through a window that holds a
    change: the starting config's usual exposure, then each new config's from
    its change on. None when any of them is unknown (the caller then falls
    back to the window average and says so)."""
    steps = [(int(start_ts), first_exposure)] + [(r["ts"], r.get("exposure")) for r in champion_changed_in(start_ts, end_ts)]
    if len(steps) < 2:
        return None
    for _, e in steps:
        if e is None or isinstance(e, bool) or not isinstance(e, (int, float)) or not math.isfinite(e):
            return None
    return [(ts, float(e)) for ts, e in steps]


def champion_note(start_ts: int, end_ts: int, by_config: bool | None = None, measured: bool = True) -> str | None:
    """One sentence for the ledger and the summary when a test's champion side
    is not one config from start to end. by_config: whether its skill was in
    fact measured stretch by stretch (the champion's metrics carry an
    exposure_schedule); None when the caller does not know, and then the
    sentence does not say. measured: False when no skill was worked out at
    all this hour (no market data), and then the sentence does not say either."""
    ch = champion_changed_in(start_ts, end_ts)
    if not ch:
        return None
    steps = ", ".join(f"{r.get('to')} from {datetime.fromtimestamp(int(r['ts']), timezone.utc):%Y-%m-%d} "
                      f"({r.get('why')})" for r in ch)
    how = ("" if by_config is None or not measured else
           ", and its skill is measured stretch by stretch, each against the usual exposure of the config that ran it"
           if by_config else
           ", and its skill is measured against its average exposure in the window, because a usual exposure is not "
           "on record for every config")
    return (f"the champion's config changed during this test ({ch[0].get('from')} at the start, then {steps}). The "
            f"champion side is that account's own record across them{how}")


def sync_idle_slots(old_signature: str) -> list[str]:
    """An idle slot mirrors the champion. When the champion's config changes,
    every idle slot must follow it, or the next hourly run sees a slot whose
    config differs from the champion's and opens a "test" of the old champion
    in it (found in review, 2026-10-05, before any promotion had happened).
    Only a slot still holding the old champion's config is touched."""
    done = []
    for n in config.challengers():
        try:
            if config.strategy_signature(config.account_cfg(n)) != old_signature:
                continue                              # a config of its own: a test, or a slot already in line
            try:
                testing = slot.load(n).get("status") == "testing"
            except Exception:  # noqa: BLE001
                # Its record cannot be read. A slot whose config is the champion's holds no test, so it follows
                # by its config alone: left behind, it would open a "test" of the old champion once the record
                # was mended (found in review, 2026-10-06).
                testing = False
            if not testing:
                config.write_challenger_from_champion(n)
                done.append(n)
        except Exception as e:  # noqa: BLE001
            print(f"[promote] could not bring idle slot {n} into line with the new champion ({e})")
    if done:
        print(f"[promote] idle slots now mirror the new champion: {', '.join(done)}")
    return done


def paired_slot(name: str, meta: dict, now: int, rules: dict) -> tuple[dict, dict, dict]:
    """paired() for a challenger slot, with its usual exposures (cached in its
    meta). If the champion's config changed inside the window, the champion
    side is benchmarked stretch by stretch (add_skill_by_config), or on its
    window average when a config's usual exposure is not on record."""
    start = int(meta["started_at"])
    ue, changed = usual_exposures(meta, config.CHAMPION, name, start)
    if changed:
        slot.save(name, meta)
    schedule = None
    if champion_changed_in(start, now):
        schedule = champion_schedule(ue.get(config.CHAMPION), start, now)
        ue = {k: v for k, v in ue.items() if k != config.CHAMPION}
    return paired(config.CHAMPION, name, start, now, meta["start_equity"], rules, ue, champ_schedule=schedule)


def _num(d, key: str, default):
    """A number from the rules file, or `default` when the key is missing, blank
    or not a number. These files are edited by hand, and a blank value must not
    stop the hourly run (found in review, 2026-10-05)."""
    try:
        v = d.get(key)
        if v is None or isinstance(v, bool):
            return default
        v = float(v)
        return v if math.isfinite(v) else default
    except (AttributeError, TypeError, ValueError, OverflowError):
        return default


TWO_LOOKS_SINCE = 7              # the ruleset that brought in the two look rule
# Every line the `challenger:` block holds. `slots` is read by bot/config.py for the whole loop, not here.
KNOWN_SETTINGS = ("slots", "window_days", "confirm_days", "min_skill_t", "fast_pass_skill_t", "two_looks_from_ruleset",
                  "confidence", "min_trades", "min_trade_profit", "max_dd_ratio", "max_dd_floor", "compare_on",
                  "min_return_edge", "min_skill", "early_kill_drawdown", "treadmill_kill_multiple",
                  "treadmill_min_days")
GATE_COST_DRAG = 0.15            # backtest_gate.max_cost_drag as configs/risk.yaml documents it
# What stands in when a line is missing or is written in a way that cannot be used. Each is the value
# configs/risk.yaml documents, so neither a slip of the hand nor a lost line ever loosens the rule. (For the
# fast pass what stands in is no fast pass: a fast pass is the one line that makes a promotion easier.)
DEFAULTS = {"window_days": 60.0, "confirm_days": 60.0, "min_skill_t": 1.0, "prior": 0.10, "edge_sharpe": 1.5,
            "min_trades": 30, "max_dd_ratio": 1.5, "max_dd_floor": 0.10, "min_return_edge": 0.0, "min_skill": 0.0,
            "early_kill": 0.15, "treadmill_multiple": 3.0, "treadmill_min_days": 14.0, "min_trade_profit": 0.0,
            "two_from": TWO_LOOKS_SINCE, "fast_pass": None, "compare_on": "skill"}


def rule_settings(rules) -> tuple[dict, list[str]]:
    """Every setting of the challenger rules as a value that can be used, plus
    one sentence for each line that is missing, cannot be used as written, or
    is not a line this code reads. None of those ever stops the hour and none
    loosens the rule: the value documented in configs/risk.yaml stands in,
    and the sentence is printed every hour and shown in the summary until the
    file is mended.

    A line that is not in the file is treated like one that cannot be used.
    It used to mean "this is switched off" for seven of the settings, and so
    a slip in a line's name switched the thing off without a word:
    `two_looks_from_rulset: 7` put a new test back on the one look rule,
    `early_kill: 0.15` left no early kill, `min_skil` dropped the floor under
    skill (found in review twice, 2026-10-05). To switch one of these off on
    purpose, write the word `off`:

      two_looks_from_ruleset   off: no new test gets two looks
      fast_pass_skill_t        off or 0: there is no fast pass
      min_skill_t              off or 0: no t bar at day 120
      min_skill                off: no floor under the challenger's skill
      max_dd_floor             off or 0: the drawdown guard has no floor
      early_kill_drawdown      off or 0: no early kill on losses
      treadmill_kill_multiple  off or 0: no cost kill

    The rest take a number (or, for compare_on, `skill` or `return`):

      window_days, confirm_days   days to the first look and between the looks; above 0
      min_trades          fills the ordinary rule asks for
      max_dd_ratio, min_return_edge   the ordinary rule's numbers
      treadmill_min_days  days before the cost kill is asked
      min_trade_profit    what a test's finished trades must have made, as a
                          share of its starting equity, for it to be of value
      confidence.prior, confidence.edge_sharpe   for the confidence figure"""
    rules = rules if isinstance(rules, dict) else {}
    out: dict = {}
    wrong: list[str] = []
    for key in rules:
        if key not in KNOWN_SETTINGS:
            wrong.append(f"challenger.{key} is not a setting this code reads; nothing uses it")

    def find(key: str):
        src = rules
        for part in key.split("."):
            if not isinstance(src, dict) or part not in src:
                return False, None
            src = src[part]
        return True, src

    def bad(key: str, used: str) -> None:
        there, raw = find(key)
        if not there:
            wrong.append(f"challenger.{key} is not in the file; {used}")
            return
        shown = repr(raw)
        shown = shown if len(shown) <= 40 else shown[:37] + "..."
        wrong.append(f"challenger.{key} is {shown}, which cannot be used; {used}")

    def number(key: str, name: str, ok, say: str, off=None) -> None:
        """out[name] from the line `key`: its number when that can be used,
        `off[0]` when the line says off and this setting can be switched off
        (off is then a one item tuple), and otherwise the documented value,
        with a sentence."""
        there, raw = find(key)
        if there and raw is False and off is not None:
            out[name] = off[0]
            return
        src = rules if "." not in key else rules.get(key.split(".")[0])
        v = _num(src, key.split(".")[-1], None) if there else None
        if v is None or not ok(v):
            out[name] = DEFAULTS[name]
            bad(key, say + (" (to switch it off, write `off`)" if off is not None else ""))
        else:
            out[name] = v

    there, v = find("two_looks_from_ruleset")
    if there and v is False:
        out["two_from"] = None                    # switched off: no new test gets two looks
    else:
        try:
            # left out, blank, not a whole number, or earlier than the ruleset that brought the rule in (which
            # would put the tests from before it onto two looks): none of these can be what was meant
            if v is None or isinstance(v, bool) or float(v) != int(float(v)) or int(float(v)) < TWO_LOOKS_SINCE:
                raise ValueError
            out["two_from"] = int(float(v))
        except (TypeError, ValueError, OverflowError):
            out["two_from"] = TWO_LOOKS_SINCE
            bad("two_looks_from_ruleset", f"ruleset {TWO_LOOKS_SINCE} stands in (to switch the rule off, write `off`)")

    number("window_days", "window_days", lambda v: v > 0, f"{DEFAULTS['window_days']:.0f} days stand in")
    number("confirm_days", "confirm_days", lambda v: v > 0, f"{DEFAULTS['confirm_days']:.0f} days stand in")
    number("min_skill_t", "min_skill_t", lambda v: v >= 0, f"{DEFAULTS['min_skill_t']:.1f} stands in", off=(0.0,))
    number("min_trades", "min_trades", lambda v: v >= 0 and v == int(v), f"{DEFAULTS['min_trades']} stands in")
    out["min_trades"] = int(out["min_trades"])
    number("max_dd_ratio", "max_dd_ratio", lambda v: v >= 0, f"{DEFAULTS['max_dd_ratio']} stands in")
    number("max_dd_floor", "max_dd_floor", lambda v: 0 <= v < 1, f"{DEFAULTS['max_dd_floor']:.0%} stands in", off=(0.0,))
    number("min_return_edge", "min_return_edge", lambda v: v >= 0, f"{DEFAULTS['min_return_edge']:.1%} stands in")
    number("min_skill", "min_skill", lambda v: True, f"a floor of {DEFAULTS['min_skill']:.1%} stands in", off=(None,))
    number("early_kill_drawdown", "early_kill", lambda v: 0 <= v < 1, f"{DEFAULTS['early_kill']:.0%} stands in",
           off=(0.0,))
    number("treadmill_kill_multiple", "treadmill_multiple", lambda v: v >= 0,
           f"{DEFAULTS['treadmill_multiple']:g} stands in", off=(0.0,))
    number("treadmill_min_days", "treadmill_min_days", lambda v: v >= 0,
           f"{DEFAULTS['treadmill_min_days']:.0f} days stand in")
    number("min_trade_profit", "min_trade_profit", lambda v: 0 <= v < 1,
           f"{DEFAULTS['min_trade_profit']:.1%} stands in (finished trades must have made money after costs)")

    there, raw = find("fast_pass_skill_t")
    f = _num(rules, "fast_pass_skill_t", None)
    if there and (raw is False or f == 0):
        out["fast_pass"] = None                   # switched off
    elif f is None or f < 0:
        out["fast_pass"] = None
        bad("fast_pass_skill_t", "there is no fast pass until it is mended (to leave it out on purpose, write `off`)")
    else:
        out["fast_pass"] = f

    there, raw = find("compare_on")
    word = raw.strip().lower() if isinstance(raw, str) else None
    if word in ("skill", "return"):
        out["compare_on"] = word
    else:
        out["compare_on"] = DEFAULTS["compare_on"]
        bad("compare_on", "`skill` stands in (the other value it can take is `return`)")

    conf = rules.get("confidence")
    if not isinstance(conf, dict):
        bad("confidence", f"{DEFAULTS['prior']:.0%} and a Sharpe ratio of {DEFAULTS['edge_sharpe']} stand in")
        out["prior"], out["edge_sharpe"] = DEFAULTS["prior"], DEFAULTS["edge_sharpe"]
    else:
        number("confidence.prior", "prior", lambda v: 0 < v < 1, f"{DEFAULTS['prior']:.0%} stands in")
        number("confidence.edge_sharpe", "edge_sharpe", lambda v: v > 0, f"{DEFAULTS['edge_sharpe']} stands in")
        for key in conf:
            if key not in ("prior", "edge_sharpe"):
                wrong.append(f"challenger.confidence.{key} is not a setting this code reads; nothing uses it")
    return out, wrong


def gate_cost_drag() -> tuple[float | None, str | None]:
    """The gate's cost limit, which the cost kill multiplies (a share of equity
    a year, so above 0 and no more than 1), and a sentence when the line is
    missing or cannot be used: the documented 15% then stands in, where
    before the cost kill was simply off with nothing said."""
    gate = config.risk_cfg().get("backtest_gate")
    there = isinstance(gate, dict) and "max_cost_drag" in gate
    v = _reading(gate.get("max_cost_drag")) if there else None
    if v is not None and 0 < v <= 1:
        return v, None
    shown = f"is {repr(gate.get('max_cost_drag'))[:40]}, which cannot be used" if there else "is not in the file"
    return GATE_COST_DRAG, f"backtest_gate.max_cost_drag {shown}; {GATE_COST_DRAG:.0%} stands in for the cost kill"


def other_notes() -> list[str]:
    """Sentences for lines outside `rule_settings` that the verdict code leans
    on and cannot use as written: the `ruleset:` line, the gate's cost limit,
    and a slot that holds a running test and lies beyond `challenger.slots`
    (it is then neither run nor ruled). Printed and shown like the
    `rule_settings` ones."""
    notes = []
    if config.ruleset_number() is None:
        notes.append(f"ruleset is {config.risk_cfg().get('ruleset')!r}, which cannot be used; a test that starts while "
                     f"it is so is stamped `{config.NO_RULESET}` and is judged as one begun under the newest rules "
                     f"(two looks)")
    note = gate_cost_drag()[1]
    if note:
        notes.append(note)
    try:
        n = config.n_slots()
        for d in sorted(config.STATE.glob("challenger*")):
            k = d.name[len("challenger"):]
            if not (k.isdigit() and int(k) > n and (d / "meta.json").exists()):
                continue
            meta = json.loads((d / "meta.json").read_text())
            if isinstance(meta, dict) and meta.get("status") == "testing":
                notes.append(f"challenger.slots is {n}, and {d.name} holds a running test ({meta.get('hypothesis')}): "
                             f"that slot is neither run nor ruled until slots covers it")
    except Exception:  # noqa: BLE001
        pass
    return notes


MIN_SKILL_T_DAYS = 10     # fewer daily readings than this and a t statistic says nothing worth printing
MIN_DAILY_SD = 1e-9       # a daily spread below this is a made up or frozen series, not a measurement


def _daily(name: str, start_ts: int, end_ts: int, base: float | None) -> pd.DataFrame:
    """Account return by day of the window (days counted from the window
    start), with the time of the reading each day's return ends on (`ts`, the
    account's last row that day). A last day that is less than half over is
    counted with the day before it, so a verdict in the first hour of day 60
    rests on 60 daily readings, not on 60 and a few minutes. A day with no row
    at all (the bot was down) is simply absent: the next row's return then
    covers the whole gap."""
    p = config.account_dir(name) / "equity.csv"
    if not p.exists():
        return pd.DataFrame()
    eq = _equity_rows(p, start_ts, end_ts)
    if not len(eq):
        return pd.DataFrame()
    eq = eq.assign(day=(eq["ts"] - start_ts) // 86400)
    last = int((end_ts - start_ts) // 86400)
    if last > 0 and end_ts - (start_ts + last * 86400) < 43200:
        eq.loc[eq["day"] == last, "day"] = last - 1
    by_day = eq.groupby("day")
    daily = by_day["equity"].last().astype(float)
    prev = daily.shift(1)
    base = _reading(base)
    prev.iloc[0] = base if base is not None and base > 0 else float(eq["equity"].iloc[0])
    return pd.DataFrame({"ret": daily / prev - 1, "ts": by_day["ts"].last().astype("int64")})


def _basket_returns(basket_path, start_ts: int, times: pd.Series) -> pd.Series:
    """The basket's return between an account's own readings: for each day in
    `times` (the time of the account's last row that day), from the reading
    before it (or the window start) to that reading. The account's return and
    the basket's then cover exactly the same span, whatever the bot missed:
    whole days (the first row back carries them all) or the rest of a day it
    stopped in. Two earlier versions did not. Reading the basket per calendar
    day, three missing days in a market up 25% turned a daily skill t of +0.4
    into +1.1. Reading it at each day's end, an outage that began six hours
    into a day in which the market then moved 12% put +6% of false skill on
    that day and -6% on the next, and a t of 1.7 became 0.6 (both found in
    review, 2026-10-05)."""
    level = _basket_level(basket_path, times.to_numpy("int64"))
    prev = np.concatenate([[float(basket_path.iloc[0])], level[:-1]])
    return pd.Series(level / prev - 1, index=times.index).replace([np.inf, -np.inf], np.nan).fillna(0.0)


def _t_stat(d: pd.Series, min_days: int) -> tuple[float | None, int]:
    """Mean over standard error of a daily series, or None when the sample is
    too small, has no spread, or does not come out as a finite number."""
    d = d.replace([np.inf, -np.inf], np.nan).dropna()
    n = int(len(d))
    if n < min_days:
        return None, n
    sd = float(d.std(ddof=1))
    if not math.isfinite(sd) or sd < MIN_DAILY_SD:
        return None, n
    t = float(d.mean() / (sd / math.sqrt(n)))
    return (t if math.isfinite(t) else None), n


def edge_t(champ_name: str, chal_name: str, start_ts: int, end_ts: int, start_equity: dict,
           champ: dict, chal: dict, basket_path, on: str) -> tuple[float | None, int]:
    """t statistic of the daily edge the verdict is decided on, and the number
    of days behind it. Informational: it says how far the edge sits from zero
    in units of its own day to day noise. |t| under about 2 is noise."""
    a = _daily(champ_name, start_ts, end_ts, start_equity.get(champ_name))
    b = _daily(chal_name, start_ts, end_ts, start_equity.get(chal_name))
    if not len(a) or not len(b):
        return None, 0
    d = b["ret"].sub(a["ret"], fill_value=0.0)
    if on == "skill" and basket_path is not None and len(basket_path) > 1:
        times = b["ts"].combine_first(a["ts"]).reindex(d.index).astype("int64")   # both accounts are written together
        bret = _basket_returns(basket_path, start_ts, times)
        e_ch, e_cp = _exposure_at(chal, times), _exposure_at(champ, times)
        e_ch, e_cp = (0.0 if e_ch is None else e_ch), (0.0 if e_cp is None else e_cp)
        d = d - (e_ch - e_cp) * bret
    return _t_stat(d, 3)


def skill_t(name: str, start_ts: int, end_ts: int, base: float | None, m: dict,
            basket_path) -> tuple[float | None, int]:
    """t statistic of one account's own daily skill (its return between one
    day's last reading and the next minus its benchmark exposure times the
    basket's return over the same span) and the days behind it. m: the
    account's metrics, for its benchmark exposure. This is the measure the two
    look rule and the confidence figure rest on: how far the strategy's skill
    stands from zero in units of its own day to day noise. It grows with the
    square root of time, so a real edge with a yearly Sharpe ratio of 2 needs
    about a year to show a t of 2. No reading (None) under MIN_SKILL_T_DAYS
    days or without market data."""
    a = _daily(name, start_ts, end_ts, base)
    if not len(a) or m.get("skill_exposure") is None or basket_path is None or len(basket_path) < 2:
        return None, 0
    d = a["ret"] - _exposure_at(m, a["ts"]) * _basket_returns(basket_path, start_ts, a["ts"])
    return _t_stat(d, MIN_SKILL_T_DAYS)


CONFIDENCE_FLOOR, CONFIDENCE_CAP = 0.01, 0.95


def _reading(t) -> float | None:
    """A figure as a finite number, or None. A comparison with NaN is always
    false, so an unchecked NaN would walk through `t < bar`."""
    try:
        if isinstance(t, bool):
            return None
        t = float(t)
    except (TypeError, ValueError, OverflowError):
        return None
    return t if math.isfinite(t) else None


def _n(count: int, word: str) -> str:
    """"1 fill", "2 fills"."""
    return f"{count} {word}{'' if count == 1 else 's'}"


def _plain(x: float) -> str:
    """A number written out in full, with no exponent and no trailing zeros ("12.5", "0.00001")."""
    text = f"{x:.12f}".rstrip("0").rstrip(".")
    return text if text.strip("-0.") else (f"{x:.3g}" if x else "0")


def _bar(x: float, percent: bool = False) -> str:
    """A bar or a limit from the rules file as it was written: "1.0" and
    "15%", and "1.25" and "12.5%" where that is what the file says (one
    decimal printed 1.25 as "the 1.2 bar")."""
    if percent:
        return f"{x:.0%}" if abs(x * 100 - round(x * 100)) < 1e-9 else f"{_plain(x * 100)}%"
    return f"{x:.1f}" if abs(x * 10 - round(x * 10)) < 1e-9 else _plain(x)


def _apart(*values: float, percent: bool = True) -> list[str]:
    """Figures that are set against each other in one sentence, each with its
    sign, with as few decimals (two to six) as still tell apart any two of
    them that differ: a skill of +0.004% that beat one of +0.001% is not
    printed as "+0.00% beat +0.00%". A zero reads the same whatever its sign."""
    def reads(text: str) -> str:
        return text if any(ch in "123456789" for ch in text) else text.lstrip("+-")
    for places in range(2, 7):
        shown = [f"{v:+.{places}%}" if percent else f"{v:+.{places}f}" for v in values]
        if all(reads(shown[i]) != reads(shown[j]) or values[i] == values[j]
               for i in range(len(values)) for j in range(i)):
            break
    return shown


def _against(value: float, bar: float, percent: bool = True) -> tuple[str, str]:
    """A figure and the bar it is set against (`_apart`; the bar without a
    plus sign): a t of 0.996 under a bar of 1.0 is not printed as "+1.00,
    under the 1.00"."""
    a, b = _apart(value, bar, percent=percent)
    return a, b.lstrip("+")


def confidence(t: float | None, days: int, rules: dict) -> float | None:
    """The chance, between 0 and 1, that a strategy has a real edge, given the t
    of its daily skill over `days` days. It starts from challenger.confidence.prior
    (1 idea in 10 is taken to be real before any evidence) and moves by how much
    more likely that t is from a strategy whose skill has a yearly Sharpe ratio
    of challenger.confidence.edge_sharpe than from one that only breaks even:

        expected t of the real edge   m = edge_sharpe * sqrt(days / 365)
        likelihood ratio              exp(m * (2t - m) / 2)

    Why this measure and not the pass or fail of a rule: in the twin study of
    2026-10-05 (FINDINGS) an edge with a Sharpe ratio of 2 was about 2 times
    as likely as a twin with no skill to pass the one look rule, is about 6
    times as likely to be promoted under the two look rule, and was 0.7 times
    as likely to show a pass under the first that the second did not confirm:
    evidence the wrong way. Both rules lean on this same t, the second over
    more days, so the figure weighs the evidence itself. It moves slowly on
    purpose: t of 1 after 60 days makes 10% into 15%, t of 2 after a year
    makes it 42%, t of 3 after a year 76%.

    It is never certain: the figure is held between CONFIDENCE_FLOOR and
    CONFIDENCE_CAP. The sum knows two stories, a real edge or none, and leaves
    out a third, that the measuring is wrong, which is the likeliest reason for
    a reading that looks certain (several measuring bugs were found in the
    first three weeks, and more in the reviews of this rule)."""
    t = _reading(t)
    if t is None or not days or days <= 0:
        return None
    st = rule_settings(rules)[0]
    prior, edge = st["prior"], st["edge_sharpe"]
    m = edge * math.sqrt(days / 365.0)
    log_lr = max(-50.0, min(50.0, m * (2.0 * t - m) / 2.0))
    odds = prior / (1.0 - prior) * math.exp(log_lr)
    return min(max(odds / (1.0 + odds), CONFIDENCE_FLOOR), CONFIDENCE_CAP)


def confidence_text(d: dict, rules: dict) -> str:
    """One sentence for a reader: the figure, what it started from and what moved it."""
    c = confidence(d.get("skill_t"), int(d.get("skill_days") or 0), rules)
    prior = rule_settings(rules)[0]["prior"]
    if c is None:
        return (f"{prior:.0%}, the starting figure for any idea (no reading of the daily skill t yet: fewer than "
                f"{MIN_SKILL_T_DAYS} days, no market data for the window, or a daily skill that does not vary)")
    shown = (f"{CONFIDENCE_FLOOR:.0%} or less" if c <= CONFIDENCE_FLOOR
             else f"{CONFIDENCE_CAP:.0%}, the most this figure will say," if c >= CONFIDENCE_CAP else f"{c:.0%}")
    return (f"{shown} that this is a real edge (every idea starts at {prior:.0%}; the daily skill t is "
            f"{d['skill_t']:+.2f} over {d['skill_days']} days)")


def standing_tilt(chal: dict) -> str | None:
    """The sentence for a test at least half of whose skill is a standing tilt,
    or None. Skill is measured against the strategy's usual exposure, so a
    test that simply held more of a rising market than it usually does (or
    less of a falling one) shows a little skill every day for one decision it
    never went back to. The tilt's share of the skill is plain arithmetic:
    (its average exposure in the window minus its usual exposure) times the
    basket's return. It is real money and it is one bet, so the confidence
    figure says so and the fast pass is not given on it. It is not used to
    kill or to refuse a promotion at day 120: a trend follower that is in for
    most of a rising window has a tilt too, and it earned it."""
    skill, basket = _reading(chal.get("skill")), _reading(chal.get("basket_return"))
    avg, usual = _reading(chal.get("avg_exposure")), _reading(chal.get("skill_exposure"))
    if None in (skill, basket, avg, usual) or chal.get("skill_basis") != "usual" or skill <= 0:
        return None
    tilt = (avg - usual) * basket
    if tilt < 0.5 * skill:
        return None
    return (f"{tilt:+.2%} of its {skill:+.2%} skill comes from holding {avg:.2f} of the market on average against "
            f"its usual {usual:.2f} while the basket moved {basket:+.2%}: one bet, not one a day")


def confidence_line(chal: dict, rules: dict) -> str:
    """`confidence_text`, with a warning where the figure would mislead. It
    reads the t of the daily skill, which counts a standing tilt as a bet a
    day (a bot that sat fully invested through a 60 day rise read 27%). So
    when the figure reads above its starting point and at least half of the
    skill behind it is that tilt (`standing_tilt`), or the test has finished
    no trade of its own, the sentence says what the figure is resting on."""
    text = confidence_text(chal, rules)
    c = confidence(chal.get("skill_t"), int(chal.get("skill_days") or 0), rules)
    prior = rule_settings(rules)[0]["prior"]
    if c is None or c <= prior or f"{c:.0%}" == f"{prior:.0%}":          # as printed: 10.3% reads "10%", the start
        return text
    if chal.get("trades") and int(chal.get("round_trips") or 0) < 1:
        return (f"{text}. Read it with care: it has finished no trade of its own, so that skill rests on its "
                f"entries alone, a few bets and not one a day")
    tilt = standing_tilt(chal)
    return f"{text}. Read it with care: {tilt}" if tilt else text




JUST_OPENED = "its window opened within the hour and no candle in it is on file yet"


def market_gap(mc: dict, end_ts: int, start_ts: int | None = None) -> str | None:
    """What is wrong with the market data for a window, or None when it can be
    ruled on: every pair asked for has candles in the window, beginning in its
    first day and ending with the candle that closed at the top of this hour.
    A window under an hour old with no candle in it on file yet is not a
    fault and is said in its own words (JUST_OPENED): the first candle that
    closes inside a window is fetched by the next hourly run.

    A basket built from the pairs that happen to have a file is a different
    market: two rising pairs missing out of three turned a kill into a
    promotion. So did the same two with their first two days missing, and so
    did every pair's candles beginning ten days in, which is what a candle
    cache that has been lost and fetched again looks like (the venue serves
    only its newest 720 hours). Candles that stop early read the hours after
    as flat, and an account valued at this hour's quotes was set against a
    basket in which two of three pairs were one failed fetch behind in a
    falling market: a test that had lost less than the market was ended for
    losing more. The hourly run fetches the candle that has just closed, so
    in a healthy hour every pair has it (all found in review, 2026-10-05)."""
    due = int(end_ts) // 3600 * 3600                     # the close the hourly run has just fetched
    if mc.get("unread"):
        return f"the candles for its window could not be read ({mc['unread']})"
    if start_ts is not None and int(end_ts) - int(start_ts) < 3600 and not mc.get("pairs"):
        return JUST_OPENED
    if not mc.get("pairs") or mc.get("basket_return") is None or mc.get("basket_path") is None:
        return "there are no candles for its window"
    missing = list(mc.get("missing") or [])
    if missing:
        return f"there are no candles in its window for {', '.join(missing)}"
    late = list(mc.get("late") or [])
    if late:
        return f"the candles for {', '.join(late)} begin more than a day into its window"
    stale = [p for p, last in (mc.get("last_close") or {}).items() if int(last) < due]
    if stale:
        return (f"the candles for {', '.join(sorted(stale))} stop before the one that closed at the top of this hour")
    return None


def paired(champ_name: str, chal_name: str, start_ts: int, end_ts: int, start_equity: dict,
           rules: dict, usual: dict | None = None, champ_schedule: list | None = None) -> tuple[dict, dict, dict]:
    """Both sides of a paired test over one window, with skill and the edge t.
    usual: each side's usual exposure (usual_exposures); without it skill falls
    back to the window's own average exposure. champ_schedule: the champion
    side's exposure by config when its config changed inside the window. The
    market context comes back with a `gap` sentence when it cannot be ruled
    on; no skill is then worked out at all, so nothing can lean on a basket
    that is not the market."""
    usual = usual or {}
    start_equity = start_equity if isinstance(start_equity, dict) else {}
    for who in (champ_name, chal_name):
        fault = record_fault(who)
        if fault:
            raise Unreadable(fault)
    champ = window_metrics(champ_name, start_ts, end_ts, start_equity.get(champ_name))
    chal = window_metrics(chal_name, start_ts, end_ts, start_equity.get(chal_name))
    try:
        mc = market_context(start_ts, end_ts, list(config.risk_cfg()["pairs"]))
    except Exception as e:  # noqa: BLE001
        mc = {"basket_return": None, "basket_path": None, "pairs": 0, "unread": f"{type(e).__name__}: {e}"[:120]}
    mc["gap"] = market_gap(mc, end_ts, start_ts)
    basket, path = (None, None) if mc["gap"] else (mc.get("basket_return"), mc.get("basket_path"))
    if champ_schedule:
        add_skill_by_config(champ, path, champ_schedule, end_ts)
    if champ.get("skill") is None:
        add_skill(champ, basket, usual.get(champ_name))
    add_skill(chal, basket, usual.get(chal_name))
    on = compare_on(rules, champ, chal)
    chal["edge_t"], chal["edge_days"] = edge_t(champ_name, chal_name, start_ts, end_ts, start_equity,
                                               champ, chal, path, on)
    for name_, m in ((champ_name, champ), (chal_name, chal)):
        m["skill_t"], m["skill_days"] = skill_t(name_, start_ts, end_ts, start_equity.get(name_), m, path)
    return champ, chal, mc


def compare_on(rules: dict, champ: dict, chal: dict) -> str:
    """"skill" when the rules ask for it and both sides have it, else "return"."""
    if rule_settings(rules)[0]["compare_on"] == "skill" and champ.get("skill") is not None \
            and chal.get("skill") is not None:
        return "skill"
    return "return"


def missing_market_data(mc: dict, rules: dict) -> str | None:
    """The rules compare on skill and the market data for the window cannot be
    ruled on: the sentence saying what is wrong with it, or None. No look is
    taken in such an hour and the shadow guard waits too; nothing is ever
    ruled on raw return because the market data was not there."""
    if rule_settings(rules)[0]["compare_on"] != "skill":
        return None
    return mc.get("gap") if isinstance(mc, dict) else "there is no market data for its window"


def no_record(champ: dict, chal: dict, chal_name: str) -> str | None:
    """The sentence for a pair of accounts one of which has no usable equity
    reading in the window, or None. Every account is written every hour, the
    first of a test included, so an empty window is a damaged record and not
    a strategy that did nothing. No look is taken on it and the shadow guard
    waits: a kill for "no data" would be a ruling on the damage."""
    for who, m in ((chal_name, chal), (config.CHAMPION, champ)):
        if _reading(m.get("return")) is None or _reading(m.get("max_drawdown")) is None:
            return f"there is no usable equity record for {who} in its window"
    return None


def drawdown_guard(champ: dict, chal: dict, rules: dict) -> str | None:
    """The sentence for a challenger whose drawdown is past the guard, or None."""
    st = rule_settings(rules)[0]
    champ_dd = abs(_reading(champ.get("max_drawdown")) or 0.0)
    chal_dd = abs(_reading(chal.get("max_drawdown")) or 0.0)
    limit = max(st["max_dd_ratio"] * champ_dd, st["max_dd_floor"])
    if chal_dd <= limit:
        return None
    shown, asked = _against(chal_dd, limit)
    return (f"challenger max drawdown {shown.lstrip('+')} exceeded the limit {asked} "
            f"(the larger of {st['max_dd_ratio']:g}x the champion's {champ_dd:.2%} and the "
            f"{_bar(st['max_dd_floor'], percent=True)} floor)")


def _held_words(m: dict) -> str:
    """What a side's skill was measured against, in words that are true for it."""
    if m.get("skill_basis") == "window":
        return f"its average exposure in the window {m['skill_exposure']:.2f} (no usual exposure is on record)"
    return f"its usual exposure {m['skill_exposure']:.2f}"


def decide(champ: dict, chal: dict, rules: dict, absolute: bool = True) -> tuple[str, str]:
    """The ordinary rule. absolute: also apply challenger.min_skill, the bar
    against simply holding the market at the same exposure. The shadow check
    passes False: reverting asks only whether the deposed config did better
    than its replacement."""
    st = rule_settings(rules)[0]
    if chal.get("return") is None or champ.get("return") is None:
        return "killed", "no equity data for the window"
    for side in (champ, chal):
        for key in ("return", "max_drawdown", "skill"):
            v = side.get(key)
            if v is not None and _reading(v) is None:
                return "killed", (f"a figure in the record is not a number ({key}), so there is no usable data "
                                  f"for the window; nothing is promoted on it")
    if chal["trades"] < st["min_trades"]:
        return "killed", (f"challenger made {_n(chal['trades'], 'fill')}, fewer than the {st['min_trades']} the rule "
                          f"asks for before it rules in a strategy's favour: too few separate bets to tell from luck")
    on = compare_on(rules, champ, chal)
    t_note = (f"; daily edge t {chal['edge_t']:+.2f} over {chal['edge_days']} days"
              if chal.get("edge_t") is not None else "")
    # the two figures the rule sets against each other, with decimals enough to tell them apart
    mine, theirs = _apart(chal[on], champ[on])
    edge = chal[on] - champ[on]
    if on == "skill":
        if edge <= st["min_return_edge"]:
            return "killed", (f"challenger skill {mine} (net {chal['return']:+.2%}, benchmark exposure "
                              f"{chal['skill_exposure']:.2f}) did not beat champion skill {theirs} (net "
                              f"{champ['return']:+.2%}, benchmark exposure {champ['skill_exposure']:.2f}) by more than "
                              f"{st['min_return_edge']:.2%}{t_note}")
        floor = st["min_skill"]
        if absolute and floor is not None and chal["skill"] <= floor:
            mine, theirs, asked = _apart(chal["skill"], champ["skill"], floor)
            return "killed", (f"challenger skill {mine} beat the champion's {theirs} but "
                              f"not the {asked} floor: it did no better than holding the basket at "
                              f"{_held_words(chal)}, so beating the champion shows the champion is weak, not that "
                              f"this has an edge{t_note}")
    elif edge <= st["min_return_edge"]:
        return "killed", (f"challenger net return {mine} did not beat champion "
                          f"{theirs} by more than {st['min_return_edge']:.2%}{t_note}")
    guard = drawdown_guard(champ, chal, rules)
    if guard:
        return "killed", (f"{guard}, although its {'skill' if on == 'skill' else 'net return'} was "
                          f"{_apart(edge, 0.0)[0]} ahead of the champion's")
    champ_dd = abs(champ["max_drawdown"] or 0.0)
    chal_dd = abs(chal["max_drawdown"] or 0.0)
    if on == "skill":
        return "promoted", (f"challenger skill {mine} (net {chal['return']:+.2%}, benchmark exposure "
                            f"{chal['skill_exposure']:.2f}) beat champion skill {theirs} (net "
                            f"{champ['return']:+.2%}, benchmark exposure {champ['skill_exposure']:.2f}) with max drawdown "
                            f"{chal_dd:.2%} vs {champ_dd:.2%}{t_note}")
    return "promoted", (f"challenger net return {mine} beat champion {theirs} "
                        f"with max drawdown {chal_dd:.2%} vs {champ_dd:.2%}{t_note}")


def first_look_of(meta: dict) -> dict | None:
    """The recorded first look of the window the slot is in now, or None. It is
    stamped with the window's start, so a slot whose clock is reset by hand
    (as H2's and H3's were) does not carry a pass over into the new window."""
    fl = meta.get("first_look")
    try:
        if isinstance(fl, dict) and int(fl.get("start")) == int(meta.get("started_at")):
            return fl
    except (TypeError, ValueError):
        pass
    return None


def two_looks(meta: dict, rules: dict) -> bool:
    """Whether a test is judged by the two look rule: it must have begun under
    the ruleset challenger.two_looks_from_ruleset names, or a later one. Tests
    already running when the rule arrived keep the one look they began with
    (Fin, 2026-10-05). A test that has had a first look stays a two look test
    whatever is later removed from the rules file: it gets its second look,
    never a one look promotion. A stamp that is there and cannot be read as a
    number is not an old test's stamp (those have none, or a number below
    seven), so it means two looks."""
    if first_look_of(meta):
        return True
    first = rule_settings(rules)[0]["two_from"]
    if first is None:
        return False
    stamp = meta.get("ruleset")
    if stamp is None:
        return False
    number = _reading(stamp)
    return True if number is None else number >= first


def total_days(meta: dict, rules: dict) -> float:
    """Days from a test's start to its verdict."""
    st = rule_settings(rules)[0]
    return st["window_days"] + (st["confirm_days"] if two_looks(meta, rules) else 0.0)


def too_few_fills(chal: dict, rules: dict) -> str | None:
    """The sentence for a test that has made fewer fills than a promotion needs, or None."""
    need = rule_settings(rules)[0]["min_trades"]
    if chal.get("return") is None or chal["trades"] >= need:
        return None
    return f"it made {_n(chal['trades'], 'fill')}, fewer than the {need} a promotion needs"


def no_trade_of_its_own(chal: dict) -> str | None:
    """The sentence for a test that has not finished a trade of its own, or
    None when it has. Fin, 2026-10-05: selling and taking profit at the right
    time is the skill, so kill bots that are just buying and holding. A test
    that has left no position by its own choice is that bot, whatever its
    numbers: one that only bought, one that sold the book it was handed in its
    first hours and sat out, one that only trimmed, and one whose only exits
    were made for it by the daily loss halt."""
    net = _reading(chal.get("return"))
    if net is None:
        return "there is no usable record of what it made"
    fills = int(chal.get("trades") or 0)
    if fills == 0:
        return "it made no trades to judge"
    if int(chal.get("round_trips") or 0) >= 1:
        return None
    forced = int(chal.get("forced_exits") or 0)
    by_halt = (f" ({_n(forced, 'position')} {'was' if forced == 1 else 'were'} closed for it by the daily loss halt "
               f"or a strategy error, which is not a choice)") if forced else ""
    shown = f"{0.0 if abs(net) < 5e-5 else net:+.2%}"                   # not "-0.00%"
    return (f"it has finished no trade of its own: none of its {_n(fills, 'fill')} closed a position it had bought "
            f"or had chosen to keep{by_halt}, so the {shown} it shows is not from an exit it chose")


def trade_tally(chal: dict) -> str:
    """"its 5 finished trades made +3.98% of its starting equity after costs (5 won, 0 lost)"."""
    wins, losses = int(chal.get("trade_wins") or 0), int(chal.get("trade_losses") or 0)
    unknown, forced = int(chal.get("trade_unknown") or 0), int(chal.get("forced_exits") or 0)
    made = _reading(chal.get("trade_profit"))
    parts = [f"{wins} won", f"{losses} lost"]
    if unknown:
        parts.append(f"{unknown} with no figure in the record")
    if forced:
        parts.append(f"{forced} of them closed by the daily loss halt or a strategy error")
    total = wins + losses + unknown
    if made is None:
        return f"its {_n(total, 'finished trade')} ({', '.join(parts)}) cannot be put a figure on from the record"
    return (f"its {_n(total, 'finished trade')} made {made:+.2%} of its starting equity after costs "
            f"({', '.join(parts)})")


def of_value(champ: dict, chal: dict, rules: dict) -> tuple[bool, str]:
    """Are a test's trades of value? This is the question that keeps a test
    which does not pass the rule (Fin, 2026-10-05: if it trades less but its
    trades are of value, that is a usable skill; if not, kill). A test's trades
    are of value when

      it has finished a trade of its own   (`no_trade_of_its_own`)
      its drawdown is inside the guard
      its finished trades made money       what they brought in after costs,
                                           as a share of its starting equity,
                                           is above challenger.min_trade_profit

    It is a plain reading of the record, not proof of an edge: in the twin
    study a strategy with no skill had finished trades in profit at day 60 in
    about 2 windows in 10 where the market fell and 6 in 10 where it rose.
    Open positions are not in it, so a bot that sits on its losers reads "of
    value" until the guard or an early kill catches it; and a finished trade
    the record cannot put a figure on adds nothing. That is why it only
    keeps a test and never promotes one. Returns (of value, the sentence
    saying why or why not)."""
    blocker = no_trade_of_its_own(chal)
    if blocker:
        return False, blocker
    guard = drawdown_guard(champ, chal, rules)
    if guard:
        return False, guard
    floor = rule_settings(rules)[0]["min_trade_profit"]
    made = _reading(chal.get("trade_profit"))
    tally = trade_tally(chal)
    if made is None:
        return False, tally
    if made <= floor:
        need = "made money" if floor == 0 else f"made more than {_against(made, floor)[1]} of it"
        return False, f"{tally}, and a test that does not pass the rule is kept only when they have {need}"
    return True, tally


def fast_pass(chal: dict, rules: dict) -> str | None:
    """A first look strong enough to stand on its own: the daily skill t over
    the first window is already challenger.fast_pass_skill_t or more, and the
    skill is not mostly a standing tilt (`standing_tilt`: a market that rose
    steadily for 60 days gives anything that held more of it than usual a high
    t for one decision). Returns the sentence for the ledger, or None. Only
    ever asked of a test that has passed its first look, and only at that
    look, never in the days after it: every extra look is another chance for
    luck to pass.

    In the twin study (FINDINGS, 2026-10-05) a twin with no skill was promoted
    this way 9 times in 1,000, a real edge with a yearly Sharpe ratio of 2
    about 12 times in 100 and one of 3 did 23 times in 100: the Sharpe 2 edge
    is about 14 times as likely as a twin to get one, against about 6 times
    for a promotion under the whole rule."""
    bar, t = rule_settings(rules)[0]["fast_pass"], _reading(chal.get("skill_t"))
    if bar is None or t is None or t < bar or standing_tilt(chal):
        return None
    return (f"daily skill t {t:+.2f} over {chal['skill_days']} days, at or above the {_bar(bar)} fast pass bar: "
            f"promoted without waiting for the second look")


def fast_pass_withheld(chal: dict, rules: dict) -> str | None:
    """The sentence for a first look whose t is at the fast pass bar and which
    is not promoted on it, because the skill is mostly a standing tilt."""
    bar, t = rule_settings(rules)[0]["fast_pass"], _reading(chal.get("skill_t"))
    tilt = standing_tilt(chal)
    if bar is None or t is None or t < bar or not tilt:
        return None
    return (f"Its daily skill t is {t:+.2f}, at or above the {_bar(bar)} fast pass bar, but {tilt}, so there is no "
            f"fast pass on it")


def look(champ: dict, chal: dict, rules: dict, fills_apart: bool = False) -> tuple[str, str, str]:
    """What a test shows at a look, before the question of how many looks it
    gets: ("pass" | "value" | "kill", the ordinary rule's sentence, the
    sentence for a kill or for being kept on value).

      kill    it has not finished a trade of its own, whatever its numbers
      pass    it passes the ordinary rule
      value   it does not, and its trades are of value
      kill    otherwise

    fills_apart: ask the ordinary rule as if the test had the fills it needs
    (the second look treats too few fills as its own question)."""
    need = rule_settings(rules)[0]["min_trades"]
    verdict, reason = decide(champ, {**chal, "trades": max(int(chal.get("trades") or 0), need)} if fills_apart
                             else chal, rules)
    blocker = no_trade_of_its_own(chal)
    if blocker:
        also = (f"It clears the rule's numbers all the same ({reason}), and a test that has not left a position "
                f"by its own choice is not promoted on them") if verdict == "promoted" \
            else f"Nor does it pass the rule: {reason}"
        return "kill", reason, f"{blocker}. {also}"
    if verdict == "promoted":
        return "pass", reason, ""
    worth, why = of_value(champ, chal, rules)
    if worth:
        return "value", reason, why
    return "kill", reason, (reason if why in reason else f"{reason}. It is not kept on value either: {why}")


def decide_final(champ: dict, chal: dict, rules: dict) -> tuple[str, str]:
    """The second look, on the whole test.

      killed    it has not finished a trade of its own; or it does not pass
                the ordinary rule and its trades are not of value
      promoted  it passes the ordinary rule, with min_trades fills and a daily
                skill t of at least challenger.min_skill_t (0 means no t bar)
      unproven  it passes the rule's numbers without the fills or the t; or
                it does not pass and its trades are of value"""
    st = rule_settings(rules)[0]
    family = "Unproven, slot freed; this does not count against the idea's family"
    short = too_few_fills(chal, rules)
    # the fill count is its own question here: first, how the rest of the test stands
    outcome, reason, why = look(champ, chal, rules, fills_apart=True)
    if outcome == "kill":
        return "killed", f"second look: {why}"
    if outcome == "value":
        return "unproven", (f"second look: {reason}. Its trades are of value all the same ({why}), so this is not "
                            f"a kill. {family}")
    if short:
        return "unproven", (f"second look: {reason}, but {short}: too few separate bets to tell from luck. {family}")
    bar = st["min_skill_t"]
    t, n = _reading(chal.get("skill_t")), int(chal.get("skill_days") or 0)
    if bar > 0:
        if t is None:
            return "unproven", (f"second look: {reason}, but there is no reading of the daily skill t, so the edge "
                                f"cannot be told from luck. {family}")
        if t < bar:
            shown, asked = _against(t, bar, percent=False)
            return "unproven", (f"second look: {reason}, but the daily skill t is {shown} over {n} days, under the "
                                f"{asked} the rule asks for: its skill is above zero in total and too thin day by "
                                f"day to tell from luck. {family}")
        return "promoted", (f"second look: {reason}; daily skill t {t:+.2f} over {n} days, at or above the "
                            f"{_bar(bar)} bar")
    return "promoted", f"second look: {reason}; no t bar is set"


def other_rule_reading(champ: dict, chal: dict, rules: dict, elapsed_days: float, early: bool = False,
                       gap: str | None = None) -> str:
    """For a test running under the one look rule: what the two look rule makes
    of the same numbers so far. Informational; it decides nothing for that test.
    early: the test was just ended by an early kill, which both rules share.
    gap: what is wrong with the market data this hour, when something is."""
    if early:
        return "the early kill is the same under both rules, so the two look rule would also have ended it here"
    if gap:
        return f"nothing to read this hour ({gap}); neither rule decides without the market data"
    st = rule_settings(rules)[0]
    first = st["window_days"]
    total = first + st["confirm_days"]
    bar = st["min_skill_t"]
    outcome, _, why = look(champ, chal, rules)
    t = _reading(chal.get("skill_t"))
    t_now = "no reading of its daily skill t yet" if t is None else f"its daily skill t is {t:+.2f} so far"
    fast_bar = st["fast_pass"]
    if elapsed_days < first:
        if outcome == "kill":
            return f"on today's numbers it would be killed at day {first:.0f}, the same as under its own rule"
        if outcome == "value":
            return (f"on today's numbers it would be kept at day {first:.0f} on the value of its trades without "
                    f"passing the rule, the same as under its own rule. From there the two rules are one: "
                    f"{total - first:.0f} more days, and a promotion asks for a daily skill t of {_bar(bar)} over all "
                    f"{total:.0f} ({t_now})")
        need = f"{_bar(bar)} by day {total:.0f}"
        if fast_bar is not None:
            need = f"{_bar(fast_bar)} at day {first:.0f} to be promoted there, or {need}"
        return (f"on today's numbers it would pass the first look at day {first:.0f}, where its own rule promotes "
                f"it; {t_now}, and the two look rule would need {need}")
    if outcome == "kill":
        return "the two look rule would also have ended it here, for the same reason"
    if outcome == "value":
        return "the two look rule would also have kept it on the value of its trades for a second look"
    if fast_pass(chal, rules):
        return (f"it passes the first look and {t_now}, at or above the {_bar(fast_bar)} fast pass bar: "
                f"the two look rule would also have promoted it here")
    return (f"it passes the first look, and the two look rule would not promote it yet: it would run "
            f"{total - first:.0f} more days and need a daily skill t of {_bar(bar)} or more over all {total:.0f} "
            f"({t_now})")


def early_kill(chal: dict, rules: dict, elapsed_days: float | None = None,
               start_equity: float | None = None, gate_cost_drag: float | None = None,
               basket_return: float | None = None) -> str | None:
    """The sentence for a test that is ended before its look, or None.

    Losses: it has lost more than challenger.early_kill_drawdown since the
    test began AND more than the market itself over the same days
    (`basket_return`, the equal weight basket held from the test's start).
    Until ruleset 7 this was 15% under its high inside the window, whatever
    the market had done. Replayed on 687 days in which the basket fell by a
    third, that ended 55 of 100 strategies with no skill and 40 of 100 with a
    Sharpe 2 edge before day 60: anything that held coins hit it. Read this
    way it ends 25 and 5 inside 120 days (FINDINGS, 2026-10-05). Without a
    figure for the market there is no early kill on losses that hour.

    Costs: live costs past treadmill_kill_multiple times the gate's cost drag
    limit after treadmill_min_days. A fees treadmill is dead on arrival and
    there is no point paying for it for 60 days."""
    st = rule_settings(rules)[0]
    limit = st["early_kill"]
    net, basket = _reading(chal.get("return")), _reading(basket_return)
    if limit and net is not None and basket is not None and net < -limit and net < basket:
        for places in range(2, 7):                 # as few decimals as tell the loss from the limit and the market's
            lost = f"{-net:.{places}%}"
            if lost != f"{limit:.{places}%}" and lost != f"{-basket:.{places}%}":
                break
        return (f"challenger has lost {lost} since its test began, past the {_bar(limit, percent=True)} early kill "
                f"limit, and more than the market itself over the same days (the basket "
                f"{'made' if basket >= 0 else 'lost'} {abs(basket):.{places}%}); no need to wait for the window to end")
    multiple, min_days = st["treadmill_multiple"], st["treadmill_min_days"]
    drag_limit, equity0 = _reading(gate_cost_drag), _reading(start_equity)
    if multiple and drag_limit and elapsed_days and equity0 and equity0 > 0 and elapsed_days >= min_days:
        drag = float(_reading(chal.get("fees")) or 0.0) / equity0 / (elapsed_days / 365)
        if drag > multiple * drag_limit:
            return (f"costs of {chal['fees']:.0f} in {elapsed_days:.1f} days are {drag:.0%} of starting equity a "
                    f"year, more than {multiple:g} times the gate's {drag_limit:.0%} limit: a fees "
                    f"treadmill, killed without waiting for the window to end")
    return None


def early_kill_waits(chal: dict, rules: dict, basket_return: float | None) -> bool:
    """A test is past the loss limit and there is no figure for the market to
    set it against this hour, so the early kill on losses cannot be asked."""
    limit, net = rule_settings(rules)[0]["early_kill"], _reading(chal.get("return"))
    return bool(limit) and net is not None and net < -limit and _reading(basket_return) is None


def _closes(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """A pair's usable closes in time order: (the moment each price is for, the
    price). A candle is stamped with its open, so its close is an hour later.
    A blank or text cell is not a price."""
    close, opened = _column(df, "close"), _column(df, "time")
    ok = np.isfinite(close) & (close > 0) & np.isfinite(opened)
    t = opened[ok].astype("int64").to_numpy() + 3600
    c = close[ok].astype(float).to_numpy()
    order = np.argsort(t, kind="stable")
    return t[order], c[order]


def _start_price(t: np.ndarray, c: np.ndarray, start_ts: int) -> float | None:
    """The price at start_ts, read between the two closes either side of it in
    proportion to the time, when they are no more than two hours apart. With
    nothing close after it, the last close before it stands if it is under two
    hours old. Otherwise None: no reading across a hole in the candles."""
    before, after = np.flatnonzero(t <= start_ts), np.flatnonzero(t > start_ts)
    if len(before) and len(after) and t[after[0]] - t[before[-1]] <= 2 * 3600:
        a, b = int(before[-1]), int(after[0])
        w = (start_ts - t[a]) / (t[b] - t[a])
        return float(c[a] + w * (c[b] - c[a]))
    if len(before) and start_ts - t[before[-1]] <= 2 * 3600:
        return float(c[int(before[-1])])
    return None


def _window_closes(df: pd.DataFrame, start_ts: int, end_ts: int) -> pd.Series | None:
    """One pair's closes over a window, indexed by candle open time, starting
    from its price at start_ts and using only candles that had closed by
    end_ts. The starting price is read between the two closes either side of
    start_ts, in proportion to the time. (Until 2026-10-05 the window began at
    the first close an hour or less AFTER start_ts and so left out whatever
    the market did in between, for the whole length of the test: H4's test
    began 21 minutes into an hour in which the basket rose 1.4%, and its
    benchmark read about 0.9 of a point too low from then on.) None when
    there are not two usable prices."""
    t, c = _closes(df)
    inside = (t > start_ts) & (t <= end_ts)
    if not inside.any():
        return None
    p0 = _start_price(t, c, int(start_ts))
    if p0 is None:
        return pd.Series(c[inside], index=t[inside] - 3600) if inside.sum() >= 2 else None    # the pair starts later
    return pd.Series(np.concatenate([[p0], c[inside]]), index=np.concatenate([[int(start_ts) - 3600], t[inside] - 3600]))


def market_context(start_ts: int, end_ts: int, pairs: list[str]) -> dict:
    """What the market did over a window: BTC return, equal weight basket
    return, basket realised vol (annualised from hourly basket returns). Also
    which of the pairs asked for have no candles in the window (`missing`),
    which have their first price more than a day after the window began
    (`late`), and when each pair's newest close in the window was
    (`last_close`), for `market_gap`. A pair whose candles begin more than a
    day after the others' is left out of the basket (in a long history that
    is a pair that did not exist yet)."""
    out = {"btc_return": None, "basket_return": None, "basket_vol": None, "basket_max_dd": None,
           "pairs": 0, "basket_path": None, "missing": list(pairs), "late": [], "last_close": {}}
    series = {}
    for p in pairs:
        df = data.load_all_candles(p)
        if not len(df):
            continue
        sr = _window_closes(df, start_ts, end_ts)
        if sr is None:
            continue
        series[p] = sr
    out["missing"] = [p for p in pairs if p not in series]          # asked for, and no candles in the window
    out["last_close"] = {p: int(sr.index[-1]) + 3600 for p, sr in series.items()}
    if not series:
        return out
    # A pair that did not exist when the window opened (XRP before July 2023 in
    # the long history) is not in the basket for that window. It used to be
    # carried as flat from the window's start, which shrank the basket's move
    # by its share.
    # For a ruling, a pair whose first price in the window comes more than a day after the window began has
    # a hole where the test started (`market_gap`): "after the window began", not "after the other pairs",
    # which missed the case of every pair beginning late together.
    out["late"] = [p for p, sr in series.items() if int(sr.index[0]) + 3600 > int(start_ts) + 24 * 3600]
    opened = min(int(sr.index[0]) for sr in series.values())
    series = {p: sr for p, sr in series.items() if int(sr.index[0]) <= opened + 24 * 3600}
    rets = {p: float(sr.iloc[-1] / sr.iloc[0] - 1) for p, sr in series.items()}
    out["pairs"] = len(rets)
    out["basket_return"] = float(np.mean(list(rets.values())))
    if "BTC" in rets:
        out["btc_return"] = rets["BTC"]
    frame = pd.DataFrame(series).sort_index().ffill().bfill()
    hourly = frame.pct_change().mean(axis=1).dropna()
    if len(hourly) > 2:
        out["basket_vol"] = float(hourly.std() * math.sqrt(24 * 365))
    path = (frame / frame.iloc[0]).mean(axis=1)          # equal weight buy and hold, rebalanced never
    out["basket_max_dd"] = float((path / path.cummax() - 1).min())
    out["basket_path"] = path
    return out


def format_market(mc: dict) -> str:
    if not mc.get("pairs"):
        return "no candle data for the window"
    parts = []
    if mc["btc_return"] is not None:
        parts.append(f"BTC {mc['btc_return']:+.2%}")
    parts.append(f"equal weight basket of {_n(mc['pairs'], 'pair')} {mc['basket_return']:+.2%}")
    if mc.get("basket_max_dd") is not None:
        parts.append(f"basket max drawdown {mc['basket_max_dd']:.0%}")
    if mc["basket_vol"] is not None:
        parts.append(f"basket realised vol {mc['basket_vol']:.0%} annualised")
    return ", ".join(parts)


def expected_bps(hyp: str) -> float | None:
    if not config.LEDGER.exists():
        return None
    text = config.LEDGER.read_text()
    # inside this hypothesis's own entry only (the same guard as the status flip in update_ledger)
    m = re.search(rf"^## {re.escape(hyp)}\b(?:(?!\n## ).)*?\n- Expected gross bps per round trip:\s*([0-9.]+)",
                  text, re.S | re.M)
    return float(m.group(1)) if m else None


def _fmt(d: dict, expected: float | None = None) -> str:
    if d["return"] is None:
        return "no data"
    gross = "n/a" if d.get("gross_pnl") is None else f"{d['gross_pnl']:.2f}"
    trips = ""
    if d.get("round_trips") is not None:
        closed = int(d.get("round_trips") or 0) + int(d.get("forced_exits") or 0)
        trips = f" ({_n(closed, 'finished trade')}"
        if d.get("forced_exits"):
            trips += f", {d['forced_exits']} of them closed by the daily loss halt or a strategy error"
        trips += ")"
    costs = f"costs {d['fees']:.2f}"
    first_hour = _reading(d.get("fees_first_hour")) or 0.0
    if first_hour >= 0.005:
        costs += (f" ({first_hour:.2f} of that on fills in the hour the test began, which the return and gross pnl "
                  f"here do not include: both run from the equity after them)")
    s = (f"return {d['return']:+.2%}, max DD {d['max_drawdown']:.2%}, {_n(d['trades'], 'fill')}{trips}, "
         f"{costs}, gross pnl {gross}")
    if d["realised_bps"] is not None:
        s += f", realised gross bps per round trip {d['realised_bps']:.0f}"
        if expected is not None:
            s += f" (ledger expected {expected:.0f})"
    if _reading(d.get("trade_profit")) is not None:
        s += (f", finished trades made {d['trade_profit']:+.2%} of starting equity after costs "
              f"({d.get('trade_wins', 0)} won, {d.get('trade_losses', 0)} lost)")
    if d.get("avg_exposure") is not None:
        s += f", average exposure {d['avg_exposure']:.2f}"
    if d.get("skill") is not None and d.get("exposure_schedule"):
        s += (f", skill {d['skill']:+.2%} against the basket at each config's usual exposure "
              f"({' then '.join(f'{e:.2f}' for _, e in d['exposure_schedule'])})")
    elif d.get("skill") is not None:
        s += (f", skill {d['skill']:+.2%} against the basket at its {d.get('skill_basis', 'window')} exposure "
              f"{d['skill_exposure']:.2f}")
    if d.get("skill_t") is not None:
        s += f", daily skill t {d['skill_t']:+.2f} over {d['skill_days']} days"
    if d.get("edge_t") is not None:
        s += f", daily edge t over the champion {d['edge_t']:+.2f} over {d['edge_days']} days"
    return s


def _ruleset_note(slot_name: str, when: str = "at the verdict") -> str:
    """Whether the protected rules changed while this test ran. A prospective
    test is only as clean as the rules it ran under were stable. when: what
    this block is ("at the verdict", or "at this look" for a first look).
    The stamp and the line are compared as numbers: `ruleset: '7'` in quotes
    is ruleset 7, and a test stamped 7 under it did not see the rules change."""
    now_rs = config.ruleset_number()
    if now_rs is None:
        return "the ruleset line in configs/risk.yaml cannot be read, so the rules this ran under are not on record"
    try:
        meta = shadow.load() if slot_name == "shadow" else slot.load(slot_name)
        if not isinstance(meta, dict):
            raise ValueError("not a record")
    except Exception:  # noqa: BLE001
        return (f"ruleset {now_rs} {when}; the test's own record could not be read, so the ruleset it began under "
                f"is not on record")
    start_rs = meta.get("ruleset")
    if start_rs is None:
        return (f"ruleset {now_rs} {when}; the test began before rulesets were stamped (2026-10-04), "
                f"so protected rules changed during it (see the ruleset list in configs/risk.yaml)")
    began = _reading(start_rs)
    if began is None:
        return f"the ruleset line could not be read when the test began; ruleset {now_rs} {when}"
    began = int(began) if began == int(began) else began
    if began == now_rs:
        return f"ruleset {now_rs} throughout" if when == "at the verdict" else f"ruleset {now_rs} so far"
    return (f"ruleset {began} at the start, {now_rs} {when}: protected rules changed during the "
            f"window (see the ruleset list in configs/risk.yaml)")


def update_ledger(hyp: str, verdict: str, reason: str, champ: dict, chal: dict,
                  start_ts: int, end_ts: int, slot_name: str, labels: tuple[str, str] = ("Champion", "Challenger"),
                  status_from: str = "testing", status_to: str | None = None,
                  heading: str = "Result", extra: list[str] | None = None) -> None:
    path = config.LEDGER
    text = path.read_text() if path.exists() else "# Ledger\n"
    status_to = verdict if status_to is None else status_to
    if verdict != "restarted" and status_to:
        # Stay inside this hypothesis's own entry: without the look ahead a missing
        # Status line let the match run on into the next entry and flip that one.
        pattern = re.compile(rf"(^## {re.escape(hyp)}\b(?:(?!\n## ).)*?\n- Status: ){status_from}", re.S | re.M)
        text, n = pattern.subn(rf"\g<1>{status_to}", text, count=1)
        if n == 0:
            print(f"[promote] warning: no 'Status: {status_from}' line found for {hyp} in LEDGER.md")
    try:
        market = format_market(market_context(start_ts, end_ts, list(config.risk_cfg()["pairs"])))
    except Exception as e:  # noqa: BLE001
        market = f"unavailable ({e})"
    block = (
        f"\n### {heading} {hyp}: {verdict}\n"
        f"- Slot: {slot_name}\n"
        f"- Window: {datetime.fromtimestamp(start_ts, timezone.utc):%Y-%m-%d} to "
        f"{datetime.fromtimestamp(end_ts, timezone.utc):%Y-%m-%d} ({(end_ts - start_ts) / 86400:.1f} days, prospective)\n"
        f"- Market: {market}\n"
        f"- Rules: {_ruleset_note(slot_name, 'at this look' if heading == 'First look' else 'at the verdict')}\n"
        f"- {labels[0]}: {_fmt(champ)}\n"
        f"- {labels[1]}: {_fmt(chal, expected_bps(hyp))}\n"
        f"- Rule: {reason}\n"
        + "".join(f"- {line}\n" for line in (extra or []))
    )
    if slot_name != config.SHADOW:
        try:
            changed = champion_note(start_ts, end_ts, bool(champ.get("exposure_schedule")),
                                    measured=champ.get("skill") is not None)
        except Exception:  # noqa: BLE001
            changed = None
        if changed:
            block += f"- Champion change: {changed}\n"
    if "\n## Results" not in text:
        text = text.rstrip("\n") + "\n\n## Results\n"
    text = text.rstrip("\n") + "\n" + block
    path.write_text(text)


def archive_slot(name: str, hyp: str) -> None:
    adir = config.account_dir(name)
    dest = config.ARCHIVE / f"{hyp}_{name}_{datetime.now(timezone.utc):%Y%m%d%H%M}"
    dest.mkdir(parents=True, exist_ok=True)
    for fname in ("account.json", "decisions.csv", "trades.csv", "equity.csv"):
        src = adir / fname
        if src.exists():
            shutil.move(str(src), str(dest / fname))


def note_superseded(new_hyp: str, now: int) -> None:
    """A promotion during another promotion's guard window drops that guard: the
    shadow account is handed to the newly deposed champion. Say so in the
    ledger, with the guard's numbers so far, so the earlier promotion is not
    left looking confirmed. It was neither confirmed nor reverted. Never raises:
    this runs inside a promotion."""
    try:
        meta = shadow.load()
        if meta.get("status") != "active":
            return
        rules = config.risk_cfg()["challenger"]
        start = int(meta["started_at"])
        # usual exposures only if the guard already worked them out: two year long
        # backtests are too much to spend on a note in the middle of a promotion
        ue = meta.get("usual_exposure") or {}
        ue = ue if ue.get("start") == start else {}
        reason = (f"{new_hyp} was promoted on day {(now - start) / 86400:.1f} of the "
                  f"{rule_settings(rules)[0]['window_days']:.0f} "
                  f"day guard on this promotion, so the guard ended early: the deposed {meta['hypothesis']} was dropped "
                  f"as the shadow and the guard now watches {new_hyp}. This promotion was neither confirmed nor reverted")
        try:
            champ, shad, _ = paired(config.CHAMPION, config.SHADOW, start, now, meta.get("start_equity"), rules, ue)
        except Exception as e:  # noqa: BLE001
            # The block is what keeps the earlier promotion from looking confirmed, so it is written without
            # the guard's numbers when they cannot be read (it used to be left out; found in review, 2026-10-05).
            champ = shad = {"return": None}
            reason += f". The guard's numbers so far could not be read ({type(e).__name__}: {e})"
        print(f"[promote] {meta['replaced_by']}: guard superseded — {reason}")
        update_ledger(meta["replaced_by"], "superseded", reason, champ, shad, start, now, "shadow",
                      labels=("Promoted champion", "Deposed config (shadow)"), status_to="")
    except Exception as e:  # noqa: BLE001
        print(f"[promote] could not record the superseded guard ({type(e).__name__}: {e})")


def apply(verdict: str, hyp: str, name: str, now: int | None = None, equities: dict[str, float] | None = None) -> None:
    if verdict == "promoted":
        now = now or int(time.time())
        note_superseded(hyp, now)
        deposed = config.account_cfg(config.CHAMPION)
        chal = config.account_cfg(name)
        config.dump_yaml(config.CONFIGS / "champion.yaml",
                         {"hypothesis": chal["hypothesis"], "strategy": chal["strategy"], "params": chal["params"]},
                         CHAMPION_HEADER)
        rcfg = config.risk_cfg()
        equities = equities or {}
        shadow.start(deposed, hyp, now,
                     equities.get(config.CHAMPION, rcfg["initial_cash"]), rcfg["initial_cash"])
        usual = (slot.load(name).get("usual_exposure") or {}).get(name)
        record_champion_change(now, deposed.get("hypothesis"), chal.get("hypothesis"), "promotion", usual)
        sync_idle_slots(config.strategy_signature(deposed))
    config.write_challenger_from_champion(name)
    archive_slot(name, hyp)
    slot.reset(name)


VOID_HEADER = (
    "# PROTECTED. Fin ends a running test here when its code or data is found to be broken.\n"
    "# Never because a test is losing: that is what the window and the kill rules are for.\n"
    "# bot/promote.py acts on each request at the next hourly run, writes the numbers so far to\n"
    "# the ledger as `voided` (not evidence about the idea), frees the slot, and empties this list.\n"
    "#\n"
    "# requests:\n"
    "#   - slot: challenger3\n"
    "#     hypothesis: H3\n"
    "#     reason: one sentence on the fault, written before looking at the profit and loss\n"
)


def _void_one(req, now: int, rules: dict) -> str | None:
    """Act on one request. Returns the hypothesis voided, or None when the request is dropped."""
    if not isinstance(req, dict):
        print(f"[promote] void request {req!r} is not a slot, hypothesis and reason; dropped")
        return None
    name, hyp = str(req.get("slot") or ""), str(req.get("hypothesis") or "")
    why = str(req.get("reason") or "").strip()
    if name not in config.challengers():
        print(f"[promote] void request for unknown slot {name!r}; dropped")
        return None
    try:
        meta = slot.load(name)
        if not isinstance(meta, dict):
            raise ValueError("it is not a slot record")
    except Exception as e:  # noqa: BLE001
        # The slot's own record cannot be read, which is a state a void is for (the request used to be dropped
        # and the test kept its slot; found in review, 2026-10-06). What runs there is read from its config
        # instead: a slot whose config is the champion's holds no test.
        try:
            running = config.account_cfg(name).get("hypothesis") if slot.configs_differ(name) else None
        except Exception:  # noqa: BLE001
            running = None
        if running != hyp:
            print(f"[promote] void request {hyp} in {name}: its slot record could not be read ({type(e).__name__}) and "
                  f"its config {'tests ' + str(running) if running else 'is the champion config'}; dropped")
            return None
        meta = {"status": "testing", "hypothesis": hyp, "unread": f"{type(e).__name__}: {e}"}
    if meta.get("status") != "testing" or meta.get("hypothesis") != hyp:
        print(f"[promote] void request {hyp} in {name} does not match the running test "
              f"({meta.get('hypothesis')}, {meta.get('status')}); dropped")
        return None
    reason = f"voided by Fin, not a verdict on the idea: {why or 'no reason given'}"
    try:
        if meta.get("unread"):
            raise Unreadable(f"{name}/meta.json cannot be read ({meta['unread']})")
        champ, chal, _ = paired_slot(name, meta, now, rules)
    except Exception as e:  # noqa: BLE001
        # A record that cannot be read is the very thing a void is for: no look, early kill or void could end
        # such a test before (found in review, 2026-10-05). It is voided without its numbers.
        champ = chal = {"return": None}
        reason += f". Its numbers so far could not be read ({type(e).__name__}: {e})"
    print(f"[promote] {name}: {hyp}: voided — {why}")
    began = _reading(meta.get("started_at"))
    update_ledger(hyp, "voided", reason, champ, chal, int(began) if began is not None else int(now), now, name)
    # (no confidence line: a void is not a reading of the idea)
    apply("killed", hyp, name, now, current_equities(now))
    return hyp


def process_voids(now: int, rules: dict) -> list[str]:
    """Act on configs/void.yaml. Returns the hypotheses voided. Whatever is in
    the file, this never raises: it runs every hour ahead of the verdicts, and
    a typo in a file edited by hand must not stop them, the summary or the
    commit (found in review, 2026-10-04)."""
    path = config.CONFIGS / "void.yaml"
    if not path.exists():
        return []
    try:
        body = config.load_yaml(path)
    except Exception as e:  # noqa: BLE001
        print(f"[promote] configs/void.yaml is not readable ({e}); ignored until it is fixed")
        return []
    requests = body.get("requests") if isinstance(body, dict) else body
    if not requests:
        if isinstance(body, dict) and body and "requests" not in body:
            print(f"[promote] configs/void.yaml has no `requests` list (it has {sorted(map(str, body))}); "
                  f"nothing is voided until the key is spelt `requests`")
        return []
    if not isinstance(requests, list):
        print(f"[promote] configs/void.yaml: requests must be a list, found {type(requests).__name__}; dropped")
        requests = []
    done = []
    for req in requests:
        try:
            hyp = _void_one(req, now, rules)
        except Exception as e:  # noqa: BLE001
            print(f"[promote] void request {req!r} failed ({type(e).__name__}: {e}); dropped")
            continue
        if hyp:
            done.append(hyp)
    try:
        config.dump_yaml(path, {"requests": []}, VOID_HEADER)
    except Exception as e:  # noqa: BLE001
        print(f"[promote] could not empty configs/void.yaml ({e})")
    return done


def _guard_reading(meta: dict, now: int, rules: dict) -> tuple[dict, dict, dict, dict]:
    """The shadow guard's two sides over its window so far, the market over
    it, and their usual exposures (worked out once and kept in its meta)."""
    start = int(meta["started_at"])
    ue, changed = usual_exposures(meta, config.CHAMPION, config.SHADOW, start)
    if changed:
        shadow.save(meta)
    champ, shad, mc = paired(config.CHAMPION, config.SHADOW, start, now, meta.get("start_equity"), rules, ue)
    return champ, shad, mc, ue


def guard_waits(now: int, rules: dict) -> str | None:
    """Why the shadow guard, past its window, is not ruled on this hour, or
    None when no guard is due a ruling or nothing stands in its way. For the
    summary; `rule_on_shadow` says the same in the hourly log."""
    meta = shadow.load()
    if not isinstance(meta, dict) or meta.get("status") != "active":
        return None
    try:
        start = int(meta["started_at"])
        if (now - start) / 86400 < rule_settings(rules)[0]["window_days"]:
            return None
        ue = meta.get("usual_exposure") or {}            # only what the guard has already worked out
        ue = ue if isinstance(ue, dict) and ue.get("start") == start else {}
        champ, shad, mc = paired(config.CHAMPION, config.SHADOW, start, now, meta.get("start_equity"), rules, ue)
    except Exception as e:  # noqa: BLE001
        return f"its record could not be read ({type(e).__name__}: {e})"
    return no_record(champ, shad, config.SHADOW) or missing_market_data(mc, rules)


def rule_on_shadow(now: int, rules: dict) -> None:
    """After a promotion's guard window: keep the promotion or revert it. The
    guard asks the ordinary rule with the two configs changed round (did the
    deposed one beat its replacement, with the drawdown guard and min_trades
    fills), not the bar against holding the market. Like the looks, it waits
    for the market data when the rules compare on skill, and for an equity
    record that has no usable reading in the window.

    A record that cannot be read is said and waited for: it must not stop
    the slots' rulings, the summary or the commit of the hour's trading. Only
    the reading is guarded that way. Once a ruling is made, a write that
    fails (the ledger, champion.yaml, the shadow's own files) stops the hour,
    so that nothing of a half made revert is committed and the next hour
    makes it again from the last whole state."""
    try:
        meta = shadow.load()
        if not isinstance(meta, dict):
            raise ValueError("it is not a shadow record")
        if meta.get("status") != "active":
            return
        start, promoted_hyp = int(meta["started_at"]), meta["replaced_by"]
        if not isinstance(promoted_hyp, str) or not promoted_hyp:
            raise ValueError("it does not name the promotion it guards")
        window = rule_settings(rules)[0]["window_days"]
        elapsed = (now - start) / 86400
        if elapsed < window:
            print(f"[promote] shadow {meta.get('hypothesis')} guarding {promoted_hyp}: day {elapsed:.1f} of {window:.0f}")
            return
        champ, shad, mc, ue = _guard_reading(meta, now, rules)
    except Exception as e:  # noqa: BLE001
        print(f"[promote] WARNING: the shadow guard could not be ruled on this hour ({type(e).__name__}: {e}); "
              f"nothing is ruled for it until its record can be read")
        return
    blank, gap = no_record(champ, shad, config.SHADOW), missing_market_data(mc, rules)
    if blank or gap:
        print(f"[promote] WARNING: the guard on {promoted_hyp} is due a ruling on day {elapsed:.1f} but "
              f"{blank or gap}; nothing is ruled until {'that record' if blank else 'the market data'} is whole")
        return
    verdict, reason = decide(champ, shad, rules, absolute=False)   # "promoted" here means the shadow beat the champion
    if verdict == "promoted":
        reason = f"the deposed config beat the promoted one over the guard window: {reason}; promotion reverted"
        print(f"[promote] {promoted_hyp}: reverted — {reason}")
        update_ledger(promoted_hyp, "reverted", reason, champ, shad, start, now, "shadow",
                      labels=("Promoted champion", "Deposed config (shadow)"), status_from="promoted")
        undone = config.account_cfg(config.CHAMPION)
        old = config.account_cfg(config.SHADOW)
        config.dump_yaml(config.CONFIGS / "champion.yaml",
                         {"hypothesis": old["hypothesis"], "strategy": old["strategy"], "params": old["params"]},
                         CHAMPION_HEADER)
        shadow.stop("reverted")
        record_champion_change(now, undone.get("hypothesis"), old.get("hypothesis"), "revert", ue.get(config.SHADOW))
        sync_idle_slots(config.strategy_signature(undone))
    else:
        reason = f"the promoted config held against the deposed one over the guard window: {reason}"
        print(f"[promote] {promoted_hyp}: held — {reason}")
        update_ledger(promoted_hyp, "held", reason, champ, shad, start, now, "shadow",
                      labels=("Promoted champion", "Deposed config (shadow)"), status_to="")
        shadow.stop("held")


def restart(name: str, now: int, equities: dict[str, float], new_champion: str) -> None:
    meta = slot.load(name)
    meta["started_at"] = int(now)
    meta["start_equity"] = {k: float(v) for k, v in equities.items() if k in (config.CHAMPION, name)}
    meta["restarted_against"] = new_champion
    meta["ruleset"] = config.ruleset_stamp()
    meta.pop("first_look", None)             # a fresh window starts with a fresh first look
    slot.save(name, meta)


def current_equities(now: int) -> dict[str, float]:
    """Each account's newest equity that is a number. A blank cell in the hour
    of a promotion used to go into the shadow's start equity as NaN and the
    guard then could never revert (found in review, 2026-10-05)."""
    out = {}
    for name in config.accounts():
        try:
            eq = _equity_rows(config.account_dir(name) / "equity.csv", 0, int(now))
        except Unreadable as e:
            print(f"[promote] WARNING: {e}; no equity figure for {name} this hour")
            continue
        if len(eq):
            out[name] = float(eq["equity"].iloc[-1])
    return out


def _days_ahead(total: float, elapsed: float) -> str:
    """What follows a first look, in words that are true for the day it came on."""
    left = total - elapsed
    if left <= 0:
        return (f"this look came on day {elapsed:.1f}, at or past day {total:.0f}, so the verdict on the whole test "
                f"follows at the next run")
    hours = int(round(max(left * 24, 1)))
    span = f"{left:.0f} more days" if left >= 1.5 else f"{hours} more hour{'' if hours == 1 else 's'}"
    return f"{span} in the same slot, then a verdict on all {total:.0f} days"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now", type=int, default=None)
    args = ap.parse_args(argv)
    config.prepare()
    now = args.now or int(time.time())
    rules = config.risk_cfg()["challenger"]
    st, unusable = rule_settings(rules)
    # one dict per verdict: slot, hyp, verdict, reason; early = an early kill;
    # base = the reason without the fast pass sentence (for a restart)
    verdicts: list[dict] = []
    for line in unusable + other_notes():
        print(f"[promote] WARNING: {line}")
    rule_on_shadow(now, rules)
    process_voids(now, rules)
    testing = []
    for n in config.challengers():
        try:
            meta_n = slot.load(n)
            if not isinstance(meta_n, dict):
                raise ValueError("it is not a slot record")
            if meta_n.get("status") == "testing":
                testing.append((n, meta_n))
        except Exception as e:  # noqa: BLE001
            print(f"[promote] WARNING: {n}: its slot record (meta.json) could not be read this hour "
                  f"({type(e).__name__}: {e}); nothing is ruled for it until it can be")
    if not testing:
        print("[promote] no test running; nothing to rule on")
        return 0
    for name, meta in testing:
        try:
            if not isinstance(meta["hypothesis"], str) or not meta["hypothesis"]:
                raise ValueError("its slot record names no hypothesis")
            sides = paired_slot(name, meta, now, rules)
        except Exception as e:  # noqa: BLE001
            # One slot whose record cannot be read must not stop the rulings for the others, the summary or
            # the commit of the hour's trading; it is said here every hour until the record is mended. Only
            # the reading is guarded this way: a ruling that fails while it is being written stops the hour.
            print(f"[promote] WARNING: {name}: {meta.get('hypothesis')} could not be looked at this hour "
                  f"({type(e).__name__}: {e}); nothing is ruled for it until its record can be read")
            continue
        _look_at(name, meta, now, rules, st, verdicts, sides)

    # strongest winner first, so a second winner in the same hour is restarted, not promoted over it
    def strength(v):
        champ_, chal_, _ = v["sides"]
        key = "skill" if compare_on(rules, champ_, chal_) == "skill" else "return"
        return chal_[key] if chal_[key] is not None else -1e9
    verdicts.sort(key=lambda v: (v["verdict"] != "promoted", -strength(v)))

    promoted_hyp: str | None = None
    for v in verdicts:
        name, hyp, verdict, reason = v["slot"], v["hyp"], v["verdict"], v["reason"]
        meta, (champ, chal, mc) = v["meta"], v["sides"]     # as read for the look: nothing a ruling does this hour
        start = int(meta["started_at"])                     # changes another slot's window
        if verdict == "promoted" and promoted_hyp is not None:
            reason = (f"beat the old champion ({v.get('base', reason)}) but {promoted_hyp} won by more this hour "
                      f"and was promoted; restarted against the new champion with a fresh window")
            print(f"[promote] {name}: {hyp}: restarted — {reason}")
            update_ledger(hyp, "restarted", reason, champ, chal, start, now, name)
            restart(name, now, current_equities(now), promoted_hyp)
            continue
        print(f"[promote] {name}: {hyp}: {verdict} — {reason}")
        extra = [f"Confidence: {confidence_line(chal, rules)}"]
        if not two_looks(meta, rules) and st["two_from"] is not None:
            extra.append("Two look rule (measured, not applied to this test): "
                         + other_rule_reading(champ, chal, rules, (now - start) / 86400, early=bool(v.get("early")),
                                              gap=missing_market_data(mc, rules)))
        update_ledger(hyp, verdict, reason, champ, chal, start, now, name, extra=extra)
        apply(verdict, hyp, name, now, current_equities(now))
        if verdict == "promoted":
            promoted_hyp = hyp
    return 0


def _look_at(name: str, meta: dict, now: int, rules: dict, st: dict, verdicts: list[dict],
             sides: tuple[dict, dict, dict]) -> None:
    """One slot's hour: the early kills, then a look if one is due. Appends a
    verdict to `verdicts`, or writes a First look block, or does nothing.
    sides: the slot's `paired_slot` reading for this hour, which `main` takes
    (and guards) before this is called. Nothing here is guarded: a first look
    whose block cannot be written stops the hour, and is taken again at the
    next one."""
    start, hyp = int(meta["started_at"]), meta["hypothesis"]
    champ, chal, mc = sides
    elapsed = (now - start) / 86400
    basket = None if mc.get("gap") else mc.get("basket_return")

    def rule(verdict: str, reason: str, **more) -> None:
        verdicts.append({"slot": name, "hyp": hyp, "verdict": verdict, "reason": reason, "meta": meta,
                         "sides": sides, **more})

    began_with = meta.get("start_equity")
    equity0 = _reading(began_with.get(name) if isinstance(began_with, dict) else None) \
        or config.risk_cfg()["initial_cash"]
    reason = early_kill(chal, rules, elapsed, equity0, gate_cost_drag()[0], basket)
    if reason:
        rule("killed", reason, early=True)
        return
    if early_kill_waits(chal, rules, basket):
        print(f"[promote] WARNING: {name}: {hyp} has lost {-chal['return']:.2%} since its test began, past the early "
              f"kill limit, but {mc.get('gap') or 'there is no figure for the market'}, so it cannot be said whether "
              f"the market lost more; no early kill this hour")
    first, total = st["window_days"], total_days(meta, rules)
    if elapsed < first:
        print(f"[promote] {name}: {hyp} on day {elapsed:.1f} of {total:.0f}; no verdict yet")
        return
    had_first_look = bool(first_look_of(meta))
    if had_first_look and elapsed < total:
        print(f"[promote] {name}: {hyp} on day {elapsed:.1f} of {total:.0f}, past its first look; no verdict yet")
        return
    # A ruling is due. It waits for an equity record and for market data that are whole.
    blank = no_record(champ, chal, name)
    if blank:
        print(f"[promote] WARNING: {name}: {hyp} is due a ruling on day {elapsed:.1f} but {blank}; nothing is "
              f"ruled until that record is whole")
        return
    gap = missing_market_data(mc, rules)
    if gap:
        # never a ruling on raw return because the candles for the window are not whole this hour
        print(f"[promote] WARNING: {name}: {hyp} is due a ruling on day {elapsed:.1f} but {gap}; nothing is "
              f"ruled until the market data is whole")
        return
    new_rule = two_looks(meta, rules)
    if had_first_look:
        rule(*decide_final(champ, chal, rules))
        return

    # The first look (for a test from before ruleset 7: its one look).
    outcome, reason, why = look(champ, chal, rules)
    if outcome == "kill":
        rule("killed", f"{'first look: ' if new_rule else ''}{why}")
        return
    if outcome == "pass":
        if not new_rule:
            rule("promoted", reason)
            return
        fast = fast_pass(chal, rules)
        if fast:
            rule("promoted", f"first look: {reason}; {fast}", base=f"first look: {reason}")
            return
    on_value = outcome == "value"
    total = first + st["confirm_days"]
    ahead = _days_ahead(total, elapsed)
    if on_value:
        note = (f"first look: it does not pass the rule ({reason}), but its trades are of value: {why}. A test "
                f"whose trades are of value is kept, not killed (Fin, 2026-10-05). Not a promotion: {ahead}")
    else:
        held_back = fast_pass_withheld(chal, rules)
        note = f"first look passed: {reason}. " + (f"{held_back}. " if held_back else "") + f"Not a promotion: {ahead}"
    print(f"[promote] {name}: {hyp}: {note}")
    update_ledger(hyp, "kept on value" if on_value else "passed", note, champ, chal, start, now, name,
                  status_to="", heading="First look", extra=[f"Confidence: {confidence_line(chal, rules)}"])
    # the block first, then the record of it: if writing the block fails, the look is simply taken again
    meta["first_look"] = {"at": int(now), "start": start, "reason": reason, "on": "value" if on_value else "rule"}
    slot.save(name, meta)
    # never a verdict in the hour of the first look


if __name__ == "__main__":
    raise SystemExit(main())
