"""Paper account and cost model. PROTECTED.

One cost model serves both the live paper loop and the backtest, so a strategy
can never look cheaper in the backtest than it is in the paper account.

Reference price = mid (paper) or the next candle's open (backtest).
Buy fill  = ref * (1 + slip)
Sell fill = ref * (1 - slip)
Fee       = notional * fee_bps / 1e4, paid on every fill.

slip is slippage_bps / 1e4 in the backtest. In the paper loop it is the larger
of that floor and the observed half spread plus impact_bps, so a wide market
costs what it really costs while a tight one never looks cheaper than the
model the backtest was judged on.

gross pnl = net pnl + fees + slippage. Everything reported as "gross" is what
the strategy would have made if trading were free; "net" is what it made.
"""
from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

TRADE_FIELDS = ["ts", "account", "pair", "side", "qty", "price", "ref_price", "notional",
                "fee", "slippage_cost", "reason", "equity_after", "half_spread_bps", "slip_bps"]
EQUITY_FIELDS = ["ts", "equity", "cash", "gross_exposure", "n_positions", "fees_paid", "slippage_paid"]


@dataclass
class Fill:
    ts: int
    account: str
    pair: str
    side: str
    qty: float
    price: float
    ref_price: float
    notional: float
    fee: float
    slippage_cost: float
    reason: str
    equity_after: float = 0.0
    half_spread_bps: float = 0.0
    slip_bps: float = 0.0


class PaperAccount:
    def __init__(self, name: str, initial_cash: float, fee_bps: float, slippage_bps: float):
        self.name = name
        self.fee_rate = fee_bps / 1e4
        self.slip_rate = slippage_bps / 1e4
        self.state = {
            "name": name,
            "initial_cash": float(initial_cash),
            "cash": float(initial_cash),
            "positions": {},
            "created_at": None,
            "day": None,
            "day_open_equity": float(initial_cash),
            "halted_day": None,
            "fees_paid": 0.0,
            "slippage_paid": 0.0,
            "n_trades": 0,
            "last_run_ts": None,
        }

    # --- persistence -------------------------------------------------------
    @classmethod
    def load(cls, path: Path, name: str, initial_cash: float, fee_bps: float, slippage_bps: float):
        acct = cls(name, initial_cash, fee_bps, slippage_bps)
        if path.exists():
            acct.state.update(json.loads(path.read_text()))
        return acct

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.state, indent=2, sort_keys=True))

    # --- valuation ---------------------------------------------------------
    @property
    def cash(self) -> float:
        return self.state["cash"]

    @property
    def positions(self) -> dict[str, float]:
        return self.state["positions"]

    def equity(self, prices: dict[str, float]) -> float:
        value = self.cash
        for pair, qty in self.positions.items():
            if pair in prices:
                value += qty * prices[pair]
        return value

    def gross_exposure(self, prices: dict[str, float]) -> float:
        return sum(qty * prices[p] for p, qty in self.positions.items() if p in prices)

    def weights(self, prices: dict[str, float]) -> dict[str, float]:
        eq = self.equity(prices)
        if eq <= 0:
            return {p: 0.0 for p in self.positions}
        return {p: qty * prices[p] / eq for p, qty in self.positions.items() if p in prices}

    def gross_pnl(self, prices: dict[str, float]) -> float:
        return (self.equity(prices) - self.state["initial_cash"]
                + self.state["fees_paid"] + self.state["slippage_paid"])

    def total_costs(self) -> float:
        return self.state["fees_paid"] + self.state["slippage_paid"]

    # --- execution ---------------------------------------------------------
    def effective_slip_rate(self, half_spread_bps: float | None, impact_bps: float = 0.0) -> float:
        """Never below the modelled floor; above it when the live market is wider."""
        if half_spread_bps is None:
            return self.slip_rate
        return max(self.slip_rate, (half_spread_bps + impact_bps) / 1e4)

    def trade(self, pair: str, delta_notional: float, ref_price: float, ts: int,
              reason: str, min_notional: float = 0.0, half_spread_bps: float | None = None,
              impact_bps: float = 0.0) -> Fill | None:
        """Move the position in `pair` by roughly `delta_notional` dollars at the
        reference price plus costs. Positive buys, negative sells. Returns the
        fill, or None when nothing sensible could be done."""
        if ref_price <= 0 or delta_notional == 0:
            return None
        slip = self.effective_slip_rate(half_spread_bps, impact_bps)
        if delta_notional > 0:
            fill_px = ref_price * (1 + slip)
            affordable = self.cash / (1 + self.fee_rate)
            notional = min(delta_notional, affordable)
            if notional < min_notional or notional <= 0:
                return None
            qty = notional / fill_px
            fee = notional * self.fee_rate
            self.state["cash"] -= notional + fee
            self.positions[pair] = self.positions.get(pair, 0.0) + qty
            slippage_cost = qty * (fill_px - ref_price)
            side = "buy"
        else:
            held = self.positions.get(pair, 0.0)
            if held <= 0:
                return None
            fill_px = ref_price * (1 - slip)
            qty = min(-delta_notional / fill_px, held)
            closing_all = qty >= held * 0.999
            notional = qty * fill_px
            if notional < min_notional and not closing_all:
                return None
            if closing_all:
                qty = held
                notional = qty * fill_px
            fee = notional * self.fee_rate
            self.state["cash"] += notional - fee
            remaining = held - qty
            if remaining <= 1e-12:
                self.positions.pop(pair, None)
            else:
                self.positions[pair] = remaining
            slippage_cost = qty * (ref_price - fill_px)
            side = "sell"
        self.state["fees_paid"] += fee
        self.state["slippage_paid"] += slippage_cost
        self.state["n_trades"] += 1
        return Fill(ts=ts, account=self.name, pair=pair, side=side, qty=qty, price=fill_px,
                    ref_price=ref_price, notional=notional, fee=fee,
                    slippage_cost=slippage_cost, reason=reason,
                    half_spread_bps=float(half_spread_bps or 0.0), slip_bps=slip * 1e4)


# --- csv logs ---------------------------------------------------------------

def append_rows(path: Path, fields: list[str], rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    if not new:
        with open(path, newline="") as f:
            header = f.readline().rstrip("\n").split(",")
        if header != fields:
            # the schema grew: rewrite the file under the new header, old rows padded
            import pandas as pd
            old = pd.read_csv(path)
            for col in fields:
                if col not in old.columns:
                    old[col] = ""
            old[fields].to_csv(path, index=False)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new:
            w.writeheader()
        for r in rows:
            w.writerow(r)


def fill_row(fill: Fill) -> dict:
    d = asdict(fill)
    for k in ("qty", "price", "ref_price", "notional", "fee", "slippage_cost", "equity_after",
              "half_spread_bps", "slip_bps"):
        d[k] = round(d[k], 8)
    return d
