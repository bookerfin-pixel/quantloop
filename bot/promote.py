"""Rule on challenger tests. PROTECTED.

    python -m bot.promote [--now <unix ts>]

Runs every hour after the accounts. For every slot whose test has run for
challenger.window_days, using only data from the test window (which the
hypothesis could not have been fitted to, because it did not exist yet):

  promoted  challenger net return > champion net return + min_return_edge
            AND challenger max drawdown <= max(max_dd_ratio * champion max drawdown, max_dd_floor)
            AND challenger placed >= min_trades fills
  killed    otherwise

Two early exits, both of which free a slot sooner and neither of which can
promote anything: a challenger whose drawdown from its window start exceeds
challenger.early_kill_drawdown is killed at once, and if two slots win in the
same hour only the stronger one is promoted, the other is restarted against
the new champion with a fresh window.

Promotion copies the winning slot's config into configs/champion.yaml and
starts the shadow (bot/shadow.py): the deposed config keeps running for one
more window and the promotion is reverted if it beats the new champion by the
same rule. Either way the slot's config is reset to the champion's, its account
is archived and restarted with fresh cash, and LEDGER.md gets the verdict with
the realised gross bps per round trip next to what the ledger entry predicted,
plus what the market did over the window (BTC, an equal weight basket of all
pairs, and the basket's realised vol) so a result can be read in context. The
champion account is never reset, so its equity curve is the one long record
of what this system has actually done.
"""
from __future__ import annotations

import argparse
import math
import re
import shutil
import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import config, data, shadow, slot

CHAMPION_HEADER = "# PROTECTED. Written only by bot/promote.py when a challenger wins.\n"


def window_metrics(name: str, start_ts: int, end_ts: int, start_equity: float | None) -> dict:
    adir = config.account_dir(name)
    eq_path, tr_path = adir / "equity.csv", adir / "trades.csv"
    out = {"return": None, "max_drawdown": None, "trades": 0, "bars": 0, "fees": 0.0,
           "gross_pnl": None, "traded_notional": 0.0, "realised_bps": None}
    if eq_path.exists():
        eq = pd.read_csv(eq_path)
        eq = eq[(eq["ts"] >= start_ts) & (eq["ts"] <= end_ts)]
        if len(eq):
            base = start_equity if start_equity else float(eq["equity"].iloc[0])
            series = eq["equity"].astype(float)
            out["return"] = float(series.iloc[-1] / base - 1)
            path = pd.concat([pd.Series([base]), series], ignore_index=True)
            out["max_drawdown"] = float((path / path.cummax() - 1).min())
            out["bars"] = int(len(eq))
            costs = float(eq["fees_paid"].iloc[-1] - eq["fees_paid"].iloc[0]
                          + eq["slippage_paid"].iloc[-1] - eq["slippage_paid"].iloc[0])
            out["fees"] = costs
            out["gross_pnl"] = float(series.iloc[-1] - base) + costs
    if tr_path.exists():
        tr = pd.read_csv(tr_path)
        tr = tr[(tr["ts"] >= start_ts) & (tr["ts"] <= end_ts)]
        out["trades"] = int(len(tr))
        out["traded_notional"] = float(tr["notional"].sum()) if len(tr) else 0.0
    if out["gross_pnl"] is not None and out["traded_notional"] > 0:
        # one round trip is a buy plus a sell, so half the traded notional
        out["realised_bps"] = out["gross_pnl"] / (out["traded_notional"] / 2) * 1e4
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
    limit = max(float(rules["max_dd_ratio"]) * champ_dd, float(rules.get("max_dd_floor", 0.0)))
    if chal_dd > limit:
        return "killed", (f"challenger max drawdown {chal_dd:.2%} exceeded the limit {limit:.2%} "
                          f"(the larger of {rules['max_dd_ratio']}x the champion's {champ_dd:.2%} and the "
                          f"{float(rules.get('max_dd_floor', 0.0)):.0%} floor) despite better return {edge:+.2%}")
    return "promoted", (f"challenger net return {chal['return']:+.2%} beat champion {champ['return']:+.2%} "
                        f"with max drawdown {chal_dd:.2%} vs {champ_dd:.2%}")


def early_kill(chal: dict, rules: dict) -> str | None:
    limit = float(rules.get("early_kill_drawdown", 0) or 0)
    if limit and chal["max_drawdown"] is not None and abs(chal["max_drawdown"]) > limit:
        return (f"challenger drew down {abs(chal['max_drawdown']):.2%} from its window start, past the "
                f"{limit:.0%} early kill limit; no need to wait for the window to end")
    return None


