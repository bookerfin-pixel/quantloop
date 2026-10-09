# quantloop summary — generated 2026-10-09 01:26Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 22.8 of 60, 37.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +5.76% (max drawdown -15.43%, 208 fills) vs challenger1 -3.27% (max drawdown -7.73%, 38 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.30% (usual 0.54, this window 0.68) vs challenger1 -8.83% (usual 0.37, this window 0.16); the rule compares on skill, daily edge t -0.56 over 23 days
  trades: its 12 finished trades made -3.56% of its starting equity after costs (5 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.60 over 23 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +7.78%, equal weight basket of 10 pairs +14.98%, basket max drawdown -14%, basket realised vol 59% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 17.7 of 60, 42.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.95% (max drawdown -15.43%, 170 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.37% (usual 0.54, this window 0.67) vs challenger2 -0.89% (usual 0.29, this window 0.20); the rule compares on skill, daily edge t +0.71 over 18 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 9% that this is a real edge (every idea starts at 10%; the daily skill t is -0.33 over 18 days)
  fills: 4 in 17.7 days; at this pace about 27 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -0.96%, equal weight basket of 10 pairs -2.93%, basket max drawdown -14%, basket realised vol 59% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 3.1 of 60, 56.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.82% (max drawdown -5.22%, 19 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +0.33% (usual 0.55, this window 0.39) vs challenger3 -1.00% (usual 0.03, this window 0.10); the rule compares on skill, daily edge t -0.57 over 3 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -4.87%, equal weight basket of 10 pairs -9.38%, basket max drawdown -14%, basket realised vol 70% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 13.1 of 60, 46.9 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.49% (max drawdown -15.43%, 142 fills) vs challenger4 -9.83% (max drawdown -11.38%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.85% (usual 0.55, this window 0.63) vs challenger4 -5.81% (usual 0.48, this window 0.95); the rule compares on skill, daily edge t +0.43 over 13 days
  trades: its 10 finished trades made -9.65% of its starting equity after costs (0 won, 10 lost, 3 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -1.31 over 13 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -2.56%, equal weight basket of 10 pairs -8.46%, basket max drawdown -14%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,576.23 (started 10,000 at 2026-09-16 03:55Z), net +5.76% since start
- 24h +0.00%, 7d -4.22%, 30d +5.76%, max drawdown -15.43%
- fills 208 total, 73 in the last 7d
- costs 480.55 (fees 318.31 + slippage 162.24); gross pnl 1,056.78; cost coverage 2.20
- cash 10,576.23; positions: none
- last run 2026-10-09 01:26Z; halted today: False

last decisions (newest last):

- 2026-10-09 00:37Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.32% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 00:37Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -14.20% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 00:37Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.56% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 00:37Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.41% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 00:37Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.51% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 00:37Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -12.00% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 00:37Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.50% not above entry band +1.0%
- 2026-10-09 00:37Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.96% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.84% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.90% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.70% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -14.21% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.98% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.40% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.06% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -11.60% not above entry band +1.0% and price below 24h EMA
- 2026-10-09 01:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.57% not above entry band +1.0%
- 2026-10-09 01:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.42% not above entry band +1.0% and price below 24h EMA

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

- equity 9,662.11 (started 10,000 at 2026-09-16 03:55Z), net -3.38% since start
- 24h -5.36%, 7d -6.10%, 30d -3.38%, max drawdown -7.73%
- fills 38 total, 30 in the last 7d
- costs 94.59 (fees 62.97 + slippage 31.62); gross pnl -243.30; cost coverage -2.57
- cash -0.00; positions: AVAX 119.636, BTC 0.0147423, DOGE 14318.8, ETH 0.486166, LINK 94.6674, LTC 18.9301, SOL 11.0391, XRP 869.779
- last run 2026-10-09 01:26Z; halted today: False

last decisions (newest last):

- 2026-10-09 00:37Z SOL buy target 0.12 (held 0.00) — enter long: z -3.37 vs 240h mean (entry -2.0, exit -0.5); vol 50% -> weight 0.25
- 2026-10-09 00:37Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.91 not below -2.0
- 2026-10-09 00:37Z AVAX buy target 0.12 (held 0.00) — enter long: z -3.18 vs 240h mean (entry -2.0, exit -0.5); vol 86% -> weight 0.25
- 2026-10-09 00:37Z LINK buy target 0.12 (held 0.00) — enter long: z -2.39 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-10-09 00:37Z XRP buy target 0.12 (held 0.00) — enter long: z -2.67 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-10-09 00:37Z DOGE buy target 0.12 (held 0.00) — enter long: z -2.95 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-09 00:37Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.95 not below -2.0
- 2026-10-09 00:37Z LTC buy target 0.12 (held 0.00) — enter long: z -2.48 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-10-09 01:26Z BTC hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: z -2.16 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-10-09 01:26Z ETH hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: z -2.88 vs 240h mean (entry -2.0, exit -0.5); vol 44% -> weight 0.25
- 2026-10-09 01:26Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: z -3.36 vs 240h mean (entry -2.0, exit -0.5); vol 50% -> weight 0.25
- 2026-10-09 01:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.87 not below -2.0
- 2026-10-09 01:26Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: z -3.11 vs 240h mean (entry -2.0, exit -0.5); vol 86% -> weight 0.25
- 2026-10-09 01:26Z LINK hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.35 vs 240h mean (entry -2.0, exit -0.5); vol 65% -> weight 0.25
- 2026-10-09 01:26Z XRP hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: z -2.44 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-10-09 01:26Z DOGE hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.81 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-09 01:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.28 not below -2.0
- 2026-10-09 01:26Z LTC hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.38 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- AVAX: 1 fill (1 buy / 0 sell), traded 1,206, gross pnl +10.71, +178 bps per round trip, avg half spread 1.0 bps, open 119.636
- BTC: 3 fills (2 buy / 1 sell), traded 6,233, gross pnl +51.55, +165 bps per round trip, avg half spread 0.0 bps, open 0.0147423
- DOGE: 6 fills (3 buy / 3 sell), traded 11,524, gross pnl -13.40, -23 bps per round trip, avg half spread 0.2 bps, open 14318.8
- DOT: 3 fills (1 buy / 2 sell), traded 5,040, gross pnl -135.21, -537 bps per round trip, avg half spread 1.6 bps
- ETH: 7 fills (3 buy / 4 sell), traded 11,354, gross pnl -46.60, -82 bps per round trip, avg half spread 0.3 bps, open 0.486166
- LINK: 3 fills (2 buy / 1 sell), traded 3,198, gross pnl -57.25, -358 bps per round trip, avg half spread 1.4 bps, open 94.6674
- LTC: 3 fills (2 buy / 1 sell), traded 3,448, gross pnl -55.41, -321 bps per round trip, avg half spread 1.3 bps, open 18.9301
- SOL: 5 fills (3 buy / 2 sell), traded 9,566, gross pnl -5.26, -11 bps per round trip, avg half spread 0.5 bps, open 11.0391
- XRP: 5 fills (2 buy / 3 sell), traded 6,277, gross pnl -122.84, -391 bps per round trip, avg half spread 0.5 bps, open 869.779

last fills:

- 2026-10-09 00:37Z buy BTC 1,206 @ 81776.6 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy ETH 1,206 @ 2479.75 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy SOL 1,206 @ 109.21 fee 1.21 slip 0.60 (half spread 0.5 bps)
- 2026-10-09 00:37Z buy AVAX 1,206 @ 10.077 fee 1.21 slip 0.60 (half spread 1.0 bps)
- 2026-10-09 00:37Z buy LINK 1,206 @ 12.7348 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy XRP 1,206 @ 1.38607 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy DOGE 1,206 @ 0.0841954 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-09 00:37Z buy LTC 1,196 @ 63.1766 fee 1.20 slip 0.60 (half spread 0.8 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h +0.00%, 7d -1.28%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 2 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-09 01:26Z; halted today: False

last decisions (newest last):

- 2026-10-09 00:37Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 109.5 not above 120h high 121.8
- 2026-10-09 00:37Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 00:37Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 00:37Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.69 not above 120h high 14.28
- 2026-10-09 00:37Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.379 not above 120h high 1.523
- 2026-10-09 00:37Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 00:37Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 00:37Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 01:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.174e+04 not above 120h high 8.663e+04
- 2026-10-09 01:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2476 not above 120h high 2731
- 2026-10-09 01:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 109.3 not above 120h high 121.8
- 2026-10-09 01:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 01:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 01:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 12.7 not above 120h high 14.28
- 2026-10-09 01:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.387 not above 120h high 1.523
- 2026-10-09 01:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 01:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-09 01:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- 24h +0.00%, 7d -1.13%, 30d -1.13%, max drawdown -1.89%
- fills 26 total, 26 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-10-09 01:26Z; halted today: False

last decisions (newest last):

- 2026-10-09 00:37Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 107.7 (need +10.0%)
- 2026-10-09 00:37Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2191 (need +10.0%)
- 2026-10-09 00:37Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.07 not a fresh close above reaction high 11.84
- 2026-10-09 00:37Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 11.95 (need +10.0%)
- 2026-10-09 00:37Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.37 (need +10.0%)
- 2026-10-09 00:37Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.08471 (need +10.0%)
- 2026-10-09 00:37Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.075 (need +10.0%)
- 2026-10-09 00:37Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 56.67 (need +10.0%)
- 2026-10-09 01:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.067e+04 not a higher low vs prior low 8.023e+04 (need +10.0%)
- 2026-10-09 01:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2415 not a higher low vs prior low 2571 (need +10.0%)
- 2026-10-09 01:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 106.3 not a higher low vs prior low 107.7 (need +10.0%)
- 2026-10-09 01:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.2251 not a higher low vs prior low 0.2191 (need +10.0%)
- 2026-10-09 01:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.07 not a fresh close above reaction high 11.84
- 2026-10-09 01:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 12.18 not a higher low vs prior low 11.95 (need +10.0%)
- 2026-10-09 01:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.326 not a higher low vs prior low 1.37 (need +10.0%)
- 2026-10-09 01:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08144 not a higher low vs prior low 0.08471 (need +10.0%)
- 2026-10-09 01:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.016 not a higher low vs prior low 1.075 (need +10.0%)
- 2026-10-09 01:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 61.36 not a higher low vs prior low 56.67 (need +10.0%)

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

- equity 9,245.09 (started 10,000 at 2026-09-25 04:23Z), net -7.55% since start
- 24h -5.68%, 7d -8.87%, 30d -7.48%, max drawdown -11.38%
- fills 43 total, 20 in the last 7d
- costs 76.53 (fees 50.91 + slippage 25.63); gross pnl -678.38; cost coverage -8.86
- cash 9,245.09; positions: none
- last run 2026-10-09 01:26Z; halted today: False

last decisions (newest last):

- 2026-10-09 00:37Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 00:37Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 00:37Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 00:37Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.39% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 00:37Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -2.68% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 00:37Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -6.72% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 00:37Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -12.56% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 00:37Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 01:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +3.78% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 01:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -0.77% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 01:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 01:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 01:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA
- 2026-10-09 01:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return +1.35% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 01:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -2.36% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 01:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -7.10% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 01:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 720h return -7.97% not above entry band +5.0% and price below 168h EMA
- 2026-10-09 01:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 168h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 6 fills (3 buy / 3 sell), traded 7,648, gross pnl -125.14, -327 bps per round trip, avg half spread 1.9 bps
- AVAX: 4 fills (3 buy / 1 sell), traded 4,667, gross pnl -123.70, -530 bps per round trip, avg half spread 0.8 bps
- BTC: 4 fills (3 buy / 1 sell), traded 4,772, gross pnl -53.58, -225 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 1,960, gross pnl -100.62, -1027 bps per round trip, avg half spread 0.1 bps
- DOT: 4 fills (2 buy / 2 sell), traded 4,028, gross pnl -51.07, -254 bps per round trip, avg half spread 2.0 bps
- ETH: 4 fills (3 buy / 1 sell), traded 4,849, gross pnl -68.19, -281 bps per round trip, avg half spread 0.0 bps
- LINK: 4 fills (1 buy / 3 sell), traded 5,043, gross pnl +45.28, +180 bps per round trip, avg half spread 2.4 bps
- LTC: 5 fills (2 buy / 3 sell), traded 6,271, gross pnl -87.08, -278 bps per round trip, avg half spread 1.7 bps
- SOL: 5 fills (3 buy / 2 sell), traded 4,625, gross pnl -80.22, -347 bps per round trip, avg half spread 0.4 bps
- XRP: 5 fills (2 buy / 3 sell), traded 7,043, gross pnl -34.06, -97 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-10-08 13:29Z buy BTC 777 @ 82387.5 fee 0.78 slip 0.39 (half spread 0.0 bps)
- 2026-10-08 13:29Z buy ETH 792 @ 2534.61 fee 0.79 slip 0.40 (half spread 0.0 bps)
- 2026-10-08 13:29Z buy ADA 809 @ 0.247799 fee 0.81 slip 0.40 (half spread 1.6 bps)
- 2026-10-08 13:29Z buy AVAX 799 @ 10.6048 fee 0.80 slip 0.40 (half spread 1.4 bps)
- 2026-10-08 14:29Z sell ETH 2,389 @ 2531.68 fee 2.39 slip 1.20 (half spread 0.0 bps)
- 2026-10-08 16:29Z sell BTC 2,358 @ 81224.3 fee 2.36 slip 1.18 (half spread 0.0 bps)
- 2026-10-08 16:29Z sell ADA 2,236 @ 0.231688 fee 2.24 slip 1.12 (half spread 1.1 bps)
- 2026-10-08 16:29Z sell AVAX 2,270 @ 10.089 fee 2.27 slip 1.14 (half spread 1.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1270 candles, 2026-08-17 03:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1270 candles, 2026-08-17 03:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1270 candles, 2026-08-17 03:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1270 candles, 2026-08-17 03:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- AVAX: live 1270 candles, 2026-08-17 03:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 0.9 bps
- LINK: live 1270 candles, 2026-08-17 03:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- XRP: live 1242 candles, 2026-08-18 07:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.4 bps
- DOGE: live 1242 candles, 2026-08-18 07:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.4 bps
- DOT: live 1242 candles, 2026-08-18 07:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LTC: live 1242 candles, 2026-08-18 07:00Z to 2026-10-09 00:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.3 bps
