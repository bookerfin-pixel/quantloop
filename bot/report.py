"""Write state/summary.md, the first thing the agent reads each day. PROTECTED."""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone

import pandas as pd

from . import config, data, shadow, slot


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
    st.setdefault("name", name)
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
        lines += ["", "by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):", ""]
        lines += per_pair_lines(tr, st)
        lines += ["", "last fills:", ""]
        for _, r in tr.tail(8).iterrows():
            spread = r.get("half_spread_bps", "")
            lines.append(f"- {_ts(r['ts'])} {r['side']} {r['pair']} {r['notional']:,.0f} @ {r['price']:.6g} "
                         f"fee {r['fee']:.2f} slip {r['slippage_cost']:.2f}"
                         + (f" (half spread {float(spread):.1f} bps)" if spread not in ("", None) and spread == spread else ""))
    return "\n".join(lines) + "\n"


def per_pair_lines(tr: pd.DataFrame, st: dict) -> list[str]:
    """Fills, traded notional, realised plus open gross pnl and gross bps per round
    trip for every pair the account has touched. Open positions are marked at the
    account's last decision price."""
    out = []
    last_price = _last_prices(st)
    for pair, g in tr.groupby("pair"):
        buys = g[g["side"] == "buy"]
        sells = g[g["side"] == "sell"]
        bought_qty, sold_qty = float(buys["qty"].sum()), float(sells["qty"].sum())
        # cash flow at reference prices (gross of costs): sells bring in ref*qty, buys pay ref*qty
        flow = float((sells["ref_price"] * sells["qty"]).sum() - (buys["ref_price"] * buys["qty"]).sum())
        open_qty = float(st.get("positions", {}).get(pair, 0.0))
        mark = last_price.get(pair)
        gross = flow + (open_qty * mark if mark is not None else 0.0)
        traded = float(g["notional"].sum())
        bps = gross / (traded / 2) * 1e4 if traded > 0 else float("nan")
        spread = g["half_spread_bps"].astype(float).replace(0, float("nan")).mean() if "half_spread_bps" in g else float("nan")
        holding = ""
        if open_qty > 0:
            holding = f", open {open_qty:.6g}"
        out.append(f"- {pair}: {len(g)} fills ({len(buys)} buy / {len(sells)} sell), traded {traded:,.0f}, "
                   f"gross pnl {gross:+,.2f}, {bps:+.0f} bps per round trip"
                   + (f", avg half spread {spread:.1f} bps" if spread == spread else "") + holding)
    return out


def _last_prices(st: dict) -> dict[str, float]:
    """Last decision price per pair, from the account's decisions log."""
    adir = config.account_dir(st.get("name", ""))
    p = adir / "decisions.csv"
    if not p.exists():
        return {}
    dec = pd.read_csv(p)
    if not len(dec):
        return {}
    last = dec.sort_values("ts").groupby("pair")["price"].last()
    return {k: float(v) for k, v in last.items()}