def market_context(start_ts: int, end_ts: int, pairs: list[str]) -> dict:
    """What the market did over a window: BTC return, equal weight basket
    return, basket realised vol (annualised from hourly basket returns)."""
    out = {"btc_return": None, "basket_return": None, "basket_vol": None, "pairs": 0}
    series = {}
    for p in pairs:
        df = data.load_all_candles(p)
        if not len(df):
            continue
        df = df[(df["time"] >= start_ts - 3600) & (df["time"] <= end_ts)]
        if len(df) < 2:
            continue
        series[p] = df.set_index("time")["close"].astype(float)
    if not series:
        return out
    rets = {p: float(sr.iloc[-1] / sr.iloc[0] - 1) for p, sr in series.items()}
    out["pairs"] = len(rets)
    out["basket_return"] = float(np.mean(list(rets.values())))
    if "BTC" in rets:
        out["btc_return"] = rets["BTC"]
    frame = pd.DataFrame(series).sort_index().ffill()
    hourly = frame.pct_change().mean(axis=1).dropna()
    if len(hourly) > 2:
        out["basket_vol"] = float(hourly.std() * math.sqrt(24 * 365))
    return out


def format_market(mc: dict) -> str:
    if not mc.get("pairs"):
        return "no candle data for the window"
    parts = []
    if mc["btc_return"] is not None:
        parts.append(f"BTC {mc['btc_return']:+.2%}")
    parts.append(f"equal weight basket of {mc['pairs']} pairs {mc['basket_return']:+.2%}")
    if mc["basket_vol"] is not None:
        parts.append(f"basket realised vol {mc['basket_vol']:.0%} annualised")
    return ", ".join(parts)


def expected_bps(hyp: str) -> float | None:
    if not config.LEDGER.exists():
        return None
    text = config.LEDGER.read_text()
    m = re.search(rf"## {re.escape(hyp)}\b.*?^- Expected gross bps per round trip:\s*([0-9.]+)", text, re.S | re.M)
    return float(m.group(1)) if m else None


def _fmt(d: dict, expected: float | None = None) -> str:
    if d["return"] is None:
        return "no data"
    gross = "n/a" if d.get("gross_pnl") is None else f"{d['gross_pnl']:.2f}"
    s = (f"return {d['return']:+.2%}, max DD {d['max_drawdown']:.2%}, {d['trades']} fills, "
         f"costs {d['fees']:.2f}, gross pnl {gross}")
    if d["realised_bps"] is not None:
        s += f", realised gross bps per round trip {d['realised_bps']:.0f}"
        if expected is not None:
            s += f" (ledger expected {expected:.0f})"
    return s


def update_ledger(hyp: str, verdict: str, reason: str, champ: dict, chal: dict,
                  start_ts: int, end_ts: int, slot_name: str, labels: tuple[str, str] = ("Champion", "Challenger"),
                  status_from: str = "testing", status_to: str | None = None) -> None:
    path = config.LEDGER
    text = path.read_text() if path.exists() else "# Ledger\n"
    status_to = verdict if status_to is None else status_to
    if verdict != "restarted" and status_to:
        pattern = re.compile(rf"(## {re.escape(hyp)}\b.*?\n- Status: ){status_from}", re.S)
        text, n = pattern.subn(rf"\g<1>{status_to}", text, count=1)
        if n == 0:
            print(f"[promote] warning: no 'Status: {status_from}' line found for {hyp} in LEDGER.md")
    try:
        market = format_market(market_context(start_ts, end_ts, list(config.risk_cfg()["pairs"])))
    except Exception as e:  # noqa: BLE001
        market = f"unavailable ({e})"
    block = (
        f"\n### Result {hyp}: {verdict}\n"
        f"- Slot: {slot_name}\n"
        f"- Window: {datetime.fromtimestamp(start_ts, timezone.utc):%Y-%m-%d} to "
        f"{datetime.fromtimestamp(end_ts, timezone.utc):%Y-%m-%d} ({(end_ts - start_ts) / 86400:.1f} days, prospective)\n"
        f"- Market: {market}\n"
        f"- {labels[0]}: {_fmt(champ)}\n"
        f"- {labels[1]}: {_fmt(chal, expected_bps(hyp))}\n"
        f"- Rule: {reason}\n"
    )
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


def apply(verdict: str, hyp: str, name: str, now: int | None = None, equities: dict[str, float] | None = None) -> None:
    if verdict == "promoted":
        deposed = config.account_cfg(config.CHAMPION)
        chal = config.account_cfg(name)
        config.dump_yaml(config.CONFIGS / "champion.yaml",
                         {"hypothesis": chal["hypothesis"], "strategy": chal["strategy"], "params": chal["params"]},
                         CHAMPION_HEADER)
        rcfg = config.risk_cfg()
        equities = equities or {}
        shadow.start(deposed, hyp, now or int(time.time()),
                     equities.get(config.CHAMPION, rcfg["initial_cash"]), rcfg["initial_cash"])
    config.write_challenger_from_champion(name)
    archive_slot(name, hyp)
    slot.reset(name)


