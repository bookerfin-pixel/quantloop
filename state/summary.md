# quantloop summary — generated 2026-09-30 21:24Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 14.7 of 60, 45.3 days until the verdict
  so far: champion +12.47% (DD -10.07%, 103 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -0.45% (usual 0.54, this window 0.70) vs challenger1 -5.89% (usual 0.37, this window 0.11); the rule compares on skill, daily edge t -0.5 over 15 days
  market over the window: BTC +10.17%, equal weight basket of 10 pairs +24.01%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 9.5 of 60, 50.5 days until the verdict
  so far: champion -2.12% (DD -10.07%, 65 fills) vs challenger2 -1.05% (DD -1.16%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.96% (usual 0.54, this window 0.69) vs challenger2 -2.03% (usual 0.29, this window 0.05); the rule compares on skill, daily edge t +0.2 over 10 days
  market over the window: BTC -0.15%, equal weight basket of 10 pairs +3.41%, basket max drawdown -7%, basket realised vol 62% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 5.8 of 60, 54.2 days until the verdict
  so far: champion -5.23% (DD -10.07%, 45 fills) vs challenger3 -2.32% (DD -4.74%, 88 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.85% (usual 0.55, this window 0.66) vs challenger3 -2.38% (usual 0.05, this window 0.47); the rule compares on skill, daily edge t +0.7 over 6 days
  market over the window: BTC -0.70%, equal weight basket of 10 pairs +1.14%, basket max drawdown -5%, basket realised vol 60% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 5.0 of 60, 55.0 days until the verdict
  so far: champion -8.00% (DD -10.07%, 37 fills) vs challenger4 -1.68% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.84% (usual 0.55, this window 0.60) vs challenger4 -0.66% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.0 over 5 days
  market over the window: BTC -0.53%, equal weight basket of 10 pairs -2.13%, basket max drawdown -5%, basket realised vol 61% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,246.60 (started 10,000 at 2026-09-16 03:55Z), net +12.47% since start
- 24h -2.63%, 7d -1.91%, 30d +12.47%, max drawdown -10.07%
- fills 103 total, 53 in the last 7d
- costs 254.79 (fees 167.88 + slippage 86.91); gross pnl 1,501.39; cost coverage 5.89
- cash 11,246.60; positions: none
- last run 2026-09-30 21:24Z; halted today: False

last decisions (newest last):

- 2026-09-30 20:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.75% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 20:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.99% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 20:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.98% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 20:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-30 20:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.81% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 20:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.22% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 20:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.52% not above entry band +1.0%
- 2026-09-30 20:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.83% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.07% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.17% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.83% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.08% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.52% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-30 21:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.11% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.67% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 21:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.75% not above entry band +1.0%
- 2026-09-30 21:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.57% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (5 buy / 6 sell), traded 18,727, gross pnl +101.44, +108 bps per round trip, avg half spread 2.4 bps
- AVAX: 13 fills (6 buy / 7 sell), traded 24,519, gross pnl +568.68, +464 bps per round trip, avg half spread 1.3 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 15,017, gross pnl -37.42, -50 bps per round trip, avg half spread 1.7 bps
- DOT: 12 fills (7 buy / 5 sell), traded 13,246, gross pnl +261.75, +395 bps per round trip, avg half spread 3.1 bps
- ETH: 6 fills (3 buy / 3 sell), traded 11,261, gross pnl +3.43, +6 bps per round trip, avg half spread 0.1 bps
- LINK: 18 fills (9 buy / 9 sell), traded 32,810, gross pnl -157.64, -96 bps per round trip, avg half spread 2.7 bps
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-29 00:29Z buy LINK 2,929 @ 15.6096 fee 2.93 slip 1.56 (half spread 3.3 bps)
- 2026-09-29 07:25Z buy AVAX 2,909 @ 11.2072 fee 2.91 slip 1.75 (half spread 4.0 bps)
- 2026-09-29 10:25Z buy ETH 2,945 @ 2714.73 fee 2.94 slip 1.47 (half spread 0.0 bps)
- 2026-09-29 18:28Z sell LINK 2,740 @ 14.6027 fee 2.74 slip 1.37 (half spread 0.0 bps)
- 2026-09-30 02:22Z sell ETH 2,896 @ 2670.19 fee 2.90 slip 1.45 (half spread 0.0 bps)
- 2026-09-30 13:27Z buy LINK 2,871 @ 14.6886 fee 2.87 slip 1.43 (half spread 2.2 bps)
- 2026-09-30 15:28Z sell AVAX 2,809 @ 10.8221 fee 2.81 slip 1.41 (half spread 0.5 bps)
- 2026-09-30 15:28Z sell LINK 2,762 @ 14.127 fee 2.76 slip 1.53 (half spread 3.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-30 21:24Z; halted today: False

last decisions (newest last):

- 2026-09-30 20:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-09-30 20:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.74 not below -2.0
- 2026-09-30 20:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-09-30 20:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.66 not below -2.0
- 2026-09-30 20:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.77 not below -2.0
- 2026-09-30 20:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.58 not below -2.0
- 2026-09-30 20:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.77 not below -2.0
- 2026-09-30 20:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.21 not below -2.0
- 2026-09-30 21:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.57 not below -2.0
- 2026-09-30 21:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.48 not below -2.0
- 2026-09-30 21:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.14 not below -2.0
- 2026-09-30 21:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.49 not below -2.0
- 2026-09-30 21:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.24 not below -2.0
- 2026-09-30 21:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.69 not below -2.0
- 2026-09-30 21:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.72 not below -2.0
- 2026-09-30 21:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.48 not below -2.0
- 2026-09-30 21:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.92 not below -2.0
- 2026-09-30 21:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.15 not below -2.0

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

- equity 10,850.12 (started 10,000 at 2026-09-16 23:20Z), net +8.50% since start
- 24h -0.50%, 7d -1.05%, 30d +8.50%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 937.30; cost coverage 10.75
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-09-30 21:24Z; halted today: False

last decisions (newest last):

- 2026-09-30 20:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 20:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 8.362e+04 still above 72h low 8.263e+04; realised vol 32% -> weight 0.25
- 2026-09-30 21:24Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 2681 still above 72h low 2640; realised vol 37% -> weight 0.25
- 2026-09-30 21:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 21:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -63.76, -157 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -65.26, -161 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,244.85 (started 10,000 at 2026-09-16 23:20Z), net +12.45% since start
- 24h -1.40%, 7d -2.32%, 30d +12.45%, max drawdown -9.51%
- fills 137 total, 88 in the last 7d
- costs 317.53 (fees 208.59 + slippage 108.95); gross pnl 1,562.39; cost coverage 4.92
- cash -0.00; positions: ADA 5740.21, AVAX 129.447, DOGE 15015.8, DOT 1141.01, ETH 0.375585, LINK 126.153, SOL 11.8866, XRP 945.012
- last run 2026-09-30 21:24Z; halted today: False

last decisions (newest last):

- 2026-09-30 20:24Z SOL hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 117.2 still above the 48h low 116.9; realised vol 59% -> weight 0.25
- 2026-09-30 20:24Z ADA hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 0.2425 still above the 48h low 0.2405; realised vol 88% -> weight 0.25
- 2026-09-30 20:24Z AVAX hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 10.89 still above the 48h low 10.33; realised vol 99% -> weight 0.25
- 2026-09-30 20:24Z LINK hold target 0.11 (held 0.16) — hold: weight change -0.049 below threshold 0.05 | stay long: price 14.24 still above the 48h low 14.21; realised vol 106% -> weight 0.25
- 2026-09-30 20:24Z XRP hold target 0.11 (held 0.13) — hold: weight change -0.014 below threshold 0.05 | stay long: price 1.488 still above the 48h low 1.476; realised vol 68% -> weight 0.25
- 2026-09-30 20:24Z DOGE hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.094 still above the 48h low 0.09226; realised vol 66% -> weight 0.25
- 2026-09-30 20:24Z DOT hold target 0.11 (held 0.12) — hold: weight change -0.014 below threshold 0.05 | stay long: price 1.222 still above the 48h low 1.151; realised vol 98% -> weight 0.25
- 2026-09-30 20:24Z LTC none target 0.11 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-09-30 21:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.093e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-30 21:24Z ETH hold target 0.11 (held 0.09) — hold: weight change +0.022 below threshold 0.05 | stay long: price 2681 still above the 48h low 2657; realised vol 37% -> weight 0.25
- 2026-09-30 21:24Z SOL hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 118 still above the 48h low 116.9; realised vol 59% -> weight 0.25
- 2026-09-30 21:24Z ADA hold target 0.11 (held 0.12) — hold: weight change -0.014 below threshold 0.05 | stay long: price 0.2444 still above the 48h low 0.2405; realised vol 88% -> weight 0.25
- 2026-09-30 21:24Z AVAX hold target 0.11 (held 0.13) — hold: weight change -0.014 below threshold 0.05 | stay long: price 10.91 still above the 48h low 10.35; realised vol 99% -> weight 0.25
- 2026-09-30 21:24Z LINK hold target 0.11 (held 0.16) — hold: weight change -0.049 below threshold 0.05 | stay long: price 14.27 still above the 48h low 14.21; realised vol 106% -> weight 0.25
- 2026-09-30 21:24Z XRP hold target 0.11 (held 0.13) — hold: weight change -0.014 below threshold 0.05 | stay long: price 1.491 still above the 48h low 1.476; realised vol 68% -> weight 0.25
- 2026-09-30 21:24Z DOGE hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.09435 still above the 48h low 0.09226; realised vol 66% -> weight 0.25
- 2026-09-30 21:24Z DOT hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 1.229 still above the 48h low 1.151; realised vol 98% -> weight 0.25
- 2026-09-30 21:24Z LTC none target 0.11 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (10 buy / 11 sell), traded 41,237, gross pnl +76.50, +37 bps per round trip, avg half spread 2.2 bps, open 5740.21
- AVAX: 17 fills (7 buy / 10 sell), traded 25,757, gross pnl +788.18, +612 bps per round trip, avg half spread 1.5 bps, open 129.447
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 7 fills (5 buy / 2 sell), traded 7,263, gross pnl -37.56, -103 bps per round trip, avg half spread 2.0 bps, open 15015.8
- DOT: 19 fills (9 buy / 10 sell), traded 31,210, gross pnl +108.74, +70 bps per round trip, avg half spread 2.9 bps, open 1141.01
- ETH: 5 fills (3 buy / 2 sell), traded 6,460, gross pnl +84.30, +261 bps per round trip, avg half spread 0.1 bps, open 0.375585
- LINK: 16 fills (8 buy / 8 sell), traded 26,835, gross pnl +245.83, +183 bps per round trip, avg half spread 3.0 bps, open 126.153
- LTC: 30 fills (15 buy / 15 sell), traded 39,880, gross pnl +90.54, +45 bps per round trip, avg half spread 2.0 bps
- SOL: 13 fills (6 buy / 7 sell), traded 18,936, gross pnl +57.17, +60 bps per round trip, avg half spread 0.5 bps, open 11.8866
- XRP: 5 fills (3 buy / 2 sell), traded 5,553, gross pnl +89.02, +321 bps per round trip, avg half spread 0.7 bps, open 945.012

last fills:

- 2026-09-30 17:24Z sell ADA 842 @ 0.24757 fee 0.84 slip 0.42 (half spread 0.0 bps)
- 2026-09-30 17:24Z sell AVAX 915 @ 10.978 fee 0.91 slip 0.46 (half spread 1.4 bps)
- 2026-09-30 17:24Z sell DOT 959 @ 1.24543 fee 0.96 slip 0.48 (half spread 1.2 bps)
- 2026-09-30 17:24Z buy XRP 1,422 @ 1.50499 fee 1.42 slip 0.71 (half spread 0.4 bps)
- 2026-09-30 17:24Z buy DOGE 1,422 @ 0.094716 fee 1.42 slip 0.71 (half spread 0.3 bps)
- 2026-09-30 17:24Z buy LTC 703 @ 66.9685 fee 0.70 slip 0.35 (half spread 0.7 bps)
- 2026-09-30 19:25Z sell LTC 1,008 @ 65.947 fee 1.01 slip 0.50 (half spread 1.5 bps)
- 2026-09-30 20:24Z buy ETH 1,006 @ 2679.68 fee 1.01 slip 0.50 (half spread 0.0 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,081.71 (started 10,000 at 2026-09-25 04:23Z), net +0.82% since start
- 24h -0.83%, 7d +0.89%, 30d +0.89%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 123.28; cost coverage 2.97
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-30 21:24Z; halted today: False

last decisions (newest last):

- 2026-09-30 20:24Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +13.10% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 20:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +21.73% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 20:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +51.10% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 20:24Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +24.78% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 20:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.28% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 20:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +12.86% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 20:24Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +46.13% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 20:24Z LTC hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +35.33% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 21:24Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +6.06% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 21:24Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +8.44% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-30 21:24Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +13.75% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 21:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +23.01% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 21:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +51.23% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 21:24Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +25.45% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 21:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.53% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 21:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +13.33% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 21:24Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +47.44% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 21:24Z LTC hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +36.10% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +29.07, +145 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +31.34, +691 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -3.06, -59 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -44.74, -868 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +34.07, +223 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -1.86, -36 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +134.38, +663 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -55.80, -280 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -16.11, -134 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +16.00, +52 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1074 candles, 2026-08-17 03:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1074 candles, 2026-08-17 03:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1074 candles, 2026-08-17 03:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1074 candles, 2026-08-17 03:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- AVAX: live 1074 candles, 2026-08-17 03:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1074 candles, 2026-08-17 03:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- XRP: live 1046 candles, 2026-08-18 07:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1046 candles, 2026-08-18 07:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 1046 candles, 2026-08-18 07:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 1046 candles, 2026-08-18 07:00Z to 2026-09-30 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.8 bps
