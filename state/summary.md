# quantloop summary — generated 2026-10-01 06:33Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 15.0 of 60, 45.0 days until the verdict
  so far: champion +12.47% (DD -10.20%, 119 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.46% (usual 0.54, this window 0.69) vs challenger1 -6.59% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.5 over 16 days
  market over the window: BTC +10.99%, equal weight basket of 10 pairs +25.89%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 9.9 of 60, 50.1 days until the verdict
  so far: champion -2.12% (DD -10.20%, 81 fills) vs challenger2 -0.63% (DD -1.16%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.79% (usual 0.54, this window 0.69) vs challenger2 -2.05% (usual 0.29, this window 0.06); the rule compares on skill, daily edge t +0.3 over 10 days
  market over the window: BTC +0.60%, equal weight basket of 10 pairs +4.96%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 6.1 of 60, 53.9 days until the verdict
  so far: champion -5.23% (DD -10.20%, 61 fills) vs challenger3 -0.84% (DD -4.74%, 88 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.67% (usual 0.55, this window 0.64) vs challenger3 -0.98% (usual 0.05, this window 0.50); the rule compares on skill, daily edge t +1.1 over 7 days
  market over the window: BTC +0.04%, equal weight basket of 10 pairs +2.65%, basket max drawdown -5%, basket realised vol 58% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 5.3 of 60, 54.7 days until the verdict
  so far: champion -8.00% (DD -10.20%, 53 fills) vs challenger4 -0.33% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.64% (usual 0.55, this window 0.59) vs challenger4 -0.02% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.6 over 6 days
  market over the window: BTC +0.22%, equal weight basket of 10 pairs -0.66%, basket max drawdown -5%, basket realised vol 59% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,246.94 (started 10,000 at 2026-09-16 03:55Z), net +12.47% since start
- 24h -1.71%, 7d -4.12%, 30d +12.47%, max drawdown -10.20%
- fills 119 total, 68 in the last 7d
- costs 289.39 (fees 190.96 + slippage 98.44); gross pnl 1,536.34; cost coverage 5.31
- cash -0.00; positions: ADA 5566.95, AVAX 126.914, BTC 0.0167185, DOGE 14715.2, DOT 1134.39, ETH 0.518607, LINK 97.3699, XRP 930.182
- last run 2026-10-01 06:33Z; halted today: False

last decisions (newest last):

- 2026-10-01 05:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.79% not above entry band +1.0%
- 2026-10-01 05:24Z ADA none target 0.17 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-01 05:24Z AVAX hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +4.01% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-01 05:24Z LINK hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: 72h return +3.71% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-10-01 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.49% not above entry band +1.0%
- 2026-10-01 05:24Z DOGE hold target 0.17 (held 0.20) — hold: weight change -0.034 below threshold 0.05 | stay long: 72h return +1.36% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-01 05:24Z DOT hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: 72h return -0.42% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-01 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.85% not above entry band +1.0%
- 2026-10-01 06:33Z BTC buy target 0.12 (held 0.00) — enter long: 72h return +1.30% vs entry band +1.0% and price above 24h EMA; realised vol 32% -> weight 0.25
- 2026-10-01 06:33Z ETH sell target 0.12 (held 0.20) — stay long: 72h return +2.47% vs exit band -1.0% and price above 24h EMA; realised vol 37% -> weight 0.25
- 2026-10-01 06:33Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.21% not above entry band +1.0%
- 2026-10-01 06:33Z ADA buy target 0.12 (held 0.00) — enter long: 72h return +2.58% vs entry band +1.0% and price above 24h EMA; realised vol 88% -> weight 0.25
- 2026-10-01 06:33Z AVAX sell target 0.12 (held 0.20) — stay long: 72h return +4.76% vs exit band -1.0% and price above 24h EMA; realised vol 99% -> weight 0.25
- 2026-10-01 06:33Z LINK sell target 0.12 (held 0.20) — stay long: 72h return +4.43% vs exit band -1.0% and price above 24h EMA; realised vol 105% -> weight 0.25
- 2026-10-01 06:33Z XRP buy target 0.12 (held 0.00) — enter long: 72h return +1.64% vs entry band +1.0% and price above 24h EMA; realised vol 67% -> weight 0.25
- 2026-10-01 06:33Z DOGE sell target 0.12 (held 0.20) — stay long: 72h return +2.63% vs exit band -1.0% and price above 24h EMA; realised vol 65% -> weight 0.25
- 2026-10-01 06:33Z DOT sell target 0.12 (held 0.20) — stay long: 72h return +0.13% vs exit band -1.0% and price above 24h EMA; realised vol 98% -> weight 0.25
- 2026-10-01 06:33Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.45% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 12 fills (6 buy / 6 sell), traded 20,135, gross pnl +101.44, +101 bps per round trip, avg half spread 2.4 bps, open 5566.95
- AVAX: 16 fills (7 buy / 9 sell), traded 28,740, gross pnl +578.72, +403 bps per round trip, avg half spread 1.3 bps, open 126.914
- BTC: 5 fills (3 buy / 2 sell), traded 6,859, gross pnl +59.67, +174 bps per round trip, avg half spread 0.5 bps, open 0.0167185
- DOGE: 12 fills (7 buy / 5 sell), traded 18,118, gross pnl -36.36, -40 bps per round trip, avg half spread 1.4 bps, open 14715.2
- DOT: 14 fills (8 buy / 6 sell), traded 16,322, gross pnl +250.57, +307 bps per round trip, avg half spread 3.0 bps, open 1134.39
- ETH: 9 fills (4 buy / 5 sell), traded 15,499, gross pnl +27.76, +36 bps per round trip, avg half spread 0.1 bps, open 0.518607
- LINK: 21 fills (10 buy / 11 sell), traded 37,032, gross pnl -146.96, -79 bps per round trip, avg half spread 2.4 bps, open 97.3699
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 10 fills (5 buy / 5 sell), traded 16,036, gross pnl +174.70, +218 bps per round trip, avg half spread 0.7 bps, open 930.182

last fills:

- 2026-10-01 06:33Z sell ETH 861 @ 2711.72 fee 0.86 slip 0.43 (half spread 0.0 bps)
- 2026-10-01 06:33Z sell AVAX 845 @ 11.081 fee 0.85 slip 0.42 (half spread 0.5 bps)
- 2026-10-01 06:33Z sell LINK 841 @ 14.4431 fee 0.84 slip 0.42 (half spread 0.8 bps)
- 2026-10-01 06:33Z sell DOGE 847 @ 0.0955692 fee 0.85 slip 0.42 (half spread 0.2 bps)
- 2026-10-01 06:33Z sell DOT 828 @ 1.23973 fee 0.83 slip 0.41 (half spread 2.8 bps)
- 2026-10-01 06:33Z buy BTC 1,407 @ 84185.1 fee 1.41 slip 0.70 (half spread 0.0 bps)
- 2026-10-01 06:33Z buy ADA 1,407 @ 0.252822 fee 1.41 slip 0.70 (half spread 1.5 bps)
- 2026-10-01 06:33Z buy XRP 1,399 @ 1.50402 fee 1.40 slip 0.70 (half spread 0.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-10-01 06:33Z; halted today: False

last decisions (newest last):

- 2026-10-01 05:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-10-01 05:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.65 not below -2.0
- 2026-10-01 05:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.80 not below -2.0
- 2026-10-01 05:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.88 not below -2.0
- 2026-10-01 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.55 not below -2.0
- 2026-10-01 05:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.15 not below -2.0
- 2026-10-01 05:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-10-01 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.01 not below -2.0
- 2026-10-01 06:33Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.13 not below -2.0
- 2026-10-01 06:33Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.59 not below -2.0
- 2026-10-01 06:33Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.30 not below -2.0
- 2026-10-01 06:33Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.76 not below -2.0
- 2026-10-01 06:33Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.84 not below -2.0
- 2026-10-01 06:33Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.87 not below -2.0
- 2026-10-01 06:33Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.43 not below -2.0
- 2026-10-01 06:33Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.12 not below -2.0
- 2026-10-01 06:33Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.12 not below -2.0
- 2026-10-01 06:33Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.06 not below -2.0

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

- equity 10,896.15 (started 10,000 at 2026-09-16 23:20Z), net +8.96% since start
- 24h +0.01%, 7d -0.63%, 30d +8.96%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 983.34; cost coverage 11.28
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-01 06:33Z; halted today: False

last decisions (newest last):

- 2026-10-01 05:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 8.425e+04 still above 72h low 8.263e+04; realised vol 32% -> weight 0.25
- 2026-10-01 06:33Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 2716 still above 72h low 2640; realised vol 37% -> weight 0.25
- 2026-10-01 06:33Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-01 06:33Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -48.82, -120 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -34.16, -84 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,416.03 (started 10,000 at 2026-09-16 23:20Z), net +14.16% since start
- 24h +1.35%, 7d -0.84%, 30d +14.16%, max drawdown -9.51%
- fills 137 total, 88 in the last 7d
- costs 317.53 (fees 208.59 + slippage 108.95); gross pnl 1,733.56; cost coverage 5.46
- cash -0.00; positions: ADA 5740.21, AVAX 129.447, DOGE 15015.8, DOT 1141.01, ETH 0.375585, LINK 126.153, SOL 11.8866, XRP 945.012
- last run 2026-10-01 06:33Z; halted today: False

last decisions (newest last):

- 2026-10-01 05:24Z SOL hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 119 still above the 48h low 117.2; realised vol 59% -> weight 0.25
- 2026-10-01 05:24Z ADA hold target 0.11 (held 0.13) — hold: weight change -0.016 below threshold 0.05 | stay long: price 0.2525 still above the 48h low 0.2413; realised vol 88% -> weight 0.25
- 2026-10-01 05:24Z AVAX hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 11.11 still above the 48h low 10.46; realised vol 99% -> weight 0.25
- 2026-10-01 05:24Z LINK hold target 0.11 (held 0.16) — hold: weight change -0.049 below threshold 0.05 | stay long: price 14.48 still above the 48h low 14.21; realised vol 105% -> weight 0.25
- 2026-10-01 05:24Z XRP hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 1.503 still above the 48h low 1.482; realised vol 67% -> weight 0.25
- 2026-10-01 05:24Z DOGE hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.09568 still above the 48h low 0.09297; realised vol 65% -> weight 0.25
- 2026-10-01 05:24Z DOT hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 1.245 still above the 48h low 1.156; realised vol 98% -> weight 0.25
- 2026-10-01 05:24Z LTC none target 0.11 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-10-01 06:33Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.154e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-01 06:33Z ETH hold target 0.11 (held 0.09) — hold: weight change +0.022 below threshold 0.05 | stay long: price 2716 still above the 48h low 2661; realised vol 37% -> weight 0.25
- 2026-10-01 06:33Z SOL hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 119.4 still above the 48h low 117.2; realised vol 58% -> weight 0.25
- 2026-10-01 06:33Z ADA hold target 0.11 (held 0.13) — hold: weight change -0.016 below threshold 0.05 | stay long: price 0.2533 still above the 48h low 0.2413; realised vol 88% -> weight 0.25
- 2026-10-01 06:33Z AVAX hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 11.13 still above the 48h low 10.62; realised vol 99% -> weight 0.25
- 2026-10-01 06:33Z LINK hold target 0.11 (held 0.16) — hold: weight change -0.049 below threshold 0.05 | stay long: price 14.48 still above the 48h low 14.21; realised vol 105% -> weight 0.25
- 2026-10-01 06:33Z XRP hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 1.508 still above the 48h low 1.482; realised vol 67% -> weight 0.25
- 2026-10-01 06:33Z DOGE hold target 0.11 (held 0.13) — hold: weight change -0.015 below threshold 0.05 | stay long: price 0.0958 still above the 48h low 0.09297; realised vol 65% -> weight 0.25
- 2026-10-01 06:33Z DOT hold target 0.11 (held 0.12) — hold: weight change -0.013 below threshold 0.05 | stay long: price 1.24 still above the 48h low 1.163; realised vol 98% -> weight 0.25
- 2026-10-01 06:33Z LTC none target 0.11 (held 0.00) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (10 buy / 11 sell), traded 41,237, gross pnl +124.07, +60 bps per round trip, avg half spread 2.2 bps, open 5740.21
- AVAX: 17 fills (7 buy / 10 sell), traded 25,757, gross pnl +811.03, +630 bps per round trip, avg half spread 1.5 bps, open 129.447
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 7 fills (5 buy / 2 sell), traded 7,263, gross pnl -17.05, -47 bps per round trip, avg half spread 2.0 bps, open 15015.8
- DOT: 19 fills (9 buy / 10 sell), traded 31,210, gross pnl +130.02, +83 bps per round trip, avg half spread 2.9 bps, open 1141.01
- ETH: 5 fills (3 buy / 2 sell), traded 6,460, gross pnl +95.97, +297 bps per round trip, avg half spread 0.1 bps, open 0.375585
- LINK: 16 fills (8 buy / 8 sell), traded 26,835, gross pnl +264.33, +197 bps per round trip, avg half spread 3.0 bps, open 126.153
- LTC: 30 fills (15 buy / 15 sell), traded 39,880, gross pnl +90.54, +45 bps per round trip, avg half spread 2.0 bps
- SOL: 13 fills (6 buy / 7 sell), traded 18,936, gross pnl +72.98, +77 bps per round trip, avg half spread 0.5 bps, open 11.8866
- XRP: 5 fills (3 buy / 2 sell), traded 5,553, gross pnl +102.01, +367 bps per round trip, avg half spread 0.7 bps, open 945.012

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

- equity 10,219.57 (started 10,000 at 2026-09-25 04:23Z), net +2.20% since start
- 24h +1.32%, 7d +2.27%, 30d +2.27%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 261.14; cost coverage 6.28
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-01 06:33Z; halted today: False

last decisions (newest last):

- 2026-10-01 05:24Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +14.92% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 05:24Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +25.70% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 05:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +53.03% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 05:24Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +26.93% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 05:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +8.90% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-01 05:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +15.11% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 05:24Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +46.18% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 05:24Z LTC hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +38.37% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-01 06:33Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +6.43% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-01 06:33Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +9.36% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-01 06:33Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +14.47% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 06:33Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +24.95% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 06:33Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +51.84% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 06:33Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +25.81% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 06:33Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +8.20% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-01 06:33Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +14.29% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 06:33Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +45.13% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-01 06:33Z LTC hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +37.03% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +62.76, +313 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +46.52, +1026 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +2.71, +52 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -30.45, -591 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +50.23, +329 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +10.16, +195 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +145.42, +717 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -46.60, -234 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -4.76, -39 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +25.14, +82 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1083 candles, 2026-08-17 03:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1083 candles, 2026-08-17 03:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1083 candles, 2026-08-17 03:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1083 candles, 2026-08-17 03:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1083 candles, 2026-08-17 03:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1083 candles, 2026-08-17 03:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 1055 candles, 2026-08-18 07:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1055 candles, 2026-08-18 07:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 1055 candles, 2026-08-18 07:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1055 candles, 2026-08-18 07:00Z to 2026-10-01 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
