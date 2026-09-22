# quantloop summary — generated 2026-09-22 18:26Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 6.5 of 60, 53.5 days until the verdict
  so far: champion +19.80% (DD -3.54%, 41 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +14.06%, equal weight basket of 10 pairs +23.87%, basket max drawdown -4%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 1.4 of 60, 58.6 days until the verdict
  so far: champion +4.26% (DD -2.71%, 3 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  market over the window: BTC +3.38%, equal weight basket of 10 pairs +3.33%, basket max drawdown -2%, basket realised vol 53% annualised
- challenger3: testing H3 since 2026-09-21 22:21Z, day 0.8 of 60, 59.2 days until the verdict
  so far: champion -0.78% (DD -2.71%, 3 fills) vs challenger3 -0.39% (DD -2.68%, 0 fills)
  market over the window: BTC +0.17%, equal weight basket of 10 pairs -0.54%, basket max drawdown -2%, basket realised vol 55% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,979.96 (started 10,000 at 2026-09-16 03:55Z), net +19.80% since start
- 24h +0.69%, 7d +19.80%, 30d +19.80%, max drawdown -3.54%
- fills 41 total, 41 in the last 7d
- costs 83.43 (fees 55.16 + slippage 28.28); gross pnl 2,063.39; cost coverage 24.73
- cash -0.00; positions: ADA 6238.97, BTC 0.0174035, DOGE 13174.9, DOT 262.916, ETH 0.539165, LINK 114.186, LTC 24.4122, SOL 10.3233, XRP 1008.59
- last run 2026-09-22 18:26Z; halted today: False

last decisions (newest last):

- 2026-09-22 17:21Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +4.91% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-22 17:21Z ADA hold target 0.10 (held 0.13) — hold: weight change -0.029 below threshold 0.05 | stay long: 72h return +8.54% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-22 17:21Z AVAX none target 0.09 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +14.28% vs entry band +1.0% and price above 24h EMA; realised vol 127%...
- 2026-09-22 17:21Z LINK hold target 0.10 (held 0.12) — hold: weight change -0.024 below threshold 0.05 | stay long: 72h return +3.34% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-22 17:21Z XRP hold target 0.10 (held 0.13) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +9.08% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-22 17:21Z DOGE hold target 0.10 (held 0.11) — hold: weight change -0.009 below threshold 0.05 | stay long: 72h return +11.00% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-22 17:21Z DOT none target 0.10 (held 0.03) — no fill possible (no cash or no position) | stay long: 72h return +3.56% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vo...
- 2026-09-22 17:21Z LTC hold target 0.10 (held 0.13) — hold: weight change -0.026 below threshold 0.05 | stay long: 72h return +6.94% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-22 18:26Z BTC hold target 0.10 (held 0.13) — hold: weight change -0.025 below threshold 0.05 | stay long: 72h return +6.31% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-09-22 18:26Z ETH hold target 0.10 (held 0.12) — hold: weight change -0.023 below threshold 0.05 | stay long: 72h return +4.13% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-09-22 18:26Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +5.93% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-22 18:26Z ADA hold target 0.10 (held 0.13) — hold: weight change -0.030 below threshold 0.05 | stay long: 72h return +8.80% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-22 18:26Z AVAX none target 0.10 (held 0.00) — no fill possible (no cash or no position) | enter long: 72h return +14.49% vs entry band +1.0% and price above 24h EMA; realised vol 127%...
- 2026-09-22 18:26Z LINK hold target 0.10 (held 0.12) — hold: weight change -0.023 below threshold 0.05 | stay long: 72h return +3.77% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-22 18:26Z XRP hold target 0.10 (held 0.13) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return +10.15% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-22 18:26Z DOGE hold target 0.10 (held 0.11) — hold: weight change -0.009 below threshold 0.05 | stay long: 72h return +11.00% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-22 18:26Z DOT none target 0.10 (held 0.03) — no fill possible (no cash or no position) | stay long: 72h return +4.48% vs exit band -1.0% and price above 24h EMA; realised vol 102% ->...
- 2026-09-22 18:26Z LTC hold target 0.10 (held 0.13) — hold: weight change -0.026 below threshold 0.05 | stay long: 72h return +7.47% vs exit band -1.0% and price above 24h EMA; realised vol 6...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 6,302, gross pnl +198.06, +629 bps per round trip, avg half spread 2.3 bps, open 6238.97
- AVAX: 8 fills (3 buy / 5 sell), traded 13,938, gross pnl +760.09, +1091 bps per round trip, avg half spread 1.3 bps
- BTC: 3 fills (2 buy / 1 sell), traded 3,989, gross pnl +99.17, +497 bps per round trip, avg half spread 0.0 bps, open 0.0174035
- DOGE: 5 fills (4 buy / 1 sell), traded 4,233, gross pnl +58.16, +275 bps per round trip, avg half spread 1.3 bps, open 13174.9
- DOT: 5 fills (3 buy / 2 sell), traded 5,517, gross pnl +212.02, +769 bps per round trip, avg half spread 3.8 bps, open 262.916
- ETH: 3 fills (2 buy / 1 sell), traded 3,991, gross pnl +100.55, +504 bps per round trip, avg half spread 0.0 bps, open 0.539165
- LINK: 3 fills (2 buy / 1 sell), traded 4,401, gross pnl +120.57, +548 bps per round trip, avg half spread 2.6 bps, open 114.186
- LTC: 4 fills (2 buy / 2 sell), traded 6,057, gross pnl +230.30, +760 bps per round trip, avg half spread 2.5 bps, open 24.4122
- SOL: 3 fills (2 buy / 1 sell), traded 4,128, gross pnl +126.17, +611 bps per round trip, avg half spread 0.5 bps, open 10.3233
- XRP: 3 fills (2 buy / 1 sell), traded 2,600, gross pnl +158.29, +1218 bps per round trip, avg half spread 0.3 bps, open 1008.59

last fills:

- 2026-09-20 16:21Z buy XRP 1,411 @ 1.3988 fee 1.41 slip 0.71 (half spread 0.4 bps)
- 2026-09-20 16:21Z buy DOT 102 @ 1.12492 fee 0.10 slip 0.08 (half spread 5.8 bps)
- 2026-09-20 16:21Z sell LTC 1,300 @ 57.7361 fee 1.30 slip 0.65 (half spread 0.9 bps)
- 2026-09-20 17:19Z buy SOL 1,135 @ 109.91 fee 1.13 slip 0.57 (half spread 0.5 bps)
- 2026-09-20 17:19Z buy DOGE 163 @ 0.0871166 fee 0.16 slip 0.08 (half spread 2.0 bps)
- 2026-09-22 05:21Z sell AVAX 1,325 @ 10.5812 fee 1.32 slip 0.66 (half spread 1.4 bps)
- 2026-09-22 05:21Z buy DOGE 1,121 @ 0.0991152 fee 1.12 slip 0.56 (half spread 0.9 bps)
- 2026-09-22 05:21Z buy DOT 201 @ 1.17023 fee 0.20 slip 0.10 (half spread 3.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-22 18:26Z; halted today: False

last decisions (newest last):

- 2026-09-22 17:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.73 not below -2.0
- 2026-09-22 17:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.07 not below -2.0
- 2026-09-22 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.64 not below -2.0
- 2026-09-22 17:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.70 not below -2.0
- 2026-09-22 17:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.44 not below -2.0
- 2026-09-22 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.42 not below -2.0
- 2026-09-22 17:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.38 not below -2.0
- 2026-09-22 17:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.96 not below -2.0
- 2026-09-22 18:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.21 not below -2.0
- 2026-09-22 18:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.84 not below -2.0
- 2026-09-22 18:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.78 not below -2.0
- 2026-09-22 18:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.07 not below -2.0
- 2026-09-22 18:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.61 not below -2.0
- 2026-09-22 18:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.66 not below -2.0
- 2026-09-22 18:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.50 not below -2.0
- 2026-09-22 18:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.41 not below -2.0
- 2026-09-22 18:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.44 not below -2.0
- 2026-09-22 18:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.92 not below -2.0

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
- last run 2026-09-22 18:26Z; halted today: False

last decisions (newest last):

- 2026-09-22 17:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 17:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-22 18:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 12,027.59 (started 10,000 at 2026-09-16 23:20Z), net +20.28% since start
- 24h +1.09%, 7d +20.28%, 30d +20.28%, max drawdown -3.54%
- fills 38 total, 38 in the last 7d
- costs 79.46 (fees 52.51 + slippage 26.95); gross pnl 2,107.05; cost coverage 26.52
- cash 0.00; positions: ADA 6238.97, AVAX 125.195, BTC 0.0174035, DOGE 1865.62, DOT 91.027, ETH 0.539165, LINK 114.186, LTC 24.4122, SOL 10.3233, XRP 1008.59
- last run 2026-09-22 18:26Z; halted today: False

last decisions (newest last):

- 2026-09-22 17:21Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: price 117.5 still above the 48h low 109.4; realised vol 60% -> weight 0.25
- 2026-09-22 17:21Z ADA hold target 0.10 (held 0.13) — hold: weight change -0.029 below threshold 0.05 | stay long: price 0.2493 still above the 48h low 0.2265; realised vol 86% -> weight 0.25
- 2026-09-22 17:21Z AVAX hold target 0.09 (held 0.12) — hold: weight change -0.020 below threshold 0.05 | stay long: price 11.07 still above the 48h low 10.7; realised vol 127% -> weight 0.24
- 2026-09-22 17:21Z LINK hold target 0.10 (held 0.12) — hold: weight change -0.023 below threshold 0.05 | stay long: price 13.02 still above the 48h low 12.42; realised vol 67% -> weight 0.25
- 2026-09-22 17:21Z XRP hold target 0.10 (held 0.13) — hold: weight change -0.031 below threshold 0.05 | stay long: price 1.564 still above the 48h low 1.402; realised vol 85% -> weight 0.25
- 2026-09-22 17:21Z DOGE none target 0.10 (held 0.02) — no fill possible (no cash or no position) | stay long: price 0.09949 still above the 48h low 0.08663; realised vol 75% -> weight 0.25
- 2026-09-22 17:21Z DOT none target 0.10 (held 0.01) — no fill possible (no cash or no position) | stay long: price 1.174 still above the 48h low 1.131; realised vol 102% -> weight 0.25
- 2026-09-22 17:21Z LTC hold target 0.10 (held 0.13) — hold: weight change -0.025 below threshold 0.05 | stay long: price 61.95 still above the 48h low 58.28; realised vol 69% -> weight 0.25
- 2026-09-22 18:26Z BTC hold target 0.10 (held 0.12) — hold: weight change -0.024 below threshold 0.05 | stay long: price 8.657e+04 still above the 48h low 8.093e+04; realised vol 39% -> weigh...
- 2026-09-22 18:26Z ETH hold target 0.10 (held 0.12) — hold: weight change -0.023 below threshold 0.05 | stay long: price 2754 still above the 48h low 2626; realised vol 44% -> weight 0.25
- 2026-09-22 18:26Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: price 118 still above the 48h low 109.4; realised vol 60% -> weight 0.25
- 2026-09-22 18:26Z ADA hold target 0.10 (held 0.13) — hold: weight change -0.029 below threshold 0.05 | stay long: price 0.2498 still above the 48h low 0.2265; realised vol 85% -> weight 0.25
- 2026-09-22 18:26Z AVAX hold target 0.10 (held 0.11) — hold: weight change -0.020 below threshold 0.05 | stay long: price 11.05 still above the 48h low 10.7; realised vol 127% -> weight 0.24
- 2026-09-22 18:26Z LINK hold target 0.10 (held 0.12) — hold: weight change -0.023 below threshold 0.05 | stay long: price 13.01 still above the 48h low 12.42; realised vol 67% -> weight 0.25
- 2026-09-22 18:26Z XRP hold target 0.10 (held 0.13) — hold: weight change -0.031 below threshold 0.05 | stay long: price 1.572 still above the 48h low 1.402; realised vol 85% -> weight 0.25
- 2026-09-22 18:26Z DOGE none target 0.10 (held 0.02) — no fill possible (no cash or no position) | stay long: price 0.0997 still above the 48h low 0.08663; realised vol 74% -> weight 0.25
- 2026-09-22 18:26Z DOT none target 0.10 (held 0.01) — no fill possible (no cash or no position) | stay long: price 1.18 still above the 48h low 1.131; realised vol 102% -> weight 0.25
- 2026-09-22 18:26Z LTC hold target 0.10 (held 0.13) — hold: weight change -0.026 below threshold 0.05 | stay long: price 61.9 still above the 48h low 58.28; realised vol 69% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 6,302, gross pnl +198.06, +629 bps per round trip, avg half spread 2.3 bps, open 6238.97
- AVAX: 7 fills (3 buy / 4 sell), traded 12,613, gross pnl +811.99, +1288 bps per round trip, avg half spread 1.3 bps, open 125.195
- BTC: 3 fills (2 buy / 1 sell), traded 3,989, gross pnl +99.17, +497 bps per round trip, avg half spread 0.0 bps, open 0.0174035
- DOGE: 4 fills (3 buy / 1 sell), traded 3,112, gross pnl +51.93, +334 bps per round trip, avg half spread 1.4 bps, open 1865.62
- DOT: 4 fills (2 buy / 2 sell), traded 5,316, gross pnl +210.01, +790 bps per round trip, avg half spread 4.0 bps, open 91.027
- ETH: 3 fills (2 buy / 1 sell), traded 3,991, gross pnl +100.55, +504 bps per round trip, avg half spread 0.0 bps, open 0.539165
- LINK: 3 fills (2 buy / 1 sell), traded 4,401, gross pnl +120.57, +548 bps per round trip, avg half spread 2.6 bps, open 114.186
- LTC: 4 fills (2 buy / 2 sell), traded 6,057, gross pnl +230.30, +760 bps per round trip, avg half spread 2.5 bps, open 24.4122
- SOL: 3 fills (2 buy / 1 sell), traded 4,128, gross pnl +126.17, +611 bps per round trip, avg half spread 0.5 bps, open 10.3233
- XRP: 3 fills (2 buy / 1 sell), traded 2,600, gross pnl +158.29, +1218 bps per round trip, avg half spread 0.3 bps, open 1008.59

last fills:

- 2026-09-20 16:21Z buy ADA 1,411 @ 0.22613 fee 1.41 slip 0.72 (half spread 3.1 bps)
- 2026-09-20 16:21Z sell AVAX 1,737 @ 11.2564 fee 1.74 slip 0.87 (half spread 1.8 bps)
- 2026-09-20 16:21Z buy LINK 1,411 @ 12.3554 fee 1.41 slip 0.71 (half spread 2.4 bps)
- 2026-09-20 16:21Z buy XRP 1,411 @ 1.3988 fee 1.41 slip 0.71 (half spread 0.4 bps)
- 2026-09-20 16:21Z buy DOT 102 @ 1.12492 fee 0.10 slip 0.08 (half spread 5.8 bps)
- 2026-09-20 16:21Z sell LTC 1,300 @ 57.7361 fee 1.30 slip 0.65 (half spread 0.9 bps)
- 2026-09-20 17:19Z buy SOL 1,135 @ 109.91 fee 1.13 slip 0.57 (half spread 0.5 bps)
- 2026-09-20 17:19Z buy DOGE 163 @ 0.0871166 fee 0.16 slip 0.08 (half spread 2.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 879 candles, 2026-08-17 03:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 879 candles, 2026-08-17 03:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 879 candles, 2026-08-17 03:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 879 candles, 2026-08-17 03:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.4 bps
- AVAX: live 879 candles, 2026-08-17 03:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.4 bps
- LINK: live 879 candles, 2026-08-17 03:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 851 candles, 2026-08-18 07:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 851 candles, 2026-08-18 07:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.9 bps
- DOT: live 851 candles, 2026-08-18 07:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 851 candles, 2026-08-18 07:00Z to 2026-09-22 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
