"""Rule on challenger tests. PROTECTED.

    python -m bot.promote [--now <unix ts>]

Runs every hour after the accounts. For every slot whose test has run for
challenger.window_days, using only data from the test window (which the
hypothesis could not have been fitted to, because it did not exist yet):

  promoted  challenger beats champion by more than min_return_edge on the
            quantity challenger.compare_on names:
              return  net return over the window
              skill   net return minus the equal weight basket held at the
                      account's own average exposure (beta removed, timing kept)
            AND challenger max drawdown <= max(max_dd_ratio * champion max drawdown, max_dd_floor)
            AND challenger placed >= min_trades fills
  killed    otherwise

Every verdict also records each side's average exposure, skill, and the t
statistic of the daily edge it was decided on, so a reader can tell a real
difference from a coin flip. None of those extra numbers decide anything.

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
           "gross_pnl": None, "traded_notional": 0.0, "realised_bps": None, "avg_exposure": None,
           "skill": None, "edge_t": None, "edge_days": 0}
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
            eqv = eq["equity"].astype(float)
            out["avg_exposure"] = float((eq["gross_exposure"].astype(float) / eqv.where(eqv > 0)).fillna(0).mean())
    if tr_path.exists():
        tr = pd.read_csv(tr_path)
        tr = tr[(tr["ts"] >= start_ts) & (tr["ts"] <= end_ts)]
        out["trades"] = int(len(tr))
        out["traded_notional"] = float(tr["notional"].sum()) if len(tr) else 0.0
    if out["gross_pnl"] is not None and out["traded_notional"] > 0:
        # one round trip is a buy plus a sell, so half the traded notional
        out["realised_bps"] = out["gross_pnl"] / (out["traded_notional"] / 2) * 1e4
    return out


def add_skill(m: dict, basket_return: float | None) -> dict:
    """Net return minus a constant position in the equal weight basket at the
    account's own average exposure over the window: what it made beyond what
    simply holding that much of the market would have made. The same
    definition backtest_gate prints, so in sample and prospective skill can be
    compared line for line in FINDINGS. Timing counts as skill (the benchmark
    holds the average exposure all the time); beta does not."""
    if m.get("return") is not None and m.get("avg_exposure") is not None and basket_return is not None:
        m["skill"] = float(m["return"] - m["avg_exposure"] * basket_return)
    return m


def _daily(name: str, start_ts: int, end_ts: int, base: float | None) -> pd.DataFrame:
    """Account equity by day of the window (days counted from the window start)."""
    p = config.account_dir(name) / "equity.csv"
    if not p.exists():
        return pd.DataFrame()
    eq = pd.read_csv(p)
    eq = eq[(eq["ts"] >= start_ts) & (eq["ts"] <= end_ts)]
    if not len(eq):
        return pd.DataFrame()
    eq = eq.assign(day=(eq["ts"] - start_ts) // 86400)
    daily = eq.groupby("day")["equity"].last().astype(float)
    prev = daily.shift(1)
    prev.iloc[0] = base if base else float(eq["equity"].iloc[0])
    return pd.DataFrame({"ret": daily / prev - 1})


def edge_t(champ_name: str, chal_name: str, start_ts: int, end_ts: int, start_equity: dict,
           champ: dict, chal: dict, basket_path, on: str) -> tuple[float | None, int]:
    """t statistic of the daily edge the verdict is decided on, and the number
    of days behind it. Informational: it says how far the edge sits from zero
    in units of its own day to day noise. |t| under about 2 is noise."""
    a = _daily(champ_name, start_ts, end_ts, start_equity.get(champ_name))
    b = _daily(chal_name, start_ts, end_ts, start_equity.get(chal_name))
    if not len(a) or not len(b):
        return None, 0
    d = b["ret"].sub(a["ret"], fill_value=0.0)
    if on == "skill" and basket_path is not None and len(basket_path) > 1:
        bp = pd.Series(basket_path.values, index=basket_path.index)
        bday = bp.groupby((bp.index.astype("int64") - start_ts) // 86400).last()
        bret = (bday / bday.shift(1) - 1).fillna(bday.iloc[0] / float(bp.iloc[0]) - 1)
        e_ch, e_cp = chal.get("avg_exposure") or 0.0, champ.get("avg_exposure") or 0.0
        d = d.sub((e_ch - e_cp) * bret.reindex(d.index).fillna(0.0), fill_value=0.0)
    d = d.dropna()
    n = int(len(d))
    if n < 3 or float(d.std(ddof=1)) == 0:
        return None, n
    return float(d.mean() / (d.std(ddof=1) / math.sqrt(n))), n


def paired(champ_name: str, chal_name: str, start_ts: int, end_ts: int, start_equity: dict,
           rules: dict) -> tuple[dict, dict, dict]:
    """Both sides of a paired test over one window, with skill and the edge t."""
    champ = window_metrics(champ_name, start_ts, end_ts, start_equity.get(champ_name))
    chal = window_metrics(chal_name, start_ts, end_ts, start_equity.get(chal_name))
    try:
        mc = market_context(start_ts, end_ts, list(config.risk_cfg()["pairs"]))
    except Exception:  # noqa: BLE001
        mc = {"basket_return": None, "basket_path": None}
    add_skill(champ, mc.get("basket_return"))
    add_skill(chal, mc.get("basket_return"))
    on = compare_on(rules, champ, chal)
    chal["edge_t"], chal["edge_days"] = edge_t(champ_name, chal_name, start_ts, end_ts, start_equity,
                                               champ, chal, mc.get("basket_path"), on)
    return champ, chal, mc


def compare_on(rules: dict, champ: dict, chal: dict) -> str:
    """"skill" when the rules ask for it and both sides have it, else "return"."""
    if str(rules.get("compare_on", "return")) == "skill" and champ.get("skill") is not None \
            and chal.get("skill") is not None:
        return "skill"
    return "return"


def decide(champ: dict, chal: dict, rules: dict) -> tuple[str, str]:
    if chal["return"] is None or champ["return"] is None:
        return "killed", "no equity data for the window"
    if chal["trades"] < int(rules["min_trades"]):
        return "killed", (f"challenger made {chal['trades']} fills, fewer than the {rules['min_trades']} "
                          f"needed for a verdict; a strategy that does not trade cannot be judged")
    on = compare_on(rules, champ, chal)
    t_note = (f"; daily edge t {chal['edge_t']:+.1f} over {chal['edge_days']} days"
              if chal.get("edge_t") is not None else "")
    if on == "skill":
        edge = chal["skill"] - champ["skill"]
        if edge <= float(rules["min_return_edge"]):
            return "killed", (f"challenger skill {chal['skill']:+.2%} (net {chal['return']:+.2%} at average exposure "
                              f"{chal['avg_exposure']:.2f}) did not beat champion skill {champ['skill']:+.2%} (net "
                              f"{champ['return']:+.2%} at {champ['avg_exposure']:.2f}) by more than "
                              f"{rules['min_return_edge']:.2%}{t_note}")
    else:
        edge = chal["return"] - champ["return"]
        if edge <= float(rules["min_return_edge"]):
            return "killed", (f"challenger net return {chal['return']:+.2%} did not beat champion "
                              f"{champ['return']:+.2%} by more than {rules['min_return_edge']:.2%}{t_note}")
    champ_dd = abs(champ["max_drawdown"] or 0.0)
    chal_dd = abs(chal["max_drawdown"] or 0.0)
    limit = max(float(rules["max_dd_ratio"]) * champ_dd, float(rules.get("max_dd_floor", 0.0)))
    if chal_dd > limit:
        return "killed", (f"challenger max drawdown {chal_dd:.2%} exceeded the limit {limit:.2%} "
                          f"(the larger of {rules['max_dd_ratio']}x the champion's {champ_dd:.2%} and the "
                          f"{float(rules.get('max_dd_floor', 0.0)):.0%} floor) despite better return {edge:+.2%}")
    if on == "skill":
        return "promoted", (f"challenger skill {chal['skill']:+.2%} (net {chal['return']:+.2%} at average exposure "
                            f"{chal['avg_exposure']:.2f}) beat champion skill {champ['skill']:+.2%} (net "
                            f"{champ['return']:+.2%} at {champ['avg_exposure']:.2f}) with max drawdown "
                            f"{chal_dd:.2%} vs {champ_dd:.2%}{t_note}")
    return "promoted", (f"challenger net return {chal['return']:+.2%} beat champion {champ['return']:+.2%} "
                        f"with max drawdown {chal_dd:.2%} vs {champ_dd:.2%}{t_note}")


def early_kill(chal: dict, rules: dict) -> str | None:
    limit = float(rules.get("early_kill_drawdown", 0) or 0)
    if limit and chal["max_drawdown"] is not None and abs(chal["max_drawdown"]) > limit:
        return (f"challenger drew down {abs(chal['max_drawdown']):.2%} from its window start, past the "
                f"{limit:.0%} early kill limit; no need to wait for the window to end")
    return None


def market_context(start_ts: int, end_ts: int, pairs: list[str]) -> dict:
    """What the market did over a window: BTC return, equal weight basket
    return, basket realised vol (annualised from hourly basket returns)."""
    out = {"btc_return": None, "basket_return": None, "basket_vol": None, "basket_max_dd": None,
           "pairs": 0, "basket_path": None}
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
    frame = pd.DataFrame(series).sort_index().ffill().bfill()
    hourly = frame.pct_change().mean(axis=1).dropna()
    if len(hourly) > 2:
        out["basket_vol"] = float(hourly.std() * math.sqrt(24 * 365))
    path = (frame / frame.iloc[0]).mean(axis=1)          # equal weight buy and hold, rebalanced never
    out["basket_max_dd"] = float((path / path.cummax() - 1).min())
    out["basket_path"] = path
    return out


def format_market(mc: dict) -> str:
    if not mc.get("pairs"):
        return "no candle data for the window"
    parts = []
    if mc["btc_return"] is not None:
        parts.append(f"BTC {mc['btc_return']:+.2%}")
    parts.append(f"equal weight basket of {mc['pairs']} pairs {mc['basket_return']:+.2%}")
    if mc.get("basket_max_dd") is not None:
        parts.append(f"basket max drawdown {mc['basket_max_dd']:.0%}")
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
    if d.get("avg_exposure") is not None:
        s += f", average exposure {d['avg_exposure']:.2f}"
    if d.get("skill") is not None:
        s += f", skill vs exposure matched basket {d['skill']:+.2%}"
    if d.get("edge_t") is not None:
        s += f", daily edge t {d['edge_t']:+.1f} over {d['edge_days']} days"
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
    champ, shad, _ = paired(config.CHAMPION, config.SHADOW, start, now, meta["start_equity"], rules)
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
        champ, chal, _ = paired(config.CHAMPION, name, start, now, meta["start_equity"], rules)
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
        champ_, chal_, _ = paired(config.CHAMPION, name, int(meta["started_at"]), now, meta["start_equity"], rules)
        key = "skill" if compare_on(rules, champ_, chal_) == "skill" else "return"
        return chal_[key] if chal_[key] is not None else -1e9
    verdicts.sort(key=lambda v: (v[2] != "promoted", -strength(v)))

    promoted_hyp: str | None = None
    for name, hyp, verdict, reason in verdicts:
        meta = slot.load(name)
        start = int(meta["started_at"])
        champ, chal, _ = paired(config.CHAMPION, name, start, now, meta["start_equity"], rules)
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
