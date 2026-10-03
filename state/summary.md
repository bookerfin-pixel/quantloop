# quantloop summary — generated 2026-10-03 19:02Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 17.6 of 60, 42.4 days until the verdict
  so far: champion +9.32% (DD -12.84%, 158 fills) vs challenger1 +3.50% (DD -1.00%, 9 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.80% (usual 0.54, this window 0.71) vs challenger1 -5.54% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.2 over 18 days
  market over the window: BTC +11.89%, equal weight basket of 10 pairs +24.38%, basket max drawdown -7%, basket realised vol 59% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 12.4 of 60, 47.6 days until the verdict
  so far: champion -4.86% (DD -12.84%, 120 fills) vs challenger2 -0.68% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.86% (usual 0.54, this window 0.71) vs challenger2 -1.74% (usual 0.29, this window 0.14); the rule compares on skill, daily edge t +0.6 over 13 days
  market over the window: BTC +1.41%, equal weight basket of 10 pairs +3.70%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 8.7 of 60, 51.3 days until the verdict
  so far: champion -7.88% (DD -12.84%, 100 fills) vs challenger3 -4.61% (DD -6.86%, 124 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.63% (usual 0.55, this window 0.69) vs challenger3 -4.69% (usual 0.05, this window 0.61); the rule compares on skill, daily edge t +0.7 over 9 days
  market over the window: BTC +0.86%, equal weight basket of 10 pairs +1.38%, basket max drawdown -5%, basket realised vol 57% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 7.9 of 60, 52.1 days until the verdict
  so far: champion -10.58% (DD -12.84%, 92 fills) vs challenger4 -1.54% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.55% (usual 0.55, this window 0.66) vs challenger4 -0.64% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.3 over 8 days
  market over the window: BTC +1.03%, equal weight basket of 10 pairs -1.88%, basket max drawdown -5%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,931.68 (started 10,000 at 2026-09-16 03:55Z), net +9.32% since start
- 24h +0.28%, 7d -11.25%, 30d +9.32%, max drawdown -12.84%
- fills 158 total, 81 in the last 7d
- costs 374.50 (fees 247.61 + slippage 126.89); gross pnl 1,306.18; cost coverage 3.49
- cash -0.00; positions: AVAX 243.024, BTC 0.0324204, LTC 39.9106, SOL 22.8189
- last run 2026-10-03 19:02Z; halted today: False

last decisions (newest last):

- 2026-10-03 14:32Z SOL sell target 0.00 (held 0.25) — exit: 72h return -1.29% fell below exit band -1.0%
- 2026-10-03 14:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.54% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 14:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.39% not above entry band +1.0%
- 2026-10-03 14:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.61% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 14:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.14% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 14:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.33% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 14:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.77% not above entry band +1.0%
- 2026-10-03 14:32Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +3.55% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-03 19:02Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.21% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-03 19:02Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.25% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 19:02Z SOL buy target 0.25 (held 0.00) — enter long: 72h return +1.09% vs entry band +1.0% and price above 24h EMA; realised vol 58% -> weight 0.25
- 2026-10-03 19:02Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.47% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 19:02Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +1.51% vs entry band +1.0% and price above 24h EMA; realised vol 94% -> weight 0.25
- 2026-10-03 19:02Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.00% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 19:02Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.34% not above entry band +1.0%
- 2026-10-03 19:02Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.02% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 19:02Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.56% not above entry band +1.0%
- 2026-10-03 19:02Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +4.28% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 16 fills (7 buy / 9 sell), traded 25,153, gross pnl +17.39, +14 bps per round trip, avg half spread 2.3 bps
- AVAX: 23 fills (10 buy / 13 sell), traded 41,072, gross pnl +570.74, +278 bps per round trip, avg half spread 1.3 bps, open 243.024
- BTC: 9 fills (5 buy / 4 sell), traded 11,314, gross pnl +110.19, +195 bps per round trip, avg half spread 0.3 bps, open 0.0324204
- DOGE: 16 fills (8 buy / 8 sell), traded 22,194, gross pnl -88.11, -79 bps per round trip, avg half spread 1.2 bps
- DOT: 17 fills (9 buy / 8 sell), traded 20,081, gross pnl +141.81, +141 bps per round trip, avg half spread 2.8 bps
- ETH: 13 fills (5 buy / 8 sell), traded 19,627, gross pnl +17.81, +18 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 13 fills (6 buy / 7 sell), traded 22,241, gross pnl +510.02, +459 bps per round trip, avg half spread 2.0 bps, open 39.9106
- SOL: 15 fills (9 buy / 6 sell), traded 26,396, gross pnl +17.69, +13 bps per round trip, avg half spread 0.5 bps, open 22.8189
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-02 19:24Z buy BTC 1,513 @ 84189.2 fee 1.51 slip 0.76 (half spread 0.0 bps)
- 2026-10-02 19:24Z buy SOL 1,519 @ 117.994 fee 1.52 slip 0.76 (half spread 0.4 bps)
- 2026-10-02 19:24Z buy LTC 1,510 @ 68.3892 fee 1.51 slip 0.75 (half spread 2.2 bps)
- 2026-10-02 21:23Z sell SOL 2,728 @ 117.926 fee 2.73 slip 1.36 (half spread 0.4 bps)
- 2026-10-03 07:25Z buy SOL 2,736 @ 119.365 fee 2.74 slip 1.37 (half spread 0.4 bps)
- 2026-10-03 14:32Z sell SOL 2,738 @ 119.425 fee 2.74 slip 1.37 (half spread 0.4 bps)
- 2026-10-03 19:02Z buy SOL 2,735 @ 119.855 fee 2.73 slip 1.37 (half spread 0.4 bps)
- 2026-10-03 19:02Z buy AVAX 2,698 @ 11.1005 fee 2.70 slip 1.35 (half spread 0.9 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,338.52 (started 10,000 at 2026-09-16 03:55Z), net +3.39% since start
- 24h +0.51%, 7d +0.47%, 30d +3.39%, max drawdown -1.00%
- fills 9 total, 1 in the last 7d
- costs 34.29 (fees 22.86 + slippage 11.43); gross pnl 372.82; cost coverage 10.87
- cash 7,714.75; positions: DOGE 28192.3
- last run 2026-10-03 19:02Z; halted today: False

last decisions (newest last):

- 2026-10-03 14:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.14 not below -2.0
- 2026-10-03 14:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.61 not below -2.0
- 2026-10-03 14:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.98 not below -2.0
- 2026-10-03 14:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.19 not below -2.0
- 2026-10-03 14:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.94 not below -2.0
- 2026-10-03 14:32Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: z -1.16 vs 240h mean (entry -2.0, exit -0.5); vol 67% -> weight 0.25
- 2026-10-03 14:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.27 not below -2.0
- 2026-10-03 14:32Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.21 not below -2.0
- 2026-10-03 19:02Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.06 not below -2.0
- 2026-10-03 19:02Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.15 not below -2.0
- 2026-10-03 19:02Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.34 not below -2.0
- 2026-10-03 19:02Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.61 not below -2.0
- 2026-10-03 19:02Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.89 not below -2.0
- 2026-10-03 19:02Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.21 not below -2.0
- 2026-10-03 19:02Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.81 not below -2.0
- 2026-10-03 19:02Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: z -1.02 vs 240h mean (entry -2.0, exit -0.5); vol 66% -> weight 0.25
- 2026-10-03 19:02Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.00 not below -2.0
- 2026-10-03 19:02Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- DOGE: 1 fills (1 buy / 0 sell), traded 2,572, gross pnl -2,571.16, -19990 bps per round trip, avg half spread 0.3 bps, open 28192.3
- ETH: 2 fills (1 buy / 1 sell), traded 5,048, gross pnl +50.93, +202 bps per round trip, avg half spread 0.4 bps
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)
- 2026-09-17 13:23Z sell ETH 2,548 @ 2449.98 fee 2.55 slip 1.27 (half spread 0.4 bps)
- 2026-09-18 01:20Z sell ADA 2,628 @ 0.205888 fee 2.63 slip 1.31 (half spread 2.2 bps)
- 2026-09-18 03:21Z sell BTC 2,538 @ 77289.3 fee 2.54 slip 1.27 (half spread 0.0 bps)
- 2026-10-02 19:24Z buy DOGE 2,572 @ 0.0912463 fee 2.57 slip 1.29 (half spread 0.3 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,891.08 (started 10,000 at 2026-09-16 23:20Z), net +8.91% since start
- 24h +0.37%, 7d -0.68%, 30d +8.91%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 978.26; cost coverage 11.22
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-03 19:02Z; halted today: False

last decisions (newest last):

- 2026-10-03 14:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 14:32Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 8.493e+04 still above 72h low 8.338e+04; realised vol 33% -> weight 0.25
- 2026-10-03 19:02Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 2685 still above 72h low 2661; realised vol 38% -> weight 0.25
- 2026-10-03 19:02Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 19:02Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -24.53, -60 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -63.53, -157 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 10,981.26 (started 10,000 at 2026-09-16 23:20Z), net +9.81% since start
- 24h +0.88%, 7d -4.61%, 30d +9.81%, max drawdown -11.53%
- fills 173 total, 124 in the last 7d
- costs 385.97 (fees 254.00 + slippage 131.97); gross pnl 1,367.23; cost coverage 3.54
- cash 2,694.66; positions: LINK 199.564, LTC 39.8619, SOL 23.1038
- last run 2026-10-03 19:02Z; halted today: False

last decisions (newest last):

- 2026-10-03 14:32Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 119.4 still above the 48h low 117.1; realised vol 58% -> weight 0.25
- 2026-10-03 14:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.245 not above reaction high 0.2599
- 2026-10-03 14:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.14 not above reaction high 11.55
- 2026-10-03 14:32Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 13.88 still above the 48h low 13.56; realised vol 95% -> weight 0.25
- 2026-10-03 14:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.487 not above reaction high 1.638
- 2026-10-03 14:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.0929 not above reaction high 0.1039
- 2026-10-03 14:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.206 not above reaction high 1.218
- 2026-10-03 14:32Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 69.79 still above the 48h low 66.92; realised vol 63% -> weight 0.25
- 2026-10-03 19:02Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-03 19:02Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 2685 not above reaction high 2784
- 2026-10-03 19:02Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 120 still above the 48h low 117.6; realised vol 58% -> weight 0.25
- 2026-10-03 19:02Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2453 not above reaction high 0.2599
- 2026-10-03 19:02Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.12 not above reaction high 11.55
- 2026-10-03 19:02Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: price 13.91 still above the 48h low 13.56; realised vol 95% -> weight 0.25
- 2026-10-03 19:02Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.49 not above reaction high 1.638
- 2026-10-03 19:02Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09318 not above reaction high 0.1039
- 2026-10-03 19:02Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.197 not above reaction high 1.218
- 2026-10-03 19:02Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 68.98 still above the 48h low 67.82; realised vol 62% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 24 fills (11 buy / 13 sell), traded 45,344, gross pnl +23.98, +11 bps per round trip, avg half spread 2.3 bps
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 11 fills (6 buy / 5 sell), traded 11,408, gross pnl -82.80, -145 bps per round trip, avg half spread 1.5 bps
- DOT: 23 fills (11 buy / 12 sell), traded 36,196, gross pnl -57.11, -32 bps per round trip, avg half spread 2.7 bps
- ETH: 9 fills (4 buy / 5 sell), traded 11,060, gross pnl +79.28, +143 bps per round trip, avg half spread 0.1 bps
- LINK: 25 fills (12 buy / 13 sell), traded 42,245, gross pnl +241.43, +114 bps per round trip, avg half spread 2.7 bps, open 199.564
- LTC: 36 fills (19 buy / 17 sell), traded 45,054, gross pnl +164.43, +73 bps per round trip, avg half spread 1.9 bps, open 39.8619
- SOL: 17 fills (9 buy / 8 sell), traded 23,112, gross pnl +61.44, +53 bps per round trip, avg half spread 0.5 bps, open 23.1038
- XRP: 6 fills (3 buy / 3 sell), traded 6,959, gross pnl +88.07, +253 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-02 19:24Z sell LINK 1,022 @ 13.6207 fee 1.02 slip 0.65 (half spread 4.3 bps)
- 2026-10-02 19:24Z sell DOGE 1,549 @ 0.0911551 fee 1.55 slip 0.77 (half spread 0.3 bps)
- 2026-10-02 19:24Z sell DOT 1,762 @ 1.14548 fee 1.76 slip 0.88 (half spread 1.3 bps)
- 2026-10-02 19:24Z buy SOL 1,159 @ 117.994 fee 1.16 slip 0.58 (half spread 0.4 bps)
- 2026-10-02 19:24Z buy LTC 1,130 @ 68.3892 fee 1.13 slip 0.56 (half spread 2.2 bps)
- 2026-10-02 20:23Z buy LINK 2,725 @ 13.6223 fee 2.72 slip 1.36 (half spread 3.0 bps)
- 2026-10-02 21:23Z sell LINK 2,723 @ 13.611 fee 2.72 slip 1.36 (half spread 2.3 bps)
- 2026-10-02 22:23Z buy LINK 2,731 @ 13.6865 fee 2.73 slip 1.36 (half spread 1.5 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,095.57 (started 10,000 at 2026-09-25 04:23Z), net +0.96% since start
- 24h +1.95%, 7d -1.91%, 30d +1.03%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 137.14; cost coverage 3.30
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-03 19:02Z; halted today: False

last decisions (newest last):

- 2026-10-03 14:32Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +17.67% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 14:32Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +16.66% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 14:32Z AVAX hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +52.43% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 14:32Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +21.28% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 14:32Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +6.66% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-03 14:32Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +11.26% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 14:32Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +38.61% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 14:32Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +37.49% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 19:02Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +4.52% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-03 19:02Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +6.84% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-03 19:02Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +13.99% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 19:02Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +10.14% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 19:02Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +47.64% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 19:02Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +17.77% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 19:02Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +1.83% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-03 19:02Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +4.06% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-03 19:02Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +33.76% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 19:02Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +34.39% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +30.73, +153 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +47.25, +1042 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +12.09, +232 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -57.12, -1108 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +8.07, +53 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -1.20, -23 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +103.61, +511 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -21.85, -110 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +0.36, +3 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +15.19, +50 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1144 candles, 2026-08-17 03:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1144 candles, 2026-08-17 03:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1144 candles, 2026-08-17 03:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1144 candles, 2026-08-17 03:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- AVAX: live 1144 candles, 2026-08-17 03:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1144 candles, 2026-08-17 03:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 1116 candles, 2026-08-18 07:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1116 candles, 2026-08-18 07:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 1116 candles, 2026-08-18 07:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1116 candles, 2026-08-18 07:00Z to 2026-10-03 18:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
