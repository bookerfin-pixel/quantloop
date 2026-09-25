# quantloop summary — generated 2026-09-25 01:20Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 8.8 of 60, 51.2 days until the verdict
  so far: champion +19.95% (DD -6.75%, 58 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +11.41%, equal weight basket of 10 pairs +23.34%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 3.7 of 60, 56.3 days until the verdict
  so far: champion +4.39% (DD -6.75%, 20 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  market over the window: BTC +0.98%, equal weight basket of 10 pairs +3.09%, basket max drawdown -7%, basket realised vol 66% annualised
- challenger3: testing H3 since 2026-09-21 22:21Z, day 3.1 of 60, 56.9 days until the verdict
  so far: champion -0.66% (DD -6.75%, 20 fills) vs challenger3 -4.66% (DD -6.43%, 11 fills)
  market over the window: BTC -2.16%, equal weight basket of 10 pairs -0.79%, basket max drawdown -7%, basket realised vol 68% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,994.63 (started 10,000 at 2026-09-16 03:55Z), net +19.95% since start
- 24h +4.36%, 7d +17.49%, 30d +19.95%, max drawdown -6.75%
- fills 58 total, 54 in the last 7d
- costs 135.29 (fees 89.33 + slippage 45.97); gross pnl 2,129.92; cost coverage 15.74
- cash -0.00; positions: ADA 12057.6, LINK 224.243, LTC 46.0622, XRP 1711.2
- last run 2026-09-25 01:20Z; halted today: False

last decisions (newest last):

- 2026-09-25 00:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-25 00:30Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +0.91% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-09-25 00:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.13% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 00:30Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.25% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 00:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.14% not above entry band +1.0%
- 2026-09-25 00:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.14% not above entry band +1.0%
- 2026-09-25 00:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.34% not above entry band +1.0%
- 2026-09-25 00:30Z LTC hold target 0.25 (held 0.27) — hold: weight change -0.025 below threshold 0.05 | stay long: 72h return +15.94% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-25 01:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.53% not above entry band +1.0%
- 2026-09-25 01:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.33% not above entry band +1.0%
- 2026-09-25 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.76% not above entry band +1.0%
- 2026-09-25 01:20Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +2.04% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-09-25 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.18% not above entry band +1.0% and price below 24h EMA
- 2026-09-25 01:20Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.35% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-25 01:20Z XRP buy target 0.25 (held 0.00) — enter long: 72h return +1.54% vs entry band +1.0% and price above 24h EMA; realised vol 80% -> weight 0.25
- 2026-09-25 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.91% not above entry band +1.0%
- 2026-09-25 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.27% not above entry band +1.0%
- 2026-09-25 01:20Z LTC hold target 0.25 (held 0.28) — hold: weight change -0.025 below threshold 0.05 | stay long: 72h return +15.84% vs exit band -1.0% and price above 24h EMA; realised vol ...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 6 fills (3 buy / 3 sell), traded 10,800, gross pnl +138.62, +257 bps per round trip, avg half spread 2.5 bps, open 12057.6
- AVAX: 8 fills (3 buy / 5 sell), traded 13,938, gross pnl +760.09, +1091 bps per round trip, avg half spread 1.3 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 8 fills (5 buy / 3 sell), traded 11,507, gross pnl +29.68, +52 bps per round trip, avg half spread 2.1 bps
- DOT: 6 fills (3 buy / 3 sell), traded 5,821, gross pnl +205.16, +705 bps per round trip, avg half spread 3.5 bps
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 5 fills (3 buy / 2 sell), traded 8,767, gross pnl +79.04, +180 bps per round trip, avg half spread 2.4 bps, open 224.243
- LTC: 6 fills (3 buy / 3 sell), traded 10,389, gross pnl +613.32, +1181 bps per round trip, avg half spread 2.3 bps, open 46.0622
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 7 fills (4 buy / 3 sell), traded 11,935, gross pnl +116.42, +195 bps per round trip, avg half spread 0.8 bps, open 1711.2

last fills:

- 2026-09-24 00:29Z buy LTC 2,866 @ 62.2261 fee 2.87 slip 1.43 (half spread 2.4 bps)
- 2026-09-24 14:23Z buy DOGE 2,997 @ 0.0950776 fee 3.00 slip 1.50 (half spread 1.5 bps)
- 2026-09-24 16:24Z buy ADA 3,017 @ 0.250202 fee 3.02 slip 1.51 (half spread 2.6 bps)
- 2026-09-24 16:24Z buy XRP 2,573 @ 1.52658 fee 2.57 slip 1.29 (half spread 1.3 bps)
- 2026-09-24 16:24Z sell DOGE 3,041 @ 0.0964721 fee 3.04 slip 1.52 (half spread 1.5 bps)
- 2026-09-24 19:20Z buy LINK 2,968 @ 13.2352 fee 2.97 slip 1.48 (half spread 0.5 bps)
- 2026-09-24 23:20Z sell XRP 2,584 @ 1.53306 fee 2.58 slip 1.29 (half spread 0.7 bps)
- 2026-09-25 01:20Z buy XRP 2,646 @ 1.54644 fee 2.65 slip 1.32 (half spread 0.8 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.16%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 1 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-25 01:20Z; halted today: False

last decisions (newest last):

- 2026-09-25 00:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.05 not below -2.0
- 2026-09-25 00:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.17 not below -2.0
- 2026-09-25 00:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.58 not below -2.0
- 2026-09-25 00:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.45 not below -2.0
- 2026-09-25 00:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.15 not below -2.0
- 2026-09-25 00:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.97 not below -2.0
- 2026-09-25 00:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.72 not below -2.0
- 2026-09-25 00:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.56 not below -2.0
- 2026-09-25 01:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.93 not below -2.0
- 2026-09-25 01:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.77 not below -2.0
- 2026-09-25 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.10 not below -2.0
- 2026-09-25 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.27 not below -2.0
- 2026-09-25 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.57 not below -2.0
- 2026-09-25 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.48 not below -2.0
- 2026-09-25 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.24 not below -2.0
- 2026-09-25 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.07 not below -2.0
- 2026-09-25 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-09-25 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.38 not below -2.0

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
- 24h +0.00%, 7d +7.41%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 28 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-25 01:20Z; halted today: False

last decisions (newest last):

- 2026-09-25 00:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 00:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-25 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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
- 24h +0.00%, 7d +12.76%, 30d +15.12%, max drawdown -6.43%
- fills 49 total, 45 in the last 7d
- costs 101.31 (fees 66.66 + slippage 34.64); gross pnl 1,613.66; cost coverage 15.93
- cash 11,512.35; positions: none
- last run 2026-09-25 01:20Z; halted today: False

last decisions (newest last):

- 2026-09-25 00:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 96.43 not a higher low vs prior low 98.64 (need +10.0%)
- 2026-09-25 00:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.191 not a higher low vs prior low 0.2025 (need +10.0%)
- 2026-09-25 00:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.197 not a higher low vs prior low 7.287 (need +10.0%)
- 2026-09-25 00:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.66 not a higher low vs prior low 11.17 (need +10.0%)
- 2026-09-25 00:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.265 not a higher low vs prior low 1.329 (need +10.0%)
- 2026-09-25 00:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.08224 (need +10.0%)
- 2026-09-25 00:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.939 not a higher low vs prior low 0.8883 (need +10.0%)
- 2026-09-25 00:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.28 not a higher low vs prior low 50.79 (need +10.0%)
- 2026-09-25 01:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.542e+04 not a higher low vs prior low 7.654e+04 (need +10.0%)
- 2026-09-25 01:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2388 not a higher low vs prior low 2414 (need +10.0%)
- 2026-09-25 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 96.43 not a higher low vs prior low 98.64 (need +10.0%)
- 2026-09-25 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.191 not a higher low vs prior low 0.2025 (need +10.0%)
- 2026-09-25 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.197 not a higher low vs prior low 7.287 (need +10.0%)
- 2026-09-25 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.66 not a higher low vs prior low 11.17 (need +10.0%)
- 2026-09-25 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.265 not a higher low vs prior low 1.329 (need +10.0%)
- 2026-09-25 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07876 not a higher low vs prior low 0.08224 (need +10.0%)
- 2026-09-25 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.939 not a higher low vs prior low 0.8883 (need +10.0%)
- 2026-09-25 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 50.28 not a higher low vs prior low 51.02 (need +10.0%)

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

- BTC: live 934 candles, 2026-08-17 03:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 934 candles, 2026-08-17 03:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 934 candles, 2026-08-17 03:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 934 candles, 2026-08-17 03:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- AVAX: live 934 candles, 2026-08-17 03:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 934 candles, 2026-08-17 03:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 906 candles, 2026-08-18 07:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 906 candles, 2026-08-18 07:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.0 bps
- DOT: live 906 candles, 2026-08-18 07:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 906 candles, 2026-08-18 07:00Z to 2026-09-25 00:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
