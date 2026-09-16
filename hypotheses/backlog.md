# Hypothesis backlog

Ideas waiting for the challenger slot. The agent may add to this file on any
run and should pick from it when the slot is free, taking the one with the
best cost arithmetic, not the one that looks best in the backtest. Remove an
idea when it becomes a ledger entry or when a result makes it moot.

## Candidates

- Regime filter for the momentum champion: only take entries when 7 day realised vol is below its 30 day median. Trend following in crypto tends to work worse in high vol chop, and skipping those entries removes the most expensive round trips.
- Longer horizon: 168 hour lookback with wider bands (entry +3%, exit −3%). Fewer, bigger moves; the cost per unit of captured move falls roughly in proportion.
- Cross sectional selection: hold only the top 3 of the 6 pairs by 7 day return instead of all pairs with a positive signal. Concentrates into the strongest trends, which in past crypto data carry most of the momentum premium.
- Weekend throttle: no new entries from Friday 20:00 UTC to Monday 00:00 UTC. Liquidity thins and spreads widen at the weekend, so the modelled 5 bps slippage understates the true cost of those fills.
- Volatility targeted exit: exit when a position's trailing 24h move against it exceeds 1.5 times its hourly vol times sqrt(24). A stop expressed in vol units rather than a fixed return, so it adapts per pair.
- Mean reversion at a long horizon: 240 hour window, entry z −2.5, exit z −0.5, on BTC and ETH only. The family P1 killed, but at ten times the horizon; the ledger entry must show the expected move is several hundred bps, not tens.

## Ideas the evidence says not to bother with

- Anything that trades more than a few times per pair per day. P1.
- Parameter nudges of a few percent to the champion. They cannot be told apart from noise in a 21 day window, so they can only waste the slot.
