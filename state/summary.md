# quantloop summary — generated 2026-10-29 20:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-22 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 1 pair day (the cap is 4 fills in one pair in one UTC day)
- champion, LINK, 2026-10-29: 4 fills (buy 02:10, sell 03:10, buy 11:10, buy 16:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 43.6 of 60, 16.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -11.28% (max drawdown -29.06%, 367 fills) vs challenger1 -6.87% (max drawdown -12.36%, 105 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.07% (usual 0.54, this window 0.53) vs challenger1 -8.79% (usual 0.37, this window 0.45); the rule compares on skill, daily edge t +0.34 over 44 days
  trades: its 34 finished trades made -3.82% of its starting equity after costs (20 won, 14 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.20 over 44 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +6.47%, equal weight basket of 10 pairs +5.18%, basket max drawdown -19%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 38.5 of 60, 21.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -22.79% (max drawdown -29.06%, 329 fills) vs challenger2 -9.46% (max drawdown -9.91%, 22 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -16.84% (usual 0.54, this window 0.51) vs challenger2 -6.31% (usual 0.29, this window 0.17); the rule compares on skill, daily edge t +1.42 over 38 days
  trades: its 7 finished trades made -6.94% of its starting equity after costs (0 won, 7 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.21 over 38 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -2.17%, equal weight basket of 10 pairs -11.01%, basket max drawdown -19%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 23.9 of 60, 36.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -20.16% (max drawdown -20.49%, 178 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.89% (usual 0.55, this window 0.38) vs challenger3 -0.79% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.22 over 24 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.74 over 24 days)
  fills: 10 in 23.9 days, 8 of them in the hour it began; at this pace about 18 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -6.03%, equal weight basket of 10 pairs -16.88%, basket max drawdown -19%, basket realised vol 54% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 13.9 of 120, 106.1 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -6.55% (max drawdown -10.30%, 18 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -2.88% (usual 0.53, this window 0.97); the rule compares on skill, daily edge t -0.73 over 14 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -9.84% so far
  trades: its 1 finished trade made +0.73% of its starting equity after costs (1 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.73 over 14 days)
  market over the window: BTC -1.92%, equal weight basket of 10 pairs -6.94%, basket max drawdown -10%, basket realised vol 48% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,871.84 (started 10,000 at 2026-09-16 03:55Z), net -11.28% since start
- 24h -3.62%, 7d -3.91%, 30d -23.20%, max drawdown -29.06%
- fills 367 total, 56 in the last 7d
- costs 815.90 (fees 540.81 + slippage 275.08); gross pnl -312.27; cost coverage -0.38
- cash -0.00; positions: BTC 0.0186912, DOGE 22825.3, ETH 0.644661, LINK 127.624, LTC 31.0344, XRP 694.317
- last run 2026-10-29 20:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.23% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.33% not above entry band +1.0%
- 2026-10-29 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 19:10Z LINK hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +2.86% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-29 19:10Z XRP none target 0.17 (held 0.10) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-29 19:10Z DOGE hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +2.90% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-29 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.96% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 19:10Z LTC hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +2.60% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-29 20:10Z BTC hold target 0.17 (held 0.17) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.07% vs exit band -1.0% and price above 24h EMA; realised vol 2...
- 2026-10-29 20:10Z ETH hold target 0.17 (held 0.17) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.88% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-29 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.60% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.40% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.77% not above entry band +1.0%
- 2026-10-29 20:10Z LINK hold target 0.17 (held 0.16) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +2.72% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-29 20:10Z XRP none target 0.17 (held 0.10) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-29 20:10Z DOGE hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +2.64% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-10-29 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.28% not above entry band +1.0% and price below 24h EMA
- 2026-10-29 20:10Z LTC hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +2.84% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 31 fills (14 buy / 17 sell), traded 41,277, gross pnl -90.33, -44 bps per round trip, avg half spread 2.1 bps
- AVAX: 41 fills (19 buy / 22 sell), traded 68,763, gross pnl +308.22, +90 bps per round trip, avg half spread 1.1 bps
- BTC: 35 fills (20 buy / 15 sell), traded 49,469, gross pnl -14.52, -6 bps per round trip, avg half spread 0.1 bps, open 0.0186912
- DOGE: 33 fills (17 buy / 16 sell), traded 42,615, gross pnl -202.33, -95 bps per round trip, avg half spread 0.7 bps, open 22825.3
- DOT: 39 fills (19 buy / 20 sell), traded 59,760, gross pnl -139.84, -47 bps per round trip, avg half spread 2.4 bps
- ETH: 37 fills (19 buy / 18 sell), traded 51,384, gross pnl -203.40, -79 bps per round trip, avg half spread 0.1 bps, open 0.644661
- LINK: 42 fills (22 buy / 20 sell), traded 69,285, gross pnl -349.98, -101 bps per round trip, avg half spread 1.9 bps, open 127.624
- LTC: 39 fills (19 buy / 20 sell), traded 54,133, gross pnl +485.75, +179 bps per round trip, avg half spread 1.6 bps, open 31.0344
- SOL: 36 fills (19 buy / 17 sell), traded 57,028, gross pnl -95.11, -33 bps per round trip, avg half spread 0.5 bps
- XRP: 34 fills (18 buy / 16 sell), traded 47,101, gross pnl -10.74, -5 bps per round trip, avg half spread 0.3 bps, open 694.317

last fills:

- 2026-10-29 04:10Z buy LTC 761 @ 56.9885 fee 0.76 slip 0.38 (half spread 1.8 bps)
- 2026-10-29 11:10Z sell DOGE 457 @ 0.0786025 fee 0.46 slip 0.23 (half spread 0.1 bps)
- 2026-10-29 11:10Z sell LTC 454 @ 57.8111 fee 0.45 slip 0.23 (half spread 1.7 bps)
- 2026-10-29 11:10Z buy LINK 909 @ 11.6099 fee 0.91 slip 0.45 (half spread 2.6 bps)
- 2026-10-29 16:10Z sell BTC 749 @ 81735.6 fee 0.75 slip 0.37 (half spread 0.0 bps)
- 2026-10-29 16:10Z sell ETH 757 @ 2369.82 fee 0.76 slip 0.38 (half spread 0.0 bps)
- 2026-10-29 16:10Z buy LINK 591 @ 11.9832 fee 0.59 slip 0.30 (half spread 2.1 bps)
- 2026-10-29 16:10Z buy XRP 912 @ 1.31321 fee 0.91 slip 0.46 (half spread 0.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,302.81 (started 10,000 at 2026-09-16 03:55Z), net -6.97% since start
- 24h -2.25%, 7d -3.30%, 30d -9.59%, max drawdown -12.36%
- fills 105 total, 29 in the last 7d
- costs 207.78 (fees 138.43 + slippage 69.35); gross pnl -489.40; cost coverage -2.36
- cash 4,719.90; positions: ADA 11493.5, DOT 2399.07
- last run 2026-10-29 20:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.03 not below -2.0
- 2026-10-29 19:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.06 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-29 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.86 not below -2.0
- 2026-10-29 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.32 not below -2.0
- 2026-10-29 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.10 not below -2.0
- 2026-10-29 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-10-29 19:10Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.26 vs 240h mean (entry -2.0, exit -0.5); vol 81% -> weight 0.25
- 2026-10-29 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.29 not below -2.0
- 2026-10-29 20:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.37 not below -2.0
- 2026-10-29 20:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.75 not below -2.0
- 2026-10-29 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.36 not below -2.0
- 2026-10-29 20:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: z -1.09 vs 240h mean (entry -2.0, exit -0.5); vol 60% -> weight 0.25
- 2026-10-29 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.83 not below -2.0
- 2026-10-29 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-10-29 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.27 not below -2.0
- 2026-10-29 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.15 not below -2.0
- 2026-10-29 20:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.25 vs 240h mean (entry -2.0, exit -0.5); vol 81% -> weight 0.25
- 2026-10-29 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.17 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (5 buy / 4 sell), traded 12,256, gross pnl -12.02, -20 bps per round trip, avg half spread 1.2 bps, open 11493.5
- AVAX: 12 fills (7 buy / 5 sell), traded 14,748, gross pnl +93.32, +127 bps per round trip, avg half spread 0.9 bps
- BTC: 7 fills (4 buy / 3 sell), traded 10,144, gross pnl +88.82, +175 bps per round trip, avg half spread 0.1 bps
- DOGE: 12 fills (6 buy / 6 sell), traded 17,820, gross pnl -128.15, -144 bps per round trip, avg half spread 0.3 bps
- DOT: 7 fills (4 buy / 3 sell), traded 9,531, gross pnl -326.34, -685 bps per round trip, avg half spread 1.4 bps, open 2399.07
- ETH: 13 fills (6 buy / 7 sell), traded 19,226, gross pnl +109.11, +114 bps per round trip, avg half spread 0.2 bps
- LINK: 12 fills (7 buy / 5 sell), traded 13,123, gross pnl +52.42, +80 bps per round trip, avg half spread 1.1 bps
- LTC: 12 fills (6 buy / 6 sell), traded 14,725, gross pnl +11.39, +15 bps per round trip, avg half spread 1.2 bps
- SOL: 12 fills (7 buy / 5 sell), traded 16,951, gross pnl -123.88, -146 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 9,910, gross pnl -254.09, -513 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-10-28 03:10Z buy DOT 612 @ 1.00045 fee 0.61 slip 0.31 (half spread 0.5 bps)
- 2026-10-28 03:10Z buy LTC 505 @ 57.4137 fee 0.51 slip 0.25 (half spread 0.9 bps)
- 2026-10-28 08:10Z sell SOL 1,905 @ 102.184 fee 1.90 slip 0.95 (half spread 0.5 bps)
- 2026-10-28 08:10Z sell LTC 1,895 @ 57.6262 fee 1.89 slip 0.95 (half spread 0.9 bps)
- 2026-10-28 08:10Z buy ADA 480 @ 0.206689 fee 0.48 slip 0.24 (half spread 0.7 bps)
- 2026-10-28 08:10Z buy AVAX 481 @ 9.02001 fee 0.48 slip 0.24 (half spread 0.6 bps)
- 2026-10-28 20:10Z sell AVAX 2,381 @ 9.03998 fee 2.38 slip 1.19 (half spread 0.6 bps)
- 2026-10-29 02:10Z buy DOT 492 @ 0.970635 fee 0.49 slip 0.25 (half spread 0.5 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 9,928.43 (started 10,000 at 2026-09-16 23:20Z), net -0.72% since start
- 24h -3.25%, 7d -3.97%, 30d -9.04%, max drawdown -10.62%
- fills 54 total, 11 in the last 7d
- costs 152.10 (fees 100.97 + slippage 51.13); gross pnl 80.53; cost coverage 0.53
- cash 512.71; positions: BTC 0.0251193, DOGE 31768.2, LINK 215.856, LTC 43.0817
- last run 2026-10-29 20:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 100.5 not above 120h high 103
- 2026-10-29 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.2023 not above 120h high 0.2087
- 2026-10-29 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.835 not above 120h high 9.042
- 2026-10-29 19:10Z LINK buy target 0.25 (held 0.10) — stay long: price 11.67 still above 72h low 11.27; realised vol 57% -> weight 0.25
- 2026-10-29 19:10Z XRP sell target 0.00 (held 0.25) — exit: closed 1.285 below 72h low 1.287
- 2026-10-29 19:10Z DOGE buy target 0.25 (held 0.20) — stay long: price 0.07924 still above 72h low 0.07688; realised vol 45% -> weight 0.25
- 2026-10-29 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9842 not above 120h high 1.052
- 2026-10-29 19:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 57.72 still above 72h low 56.05; realised vol 51% -> weight 0.25
- 2026-10-29 20:10Z BTC hold target 0.25 (held 0.20) — hold: weight change +0.047 below threshold 0.05 | stay long: price 8.074e+04 still above 72h low 7.953e+04; realised vol 29% -> weight 0.25
- 2026-10-29 20:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2335 not above 120h high 2370
- 2026-10-29 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 99.72 not above 120h high 103
- 2026-10-29 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.202 not above 120h high 0.2087
- 2026-10-29 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.841 not above 120h high 9.042
- 2026-10-29 20:10Z LINK hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 11.68 still above 72h low 11.27; realised vol 57% -> weight 0.25
- 2026-10-29 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.281 not above 120h high 1.337
- 2026-10-29 20:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 0.07917 still above 72h low 0.07688; realised vol 45% -> weight 0.25
- 2026-10-29 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.984 not above 120h high 1.052
- 2026-10-29 20:10Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 57.92 still above 72h low 56.05; realised vol 51% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 9 fills (5 buy / 4 sell), traded 19,247, gross pnl -146.23, -152 bps per round trip, avg half spread 0.0 bps, open 0.0251193
- DOGE: 8 fills (5 buy / 3 sell), traded 11,867, gross pnl -151.26, -255 bps per round trip, avg half spread 0.7 bps, open 31768.2
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 4 fills (3 buy / 1 sell), traded 5,535, gross pnl -25.35, -92 bps per round trip, avg half spread 2.4 bps, open 215.856
- LTC: 5 fills (3 buy / 2 sell), traded 9,981, gross pnl -17.24, -35 bps per round trip, avg half spread 2.5 bps, open 43.0817
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 6 fills (3 buy / 3 sell), traded 11,524, gross pnl -217.79, -378 bps per round trip, avg half spread 0.1 bps

last fills:

- 2026-10-28 17:10Z buy LTC 2,555 @ 59.2946 fee 2.55 slip 1.28 (half spread 0.8 bps)
- 2026-10-28 20:10Z buy BTC 2,579 @ 81410.7 fee 2.58 slip 1.29 (half spread 0.0 bps)
- 2026-10-29 16:10Z sell BTC 536 @ 81735.6 fee 0.54 slip 0.27 (half spread 0.0 bps)
- 2026-10-29 16:10Z sell DOGE 545 @ 0.0810415 fee 0.55 slip 0.27 (half spread 2.0 bps)
- 2026-10-29 16:10Z buy LINK 1,086 @ 11.9832 fee 1.09 slip 0.54 (half spread 2.1 bps)
- 2026-10-29 19:10Z sell XRP 2,485 @ 1.28014 fee 2.48 slip 1.24 (half spread 0.0 bps)
- 2026-10-29 19:10Z buy LINK 1,458 @ 11.6425 fee 1.46 slip 0.73 (half spread 2.2 bps)
- 2026-10-29 19:10Z buy DOGE 509 @ 0.0791227 fee 0.51 slip 0.25 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-29 20:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 19:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-29 19:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1973 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-29 19:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.586 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-29 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-29 19:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.267 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-29 19:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-29 19:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9697 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-29 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)
- 2026-10-29 20:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.948e+04 not a higher low vs prior low 8.011e+04 (need +10.0%)
- 2026-10-29 20:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2299 not a higher low vs prior low 2335 (need +10.0%)
- 2026-10-29 20:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 99.43 not a higher low vs prior low 100.7 (need +10.0%)
- 2026-10-29 20:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1973 not a higher low vs prior low 0.2117 (need +10.0%)
- 2026-10-29 20:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.586 not a higher low vs prior low 9.315 (need +10.0%)
- 2026-10-29 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.27 not a higher low vs prior low 11.56 (need +10.0%)
- 2026-10-29 20:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.267 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-10-29 20:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07566 not a higher low vs prior low 0.07626 (need +10.0%)
- 2026-10-29 20:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.9697 not a higher low vs prior low 1.048 (need +10.0%)
- 2026-10-29 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 55.7 not a higher low vs prior low 56.77 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 4 fills (2 buy / 2 sell), traded 7,389, gross pnl -111.53, -302 bps per round trip, avg half spread 0.7 bps
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)
- 2026-10-06 15:25Z buy AVAX 2,503 @ 11.5663 fee 2.50 slip 1.25 (half spread 0.4 bps)
- 2026-10-07 22:22Z sell AVAX 2,381 @ 11.0025 fee 2.38 slip 1.19 (half spread 0.9 bps)

## challenger4: relative_reversion (H6)

params: {"entry_z": 2.0, "exit_z": 0.25, "max_weight": 0.25, "ratio_hours": 720, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,341.40 (started 10,000 at 2026-10-13 17:26Z), net -6.59% since start
- 24h -3.77%, 7d -4.68%, 30d -6.59%, max drawdown -10.30%
- fills 18 total, 5 in the last 7d
- costs 29.22 (fees 19.48 + slippage 9.74); gross pnl -629.38; cost coverage -21.54
- cash -0.00; positions: ADA 6863.3, AVAX 154.27, DOGE 20854.4, DOT 1030.18, ETH 0.582751, SOL 13.5467, XRP 1066.7
- last run 2026-10-29 20:10Z; halted today: False

last decisions (newest last):

- 2026-10-29 19:10Z SOL hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.26 vs 720h mean (entry -2.0, exit -0.25); vol 43% -> weigh...
- 2026-10-29 19:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -1.63 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-10-29 19:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.59 vs 720h mean (entry -2.0, exit -0.25); vol 56% -> weigh...
- 2026-10-29 19:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.08 not below -2.0
- 2026-10-29 19:10Z XRP hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.14 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-29 19:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.031 below threshold 0.05 | stay long: ratio to BTC z -0.73 vs 720h mean (entry -2.0, exit -0.25); vol 45% -> weigh...
- 2026-10-29 19:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.036 below threshold 0.05 | stay long: ratio to BTC z -2.25 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...
- 2026-10-29 19:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.00 not below -2.0
- 2026-10-29 20:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-10-29 20:10Z ETH hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: ratio to BTC z -1.25 vs 720h mean (entry -2.0, exit -0.25); vol 40% -> weigh...
- 2026-10-29 20:10Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.41 vs 720h mean (entry -2.0, exit -0.25); vol 43% -> weigh...
- 2026-10-29 20:10Z ADA hold target 0.14 (held 0.15) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -1.65 vs 720h mean (entry -2.0, exit -0.25); vol 60% -> weigh...
- 2026-10-29 20:10Z AVAX hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.58 vs 720h mean (entry -2.0, exit -0.25); vol 56% -> weigh...
- 2026-10-29 20:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.07 not below -2.0
- 2026-10-29 20:10Z XRP hold target 0.14 (held 0.14) — hold: weight change -0.002 below threshold 0.05 | stay long: ratio to BTC z -1.22 vs 720h mean (entry -2.0, exit -0.25); vol 41% -> weigh...
- 2026-10-29 20:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.031 below threshold 0.05 | stay long: ratio to BTC z -0.74 vs 720h mean (entry -2.0, exit -0.25); vol 45% -> weigh...
- 2026-10-29 20:10Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.037 below threshold 0.05 | stay long: ratio to BTC z -2.23 vs 720h mean (entry -2.0, exit -0.25); vol 81% -> weigh...
- 2026-10-29 20:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.92 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (2 buy / 0 sell), traded 1,502, gross pnl -140.82, -1875 bps per round trip, avg half spread 1.6 bps, open 6863.3
- AVAX: 2 fills (2 buy / 0 sell), traded 1,424, gross pnl -84.89, -1192 bps per round trip, avg half spread 1.9 bps, open 154.27
- DOGE: 2 fills (1 buy / 1 sell), traded 3,263, gross pnl -109.82, -673 bps per round trip, avg half spread 0.1 bps, open 20854.4
- DOT: 3 fills (2 buy / 1 sell), traded 2,672, gross pnl -9.87, -74 bps per round trip, avg half spread 2.1 bps, open 1030.18
- ETH: 3 fills (1 buy / 2 sell), traded 3,537, gross pnl -115.94, -656 bps per round trip, avg half spread 0.6 bps, open 0.582751
- SOL: 3 fills (1 buy / 2 sell), traded 3,527, gross pnl -95.90, -544 bps per round trip, avg half spread 0.5 bps, open 13.5467
- XRP: 3 fills (1 buy / 2 sell), traded 3,557, gross pnl -72.14, -406 bps per round trip, avg half spread 0.6 bps, open 1066.7

last fills:

- 2026-10-18 20:10Z buy DOT 761 @ 1.05068 fee 0.76 slip 0.38 (half spread 1.4 bps)
- 2026-10-19 16:10Z sell DOT 836 @ 1.15392 fee 0.84 slip 0.42 (half spread 2.6 bps)
- 2026-10-19 16:10Z buy AVAX 834 @ 9.5953 fee 0.83 slip 0.42 (half spread 1.6 bps)
- 2026-10-24 15:10Z sell ETH 544 @ 2316.84 fee 0.54 slip 0.27 (half spread 1.6 bps)
- 2026-10-24 15:10Z sell SOL 552 @ 99.6651 fee 0.55 slip 0.28 (half spread 0.5 bps)
- 2026-10-24 15:10Z sell XRP 573 @ 1.2657 fee 0.57 slip 0.29 (half spread 0.0 bps)
- 2026-10-24 15:10Z buy AVAX 590 @ 8.76038 fee 0.59 slip 0.29 (half spread 2.3 bps)
- 2026-10-24 15:10Z buy DOT 1,076 @ 1.04407 fee 1.08 slip 0.54 (half spread 2.4 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1769 candles, 2026-08-17 03:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1769 candles, 2026-08-17 03:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1769 candles, 2026-08-17 03:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1769 candles, 2026-08-17 03:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- AVAX: live 1769 candles, 2026-08-17 03:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LINK: live 1769 candles, 2026-08-17 03:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.2 bps
- XRP: live 1741 candles, 2026-08-18 07:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1741 candles, 2026-08-18 07:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- DOT: live 1741 candles, 2026-08-18 07:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LTC: live 1741 candles, 2026-08-18 07:00Z to 2026-10-29 19:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
