# quantloop summary — generated 2026-09-23 16:24Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 7.5 of 60, 52.5 days until the verdict
  so far: champion +14.65% (DD -6.66%, 50 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +10.66%, equal weight basket of 10 pairs +17.48%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 2.3 of 60, 57.7 days until the verdict
  so far: champion -0.22% (DD -6.66%, 12 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  market over the window: BTC +0.30%, equal weight basket of 10 pairs -1.91%, basket max drawdown -7%, basket realised vol 65% annualised
- challenger3: testing H3 since 2026-09-21 22:21Z, day 1.8 of 60, 58.2 days until the verdict
  so far: champion -5.05% (DD -6.66%, 12 fills) vs challenger3 -4.66% (DD -6.43%, 11 fills)
  market over the window: BTC -2.82%, equal weight basket of 10 pairs -5.58%, basket max drawdown -7%, basket realised vol 68% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,465.09 (started 10,000 at 2026-09-16 03:55Z), net +14.65% since start
- 24h -4.14%, 7d +14.65%, 30d +14.65%, max drawdown -6.66%
- fills 50 total, 50 in the last 7d
- costs 101.26 (fees 66.63 + slippage 34.62); gross pnl 1,566.35; cost coverage 15.47
- cash 11,465.09; positions: none
- last run 2026-09-23 16:24Z; halted today: True

last decisions (newest last):

- 2026-09-23 15:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 7,783, gross pnl +116.26, +299 bps per round trip, avg half spread 2.4 bps
- AVAX: 8 fills (3 buy / 5 sell), traded 13,938, gross pnl +760.09, +1091 bps per round trip, avg half spread 1.3 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,468, gross pnl -17.30, -63 bps per round trip, avg half spread 2.3 bps
- DOT: 6 fills (3 buy / 3 sell), traded 5,821, gross pnl +205.16, +705 bps per round trip, avg half spread 3.5 bps
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 4 fills (2 buy / 2 sell), traded 5,799, gross pnl +34.05, +117 bps per round trip, avg half spread 2.8 bps
- LTC: 5 fills (2 buy / 3 sell), traded 7,523, gross pnl +177.57, +472 bps per round trip, avg half spread 2.3 bps
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-23 14:23Z sell BTC 1,463 @ 84040.5 fee 1.46 slip 0.73 (half spread 2.3 bps)
- 2026-09-23 14:23Z sell ETH 1,429 @ 2649.95 fee 1.43 slip 0.71 (half spread 0.6 bps)
- 2026-09-23 14:23Z sell SOL 1,170 @ 113.378 fee 1.17 slip 0.59 (half spread 0.4 bps)
- 2026-09-23 14:23Z sell ADA 1,481 @ 0.237347 fee 1.48 slip 0.74 (half spread 2.9 bps)
- 2026-09-23 14:23Z sell LINK 1,397 @ 12.2379 fee 1.40 slip 0.77 (half spread 3.5 bps)
- 2026-09-23 14:23Z sell XRP 1,531 @ 1.51841 fee 1.53 slip 0.77 (half spread 1.9 bps)
- 2026-09-23 14:23Z sell DOGE 1,236 @ 0.0938014 fee 1.24 slip 1.15 (half spread 7.3 bps)
- 2026-09-23 14:23Z sell LTC 1,466 @ 60.04 fee 1.47 slip 0.73 (half spread 1.7 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +3.74%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 4 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-23 16:24Z; halted today: False

last decisions (newest last):

- 2026-09-23 15:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.05 not below -2.0
- 2026-09-23 15:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.04 not below -2.0
- 2026-09-23 15:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.95 not below -2.0
- 2026-09-23 15:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.49 not below -2.0
- 2026-09-23 15:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-09-23 15:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.06 not below -2.0
- 2026-09-23 15:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.36 not below -2.0
- 2026-09-23 15:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.14 not below -2.0
- 2026-09-23 16:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.04 not below -2.0
- 2026-09-23 16:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.69 not below -2.0
- 2026-09-23 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.88 not below -2.0
- 2026-09-23 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.90 not below -2.0
- 2026-09-23 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.80 not below -2.0
- 2026-09-23 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.29 not below -2.0
- 2026-09-23 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.06 not below -2.0
- 2026-09-23 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-09-23 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-09-23 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.81 not below -2.0

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

- equity 10,965.71 (started 10,000 at 2026-09-16 23:20Z), net +9.66% since start
- 24h +0.00%, 7d +9.66%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 32 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-23 16:24Z; halted today: False

last decisions (newest last):

- 2026-09-23 15:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 15:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-23 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 3 fills (2 buy / 1 sell), traded 5,380, gross pnl -12.20, -45 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 3 fills (2 buy / 1 sell), traded 5,361, gross pnl -9.44, -35 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)

## challenger3: swing_reversal (H3)

params: {"exit_hours": 48, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,512.35 (started 10,000 at 2026-09-16 23:20Z), net +15.12% since start
- 24h -4.18%, 7d +15.12%, 30d +15.12%, max drawdown -6.43%
- fills 49 total, 49 in the last 7d
- costs 101.31 (fees 66.66 + slippage 34.64); gross pnl 1,613.66; cost coverage 15.93
- cash 11,512.35; positions: none
- last run 2026-09-23 16:24Z; halted today: True

last decisions (newest last):

- 2026-09-23 15:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 15:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day
- 2026-09-23 16:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | daily halt in force: flat for the rest of the UTC day

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 7,783, gross pnl +116.26, +299 bps per round trip, avg half spread 2.4 bps
- AVAX: 8 fills (3 buy / 5 sell), traded 13,906, gross pnl +728.79, +1048 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 5 fills (2 buy / 3 sell), traded 5,421, gross pnl +207.63, +766 bps per round trip, avg half spread 3.6 bps
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 4 fills (2 buy / 2 sell), traded 5,855, gross pnl +90.07, +308 bps per round trip, avg half spread 2.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 7,523, gross pnl +177.57, +472 bps per round trip, avg half spread 2.3 bps
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-23 13:24Z sell ETH 1,463 @ 2713.17 fee 1.46 slip 0.73 (half spread 0.4 bps)
- 2026-09-23 14:23Z sell BTC 1,463 @ 84040.5 fee 1.46 slip 0.73 (half spread 2.3 bps)
- 2026-09-23 14:23Z sell SOL 1,170 @ 113.378 fee 1.17 slip 0.59 (half spread 0.4 bps)
- 2026-09-23 14:23Z sell ADA 1,481 @ 0.237347 fee 1.48 slip 0.74 (half spread 2.9 bps)
- 2026-09-23 14:23Z sell AVAX 1,293 @ 10.3313 fee 1.29 slip 0.65 (half spread 2.4 bps)
- 2026-09-23 14:23Z sell XRP 1,531 @ 1.51841 fee 1.53 slip 0.77 (half spread 1.9 bps)
- 2026-09-23 14:23Z sell DOGE 1,415 @ 0.0938014 fee 1.42 slip 1.32 (half spread 7.3 bps)
- 2026-09-23 14:23Z sell LTC 1,466 @ 60.04 fee 1.47 slip 0.73 (half spread 1.7 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 901 candles, 2026-08-17 03:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 901 candles, 2026-08-17 03:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 901 candles, 2026-08-17 03:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 901 candles, 2026-08-17 03:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- AVAX: live 901 candles, 2026-08-17 03:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 901 candles, 2026-08-17 03:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 873 candles, 2026-08-18 07:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 873 candles, 2026-08-18 07:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.0 bps
- DOT: live 873 candles, 2026-08-18 07:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 873 candles, 2026-08-18 07:00Z to 2026-09-23 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
