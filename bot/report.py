"""Write state/summary.md, the first thing the agent reads each day. PROTECTED."""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone

import pandas as pd

from . import config, data, slot


def _ts(t: int | float | None) -> str:
    if t is None:
        return "never"
    return datetime.fromtimestamp(int(t), timezone.utc).strftime("%Y-%m-%d %H:%M") + "Z"


def _pct(x) -> str:
    return "n/a" if x is None else f"{x:+.2%}"


def account_section(name: str, now: int) -> str:
    adir = config.account_dir(name)
    cfg = config.account_cfg(name)
    lines = [f"## {name}: {cfg['strategy']} ({cfg['hypothesis']})", ""]
    lines.append("params: " + json.dumps(cfg["params"], sort_keys=True))
    acct_path = adir / "account.json"
    if not acct_path.exists():
        lines.append("no runs yet")
        return "\n".join(lines) + "\n"
    st = json.loads(acct_path.read_text())
    eq = pd.read_csv(adir / "equity.csv") if (adir / "equity.csv").exists() else pd.DataFrame()
    tr = pd.read_csv(adir / "trades.csv") if (adir / "trades.csv").exists() else pd.DataFrame()
    if len(eq):
        e = eq["equity"].astype(float)
        last = float(e.iloc[-1])
        initial = float(st["initial_cash"])
        since = st["created_at"]
        dd = float((e / e.cummax() - 1).min())
        def ret_over(hours):
            cut = now - hours * 3600
            sub = eq[eq["ts"] >= cut]
            if len(sub) < 2:
                return None
            return float(sub["equity"].iloc[-1] / sub["equity"].iloc[0] - 1)
        costs = float(st["fees_paid"] + st["slippage_paid"])
        gross = (last - initial) + costs
        lines += [
            "",
            f"- equity {last:,.2f} (started {initial:,.0f} at {_ts(since)}), net {_pct(last / initial - 1)} since start",
            f"- 24h {_pct(ret_over(24))}, 7d {_pct(ret_over(24 * 7))}, 30d {_pct(ret_over(24 * 30))}, max drawdown {dd:.2%}",
            f"- fills {st['n_trades']} total, {int((tr['ts'] >= now - 7 * 86400).sum()) if len(tr) else 0} in the last 7d",
            f"- costs {costs:,.2f} (fees {st['fees_paid']:,.2f} + slippage {st['slippage_paid']:,.2f}); "
            f"gross pnl {gross:,.2f}; cost coverage {'n/a' if costs == 0 else f'{gross / costs:.2f}'}",
            f"- cash {st['cash']:,.2f}; positions: "
            + (", ".join(f"{p} {q:.6g}" for p, q in st["positions"].items()) or "none"),
            f"- last run {_ts(st['last_run_ts'])}; halted today: {st['halted_day'] == datetime.fromtimestamp(now, timezone.utc).strftime('%Y-%m-%d')}",
        ]
    dec_path = adir / "decisions.csv"
    if dec_path.exists():
        dec = pd.read_csv(dec_path).tail(18)
        lines += ["", "last decisions (newest last):", ""]
        for _, r in dec.iterrows():
            reason = str(r["reason"])
            if len(reason) > 140:
                reason = reason[:137] + "..."
            lines.append(f"- {_ts(r['ts'])} {r['pair']} {r['action']} target {r['target_weight']:.2f} "
                         f"(held {r['current_weight']:.2f}) — {reason}")
    if len(tr):
        lines += ["", "last fills:", ""]
        for _, r in tr.tail(8).iterrows():
            lines.append(f"- {_ts(r['ts'])} {r['side']} {r['pair']} {r['notional']:,.0f} @ {r['price']:.6g} "
                         f"fee {r['fee']:.2f} slip {r['slippage_cost']:.2f}")
    return "\n".join(lines) + "\n"


def data_section(pairs: list[str], now: int) -> str:
    lines = ["## Data", ""]
    for p in pairs:
        df = data.load_candles(p)
        if not len(df):
            lines.append(f"- {p}: no candles")
            continue
        t = df["time"].astype(int)
        cutoff = now - 7 * 86400
        recent = t[t >= cutoff]
        # hourly slots between the cutoff and the last closed candle; only meaningful once
        # the cache reaches back a full week
        expected = int((t.max() - cutoff) // 3600) + 1 if len(t) and t.min() <= cutoff else len(recent)
        gaps = max(0, expected - len(recent))
        lines.append(f"- {p}: {len(df)} candles, {_ts(t.min())} to {_ts(t.max())}, "
                     f"missing hours in last 7d: {gaps}")
    return "\n".join(lines) + "\n"


def test_section(now: int) -> str:
    meta = slot.load()
    lines = ["## Challenger slot", "", f"- {slot.describe(now)}"]
    if meta["status"] == "testing":
        from .promote import window_metrics
        champ = window_metrics("champion", meta["started_at"], now, meta["start_equity"].get("champion"))
        chal = window_metrics("challenger", meta["started_at"], now, meta["start_equity"].get("challenger"))
        lines.append(f"- so far: champion {_pct(champ['return'])} (DD {champ['max_drawdown'] or 0:.2%}, "
                     f"{champ['trades']} fills) vs challenger {_pct(chal['return'])} "
                     f"(DD {chal['max_drawdown'] or 0:.2%}, {chal['trades']} fills)")
        lines.append("- this is an interim reading; only the verdict at the end of the window counts")
    return "\n".join(lines) + "\n"


def build(now: int | None = None) -> str:
    now = now or int(time.time())
    rcfg = config.risk_cfg()
    parts = [f"# quantloop summary — generated {_ts(now)}", "",
             f"Cost model: fee {rcfg['fee_bps']} bps + slippage {rcfg['slippage_bps']} bps per side "
             f"(~{2 * (rcfg['fee_bps'] + rcfg['slippage_bps'])} bps per round trip). "
             f"Pairs: {', '.join(rcfg['pairs'])}. Paper only.", ""]
    parts.append(test_section(now))
    for name in config.ACCOUNTS:
        parts.append(account_section(name, now))
    parts.append(data_section(list(rcfg["pairs"]), now))
    return "\n".join(parts)


def main() -> int:
    text = build()
    out = config.STATE / "summary.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"[report] wrote {out} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
