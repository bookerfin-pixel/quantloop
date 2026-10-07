# quantloop summary — generated 2026-10-07 17:27Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 21.5 of 60, 38.5 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +5.76% (max drawdown -15.43%, 208 fills) vs challenger1 +1.58% (max drawdown -2.78%, 23 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.58% (usual 0.54, this window 0.72) vs challenger1 -6.24% (usual 0.37, this window 0.12); the rule compares on skill, daily edge t -0.13 over 22 days
  trades: its 5 finished trades made +3.98% of its starting equity after costs (5 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -1.21 over 22 days)
  two look rule (measured, not applied to this test): on today's numbers it would be kept at day 60 on the value of its trades without passing the rule, the same as under its own rule. From there the two rules are one: 60 more days, and a promotion asks for a daily skill t of 1.0 over all 120 (its daily skill t is -1.21 so far)
  market over the window: BTC +9.90%, equal weight basket of 10 pairs +21.07%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 16.4 of 60, 43.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.95% (max drawdown -15.43%, 170 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.05% (usual 0.54, this window 0.73) vs challenger2 -2.31% (usual 0.29, this window 0.21); the rule compares on skill, daily edge t +0.89 over 16 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.91 over 16 days)
  fills: 4 in 16.4 days; at this pace about 29 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +0.99%, equal weight basket of 10 pairs +2.02%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 1.8 of 60, 58.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.82% (max drawdown -5.22%, 19 fills) vs challenger3 -0.79% (max drawdown -1.52%, 9 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.20% (usual 0.55, this window 0.68) vs challenger3 -0.66% (usual 0.03, this window 0.15); the rule compares on skill
  trades: it has finished no trade of its own: none of its 9 fills closed a position it had bought or had chosen to keep, so the -0.79% it shows is not from an exit it chose. A test that has finished no trade of its own by its look is killed
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -3.00%, equal weight basket of 10 pairs -4.77%, basket max drawdown -6%, basket realised vol 47% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 11.8 of 60, 48.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.49% (max drawdown -15.43%, 142 fills) vs challenger4 -4.30% (max drawdown -5.94%, 12 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -11.42% (usual 0.55, this window 0.70) vs challenger4 -2.51% (usual 0.48, this window 0.99); the rule compares on skill, daily edge t +2.15 over 12 days
  trades: its 2 finished trades made -1.66% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.78 over 12 days)
  fills: 12 in 11.8 days, 10 of them in the hour it began; at this pace about 20 by day 60, under the 30 a promotion there needs, and about 30 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -0.64%, equal weight basket of 10 pairs -3.76%, basket max drawdown -6%, basket realised vol 52% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,576.23 (started 10,000 at 2026-09-16 03:55Z), net +5.76% since start
- 24h -4.54%, 7d -5.96%, 30d +5.76%, max drawdown -15.43%
- fills 208 total, 105 in the last 7d
- costs 480.55 (fees 318.31 + slippage 162.24); gross pnl 1,056.78; cost coverage 2.20
- cash 10,576.23; positions: none
- last run 2026-10-07 17:26Z; halted today: False

last decisions (newest last):

- 2026-10-07 16:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.97% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 16:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-07 16:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-07 16:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.15% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 16:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.69% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 16:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.75% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 16:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.04% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 16:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.91% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.36% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.02% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.09% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-07 17:26Z AVAX none target 0.25 (held 0.00) — capped: 4 fills in AVAX today, the limit is 4 a day, so no new buys until the next UTC day (sells are never capped) | enter long: 72h ret...
- 2026-10-07 17:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.10% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.98% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.30% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.79% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 17:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.36% not above entry band +1.0% and price below 24h EMA

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

- equity 10,146.12 (started 10,000 at 2026-09-16 03:55Z), net +1.46% since start
- 24h -2.42%, 7d -1.40%, 30d +1.46%, max drawdown -2.78%
- fills 23 total, 15 in the last 7d
- costs 65.52 (fees 43.68 + slippage 21.84); gross pnl 211.64; cost coverage 3.23
- cash 0.00; positions: DOGE 19195.1, DOT 1541.15, ETH 0.567281, LINK 76.9551, LTC 17.4878, SOL 14.5071, XRP 1016.78
- last run 2026-10-07 17:26Z; halted today: False

last decisions (newest last):

- 2026-10-07 16:28Z SOL hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -2.03 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-07 16:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.35 not below -2.0
- 2026-10-07 16:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.70 not below -2.0
- 2026-10-07 16:28Z LINK hold target 0.14 (held 0.10) — hold: weight change +0.042 below threshold 0.05 | stay long: z -1.86 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-07 16:28Z XRP hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: z -3.42 vs 240h mean (entry -2.0, exit -0.5); vol 41% -> weight 0.25
- 2026-10-07 16:28Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -3.10 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-07 16:28Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -2.80 vs 240h mean (entry -2.0, exit -0.5); vol 86% -> weight 0.25
- 2026-10-07 16:28Z LTC hold target 0.14 (held 0.11) — hold: weight change +0.030 below threshold 0.05 | stay long: z -2.06 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-10-07 17:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.21 not below -2.0
- 2026-10-07 17:26Z ETH hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: z -3.70 vs 240h mean (entry -2.0, exit -0.5); vol 34% -> weight 0.25
- 2026-10-07 17:26Z SOL hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -1.99 vs 240h mean (entry -2.0, exit -0.5); vol 42% -> weight 0.25
- 2026-10-07 17:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.34 not below -2.0
- 2026-10-07 17:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.87 not below -2.0
- 2026-10-07 17:26Z LINK hold target 0.14 (held 0.10) — hold: weight change +0.041 below threshold 0.05 | stay long: z -1.81 vs 240h mean (entry -2.0, exit -0.5); vol 54% -> weight 0.25
- 2026-10-07 17:26Z XRP hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: z -3.60 vs 240h mean (entry -2.0, exit -0.5); vol 41% -> weight 0.25
- 2026-10-07 17:26Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -3.16 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-07 17:26Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -2.83 vs 240h mean (entry -2.0, exit -0.5); vol 85% -> weight 0.25
- 2026-10-07 17:26Z LTC hold target 0.14 (held 0.11) — hold: weight change +0.029 below threshold 0.05 | stay long: z -2.15 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- DOGE: 4 fills (2 buy / 2 sell), traded 8,707, gross pnl +61.82, +142 bps per round trip, avg half spread 0.3 bps, open 19195.1
- DOT: 2 fills (1 buy / 1 sell), traded 3,428, gross pnl -59.15, -345 bps per round trip, avg half spread 0.4 bps, open 1541.15
- ETH: 5 fills (2 buy / 3 sell), traded 8,747, gross pnl +5.23, +12 bps per round trip, avg half spread 0.1 bps, open 0.567281
- LINK: 1 fill (1 buy / 0 sell), traded 1,027, gross pnl +2.25, +44 bps per round trip, avg half spread 1.5 bps, open 76.9551
- LTC: 1 fill (1 buy / 0 sell), traded 1,158, gross pnl -5.07, -88 bps per round trip, avg half spread 0.8 bps, open 17.4878
- SOL: 3 fills (2 buy / 1 sell), traded 6,771, gross pnl +90.68, +268 bps per round trip, avg half spread 0.5 bps, open 14.5071
- XRP: 3 fills (1 buy / 2 sell), traded 3,689, gross pnl -65.44, -355 bps per round trip, avg half spread 0.3 bps, open 1016.78

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
- 24h -1.41%, 7d -0.70%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-07 17:26Z; halted today: False

last decisions (newest last):

- 2026-10-07 16:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 116.7 not above 120h high 121.8
- 2026-10-07 16:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 16:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 16:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.42 not above 120h high 14.28
- 2026-10-07 16:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.434 not above 120h high 1.523
- 2026-10-07 16:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 16:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 16:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 17:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.335e+04 not above 120h high 8.663e+04
- 2026-10-07 17:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2567 not above 120h high 2731
- 2026-10-07 17:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 116.8 not above 120h high 121.8
- 2026-10-07 17:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 17:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 17:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.44 not above 120h high 14.28
- 2026-10-07 17:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.428 not above 120h high 1.523
- 2026-10-07 17:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 17:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 17:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 9,931.22 (started 10,000 at 2026-10-05 05:28Z), net -0.69% since start
- 24h -0.52%, 7d -0.65%, 30d -0.65%, max drawdown -1.89%
- fills 25 total, 25 in the last 7d
- costs 55.56 (fees 37.00 + slippage 18.56); gross pnl -13.22; cost coverage -0.24
- cash 7,505.37; positions: AVAX 216.372
- last run 2026-10-07 17:26Z; halted today: False

last decisions (newest last):

- 2026-10-07 16:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 116.7 not a fresh close above reaction high 124.4
- 2026-10-07 16:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2562 not a fresh close above reaction high 0.2616
- 2026-10-07 16:28Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 11.23 still above the 48h low 10.85; realised vol 71% -> weight 0.25
- 2026-10-07 16:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.42 not a fresh close above reaction high 15.46
- 2026-10-07 16:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.434 not a fresh close above reaction high 1.638
- 2026-10-07 16:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08815 not a higher low vs prior low 0.08136 (need +10.0%)
- 2026-10-07 16:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.1 not a higher low vs prior low 1.055 (need +10.0%)
- 2026-10-07 16:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 66.12 not a fresh close above reaction high 74.29
- 2026-10-07 17:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.635e+04 (need +10.0%)
- 2026-10-07 17:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2563 not a higher low vs prior low 2444 (need +10.0%)
- 2026-10-07 17:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 116.8 not a fresh close above reaction high 124.4
- 2026-10-07 17:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2561 not a fresh close above reaction high 0.2616
- 2026-10-07 17:26Z AVAX hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: price 11.28 still above the 48h low 10.88; realised vol 71% -> weight 0.25
- 2026-10-07 17:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.44 not a fresh close above reaction high 15.46
- 2026-10-07 17:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.428 not a fresh close above reaction high 1.638
- 2026-10-07 17:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08815 not a higher low vs prior low 0.08136 (need +10.0%)
- 2026-10-07 17:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.1 not a higher low vs prior low 1.055 (need +10.0%)
- 2026-10-07 17:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 65.95 not a fresh close above reaction high 74.29

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 3 fills (2 buy / 1 sell), traded 5,009, gross pnl -67.49, -269 bps per round trip, avg half spread 0.6 bps, open 216.372
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

- equity 9,812.87 (started 10,000 at 2026-09-25 04:23Z), net -1.87% since start
- 24h -4.90%, 7d -2.90%, 30d -1.80%, max drawdown -5.94%
- fills 25 total, 2 in the last 7d
- costs 44.42 (fees 29.54 + slippage 14.88); gross pnl -142.70; cost coverage -3.21
- cash 1,900.42; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-07 17:26Z; halted today: False

last decisions (newest last):

- 2026-10-07 16:28Z SOL hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 720h return +13.05% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 16:28Z ADA hold target 0.12 (held 0.11) — hold: weight change +0.019 below threshold 0.05 | stay long: 720h return +18.00% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 16:28Z AVAX hold target 0.12 (held 0.10) — hold: weight change +0.026 below threshold 0.05 | stay long: 720h return +38.89% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 16:28Z LINK hold target 0.12 (held 0.10) — hold: weight change +0.023 below threshold 0.05 | stay long: 720h return +4.33% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 16:28Z XRP hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +3.67% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 16:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -0.24% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 16:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +2.41% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 16:28Z LTC hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +19.37% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 17:26Z BTC hold target 0.12 (held 0.10) — hold: weight change +0.020 below threshold 0.05 | stay long: 720h return +5.49% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 17:26Z ETH hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 720h return +3.41% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 17:26Z SOL hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 720h return +12.42% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 17:26Z ADA hold target 0.12 (held 0.11) — hold: weight change +0.019 below threshold 0.05 | stay long: 720h return +15.95% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 17:26Z AVAX hold target 0.12 (held 0.10) — hold: weight change +0.027 below threshold 0.05 | stay long: 720h return +39.90% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 17:26Z LINK hold target 0.12 (held 0.10) — hold: weight change +0.022 below threshold 0.05 | stay long: 720h return +3.99% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 17:26Z XRP hold target 0.12 (held 0.10) — hold: weight change +0.029 below threshold 0.05 | stay long: 720h return +2.36% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 17:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -1.70% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 17:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +0.17% not above entry band +5.0% and price below 168h EMA
- 2026-10-07 17:26Z LTC hold target 0.12 (held 0.10) — hold: weight change +0.028 below threshold 0.05 | stay long: 720h return +18.70% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +71.03, +354 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fill (1 buy / 0 sell), traded 907, gross pnl +57.27, +1262 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fill (1 buy / 0 sell), traded 1,040, gross pnl -8.80, -169 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 4 fills (2 buy / 2 sell), traded 4,028, gross pnl -51.07, -254 bps per round trip, avg half spread 2.0 bps
- ETH: 1 fill (1 buy / 0 sell), traded 1,040, gross pnl -49.16, -945 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +64.14, +316 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -64.87, -326 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -29.25, -243 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl -31.38, -103 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1238 candles, 2026-08-17 03:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1238 candles, 2026-08-17 03:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1238 candles, 2026-08-17 03:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1238 candles, 2026-08-17 03:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- AVAX: live 1238 candles, 2026-08-17 03:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- LINK: live 1238 candles, 2026-08-17 03:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- XRP: live 1210 candles, 2026-08-18 07:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.4 bps
- DOGE: live 1210 candles, 2026-08-18 07:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- DOT: live 1210 candles, 2026-08-18 07:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- LTC: live 1210 candles, 2026-08-18 07:00Z to 2026-10-07 16:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
