"""Rule on a finished challenger test. PROTECTED.

    python -m bot.promote [--now <unix ts>]

Runs every hour after the accounts. Does nothing until the challenger has run
for challenger.window_days. Then, using only data from the test window (which
the hypothesis could not have been fitted to, because it did not exist yet):

  promoted  challenger net return > champion net return + min_return_edge
            AND challenger max drawdown <= max_dd_ratio * champion max drawdown
            AND challenger placed >= min_trades fills
  killed    otherwise

Promotion copies configs/challenger.yaml into configs/champion.yaml. Either
way the challenger config is reset to the champion's, the challenger account
is archived and restarted with fresh cash, and LEDGER.md gets the verdict.
The champion account is never reset, so its equity curve is the one long
record of what this system has actually done.
"""
from __future__ import annotations

import argparse
import re
import shutil
import time
from datetime import datetime, timezone

import pandas as pd

from . import config, slot

CHAMPION_HEADER = "# PROTECTED. Written only by bot/promote.py when a challenger wins.\n"
CHALLENGER_HEADER = ("# The agent edits this file. When it differs from champion.yaml the bot starts a\n"
                     "# prospective test automatically. `hypothesis` must match the newest entry in LEDGER.md.\n")


def window_metrics(name: str, start_ts: int, end_ts: int, start_equity: float | None) -> dict:
    adir = config.account_dir(name)
    eq_path, tr_path = adir / "equity.csv", adir / "trades.csv"
    out = {"return": None, "max_drawdown": None, "trades": 0, "bars": 0, "fees": 0.0}
    if eq_path.exists():
        eq = pd.read_csv(eq_path)
        eq = eq[(eq["ts"] >= start_ts) & (eq["ts"] <= end_ts)]
        if len(eq):
            base = start_equity if start_equity else float(eq["equity"].iloc[0])
            series = eq["equity"].astype(float)
            out["return"] = float(series.iloc[-1] / base - 1)
            running = pd.concat([pd.Series([base]), series]).cummax()
            out["max_drawdown"] = float((pd.concat([pd.Series([base]), series]) / running - 1).min())
            out["bars"] = int(len(eq))
            out["fees"] = float(eq["fees_paid"].iloc[-1] - eq["fees_paid"].iloc[0]
                                + eq["slippage_paid"].iloc[-1] - eq["slippage_paid"].iloc[0])
    if tr_path.exists():
        tr = pd.read_csv(tr_path)
        out["trades"] = int(((tr["ts"] >= start_ts) & (tr["ts"] <= end_ts)).sum())
    return out


def decide(champ: dict, chal: dict, rules: dict) -> tuple[str, str]:
    if chal["return"] is None or champ["return"] is None:
        return "killed", "no equity data for the window"
    if chal["trades"] < int(rules["min_trades"]):
        return "killed", (f"challenger made {chal['trades']} fills, fewer than the {rules['min_trades']} "
                          f"needed for a verdict; a strategy that does not trade cannot be judged")
    edge = chal["return"] - champ["return"]
    if edge <= float(rules["min_return_edge"]):
        return "killed", (f"challenger net return {chal['return']:+.2%} did not beat champion "
                          f"{champ['return']:+.2%} by more than {rules['min_return_edge']:.2%}")
    champ_dd = abs(champ["max_drawdown"] or 0.0)
    chal_dd = abs(chal["max_drawdown"] or 0.0)
    limit = float(rules["max_dd_ratio"]) * max(champ_dd, 0.01)
    if chal_dd > limit:
        return "killed", (f"challenger max drawdown {chal_dd:.2%} exceeded {rules['max_dd_ratio']}x the "
                          f"champion's {champ_dd:.2%} (limit {limit:.2%}) despite better return {edge:+.2%}")
    return "promoted", (f"challenger net return {chal['return']:+.2%} beat champion {champ['return']:+.2%} "
                        f"with max drawdown {chal_dd:.2%} vs {champ_dd:.2%}")


def update_ledger(hyp: str, verdict: str, reason: str, champ: dict, chal: dict, start_ts: int, end_ts: int) -> None:
    path = config.LEDGER
    text = path.read_text() if path.exists() else "# Ledger\n"
    # flip the status line inside the hypothesis entry, if present
    pattern = re.compile(rf"(## {re.escape(hyp)}\b.*?\n- Status: )testing", re.S)
    text, n = pattern.subn(rf"\g<1>{verdict}", text, count=1)
    if n == 0:
        print(f"[promote] warning: no 'Status: testing' line found for {hyp} in LEDGER.md")
    fmt = lambda d: (f"return {d['return']:+.2%}, max DD {d['max_drawdown']:.2%}, "  # noqa: E731
                     f"{d['trades']} fills, costs {d['fees']:.2f}") if d["return"] is not None else "no data"
    block = (
        f"\n### Result {hyp}: {verdict}\n"
        f"- Window: {datetime.fromtimestamp(start_ts, timezone.utc):%Y-%m-%d} to "
        f"{datetime.fromtimestamp(end_ts, timezone.utc):%Y-%m-%d} ({(end_ts - start_ts) / 86400:.1f} days, prospective)\n"
        f"- Champion: {fmt(champ)}\n"
        f"- Challenger: {fmt(chal)}\n"
        f"- Rule: {reason}\n"
    )
    if "\n## Results" not in text:
        text = text.rstrip("\n") + "\n\n## Results\n"
    text = text.rstrip("\n") + "\n" + block
    path.write_text(text)


def archive_challenger(hyp: str) -> None:
    adir = config.account_dir("challenger")
    dest = config.ARCHIVE / f"{hyp}_{datetime.now(timezone.utc):%Y%m%d%H%M}"
    dest.mkdir(parents=True, exist_ok=True)
    for fname in ("account.json", "decisions.csv", "trades.csv", "equity.csv"):
        src = adir / fname
        if src.exists():
            shutil.move(str(src), str(dest / fname))


def apply(verdict: str, hyp: str) -> None:
    champ = config.account_cfg("champion")
    chal = config.account_cfg("challenger")
    if verdict == "promoted":
        new_champ = {"hypothesis": chal["hypothesis"], "strategy": chal["strategy"], "params": chal["params"]}
        config.dump_yaml(config.CONFIGS / "champion.yaml", new_champ, CHAMPION_HEADER)
        champ = new_champ
    reset = {"hypothesis": champ["hypothesis"], "strategy": champ["strategy"], "params": champ["params"]}
    config.dump_yaml(config.CONFIGS / "challenger.yaml", reset, CHALLENGER_HEADER)
    archive_challenger(hyp)
    slot.save({"status": "idle", "hypothesis": None, "started_at": None, "start_equity": {}})


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now", type=int, default=None)
    args = ap.parse_args(argv)
    now = args.now or int(time.time())
    meta = slot.load()
    if meta["status"] != "testing":
        print("[promote] slot idle; nothing to rule on")
        return 0
    rules = config.risk_cfg()["challenger"]
    elapsed = (now - meta["started_at"]) / 86400
    if elapsed < float(rules["window_days"]):
        print(f"[promote] {meta['hypothesis']} on day {elapsed:.1f} of {rules['window_days']}; no verdict yet")
        return 0
    start, hyp = int(meta["started_at"]), meta["hypothesis"]
    champ = window_metrics("champion", start, now, meta["start_equity"].get("champion"))
    chal = window_metrics("challenger", start, now, meta["start_equity"].get("challenger"))
    verdict, reason = decide(champ, chal, rules)
    print(f"[promote] {hyp}: {verdict} — {reason}")
    update_ledger(hyp, verdict, reason, champ, chal, start, now)
    apply(verdict, hyp)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
