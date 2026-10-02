# quantloop summary — generated 2026-10-02 02:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 15.9 of 60, 44.1 days until the verdict
  so far: champion +10.42% (DD -12.10%, 135 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.75% (usual 0.54, this window 0.70) vs challenger1 -6.07% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.4 over 16 days
  market over the window: BTC +11.83%, equal weight basket of 10 pairs +24.48%, basket max drawdown -7%, basket realised vol 59% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 10.7 of 60, 49.3 days until the verdict
  so far: champion -3.90% (DD -12.10%, 97 fills) vs challenger2 -0.45% (DD -1.17%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.97% (usual 0.54, this window 0.71) vs challenger2 -1.55% (usual 0.29, this window 0.10); the rule compares on skill, daily edge t +0.5 over 11 days
  market over the window: BTC +1.36%, equal weight basket of 10 pairs +3.84%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 7.0 of 60, 53.0 days until the verdict
  so far: champion -6.95% (DD -12.10%, 77 fills) vs challenger3 -2.48% (DD -4.74%, 104 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.76% (usual 0.55, this window 0.68) vs challenger3 -2.56% (usual 0.05, this window 0.56); the rule compares on skill, daily edge t +1.0 over 7 days
  market over the window: BTC +0.80%, equal weight basket of 10 pairs +1.49%, basket max drawdown -5%, basket realised vol 57% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 6.2 of 60, 53.8 days until the verdict
  so far: champion -9.68% (DD -12.10%, 69 fills) vs challenger4 -1.06% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.71% (usual 0.55, this window 0.64) vs challenger4 -0.22% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.7 over 7 days
  market over the window: BTC +0.97%, equal weight basket of 10 pairs -1.76%, basket max drawdown -5%, basket realised vol 57% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,042.28 (started 10,000 at 2026-09-16 03:55Z), net +10.42% since start
- 24h -1.78%, 7d -6.95%, 30d +10.42%, max drawdown -12.10%
- fills 135 total, 77 in the last 7d
- costs 325.13 (fees 214.78 + slippage 110.35); gross pnl 1,367.41; cost coverage 4.21
- cash -0.00; positions: ADA 7446.71, AVAX 167.946, BTC 0.0217956, DOGE 19500, ETH 0.684107, XRP 1224.29
- last run 2026-10-02 02:22Z; halted today: False

last decisions (newest last):

- 2026-10-02 01:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.66% not above entry band +1.0%
- 2026-10-02 01:24Z ADA hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.18% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 01:24Z AVAX hold target 0.17 (held 0.17) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +2.51% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 01:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.39% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 01:24Z XRP hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.46% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-02 01:24Z DOGE hold target 0.17 (held 0.17) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.41% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 01:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.86% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 01:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.57% not above entry band +1.0%
- 2026-10-02 02:22Z BTC hold target 0.12 (held 0.17) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +2.23% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-02 02:22Z ETH hold target 0.12 (held 0.17) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +1.90% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-02 02:22Z SOL none target 0.12 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-02 02:22Z ADA hold target 0.12 (held 0.17) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +1.67% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 02:22Z AVAX hold target 0.12 (held 0.17) — hold: weight change -0.042 below threshold 0.05 | stay long: 72h return +3.61% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 02:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.16% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 02:22Z XRP hold target 0.12 (held 0.17) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +1.33% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-02 02:22Z DOGE hold target 0.12 (held 0.17) — hold: weight change -0.041 below threshold 0.05 | stay long: 72h return +1.28% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 02:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-02 02:22Z LTC none target 0.12 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 14 fills (7 buy / 7 sell), traded 23,348, gross pnl +50.30, +43 bps per round trip, avg half spread 2.2 bps, open 7446.71
- AVAX: 20 fills (9 buy / 11 sell), traded 36,514, gross pnl +550.86, +302 bps per round trip, avg half spread 1.3 bps, open 167.946
- BTC: 7 fills (4 buy / 3 sell), traded 9,176, gross pnl +93.36, +203 bps per round trip, avg half spread 0.3 bps, open 0.0217956
- DOGE: 14 fills (8 buy / 6 sell), traded 20,397, gross pnl -57.63, -57 bps per round trip, avg half spread 1.3 bps, open 19500
- DOT: 15 fills (8 buy / 7 sell), traded 17,668, gross pnl +189.99, +215 bps per round trip, avg half spread 3.0 bps
- ETH: 11 fills (5 buy / 6 sell), traded 17,792, gross pnl +36.28, +41 bps per round trip, avg half spread 0.1 bps, open 0.684107
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 12 fills (6 buy / 6 sell), traded 19,252, gross pnl +142.02, +148 bps per round trip, avg half spread 0.6 bps, open 1224.29

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
- last run 2026-10-02 02:22Z; halted today: False

last decisions (newest last):

- 2026-10-02 01:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.07 not below -2.0
- 2026-10-02 01:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.49 not below -2.0
- 2026-10-02 01:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0
- 2026-10-02 01:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.50 not below -2.0
- 2026-10-02 01:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.81 not below -2.0
- 2026-10-02 01:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.79 not below -2.0
- 2026-10-02 01:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.38 not below -2.0
- 2026-10-02 01:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.27 not below -2.0
- 2026-10-02 02:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.65 not below -2.0
- 2026-10-02 02:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-10-02 02:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.32 not below -2.0
- 2026-10-02 02:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-10-02 02:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.33 not below -2.0
- 2026-10-02 02:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.52 not below -2.0
- 2026-10-02 02:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.76 not below -2.0
- 2026-10-02 02:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.86 not below -2.0
- 2026-10-02 02:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-10-02 02:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.18 not below -2.0

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

- equity 10,916.11 (started 10,000 at 2026-09-16 23:20Z), net +9.16% since start
- 24h +0.63%, 7d -0.45%, 30d +9.16%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,003.29; cost coverage 11.51
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-02 02:22Z; halted today: False

last decisions (newest last):

- 2026-10-02 01:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 01:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 8.488e+04 still above 72h low 8.294e+04; realised vol 30% -> weight 0.25
- 2026-10-02 02:22Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 2715 still above 72h low 2657; realised vol 36% -> weight 0.25
- 2026-10-02 02:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 02:22Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -26.13, -64 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -36.89, -91 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,226.91 (started 10,000 at 2026-09-16 23:20Z), net +12.27% since start
- 24h -0.32%, 7d -2.48%, 30d +12.27%, max drawdown -9.51%
- fills 153 total, 104 in the last 7d
- costs 344.71 (fees 226.71 + slippage 118.01); gross pnl 1,571.62; cost coverage 4.56
- cash -0.00; positions: ADA 11257.7, DOGE 23682.3, ETH 0.832737, LINK 117.602, LTC 33.1394
- last run 2026-10-02 02:22Z; halted today: False

last decisions (newest last):

- 2026-10-02 01:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 118.9 not above reaction high 119.5
- 2026-10-02 01:24Z ADA hold target 0.20 (held 0.25) — hold: weight change -0.047 below threshold 0.05 | stay long: price 0.2462 still above the 48h low 0.2425; realised vol 86% -> weight 0.25
- 2026-10-02 01:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.95 not above reaction high 11.55
- 2026-10-02 01:24Z LINK none target 0.20 (held 0.15) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-02 01:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.494 not above reaction high 1.638
- 2026-10-02 01:24Z DOGE hold target 0.20 (held 0.20) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.09401 still above the 48h low 0.09297; realised vol 62% -> weight 0.25
- 2026-10-02 01:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.177 not above reaction high 1.218
- 2026-10-02 01:24Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.004 below threshold 0.05 | stay long: price 69.05 still above the 48h low 66.15; realised vol 62% -> weight 0.25
- 2026-10-02 02:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-02 02:22Z ETH hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: price 2715 still above the 48h low 2661; realised vol 36% -> weight 0.25
- 2026-10-02 02:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 119.5 not above reaction high 119.5
- 2026-10-02 02:22Z ADA hold target 0.20 (held 0.25) — hold: weight change -0.048 below threshold 0.05 | stay long: price 0.2464 still above the 48h low 0.2425; realised vol 86% -> weight 0.25
- 2026-10-02 02:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.91 not above reaction high 11.55
- 2026-10-02 02:22Z LINK hold target 0.20 (held 0.15) — hold: weight change +0.049 below threshold 0.05 | stay long: price 14.28 still above the 48h low 14.18; realised vol 98% -> weight 0.25
- 2026-10-02 02:22Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.496 not above reaction high 1.638
- 2026-10-02 02:22Z DOGE hold target 0.20 (held 0.20) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.09383 still above the 48h low 0.09297; realised vol 62% -> weight 0.25
- 2026-10-02 02:22Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.18 not above reaction high 1.218
- 2026-10-02 02:22Z LTC hold target 0.20 (held 0.20) — hold: weight change -0.003 below threshold 0.05 | stay long: price 68.74 still above the 48h low 66.15; realised vol 62% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 22 fills (11 buy / 11 sell), traded 42,616, gross pnl +74.20, +35 bps per round trip, avg half spread 2.2 bps, open 11257.7
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 9 fills (6 buy / 3 sell), traded 9,216, gross pnl -54.91, -119 bps per round trip, avg half spread 1.7 bps, open 23682.3
- DOT: 20 fills (9 buy / 11 sell), traded 32,554, gross pnl +58.88, +36 bps per round trip, avg half spread 2.8 bps
- ETH: 7 fills (4 buy / 3 sell), traded 8,825, gross pnl +100.12, +227 bps per round trip, avg half spread 0.1 bps, open 0.832737
- LINK: 19 fills (9 buy / 10 sell), traded 30,334, gross pnl +252.30, +166 bps per round trip, avg half spread 2.7 bps, open 117.602
- LTC: 34 fills (18 buy / 16 sell), traded 43,238, gross pnl +141.96, +66 bps per round trip, avg half spread 1.9 bps, open 33.1394
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

- equity 10,145.26 (started 10,000 at 2026-09-25 04:23Z), net +1.45% since start
- 24h +0.47%, 7d +1.53%, 30d +1.53%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 186.83; cost coverage 4.49
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-02 02:22Z; halted today: False

last decisions (newest last):

- 2026-10-02 01:24Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +19.32% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 01:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +25.43% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 01:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +52.42% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 01:24Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +27.80% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 01:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +11.45% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 01:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +15.89% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 01:24Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +35.90% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 01:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +40.55% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 02:22Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +10.28% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 02:22Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +13.19% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 02:22Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +20.60% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 02:22Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +26.68% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 02:22Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +53.04% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 02:22Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +28.57% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 02:22Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +12.13% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 02:22Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +16.37% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 02:22Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +36.32% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 02:22Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +40.29% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +39.10, +195 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +35.99, +793 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +11.47, +221 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -49.83, -967 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +6.47, +42 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +9.10, +175 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +139.58, +688 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -23.14, -116 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -1.69, -14 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +19.78, +65 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1103 candles, 2026-08-17 03:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1103 candles, 2026-08-17 03:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1103 candles, 2026-08-17 03:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1103 candles, 2026-08-17 03:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1103 candles, 2026-08-17 03:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1103 candles, 2026-08-17 03:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1075 candles, 2026-08-18 07:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1075 candles, 2026-08-18 07:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 1075 candles, 2026-08-18 07:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1075 candles, 2026-08-18 07:00Z to 2026-10-02 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
