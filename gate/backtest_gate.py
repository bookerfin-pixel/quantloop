"""Gate 3: the slot config a PR changed must load and run over the last year
of history with the live cost model, and clear the regime independent sanity
bounds in configs/risk.yaml:backtest_gate. Run from the PR checkout:

    python <base>/gate/backtest_gate.py

What this is: a floor against the obviously broken, and against fee
treadmills. What it is not: a judgement of edge. The in sample skill figure
(net return against the exposure matched basket, quarter by quarter) is
printed for the ledger entry and never blocks. Alpha is judged in the
prospective challenger window.

A PR that changes no slot config has nothing to backtest and passes this
step without running one. (An earlier version fell back to slot 1 here and
re-judged a running test on every notes only PR; that was a bug, found by
the agent on 2026-09-18 and fixed on 2026-09-20.)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.getcwd())

from bot import backtest, config  # noqa: E402
from bot.promote import market_context  # noqa: E402


def slot_from_paths(paths: list[str]) -> str | None:
    for path in paths:
        m = re.match(r"configs/(challenger\d+)\.yaml$", path.strip())
        if m:
            return m.group(1)
    return None


def changed_slot() -> str | None:
    """The slot this PR changed (from the diff against main), or None."""
    try:
        out = subprocess.run(["git", "diff", "--name-only", "origin/main...HEAD"], check=True,
                             capture_output=True, text=True).stdout.splitlines()
    except Exception:  # noqa: BLE001
        out = []
    return slot_from_paths(out)


def main() -> int:
    config.prepare()
    rcfg = config.risk_cfg()
    rules = rcfg["backtest_gate"]
    name = changed_slot()
    if name is None:
        print("no slot config changed; backtest gate not required")
        return 0
    try:
        cfg = config.account_cfg(name)
    except Exception as e:  # noqa: BLE001
        print(f"GATE FAILED: configs/{name}.yaml does not load: {e}")
        return 1
    print(f"backtesting configs/{name}.yaml ({cfg['hypothesis']})")
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
    curve = m.get("equity_curve") or []
    try:
        market = market_context(curve[0][0], curve[-1][0], list(rcfg["pairs"])) if curve else None
    except Exception as e:  # noqa: BLE001
        print(f"market context unavailable ({e}); drawdown limit falls back to the absolute floor")
        market = None
    problems, report = backtest.plausibility(m, rules, market, rcfg["initial_cash"])
    m.pop("equity_curve", None)
    metrics_txt = backtest.format_metrics(m)
    report_txt = backtest.format_report(report)
    print(metrics_txt)
    print(report_txt)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(f"### Backtest gate: configs/{name}.yaml ({cfg['hypothesis']})\n\n```\n{metrics_txt}\n\n{report_txt}\n```\n")
            if problems:
                f.write("\n**Failed:**\n" + "".join(f"- {p}\n" for p in problems))
    if problems:
        print("\nGATE FAILED: sanity bounds")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nbacktest gate passed")
    print(json.dumps({**m, **{k: v for k, v in report.items() if k != "quarters"}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
