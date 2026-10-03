# quantloop summary — generated 2026-10-03 05:32Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 17.0 of 60, 43.0 days until the verdict
  so far: champion +9.46% (DD -12.84%, 154 fills) vs challenger1 +3.54% (DD -1.00%, 9 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.09% (usual 0.54, this window 0.71) vs challenger1 -5.11% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.2 over 18 days
  market over the window: BTC +11.41%, equal weight basket of 10 pairs +23.32%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 11.9 of 60, 48.1 days until the verdict
  so far: champion -4.74% (DD -12.84%, 116 fills) vs challenger2 -0.81% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.29% (usual 0.54, this window 0.71) vs challenger2 -1.64% (usual 0.29, this window 0.13); the rule compares on skill, daily edge t +0.6 over 12 days
  market over the window: BTC +0.98%, equal weight basket of 10 pairs +2.87%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 8.1 of 60, 51.9 days until the verdict
  so far: champion -7.76% (DD -12.84%, 96 fills) vs challenger3 -4.32% (DD -6.86%, 124 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.05% (usual 0.55, this window 0.69) vs challenger3 -4.34% (usual 0.05, this window 0.60); the rule compares on skill, daily edge t +0.7 over 9 days
  market over the window: BTC +0.42%, equal weight basket of 10 pairs +0.52%, basket max drawdown -5%, basket realised vol 59% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 7.3 of 60, 52.7 days until the verdict
  so far: champion -10.46% (DD -12.84%, 88 fills) vs challenger4 -1.83% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.99% (usual 0.55, this window 0.66) vs challenger4 -0.55% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.2 over 8 days
  market over the window: BTC +0.60%, equal weight basket of 10 pairs -2.70%, basket max drawdown -5%, basket realised vol 60% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,945.76 (started 10,000 at 2026-09-16 03:55Z), net +9.46% since start
- 24h -2.70%, 7d -10.83%, 30d +9.46%, max drawdown -12.84%
- fills 154 total, 85 in the last 7d
- costs 358.14 (fees 236.70 + slippage 121.43); gross pnl 1,303.90; cost coverage 3.64
- cash 5,442.17; positions: BTC 0.0324204, LTC 39.9106
- last run 2026-10-03 05:32Z; halted today: False

last decisions (newest last):

- 2026-10-03 04:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.25% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 04:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-03 04:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.17% not above entry band +1.0%
- 2026-10-03 04:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.94% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 04:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.21% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 04:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.08% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 04:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.65% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 04:24Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +3.09% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-03 05:32Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.68% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-03 05:32Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.25% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.38% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.58% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.45% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.88% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.50% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.41% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.91% not above entry band +1.0% and price below 24h EMA
- 2026-10-03 05:32Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.73% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 16 fills (7 buy / 9 sell), traded 25,153, gross pnl +17.39, +14 bps per round trip, avg half spread 2.3 bps
- AVAX: 22 fills (9 buy / 13 sell), traded 38,374, gross pnl +570.74, +297 bps per round trip, avg half spread 1.3 bps
- BTC: 9 fills (5 buy / 4 sell), traded 11,314, gross pnl +101.26, +179 bps per round trip, avg half spread 0.3 bps, open 0.0324204
- DOGE: 16 fills (8 buy / 8 sell), traded 22,194, gross pnl -88.11, -79 bps per round trip, avg half spread 1.2 bps
- DOT: 17 fills (9 buy / 8 sell), traded 20,081, gross pnl +141.81, +141 bps per round trip, avg half spread 2.8 bps
- ETH: 13 fills (5 buy / 8 sell), traded 19,627, gross pnl +17.81, +18 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 13 fills (6 buy / 7 sell), traded 22,241, gross pnl +520.80, +468 bps per round trip, avg half spread 2.0 bps, open 39.9106
- SOL: 12 fills (7 buy / 5 sell), traded 18,186, gross pnl +13.57, +15 bps per round trip, avg half spread 0.5 bps
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-02 19:24Z sell ETH 1,209 @ 2666.3 fee 1.21 slip 0.60 (half spread 0.0 bps)
- 2026-10-02 19:24Z sell ADA 1,188 @ 0.239444 fee 1.19 slip 0.71 (half spread 4.0 bps)
- 2026-10-02 19:24Z sell DOGE 1,191 @ 0.0911551 fee 1.19 slip 0.60 (half spread 0.3 bps)
- 2026-10-02 19:24Z sell DOT 1,182 @ 1.14548 fee 1.18 slip 0.59 (half spread 1.3 bps)
- 2026-10-02 19:24Z buy BTC 1,513 @ 84189.2 fee 1.51 slip 0.76 (half spread 0.0 bps)
- 2026-10-02 19:24Z buy SOL 1,519 @ 117.994 fee 1.52 slip 0.76 (half spread 0.4 bps)
- 2026-10-02 19:24Z buy LTC 1,510 @ 68.3892 fee 1.51 slip 0.75 (half spread 2.2 bps)
- 2026-10-02 21:23Z sell SOL 2,728 @ 117.926 fee 2.73 slip 1.36 (half spread 0.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,342.53 (started 10,000 at 2026-09-16 03:55Z), net +3.43% since start
- 24h +0.51%, 7d +0.51%, 30d +3.43%, max drawdown -1.00%
- fills 9 total, 1 in the last 7d
- costs 34.29 (fees 22.86 + slippage 11.43); gross pnl 376.82; cost coverage 10.99
- cash 7,714.75; positions: DOGE 28192.3
- last run 2026-10-03 05:32Z; halted today: False

last decisions (newest last):

- 2026-10-03 04:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-10-03 04:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.24 not below -2.0
- 2026-10-03 04:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.37 not below -2.0
- 2026-10-03 04:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.05 not below -2.0
- 2026-10-03 04:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.86 not below -2.0
- 2026-10-03 04:24Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: z -0.99 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-03 04:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.83 not below -2.0
- 2026-10-03 04:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.04 not below -2.0
- 2026-10-03 05:32Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.47 not below -2.0
- 2026-10-03 05:32Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.62 not below -2.0
- 2026-10-03 05:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.07 not below -2.0
- 2026-10-03 05:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.60 not below -2.0
- 2026-10-03 05:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.26 not below -2.0
- 2026-10-03 05:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.06 not below -2.0
- 2026-10-03 05:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.99 not below -2.0
- 2026-10-03 05:32Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: z -1.17 vs 240h mean (entry -2.0, exit -0.5); vol 68% -> weight 0.25
- 2026-10-03 05:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.06 not below -2.0
- 2026-10-03 05:32Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.05 not below -2.0

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

- equity 10,876.41 (started 10,000 at 2026-09-16 23:20Z), net +8.76% since start
- 24h -0.87%, 7d -0.81%, 30d +8.76%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 963.59; cost coverage 11.05
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-03 05:32Z; halted today: False

last decisions (newest last):

- 2026-10-03 04:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 04:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 8.457e+04 still above 72h low 8.3e+04; realised vol 33% -> weight 0.25
- 2026-10-03 05:32Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 2676 still above 72h low 2661; realised vol 38% -> weight 0.25
- 2026-10-03 05:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-03 05:32Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -33.36, -82 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -69.36, -171 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,015.52 (started 10,000 at 2026-09-16 23:20Z), net +10.16% since start
- 24h -3.45%, 7d -4.32%, 30d +10.16%, max drawdown -11.53%
- fills 173 total, 124 in the last 7d
- costs 385.97 (fees 254.00 + slippage 131.97); gross pnl 1,401.49; cost coverage 3.63
- cash 2,694.66; positions: LINK 199.564, LTC 39.8619, SOL 23.1038
- last run 2026-10-03 05:32Z; halted today: False

last decisions (newest last):

- 2026-10-03 04:24Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 119.4 still above the 48h low 117.1; realised vol 58% -> weight 0.25
- 2026-10-03 04:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2475 not above reaction high 0.2599
- 2026-10-03 04:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.92 not above reaction high 11.55
- 2026-10-03 04:24Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: price 13.94 still above the 48h low 13.56; realised vol 96% -> weight 0.25
- 2026-10-03 04:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.489 not above reaction high 1.638
- 2026-10-03 04:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09329 not above reaction high 0.1039
- 2026-10-03 04:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.159 not above reaction high 1.218
- 2026-10-03 04:24Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 69.06 still above the 48h low 66.92; realised vol 65% -> weight 0.25
- 2026-10-03 05:32Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-03 05:32Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 2676 not above reaction high 2784
- 2026-10-03 05:32Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 119.2 still above the 48h low 117.1; realised vol 58% -> weight 0.25
- 2026-10-03 05:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2454 not above reaction high 0.2599
- 2026-10-03 05:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.88 not above reaction high 11.55
- 2026-10-03 05:32Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: price 13.94 still above the 48h low 13.56; realised vol 96% -> weight 0.25
- 2026-10-03 05:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.485 not above reaction high 1.638
- 2026-10-03 05:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09294 not above reaction high 0.1039
- 2026-10-03 05:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.148 not above reaction high 1.218
- 2026-10-03 05:32Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 68.83 still above the 48h low 66.92; realised vol 64% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 24 fills (11 buy / 13 sell), traded 45,344, gross pnl +23.98, +11 bps per round trip, avg half spread 2.3 bps
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 11 fills (6 buy / 5 sell), traded 11,408, gross pnl -82.80, -145 bps per round trip, avg half spread 1.5 bps
- DOT: 23 fills (11 buy / 12 sell), traded 36,196, gross pnl -57.11, -32 bps per round trip, avg half spread 2.7 bps
- ETH: 9 fills (4 buy / 5 sell), traded 11,060, gross pnl +79.28, +143 bps per round trip, avg half spread 0.1 bps
- LINK: 25 fills (12 buy / 13 sell), traded 42,245, gross pnl +269.09, +127 bps per round trip, avg half spread 2.7 bps, open 199.564
- LTC: 36 fills (19 buy / 17 sell), traded 45,054, gross pnl +175.20, +78 bps per round trip, avg half spread 1.9 bps, open 39.8619
- SOL: 17 fills (9 buy / 8 sell), traded 23,112, gross pnl +57.28, +50 bps per round trip, avg half spread 0.5 bps, open 23.1038
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

- equity 10,065.57 (started 10,000 at 2026-09-25 04:23Z), net +0.66% since start
- 24h -2.49%, 7d -1.78%, 30d +0.73%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 107.14; cost coverage 2.58
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-03 05:32Z; halted today: False

last decisions (newest last):

- 2026-10-03 04:24Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +18.82% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 04:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +20.91% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 04:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +50.10% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 04:24Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +24.63% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 04:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +9.01% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-03 04:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +12.74% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 04:24Z DOT hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +32.79% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 04:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +37.76% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 05:32Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +8.78% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-03 05:32Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +11.18% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 05:32Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +18.11% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 05:32Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +18.42% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 05:32Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +49.27% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-03 05:32Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +24.01% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 05:32Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +8.55% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-03 05:32Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +12.04% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 05:32Z DOT hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +30.66% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-03 05:32Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +36.68% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +39.23, +196 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +32.98, +727 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +8.68, +167 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -55.63, -1079 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl -24.55, -161 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -3.45, -66 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +114.05, +563 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -17.96, -90 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -1.17, -10 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +14.98, +49 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1130 candles, 2026-08-17 03:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1130 candles, 2026-08-17 03:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1130 candles, 2026-08-17 03:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1130 candles, 2026-08-17 03:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- AVAX: live 1130 candles, 2026-08-17 03:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1130 candles, 2026-08-17 03:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1102 candles, 2026-08-18 07:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1102 candles, 2026-08-18 07:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 1102 candles, 2026-08-18 07:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1102 candles, 2026-08-18 07:00Z to 2026-10-03 04:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
