"""Gate 3: the challenger config must load, run over cached candles with the
live cost model, and clear pre registered plausibility bounds from
configs/risk.yaml:backtest_gate. Run from the PR checkout:

    python <base>/gate/backtest_gate.py

This is a floor, not a target. Passing it says "not obviously broken and not
paying more in costs than it earns in sample". Only the prospective
challenger test says anything about edge.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.getcwd())

from bot import backtest, config  # noqa: E402


def main() -> int:
    rcfg = config.risk_cfg()
    rules = rcfg["backtest_gate"]
    try:
        cfg = config.account_cfg("challenger")
    except Exception as e:  # noqa: BLE001
        print(f"GATE FAILED: configs/challenger.yaml does not load: {e}")
        return 1
    candles = backtest.load_cached_candles(list(rcfg["pairs"]))
    have = min((len(df) for df in candles.values()), default=0)
    if have < rules["min_days"] * 24:
        print(f"GATE FAILED: only {have} cached candles for the thinnest pair; need {rules['min_days']} days")
        return 1
    try:
        m = backtest.run_backtest(candles, cfg, rcfg, max_days=rules["max_days"])
    except Exception as e:  # noqa: BLE001
        print(f"GATE FAILED: backtest raised {type(e).__name__}: {e}")
        return 1
    m.pop("equity_curve", None)
    print(backtest.format_metrics(m))
    problems = []
    if m["n_trades"] == 0:
        problems.append("strategy placed no trades in the backtest window, so it cannot be evaluated")
    if m["cost_coverage"] is not None and m["cost_coverage"] < rules["min_cost_coverage"]:
        problems.append(f"cost coverage {m['cost_coverage']} below {rules['min_cost_coverage']}: "
                        f"gross pnl {m['gross_pnl']} does not cover costs {m['fees'] + m['slippage']:.2f}")
    if m["gross_pnl"] <= 0 and m["n_trades"] > 0:
        problems.append(f"gross pnl {m['gross_pnl']} is not positive even before costs")
    if m["max_drawdown"] < -rules["max_drawdown"]:
        problems.append(f"max drawdown {m['max_drawdown']:.2%} worse than {-rules['max_drawdown']:.0%}")
    if m["trades_per_pair_per_day_max"] > rules["max_trades_per_pair_per_day"]:
        problems.append(f"{m['trades_per_pair_per_day_max']} fills in one pair in one day exceeds "
                        f"{rules['max_trades_per_pair_per_day']}; that is a costs treadmill, not a strategy")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write("### Backtest gate\n\n```\n" + backtest.format_metrics(m) + "\n```\n")
            if problems:
                f.write("\n**Failed:**\n" + "".join(f"- {p}\n" for p in problems))
    if problems:
        print("\nGATE FAILED: backtest plausibility")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nbacktest gate passed")
    print(json.dumps({k: v for k, v in m.items() if k != "equity_curve"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
