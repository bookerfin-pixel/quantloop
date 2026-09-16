# Hypothesis backlog

Ideas waiting for the challenger slot. The agent may add to this file on any
run and should pick from it when the slot is free, taking the one with the
best cost arithmetic, not the one that looks best in the backtest. Remove an
idea when it becomes a ledger entry or when a result makes it moot.

## Candidates

- Regime filter for the momentum champion: only take entries when 7 day realised vol is below its 30 day median. Trend following in crypto tends to work worse in high vol chop, and skipping those entries removes the most expensive round trips. Tried against the current data (2026-09-16, on a 21-day median rather than 30 because history is capped at 720 hours): backtest cost coverage came in worse than H0's own (-6.88 vs -0.96), on a short 8.9 day window since the 504h median eats most of the available history. The direction of the mechanism may still be right; the test window was too short to trust. Worth another look once more candle history has accumulated.
- Longer horizon: 168 hour lookback with wider bands (entry +3%, exit −3%). Fewer, bigger moves; the cost per unit of captured move falls roughly in proportion. Tried against the current data (2026-09-16): backtest cost coverage was worse than H0's, not better (-4.75 vs -0.96) — wider bands wait longer to exit, which let losses run further in this falling window. The "fewer, bigger moves" logic held for entries but not for the matching exit; a version of this idea should pair the wider entry band with a faster exit, not the same one.
- Cross sectional selection: hold only the top 3 of the 6 pairs by 7 day return instead of all pairs with a positive signal. Concentrates into the strongest trends, which in past crypto data carry most of the momentum premium.
- Weekend throttle: no new entries from Friday 20:00 UTC to Monday 00:00 UTC. Liquidity thins and spreads widen at the weekend, so the modelled 5 bps slippage understates the true cost of those fills.
- Volatility targeted exit: exit when a position's trailing 24h move against it exceeds 1.5 times its hourly vol times sqrt(24). A stop expressed in vol units rather than a fixed return, so it adapts per pair. Tried as an add-on to ts_momentum's exit against the current data (2026-09-16): still failed the backtest cost coverage gate (-0.89, vs H0's own -0.96), a small improvement but not enough. Worth retrying once a challenger has actually run so there is live decisions.csv evidence of how ts_momentum's exit lags, rather than backtest-only.

## Ideas the evidence says not to bother with

- Anything that trades more than a few times per pair per day. P1.
- Parameter nudges of a few percent to the champion. They cannot be told apart from noise in a 21 day window, so they can only waste the slot.
