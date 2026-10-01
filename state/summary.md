# quantloop summary — generated 2026-10-01 14:27Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 15.4 of 60, 44.6 days until the verdict
  so far: champion +10.87% (DD -11.90%, 127 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.17% (usual 0.54, this window 0.70) vs challenger1 -5.98% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.4 over 16 days
  market over the window: BTC +10.55%, equal weight basket of 10 pairs +24.25%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 10.3 of 60, 49.7 days until the verdict
  so far: champion -3.51% (DD -11.90%, 89 fills) vs challenger2 -0.76% (DD -1.17%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.46% (usual 0.54, this window 0.70) vs challenger2 -1.80% (usual 0.29, this window 0.08); the rule compares on skill, daily edge t +0.4 over 11 days
  market over the window: BTC +0.20%, equal weight basket of 10 pairs +3.61%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 6.5 of 60, 53.5 days until the verdict
  so far: champion -6.57% (DD -11.90%, 69 fills) vs challenger3 -2.27% (DD -4.74%, 90 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.29% (usual 0.55, this window 0.66) vs challenger3 -2.34% (usual 0.05, this window 0.52); the rule compares on skill, daily edge t +1.0 over 7 days
  market over the window: BTC -0.35%, equal weight basket of 10 pairs +1.31%, basket max drawdown -5%, basket realised vol 58% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 5.7 of 60, 54.3 days until the verdict
  so far: champion -9.31% (DD -11.90%, 61 fills) vs challenger4 -1.48% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.24% (usual 0.55, this window 0.62) vs challenger4 -0.55% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.6 over 6 days
  market over the window: BTC -0.18%, equal weight basket of 10 pairs -1.95%, basket max drawdown -5%, basket realised vol 59% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,087.27 (started 10,000 at 2026-09-16 03:55Z), net +10.87% since start
- 24h -1.79%, 7d -7.47%, 30d +10.87%, max drawdown -11.90%
- fills 127 total, 75 in the last 7d
- costs 305.80 (fees 201.89 + slippage 103.91); gross pnl 1,393.07; cost coverage 4.56
- cash -0.00; positions: AVAX 252.39, BTC 0.0330404, DOGE 29185.8, ETH 1.02721
- last run 2026-10-01 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-01 13:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.23% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 13:29Z ADA sell target 0.00 (held 0.12) — exit: 72h return -1.85% fell below exit band -1.0%
- 2026-10-01 13:29Z AVAX buy target 0.25 (held 0.13) — stay long: 72h return +4.10% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 99% -> weight 0.25
- 2026-10-01 13:29Z LINK sell target 0.00 (held 0.13) — exit: 72h return -2.98% fell below exit band -1.0%
- 2026-10-01 13:29Z XRP sell target 0.00 (held 0.12) — exit: 72h return -2.42% fell below exit band -1.0%
- 2026-10-01 13:29Z DOGE buy target 0.25 (held 0.13) — stay long: 72h return +0.04% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 64% -> weight 0.25
- 2026-10-01 13:29Z DOT sell target 0.00 (held 0.12) — exit: price more than 2.0% below 24h EMA
- 2026-10-01 13:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.40% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 14:27Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +0.35% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-01 14:27Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.26% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-01 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.54% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.77% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 14:27Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +4.67% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.45% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.03% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 14:27Z DOGE hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.79% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-01 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.24% not above entry band +1.0% and price below 24h EMA
- 2026-10-01 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.52% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 13 fills (6 buy / 7 sell), traded 21,499, gross pnl +59.73, +56 bps per round trip, avg half spread 2.3 bps
- AVAX: 17 fills (8 buy / 9 sell), traded 30,112, gross pnl +573.12, +381 bps per round trip, avg half spread 1.3 bps, open 252.39
- BTC: 6 fills (4 buy / 2 sell), traded 8,222, gross pnl +70.32, +171 bps per round trip, avg half spread 0.4 bps, open 0.0330404
- DOGE: 13 fills (8 buy / 5 sell), traded 19,479, gross pnl -41.81, -43 bps per round trip, avg half spread 1.4 bps, open 29185.8
- DOT: 15 fills (8 buy / 7 sell), traded 17,668, gross pnl +189.99, +215 bps per round trip, avg half spread 3.0 bps
- ETH: 10 fills (5 buy / 5 sell), traded 16,866, gross pnl +27.57, +33 bps per round trip, avg half spread 0.1 bps, open 1.02721
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
- last run 2026-10-01 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-01 13:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.62 not below -2.0
- 2026-10-01 13:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.24 not below -2.0
- 2026-10-01 13:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.46 not below -2.0
- 2026-10-01 13:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.64 not below -2.0
- 2026-10-01 13:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.08 not below -2.0
- 2026-10-01 13:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.65 not below -2.0
- 2026-10-01 13:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.01 not below -2.0
- 2026-10-01 13:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0
- 2026-10-01 14:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-10-01 14:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.03 not below -2.0
- 2026-10-01 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.33 not below -2.0
- 2026-10-01 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.25 not below -2.0
- 2026-10-01 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.49 not below -2.0
- 2026-10-01 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.68 not below -2.0
- 2026-10-01 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.98 not below -2.0
- 2026-10-01 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.59 not below -2.0
- 2026-10-01 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.01 not below -2.0
- 2026-10-01 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.16 not below -2.0

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

- equity 10,881.87 (started 10,000 at 2026-09-16 23:20Z), net +8.82% since start
- 24h +0.31%, 7d -0.76%, 30d +8.82%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 969.06; cost coverage 11.12
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-01 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-01 13:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 13:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 8.392e+04 still above 72h low 8.294e+04; realised vol 31% -> weight 0.25
- 2026-10-01 14:27Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 2697 still above 72h low 2657; realised vol 37% -> weight 0.25
- 2026-10-01 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -49.02, -121 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -48.24, -119 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,251.11 (started 10,000 at 2026-09-16 23:20Z), net +12.51% since start
- 24h +0.01%, 7d -2.27%, 30d +12.51%, max drawdown -9.51%
- fills 139 total, 90 in the last 7d
- costs 319.22 (fees 209.71 + slippage 109.51); gross pnl 1,570.33; cost coverage 4.92
- cash -0.00; positions: ADA 5740.21, AVAX 129.447, DOGE 15015.8, DOT 1141.01, ETH 0.375585, LINK 86.9199, LTC 8.36491, SOL 11.8866, XRP 945.012
- last run 2026-10-01 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-01 13:29Z SOL hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 117.3 still above the 48h low 117.2; realised vol 58% -> weight 0.25
- 2026-10-01 13:29Z ADA hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.2475 still above the 48h low 0.2413; realised vol 87% -> weight 0.25
- 2026-10-01 13:29Z AVAX hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 10.97 still above the 48h low 10.85; realised vol 99% -> weight 0.25
- 2026-10-01 13:29Z LINK hold target 0.11 (held 0.16) — hold: weight change -0.050 below threshold 0.05 | stay long: price 14.32 still above the 48h low 14.21; realised vol 105% -> weight 0.25
- 2026-10-01 13:29Z XRP hold target 0.11 (held 0.12) — hold: weight change -0.014 below threshold 0.05 | stay long: price 1.487 still above the 48h low 1.482; realised vol 65% -> weight 0.25
- 2026-10-01 13:29Z DOGE hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.09452 still above the 48h low 0.09297; realised vol 64% -> weight 0.25
- 2026-10-01 13:29Z DOT hold target 0.11 (held 0.12) — hold: weight change -0.010 below threshold 0.05 | stay long: price 1.194 still above the 48h low 1.163; realised vol 98% -> weight 0.25
- 2026-10-01 13:29Z LTC none target 0.11 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-01 14:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-01 14:27Z ETH hold target 0.11 (held 0.09) — hold: weight change +0.021 below threshold 0.05 | stay long: price 2697 still above the 48h low 2661; realised vol 37% -> weight 0.25
- 2026-10-01 14:27Z SOL hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 118 still above the 48h low 117.2; realised vol 58% -> weight 0.25
- 2026-10-01 14:27Z ADA hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.2475 still above the 48h low 0.2413; realised vol 86% -> weight 0.25
- 2026-10-01 14:27Z AVAX hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 10.98 still above the 48h low 10.85; realised vol 98% -> weight 0.25
- 2026-10-01 14:27Z LINK sell target 0.11 (held 0.16) — stay long: price 14.36 still above the 48h low 14.21; realised vol 104% -> weight 0.25
- 2026-10-01 14:27Z XRP hold target 0.11 (held 0.12) — hold: weight change -0.014 below threshold 0.05 | stay long: price 1.49 still above the 48h low 1.482; realised vol 64% -> weight 0.25
- 2026-10-01 14:27Z DOGE hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.0947 still above the 48h low 0.09297; realised vol 63% -> weight 0.25
- 2026-10-01 14:27Z DOT hold target 0.11 (held 0.12) — hold: weight change -0.009 below threshold 0.05 | stay long: price 1.195 still above the 48h low 1.163; realised vol 96% -> weight 0.25
- 2026-10-01 14:27Z LTC buy target 0.11 (held 0.00) — enter long: higher low 59.46 vs prior low 50.28 (+18.3%) then broke above the reaction high 64.52 at 67.15; realised vol 70% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (10 buy / 11 sell), traded 41,237, gross pnl +91.47, +44 bps per round trip, avg half spread 2.2 bps, open 5740.21
- AVAX: 17 fills (7 buy / 10 sell), traded 25,757, gross pnl +797.95, +620 bps per round trip, avg half spread 1.5 bps, open 129.447
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 7 fills (5 buy / 2 sell), traded 7,263, gross pnl -31.64, -87 bps per round trip, avg half spread 2.0 bps, open 15015.8
- DOT: 19 fills (9 buy / 10 sell), traded 31,210, gross pnl +70.80, +45 bps per round trip, avg half spread 2.9 bps, open 1141.01
- ETH: 5 fills (3 buy / 2 sell), traded 6,460, gross pnl +90.69, +281 bps per round trip, avg half spread 0.1 bps, open 0.375585
- LINK: 17 fills (8 buy / 9 sell), traded 27,399, gross pnl +255.63, +187 bps per round trip, avg half spread 2.9 bps, open 86.9199
- LTC: 31 fills (16 buy / 15 sell), traded 40,443, gross pnl +90.54, +45 bps per round trip, avg half spread 1.9 bps, open 8.36491
- SOL: 13 fills (6 buy / 7 sell), traded 18,936, gross pnl +58.24, +62 bps per round trip, avg half spread 0.5 bps, open 11.8866
- XRP: 5 fills (3 buy / 2 sell), traded 5,553, gross pnl +86.99, +313 bps per round trip, avg half spread 0.7 bps, open 945.012

last fills:

- 2026-09-30 17:24Z sell DOT 959 @ 1.24543 fee 0.96 slip 0.48 (half spread 1.2 bps)
- 2026-09-30 17:24Z buy XRP 1,422 @ 1.50499 fee 1.42 slip 0.71 (half spread 0.4 bps)
- 2026-09-30 17:24Z buy DOGE 1,422 @ 0.094716 fee 1.42 slip 0.71 (half spread 0.3 bps)
- 2026-09-30 17:24Z buy LTC 703 @ 66.9685 fee 0.70 slip 0.35 (half spread 0.7 bps)
- 2026-09-30 19:25Z sell LTC 1,008 @ 65.947 fee 1.01 slip 0.50 (half spread 1.5 bps)
- 2026-09-30 20:24Z buy ETH 1,006 @ 2679.68 fee 1.01 slip 0.50 (half spread 0.0 bps)
- 2026-10-01 14:27Z sell LINK 564 @ 14.3742 fee 0.56 slip 0.28 (half spread 1.3 bps)
- 2026-10-01 14:27Z buy LTC 563 @ 67.2836 fee 0.56 slip 0.28 (half spread 1.5 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,102.00 (started 10,000 at 2026-09-25 04:23Z), net +1.02% since start
- 24h +0.08%, 7d +1.10%, 30d +1.10%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 143.57; cost coverage 3.45
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-01 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-01 13:29Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +15.12% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 13:29Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +24.86% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 13:29Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.006 below threshold 0.05 | stay long: 720h return +50.68% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 13:29Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +25.70% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 13:29Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +8.59% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-01 13:29Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +14.41% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 13:29Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +38.92% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 13:29Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +36.49% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 14:27Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +7.53% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-01 14:27Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +10.37% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 14:27Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +15.76% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 14:27Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +24.54% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 14:27Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.006 below threshold 0.05 | stay long: 720h return +50.75% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 14:27Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +26.14% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 14:27Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +8.36% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-01 14:27Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +14.59% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 14:27Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +38.53% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 14:27Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +35.79% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +39.67, +198 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +37.84, +834 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +2.63, +51 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -40.62, -788 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +5.26, +34 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +4.71, +91 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +140.23, +692 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -45.37, -228 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -15.34, -127 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +14.57, +48 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1091 candles, 2026-08-17 03:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1091 candles, 2026-08-17 03:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1091 candles, 2026-08-17 03:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1091 candles, 2026-08-17 03:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1091 candles, 2026-08-17 03:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1091 candles, 2026-08-17 03:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1063 candles, 2026-08-18 07:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1063 candles, 2026-08-18 07:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 1063 candles, 2026-08-18 07:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1063 candles, 2026-08-18 07:00Z to 2026-10-01 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
