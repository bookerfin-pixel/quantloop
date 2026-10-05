# quantloop summary — generated 2026-10-05 06:36Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 12 of the last 24, 141 of the last 168
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 19.1 of 60, 40.9 days until the verdict
  so far: champion +11.05% (DD -12.84%, 175 fills) vs challenger1 +4.09% (DD -1.00%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.24% (usual 0.54, this window 0.71) vs challenger1 -5.77% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.3 over 20 days
  market over the window: BTC +12.96%, equal weight basket of 10 pairs +26.57%, basket max drawdown -7%, basket realised vol 57% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 13.9 of 60, 46.1 days until the verdict
  so far: champion -3.35% (DD -12.84%, 137 fills) vs challenger2 -0.16% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.37% (usual 0.54, this window 0.72) vs challenger2 -1.76% (usual 0.29, this window 0.16); the rule compares on skill, daily edge t +0.6 over 14 days
  market over the window: BTC +2.38%, equal weight basket of 10 pairs +5.59%, basket max drawdown -7%, basket realised vol 57% annualised
- challenger3: idle (free for a hypothesis)
- challenger4: testing H4 since 2026-09-25 22:21Z, day 9.3 of 60, 50.7 days until the verdict
  so far: champion -9.16% (DD -12.84%, 109 fills) vs challenger4 +0.66% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.08% (usual 0.55, this window 0.68) vs challenger4 +0.73% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.4 over 10 days
  market over the window: BTC +1.99%, equal weight basket of 10 pairs -0.15%, basket max drawdown -5%, basket realised vol 54% annualised
- free slots: challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,105.20 (started 10,000 at 2026-09-16 03:55Z), net +11.05% since start
- 24h +0.60%, 7d -6.66%, 30d +11.05%, max drawdown -12.84%
- fills 175 total, 89 in the last 7d
- costs 403.88 (fees 267.20 + slippage 136.68); gross pnl 1,509.07; cost coverage 3.74
- cash 5,512.40; positions: ADA 10369.5, LTC 39.6614
- last run 2026-10-05 06:36Z; halted today: False

last decisions (newest last):

- 2026-10-05 05:28Z SOL sell target 0.00 (held 0.14) — exit: 72h return -2.41% fell below exit band -1.0%
- 2026-10-05 05:28Z ADA buy target 0.25 (held 0.15) — stay long: 72h return +4.04% vs exit band -1.0% and price above 24h EMA; realised vol 93% -> weight 0.25
- 2026-10-05 05:28Z AVAX sell target 0.00 (held 0.14) — exit: 72h return -2.79% fell below exit band -1.0%
- 2026-10-05 05:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.80% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 05:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.74% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 05:28Z DOGE sell target 0.00 (held 0.13) — exit: 72h return -1.60% fell below exit band -1.0%
- 2026-10-05 05:28Z DOT sell target 0.00 (held 0.16) — exit: 72h return -1.56% fell below exit band -1.0%
- 2026-10-05 05:28Z LTC buy target 0.25 (held 0.14) — stay long: 72h return +0.17% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 63% -> weight 0.25
- 2026-10-05 06:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.27% not above entry band +1.0%
- 2026-10-05 06:36Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +6.38% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-05 06:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.35% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.18% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.69% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.56% not above entry band +1.0%
- 2026-10-05 06:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.42% not above entry band +1.0%
- 2026-10-05 06:36Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return -0.47% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 18 fills (9 buy / 9 sell), traded 27,823, gross pnl +160.82, +116 bps per round trip, avg half spread 2.2 bps, open 10369.5
- AVAX: 25 fills (10 buy / 15 sell), traded 43,731, gross pnl +535.38, +245 bps per round trip, avg half spread 1.3 bps
- BTC: 12 fills (5 buy / 7 sell), traded 14,086, gross pnl +130.80, +186 bps per round trip, avg half spread 0.2 bps
- DOGE: 18 fills (9 buy / 9 sell), traded 25,001, gross pnl -113.62, -91 bps per round trip, avg half spread 1.2 bps
- DOT: 19 fills (10 buy / 9 sell), traded 23,558, gross pnl +152.85, +130 bps per round trip, avg half spread 2.7 bps
- ETH: 13 fills (5 buy / 8 sell), traded 19,627, gross pnl +17.81, +18 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 16 fills (7 buy / 9 sell), traded 24,689, gross pnl +578.82, +469 bps per round trip, avg half spread 1.9 bps, open 39.6614
- SOL: 18 fills (9 buy / 9 sell), traded 29,148, gross pnl +37.60, +26 bps per round trip, avg half spread 0.5 bps
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-04 21:24Z buy DOGE 1,417 @ 0.0968552 fee 1.42 slip 0.71 (half spread 2.5 bps)
- 2026-10-05 05:28Z sell BTC 1,571 @ 85456.2 fee 1.57 slip 0.79 (half spread 0.0 bps)
- 2026-10-05 05:28Z sell SOL 1,561 @ 120.075 fee 1.56 slip 0.78 (half spread 0.4 bps)
- 2026-10-05 05:28Z sell AVAX 1,556 @ 10.8821 fee 1.56 slip 0.78 (half spread 1.4 bps)
- 2026-10-05 05:28Z sell DOGE 1,390 @ 0.0950154 fee 1.39 slip 0.70 (half spread 0.1 bps)
- 2026-10-05 05:28Z sell DOT 1,743 @ 1.20735 fee 1.74 slip 0.87 (half spread 2.1 bps)
- 2026-10-05 05:28Z buy ADA 1,092 @ 0.266556 fee 1.09 slip 0.55 (half spread 1.2 bps)
- 2026-10-05 05:28Z buy LTC 1,206 @ 69.6898 fee 1.21 slip 0.60 (half spread 0.7 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,397.39 (started 10,000 at 2026-09-16 03:55Z), net +3.97% since start
- 24h +0.44%, 7d +1.05%, 30d +3.97%, max drawdown -1.00%
- fills 10 total, 2 in the last 7d
- costs 38.32 (fees 25.55 + slippage 12.77); gross pnl 435.71; cost coverage 11.37
- cash 10,397.39; positions: none
- last run 2026-10-05 06:36Z; halted today: False

last decisions (newest last):

- 2026-10-05 05:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.32 not below -2.0
- 2026-10-05 05:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.01 not below -2.0
- 2026-10-05 05:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.12 not below -2.0
- 2026-10-05 05:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-10-05 05:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.27 not below -2.0
- 2026-10-05 05:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.08 not below -2.0
- 2026-10-05 05:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.32 not below -2.0
- 2026-10-05 05:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.05 not below -2.0
- 2026-10-05 06:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.64 not below -2.0
- 2026-10-05 06:36Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.71 not below -2.0
- 2026-10-05 06:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.27 not below -2.0
- 2026-10-05 06:36Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.44 not below -2.0
- 2026-10-05 06:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.01 not below -2.0
- 2026-10-05 06:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.36 not below -2.0
- 2026-10-05 06:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.17 not below -2.0
- 2026-10-05 06:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.12 not below -2.0
- 2026-10-05 06:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.51 not below -2.0
- 2026-10-05 06:36Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.02 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 5,258, gross pnl +115.51, +439 bps per round trip, avg half spread 0.3 bps
- ETH: 2 fills (1 buy / 1 sell), traded 5,048, gross pnl +50.93, +202 bps per round trip, avg half spread 0.4 bps
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)
- 2026-09-17 13:23Z sell ETH 2,548 @ 2449.98 fee 2.55 slip 1.27 (half spread 0.4 bps)
- 2026-09-18 01:20Z sell ADA 2,628 @ 0.205888 fee 2.63 slip 1.31 (half spread 2.2 bps)
- 2026-09-18 03:21Z sell BTC 2,538 @ 77289.3 fee 2.54 slip 1.27 (half spread 0.0 bps)
- 2026-10-02 19:24Z buy DOGE 2,572 @ 0.0912463 fee 2.57 slip 1.29 (half spread 0.3 bps)
- 2026-10-04 18:21Z sell DOGE 2,685 @ 0.0952504 fee 2.69 slip 1.34 (half spread 0.3 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,947.87 (started 10,000 at 2026-09-16 23:20Z), net +9.48% since start
- 24h +0.24%, 7d -0.16%, 30d +9.48%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,035.05; cost coverage 11.87
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-05 06:36Z; halted today: False

last decisions (newest last):

- 2026-10-05 05:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 05:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 8.574e+04 still above 72h low 8.424e+04; realised vol 33% -> weight 0.25
- 2026-10-05 06:36Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 2706 still above 72h low 2661; realised vol 38% -> weight 0.25
- 2026-10-05 06:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 06:36Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl +4.74, +12 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -36.00, -89 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,041.71 (started 10,000 at 2026-10-05 05:28Z), net +0.42% since start
- 24h +0.45%, 7d +0.45%, 30d +0.45%, max drawdown 0.00%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 45.45; cost coverage 12.12
- cash 7,497.50; positions: ADA 9378.9
- last run 2026-10-05 06:36Z; halted today: False

last decisions (newest last):

- 2026-10-05 05:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.41% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 05:28Z ADA buy target 0.25 (held 0.00) — enter long: 72h return +4.04% vs entry band +1.0% and price above 24h EMA; realised vol 93% -> weight 0.25
- 2026-10-05 05:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.79% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 05:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.80% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 05:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.74% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 05:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.60% not above entry band +1.0%
- 2026-10-05 05:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-10-05 05:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.17% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.27% not above entry band +1.0%
- 2026-10-05 06:36Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.19% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: 72h return +6.38% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-05 06:36Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.35% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.18% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.69% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 06:36Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.56% not above entry band +1.0%
- 2026-10-05 06:36Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.42% not above entry band +1.0%
- 2026-10-05 06:36Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.47% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl +45.45, +364 bps per round trip, avg half spread 1.2 bps, open 9378.9

last fills:

- 2026-10-05 05:28Z buy ADA 2,500 @ 0.266556 fee 2.50 slip 1.25 (half spread 1.2 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,321.41 (started 10,000 at 2026-09-25 04:23Z), net +3.21% since start
- 24h +1.48%, 7d +3.29%, 30d +3.29%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 362.98; cost coverage 8.73
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-05 06:36Z; halted today: False

last decisions (newest last):

- 2026-10-05 05:28Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +18.36% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 05:28Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +26.46% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 05:28Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.009 below threshold 0.05 | stay long: 720h return +46.79% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 05:28Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +20.82% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 05:28Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +7.52% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 05:28Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +12.31% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 05:28Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +36.80% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 05:28Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +32.76% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +7.72% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 06:36Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +10.38% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +18.19% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +27.64% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.009 below threshold 0.05 | stay long: 720h return +47.20% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 06:36Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +21.21% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +7.61% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 06:36Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +12.50% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +35.34% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 06:36Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +32.05% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +138.28, +689 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +33.02, +728 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +23.39, +450 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -30.65, -595 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +33.59, +220 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +9.44, +182 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +121.10, +597 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -4.51, -23 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +9.07, +75 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +30.24, +99 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1179 candles, 2026-08-17 03:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1179 candles, 2026-08-17 03:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1179 candles, 2026-08-17 03:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1179 candles, 2026-08-17 03:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 1179 candles, 2026-08-17 03:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- LINK: live 1179 candles, 2026-08-17 03:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- XRP: live 1151 candles, 2026-08-18 07:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 1151 candles, 2026-08-18 07:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 1151 candles, 2026-08-18 07:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LTC: live 1151 candles, 2026-08-18 07:00Z to 2026-10-05 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
