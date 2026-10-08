"""Replay a strategy over cached candles with the live cost model. PROTECTED.

    python -m bot.backtest --config configs/challenger1.yaml [--days 60]

Signal at the close of bar t, fill at the open of bar t+1 with slippage and
fee, mark at the close of bar t+1. Uses bot.run.step, the same code path as
the hourly loop, so the backtest cannot be kinder than paper trading.

A backtest here is a plausibility filter, not evidence. The strategy was
designed after looking at this same data. The prospective challenger test is
the evidence.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import config, data, paper, strategy
from .run import CAPPED, ERRED, STARVED, step

HOURS_PER_YEAR = 24 * 365


def _last_price(arr, i: int):
    """Last non NaN value at or before index i, else None."""
    j = i
    while j >= 0:
        v = arr[j]
        if v == v:  # not NaN
            return float(v)
        j -= 1
    return None


def warmup_hours(params: dict, floor: int = 48) -> int:
    hours = [int(v) for k, v in params.items() if k.endswith("_hours") and isinstance(v, (int, float))]
    return max(hours + [floor]) + 2


def run_backtest(candles: dict[str, pd.DataFrame], cfg: dict, rcfg: dict,
                 max_days: int | None = None, name: str = "backtest", record: bool = False) -> dict:
    """Pairs need not share the same coverage: the clock is the union of all
    candle times, and a pair simply sits out any hour it has no candle for
    (a newer listing, a gap in one venue's history).

    record: also return the run hour by hour under `path`, for bot/bench.py:
    what the book was worth just after each hour's fills, at that hour's
    opens, the share of it in each pair, the costs paid so far, and every
    pair's open; when the run left each position by its own choice; how many
    hours of candles the strategy was handed; and on how many hours it
    failed (the engine goes flat on such an hour, as it does live), with
    what it said the first time. Keeping it changes nothing the run does."""
    fn = strategy.get(cfg["strategy"])
    frames = {p: df.sort_values("time").drop_duplicates("time").reset_index(drop=True)
              for p, df in candles.items() if len(df)}
    if not frames:
        raise ValueError("no candle data")
    times = sorted(set.union(*[set(df["time"].astype(int)) for df in frames.values()]))
    hist = int(rcfg.get("history_hours", 720))
    warm = warmup_hours(cfg["params"])
    if max_days:
        keep = max_days * 24 + warm + 1
        times = times[-keep:]
    if len(times) < warm + 24:
        raise ValueError(f"need at least {warm + 24} candles, have {len(times)}")
    tindex = pd.Index(times)
    # reindex every pair onto the shared clock; NaN where a pair has no candle
    aligned = {p: df.set_index("time").reindex(tindex) for p, df in frames.items()}
    present = {p: aligned[p]["close"].notna().to_numpy() for p in aligned}
    opens = {p: aligned[p]["open"].to_numpy() for p in aligned}
    closes = {p: aligned[p]["close"].to_numpy() for p in aligned}
    # The history handed to the strategy comes from the full frames, exactly as
    # the hourly loop hands it (bot.run.run_account): up to history_hours
    # candles ending at the bar being decided, however short the replayed window
    # is. Until 2026-10-04 it was cut to the replayed window plus warmup_hours,
    # and warmup_hours only knows the largest single *_hours parameter, so a
    # strategy that needs more than that (swing_reversal needs two recent_hours)
    # sat flat on "only N candles" for a whole short backtest: `--days 9` of H3
    # showed 0 trades while the live account made 124.
    compact = frames
    # position of each shared clock tick inside the pair's full frame (for fast slicing)
    pos = {p: np.searchsorted(frames[p]["time"].to_numpy().astype("int64"), np.array(times), side="right")
           for p in aligned}

    acct = paper.PaperAccount(name, rcfg["initial_cash"], rcfg["fee_bps"], rcfg["slippage_bps"])
    n_decisions = n_starved = 0
    capped_pair_days: set[tuple[str, str]] = set()
    equity_curve, fills_all = [], []
    trades_per_pair_day: dict[tuple[str, str], int] = defaultdict(int)
    exposure = []
    names = sorted(aligned)
    path = {"ts": [], "equity": [], "costs": [], "fills": [], "starved": [], "weights": [], "opens": [],
            "errors": 0, "first_error": None} if record else None
    for i in range(warm, len(times) - 1):
        live = [p for p in aligned if present[p][i] and present[p][i + 1]]
        if not live:
            continue
        window = {p: compact[p].iloc[max(0, pos[p][i] - hist): pos[p][i]] for p in live}
        next_open = {p: float(opens[p][i + 1]) for p in live if opens[p][i + 1] > 0}
        ts_fill = int(times[i + 1])
        # a held pair with no candle this hour sits it out, valued at its newest close (as in the hourly loop)
        marks = None
        if any(p not in next_open for p in acct.positions):
            marks = {}
            for p in acct.positions:
                if p in next_open or p not in aligned:
                    continue
                j = i
                while j >= 0 and not present[p][j]:
                    j -= 1
                if j >= 0:
                    marks[p] = (float(closes[p][j]), int(times[j]) + 3600)
        decisions, fills, at_open = step(acct, cfg, fn, window, next_open, ts_fill, rcfg, marks=marks)
        n_decisions += len(decisions)
        starved_now = sum(1 for d in decisions if STARVED.search(d["reason"]))
        n_starved += starved_now
        if path is not None:
            held = acct.weights(next_open)
            # the price each pair stands at this hour: its open; for a held pair that sits the hour out, the
            # mark the account values it at, so that equity moves from hour to hour by exactly these prices
            at = {**{p: float(opens[p][i + 1]) for p in names if present[p][i + 1] and opens[p][i + 1] > 0},
                  **{p: float(v) for p, v in acct.valued(next_open).items()}}
            path["ts"].append(ts_fill)
            path["equity"].append(float(at_open))
            path["costs"].append(float(acct.total_costs()))
            path["fills"].append(len(fills))
            path["starved"].append(starved_now == len(decisions))
            path["weights"].append([float(held.get(p, 0.0)) for p in names])
            path["opens"].append([at.get(p, float("nan")) for p in names])
            failed = next((d["reason"] for d in decisions if ERRED in d["reason"]), None)
            if failed is not None:
                path["errors"] += 1
                path["first_error"] = path["first_error"] or failed[failed.index(ERRED) + len(ERRED):][:200]
        day_fill = datetime.fromtimestamp(ts_fill, timezone.utc).strftime("%Y-%m-%d")
        # the engine's own words at the head of the reason, on a decision it did not fill: a strategy that
        # writes "capped:" in a reason of its own has had no buy stopped
        capped_pair_days.update((d["pair"], day_fill) for d in decisions
                                if d["action"] == "none" and d["reason"].startswith(CAPPED))
        for f in fills:
            fills_all.append(f)
            trades_per_pair_day[(f.pair, datetime.fromtimestamp(ts_fill, timezone.utc).strftime("%Y-%m-%d"))] += 1
        # mark at the next close; a pair without a candle keeps its last known price
        mark = {p: float(closes[p][i + 1]) if present[p][i + 1] else _last_price(closes[p], i + 1) for p in aligned}
        mark = {p: v for p, v in mark.items() if v is not None}
        eq = acct.equity(mark)
        equity_curve.append((ts_fill, eq))
        exposure.append(acct.gross_exposure(mark) / eq if eq > 0 else 0.0)
    if not equity_curve:
        raise ValueError("no hour had candles for any pair")

    eq = pd.Series([e for _, e in equity_curve], index=[t for t, _ in equity_curve])
    rets = eq.pct_change().dropna()
    total_return = float(eq.iloc[-1] / rcfg["initial_cash"] - 1)
    ann_vol = float(rets.std() * math.sqrt(HOURS_PER_YEAR)) if len(rets) > 1 else float("nan")
    ann_ret = float(rets.mean() * HOURS_PER_YEAR) if len(rets) else float("nan")
    sharpe = ann_ret / ann_vol if ann_vol and ann_vol > 0 else float("nan")
    running_max = eq.cummax()
    max_dd = float((eq / running_max - 1).min()) if len(eq) else 0.0
    last_prices = {p: v for p, v in ((p, _last_price(closes[p], len(times) - 1)) for p in aligned) if v is not None}
    gross = acct.gross_pnl(last_prices)
    costs = acct.total_costs()
    days = (times[-1] - times[warm]) / 86400
    n_pairs = len(aligned)
    max_tpd = max(trades_per_pair_day.values()) if trades_per_pair_day else 0
    from .promote import rule_settings                  # the one place the rules file is read into usable values
    window_days = rule_settings(rcfg.get("challenger"))[0]["window_days"]
    finished, forced, none_share = finished_trades(fills_all, int(times[warm]), int(times[-1]), window_days)
    if path is not None:
        path["exits"], path["span"] = own_exits(fills_all, int(times[warm]))[0], (int(times[warm]), int(times[-1]))
    # pair days on which the daily fill cap actually stopped a buy: the mark of a loop
    at_cap = len(capped_pair_days)
    kept = {} if path is None else {"path": {
        "pairs": names, "ts": np.array(path["ts"], dtype="int64"), "equity": np.array(path["equity"], dtype=float),
        "costs": np.array(path["costs"], dtype=float), "fills": np.array(path["fills"], dtype="int64"),
        "starved": np.array(path["starved"], dtype=bool),
        "weights": np.array(path["weights"], dtype=float).reshape(len(path["ts"]), len(names)),
        "opens": np.array(path["opens"], dtype=float).reshape(len(path["ts"]), len(names)),
        "exits": path["exits"], "span": path["span"], "memory_hours": hist,
        "errors": int(path["errors"]), "first_error": path["first_error"]}}
    return {
        **kept,
        "strategy": cfg["strategy"],
        "hypothesis": cfg.get("hypothesis"),
        "start": datetime.fromtimestamp(times[warm], timezone.utc).strftime("%Y-%m-%d"),
        "end": datetime.fromtimestamp(times[-1], timezone.utc).strftime("%Y-%m-%d"),
        "days": round(days, 1),
        "pairs": n_pairs,
        "bars": len(equity_curve),
        "final_equity": round(float(eq.iloc[-1]), 2),
        "total_return": round(total_return, 4),
        "annualised_return": round(ann_ret, 4) if np.isfinite(ann_ret) else None,
        "annualised_vol": round(ann_vol, 4) if np.isfinite(ann_vol) else None,
        "sharpe": round(sharpe, 2) if np.isfinite(sharpe) else None,
        "max_drawdown": round(max_dd, 4),
        "n_trades": len(fills_all),
        "trades_per_pair_per_day_avg": round(len(fills_all) / max(days, 1e-9) / n_pairs, 3),
        "trades_per_pair_per_day_max": max_tpd,
        "finished_trades": finished,
        "closed_by_halt_or_error": forced,
        "windows_with_no_finished_trade": none_share,
        "pair_days_at_fill_cap": at_cap,
        "starved_share": round(n_starved / n_decisions, 4) if n_decisions else 0.0,
        "gross_pnl": round(gross, 2),
        "fees": round(acct.state["fees_paid"], 2),
        "slippage": round(acct.state["slippage_paid"], 2),
        "net_pnl": round(gross - costs, 2),
        "cost_coverage": round(gross / costs, 2) if costs > 0 else None,
        "avg_gross_exposure": round(float(np.mean(exposure)), 3) if exposure else 0.0,
        "equity_curve": equity_curve,
    }


def finished_trades(fills: list, start_ts: int, end_ts: int, window_days: float = 60.0) -> tuple[int, int, float | None]:
    """Positions the run left by the strategy's own choice, positions the
    daily loss halt or a strategy error closed for it, and the share of test
    windows, one starting each day of the run, in which the strategy left
    none of its own. Counted by bot.promote.finished_trades, as a live test's
    are. A live test that has finished no trade of its own by the end of its
    first window is killed (PROMOTION.md), so that share is how often this
    strategy would have been, whatever it made. None when
    the run is shorter than one window."""
    exits, forced = own_exits(fills, start_ts)
    none = windows_with_no_exit(exits, start_ts, end_ts, window_days)
    return int(len(exits)), forced, None if none is None else round(none, 3)


def own_exits(fills: list, start_ts: int) -> tuple[np.ndarray, int]:
    """When the run left each position by the strategy's own choice, oldest
    first, and how many positions the daily loss halt or a strategy error
    closed for it. Counted by bot.promote.finished_trades, as a live test's are."""
    from .promote import finished_trades as positions_left      # promote does not load this module until it needs a backtest
    done = positions_left(pd.DataFrame([{"ts": f.ts, "pair": f.pair, "side": f.side, "qty": f.qty, "price": f.price,
                                          "notional": f.notional, "fee": f.fee, "reason": f.reason} for f in fills]),
                          start_ts) if fills else []
    return (np.array(sorted(t["ts"] for t in done if t["chosen"]), dtype="int64"),
            sum(1 for t in done if not t["chosen"]))


def windows_with_no_exit(exits: np.ndarray, start_ts: int, end_ts: int, window_days: float) -> float | None:
    """The share of test windows of `window_days`, one starting each day from
    start_ts and ending by end_ts, in which none of `exits` falls. None when
    the run is shorter than one window."""
    span = int(window_days * 86400)
    starts = np.arange(int(start_ts), int(end_ts) - span + 1, 86400, dtype="int64")
    if not len(starts):
        return None
    exits = np.asarray(exits, dtype="int64")
    inside = np.searchsorted(exits, starts + span, side="right") - np.searchsorted(exits, starts, side="right")
    return float((inside == 0).mean())


def plausibility(m: dict, rules: dict, market: dict | None, initial_cash: float,
                 market_fn=None) -> tuple[list[str], dict]:
    """The gate's sanity checks, regime independent, plus the informational
    skill figures. Returns (problems, report). Empty problems means pass.
    market_fn(start_ts, end_ts) gives the market context of any span; with it,
    a run longer than 400 days also gets a line per calendar year, each year
    against an equal weight basket of the pairs that existed when it began."""
    days = max(float(m["days"]), 1e-9)
    n_pairs = max(int(m["pairs"]), 1)
    costs = float(m["fees"]) + float(m["slippage"])
    cost_drag = costs / float(initial_cash) / (days / 365)
    avg_fills = float(m["n_trades"]) / days / n_pairs
    basket_dd = abs(float(market["basket_max_dd"])) if market and market.get("basket_max_dd") is not None else 0.0
    dd_limit = max(float(rules["max_drawdown"]), float(rules.get("drawdown_vs_basket", 0.0)) * basket_dd)
    problems = []
    if m["n_trades"] < int(rules.get("min_trades", 0)):
        problems.append(f"{m['n_trades']} fills over {days:.0f} days, fewer than the {rules['min_trades']} the gate needs "
                        f"before any of its numbers mean anything")
    if cost_drag > float(rules["max_cost_drag"]):
        problems.append(f"costs {costs:.0f} over {days:.0f} days is {cost_drag:.1%} of starting equity per year, above "
                        f"the {float(rules['max_cost_drag']):.0%} limit; that is a fees treadmill (P1)")
    if avg_fills > float(rules["max_avg_fills_per_pair_per_day"]):
        problems.append(f"{avg_fills:.2f} fills per pair per day on average, above {rules['max_avg_fills_per_pair_per_day']}")
    if float(m.get("starved_share", 0.0)) > float(rules.get("max_starved_share", 0.02)):
        problems.append(f"the strategy said it had too few candles on {float(m['starved_share']):.0%} of its "
                        f"decisions. Every strategy is handed history_hours of candles, so it is asking for more "
                        f"than it can ever get and this backtest is mostly not the strategy")
    cap_days = int(m.get("pair_days_at_fill_cap", 0))
    max_cap_days = rules.get("max_pair_days_at_fill_cap")
    if max_cap_days is not None and cap_days > int(max_cap_days) * days / 365:
        problems.append(f"the daily fill cap stopped a buy on {cap_days} pair days over {days:.0f} days (limit "
                        f"{int(max_cap_days)} a year): the strategy is entering and exiting the same pair in a "
                        f"loop and only the cap is stopping it")
    if float(m["max_drawdown"]) < -dd_limit:
        problems.append(f"max drawdown {m['max_drawdown']:.1%} worse than the limit {-dd_limit:.1%} (the larger of "
                        f"{float(rules['max_drawdown']):.0%} and {float(rules.get('drawdown_vs_basket', 0)):.2f} x the "
                        f"basket's own {basket_dd:.1%})")
    report = {"cost_drag_per_year": round(cost_drag, 4), "avg_fills_per_pair_per_day": round(avg_fills, 3),
              "pair_days_at_fill_cap": cap_days, "years": [],
              "drawdown_limit": round(-dd_limit, 4), "basket_return": None, "basket_max_dd": None,
              "exposure_matched_benchmark": None, "skill_vs_benchmark": None, "quarters": []}
    if market and market.get("basket_return") is not None:
        bench = float(market["basket_return"]) * float(m["avg_gross_exposure"])
        report.update({"basket_return": round(float(market["basket_return"]), 4),
                       "basket_max_dd": round(float(market["basket_max_dd"]), 4),
                       "exposure_matched_benchmark": round(bench, 4),
                       "skill_vs_benchmark": round(float(m["total_return"]) - bench, 4)})
        path = market.get("basket_path")
        curve = m.get("equity_curve")
        if path is not None and curve:
            eq = pd.Series([e for _, e in curve], index=[t for t, _ in curve])
            edges = np.linspace(eq.index.min(), eq.index.max(), 5).astype(int)
            for i in range(4):
                e = eq[(eq.index >= edges[i]) & (eq.index <= edges[i + 1])]
                b = path[(path.index >= edges[i]) & (path.index <= edges[i + 1])]
                if len(e) > 1 and len(b) > 1:
                    report["quarters"].append({"strategy": round(float(e.iloc[-1] / e.iloc[0] - 1), 4),
                                               "basket": round(float(b.iloc[-1] / b.iloc[0] - 1), 4)})
    curve = m.get("equity_curve")
    if market_fn is not None and curve and days > 400:
        eq = pd.Series([e for _, e in curve], index=[t for t, _ in curve])
        years = pd.to_datetime(eq.index, unit="s").year
        for y in sorted(set(years)):
            e = eq[years == y]
            if len(e) <= 24 * 20:
                continue
            mc = market_fn(int(e.index.min()), int(e.index.max()))
            if mc and mc.get("basket_return") is not None:
                report["years"].append({"year": int(y), "strategy": round(float(e.iloc[-1] / e.iloc[0] - 1), 4),
                                        "basket": round(float(mc["basket_return"]), 4), "pairs": int(mc["pairs"])})
    return problems, report


def format_report(report: dict) -> str:
    lines = [f"cost drag per year {report['cost_drag_per_year']:.1%} of equity, "
             f"{report['avg_fills_per_pair_per_day']:.2f} fills per pair per day, drawdown limit {report['drawdown_limit']:.1%}"]
    if report["basket_return"] is not None:
        lines.append(f"market: equal weight basket {report['basket_return']:+.1%} with max drawdown "
                     f"{report['basket_max_dd']:.1%}; exposure matched benchmark {report['exposure_matched_benchmark']:+.1%}; "
                     f"skill vs benchmark {report['skill_vs_benchmark']:+.1%} (informational, not a gate)")
    if report["quarters"]:
        lines.append("quarters (strategy / basket): " + ", ".join(
            f"{q['strategy']:+.1%} / {q['basket']:+.1%}" for q in report["quarters"]))
    if report.get("years"):
        most = max(y["pairs"] for y in report["years"])
        lines.append("by calendar year (strategy / basket): " + ", ".join(
            f"{y['year']} {y['strategy']:+.1%} / {y['basket']:+.1%}"
            + (f" ({y['pairs']} pairs)" if y["pairs"] < most else "") for y in report["years"]))
    if report.get("pair_days_at_fill_cap"):
        lines.append(f"the daily fill cap stopped a buy on {report['pair_days_at_fill_cap']} pair days")
    return "\n".join(lines)


def load_cached_candles(pairs: list[str]) -> dict[str, pd.DataFrame]:
    """History plus live for every pair."""
    return {p: data.load_all_candles(p) for p in pairs}


def format_metrics(m: dict) -> str:
    keys = ["strategy", "hypothesis", "start", "end", "days", "pairs", "bars", "final_equity",
            "total_return", "annualised_return", "annualised_vol", "sharpe", "max_drawdown", "n_trades",
            "trades_per_pair_per_day_avg", "trades_per_pair_per_day_max", "finished_trades",
            "closed_by_halt_or_error", "windows_with_no_finished_trade", "pair_days_at_fill_cap",
            "starved_share", "gross_pnl", "fees",
            "slippage", "net_pnl", "cost_coverage", "avg_gross_exposure"]
    return "\n".join(f"{k:>30}: {m.get(k)}" for k in keys)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/challenger1.yaml")
    ap.add_argument("--days", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--gate", action="store_true", help="also print exactly what the gate will say")
    args = ap.parse_args(argv)
    config.prepare()
    rcfg = config.risk_cfg()
    cfg = config.load_yaml(config.ROOT / args.config)
    candles = load_cached_candles(list(rcfg["pairs"]))
    m = run_backtest(candles, cfg, rcfg, max_days=args.days or rcfg["backtest_gate"]["max_days"])
    curve = m.pop("equity_curve")
    print(json.dumps(m, indent=2) if args.json else format_metrics(m))
    if args.gate:
        from .promote import market_context
        pairs = list(rcfg["pairs"])
        # the curve is stamped with candle open times and marked at their closes, an hour later
        market = market_context(curve[0][0], curve[-1][0] + 3600, pairs) if curve else None
        problems, report = plausibility({**m, "equity_curve": curve}, rcfg["backtest_gate"], market, rcfg["initial_cash"],
                                        market_fn=lambda a, b: market_context(a + 3600, b + 3600, pairs))
        print(format_report(report))
        print("gate: " + ("PASS" if not problems else "FAIL\n  - " + "\n  - ".join(problems)))
        if args.days and args.days != rcfg["backtest_gate"]["max_days"]:
            print(f"(the gate itself replays the last {rcfg['backtest_gate']['max_days']} days; "
                  f"this verdict is for {args.days})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
