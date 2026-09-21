"""Hourly entry point and the single decision step shared with the backtest. PROTECTED.

    python -m bot.run                      # champion plus every challenger slot
    python -m bot.run --account champion   # a subset

For every account: refresh candles, read quotes, ask the strategy for target
weights, let risk.py trim them, fill the difference in the paper account, and
log every decision with its reason. bot/backtest.py replays the same `step`
over history so the two can never disagree about how a decision becomes a fill.
"""
from __future__ import annotations

import argparse
import time
from datetime import datetime, timezone

from . import config, data, paper, risk, slot, strategy

DECISION_FIELDS = ["ts", "account", "pair", "price", "signal_weight", "target_weight",
                   "current_weight", "action", "reason", "half_spread_bps"]


def utc_day(ts: int) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")


def step(acct: paper.PaperAccount, cfg: dict, fn, candles: dict, prices: dict[str, float],
         ts: int, rcfg: dict, half_spreads: dict[str, float] | None = None) -> tuple[list[dict], list[paper.Fill], float]:
    """One decision cycle for one account at one timestamp. Mutates the account.
    half_spreads (bps, per pair) come from live quotes; the backtest passes none
    and pays the modelled floor."""
    half_spreads = half_spreads or {}
    impact = float(rcfg.get("impact_bps", 0.0))
    st = acct.state
    name = acct.name
    if st["created_at"] is None:
        st["created_at"] = ts
    day = utc_day(ts)
    equity = acct.equity(prices)
    if st["day"] != day:
        st["day"] = day
        st["day_open_equity"] = equity
    halted = st["halted_day"] == day
    halt_note = ""
    if not halted and risk.daily_halt_triggered(equity, st["day_open_equity"], rcfg):
        halted = True
        st["halted_day"] = day
        halt_note = (f"daily halt: equity {equity:.2f} is down "
                     f"{1 - equity / st['day_open_equity']:.1%} from the day's open {st['day_open_equity']:.2f}")

    current_w = acct.weights(prices)
    tradable = {p: df for p, df in candles.items() if p in prices and len(df)}
    if halted:
        targets = {p: strategy.Target(0.0, halt_note or "daily halt in force: flat for the rest of the UTC day")
                   for p in tradable}
    else:
        try:
            targets = strategy.normalise(fn(tradable, cfg["params"], current_w))
        except Exception as e:  # noqa: BLE001
            # A broken strategy must not crash the loop or leave stale positions: go flat and say why.
            targets = {p: strategy.Target(0.0, f"strategy error {type(e).__name__}: {e}") for p in tradable}
    for p in tradable:
        targets.setdefault(p, strategy.Target(0.0, "strategy returned no target for this pair"))
    limited = risk.apply_limits({p: targets[p].weight for p in tradable}, rcfg)

    decisions, fills = [], []
    for pair in tradable:
        sig_w = targets[pair].weight
        tgt_w = limited.get(pair, 0.0)
        cur_w = current_w.get(pair, 0.0)
        reason = targets[pair].reason
        ok, why = risk.worth_trading(tgt_w, cur_w, equity, rcfg)
        action = "hold"
        if ok:
            delta = (tgt_w - cur_w) * equity
            fill = acct.trade(pair, delta, prices[pair], ts, reason, rcfg["min_trade_notional"],
                              half_spread_bps=half_spreads.get(pair), impact_bps=impact)
            if fill:
                fill.equity_after = acct.equity(prices)
                fills.append(fill)
                action = fill.side
            else:
                action = "none"
                why = "no fill possible (no cash or no position)"
        decisions.append({
            "ts": ts, "account": name, "pair": pair, "price": round(prices[pair], 6),
            "signal_weight": round(sig_w, 4), "target_weight": round(tgt_w, 4),
            "current_weight": round(cur_w, 4), "action": action,
            "reason": (why + " | " if why else "") + reason,
            "half_spread_bps": round(half_spreads.get(pair, 0.0), 3),
        })
    st["last_run_ts"] = ts
    return decisions, fills, acct.equity(prices)


def run_account(name: str, candles: dict, prices: dict[str, float], ts: int, rcfg: dict,
                half_spreads: dict[str, float] | None = None) -> float:
    cfg = config.account_cfg(name)
    fn = strategy.get(cfg["strategy"])
    adir = config.account_dir(name)
    acct = paper.PaperAccount.load(adir / "account.json", name, rcfg["initial_cash"],
                                   rcfg["fee_bps"], rcfg["slippage_bps"])
    decisions, fills, equity = step(acct, cfg, fn, candles, prices, ts, rcfg, half_spreads)
    st = acct.state
    acct.save(adir / "account.json")
    paper.append_rows(adir / "decisions.csv", DECISION_FIELDS, decisions)
    paper.append_rows(adir / "trades.csv", paper.TRADE_FIELDS, [paper.fill_row(f) for f in fills])
    paper.append_rows(adir / "equity.csv", paper.EQUITY_FIELDS, [{
        "ts": ts, "equity": round(equity, 4), "cash": round(acct.cash, 4),
        "gross_exposure": round(acct.gross_exposure(prices), 4), "n_positions": len(acct.positions),
        "fees_paid": round(st["fees_paid"], 4), "slippage_paid": round(st["slippage_paid"], 4),
    }])
    n_buy = sum(1 for f in fills if f.side == "buy")
    n_sell = len(fills) - n_buy
    halted = st["halted_day"] == utc_day(ts)
    print(f"[{name}] {cfg['strategy']} ({cfg['hypothesis']}) equity {equity:,.2f} "
          f"cash {acct.cash:,.2f} positions {len(acct.positions)} fills {n_buy} buy / {n_sell} sell"
          + (" HALTED" if halted else ""))
    return equity


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--account", action="append", default=None)
    ap.add_argument("--now", type=int, default=None, help="unix ts override (tests)")
    args = ap.parse_args(argv)
    config.prepare()
    accounts = args.account or config.accounts()
    ts = args.now or int(time.time())
    rcfg = config.risk_cfg()
    pairs = list(rcfg["pairs"])
    source = data.get_source(pairs, rcfg.get("quote", "USD"))

    candles = data.update_candles(pairs, source)
    target = int(rcfg.get("history_target_hours", 0))
    if target:
        data.backfill_if_short(pairs, target, data.get_history_source(pairs, rcfg.get("quote", "USD")), now=ts)
    hist = int(rcfg.get("history_hours", 720))
    # History plus live, the same frames the backtest replays. The live cache
    # alone is a few weeks deep and starves any lookback longer than that
    # (found by the weekly digest on 2026-09-21: H2 sat flat on "need 1610").
    candles = data.strategy_frames(pairs, hist)
    qs = data.quotes(pairs, source)
    prices = {p: q.mid for p, q in qs.items()}
    half_spreads = {p: q.half_spread_bps for p, q in qs.items()}
    missing = [p for p in pairs if p not in prices]
    if missing:
        print(f"[data] no quote for {missing}; those pairs are held as they are this run")
    if not prices:
        print("[data] no quotes at all; nothing to do")
        return 1
    print(f"[run] {datetime.fromtimestamp(ts, timezone.utc):%Y-%m-%d %H:%M}Z "
          + " ".join(f"{p}={prices[p]:.4g}" for p in prices))

    equities = {}
    for name in accounts:
        equities[name] = run_account(name, candles, prices, ts, rcfg, half_spreads)
    if set(accounts) >= set(config.accounts()):
        slot.maybe_start(ts, equities)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
