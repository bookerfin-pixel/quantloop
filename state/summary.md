# quantloop summary — generated 2026-10-08 04:26Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 22.0 of 60, 38.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +5.76% (max drawdown -15.43%, 208 fills) vs challenger1 +0.93% (max drawdown -3.40%, 23 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.00% (usual 0.54, this window 0.70) vs challenger1 -6.49% (usual 0.37, this window 0.14); the rule compares on skill, daily edge t -0.19 over 22 days
  trades: its 5 finished trades made +3.98% of its starting equity after costs (5 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.24 over 22 days)
  two look rule (measured, not applied to this test): on today's numbers it would be kept at day 60 on the value of its trades without passing the rule, the same as under its own rule. From there the two rules are one: 60 more days, and a promotion asks for a daily skill t of 1.0 over all 120 (its daily skill t is -1.24 so far)
  market over the window: BTC +9.04%, equal weight basket of 10 pairs +20.00%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 16.8 of 60, 43.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.95% (max drawdown -15.43%, 170 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.58% (usual 0.54, this window 0.71) vs challenger2 -2.06% (usual 0.29, this window 0.21); the rule compares on skill, daily edge t +0.85 over 17 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.76 over 17 days)
  fills: 4 in 16.8 days; at this pace about 28 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +0.20%, equal weight basket of 10 pairs +1.17%, basket max drawdown -7%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 2.3 of 60, 57.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.82% (max drawdown -5.22%, 19 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.76% (usual 0.55, this window 0.54) vs challenger3 -1.11% (usual 0.03, this window 0.14); the rule compares on skill
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -3.76%, equal weight basket of 10 pairs -5.58%, basket max drawdown -7%, basket realised vol 44% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 12.3 of 60, 47.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.49% (max drawdown -15.43%, 142 fills) vs challenger4 -5.19% (max drawdown -6.81%, 20 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.97% (usual 0.55, this window 0.67) vs challenger4 -3.00% (usual 0.48, this window 0.98); the rule compares on skill, daily edge t +1.77 over 12 days
  trades: its 4 finished trades made -3.16% of its starting equity after costs (0 won, 4 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.83 over 12 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -1.42%, equal weight basket of 10 pairs -4.59%, basket max drawdown -7%, basket realised vol 52% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,576.23 (started 10,000 at 2026-09-16 03:55Z), net +5.76% since start
- 24h -0.31%, 7d -6.11%, 30d +5.76%, max drawdown -15.43%
- fills 208 total, 97 in the last 7d
- costs 480.55 (fees 318.31 + slippage 162.24); gross pnl 1,056.78; cost coverage 2.20
- cash 10,576.23; positions: none
- last run 2026-10-08 04:26Z; halted today: False

last decisions (newest last):

- 2026-10-08 03:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.92% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.33% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.40% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.38% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.13% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.52% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.81% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 03:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.28% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.90% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.63% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.93% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.44% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.37% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.93% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.27% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.62% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.13% not above entry band +1.0% and price below 24h EMA
- 2026-10-08 04:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.49% not above entry band +1.0% and price below 24h EMA

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

- equity 10,081.76 (started 10,000 at 2026-09-16 03:55Z), net +0.82% since start
- 24h -3.08%, 7d -2.02%, 30d +0.82%, max drawdown -3.40%
- fills 23 total, 15 in the last 7d
- costs 65.52 (fees 43.68 + slippage 21.84); gross pnl 147.28; cost coverage 2.25
- cash 0.00; positions: DOGE 19195.1, DOT 1541.15, ETH 0.567281, LINK 76.9551, LTC 17.4878, SOL 14.5071, XRP 1016.78
- last run 2026-10-08 04:26Z; halted today: False

last decisions (newest last):

- 2026-10-08 03:25Z SOL hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -1.95 vs 240h mean (entry -2.0, exit -0.5); vol 40% -> weight 0.25
- 2026-10-08 03:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.40 not below -2.0
- 2026-10-08 03:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.13 not below -2.0
- 2026-10-08 03:25Z LINK hold target 0.14 (held 0.10) — hold: weight change +0.043 below threshold 0.05 | stay long: z -2.00 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-08 03:25Z XRP hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.83 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-08 03:25Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.025 below threshold 0.05 | stay long: z -2.43 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-08 03:25Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.026 below threshold 0.05 | stay long: z -2.01 vs 240h mean (entry -2.0, exit -0.5); vol 85% -> weight 0.25
- 2026-10-08 03:25Z LTC hold target 0.14 (held 0.11) — hold: weight change +0.030 below threshold 0.05 | stay long: z -1.84 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-10-08 04:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.74 not below -2.0
- 2026-10-08 04:26Z ETH hold target 0.14 (held 0.14) — hold: weight change -0.002 below threshold 0.05 | stay long: z -2.94 vs 240h mean (entry -2.0, exit -0.5); vol 34% -> weight 0.25
- 2026-10-08 04:26Z SOL hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -2.42 vs 240h mean (entry -2.0, exit -0.5); vol 40% -> weight 0.25
- 2026-10-08 04:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.14 not below -2.0
- 2026-10-08 04:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.21 not below -2.0
- 2026-10-08 04:26Z LINK hold target 0.14 (held 0.10) — hold: weight change +0.043 below threshold 0.05 | stay long: z -2.16 vs 240h mean (entry -2.0, exit -0.5); vol 53% -> weight 0.25
- 2026-10-08 04:26Z XRP hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: z -3.14 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-08 04:26Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -2.59 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-08 04:26Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.025 below threshold 0.05 | stay long: z -2.31 vs 240h mean (entry -2.0, exit -0.5); vol 85% -> weight 0.25
- 2026-10-08 04:26Z LTC hold target 0.14 (held 0.11) — hold: weight change +0.030 below threshold 0.05 | stay long: z -2.13 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- DOGE: 4 fills (2 buy / 2 sell), traded 8,707, gross pnl +49.23, +113 bps per round trip, avg half spread 0.3 bps, open 19195.1
- DOT: 2 fills (1 buy / 1 sell), traded 3,428, gross pnl -52.68, -307 bps per round trip, avg half spread 0.4 bps, open 1541.15
- ETH: 5 fills (2 buy / 3 sell), traded 8,747, gross pnl +9.83, +22 bps per round trip, avg half spread 0.1 bps, open 0.567281
- LINK: 1 fill (1 buy / 0 sell), traded 1,027, gross pnl -17.02, -331 bps per round trip, avg half spread 1.5 bps, open 76.9551
- LTC: 1 fill (1 buy / 0 sell), traded 1,158, gross pnl -20.29, -350 bps per round trip, avg half spread 0.8 bps, open 17.4878
- SOL: 3 fills (2 buy / 1 sell), traded 6,771, gross pnl +75.74, +224 bps per round trip, avg half spread 0.5 bps, open 14.5071
- XRP: 3 fills (1 buy / 2 sell), traded 3,689, gross pnl -78.87, -428 bps per round trip, avg half spread 0.3 bps, open 1016.78

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
- 24h +0.00%, 7d -1.12%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-08 04:26Z; halted today: False

last decisions (newest last):

- 2026-10-08 03:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 116.4 not above 120h high 121.8
- 2026-10-08 03:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 03:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 03:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.26 not above 120h high 14.28
- 2026-10-08 03:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.425 not above 120h high 1.523
- 2026-10-08 03:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 03:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 03:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 04:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.27e+04 not above 120h high 8.663e+04
- 2026-10-08 04:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2563 not above 120h high 2731
- 2026-10-08 04:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 115.7 not above 120h high 121.8
- 2026-10-08 04:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 04:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 04:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.17 not above 120h high 14.28
- 2026-10-08 04:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.416 not above 120h high 1.523
- 2026-10-08 04:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 04:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-08 04:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h -0.26%, 7d -1.13%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 26 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-08 04:26Z; halted today: False

last decisions (newest last):

- 2026-10-08 03:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 116.4 not a fresh close above reaction high 124.4
- 2026-10-08 03:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2567 not a fresh close above reaction high 0.2616
- 2026-10-08 03:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.08 not a fresh close above reaction high 11.55
- 2026-10-08 03:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.26 not a fresh close above reaction high 15.46
- 2026-10-08 03:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.414 not a higher low vs prior low 1.305 (need +10.0%)
- 2026-10-08 03:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08815 not a higher low vs prior low 0.08274 (need +10.0%)
- 2026-10-08 03:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.096 not a higher low vs prior low 1.075 (need +10.0%)
- 2026-10-08 03:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 66.06 not a fresh close above reaction high 74.29
- 2026-10-08 04:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.73e+04 (need +10.0%)
- 2026-10-08 04:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2550 not a higher low vs prior low 2477 (need +10.0%)
- 2026-10-08 04:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 115.7 not a fresh close above reaction high 124.4
- 2026-10-08 04:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2541 not a fresh close above reaction high 0.2616
- 2026-10-08 04:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.98 not a fresh close above reaction high 11.55
- 2026-10-08 04:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.17 not a fresh close above reaction high 15.46
- 2026-10-08 04:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.414 not a higher low vs prior low 1.317 (need +10.0%)
- 2026-10-08 04:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08815 not a higher low vs prior low 0.08409 (need +10.0%)
- 2026-10-08 04:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.096 not a higher low vs prior low 1.075 (need +10.0%)
- 2026-10-08 04:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 65.58 not a fresh close above reaction high 74.29

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

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,721.65 (started 10,000 at 2026-09-25 04:23Z), net -2.78% since start
- 24h -2.40%, 7d -4.93%, 30d -2.71%, max drawdown -6.81%
- fills 33 total, 10 in the last 7d
- costs 53.11 (fees 35.29 + slippage 17.82); gross pnl -225.24; cost coverage -4.24
- cash 0.00; positions: ADA 6386.82, AVAX 149.711, BTC 0.0196004, ETH 0.631331, LTC 24.8496, SOL 14.0611
- last run 2026-10-08 04:26Z; halted today: False

last decisions (newest last):

- 2026-10-08 03:25Z SOL hold target 0.14 (held 0.10) — hold: weight change +0.042 below threshold 0.05 | stay long: 720h return +12.72% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-08 03:25Z ADA hold target 0.14 (held 0.11) — hold: weight change +0.037 below threshold 0.05 | stay long: 720h return +18.00% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-08 03:25Z AVAX hold target 0.14 (held 0.10) — hold: weight change +0.046 below threshold 0.05 | stay long: 720h return +37.91% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-08 03:25Z LINK hold target 0.14 (held 0.10) — hold: weight change +0.041 below threshold 0.05 | stay long: 720h return +4.95% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-08 03:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +2.43% not above entry band +5.0% and price below 168h EMA
- 2026-10-08 03:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -1.08% not above entry band +5.0% and price below 168h EMA
- 2026-10-08 03:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-08 03:25Z LTC hold target 0.14 (held 0.10) — hold: weight change +0.046 below threshold 0.05 | stay long: 720h return +19.67% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-08 04:26Z BTC buy target 0.17 (held 0.11) — stay long: 720h return +4.81% vs exit band -5.0% and price within 5.0% of 168h EMA; realised vol 30% -> weight 0.25
- 2026-10-08 04:26Z ETH buy target 0.17 (held 0.10) — stay long: 720h return +3.10% vs exit band -5.0% and price within 5.0% of 168h EMA; realised vol 34% -> weight 0.25
- 2026-10-08 04:26Z SOL buy target 0.17 (held 0.10) — stay long: 720h return +11.90% vs exit band -5.0% and price within 5.0% of 168h EMA; realised vol 40% -> weight 0.25
- 2026-10-08 04:26Z ADA buy target 0.17 (held 0.11) — stay long: 720h return +16.27% vs exit band -5.0% and price within 5.0% of 168h EMA; realised vol 82% -> weight 0.25
- 2026-10-08 04:26Z AVAX buy target 0.17 (held 0.10) — stay long: 720h return +36.54% vs exit band -5.0% and price within 5.0% of 168h EMA; realised vol 72% -> weight 0.25
- 2026-10-08 04:26Z LINK sell target 0.00 (held 0.10) — exit: price more than 5.0% below 168h EMA
- 2026-10-08 04:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.55% not above entry band +5.0% and price below 168h EMA
- 2026-10-08 04:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -1.57% not above entry band +5.0% and price below 168h EMA
- 2026-10-08 04:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +2.70% not above entry band +5.0% and price below 168h EMA
- 2026-10-08 04:26Z LTC buy target 0.17 (held 0.10) — stay long: 720h return +19.06% vs exit band -5.0% and price within 5.0% of 168h EMA; realised vol 57% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 4,602, gross pnl +67.35, +293 bps per round trip, avg half spread 2.2 bps, open 6386.82
- AVAX: 2 fills (2 buy / 0 sell), traded 1,598, gross pnl +24.33, +305 bps per round trip, avg half spread 0.5 bps, open 149.711
- BTC: 2 fills (2 buy / 0 sell), traded 1,637, gross pnl -15.02, -183 bps per round trip, avg half spread 0.0 bps, open 0.0196004
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 4 fills (2 buy / 2 sell), traded 4,028, gross pnl -51.07, -254 bps per round trip, avg half spread 2.0 bps
- ETH: 2 fills (2 buy / 0 sell), traded 1,668, gross pnl -46.02, -552 bps per round trip, avg half spread 0.0 bps, open 0.631331
- LINK: 4 fills (1 buy / 3 sell), traded 5,043, gross pnl +45.28, +180 bps per round trip, avg half spread 2.4 bps
- LTC: 4 fills (2 buy / 2 sell), traded 4,665, gross pnl -77.39, -332 bps per round trip, avg half spread 2.0 bps, open 24.8496
- SOL: 4 fills (3 buy / 1 sell), traded 3,047, gross pnl -38.04, -250 bps per round trip, avg half spread 0.4 bps, open 14.0611
- XRP: 5 fills (2 buy / 3 sell), traded 7,043, gross pnl -34.06, -97 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-07 22:22Z sell XRP 941 @ 1.41359 fee 0.94 slip 0.47 (half spread 0.0 bps)
- 2026-10-08 04:26Z sell LINK 988 @ 13.1143 fee 0.99 slip 0.49 (half spread 3.0 bps)
- 2026-10-08 04:26Z buy BTC 597 @ 82753.3 fee 0.60 slip 0.30 (half spread 0.0 bps)
- 2026-10-08 04:26Z buy ETH 628 @ 2569.15 fee 0.63 slip 0.31 (half spread 0.0 bps)
- 2026-10-08 04:26Z buy SOL 638 @ 115.353 fee 0.64 slip 0.32 (half spread 0.4 bps)
- 2026-10-08 04:26Z buy ADA 589 @ 0.253977 fee 0.59 slip 0.35 (half spread 4.0 bps)
- 2026-10-08 04:26Z buy AVAX 690 @ 10.8339 fee 0.69 slip 0.35 (half spread 0.5 bps)
- 2026-10-08 04:26Z buy LTC 681 @ 65.0575 fee 0.68 slip 0.34 (half spread 2.3 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1249 candles, 2026-08-17 03:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1249 candles, 2026-08-17 03:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1249 candles, 2026-08-17 03:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1249 candles, 2026-08-17 03:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- AVAX: live 1249 candles, 2026-08-17 03:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- LINK: live 1249 candles, 2026-08-17 03:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- XRP: live 1221 candles, 2026-08-18 07:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.4 bps
- DOGE: live 1221 candles, 2026-08-18 07:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- DOT: live 1221 candles, 2026-08-18 07:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LTC: live 1221 candles, 2026-08-18 07:00Z to 2026-10-08 03:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