def data_section(pairs: list[str], now: int) -> str:
    lines = ["## Data", "", "live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):", ""]
    spreads = recent_spreads(now)
    for p in pairs:
        df = data.load_candles(p)
        hist = data.load_history(p)
        if not len(df):
            lines.append(f"- {p}: no live candles" + (f"; history {len(hist)} candles" if len(hist) else ""))
            continue
        t = df["time"].astype(int)
        cutoff = now - 7 * 86400
        recent = t[t >= cutoff]
        # hourly slots between the cutoff and the last closed candle; only meaningful once
        # the cache reaches back a full week
        expected = int((t.max() - cutoff) // 3600) + 1 if len(t) and t.min() <= cutoff else len(recent)
        gaps = max(0, expected - len(recent))
        hist_txt = (f"; history {len(hist)} candles from {_ts(int(hist['time'].min()))[:10]}" if len(hist)
                    else "; history: none yet")
        sp = spreads.get(p)
        sp_txt = f"; avg half spread last 7d {sp:.1f} bps" if sp is not None else ""
        lines.append(f"- {p}: live {len(df)} candles, {_ts(t.min())} to {_ts(t.max())}, "
                     f"missing hours in last 7d: {gaps}{hist_txt}{sp_txt}")
    return "\n".join(lines) + "\n"


def recent_spreads(now: int) -> dict[str, float]:
    """Average observed half spread per pair over the last 7 days, from the
    champion's decisions log (every run records it for every pair)."""
    p = config.account_dir(config.CHAMPION) / "decisions.csv"
    if not p.exists():
        return {}
    dec = pd.read_csv(p)
    if "half_spread_bps" not in dec.columns or not len(dec):
        return {}
    dec = dec[dec["ts"] >= now - 7 * 86400]
    dec = dec[pd.to_numeric(dec["half_spread_bps"], errors="coerce") > 0]
    if not len(dec):
        return {}
    return {k: float(v) for k, v in dec.groupby("pair")["half_spread_bps"].mean().items()}


def test_section(now: int) -> str:
    from .promote import compare_on, format_market, market_context, paired
    pairs = list(config.risk_cfg()["pairs"])
    rules = config.risk_cfg()["challenger"]
    lines = ["## Challenger slots", ""]
    any_testing = False
    for name in config.challengers():
        meta = slot.load(name)
        lines.append(f"- {slot.describe_one(name, now)}")
        if meta["status"] == "testing":
            any_testing = True
            champ, chal, _ = paired(config.CHAMPION, name, int(meta["started_at"]), now, meta["start_equity"], rules)
            lines.append(f"  so far: champion {_pct(champ['return'])} (DD {champ['max_drawdown'] or 0:.2%}, "
                         f"{champ['trades']} fills) vs {name} {_pct(chal['return'])} "
                         f"(DD {chal['max_drawdown'] or 0:.2%}, {chal['trades']} fills)")
            if champ.get("skill") is not None and chal.get("skill") is not None:
                t_txt = f", daily edge t {chal['edge_t']:+.1f} over {chal['edge_days']} days" \
                    if chal.get("edge_t") is not None else ""
                lines.append(f"  skill (net return minus the basket at the same average exposure): champion "
                             f"{champ['skill']:+.2%} at {champ['avg_exposure']:.2f} vs {name} {chal['skill']:+.2%} at "
                             f"{chal['avg_exposure']:.2f}; the rule compares on {compare_on(rules, champ, chal)}{t_txt}")
            try:
                lines.append(f"  market over the window: {format_market(market_context(meta['started_at'], now, pairs))}")
            except Exception as e:  # noqa: BLE001
                lines.append(f"  market over the window: unavailable ({e})")
    free = slot.free_slots()
    lines.append(f"- free slots: {', '.join(free) if free else 'none'}")
    lines.append(f"- {shadow.describe(now)}")
    if any_testing:
        lines.append("- interim readings are not verdicts; only the end of window rule counts")
    return "\n".join(lines) + "\n"


def build(now: int | None = None) -> str:
    now = now or int(time.time())
    rcfg = config.risk_cfg()
    parts = [f"# quantloop summary — generated {_ts(now)}", "",
             f"Cost model: fee {rcfg['fee_bps']} bps + slippage {rcfg['slippage_bps']} bps per side "
             f"(~{2 * (rcfg['fee_bps'] + rcfg['slippage_bps'])} bps per round trip). "
             f"Pairs: {', '.join(rcfg['pairs'])}. Paper only.", ""]
    parts.append(test_section(now))
    for name in config.accounts():
        parts.append(account_section(name, now))
    parts.append(data_section(list(rcfg["pairs"]), now))
    return "\n".join(parts)


def main() -> int:
    config.prepare()
    text = build()
    out = config.STATE / "summary.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"[report] wrote {out} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
