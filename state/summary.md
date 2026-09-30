# quantloop summary — generated 2026-09-30 16:28Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 14.5 of 60, 45.5 days until the verdict
  so far: champion +12.47% (DD -10.07%, 103 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -0.84% (usual 0.54, this window 0.71) vs challenger1 -6.16% (usual 0.37, this window 0.11); the rule compares on skill, daily edge t -0.5 over 15 days
  market over the window: BTC +10.78%, equal weight basket of 10 pairs +24.74%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 9.3 of 60, 50.7 days until the verdict
  so far: champion -2.12% (DD -10.07%, 65 fills) vs challenger2 -0.81% (DD -1.12%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.29% (usual 0.54, this window 0.71) vs challenger2 -1.96% (usual 0.29, this window 0.04); the rule compares on skill, daily edge t +0.3 over 10 days
  market over the window: BTC +0.40%, equal weight basket of 10 pairs +4.02%, basket max drawdown -7%, basket realised vol 62% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 5.5 of 60, 54.5 days until the verdict
  so far: champion -5.23% (DD -10.07%, 45 fills) vs challenger3 -1.04% (DD -4.74%, 79 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.17% (usual 0.55, this window 0.68) vs challenger3 -1.14% (usual 0.05, this window 0.45); the rule compares on skill, daily edge t +0.9 over 6 days
  market over the window: BTC -0.15%, equal weight basket of 10 pairs +1.73%, basket max drawdown -5%, basket realised vol 60% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 4.8 of 60, 55.2 days until the verdict
  so far: champion -8.00% (DD -10.07%, 37 fills) vs challenger4 -0.59% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.15% (usual 0.55, this window 0.63) vs challenger4 +0.15% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.1 over 5 days
  market over the window: BTC +0.02%, equal weight basket of 10 pairs -1.56%, basket max drawdown -5%, basket realised vol 61% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,246.60 (started 10,000 at 2026-09-16 03:55Z), net +12.47% since start
- 24h -1.79%, 7d -1.91%, 30d +12.47%, max drawdown -10.07%
- fills 103 total, 53 in the last 7d
- costs 254.79 (fees 167.88 + slippage 86.91); gross pnl 1,501.39; cost coverage 5.89
- cash 11,246.60; positions: none
- last run 2026-09-30 16:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 15:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.38% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 15:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.35% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 15:28Z AVAX sell target 0.00 (held 0.25) — exit: price more than 2.0% below 24h EMA
- 2026-09-30 15:28Z LINK sell target 0.00 (held 0.25) — exit: price more than 2.0% below 24h EMA
- 2026-09-30 15:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 15:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.00% not above entry band +1.0%
- 2026-09-30 15:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.60% not above entry band +1.0%
- 2026-09-30 15:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.65% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 16:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.43% not above entry band +1.0%
- 2026-09-30 16:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.28% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 16:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.05% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 16:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.89% not above entry band +1.0%
- 2026-09-30 16:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.59% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 16:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.91% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 16:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.74% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 16:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-30 16:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.17% not above entry band +1.0%
- 2026-09-30 16:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.72% not above entry band +1.0% and price below 24h EMA

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
- last run 2026-09-30 16:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 15:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.20 not below -2.0
- 2026-09-30 15:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.34 not below -2.0
- 2026-09-30 15:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-09-30 15:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.66 not below -2.0
- 2026-09-30 15:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.48 not below -2.0
- 2026-09-30 15:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.27 not below -2.0
- 2026-09-30 15:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.84 not below -2.0
- 2026-09-30 15:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.09 not below -2.0
- 2026-09-30 16:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.12 not below -2.0
- 2026-09-30 16:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.41 not below -2.0
- 2026-09-30 16:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.35 not below -2.0
- 2026-09-30 16:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.08 not below -2.0
- 2026-09-30 16:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.32 not below -2.0
- 2026-09-30 16:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.69 not below -2.0
- 2026-09-30 16:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-09-30 16:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.11 not below -2.0
- 2026-09-30 16:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.07 not below -2.0
- 2026-09-30 16:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.00 not below -2.0

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

- equity 10,876.39 (started 10,000 at 2026-09-16 23:20Z), net +8.76% since start
- 24h -0.20%, 7d -0.81%, 30d +8.76%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 963.58; cost coverage 11.05
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-09-30 16:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 15:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 15:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 8.408e+04 still above 72h low 8.263e+04; realised vol 32% -> weight 0.25
- 2026-09-30 16:27Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 2682 still above 72h low 2640; realised vol 37% -> weight 0.25
- 2026-09-30 16:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 16:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -43.07, -106 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -59.67, -147 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,392.05 (started 10,000 at 2026-09-16 23:20Z), net +13.92% since start
- 24h +1.72%, 7d -1.04%, 30d +13.92%, max drawdown -9.51%
- fills 128 total, 79 in the last 7d
- costs 303.85 (fees 199.47 + slippage 104.39); gross pnl 1,695.91; cost coverage 5.58
- cash 0.00; positions: ADA 9141.44, AVAX 212.774, DOT 1910.95, LINK 126.153, LTC 4.79236, SOL 18.9043
- last run 2026-09-30 16:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 15:28Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: price 118.8 still above the 48h low 116.9; realised vol 58% -> weight 0.25
- 2026-09-30 15:28Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: price 0.2448 still above the 48h low 0.2405; realised vol 87% -> weight 0.25
- 2026-09-30 15:28Z AVAX hold target 0.17 (held 0.21) — hold: weight change -0.039 below threshold 0.05 | stay long: price 10.89 still above the 48h low 10.23; realised vol 100% -> weight 0.25
- 2026-09-30 15:28Z LINK hold target 0.17 (held 0.16) — hold: weight change +0.007 below threshold 0.05 | stay long: price 14.21 still above the 48h low 14.18; realised vol 106% -> weight 0.25
- 2026-09-30 15:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.378 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-30 15:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08507 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-30 15:28Z DOT hold target 0.17 (held 0.21) — hold: weight change -0.041 below threshold 0.05 | stay long: price 1.223 still above the 48h low 1.151; realised vol 98% -> weight 0.25
- 2026-09-30 15:28Z LTC none target 0.17 (held 0.03) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-09-30 16:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.088e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-30 16:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2612 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-30 16:27Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: price 119.2 still above the 48h low 116.9; realised vol 58% -> weight 0.25
- 2026-09-30 16:27Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: price 0.2469 still above the 48h low 0.2405; realised vol 87% -> weight 0.25
- 2026-09-30 16:27Z AVAX hold target 0.17 (held 0.21) — hold: weight change -0.039 below threshold 0.05 | stay long: price 10.95 still above the 48h low 10.33; realised vol 99% -> weight 0.25
- 2026-09-30 16:27Z LINK hold target 0.17 (held 0.16) — hold: weight change +0.007 below threshold 0.05 | stay long: price 14.24 still above the 48h low 14.21; realised vol 106% -> weight 0.25
- 2026-09-30 16:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.391 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-30 16:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.0858 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-30 16:27Z DOT hold target 0.17 (held 0.21) — hold: weight change -0.042 below threshold 0.05 | stay long: price 1.233 still above the 48h low 1.151; realised vol 98% -> weight 0.25
- 2026-09-30 16:27Z LTC none target 0.17 (held 0.03) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 20 fills (10 buy / 10 sell), traded 40,395, gross pnl +99.76, +49 bps per round trip, avg half spread 2.3 bps, open 9141.44
- AVAX: 16 fills (7 buy / 9 sell), traded 24,842, gross pnl +804.72, +648 bps per round trip, avg half spread 1.6 bps, open 212.774
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 18 fills (9 buy / 9 sell), traded 30,251, gross pnl +136.33, +90 bps per round trip, avg half spread 3.0 bps, open 1910.95
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 16 fills (8 buy / 8 sell), traded 26,835, gross pnl +254.92, +190 bps per round trip, avg half spread 3.0 bps, open 126.153
- LTC: 28 fills (14 buy / 14 sell), traded 38,169, gross pnl +106.65, +56 bps per round trip, avg half spread 2.0 bps, open 4.79236
- SOL: 12 fills (6 buy / 6 sell), traded 18,097, gross pnl +79.29, +88 bps per round trip, avg half spread 0.5 bps, open 18.9043
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-29 18:28Z sell LTC 330 @ 67.3913 fee 0.33 slip 0.17 (half spread 0.7 bps)
- 2026-09-29 19:24Z buy LTC 329 @ 67.6838 fee 0.33 slip 0.16 (half spread 1.5 bps)
- 2026-09-29 22:23Z sell LTC 327 @ 67.0814 fee 0.33 slip 0.16 (half spread 2.2 bps)
- 2026-09-29 23:21Z buy LTC 326 @ 67.0635 fee 0.33 slip 0.16 (half spread 1.5 bps)
- 2026-09-30 00:32Z sell LTC 324 @ 66.7216 fee 0.32 slip 0.16 (half spread 2.2 bps)
- 2026-09-30 01:24Z buy LTC 324 @ 67.3136 fee 0.32 slip 0.16 (half spread 3.0 bps)
- 2026-09-30 07:27Z sell LTC 321 @ 66.6916 fee 0.32 slip 0.16 (half spread 2.2 bps)
- 2026-09-30 08:27Z buy LTC 320 @ 66.7633 fee 0.32 slip 0.18 (half spread 3.7 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,193.16 (started 10,000 at 2026-09-25 04:23Z), net +1.93% since start
- 24h +1.47%, 7d +2.01%, 30d +2.01%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 234.73; cost coverage 5.65
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-30 16:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 15:28Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +14.79% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 15:28Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +24.35% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 15:28Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +50.63% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 15:28Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +25.49% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 15:28Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +8.71% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 15:28Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +14.11% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 15:28Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +47.23% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 15:28Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +37.52% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 16:27Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +7.03% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-30 16:27Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +8.71% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-30 16:27Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +16.01% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 16:27Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +26.08% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 16:27Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +51.95% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 16:27Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +25.12% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 16:27Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +9.64% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 16:27Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +15.13% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 16:27Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +49.57% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 16:27Z LTC hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +38.27% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +44.38, +221 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +40.50, +893 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +4.93, +95 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -34.76, -674 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +55.08, +361 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +0.29, +6 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +139.80, +690 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -45.37, -228 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -0.58, -5 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +30.45, +100 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1069 candles, 2026-08-17 03:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1069 candles, 2026-08-17 03:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1069 candles, 2026-08-17 03:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1069 candles, 2026-08-17 03:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- AVAX: live 1069 candles, 2026-08-17 03:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1069 candles, 2026-08-17 03:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 1041 candles, 2026-08-18 07:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOGE: live 1041 candles, 2026-08-18 07:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 1041 candles, 2026-08-18 07:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1041 candles, 2026-08-18 07:00Z to 2026-09-30 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.8 bps
