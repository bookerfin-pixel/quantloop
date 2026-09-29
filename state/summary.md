# quantloop summary — generated 2026-09-29 15:27Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 13.4 of 60, 46.6 days until the verdict
  so far: champion +15.02% (DD -8.03%, 98 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +0.42% (usual 0.54, this window 0.73) vs challenger1 -7.06% (usual 0.37, this window 0.12); the rule compares on skill, daily edge t -0.7 over 14 days
  market over the window: BTC +10.30%, equal weight basket of 10 pairs +27.15%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 8.3 of 60, 51.7 days until the verdict
  so far: champion +0.11% (DD -8.03%, 60 fills) vs challenger2 -0.61% (DD -0.61%, 1 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.10% (usual 0.54, this window 0.75) vs challenger2 -2.31% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t +0.1 over 9 days
  market over the window: BTC -0.03%, equal weight basket of 10 pairs +5.94%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 4.5 of 60, 55.5 days until the verdict
  so far: champion -3.07% (DD -8.03%, 40 fills) vs challenger3 -1.75% (DD -4.74%, 68 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.04% (usual 0.55, this window 0.75) vs challenger3 -1.94% (usual 0.05, this window 0.32); the rule compares on skill, daily edge t +0.6 over 5 days
  market over the window: BTC -0.58%, equal weight basket of 10 pairs +3.60%, basket max drawdown -5%, basket realised vol 57% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 3.7 of 60, 56.3 days until the verdict
  so far: champion -5.91% (DD -8.03%, 32 fills) vs challenger4 -1.23% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.05% (usual 0.55, this window 0.70) vs challenger4 -1.35% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +1.5 over 4 days
  market over the window: BTC -0.41%, equal weight basket of 10 pairs +0.26%, basket max drawdown -5%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,502.38 (started 10,000 at 2026-09-16 03:55Z), net +15.02% since start
- 24h -1.83%, 7d -3.05%, 30d +15.02%, max drawdown -8.03%
- fills 98 total, 57 in the last 7d
- costs 233.52 (fees 153.81 + slippage 79.71); gross pnl 1,735.90; cost coverage 7.43
- cash 2,924.85; positions: AVAX 259.561, ETH 1.08473, LINK 187.649
- last run 2026-09-29 15:26Z; halted today: False

last decisions (newest last):

- 2026-09-29 14:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.20% not above entry band +1.0%
- 2026-09-29 14:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.52% not above entry band +1.0%
- 2026-09-29 14:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +7.21% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-29 14:25Z LINK hold target 0.25 (held 0.24) — hold: weight change +0.009 below threshold 0.05 | stay long: 72h return +5.85% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-29 14:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.45% not above entry band +1.0%
- 2026-09-29 14:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.46% not above entry band +1.0%
- 2026-09-29 14:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.69% not above entry band +1.0%
- 2026-09-29 14:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.13% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 15:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.34% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 15:26Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +0.80% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-09-29 15:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.64% not above entry band +1.0%
- 2026-09-29 15:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.05% not above entry band +1.0%
- 2026-09-29 15:26Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +4.33% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-29 15:26Z LINK hold target 0.25 (held 0.24) — hold: weight change +0.009 below threshold 0.05 | stay long: 72h return +5.39% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-29 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.06% not above entry band +1.0%
- 2026-09-29 15:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.36% not above entry band +1.0%
- 2026-09-29 15:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.06% not above entry band +1.0%
- 2026-09-29 15:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.09% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (5 buy / 6 sell), traded 18,727, gross pnl +101.44, +108 bps per round trip, avg half spread 2.4 bps
- AVAX: 12 fills (6 buy / 6 sell), traded 21,710, gross pnl +661.35, +609 bps per round trip, avg half spread 1.3 bps, open 259.561
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 15,017, gross pnl -37.42, -50 bps per round trip, avg half spread 1.7 bps
- DOT: 12 fills (7 buy / 5 sell), traded 13,246, gross pnl +261.75, +395 bps per round trip, avg half spread 3.1 bps
- ETH: 5 fills (3 buy / 2 sell), traded 8,364, gross pnl +7.05, +17 bps per round trip, avg half spread 0.1 bps, open 1.08473
- LINK: 15 fills (8 buy / 7 sell), traded 24,437, gross pnl -19.41, -16 bps per round trip, avg half spread 2.8 bps, open 187.649
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-28 08:27Z sell DOT 2,970 @ 1.21149 fee 2.97 slip 1.49 (half spread 2.5 bps)
- 2026-09-28 12:29Z buy LTC 2,971 @ 72.2361 fee 2.97 slip 1.48 (half spread 1.4 bps)
- 2026-09-28 13:25Z buy LINK 2,952 @ 14.5956 fee 2.95 slip 1.48 (half spread 2.3 bps)
- 2026-09-28 14:27Z sell LINK 2,906 @ 14.3673 fee 2.91 slip 2.00 (half spread 4.9 bps)
- 2026-09-28 14:27Z sell LTC 2,862 @ 69.5802 fee 2.86 slip 1.43 (half spread 2.2 bps)
- 2026-09-29 00:29Z buy LINK 2,929 @ 15.6096 fee 2.93 slip 1.56 (half spread 3.3 bps)
- 2026-09-29 07:25Z buy AVAX 2,909 @ 11.2072 fee 2.91 slip 1.75 (half spread 4.0 bps)
- 2026-09-29 10:25Z buy ETH 2,945 @ 2714.73 fee 2.94 slip 1.47 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-29 15:26Z; halted today: False

last decisions (newest last):

- 2026-09-29 14:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.96 not below -2.0
- 2026-09-29 14:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.63 not below -2.0
- 2026-09-29 14:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.98 not below -2.0
- 2026-09-29 14:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.90 not below -2.0
- 2026-09-29 14:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.71 not below -2.0
- 2026-09-29 14:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.21 not below -2.0
- 2026-09-29 14:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.68 not below -2.0
- 2026-09-29 14:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.43 not below -2.0
- 2026-09-29 15:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.14 not below -2.0
- 2026-09-29 15:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.51 not below -2.0
- 2026-09-29 15:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.74 not below -2.0
- 2026-09-29 15:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.64 not below -2.0
- 2026-09-29 15:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.73 not below -2.0
- 2026-09-29 15:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.85 not below -2.0
- 2026-09-29 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.65 not below -2.0
- 2026-09-29 15:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.14 not below -2.0
- 2026-09-29 15:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.84 not below -2.0
- 2026-09-29 15:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.44 not below -2.0

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

- equity 10,898.63 (started 10,000 at 2026-09-16 23:20Z), net +8.99% since start
- 24h -0.61%, 7d -0.61%, 30d +8.99%, max drawdown -3.54%
- fills 33 total, 1 in the last 7d
- costs 83.08 (fees 54.95 + slippage 28.13); gross pnl 981.71; cost coverage 11.82
- cash 8,221.54; positions: ETH 1.00083
- last run 2026-09-29 15:26Z; halted today: False

last decisions (newest last):

- 2026-09-29 14:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 14:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.372e+04 not above 120h high 8.502e+04
- 2026-09-29 15:26Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 2710 still above 72h low 2640; realised vol 35% -> weight 0.25
- 2026-09-29 15:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 15:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 3 fills (2 buy / 1 sell), traded 5,380, gross pnl -12.20, -45 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -72.41, -179 bps per round trip, avg half spread 0.0 bps, open 1.00083
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)
- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)

## challenger3: swing_reversal (H3)

params: {"exit_hours": 48, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,310.97 (started 10,000 at 2026-09-16 23:20Z), net +13.11% since start
- 24h -1.14%, 7d -5.23%, 30d +13.11%, max drawdown -9.51%
- fills 117 total, 79 in the last 7d
- costs 294.76 (fees 193.45 + slippage 101.30); gross pnl 1,605.73; cost coverage 5.45
- cash -0.00; positions: ADA 9141.44, AVAX 212.774, DOT 752.629, LINK 126.153, LTC 25.2009, SOL 18.9043
- last run 2026-09-29 15:26Z; halted today: False

last decisions (newest last):

- 2026-09-29 14:25Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.030 below threshold 0.05 | stay long: price 121 still above the 48h low 116.9; realised vol 54% -> weight 0.25
- 2026-09-29 14:25Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: price 0.2519 still above the 48h low 0.2405; realised vol 86% -> weight 0.25
- 2026-09-29 14:25Z AVAX hold target 0.17 (held 0.21) — hold: weight change -0.046 below threshold 0.05 | stay long: price 11.62 still above the 48h low 10.23; realised vol 102% -> weight 0.25
- 2026-09-29 14:25Z LINK hold target 0.17 (held 0.16) — hold: weight change +0.003 below threshold 0.05 | stay long: price 15.13 still above the 48h low 13.57; realised vol 105% -> weight 0.25
- 2026-09-29 14:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.37 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-29 14:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-29 14:25Z DOT none target 0.17 (held 0.08) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-09-29 14:25Z LTC hold target 0.17 (held 0.15) — hold: weight change +0.018 below threshold 0.05 | stay long: price 68.36 still above the 48h low 67.57; realised vol 104% -> weight 0.25
- 2026-09-29 15:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.023e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-29 15:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2571 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-29 15:26Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.031 below threshold 0.05 | stay long: price 120.2 still above the 48h low 116.9; realised vol 54% -> weight 0.25
- 2026-09-29 15:26Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.031 below threshold 0.05 | stay long: price 0.252 still above the 48h low 0.2405; realised vol 86% -> weight 0.25
- 2026-09-29 15:26Z AVAX hold target 0.17 (held 0.21) — hold: weight change -0.044 below threshold 0.05 | stay long: price 11.51 still above the 48h low 10.23; realised vol 103% -> weight 0.25
- 2026-09-29 15:26Z LINK hold target 0.17 (held 0.16) — hold: weight change +0.002 below threshold 0.05 | stay long: price 15.1 still above the 48h low 13.57; realised vol 105% -> weight 0.25
- 2026-09-29 15:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.37 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-29 15:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-29 15:26Z DOT none target 0.17 (held 0.08) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-09-29 15:26Z LTC hold target 0.17 (held 0.15) — hold: weight change +0.017 below threshold 0.05 | stay long: price 68.45 still above the 48h low 67.57; realised vol 104% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 20 fills (10 buy / 10 sell), traded 40,395, gross pnl +71.62, +35 bps per round trip, avg half spread 2.3 bps, open 9141.44
- AVAX: 16 fills (7 buy / 9 sell), traded 24,842, gross pnl +840.46, +677 bps per round trip, avg half spread 1.6 bps, open 212.774
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 17 fills (8 buy / 9 sell), traded 28,876, gross pnl +24.24, +17 bps per round trip, avg half spread 3.0 bps, open 752.629
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 16 fills (8 buy / 8 sell), traded 26,835, gross pnl +305.59, +228 bps per round trip, avg half spread 3.0 bps, open 126.153
- LTC: 18 fills (9 buy / 9 sell), traded 33,530, gross pnl +97.60, +58 bps per round trip, avg half spread 2.1 bps, open 25.2009
- SOL: 12 fills (6 buy / 6 sell), traded 18,097, gross pnl +51.98, +57 bps per round trip, avg half spread 0.5 bps, open 18.9043
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-29 03:24Z sell LTC 2,797 @ 67.7211 fee 2.80 slip 1.40 (half spread 0.7 bps)
- 2026-09-29 03:24Z buy SOL 2,796 @ 117.854 fee 2.80 slip 1.40 (half spread 0.4 bps)
- 2026-09-29 04:24Z sell SOL 568 @ 117.796 fee 0.57 slip 0.28 (half spread 0.4 bps)
- 2026-09-29 04:24Z sell AVAX 574 @ 10.4658 fee 0.57 slip 0.29 (half spread 1.0 bps)
- 2026-09-29 04:24Z buy ADA 2,228 @ 0.243752 fee 2.23 slip 1.11 (half spread 0.3 bps)
- 2026-09-29 04:24Z buy LTC 1,715 @ 68.069 fee 1.72 slip 0.86 (half spread 0.7 bps)
- 2026-09-29 06:29Z sell LINK 880 @ 14.8797 fee 0.88 slip 0.44 (half spread 1.9 bps)
- 2026-09-29 06:29Z buy DOT 878 @ 1.16658 fee 0.88 slip 0.44 (half spread 2.6 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,127.14 (started 10,000 at 2026-09-25 04:23Z), net +1.27% since start
- 24h -0.81%, 7d +1.35%, 30d +1.35%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 168.71; cost coverage 4.06
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-29 15:26Z; halted today: False

last decisions (newest last):

- 2026-09-29 14:25Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +12.97% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 14:25Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +23.02% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 14:25Z AVAX hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +56.45% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 14:25Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.010 below threshold 0.05 | stay long: 720h return +30.86% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 14:25Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +9.84% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-29 14:25Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +11.77% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 14:25Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +39.59% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 14:25Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +37.55% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +6.27% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-29 15:26Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +9.41% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-29 15:26Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +12.57% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +23.17% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z AVAX hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +55.05% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.010 below threshold 0.05 | stay long: 720h return +30.80% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +10.06% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +11.78% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +42.29% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 15:26Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +37.15% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +31.87, +159 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +54.95, +1211 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -11.46, -220 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -51.62, -1001 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +4.91, +32 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -4.63, -89 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +170.05, +839 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -44.08, -221 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -12.91, -107 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +31.63, +104 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1044 candles, 2026-08-17 03:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1044 candles, 2026-08-17 03:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1044 candles, 2026-08-17 03:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1044 candles, 2026-08-17 03:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1044 candles, 2026-08-17 03:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.2 bps
- LINK: live 1044 candles, 2026-08-17 03:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1016 candles, 2026-08-18 07:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOGE: live 1016 candles, 2026-08-18 07:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 1016 candles, 2026-08-18 07:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1016 candles, 2026-08-18 07:00Z to 2026-09-29 14:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.8 bps
