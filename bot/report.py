"""Write state/summary.md, the first thing the agent reads each day. PROTECTED."""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone

import pandas as pd

from . import config, data, shadow, slot
from .run import REPLAYED


def _ts(t: int | float | None) -> str:
    if t is None:
        return "never"
    return datetime.fromtimestamp(int(t), timezone.utc).strftime("%Y-%m-%d %H:%M") + "Z"


def _pct(x) -> str:
    """A return as a signed percentage; one too small to show is not printed as "-0.00%"."""
    return "n/a" if x is None else f"{0.0 if abs(x) < 5e-5 else x:+.2%}"


def _dd(x) -> str:
    """A drawdown as a percentage (none on record reads as none)."""
    x = float(x or 0.0)
    return f"{0.0 if abs(x) < 5e-5 else x:.2%}"


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
    # The folder is the account's identity. challenger1's file still said
    # "challenger" from before the slots were numbered, so its open positions
    # were marked from a decisions log that does not exist and counted as zero
    # (found by the agent on 2026-10-04: DOGE at -19,990 bps per round trip).
    st["name"] = name
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
        out.append(f"- {pair}: {len(g)} fill{'' if len(g) == 1 else 's'} ({len(buys)} buy / {len(sells)} sell), "
                   f"traded {traded:,.0f}, "
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


def runs_section(now: int) -> str:
    """Whether the hourly loop itself ran. The Data section cannot show this:
    the venue backfills candles, so every candle can be there while most hourly
    runs never happened. GitHub dropped 26 of 40 runs from 2026-10-03 and the
    daily review, reading candle gaps, reported "no missing hours" (caught by
    the weekly digest). Every account runs in the same job, so the champion's
    record stands for all of them."""
    lines = ["## Runs", ""]
    adir = config.account_dir(config.CHAMPION)
    if not (adir / "equity.csv").exists():
        return "\n".join(lines + ["- no hourly run on record yet"]) + "\n"
    ts = pd.read_csv(adir / "equity.csv")["ts"].astype(int)
    if not len(ts):
        return "\n".join(lines + ["- no hourly run on record yet"]) + "\n"
    replayed: set[int] = set()
    if (adir / "decisions.csv").exists():
        dec = pd.read_csv(adir / "decisions.csv", usecols=["ts", "reason"])
        replayed = set(dec.loc[dec["reason"].astype(str).str.startswith(REPLAYED), "ts"].astype(int))
    age_hours = int((now - int(ts.min())) // 3600) + 1
    counts = {}
    for hours in (24, 168):
        got = set(ts[ts > now - hours * 3600])
        due = min(hours, age_hours)
        counts[hours] = (len(got), due, len(got & replayed), max(0, due - len(got)))
    (n24, due24, _, _), (n7, due7, rep7, lost7) = counts[24], counts[168]
    lines.append(f"- hours on record: {min(n24, due24)} of the last {due24}, {min(n7, due7)} of the last {due7}"
                 + (f" ({rep7} of them replayed after a missed run)" if rep7 else ""))
    week = sorted(t for t in ts if t > now - 168 * 3600)
    gaps = [(b - a, b) for a, b in zip(week, week[1:]) if b - a > 5400]
    if lost7:
        worst = max(gaps) if gaps else None
        lines.append(f"- {lost7} hours in the last 7 days have no decision at all: the run never happened and was not "
                     f"replayed" + (f" (longest gap {worst[0] / 3600:.1f} hours, ending {_ts(worst[1])})" if worst else "")
                     + ". Accounts held their books through those hours; every account shares the same gaps")
    else:
        lines.append("- no hour in the last 7 days is without a decision")
    lines.append("- this is the loop's own record. Missing candles are a different thing and are listed under Data; "
                 "a clean Data section says nothing about whether the bot ran")
    return "\n".join(lines) + "\n"


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


def _exposure_words(m: dict) -> str:
    """How a side's skill was benchmarked, for the skill line of the summary."""
    window = f"this window {m['avg_exposure']:.2f}" if m.get("avg_exposure") is not None else "this window n/a"
    if m.get("exposure_schedule"):
        return "usual " + " then ".join(f"{e:.2f}" for _, e in m["exposure_schedule"]) + f" by config, {window}"
    if m.get("skill_basis") == "usual":
        return f"usual {m['skill_exposure']:.2f}, {window}"
    return f"{window}, which stands in for a usual exposure"


def fills_pace(chal: dict, rules: dict, elapsed_days: float, total_days: float, one_look: bool = False) -> str | None:
    """A note, once a test is a week old, when it is not on pace for the fills
    the rule asks for: by its verdict, or by its first look. A test with fewer
    cannot pass a look. It can still be kept on the value of its trades; it
    cannot be promoted. one_look: a test from before ruleset 7, which is
    promoted at its first look if it passes there."""
    from .promote import rule_settings
    st = rule_settings(rules)[0]
    need, first = st["min_trades"], st["window_days"]
    if elapsed_days < 7 or elapsed_days >= total_days or chal["trades"] >= need:
        return None
    # The fills of the hour a test began in are the move from the book it was handed to its own. They are
    # not a pace: H4's ten fills in ten days, all in that hour, read as on course for sixty.
    early = min(int(chal.get("trades_first_hour") or 0), chal["trades"])
    rate = (chal["trades"] - early) / elapsed_days
    by_first, by_end = early + rate * first, early + rate * total_days
    so_far = f"{chal['trades']} in {elapsed_days:.1f} days" + (
        "" if not early else ", all of them in the hour it began" if early == chal["trades"]
        else f", {early} of them in the hour it began")
    if by_end < need:
        look = (f"day {first:.0f} keeps a test whose trades are of value and kills one whose are not"
                if elapsed_days < first else f"it is past day {first:.0f} and still running")
        return (f"{so_far}; at this pace about {int(by_end)} by day {total_days:.0f}, under the {need} a promotion "
                f"needs. Trading little does not end a test by itself: {look}, and a test that is kept and still "
                f"short of {need} fills at its verdict ends unproven, not promoted")
    if elapsed_days < first and by_first < need:
        asks = "a promotion there needs" if one_look else "a pass at the first look needs"
        return (f"{so_far}; at this pace about {int(by_first)} by day {first:.0f}, under the {need} {asks}, and "
                f"about {int(by_end)} by day {total_days:.0f}. Short of them at day {first:.0f} it is kept only if "
                f"its trades are of value, and then ruled on at day {total_days:.0f}")
    return None


def test_section(now: int) -> str:
    from .promote import (JUST_OPENED, _n, champion_note, compare_on, confidence_line, format_market, guard_waits,
                          market_context, missing_market_data, no_record, no_trade_of_its_own, of_value,
                          other_notes, other_rule_reading, paired_slot, rule_settings, trade_tally, two_looks)
    pairs = list(config.risk_cfg()["pairs"])
    rules = config.risk_cfg()["challenger"]
    st, unusable = rule_settings(rules)
    lines = ["## Challenger slots", ""]
    any_testing = False
    for name in config.challengers():
        try:
            meta = slot.load(name)
            lines.append(f"- {slot.describe_one(name, now)}")
        except Exception as e:  # noqa: BLE001
            lines.append(f"- {name}: its record could not be read this hour ({type(e).__name__}: {e})")
            continue
        if meta["status"] == "testing":
            any_testing = True
            try:
                champ, chal, mc = paired_slot(name, meta, now, rules)
            except Exception as e:  # noqa: BLE001
                lines.append(f"  its record could not be read this hour ({type(e).__name__}: {e}); nothing is ruled "
                             f"for it until it can be")
                continue
            lines.append(f"  so far: champion {_pct(champ['return'])} (max drawdown "
                         f"{_dd(champ['max_drawdown'])}, {_n(champ['trades'], 'fill')}) vs {name} "
                         f"{_pct(chal['return'])} (max drawdown {_dd(chal['max_drawdown'])}, "
                         f"{_n(chal['trades'], 'fill')})")
            if champ.get("skill") is not None and chal.get("skill") is not None:
                t_txt = f", daily edge t {chal['edge_t']:+.2f} over {chal['edge_days']} days" \
                    if chal.get("edge_t") is not None else ""
                lines.append(f"  skill (net return minus the basket held at the strategy's usual exposure): champion "
                             f"{champ['skill']:+.2%} ({_exposure_words(champ)}) vs {name} {chal['skill']:+.2%} "
                             f"({_exposure_words(chal)}); the rule compares "
                             f"on {compare_on(rules, champ, chal)}{t_txt}")
            # the readings added with ruleset 7 are for the reader; none of them may stop the summary
            try:
                elapsed = (now - meta["started_at"]) / 86400
                blank = no_record(champ, chal, name)
                gap = missing_market_data(mc, rules)
                if blank and elapsed * 24 < 1.5:
                    # a window opened by a restart begins after this hour's readings were written
                    lines.append("  no reading yet: its window opened this hour, and the first reading in it is "
                                 "written at the next run")
                elif blank:
                    lines.append(f"  no reading this hour: {blank}. Nothing is ruled on a test until that record "
                                 f"is whole")
                elif gap == JUST_OPENED:
                    lines.append("  no skill figure yet: its window opened within the hour, and no candle in it "
                                 "is on file yet")
                elif gap:
                    lines.append(f"  no skill figure this hour: {gap}. Nothing is ruled on a test until the market "
                                 f"data is whole")
                worth, why = of_value(champ, chal, rules)
                tally = trade_tally(chal)
                if not chal.get("trades"):
                    lines.append("  trades: none yet. A test that has finished no trade of its own by its look is "
                                 "killed")
                elif chal.get("return") is None:
                    lines.append("  trades: there is no usable equity record in its window to set them against")
                elif no_trade_of_its_own(chal):
                    lines.append(f"  trades: {why}. A test that has finished no trade of its own by its look is "
                                 f"killed")
                elif worth:
                    lines.append(f"  trades: {tally}. Of value on today's numbers, which keeps a test that does not "
                                 f"pass the rule (kept is not promoted)")
                else:
                    lines.append(f"  trades: {why}" if why.startswith(tally)
                                 else f"  trades: {tally}. Not of value on today's numbers: {why}")
                lines.append(f"  confidence: {confidence_line(chal, rules)}")
                one_look = not two_looks(meta, rules)
                pace = fills_pace(chal, rules, elapsed, st["window_days"] + st["confirm_days"], one_look)
                if pace:
                    lines.append(f"  fills: {pace}")
                if st["two_from"] is not None and one_look and not blank and gap != JUST_OPENED:
                    lines.append("  two look rule (measured, not applied to this test): "
                                 + other_rule_reading(champ, chal, rules, elapsed, gap=gap))
                changed = champion_note(meta["started_at"], now, bool(champ.get("exposure_schedule")),
                                        measured=champ.get("skill") is not None)
                if changed:
                    lines.append(f"  champion change: {changed}")
            except Exception as e:  # noqa: BLE001
                lines.append(f"  confidence and rule readings unavailable ({type(e).__name__}: {e})")
            try:
                lines.append("  market over the window: nothing yet (no candle in it is on file)"
                             if mc.get("gap") == JUST_OPENED else
                             f"  market over the window: {format_market(market_context(meta['started_at'], now, pairs))}")
            except Exception as e:  # noqa: BLE001
                lines.append(f"  market over the window: unavailable ({e})")
    free = slot.free_slots()
    lines.append(f"- free slots: {', '.join(free) if free else 'none'}")
    try:
        lines.append(f"- {shadow.describe(now)}")
        waits = guard_waits(now, rules)
        if waits:
            lines.append(f"  no ruling this hour: {waits}. The guard is ruled on once that is whole")
    except Exception as e:  # noqa: BLE001
        lines.append(f"- shadow: its record could not be read this hour ({type(e).__name__}: {e})")
    for line in unusable + other_notes():
        lines.append(f"- SETTING NOT USED: {line}")
    if any_testing:
        lines.append("- interim readings are not verdicts. A test is ruled on at its looks, day "
                     f"{st['window_days']:.0f} and day {st['window_days'] + st['confirm_days']:.0f}, and before them "
                     "only by an early kill")
        lines.append("- a finished trade is a position the account left (sold down to a twentieth or less); one of "
                     "its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has "
                     "finished none of its own is killed at its look; one that does not pass the rule is kept when "
                     "its finished trades made money after costs (PROMOTION.md)")
        lines.append("- confidence is the chance the strategy has a real edge, from the t of its daily skill over the "
                     "whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)")
    return "\n".join(lines) + "\n"


def _section(title: str, fn, *args) -> str:
    """One section of the summary, or two lines saying it could not be built.
    A state file that cannot be read must not cost the hour its summary and,
    with it, the commit of the hour's trading: the section says so, every
    hour, until the file is mended."""
    try:
        return fn(*args)
    except Exception as e:  # noqa: BLE001
        return f"## {title}\n\nits record could not be read this hour ({type(e).__name__}: {e})\n"


def build(now: int | None = None) -> str:
    now = now or int(time.time())
    rcfg = config.risk_cfg()
    parts = [f"# quantloop summary — generated {_ts(now)}", "",
             f"Cost model: fee {rcfg['fee_bps']} bps + slippage {rcfg['slippage_bps']} bps per side "
             f"(~{2 * (rcfg['fee_bps'] + rcfg['slippage_bps'])} bps per round trip). "
             f"Pairs: {', '.join(rcfg['pairs'])}. Paper only.", ""]
    parts.append(_section("Runs", runs_section, now))
    parts.append(_section("Challenger slots", test_section, now))
    for name in config.accounts():
        parts.append(_section(name, account_section, name, now))
    parts.append(_section("Data", data_section, list(rcfg["pairs"]), now))
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
