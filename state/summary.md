# quantloop summary — generated 2026-10-07 15:36Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 21.4 of 60, 38.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +5.76% (max drawdown -15.43%, 208 fills) vs challenger1 +1.97% (max drawdown -2.47%, 23 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.31% (usual 0.54, this window 0.72) vs challenger1 -5.66% (usual 0.37, this window 0.12); the rule compares on skill, daily edge t -0.11 over 21 days
  trades: its 5 finished trades made +3.98% of its starting equity after costs (5 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.20 over 21 days)
  two look rule (measured, not applied to this test): on today's numbers it would be kept at day 60 on the value of its trades without passing the rule, the same as under its own rule. From there the two rules are one: 60 more days, and a promotion asks for a daily skill t of 1.0 over all 120 (its daily skill t is -1.20 so far)
  market over the window: BTC +9.41%, equal weight basket of 10 pairs +20.58%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 16.3 of 60, 43.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.95% (max drawdown -15.43%, 170 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.83% (usual 0.54, this window 0.73) vs challenger2 -2.19% (usual 0.29, this window 0.22); the rule compares on skill, daily edge t +0.88 over 16 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.87 over 16 days)
  fills: 4 in 16.3 days; at this pace about 29 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +0.54%, equal weight basket of 10 pairs +1.61%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 1.7 of 60, 58.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.82% (max drawdown -5.22%, 19 fills) vs challenger3 -0.93% (max drawdown -1.52%, 9 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.99% (usual 0.55, this window 0.71) vs challenger3 -0.78% (usual 0.03, this window 0.14); the rule compares on skill
  trades: it has finished no trade of its own: none of its 9 fills closed a position it had bought or had chosen to keep, so the -0.93% it shows is not from an exit it chose. A test that has finished no trade of its own by its look is killed
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -3.43%, equal weight basket of 10 pairs -5.15%, basket max drawdown -6%, basket realised vol 47% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 11.7 of 60, 48.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.49% (max drawdown -15.43%, 142 fills) vs challenger4 -4.17% (max drawdown -5.87%, 12 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.21% (usual 0.55, this window 0.70) vs challenger4 -2.19% (usual 0.48, this window 0.99); the rule compares on skill, daily edge t +2.19 over 12 days
  trades: its 2 finished trades made -1.66% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.73 over 12 days)
  fills: 12 in 11.7 days, 10 of them in the hour it began; at this pace about 20 by day 60, under the 30 a promotion there needs, and about 30 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -1.09%, equal weight basket of 10 pairs -4.16%, basket max drawdown -6%, basket realised vol 53% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,576.23 (started 10,000 at 2026-09-16 03:55Z), net +5.76% since start
- 24h -4.62%, 7d -5.96%, 30d +5.76%, max drawdown -15.43%
- fills 208 total, 105 in the last 7d
- costs 480.55 (fees 318.31 + slippage 162.24); gross pnl 1,056.78; cost coverage 2.20
- cash 10,576.23; positions: none
- last run 2026-10-07 15:36Z; halted today: False

last decisions (newest last):

- 2026-10-07 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.52% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-07 14:27Z AVAX none target 0.25 (held 0.00) — capped: 4 fills in AVAX today, the limit is 4 a day, so no new buys until the next UTC day (sells are never capped) | enter long: 72h ret...
- 2026-10-07 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.70% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.53% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.36% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.01% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.69% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.98% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.90% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-07 15:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-07 15:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.47% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.06% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.24% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.77% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 15:36Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.32% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (9 buy / 12 sell), traded 30,528, gross pnl +54.04, +35 bps per round trip, avg half spread 2.2 bps
- AVAX: 30 fills (13 buy / 17 sell), traded 54,282, gross pnl +498.76, +184 bps per round trip, avg half spread 1.2 bps
- BTC: 15 fills (7 buy / 8 sell), traded 19,440, gross pnl +105.45, +108 bps per round trip, avg half spread 0.2 bps
- DOGE: 20 fills (10 buy / 10 sell), traded 27,173, gross pnl -175.84, -129 bps per round trip, avg half spread 1.1 bps
- DOT: 23 fills (11 buy / 12 sell), traded 28,978, gross pnl +68.78, +47 bps per round trip, avg half spread 2.6 bps
- ETH: 16 fills (6 buy / 10 sell), traded 25,082, gross pnl -30.95, -25 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 22 fills (9 buy / 13 sell), traded 33,431, gross pnl +545.56, +326 bps per round trip, avg half spread 1.8 bps
- SOL: 21 fills (11 buy / 10 sell), traded 34,513, gross pnl +17.41, +10 bps per round trip, avg half spread 0.5 bps
- XRP: 18 fills (9 buy / 9 sell), traded 26,463, gross pnl +138.10, +104 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-07 02:24Z buy AVAX 1,259 @ 11.1096 fee 1.26 slip 0.63 (half spread 1.8 bps)
- 2026-10-07 02:24Z buy XRP 1,310 @ 1.4578 fee 1.31 slip 0.65 (half spread 0.2 bps)
- 2026-10-07 03:25Z sell BTC 2,663 @ 84007.1 fee 2.66 slip 1.33 (half spread 0.0 bps)
- 2026-10-07 03:25Z sell SOL 2,671 @ 118.276 fee 2.67 slip 1.34 (half spread 0.4 bps)
- 2026-10-07 03:25Z sell AVAX 2,630 @ 10.985 fee 2.63 slip 1.32 (half spread 0.5 bps)
- 2026-10-07 03:25Z sell XRP 2,656 @ 1.46281 fee 2.66 slip 1.33 (half spread 0.0 bps)
- 2026-10-07 08:28Z buy AVAX 2,652 @ 11.2336 fee 2.65 slip 1.33 (half spread 0.9 bps)
- 2026-10-07 10:27Z sell AVAX 2,625 @ 11.1159 fee 2.62 slip 1.31 (half spread 1.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,185.84 (started 10,000 at 2026-09-16 03:55Z), net +1.86% since start
- 24h -2.03%, 7d -1.01%, 30d +1.86%, max drawdown -2.47%
- fills 23 total, 15 in the last 7d
- costs 65.52 (fees 43.68 + slippage 21.84); gross pnl 251.37; cost coverage 3.84
- cash 0.00; positions: DOGE 19195.1, DOT 1541.15, ETH 0.567281, LINK 76.9551, LTC 17.4878, SOL 14.5071, XRP 1016.78
- last run 2026-10-07 15:36Z; halted today: False

last decisions (newest last):

- 2026-10-07 14:27Z SOL hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.46 vs 240h mean (entry -2.0, exit -0.5); vol 44% -> weight 0.25
- 2026-10-07 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.23 not below -2.0
- 2026-10-07 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.88 not below -2.0
- 2026-10-07 14:27Z LINK none target 0.17 (held 0.10) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-07 14:27Z XRP hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: z -3.70 vs 240h mean (entry -2.0, exit -0.5); vol 43% -> weight 0.25
- 2026-10-07 14:27Z DOGE hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: z -3.41 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-07 14:27Z DOT hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.94 vs 240h mean (entry -2.0, exit -0.5); vol 86% -> weight 0.25
- 2026-10-07 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.64 not below -2.0
- 2026-10-07 15:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.59 not below -2.0
- 2026-10-07 15:36Z ETH sell target 0.14 (held 0.20) — stay long: z -4.10 vs 240h mean (entry -2.0, exit -0.5); vol 34% -> weight 0.25
- 2026-10-07 15:36Z SOL hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -2.67 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-07 15:36Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.06 not below -2.0
- 2026-10-07 15:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.67 not below -2.0
- 2026-10-07 15:36Z LINK hold target 0.14 (held 0.10) — hold: weight change +0.042 below threshold 0.05 | stay long: z -1.98 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-07 15:36Z XRP sell target 0.14 (held 0.20) — stay long: z -3.95 vs 240h mean (entry -2.0, exit -0.5); vol 41% -> weight 0.25
- 2026-10-07 15:36Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -3.55 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-07 15:36Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -3.00 vs 240h mean (entry -2.0, exit -0.5); vol 86% -> weight 0.25
- 2026-10-07 15:36Z LTC buy target 0.14 (held 0.00) — enter long: z -2.09 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- DOGE: 4 fills (2 buy / 2 sell), traded 8,707, gross pnl +68.19, +157 bps per round trip, avg half spread 0.3 bps, open 19195.1
- DOT: 2 fills (1 buy / 1 sell), traded 3,428, gross pnl -49.21, -287 bps per round trip, avg half spread 0.4 bps, open 1541.15
- ETH: 5 fills (2 buy / 3 sell), traded 8,747, gross pnl +8.45, +19 bps per round trip, avg half spread 0.1 bps, open 0.567281
- LINK: 1 fill (1 buy / 0 sell), traded 1,027, gross pnl +3.13, +61 bps per round trip, avg half spread 1.5 bps, open 76.9551
- LTC: 1 fill (1 buy / 0 sell), traded 1,158, gross pnl -0.00, -0 bps per round trip, avg half spread 0.8 bps, open 17.4878
- SOL: 3 fills (2 buy / 1 sell), traded 6,771, gross pnl +91.70, +271 bps per round trip, avg half spread 0.5 bps, open 14.5071
- XRP: 3 fills (1 buy / 2 sell), traded 3,689, gross pnl -52.23, -283 bps per round trip, avg half spread 0.3 bps, open 1016.78

last fills:

- 2026-10-07 12:32Z sell XRP 516 @ 1.44455 fee 0.52 slip 0.26 (half spread 0.8 bps)
- 2026-10-07 12:32Z buy LINK 1,027 @ 13.3486 fee 1.03 slip 0.51 (half spread 1.5 bps)
- 2026-10-07 13:28Z sell DOGE 850 @ 0.0884213 fee 0.85 slip 0.43 (half spread 0.3 bps)
- 2026-10-07 13:28Z sell DOT 839 @ 1.1013 fee 0.84 slip 0.42 (half spread 0.5 bps)
- 2026-10-07 13:28Z buy SOL 1,686 @ 116.193 fee 1.69 slip 0.84 (half spread 0.4 bps)
- 2026-10-07 15:36Z sell ETH 587 @ 2564.15 fee 0.59 slip 0.29 (half spread 0.0 bps)
- 2026-10-07 15:36Z sell XRP 574 @ 1.43059 fee 0.57 slip 0.29 (half spread 0.1 bps)
- 2026-10-07 15:36Z buy LTC 1,158 @ 66.2181 fee 1.16 slip 0.58 (half spread 0.8 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h -1.49%, 7d -0.92%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-07 15:36Z; halted today: False

last decisions (newest last):

- 2026-10-07 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 116.2 not above 120h high 122
- 2026-10-07 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.42 not above 120h high 14.36
- 2026-10-07 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.433 not above 120h high 1.532
- 2026-10-07 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 15:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.298e+04 not above 120h high 8.663e+04
- 2026-10-07 15:36Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2563 not above 120h high 2731
- 2026-10-07 15:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 115.8 not above 120h high 121.8
- 2026-10-07 15:36Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 15:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 15:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.38 not above 120h high 14.28
- 2026-10-07 15:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.426 not above 120h high 1.523
- 2026-10-07 15:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 15:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 15:36Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 5 fills (3 buy / 2 sell), traded 10,806, gross pnl -58.08, -108 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)
- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)
- 2026-09-30 13:27Z buy BTC 2,737 @ 85327.3 fee 2.74 slip 1.37 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell BTC 2,689 @ 83812.2 fee 2.69 slip 1.34 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell ETH 2,611 @ 2609.08 fee 2.61 slip 1.31 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,917.59 (started 10,000 at 2026-10-05 05:28Z), net -0.82% since start
- 24h -0.68%, 7d -0.79%, 30d -0.79%, max drawdown -1.89%
- fills 25 total, 25 in the last 7d
- costs 55.56 (fees 37.00 + slippage 18.56); gross pnl -26.85; cost coverage -0.48
- cash 7,505.37; positions: AVAX 216.372
- last run 2026-10-07 15:36Z; halted today: False

last decisions (newest last):

- 2026-10-07 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 116.2 not a fresh close above reaction high 124.4
- 2026-10-07 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.255 not a fresh close above reaction high 0.2616
- 2026-10-07 14:27Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: price 11.28 still above the 48h low 10.85; realised vol 73% -> weight 0.25
- 2026-10-07 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.42 not a fresh close above reaction high 15.46
- 2026-10-07 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.433 not a fresh close above reaction high 1.638
- 2026-10-07 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08873 not a higher low vs prior low 0.08128 (need +10.0%)
- 2026-10-07 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.105 not a higher low vs prior low 1.034 (need +10.0%)
- 2026-10-07 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 66.8 not a fresh close above reaction high 74.29
- 2026-10-07 15:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.635e+04 (need +10.0%)
- 2026-10-07 15:36Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2569 not a higher low vs prior low 2444 (need +10.0%)
- 2026-10-07 15:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 115.8 not a fresh close above reaction high 124.4
- 2026-10-07 15:36Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2533 not a fresh close above reaction high 0.2616
- 2026-10-07 15:36Z AVAX hold target 0.25 (held 0.24) — hold: weight change +0.007 below threshold 0.05 | stay long: price 11.22 still above the 48h low 10.85; realised vol 71% -> weight 0.25
- 2026-10-07 15:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.38 not a fresh close above reaction high 15.46
- 2026-10-07 15:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.426 not a fresh close above reaction high 1.638
- 2026-10-07 15:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08855 not a higher low vs prior low 0.08136 (need +10.0%)
- 2026-10-07 15:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.104 not a higher low vs prior low 1.034 (need +10.0%)
- 2026-10-07 15:36Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 66.12 not a fresh close above reaction high 74.29

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 3 fills (2 buy / 1 sell), traded 5,009, gross pnl -81.12, -324 bps per round trip, avg half spread 0.6 bps, open 216.372
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell ETH 1,250 @ 2715.8 fee 1.25 slip 0.63 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)
- 2026-10-06 15:25Z buy AVAX 2,503 @ 11.5663 fee 2.50 slip 1.25 (half spread 0.4 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,825.94 (started 10,000 at 2026-09-25 04:23Z), net -1.74% since start
- 24h -4.94%, 7d -3.60%, 30d -1.67%, max drawdown -5.87%
- fills 25 total, 2 in the last 7d
- costs 44.42 (fees 29.54 + slippage 14.88); gross pnl -129.64; cost coverage -2.92
- cash 1,900.42; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-07 15:36Z; halted today: False

last decisions (newest last):

- 2026-10-07 14:27Z SOL hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 720h return +10.56% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 14:27Z ADA hold target 0.12 (held 0.10) — hold: weight change +0.020 below threshold 0.05 | stay long: 720h return +14.52% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 14:27Z AVAX hold target 0.12 (held 0.10) — hold: weight change +0.026 below threshold 0.05 | stay long: 720h return +39.46% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 14:27Z LINK hold target 0.12 (held 0.10) — hold: weight change +0.022 below threshold 0.05 | stay long: 720h return +2.11% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 14:27Z XRP hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +2.16% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -2.63% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +4.36% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 14:27Z LTC hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +16.23% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 15:36Z BTC hold target 0.12 (held 0.10) — hold: weight change +0.020 below threshold 0.05 | stay long: 720h return +4.80% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 15:36Z ETH hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 720h return +2.93% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 15:36Z SOL hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 720h return +10.70% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 15:36Z ADA hold target 0.12 (held 0.11) — hold: weight change +0.019 below threshold 0.05 | stay long: 720h return +14.27% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 15:36Z AVAX hold target 0.12 (held 0.10) — hold: weight change +0.027 below threshold 0.05 | stay long: 720h return +39.07% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 15:36Z LINK hold target 0.12 (held 0.10) — hold: weight change +0.022 below threshold 0.05 | stay long: 720h return +2.47% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 15:36Z XRP hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +1.96% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 15:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -2.71% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 15:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +2.98% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 15:36Z LTC hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +15.94% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +72.72, +362 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fill (1 buy / 0 sell), traded 907, gross pnl +51.85, +1143 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fill (1 buy / 0 sell), traded 1,040, gross pnl -8.48, -163 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 4 fills (2 buy / 2 sell), traded 4,028, gross pnl -51.07, -254 bps per round trip, avg half spread 2.0 bps
- ETH: 1 fill (1 buy / 0 sell), traded 1,040, gross pnl -46.96, -903 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +65.00, +321 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -60.70, -305 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -28.65, -238 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl -22.74, -75 bps per round trip, avg half spread 0.7 bps, open 665.342

last fills:

- 2026-09-25 22:21Z sell LTC 719 @ 72.2139 fee 0.72 slip 0.36 (half spread 2.8 bps)
- 2026-09-25 22:21Z buy BTC 1,040 @ 83966.2 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-09-25 22:21Z buy ETH 1,040 @ 2688.17 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-09-25 22:21Z buy AVAX 907 @ 10.5508 fee 0.91 slip 0.45 (half spread 0.5 bps)
- 2026-09-25 22:21Z buy XRP 1,040 @ 1.5631 fee 1.04 slip 0.52 (half spread 1.0 bps)
- 2026-09-25 22:21Z buy DOGE 1,031 @ 0.0985782 fee 1.03 slip 0.52 (half spread 0.1 bps)
- 2026-10-07 03:25Z sell DOT 973 @ 1.12289 fee 0.97 slip 0.49 (half spread 0.4 bps)
- 2026-10-07 12:32Z sell DOGE 929 @ 0.0888629 fee 0.93 slip 0.46 (half spread 0.1 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1236 candles, 2026-08-17 03:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1236 candles, 2026-08-17 03:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1236 candles, 2026-08-17 03:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1236 candles, 2026-08-17 03:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- AVAX: live 1236 candles, 2026-08-17 03:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- LINK: live 1236 candles, 2026-08-17 03:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- XRP: live 1208 candles, 2026-08-18 07:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.4 bps
- DOGE: live 1208 candles, 2026-08-18 07:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1208 candles, 2026-08-18 07:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- LTC: live 1208 candles, 2026-08-18 07:00Z to 2026-10-07 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
