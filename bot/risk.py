"""Position limits and the daily halt. PROTECTED.

The strategy proposes weights; this module decides what is allowed. Spot only:
weights are clipped to [0, max_weight_per_pair], gross exposure to
max_gross_weight, and a bad day ends trading for that UTC day.
"""
from __future__ import annotations

import math


def apply_limits(targets: dict[str, float], cfg: dict) -> dict[str, float]:
    per_pair = float(cfg["max_weight_per_pair"])
    gross_cap = float(cfg["max_gross_weight"])
    clean: dict[str, float] = {}
    for pair, w in targets.items():
        try:
            w = float(w)
        except (TypeError, ValueError):
            w = 0.0
        if math.isnan(w) or math.isinf(w):
            w = 0.0
        clean[pair] = min(max(w, 0.0), per_pair)
    gross = sum(clean.values())
    if gross > gross_cap and gross > 0:
        scale = gross_cap / gross
        clean = {p: w * scale for p, w in clean.items()}
    return clean


def worth_trading(target_w: float, current_w: float, equity: float, cfg: dict) -> tuple[bool, str]:
    """Skip trades that are too small to matter. Fees are paid on every fill,
    so churn from tiny rebalances is pure cost."""
    delta_w = target_w - current_w
    if abs(delta_w) < float(cfg["rebalance_threshold"]) and not (target_w == 0 and current_w > 0):
        return False, f"hold: weight change {delta_w:+.3f} below threshold {cfg['rebalance_threshold']}"
    if abs(delta_w) * equity < float(cfg["min_trade_notional"]) and not (target_w == 0 and current_w > 0):
        return False, f"hold: notional {abs(delta_w) * equity:.0f} below minimum {cfg['min_trade_notional']}"
    return True, ""


def daily_halt_triggered(equity: float, day_open_equity: float, cfg: dict) -> bool:
    if day_open_equity <= 0:
        return False
    return (equity / day_open_equity - 1.0) <= -float(cfg["daily_loss_halt"])
