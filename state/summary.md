# quantloop summary — generated 2026-10-01 16:25Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 15.5 of 60, 44.5 days until the verdict
  so far: champion +10.48% (DD -11.90%, 127 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.18% (usual 0.54, this window 0.70) vs challenger1 -5.72% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.4 over 16 days
  market over the window: BTC +10.83%, equal weight basket of 10 pairs +23.53%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 10.3 of 60, 49.7 days until the verdict
  so far: champion -3.85% (DD -11.90%, 89 fills) vs challenger2 -0.85% (DD -1.17%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.49% (usual 0.54, this window 0.70) vs challenger2 -1.72% (usual 0.29, this window 0.08); the rule compares on skill, daily edge t +0.5 over 11 days
  market over the window: BTC +0.45%, equal weight basket of 10 pairs +3.03%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 6.5 of 60, 53.5 days until the verdict
  so far: champion -6.90% (DD -11.90%, 69 fills) vs challenger3 -2.80% (DD -4.74%, 92 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.30% (usual 0.55, this window 0.67) vs challenger3 -2.84% (usual 0.05, this window 0.53); the rule compares on skill, daily edge t +0.9 over 7 days
  market over the window: BTC -0.10%, equal weight basket of 10 pairs +0.73%, basket max drawdown -5%, basket realised vol 58% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 5.8 of 60, 54.2 days until the verdict
  so far: champion -9.63% (DD -11.90%, 61 fills) vs challenger4 -1.91% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.26% (usual 0.55, this window 0.62) vs challenger4 -0.71% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.6 over 6 days
  market over the window: BTC +0.07%, equal weight basket of 10 pairs -2.51%, basket max drawdown -5%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,047.99 (started 10,000 at 2026-09-16 03:55Z), net +10.48% since start
- 24h -1.77%, 7d -8.13%, 30d +10.48%, max drawdown -11.90%
- fills 127 total, 72 in the last 7d
- costs 305.80 (fees 201.89 + slippage 103.91); gross pnl 1,353.79; cost coverage 4.43
- cash -0.00; positions: AVAX 252.39, BTC 0.0330404, DOGE 29185.8, ETH 1.02721
- last run 2026-10-01 16:24Z; halted today: False

last decisions (newest last):

- 2026-10-01 15:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.56% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 15:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-01 15:26Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +7.09% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 15:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.87% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.20% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 15:26Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.94% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 15:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.88% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 15:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.55% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 16:24Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +0.94% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-01 16:24Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.14% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.11% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.68% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 16:24Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +5.39% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.01% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.55% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 16:24Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.95% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.37% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.46% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 13 fills (6 buy / 7 sell), traded 21,499, gross pnl +59.73, +56 bps per round trip, avg half spread 2.3 bps
- AVAX: 17 fills (8 buy / 9 sell), traded 30,112, gross pnl +554.95, +369 bps per round trip, avg half spread 1.3 bps, open 252.39
- BTC: 6 fills (4 buy / 2 sell), traded 8,222, gross pnl +75.40, +183 bps per round trip, avg half spread 0.4 bps, open 0.0330404
- DOGE: 13 fills (8 buy / 5 sell), traded 19,479, gross pnl -53.40, -55 bps per round trip, avg half spread 1.4 bps, open 29185.8
- DOT: 15 fills (8 buy / 7 sell), traded 17,668, gross pnl +189.99, +215 bps per round trip, avg half spread 3.0 bps
- ETH: 10 fills (5 buy / 5 sell), traded 16,866, gross pnl +12.96, +15 bps per round trip, avg half spread 0.1 bps, open 1.02721
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 11 fills (5 buy / 6 sell), traded 17,411, gross pnl +151.93, +175 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-01 13:29Z sell ADA 1,364 @ 0.24508 fee 1.36 slip 0.68 (half spread 1.1 bps)
- 2026-10-01 13:29Z sell LINK 1,389 @ 14.2626 fee 1.39 slip 0.69 (half spread 0.5 bps)
- 2026-10-01 13:29Z sell XRP 1,375 @ 1.47805 fee 1.37 slip 0.69 (half spread 0.3 bps)
- 2026-10-01 13:29Z sell DOT 1,346 @ 1.18636 fee 1.35 slip 0.67 (half spread 2.1 bps)
- 2026-10-01 13:29Z buy BTC 1,363 @ 83519.1 fee 1.36 slip 0.68 (half spread 0.0 bps)
- 2026-10-01 13:29Z buy ETH 1,366 @ 2686.4 fee 1.37 slip 0.68 (half spread 0.0 bps)
- 2026-10-01 13:29Z buy AVAX 1,372 @ 10.9335 fee 1.37 slip 0.69 (half spread 1.8 bps)
- 2026-10-01 13:29Z buy DOGE 1,361 @ 0.0940806 fee 1.36 slip 0.68 (half spread 0.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-10-01 16:24Z; halted today: False

last decisions (newest last):

- 2026-10-01 15:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.59 not below -2.0
- 2026-10-01 15:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.71 not below -2.0
- 2026-10-01 15:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0
- 2026-10-01 15:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.61 not below -2.0
- 2026-10-01 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.22 not below -2.0
- 2026-10-01 15:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.82 not below -2.0
- 2026-10-01 15:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.51 not below -2.0
- 2026-10-01 15:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0
- 2026-10-01 16:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-10-01 16:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.51 not below -2.0
- 2026-10-01 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.61 not below -2.0
- 2026-10-01 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-10-01 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.26 not below -2.0
- 2026-10-01 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.57 not below -2.0
- 2026-10-01 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.08 not below -2.0
- 2026-10-01 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.75 not below -2.0
- 2026-10-01 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.53 not below -2.0
- 2026-10-01 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.21 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- ETH: 2 fills (1 buy / 1 sell), traded 5,048, gross pnl +50.93, +202 bps per round trip, avg half spread 0.4 bps
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)
- 2026-09-17 13:23Z sell ETH 2,548 @ 2449.98 fee 2.55 slip 1.27 (half spread 0.4 bps)
- 2026-09-18 01:20Z sell ADA 2,628 @ 0.205888 fee 2.63 slip 1.31 (half spread 2.2 bps)
- 2026-09-18 03:21Z sell BTC 2,538 @ 77289.3 fee 2.54 slip 1.27 (half spread 0.0 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,872.57 (started 10,000 at 2026-09-16 23:20Z), net +8.73% since start
- 24h -0.04%, 7d -0.85%, 30d +8.73%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 959.75; cost coverage 11.01
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-01 16:24Z; halted today: False

last decisions (newest last):

- 2026-10-01 15:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 15:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 8.413e+04 still above 72h low 8.294e+04; realised vol 30% -> weight 0.25
- 2026-10-01 16:24Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 2682 still above 72h low 2657; realised vol 37% -> weight 0.25
- 2026-10-01 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -44.09, -109 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -62.48, -154 bps per round trip, avg half spread 0.0 bps, open 1.00083
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)
- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)
- 2026-09-30 13:27Z buy BTC 2,737 @ 85327.3 fee 2.74 slip 1.37 (half spread 0.0 bps)

## challenger3: swing_reversal (H3)

params: {"exit_hours": 48, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,189.45 (started 10,000 at 2026-09-16 23:20Z), net +11.89% since start
- 24h -1.78%, 7d -2.80%, 30d +11.89%, max drawdown -9.51%
- fills 141 total, 92 in the last 7d
- costs 322.59 (fees 211.96 + slippage 110.63); gross pnl 1,512.04; cost coverage 4.69
- cash 564.15; positions: ADA 5740.21, AVAX 129.447, DOGE 15015.8, DOT 1141.01, ETH 0.375585, LINK 86.9199, LTC 20.8551, SOL 11.8866
- last run 2026-10-01 16:24Z; halted today: False

last decisions (newest last):

- 2026-10-01 15:26Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: price 117.4 still above the 48h low 117.2; realised vol 58% -> weight 0.25
- 2026-10-01 15:26Z ADA hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.2448 still above the 48h low 0.2413; realised vol 86% -> weight 0.25
- 2026-10-01 15:26Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: price 10.96 still above the 48h low 10.85; realised vol 98% -> weight 0.25
- 2026-10-01 15:26Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: price 14.31 still above the 48h low 14.21; realised vol 104% -> weight 0.25
- 2026-10-01 15:26Z XRP sell target 0.00 (held 0.13) — exit: closed 1.482 below the 48h low 1.482
- 2026-10-01 15:26Z DOGE hold target 0.12 (held 0.13) — hold: weight change -0.002 below threshold 0.05 | stay long: price 0.0941 still above the 48h low 0.09297; realised vol 63% -> weight 0.25
- 2026-10-01 15:26Z DOT hold target 0.12 (held 0.12) — hold: weight change +0.005 below threshold 0.05 | stay long: price 1.173 still above the 48h low 1.163; realised vol 97% -> weight 0.25
- 2026-10-01 15:26Z LTC buy target 0.12 (held 0.05) — stay long: price 67.1 still above the 48h low 66.15; realised vol 67% -> weight 0.25
- 2026-10-01 16:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-01 16:24Z ETH hold target 0.12 (held 0.09) — hold: weight change +0.035 below threshold 0.05 | stay long: price 2682 still above the 48h low 2661; realised vol 37% -> weight 0.25
- 2026-10-01 16:24Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: price 117.3 still above the 48h low 117.2; realised vol 57% -> weight 0.25
- 2026-10-01 16:24Z ADA hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.2463 still above the 48h low 0.2413; realised vol 85% -> weight 0.25
- 2026-10-01 16:24Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: price 10.89 still above the 48h low 10.85; realised vol 98% -> weight 0.25
- 2026-10-01 16:24Z LINK hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: price 14.28 still above the 48h low 14.21; realised vol 103% -> weight 0.25
- 2026-10-01 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.487 not above reaction high 1.638
- 2026-10-01 16:24Z DOGE hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.09425 still above the 48h low 0.09297; realised vol 62% -> weight 0.25
- 2026-10-01 16:24Z DOT hold target 0.12 (held 0.12) — hold: weight change +0.006 below threshold 0.05 | stay long: price 1.172 still above the 48h low 1.163; realised vol 96% -> weight 0.25
- 2026-10-01 16:24Z LTC hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: price 66.98 still above the 48h low 66.15; realised vol 66% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (10 buy / 11 sell), traded 41,237, gross pnl +88.81, +43 bps per round trip, avg half spread 2.2 bps, open 5740.21
- AVAX: 17 fills (7 buy / 10 sell), traded 25,757, gross pnl +788.63, +612 bps per round trip, avg half spread 1.5 bps, open 129.447
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 7 fills (5 buy / 2 sell), traded 7,263, gross pnl -37.60, -104 bps per round trip, avg half spread 2.0 bps, open 15015.8
- DOT: 19 fills (9 buy / 10 sell), traded 31,210, gross pnl +49.75, +32 bps per round trip, avg half spread 2.9 bps, open 1141.01
- ETH: 5 fills (3 buy / 2 sell), traded 6,460, gross pnl +85.35, +264 bps per round trip, avg half spread 0.1 bps, open 0.375585
- LINK: 17 fills (8 buy / 9 sell), traded 27,399, gross pnl +249.31, +182 bps per round trip, avg half spread 2.9 bps, open 86.9199
- LTC: 32 fills (17 buy / 15 sell), traded 41,283, gross pnl +88.12, +43 bps per round trip, avg half spread 1.9 bps, open 20.8551
- SOL: 13 fills (6 buy / 7 sell), traded 18,936, gross pnl +51.94, +55 bps per round trip, avg half spread 0.5 bps, open 11.8866
- XRP: 6 fills (3 buy / 3 sell), traded 6,959, gross pnl +88.07, +253 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-09-30 17:24Z buy DOGE 1,422 @ 0.094716 fee 1.42 slip 0.71 (half spread 0.3 bps)
- 2026-09-30 17:24Z buy LTC 703 @ 66.9685 fee 0.70 slip 0.35 (half spread 0.7 bps)
- 2026-09-30 19:25Z sell LTC 1,008 @ 65.947 fee 1.01 slip 0.50 (half spread 1.5 bps)
- 2026-09-30 20:24Z buy ETH 1,006 @ 2679.68 fee 1.01 slip 0.50 (half spread 0.0 bps)
- 2026-10-01 14:27Z sell LINK 564 @ 14.3742 fee 0.56 slip 0.28 (half spread 1.3 bps)
- 2026-10-01 14:27Z buy LTC 563 @ 67.2836 fee 0.56 slip 0.28 (half spread 1.5 bps)
- 2026-10-01 15:26Z sell XRP 1,406 @ 1.48778 fee 1.41 slip 0.70 (half spread 0.5 bps)
- 2026-10-01 15:26Z buy LTC 840 @ 67.2186 fee 0.84 slip 0.42 (half spread 0.7 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,058.16 (started 10,000 at 2026-09-25 04:23Z), net +0.58% since start
- 24h -1.32%, 7d +0.66%, 30d +0.66%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 99.73; cost coverage 2.40
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-01 16:24Z; halted today: False

last decisions (newest last):

- 2026-10-01 15:26Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +15.13% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 15:26Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +22.63% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 15:26Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +49.45% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 15:26Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +24.89% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 15:26Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.56% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-01 15:26Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +13.72% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 15:26Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +35.00% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 15:26Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +35.20% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 16:24Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +8.01% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-01 16:24Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +9.53% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-01 16:24Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +15.02% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 16:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +23.42% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 16:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +49.12% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 16:24Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +24.98% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 16:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.88% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-01 16:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +13.92% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 16:24Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +34.94% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 16:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +34.28% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +37.79, +188 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +31.64, +698 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +4.53, +87 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -44.77, -869 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl -10.73, -70 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -0.79, -15 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +134.75, +665 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -47.60, -239 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -19.86, -165 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +14.77, +48 bps per round trip, avg half spread 0.7 bps, open 665.342

last fills:

- 2026-09-25 22:21Z sell LINK 979 @ 13.7945 fee 0.98 slip 0.49 (half spread 2.4 bps)
- 2026-09-25 22:21Z sell DOT 1,014 @ 1.19895 fee 1.01 slip 0.51 (half spread 0.4 bps)
- 2026-09-25 22:21Z sell LTC 719 @ 72.2139 fee 0.72 slip 0.36 (half spread 2.8 bps)
- 2026-09-25 22:21Z buy BTC 1,040 @ 83966.2 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-09-25 22:21Z buy ETH 1,040 @ 2688.17 fee 1.04 slip 0.52 (half spread 0.0 bps)
- 2026-09-25 22:21Z buy AVAX 907 @ 10.5508 fee 0.91 slip 0.45 (half spread 0.5 bps)
- 2026-09-25 22:21Z buy XRP 1,040 @ 1.5631 fee 1.04 slip 0.52 (half spread 1.0 bps)
- 2026-09-25 22:21Z buy DOGE 1,031 @ 0.0985782 fee 1.03 slip 0.52 (half spread 0.1 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1093 candles, 2026-08-17 03:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1093 candles, 2026-08-17 03:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1093 candles, 2026-08-17 03:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1093 candles, 2026-08-17 03:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1093 candles, 2026-08-17 03:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1093 candles, 2026-08-17 03:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1065 candles, 2026-08-18 07:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1065 candles, 2026-08-18 07:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 1065 candles, 2026-08-18 07:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1065 candles, 2026-08-18 07:00Z to 2026-10-01 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
