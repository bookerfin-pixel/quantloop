"""Signal logic. THE AGENT MAY EDIT THIS FILE.

Contract
--------
A strategy is a function registered with @register("name"):

    def my_strategy(candles, params, current_weights) -> dict[pair, Target | float]

candles         : {pair: DataFrame[time, open, high, low, close, vwap, volume, count]}
                  hourly, oldest first, closed candles only, at most
                  risk.yaml:history_hours rows. The last row is the most recent
                  closed hour.
params          : the `params` mapping from configs/<account>.yaml
current_weights : {pair: weight} currently held (0 if flat), so a strategy can
                  use hysteresis (enter at one level, exit at another)
returns         : {pair: Target(weight, reason)} or {pair: weight}. Weights are
                  fractions of equity in [0, 1]. Spot only, so no negatives.
                  bot/risk.py clips per pair and gross exposure afterwards.

The reason string is logged with every decision. Write it for a human reading
the log a month later: what the signal saw and why that means this weight.

Rules of thumb that survived Fin's first bot (see LEDGER.md, entries P1 and P2):
every round trip costs about 30 bps (fee 10 + slippage 5, each side). A signal
whose average gross move per trade is not several times that is dead on
arrival, no matter how good it looks before costs. Prefer fewer, larger moves.
"""
from __future__ import annotations

from typing import Callable, NamedTuple

import numpy as np
import pandas as pd

HOURS_PER_YEAR = 24 * 365


class Target(NamedTuple):
    weight: float
    reason: str


STRATEGIES: dict[str, Callable] = {}


def register(name: str):
    def deco(fn):
        STRATEGIES[name] = fn
        return fn
    return deco


def get(name: str) -> Callable:
    if name not in STRATEGIES:
        raise KeyError(f"unknown strategy {name!r}; registered: {sorted(STRATEGIES)}")
    return STRATEGIES[name]


def normalise(raw: dict) -> dict[str, Target]:
    out = {}
    for pair, t in raw.items():
        if isinstance(t, Target):
            out[pair] = t
        else:
            out[pair] = Target(float(t), "")
    return out


# --- helpers ----------------------------------------------------------------

