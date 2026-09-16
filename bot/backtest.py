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
from .run import step

HOURS_PER_YEAR = 24 * 365


def warmup_hours(params: dict, floor: int = 48) -> int:
    hours = [int(v) for k, v in params.items() if k.endswith("_hours") and isinstance(v, (int, float))]
    return max(hours + [floor]) + 2


def run_backtest(candles: dict[str, pd.DataFrame], cfg: dict, rcfg: dict,
                 max_days: int | None = None, name: str = "backtest") -> dict:
    fn = strategy.get(cfg["strategy"])
    frames = {p: df.sort_values("time").reset_index(drop=True) for p, df in candles.items() if len(df)}
    if not frames:
        raise ValueError("no candle data")
    common = set.intersection(*[set(df["time"].astype(int)) for df in frames.values()])
    times = sorted(common)
    hist = int(rcfg.get("history_hours", 720))
    warm = warmup_hours(cfg["params"])
    if max_days:
        keep = max_days * 24 + warm + 1
        times = times[-keep:]
    if len(times) < warm + 24:
        raise ValueError(f"need at least {warm + 24} aligned candles, have {len(times)}")
    idx = {p: df.set_index("time") for p, df in frames.items()}
    aligned = {p: idx[p].loc[times].reset_index() for p in frames}

    acct = paper.PaperAccount(name, rcfg["initial_cash"], rcfg["fee_bps"], rcfg["slippage_bps"])
    equity_curve, fills_all = [], []
    trades_per_pair_day: dict[tuple[str, str], int] = defaultdict(int)
    exposure = []
    for i in range(warm, len(times) - 1):
        window = {p: aligned[p].iloc[max(0, i + 1 - hist): i + 1] for p in aligned}
        next_open = {p: float(aligned[p]["open"].iloc[i + 1]) for p in aligned}
        ts_fill = int(times[i + 1])
        _, fills, _ = step(acct, cfg, fn, window, next_open, ts_fill, rcfg)
        for f in fills:
            fills_all.append(f)
            trades_per_pair_day[(f.pair, datetime.fromtimestamp(ts_fill, timezone.utc).strftime("%Y-%m-%d"))] += 1
        next_close = {p: float(aligned[p]["close"].iloc[i + 1]) for p in aligned}
        eq = acct.equity(next_close)
        equity_curve.append((ts_fill, eq))
        exposure.append(acct.gross_exposure(next_close) / eq if eq > 0 else 0.0)

    eq = pd.Series([e for _, e in equity_curve], index=[t for t, _ in equity_curve])
    rets = eq.pct_change().dropna()
    total_return = float(eq.iloc[-1] / rcfg["initial_cash"] - 1)
    ann_vol = float(rets.std() * math.sqrt(HOURS_PER_YEAR)) if len(rets) > 1 else float("nan")
    ann_ret = float(rets.mean() * HOURS_PER_YEAR) if len(rets) else float("nan")
    sharpe = ann_ret / ann_vol if ann_vol and ann_vol > 0 else float("nan")
    running_max = eq.cummax()
    max_dd = float((eq / running_max - 1).min()) if len(eq) else 0.0
    last_prices = {p: float(aligned[p]["close"].iloc[-1]) for p in aligned}
    gross = acct.gross_pnl(last_prices)
    costs = acct.total_costs()
    days = (times[-1] - times[warm]) / 86400
    n_pairs = len(aligned)
    max_tpd = max(trades_per_pair_day.values()) if trades_per_pair_day else 0
    return {
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
        "gross_pnl": round(gross, 2),
        "fees": round(acct.state["fees_paid"], 2),
        "slippage": round(acct.state["slippage_paid"], 2),
        "net_pnl": round(gross - costs, 2),
        "cost_coverage": round(gross / costs, 2) if costs > 0 else None,
        "avg_gross_exposure": round(float(np.mean(exposure)), 3) if exposure else 0.0,
        "equity_curve": equity_curve,
    }


def load_cached_candles(pairs: list[str]) -> dict[str, pd.DataFrame]:
    return {p: data.load_candles(p) for p in pairs}


def format_metrics(m: dict) -> str:
    keys = ["strategy", "hypothesis", "start", "end", "days", "pairs", "bars", "final_equity",
            "total_return", "annualised_return", "annualised_vol", "sharpe", "max_drawdown", "n_trades",
            "trades_per_pair_per_day_avg", "trades_per_pair_per_day_max", "gross_pnl", "fees",
            "slippage", "net_pnl", "cost_coverage", "avg_gross_exposure"]
    return "\n".join(f"{k:>28}: {m.get(k)}" for k in keys)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/challenger1.yaml")
    ap.add_argument("--days", type=int, default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    config.prepare()
    rcfg = config.risk_cfg()
    cfg = config.load_yaml(config.ROOT / args.config)
    candles = load_cached_candles(list(rcfg["pairs"]))
    m = run_backtest(candles, cfg, rcfg, max_days=args.days or rcfg["backtest_gate"]["max_days"])
    m.pop("equity_curve")
    print(json.dumps(m, indent=2) if args.json else format_metrics(m))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