def rule_on_shadow(now: int, rules: dict) -> None:
    """After a promotion's guard window: keep the promotion or revert it."""
    meta = shadow.load()
    if meta.get("status") != "active":
        return
    elapsed = (now - meta["started_at"]) / 86400
    if elapsed < float(rules["window_days"]):
        print(f"[promote] shadow {meta['hypothesis']} guarding {meta['replaced_by']}: day {elapsed:.1f} of {rules['window_days']}")
        return
    start = int(meta["started_at"])
    champ = window_metrics(config.CHAMPION, start, now, meta["start_equity"].get(config.CHAMPION))
    shad = window_metrics(config.SHADOW, start, now, meta["start_equity"].get(config.SHADOW))
    verdict, reason = decide(champ, shad, rules)   # "promoted" here means the shadow beat the champion
    promoted_hyp = meta["replaced_by"]
    if verdict == "promoted":
        reason = f"the deposed config beat the promoted one over the guard window: {reason}; promotion reverted"
        print(f"[promote] {promoted_hyp}: reverted — {reason}")
        update_ledger(promoted_hyp, "reverted", reason, champ, shad, start, now, "shadow",
                      labels=("Promoted champion", "Deposed config (shadow)"), status_from="promoted")
        old = config.account_cfg(config.SHADOW)
        config.dump_yaml(config.CONFIGS / "champion.yaml",
                         {"hypothesis": old["hypothesis"], "strategy": old["strategy"], "params": old["params"]},
                         CHAMPION_HEADER)
        shadow.stop("reverted")
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
    slot.save(name, meta)


def current_equities(now: int) -> dict[str, float]:
    out = {}
    for name in config.accounts():
        p = config.account_dir(name) / "equity.csv"
        if p.exists():
            eq = pd.read_csv(p)
            eq = eq[eq["ts"] <= now]
            if len(eq):
                out[name] = float(eq["equity"].iloc[-1])
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now", type=int, default=None)
    args = ap.parse_args(argv)
    config.prepare()
    now = args.now or int(time.time())
    rules = config.risk_cfg()["challenger"]
    verdicts: list[tuple[str, str, str, str]] = []   # (slot, hyp, verdict, reason)
    rule_on_shadow(now, rules)
    testing = [(n, slot.load(n)) for n in config.challengers() if slot.load(n)["status"] == "testing"]
    if not testing:
        print("[promote] no test running; nothing to rule on")
        return 0
    for name, meta in testing:
        start, hyp = int(meta["started_at"]), meta["hypothesis"]
        champ = window_metrics(config.CHAMPION, start, now, meta["start_equity"].get(config.CHAMPION))
        chal = window_metrics(name, start, now, meta["start_equity"].get(name))
        reason = early_kill(chal, rules)
        if reason:
            verdicts.append((name, hyp, "killed", reason))
            continue
        elapsed = (now - start) / 86400
        if elapsed < float(rules["window_days"]):
            print(f"[promote] {name}: {hyp} on day {elapsed:.1f} of {rules['window_days']}; no verdict yet")
            continue
        verdict, reason = decide(champ, chal, rules)
        verdicts.append((name, hyp, verdict, reason))

    # strongest winner first, so a second winner in the same hour is restarted, not promoted over it
    def strength(v):
        name, meta = v[0], slot.load(v[0])
        m = window_metrics(name, int(meta["started_at"]), now, meta["start_equity"].get(name))
        return m["return"] or -1e9
    verdicts.sort(key=lambda v: (v[2] != "promoted", -strength(v)))

    promoted_hyp: str | None = None
    for name, hyp, verdict, reason in verdicts:
        meta = slot.load(name)
        start = int(meta["started_at"])
        champ = window_metrics(config.CHAMPION, start, now, meta["start_equity"].get(config.CHAMPION))
        chal = window_metrics(name, start, now, meta["start_equity"].get(name))
        if verdict == "promoted" and promoted_hyp is not None:
            reason = (f"beat the old champion ({reason}) but {promoted_hyp} won by more this hour and was promoted; "
                      f"restarted against the new champion with a fresh window")
            print(f"[promote] {name}: {hyp}: restarted — {reason}")
            update_ledger(hyp, "restarted", reason, champ, chal, start, now, name)
            restart(name, now, current_equities(now), promoted_hyp)
            continue
        print(f"[promote] {name}: {hyp}: {verdict} — {reason}")
        update_ledger(hyp, verdict, reason, champ, chal, start, now, name)
        apply(verdict, hyp, name, now, current_equities(now))
        if verdict == "promoted":
            promoted_hyp = hyp
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