def realised_vol_annual(close: pd.Series, hours: int) -> float:
    rets = np.log(close).diff().dropna().tail(hours)
    if len(rets) < max(10, hours // 4):
        return float("nan")
    return float(rets.std() * np.sqrt(HOURS_PER_YEAR))


def vol_scaled_weight(close: pd.Series, params: dict) -> tuple[float, float]:
    """Size so the position's annualised vol is about target_vol_annual.
    Returns (weight, realised_vol)."""
    vol = realised_vol_annual(close, int(params.get("vol_lookback_hours", 168)))
    if not np.isfinite(vol) or vol <= 0:
        return 0.0, vol
    w = float(params.get("target_vol_annual", 0.30)) / vol
    return min(w, float(params.get("max_weight", 0.25))), vol


# --- strategies -------------------------------------------------------------

@register("ts_momentum")
def ts_momentum(candles: dict[str, pd.DataFrame], params: dict,
                current_weights: dict[str, float]) -> dict[str, Target]:
    """Time series momentum, long or flat, with bands so it does not flip on
    noise. Enter when the trailing lookback_hours return is above entry_return
    and price sits above its ema_hours EMA. Once long, stay long until that
    return drops below exit_return or price closes more than ema_exit_buffer
    below the EMA. Size by inverse realised vol. Slow by design: a handful of
    decisions per week per pair, so a 30 bps round trip stays small next to
    the moves it is after."""
    lookback = int(params.get("lookback_hours", 72))
    ema_hours = int(params.get("ema_hours", 24))
    entry = float(params.get("entry_return", 0.01))
    exit_ = float(params.get("exit_return", -0.01))
    ema_buffer = float(params.get("ema_exit_buffer", 0.02))
    out: dict[str, Target] = {}
    for pair, df in candles.items():
        close = df["close"].astype(float)
        if len(close) < max(lookback, ema_hours) + 2:
            out[pair] = Target(0.0, f"flat: only {len(close)} candles, need {max(lookback, ema_hours) + 2}")
            continue
        ret = float(close.iloc[-1] / close.iloc[-1 - lookback] - 1)
        ema = float(close.ewm(span=ema_hours, adjust=False).mean().iloc[-1])
        above = float(close.iloc[-1]) > ema
        far_below = float(close.iloc[-1]) < ema * (1 - ema_buffer)
        holding = current_weights.get(pair, 0.0) > 0
        if holding:
            go_long = ret > exit_ and not far_below
        else:
            go_long = ret > entry and above
        if go_long:
            w, vol = vol_scaled_weight(close, params)
            state = "stay long" if holding else "enter long"
            where = "above" if above else f"within {ema_buffer:.1%} of"
            out[pair] = Target(w, f"{state}: {lookback}h return {ret:+.2%} vs {'exit' if holding else 'entry'} band "
                                  f"{exit_ if holding else entry:+.1%} and price {where} {ema_hours}h EMA; "
                                  f"realised vol {vol:.0%} -> weight {w:.2f}")
        else:
            why = []
            if holding and ret <= exit_:
                why.append(f"{lookback}h return {ret:+.2%} fell below exit band {exit_:+.1%}")
            elif not holding and ret <= entry:
                why.append(f"{lookback}h return {ret:+.2%} not above entry band {entry:+.1%}")
            if holding and far_below:
                why.append(f"price more than {ema_buffer:.1%} below {ema_hours}h EMA")
            elif not holding and not above:
                why.append(f"price below {ema_hours}h EMA")
            out[pair] = Target(0.0, ("exit: " if holding else "flat: ") + " and ".join(why))
    return out


@register("mean_reversion")
def mean_reversion(candles: dict[str, pd.DataFrame], params: dict,
                   current_weights: dict[str, float]) -> dict[str, Target]:
    """Long only mean reversion with hysteresis. Enter when the z score of price
    against its rolling mean drops below -entry_z, exit when it recovers above
    -exit_z. Kept here as a second family for the agent to work from; the
    short horizon version of this idea is what costs killed in Fin's first bot,
    so a hypothesis in this family has to explain why its horizon is long enough."""
    window = int(params.get("window_hours", 96))
    entry_z = float(params.get("entry_z", 2.0))
    exit_z = float(params.get("exit_z", 0.5))
    out: dict[str, Target] = {}
    for pair, df in candles.items():
        close = df["close"].astype(float)
        if len(close) < window + 2:
            out[pair] = Target(0.0, f"flat: only {len(close)} candles, need {window + 2}")
            continue
        mean = float(close.rolling(window).mean().iloc[-1])
        std = float(close.rolling(window).std().iloc[-1])
        if not np.isfinite(std) or std <= 0:
            out[pair] = Target(0.0, "flat: zero dispersion")
            continue
        z = (float(close.iloc[-1]) - mean) / std
        holding = current_weights.get(pair, 0.0) > 0
        if z < -entry_z or (holding and z < -exit_z):
            w, vol = vol_scaled_weight(close, params)
            state = "stay long" if holding else "enter long"
            out[pair] = Target(w, f"{state}: z {z:+.2f} vs {window}h mean (entry {-entry_z}, exit {-exit_z}); "
                                  f"vol {vol:.0%} -> weight {w:.2f}")
        else:
            out[pair] = Target(0.0, f"flat: z {z:+.2f} not below {-entry_z if not holding else -exit_z}")
    return out


@register("swing_reversal")
def swing_reversal(candles: dict[str, pd.DataFrame], params: dict,
                    current_weights: dict[str, float]) -> dict[str, Target]:
    """Long only reversal off a higher low. Split the trailing 2*recent_hours
    into two adjacent halves. Find the lowest close in each half (the older
    swing low and the more recent one). If the recent low is at least
    min_higher_low above the older low (sellers made less progress the second
    time) and price then closes above the high made between the two lows
    (the reaction high sellers failed to hold below), that is a structural
    reversal, not a threshold on price (ts_momentum), a distance from a
    rolling mean (mean_reversion), or a volatility regime change
    (vol_breakout). A sustained one-directional slide keeps making lower
    lows, so the higher-low precondition has nothing to fire on for most of
    it. Exit on a close below the trailing exit_hours low, a much shorter
    window than the one used to detect the pattern, so a failed reversal is
    cut quickly rather than waiting for the wide swing-low used to find it."""
    recent_hours = int(params.get("recent_hours", 240))
    min_higher_low = float(params.get("min_higher_low", 0.03))
    exit_hours = int(params.get("exit_hours", 48))
    need = max(2 * recent_hours, exit_hours) + 2
    out: dict[str, Target] = {}
    for pair, df in candles.items():
        close = df["close"].astype(float)
        n = len(close)
        if n < need:
            out[pair] = Target(0.0, f"flat: only {n} candles, need {need}")
            continue
        first_start, first_end = n - 2 * recent_hours - 1, n - recent_hours - 1
        second_start, second_end = first_end, n - 1
        first_half = close.iloc[first_start:first_end]
        second_half = close.iloc[second_start:second_end]
        low1 = float(first_half.min())
        low2 = float(second_half.min())
        t1 = first_start + int(first_half.values.argmin())
        t2 = second_start + int(second_half.values.argmin())
        swing_high = float(close.iloc[t1:t2 + 1].max())
        price = float(close.iloc[-1])
        exit_low = float(close.iloc[-1 - exit_hours:-1].min())
        higher_low = low2 > low1 * (1 + min_higher_low)
        breaking_out = price > swing_high
        holding = current_weights.get(pair, 0.0) > 0
        if holding:
            go_long = price > exit_low
        else:
            go_long = higher_low and breaking_out
        if go_long:
            w, vol = vol_scaled_weight(close, params)
            if holding:
                reason = (f"stay long: price {price:.4g} still above the {exit_hours}h low "
                          f"{exit_low:.4g}; realised vol {vol:.0%} -> weight {w:.2f}")
            else:
                reason = (f"enter long: higher low {low2:.4g} vs prior low {low1:.4g} "
                          f"(+{(low2 / low1 - 1):.1%}) then broke above the reaction high {swing_high:.4g} "
                          f"at {price:.4g}; realised vol {vol:.0%} -> weight {w:.2f}")
            out[pair] = Target(w, reason)
        else:
            if holding:
                out[pair] = Target(0.0, f"exit: closed {price:.4g} below the {exit_hours}h low {exit_low:.4g}")
            elif not higher_low:
                out[pair] = Target(0.0, f"flat: low {low2:.4g} not a higher low vs prior low {low1:.4g} "
                                        f"(need +{min_higher_low:.1%})")
            else:
                out[pair] = Target(0.0, f"flat: higher low confirmed but {price:.4g} not above reaction high "
                                        f"{swing_high:.4g}")
    return out


@register("vol_breakout")
def vol_breakout(candles: dict[str, pd.DataFrame], params: dict,
                  current_weights: dict[str, float]) -> dict[str, Target]:
    """Long only breakout out of a volatility squeeze. Enter when a pair's
    trailing compression_hours realised vol has recently (within
    squeeze_memory_hours) sat at or below the vol_percentile quantile of its
    own trailing lookback_hours distribution, and price then closes above its
    trailing breakout_hours high. Exit on a close below the trailing
    exit_hours low. Neither the entry nor the exit reference a fixed return
    threshold (ts_momentum) or a distance from a rolling mean
    (mean_reversion): the trigger is a change in the pair's own volatility
    regime, not its level or its direction. A sustained one-directional slide
    keeps realised vol elevated rather than compressed (that is what
    "trending" means), so this signal has nothing to fire on for most of a
    slide like the trailing year's; a quiet, narrowing range is a different,
    much rarer event, and the ones that resolve upward are what this buys."""
    compression_hours = int(params.get("compression_hours", 168))
    lookback_hours = int(params.get("lookback_hours", 1440))
    vol_percentile = float(params.get("vol_percentile", 0.25))
    breakout_hours = int(params.get("breakout_hours", 120))
    squeeze_memory_hours = int(params.get("squeeze_memory_hours", 72))
    exit_hours = int(params.get("exit_hours", 72))
    need = max(lookback_hours + compression_hours, breakout_hours, exit_hours) + 2
    out: dict[str, Target] = {}
    for pair, df in candles.items():
        close = df["close"].astype(float)
        if len(close) < need:
            out[pair] = Target(0.0, f"flat: only {len(close)} candles, need {need}")
            continue
        rets = np.log(close).diff()
        vol = rets.rolling(compression_hours).std()
        vol_window = vol.tail(lookback_hours)
        threshold = float(vol_window.quantile(vol_percentile))
        squeezed_recently = bool((vol.tail(squeeze_memory_hours) <= threshold).any())
        price = float(close.iloc[-1])
        breakout_high = float(close.iloc[-1 - breakout_hours:-1].max())
        breakdown_low = float(close.iloc[-1 - exit_hours:-1].min())
        breaking_out = price > breakout_high
        breaking_down = price < breakdown_low
        holding = current_weights.get(pair, 0.0) > 0
        if holding:
            go_long = not breaking_down
        else:
            go_long = squeezed_recently and breaking_out
        if go_long:
            w, rv = vol_scaled_weight(close, params)
            if holding:
                reason = (f"stay long: price {price:.4g} still above {exit_hours}h low {breakdown_low:.4g}; "
                          f"realised vol {rv:.0%} -> weight {w:.2f}")
            else:
                reason = (f"enter long: squeeze in last {squeeze_memory_hours}h ({compression_hours}h vol at or "
                          f"below its own {vol_percentile:.0%} percentile over {lookback_hours}h) then broke above "
                          f"{breakout_hours}h high {breakout_high:.4g} at {price:.4g}; "
                          f"realised vol {rv:.0%} -> weight {w:.2f}")
            out[pair] = Target(w, reason)
        else:
            if holding:
                out[pair] = Target(0.0, f"exit: closed {price:.4g} below {exit_hours}h low {breakdown_low:.4g}")
            elif not squeezed_recently:
                out[pair] = Target(0.0, f"flat: {compression_hours}h vol not at or below its own "
                                        f"{vol_percentile:.0%} percentile over {lookback_hours}h in the last "
                                        f"{squeeze_memory_hours}h")
            else:
                out[pair] = Target(0.0, f"flat: squeezed but {price:.4g} not above {breakout_hours}h high "
                                        f"{breakout_high:.4g}")
    return out
