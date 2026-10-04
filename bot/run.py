"""Hourly entry point and the single decision step shared with the backtest. PROTECTED.

    python -m bot.run                      # champion plus every challenger slot
    python -m bot.run --account champion   # a subset

For every account: refresh candles, read quotes, ask the strategy for target
weights, let risk.py trim them, fill the difference in the paper account, and
log every decision with its reason. bot/backtest.py replays the same `step`
over history so the two can never disagree about how a decision becomes a fill.

The run is driven by closed candles, not by the clock. Each account remembers
the last candle it decided on (`last_bar`). A run that finds that candle
already decided does nothing, so a second trigger in the same hour is
harmless. A run that finds several undecided candles (GitHub dropped scheduled
runs for hours on 2026-10-03) replays the missed ones first, oldest first,
through the same `step`, filling at the next candle's open exactly as the
backtest does, and then makes the live decision at the live quote. A late run
delays the record; it no longer leaves holes in it.

Three things a replay must not do, each found in review before this shipped:
count a held pair as worth nothing in an hour it has no price for (it keeps its
last known price and sits the hour out), run a strategy over hours from before
it existed (a changed strategy is never replayed; it starts fresh on the
current candle), or mistake a dead candle feed for a duplicate trigger (a run
that cannot get the candle that just closed fails, loudly, and decides nothing).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from datetime import datetime, timezone

from . import config, data, paper, risk, slot, strategy

DECISION_FIELDS = ["ts", "account", "pair", "price", "signal_weight", "target_weight",
                   "current_weight", "action", "reason", "half_spread_bps"]
MAX_REPLAY_BARS = 72      # a gap longer than three days is not replayed hour by hour
REPLAYED = "replayed after a missed run | "
STARVED = re.compile(r"only \d+ candles")
SITS_OUT = ("sits this hour out: no candle or no price for it this hour, so it is held as it is "
            "and valued at its last known price")


def utc_day(ts: int) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")


def step(acct: paper.PaperAccount, cfg: dict, fn, candles: dict, prices: dict[str, float],
         ts: int, rcfg: dict, half_spreads: dict[str, float] | None = None,
         fresh: bool = False, marks: dict | None = None) -> tuple[list[dict], list[paper.Fill], float]:
    """One decision cycle for one account at one timestamp. Mutates the account.
    half_spreads (bps, per pair) come from live quotes; the backtest passes none
    and pays the modelled floor.

    A pair is decided on only when it is in both `candles` and `prices`. A held
    pair that is not sits the hour out: it is not traded, it keeps its weight,
    and it is valued at the last price known for it (paper.PaperAccount.remember;
    `marks` is {pair: (price, time)}, the caller's newest candle closes).

    fresh: this is the account's first hour under a new strategy. The strategy
    then decides as if the account were flat, and the account trades from the
    book it actually holds to those targets. Without this a new strategy treats
    positions another strategy opened as its own and holds them under its own
    exit rule (found 2026-09-25: H3 spent its first 40 hours riding the
    champion copy's book, and every fill in that stretch was an exit of it)."""
    half_spreads = half_spreads or {}
    impact = float(rcfg.get("impact_bps", 0.0))
    st = acct.state
    name = acct.name
    if st["created_at"] is None:
        st["created_at"] = ts
    prices = {p: v for p, v in prices.items() if v > 0}     # a zero or missing price is no price
    acct.remember(prices, ts, marks)      # before anything is valued
    day = utc_day(ts)
    equity = acct.equity(prices)
    if st["day"] != day:
        st["day"] = day
        st["day_open_equity"] = equity
    halted = st["halted_day"] == day
    halt_note = ""
    if not halted and risk.daily_halt_triggered(equity, st["day_open_equity"], rcfg):
        halted = True
        st["halted_day"] = day
        halt_note = (f"daily halt: equity {equity:.2f} is down "
                     f"{1 - equity / st['day_open_equity']:.1%} from the day's open {st['day_open_equity']:.2f}")

    # Fills per pair per UTC day. Buys stop at the cap; sells never do, so a
    # position can always be closed. Found the hard way: H3 looped enter, exit,
    # enter for nine days (124 fills, costs at 116% of equity a year) because
    # nothing in the execution path bounded it.
    cap = int(rcfg.get("max_fills_per_pair_per_day", 0) or 0)
    fd = st.get("fills_day")
    if not fd or fd.get("day") != day:
        fd = st["fills_day"] = {"day": day, "counts": {}}
    counts = fd["counts"]

    current_w = acct.weights(prices)
    tradable = {p: df for p, df in candles.items() if p in prices and len(df)}
    idle = [p for p in acct.positions if p not in tradable]     # held, and nothing to decide on this hour
    # Positions another strategy opened: the whole book on the first hour under
    # a new strategy. One that sits that hour out stays on the list until it
    # can be decided on, so the new strategy never adopts it as its own.
    inherited = set(acct.positions) if fresh else set(st.get("inherited") or ()) & set(acct.positions)
    if halted:
        targets = {p: strategy.Target(0.0, halt_note or "daily halt in force: flat for the rest of the UTC day")
                   for p in tradable}
    else:
        own_w = {p: w for p, w in current_w.items() if p not in inherited}
        try:
            targets = strategy.normalise(fn(tradable, cfg["params"], own_w))
        except Exception as e:  # noqa: BLE001
            # A broken strategy must not crash the loop or leave stale positions: go flat and say why.
            targets = {p: strategy.Target(0.0, f"strategy error {type(e).__name__}: {e}") for p in tradable}
        if fresh:
            targets = {p: strategy.Target(t.weight, "first hour under a new strategy, decided as if flat | " + t.reason)
                       for p, t in targets.items()}
        elif inherited:
            targets = {p: strategy.Target(t.weight, "held over from the previous strategy, decided as if flat | "
                                          + t.reason) if p in inherited else t for p, t in targets.items()}
    for p in tradable:
        targets.setdefault(p, strategy.Target(0.0, "strategy returned no target for this pair"))
    # the gross limit is for the whole book, so a position that sits out uses up its share of it
    frozen = sum(current_w.get(p, 0.0) for p in idle)
    room = rcfg if not frozen else {**rcfg, "max_gross_weight": max(0.0, float(rcfg["max_gross_weight"]) - frozen)}
    limited = risk.apply_limits({p: targets[p].weight for p in tradable}, room)

    # Reductions fill before additions, so cash an exit frees this hour can fund
    # this hour's entries (a real bot sells first too). Before 2026-09-25 the
    # loop ran in pairs order and an entry early in the list could find no cash
    # while an exit later in the list freed it. The sort is stable, and the
    # decision log keeps pairs order.
    order = sorted(tradable, key=lambda p: 0 if limited.get(p, 0.0) < current_w.get(p, 0.0) else 1)
    by_pair, fills = {}, []
    for pair in order:
        sig_w = targets[pair].weight
        tgt_w = limited.get(pair, 0.0)
        cur_w = current_w.get(pair, 0.0)
        reason = targets[pair].reason
        ok, why = risk.worth_trading(tgt_w, cur_w, equity, rcfg)
        action = "hold"
        delta = (tgt_w - cur_w) * equity
        if ok and delta > 0 and cap and counts.get(pair, 0) >= cap:
            action = "none"
            why = (f"capped: {counts[pair]} fills in {pair} today, the limit is {cap} a day, so no new buys "
                   f"until the next UTC day (sells are never capped)")
        elif ok:
            fill = acct.trade(pair, delta, prices[pair], ts, reason, rcfg["min_trade_notional"],
                              half_spread_bps=half_spreads.get(pair), impact_bps=impact)
            if fill:
                fill.equity_after = acct.equity(prices)
                fills.append(fill)
                action = fill.side
                counts[pair] = counts.get(pair, 0) + 1
            else:
                action = "none"
                if delta > 0:
                    # Not a bug: see FINDINGS, blocked entries. Funding the buy by
                    # trimming other positions was tested on H0 and H4 over one and
                    # two years (2026-09-25 and 2026-09-27) and did not pay.
                    why = ("waits for cash: the book is fully invested and no position is far enough above "
                           "its target to trim, so this buy fills when an exit or a bigger drift frees cash")
                else:
                    why = "no fill possible (no position to sell)"
        by_pair[pair] = {
            "ts": ts, "account": name, "pair": pair, "price": round(prices[pair], 6),
            "signal_weight": round(sig_w, 4), "target_weight": round(tgt_w, 4),
            "current_weight": round(cur_w, 4), "action": action,
            "reason": (why + " | " if why else "") + reason,
            "half_spread_bps": round(half_spreads.get(pair, 0.0), 3),
        }
    decisions = [by_pair[p] for p in tradable]
    valued = acct.valued(prices)
    for pair in idle:
        w = round(current_w.get(pair, 0.0), 4)
        decisions.append({"ts": ts, "account": name, "pair": pair, "price": round(valued.get(pair, 0.0), 6),
                          "signal_weight": w, "target_weight": w, "current_weight": w, "action": "none",
                          "reason": SITS_OUT, "half_spread_bps": round(half_spreads.get(pair, 0.0), 3)})
    acct.remember(prices, ts)             # positions opened this hour get their mark
    left = sorted(p for p in inherited if p not in tradable and p in acct.positions)
    if left:
        st["inherited"] = left
    else:
        st.pop("inherited", None)
    st["last_run_ts"] = ts
    return decisions, fills, acct.equity(prices)


def _equity_row(acct: paper.PaperAccount, ts: int, equity: float, prices: dict[str, float]) -> dict:
    st = acct.state
    return {"ts": ts, "equity": round(equity, 4), "cash": round(acct.cash, 4),
            "gross_exposure": round(acct.gross_exposure(prices), 4), "n_positions": len(acct.positions),
            "fees_paid": round(st["fees_paid"], 4), "slippage_paid": round(st["slippage_paid"], 4)}


def decided_bar(state: dict) -> int | None:
    """The newest candle this account has decided on. An account from before
    that was recorded (2026-10-04) had last decided at last_run_ts, on the
    candle that had closed by then, so it carries on from there and the hours
    GitHub dropped just before the change are replayed like any others."""
    if state.get("last_bar") is not None:
        return int(state["last_bar"])
    if state.get("last_run_ts"):
        return int(state["last_run_ts"]) // 3600 * 3600 - 3600
    return None


def pending_bars(full: dict, last_bar: int | None, latest_bar: int) -> list[int]:
    """Candle open times this account still has to decide on, oldest first,
    ending at the newest closed candle. A new account decides on the newest
    candle only."""
    if last_bar is None:
        return [latest_bar]
    if last_bar >= latest_bar:
        return []
    found: set[int] = set()
    for df in full.values():
        tt = df["time"].to_numpy()
        found.update(int(x) for x in tt[(tt > last_bar) & (tt <= latest_bar)])
    times = sorted(found)
    if latest_bar not in times:
        times.append(latest_bar)
    if len(times) > MAX_REPLAY_BARS + 1:
        print(f"[run] {len(times) - 1} missed candles is more than {MAX_REPLAY_BARS}; "
              f"replaying only the last {MAX_REPLAY_BARS}")
        times = times[-(MAX_REPLAY_BARS + 1):]
    return times


def run_account(name: str, full: dict, prices: dict[str, float], ts: int, rcfg: dict,
                half_spreads: dict[str, float] | None = None, latest_bar: int | None = None) -> float:
    """Bring one account up to date. `full` is history plus live per pair (all
    of it); the strategy is shown the trailing history_hours ending at the
    candle being decided. Returns the account's equity at the live prices."""
    cfg = config.account_cfg(name)
    fn = strategy.get(cfg["strategy"])
    adir = config.account_dir(name)
    acct = paper.PaperAccount.load(adir / "account.json", name, rcfg["initial_cash"],
                                   rcfg["fee_bps"], rcfg["slippage_bps"])
    hist = int(rcfg.get("history_hours", 720))
    if latest_bar is None:
        latest_bar = max((int(df["time"].max()) for df in full.values() if len(df)), default=ts // 3600 * 3600 - 3600)
    bars = pending_bars(full, decided_bar(acct.state), latest_bar)
    if not bars:
        print(f"[{name}] already decided on the candle of "
              f"{datetime.fromtimestamp(latest_bar, timezone.utc):%Y-%m-%d %H:%M}Z; nothing to do")
        return acct.equity(prices)
    # A changed strategy (a new test in a slot, a promotion, a revert) decides
    # its first hour as if flat. An account with no signature on record predates
    # this rule: record it and carry on, so deploying it moves nothing.
    sig = config.strategy_signature(cfg)
    prev = acct.state.get("strategy_sig")
    fresh = prev is not None and prev != sig
    if fresh and len(bars) > 1:
        # Nobody can say at which of the missed hours the new strategy arrived,
        # and replaying it over hours from before it existed would date its
        # first fills before its test window opens. It starts on the current
        # candle, as it would have with no hours missed.
        print(f"[{name}] the strategy changed since the last run, so the {len(bars) - 1} missed hours are "
              f"not replayed; it starts fresh on the current candle")
        bars = bars[-1:]

    all_decisions, all_fills, equity_rows = [], [], []
    for i, bar in enumerate(bars):
        live = i == len(bars) - 1
        upto = {p: df[df["time"] <= bar] for p, df in full.items()}
        upto = {p: df for p, df in upto.items() if len(df)}
        # every pair's newest close and when it closed: what a held pair is valued at if it has no price
        known = {p: (float(df["close"].iloc[-1]), int(df["time"].iloc[-1]) + 3600) for p, df in upto.items()}
        # a pair is decided on only when its candle for this hour exists, as in the backtest
        frames = {p: df.tail(hist).reset_index(drop=True) for p, df in upto.items()
                  if int(df["time"].iloc[-1]) == bar}
        if live:
            step_prices, step_ts, spreads = prices, ts, half_spreads
        else:
            # a missed hour: decide on the candle that closed then, fill at the next candle's open
            nxt = bars[i + 1]
            step_prices = {}
            for p in frames:
                row = full[p][full[p]["time"] == nxt]
                if len(row) and float(row["open"].iloc[0]) > 0:
                    step_prices[p] = float(row["open"].iloc[0])
            step_ts, spreads = nxt, None
            if not step_prices:
                continue
        decisions, fills, equity = step(acct, cfg, fn, frames, step_prices, step_ts, rcfg, spreads,
                                        fresh=fresh, marks=known)
        fresh = False
        if not live:
            for d in decisions:
                d["reason"] = REPLAYED + d["reason"]
            for f in fills:
                f.reason = REPLAYED + f.reason
        if frames and any(STARVED.search(d["reason"]) for d in decisions) \
                and min(len(f) for f in frames.values()) >= hist:
            print(f"[{name}] WARNING: {cfg['strategy']} says it has too few candles although it was handed "
                  f"{hist}. It needs more history than history_hours provides and cannot trade.")
        out = sorted({d["pair"] for d in decisions if d["reason"].endswith(SITS_OUT)})
        if out:
            print(f"[{name}] {', '.join(out)} held with no candle or no price at "
                  f"{datetime.fromtimestamp(step_ts, timezone.utc):%Y-%m-%d %H:%M}Z: valued at the last known price")
        all_decisions += decisions
        all_fills += fills
        equity_rows.append(_equity_row(acct, step_ts, equity, step_prices))
    acct.state["strategy_sig"] = sig
    acct.state["last_bar"] = int(latest_bar)
    acct.save(adir / "account.json")
    paper.append_rows(adir / "decisions.csv", DECISION_FIELDS, all_decisions)
    paper.append_rows(adir / "trades.csv", paper.TRADE_FIELDS, [paper.fill_row(f) for f in all_fills])
    paper.append_rows(adir / "equity.csv", paper.EQUITY_FIELDS, equity_rows)
    st = acct.state
    equity = acct.equity(prices)
    n_buy = sum(1 for f in all_fills if f.side == "buy")
    n_sell = len(all_fills) - n_buy
    halted = st["halted_day"] == utc_day(ts)
    replayed = f" (replayed {len(bars) - 1} missed hours)" if len(bars) > 1 else ""
    print(f"[{name}] {cfg['strategy']} ({cfg['hypothesis']}) equity {equity:,.2f} "
          f"cash {acct.cash:,.2f} positions {len(acct.positions)} fills {n_buy} buy / {n_sell} sell"
          + (" HALTED" if halted else "") + replayed)
    return equity


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--account", action="append", default=None)
    ap.add_argument("--now", type=int, default=None, help="unix ts override (tests)")
    args = ap.parse_args(argv)
    config.prepare()
    accounts = args.account or config.accounts()
    ts = args.now or int(time.time())
    rcfg = config.risk_cfg()
    pairs = list(rcfg["pairs"])
    source = data.get_source(pairs, rcfg.get("quote", "USD"))

    data.update_candles(pairs, source)
    # History plus live, the same frames the backtest replays. The live cache
    # alone is a few weeks deep and starves any lookback longer than that
    # (found by the weekly digest on 2026-09-21: H2 sat flat on "need 1610").
    full = {p: data.load_all_candles(p) for p in pairs}
    full = {p: df for p, df in full.items() if len(df)}
    if not full:
        print("[data] no candles at all; nothing to do")
        return 1
    latest_bar = max(int(df["time"].max()) for df in full.values())
    due = ts // 3600 * 3600 - 3600        # the candle that closed at the top of this hour
    if latest_bar < due:
        # Not a duplicate trigger: the feed is down or behind. Deciding now, on a
        # candle that is hours old, would also put this hour's rows after the
        # rows a later replay writes for the hours in between. Fail so it is
        # seen; the next run that gets candles replays what was missed.
        print(f"[data] no pair has the candle that closed at "
              f"{datetime.fromtimestamp(due + 3600, timezone.utc):%Y-%m-%d %H:%M}Z (the newest closed at "
              f"{datetime.fromtimestamp(latest_bar + 3600, timezone.utc):%Y-%m-%d %H:%M}Z). The candle feed is "
              f"down or behind, so nothing is decided this run")
        return 1
    # A run that starts seconds before the hour can fetch its last pairs after
    # it, and those then hold a candle the others do not. This run decides on
    # the candle that was due when it started; the newer one waits for the next.
    latest_bar = min(latest_bar, due)
    done = {name: _decided(name) for name in accounts}
    if all(b is not None and b >= latest_bar for b in done.values()):
        print(f"[run] every account has already decided on the candle of "
              f"{datetime.fromtimestamp(latest_bar, timezone.utc):%Y-%m-%d %H:%M}Z; nothing to do this run")
        _github_output("skipped", "1")
        return 0
    qs = data.quotes(pairs, source)
    prices = {p: q.mid for p, q in qs.items()}
    half_spreads = {p: q.half_spread_bps for p, q in qs.items()}
    missing = [p for p in pairs if p not in prices]
    if missing:
        print(f"[data] no quote for {missing}; those pairs are held as they are this run")
    if not prices:
        print("[data] no quotes at all; nothing to do")
        return 1
    print(f"[run] {datetime.fromtimestamp(ts, timezone.utc):%Y-%m-%d %H:%M}Z "
          + " ".join(f"{p}={prices[p]:.4g}" for p in prices))

    equities = {}
    for name in accounts:
        equities[name] = run_account(name, full, prices, ts, rcfg, half_spreads, latest_bar)
    if set(accounts) >= set(config.accounts()):
        slot.maybe_start(ts, equities)
    _github_output("skipped", "0")
    _deep_history(pairs, rcfg, ts)
    return 0


def _deep_history(pairs: list[str], rcfg: dict, ts: int) -> None:
    """Years of history are for backtests, not for this hour's decisions, so
    they are fetched after every account has decided, within a time budget,
    and nothing that goes wrong here can fail the run. (It used to come first:
    a slow venue could then have run the job into its timeout before any
    account acted, every hour, and a duplicate trigger fetched it all and threw
    it away.)"""
    target = int(rcfg.get("history_target_hours", 0))
    if not target:
        return
    try:
        data.backfill_if_short(pairs, target, data.get_history_source(pairs, rcfg.get("quote", "USD")), now=ts,
                               budget_s=float(rcfg.get("history_backfill_budget_s", 600)))
    except Exception as e:  # noqa: BLE001
        print(f"[data] history backfill failed ({type(e).__name__}: {e}); this hour's run is unaffected")


def _decided(name: str) -> int | None:
    p = config.account_dir(name) / "account.json"
    if not p.exists():
        return None
    try:
        return decided_bar(json.loads(p.read_text()))
    except Exception:  # noqa: BLE001
        return None


def _github_output(key: str, value: str) -> None:
    """Tell the workflow whether this run did anything (it skips the commit when not)."""
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a") as f:
            f.write(f"{key}={value}\n")


if __name__ == "__main__":
    raise SystemExit(main())
