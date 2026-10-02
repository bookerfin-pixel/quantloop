# quantloop summary — generated 2026-10-02 21:23Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 16.7 of 60, 43.3 days until the verdict
  so far: champion +9.51% (DD -12.84%, 154 fills) vs challenger1 +3.10% (DD -1.00%, 9 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.10% (usual 0.54, this window 0.71) vs challenger1 -4.91% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.3 over 17 days
  market over the window: BTC +11.24%, equal weight basket of 10 pairs +21.58%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 11.5 of 60, 48.5 days until the verdict
  so far: champion -4.70% (DD -12.84%, 116 fills) vs challenger2 -1.01% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.50% (usual 0.54, this window 0.72) vs challenger2 -1.43% (usual 0.29, this window 0.12); the rule compares on skill, daily edge t +0.5 over 12 days
  market over the window: BTC +0.83%, equal weight basket of 10 pairs +1.48%, basket max drawdown -7%, basket realised vol 62% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 7.8 of 60, 52.2 days until the verdict
  so far: champion -7.72% (DD -12.84%, 96 fills) vs challenger3 -5.14% (DD -6.86%, 123 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.25% (usual 0.55, this window 0.70) vs challenger3 -5.09% (usual 0.05, this window 0.60); the rule compares on skill, daily edge t +0.3 over 8 days
  market over the window: BTC +0.27%, equal weight basket of 10 pairs -0.86%, basket max drawdown -5%, basket realised vol 60% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 7.0 of 60, 53.0 days until the verdict
  so far: champion -10.42% (DD -12.84%, 88 fills) vs challenger4 -3.14% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.22% (usual 0.55, this window 0.67) vs challenger4 -1.22% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +1.8 over 7 days
  market over the window: BTC +0.45%, equal weight basket of 10 pairs -4.02%, basket max drawdown -5%, basket realised vol 60% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,950.69 (started 10,000 at 2026-09-16 03:55Z), net +9.51% since start
- 24h -0.78%, 7d -10.42%, 30d +9.51%, max drawdown -12.84%
- fills 154 total, 88 in the last 7d
- costs 358.14 (fees 236.70 + slippage 121.43); gross pnl 1,308.82; cost coverage 3.65
- cash 5,442.17; positions: BTC 0.0324204, LTC 39.9106
- last run 2026-10-02 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-02 20:23Z SOL hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return -0.61% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 20:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.44% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 20:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.44% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 20:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.17% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 20:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.61% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 20:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.27% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 20:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.43% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 20:23Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.10% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 21:23Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +1.02% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-02 21:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.02% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z SOL sell target 0.00 (held 0.25) — exit: 72h return -1.07% fell below exit band -1.0%
- 2026-10-02 21:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.25% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.01% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.78% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.62% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.85% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.55% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 21:23Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +2.01% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 16 fills (7 buy / 9 sell), traded 25,153, gross pnl +17.39, +14 bps per round trip, avg half spread 2.3 bps
- AVAX: 22 fills (9 buy / 13 sell), traded 38,374, gross pnl +570.74, +297 bps per round trip, avg half spread 1.3 bps
- BTC: 9 fills (5 buy / 4 sell), traded 11,314, gross pnl +96.41, +170 bps per round trip, avg half spread 0.3 bps, open 0.0324204
- DOGE: 16 fills (8 buy / 8 sell), traded 22,194, gross pnl -88.11, -79 bps per round trip, avg half spread 1.2 bps
- DOT: 17 fills (9 buy / 8 sell), traded 20,081, gross pnl +141.81, +141 bps per round trip, avg half spread 2.8 bps
- ETH: 13 fills (5 buy / 8 sell), traded 19,627, gross pnl +17.81, +18 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 13 fills (6 buy / 7 sell), traded 22,241, gross pnl +530.58, +477 bps per round trip, avg half spread 2.0 bps, open 39.9106
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

- equity 10,298.58 (started 10,000 at 2026-09-16 03:55Z), net +2.99% since start
- 24h +0.09%, 7d +0.09%, 30d +2.99%, max drawdown -1.00%
- fills 9 total, 1 in the last 7d
- costs 34.29 (fees 22.86 + slippage 11.43); gross pnl 332.87; cost coverage 9.71
- cash 7,714.75; positions: DOGE 28192.3
- last run 2026-10-02 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-02 20:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-10-02 20:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.65 not below -2.0
- 2026-10-02 20:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.54 not below -2.0
- 2026-10-02 20:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.45 not below -2.0
- 2026-10-02 20:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.50 not below -2.0
- 2026-10-02 20:23Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.80 vs 240h mean (entry -2.0, exit -0.5); vol 69% -> weight 0.25
- 2026-10-02 20:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.11 not below -2.0
- 2026-10-02 20:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.01 not below -2.0
- 2026-10-02 21:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.20 not below -2.0
- 2026-10-02 21:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.22 not below -2.0
- 2026-10-02 21:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.54 not below -2.0
- 2026-10-02 21:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.70 not below -2.0
- 2026-10-02 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.65 not below -2.0
- 2026-10-02 21:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.50 not below -2.0
- 2026-10-02 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.42 not below -2.0
- 2026-10-02 21:23Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.85 vs 240h mean (entry -2.0, exit -0.5); vol 69% -> weight 0.25
- 2026-10-02 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.25 not below -2.0
- 2026-10-02 21:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.03 not below -2.0

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

- equity 10,855.46 (started 10,000 at 2026-09-16 23:20Z), net +8.55% since start
- 24h -0.42%, 7d -1.01%, 30d +8.55%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 942.65; cost coverage 10.81
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-02 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-02 20:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 20:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 8.444e+04 still above 72h low 8.3e+04; realised vol 33% -> weight 0.25
- 2026-10-02 21:23Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: price 2661 still above 72h low 2661; realised vol 38% -> weight 0.25
- 2026-10-02 21:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 21:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -38.16, -94 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -85.50, -211 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 10,921.06 (started 10,000 at 2026-09-16 23:20Z), net +9.21% since start
- 24h -2.43%, 7d -5.14%, 30d +9.21%, max drawdown -11.53%
- fills 172 total, 123 in the last 7d
- costs 381.87 (fees 251.27 + slippage 130.61); gross pnl 1,302.93; cost coverage 3.41
- cash 5,428.74; positions: LTC 39.8619, SOL 23.1038
- last run 2026-10-02 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-02 20:23Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: price 118 still above the 48h low 117.1; realised vol 59% -> weight 0.25
- 2026-10-02 20:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2395 not above reaction high 0.2599
- 2026-10-02 20:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.59 not above reaction high 11.55
- 2026-10-02 20:23Z LINK buy target 0.25 (held 0.00) — enter long: higher low 12.18 vs prior low 10.66 (+14.2%) then broke above the reaction high 13.22 at 13.59; realised vol 97% -> weight 0.25
- 2026-10-02 20:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.47 not above reaction high 1.638
- 2026-10-02 20:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09149 not above reaction high 0.1039
- 2026-10-02 20:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.149 not above reaction high 1.218
- 2026-10-02 20:23Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 68.69 still above the 48h low 66.26; realised vol 65% -> weight 0.25
- 2026-10-02 21:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-02 21:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 2661 not above reaction high 2784
- 2026-10-02 21:23Z SOL hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: price 117.7 still above the 48h low 117.1; realised vol 59% -> weight 0.25
- 2026-10-02 21:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2392 not above reaction high 0.2599
- 2026-10-02 21:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.55 not above reaction high 11.55
- 2026-10-02 21:23Z LINK sell target 0.00 (held 0.25) — exit: closed 13.56 below the 48h low 13.59
- 2026-10-02 21:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.472 not above reaction high 1.638
- 2026-10-02 21:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09133 not above reaction high 0.1039
- 2026-10-02 21:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.142 not above reaction high 1.218
- 2026-10-02 21:23Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: price 68.66 still above the 48h low 66.54; realised vol 65% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 24 fills (11 buy / 13 sell), traded 45,344, gross pnl +23.98, +11 bps per round trip, avg half spread 2.3 bps
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 11 fills (6 buy / 5 sell), traded 11,408, gross pnl -82.80, -145 bps per round trip, avg half spread 1.5 bps
- DOT: 23 fills (11 buy / 12 sell), traded 36,196, gross pnl -57.11, -32 bps per round trip, avg half spread 2.7 bps
- ETH: 9 fills (4 buy / 5 sell), traded 11,060, gross pnl +79.28, +143 bps per round trip, avg half spread 0.1 bps
- LINK: 24 fills (11 buy / 13 sell), traded 39,514, gross pnl +198.42, +100 bps per round trip, avg half spread 2.8 bps
- LTC: 36 fills (19 buy / 17 sell), traded 45,054, gross pnl +184.96, +82 bps per round trip, avg half spread 1.9 bps, open 39.8619
- SOL: 17 fills (9 buy / 8 sell), traded 23,112, gross pnl +19.62, +17 bps per round trip, avg half spread 0.5 bps, open 23.1038
- XRP: 6 fills (3 buy / 3 sell), traded 6,959, gross pnl +88.07, +253 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-02 19:24Z sell ADA 1,808 @ 0.239444 fee 1.81 slip 1.09 (half spread 4.0 bps)
- 2026-10-02 19:24Z sell LINK 1,022 @ 13.6207 fee 1.02 slip 0.65 (half spread 4.3 bps)
- 2026-10-02 19:24Z sell DOGE 1,549 @ 0.0911551 fee 1.55 slip 0.77 (half spread 0.3 bps)
- 2026-10-02 19:24Z sell DOT 1,762 @ 1.14548 fee 1.76 slip 0.88 (half spread 1.3 bps)
- 2026-10-02 19:24Z buy SOL 1,159 @ 117.994 fee 1.16 slip 0.58 (half spread 0.4 bps)
- 2026-10-02 19:24Z buy LTC 1,130 @ 68.3892 fee 1.13 slip 0.56 (half spread 2.2 bps)
- 2026-10-02 20:23Z buy LINK 2,725 @ 13.6223 fee 2.72 slip 1.36 (half spread 3.0 bps)
- 2026-10-02 21:23Z sell LINK 2,723 @ 13.611 fee 2.72 slip 1.36 (half spread 2.3 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,931.87 (started 10,000 at 2026-09-25 04:23Z), net -0.68% since start
- 24h -1.67%, 7d -3.14%, 30d -0.61%, max drawdown -5.08%
- fills 23 total, 10 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl -26.56; cost coverage -0.64
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-02 21:23Z; halted today: False

last decisions (newest last):

- 2026-10-02 20:23Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +18.77% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 20:23Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +21.50% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 20:23Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +47.84% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 20:23Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +22.37% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 20:23Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +9.41% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-02 20:23Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +12.60% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 20:23Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +33.47% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 20:23Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +38.07% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 21:23Z BTC hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +9.14% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-02 21:23Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +11.21% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +18.12% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +20.55% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +46.98% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +21.90% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +8.98% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-02 21:23Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +11.84% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +32.49% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-02 21:23Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +38.09% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +12.65, +63 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +6.66, +147 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +6.82, +131 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -71.93, -1396 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl -29.49, -193 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -9.69, -186 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +82.72, +408 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -14.44, -72 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -15.08, -125 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +5.22, +17 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1122 candles, 2026-08-17 03:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1122 candles, 2026-08-17 03:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1122 candles, 2026-08-17 03:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1122 candles, 2026-08-17 03:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- AVAX: live 1122 candles, 2026-08-17 03:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1122 candles, 2026-08-17 03:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 1094 candles, 2026-08-18 07:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1094 candles, 2026-08-18 07:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 1094 candles, 2026-08-18 07:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1094 candles, 2026-08-18 07:00Z to 2026-10-02 20:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
