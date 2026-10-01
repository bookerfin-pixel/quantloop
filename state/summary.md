# quantloop summary — generated 2026-10-01 21:23Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 15.7 of 60, 44.3 days until the verdict
  so far: champion +10.38% (DD -11.90%, 135 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.82% (usual 0.54, this window 0.70) vs challenger1 -6.09% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.3 over 16 days
  market over the window: BTC +11.46%, equal weight basket of 10 pairs +24.54%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 10.5 of 60, 49.5 days until the verdict
  so far: champion -3.93% (DD -11.90%, 97 fills) vs challenger2 -0.67% (DD -1.17%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.02% (usual 0.54, this window 0.70) vs challenger2 -1.77% (usual 0.29, this window 0.09); the rule compares on skill, daily edge t +0.5 over 11 days
  market over the window: BTC +1.02%, equal weight basket of 10 pairs +3.87%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 6.8 of 60, 53.2 days until the verdict
  so far: champion -6.98% (DD -11.90%, 77 fills) vs challenger3 -2.59% (DD -4.74%, 104 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.82% (usual 0.55, this window 0.67) vs challenger3 -2.67% (usual 0.05, this window 0.54); the rule compares on skill, daily edge t +1.0 over 7 days
  market over the window: BTC +0.47%, equal weight basket of 10 pairs +1.53%, basket max drawdown -5%, basket realised vol 58% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 6.0 of 60, 54.0 days until the verdict
  so far: champion -9.71% (DD -11.90%, 69 fills) vs challenger4 -1.38% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.76% (usual 0.55, this window 0.63) vs challenger4 -0.56% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.7 over 6 days
  market over the window: BTC +0.64%, equal weight basket of 10 pairs -1.73%, basket max drawdown -5%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,038.47 (started 10,000 at 2026-09-16 03:55Z), net +10.38% since start
- 24h -1.85%, 7d -6.69%, 30d +10.38%, max drawdown -11.90%
- fills 135 total, 79 in the last 7d
- costs 325.13 (fees 214.78 + slippage 110.35); gross pnl 1,363.60; cost coverage 4.19
- cash -0.00; positions: ADA 7446.71, AVAX 167.946, BTC 0.0217956, DOGE 19500, ETH 0.684107, XRP 1224.29
- last run 2026-10-01 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-01 20:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.07% not above entry band +1.0%
- 2026-10-01 20:25Z ADA buy target 0.17 (held 0.00) — enter long: 72h return +1.98% vs entry band +1.0% and price above 24h EMA; realised vol 87% -> weight 0.25
- 2026-10-01 20:25Z AVAX sell target 0.17 (held 0.25) — stay long: 72h return +6.49% vs exit band -1.0% and price above 24h EMA; realised vol 98% -> weight 0.25
- 2026-10-01 20:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.39% not above entry band +1.0%
- 2026-10-01 20:25Z XRP buy target 0.17 (held 0.00) — enter long: 72h return +1.18% vs entry band +1.0% and price above 24h EMA; realised vol 63% -> weight 0.25
- 2026-10-01 20:25Z DOGE sell target 0.17 (held 0.25) — stay long: 72h return +1.59% vs exit band -1.0% and price above 24h EMA; realised vol 62% -> weight 0.25
- 2026-10-01 20:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-01 20:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.13% not above entry band +1.0%
- 2026-10-01 21:23Z BTC hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +1.32% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-01 21:23Z ETH hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.60% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-01 21:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.56% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 21:23Z ADA hold target 0.17 (held 0.17) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.60% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 21:23Z AVAX hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +5.25% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-01 21:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.20% not above entry band +1.0%
- 2026-10-01 21:23Z XRP hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.25% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-01 21:23Z DOGE hold target 0.17 (held 0.17) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.64% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.47% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 21:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.84% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 14 fills (7 buy / 7 sell), traded 23,348, gross pnl +48.19, +41 bps per round trip, avg half spread 2.2 bps, open 7446.71
- AVAX: 20 fills (9 buy / 11 sell), traded 36,514, gross pnl +554.38, +304 bps per round trip, avg half spread 1.3 bps, open 167.946
- BTC: 7 fills (4 buy / 3 sell), traded 9,176, gross pnl +87.99, +192 bps per round trip, avg half spread 0.3 bps, open 0.0217956
- DOGE: 14 fills (8 buy / 6 sell), traded 20,397, gross pnl -46.20, -45 bps per round trip, avg half spread 1.3 bps, open 19500
- DOT: 15 fills (8 buy / 7 sell), traded 17,668, gross pnl +189.99, +215 bps per round trip, avg half spread 3.0 bps
- ETH: 11 fills (5 buy / 6 sell), traded 17,792, gross pnl +25.70, +29 bps per round trip, avg half spread 0.1 bps, open 0.684107
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 12 fills (6 buy / 6 sell), traded 19,252, gross pnl +141.31, +147 bps per round trip, avg half spread 0.6 bps, open 1224.29

last fills:

- 2026-10-01 17:24Z sell AVAX 2,753 @ 10.9095 fee 2.75 slip 1.38 (half spread 1.8 bps)
- 2026-10-01 19:24Z buy AVAX 2,748 @ 11.001 fee 2.75 slip 1.37 (half spread 1.4 bps)
- 2026-10-01 20:25Z sell BTC 953 @ 84759.3 fee 0.95 slip 0.48 (half spread 0.0 bps)
- 2026-10-01 20:25Z sell ETH 927 @ 2700.44 fee 0.93 slip 0.46 (half spread 0.0 bps)
- 2026-10-01 20:25Z sell AVAX 900 @ 11 fee 0.90 slip 0.45 (half spread 1.4 bps)
- 2026-10-01 20:25Z sell DOGE 918 @ 0.0947384 fee 0.92 slip 0.46 (half spread 0.6 bps)
- 2026-10-01 20:25Z buy ADA 1,849 @ 0.248268 fee 1.85 slip 0.92 (half spread 1.1 bps)
- 2026-10-01 20:25Z buy XRP 1,841 @ 1.50405 fee 1.84 slip 0.92 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-10-01 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-01 20:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.22 not below -2.0
- 2026-10-01 20:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.15 not below -2.0
- 2026-10-01 20:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.54 not below -2.0
- 2026-10-01 20:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.74 not below -2.0
- 2026-10-01 20:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.67 not below -2.0
- 2026-10-01 20:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.53 not below -2.0
- 2026-10-01 20:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.27 not below -2.0
- 2026-10-01 20:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.07 not below -2.0
- 2026-10-01 21:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.29 not below -2.0
- 2026-10-01 21:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.06 not below -2.0
- 2026-10-01 21:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.27 not below -2.0
- 2026-10-01 21:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.30 not below -2.0
- 2026-10-01 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.56 not below -2.0
- 2026-10-01 21:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.66 not below -2.0
- 2026-10-01 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.74 not below -2.0
- 2026-10-01 21:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.62 not below -2.0
- 2026-10-01 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.29 not below -2.0
- 2026-10-01 21:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.13 not below -2.0

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

- equity 10,892.74 (started 10,000 at 2026-09-16 23:20Z), net +8.93% since start
- 24h +0.39%, 7d -0.67%, 30d +8.93%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 979.92; cost coverage 11.24
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-01 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-01 20:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 20:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 8.46e+04 still above 72h low 8.294e+04; realised vol 30% -> weight 0.25
- 2026-10-01 21:23Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 2698 still above 72h low 2657; realised vol 36% -> weight 0.25
- 2026-10-01 21:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 21:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -34.03, -84 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -52.37, -129 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,213.99 (started 10,000 at 2026-09-16 23:20Z), net +12.14% since start
- 24h -0.27%, 7d -2.59%, 30d +12.14%, max drawdown -9.51%
- fills 153 total, 104 in the last 7d
- costs 344.71 (fees 226.71 + slippage 118.01); gross pnl 1,558.70; cost coverage 4.52
- cash -0.00; positions: ADA 11257.7, DOGE 23682.3, ETH 0.832737, LINK 117.602, LTC 33.1394
- last run 2026-10-01 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-01 20:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 118.2 not above reaction high 119.5
- 2026-10-01 20:25Z ADA hold target 0.20 (held 0.25) — hold: weight change -0.048 below threshold 0.05 | stay long: price 0.2481 still above the 48h low 0.2425; realised vol 87% -> weight 0.25
- 2026-10-01 20:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11 not above reaction high 11.55
- 2026-10-01 20:25Z LINK hold target 0.20 (held 0.15) — hold: weight change +0.049 below threshold 0.05 | stay long: price 14.44 still above the 48h low 14.18; realised vol 98% -> weight 0.25
- 2026-10-01 20:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.5 not above reaction high 1.638
- 2026-10-01 20:25Z DOGE hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: price 0.09477 still above the 48h low 0.09297; realised vol 62% -> weight 0.25
- 2026-10-01 20:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.183 not above reaction high 1.218
- 2026-10-01 20:25Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: price 68.17 still above the 48h low 66.15; realised vol 62% -> weight 0.25
- 2026-10-01 21:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-01 21:23Z ETH hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: price 2698 still above the 48h low 2661; realised vol 36% -> weight 0.25
- 2026-10-01 21:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 118.1 not above reaction high 119.5
- 2026-10-01 21:23Z ADA hold target 0.20 (held 0.25) — hold: weight change -0.048 below threshold 0.05 | stay long: price 0.2473 still above the 48h low 0.2425; realised vol 87% -> weight 0.25
- 2026-10-01 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.01 not above reaction high 11.55
- 2026-10-01 21:23Z LINK hold target 0.20 (held 0.15) — hold: weight change +0.049 below threshold 0.05 | stay long: price 14.38 still above the 48h low 14.18; realised vol 98% -> weight 0.25
- 2026-10-01 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.498 not above reaction high 1.638
- 2026-10-01 21:23Z DOGE hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: price 0.09452 still above the 48h low 0.09297; realised vol 62% -> weight 0.25
- 2026-10-01 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.182 not above reaction high 1.218
- 2026-10-01 21:23Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: price 68.44 still above the 48h low 66.15; realised vol 62% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 22 fills (11 buy / 11 sell), traded 42,616, gross pnl +71.00, +33 bps per round trip, avg half spread 2.2 bps, open 11257.7
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 9 fills (6 buy / 3 sell), traded 9,216, gross pnl -41.03, -89 bps per round trip, avg half spread 1.7 bps, open 23682.3
- DOT: 20 fills (9 buy / 11 sell), traded 32,554, gross pnl +58.88, +36 bps per round trip, avg half spread 2.8 bps
- ETH: 7 fills (4 buy / 3 sell), traded 8,825, gross pnl +87.24, +198 bps per round trip, avg half spread 0.1 bps, open 0.832737
- LINK: 19 fills (9 buy / 10 sell), traded 30,334, gross pnl +251.18, +166 bps per round trip, avg half spread 2.7 bps, open 117.602
- LTC: 34 fills (18 buy / 16 sell), traded 43,238, gross pnl +132.34, +61 bps per round trip, avg half spread 1.9 bps, open 33.1394
- SOL: 14 fills (6 buy / 8 sell), traded 20,342, gross pnl +62.52, +61 bps per round trip, avg half spread 0.5 bps
- XRP: 6 fills (3 buy / 3 sell), traded 6,959, gross pnl +88.07, +253 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-01 17:24Z buy ETH 1,800 @ 2700.54 fee 1.80 slip 0.90 (half spread 0.0 bps)
- 2026-10-01 17:24Z buy ADA 1,379 @ 0.249988 fee 1.38 slip 0.69 (half spread 1.9 bps)
- 2026-10-01 17:24Z buy DOGE 1,388 @ 0.0949706 fee 1.39 slip 0.69 (half spread 0.5 bps)
- 2026-10-01 17:24Z buy LTC 1,391 @ 67.5488 fee 1.39 slip 0.70 (half spread 0.7 bps)
- 2026-10-01 18:29Z sell ETH 565 @ 2698.2 fee 0.56 slip 0.28 (half spread 0.0 bps)
- 2026-10-01 18:29Z sell DOGE 565 @ 0.0948764 fee 0.56 slip 0.28 (half spread 0.4 bps)
- 2026-10-01 18:29Z sell LTC 564 @ 67.8011 fee 0.56 slip 0.28 (half spread 2.2 bps)
- 2026-10-01 18:29Z buy LINK 1,690 @ 14.3682 fee 1.69 slip 0.84 (half spread 0.0 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,112.00 (started 10,000 at 2026-09-25 04:23Z), net +1.12% since start
- 24h +0.30%, 7d +1.20%, 30d +1.20%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 153.57; cost coverage 3.69
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-01 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-01 20:25Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +18.17% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 20:25Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +26.36% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 20:25Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +52.09% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 20:25Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +28.83% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 20:25Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +10.80% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 20:25Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +15.71% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 20:25Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +35.29% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 20:25Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +37.66% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 21:23Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +9.29% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-01 21:23Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +11.47% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 21:23Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +18.02% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 21:23Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +25.95% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 21:23Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +52.28% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 21:23Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +27.90% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 21:23Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +10.64% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 21:23Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +15.37% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 21:23Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +36.49% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 21:23Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +37.98% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +37.95, +189 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +37.79, +833 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +8.42, +162 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -43.70, -848 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl -5.36, -35 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +3.12, +60 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +138.87, +685 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -27.31, -137 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -15.60, -129 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +19.39, +64 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1098 candles, 2026-08-17 03:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1098 candles, 2026-08-17 03:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1098 candles, 2026-08-17 03:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1098 candles, 2026-08-17 03:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1098 candles, 2026-08-17 03:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1098 candles, 2026-08-17 03:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1070 candles, 2026-08-18 07:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1070 candles, 2026-08-18 07:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 1070 candles, 2026-08-18 07:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1070 candles, 2026-08-18 07:00Z to 2026-10-01 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
