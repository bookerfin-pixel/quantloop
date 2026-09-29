# quantloop summary — generated 2026-09-29 06:29Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 13.0 of 60, 47.0 days until the verdict
  so far: champion +15.78% (DD -7.61%, 96 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +3.02% (usual 0.54, this window 0.73) vs challenger1 -5.79% (usual 0.37, this window 0.12); the rule compares on skill, daily edge t -0.8 over 14 days
  market over the window: BTC +9.87%, equal weight basket of 10 pairs +23.72%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 7.9 of 60, 52.1 days until the verdict
  so far: champion +0.76% (DD -7.61%, 58 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.00% (usual 0.54, this window 0.76) vs challenger2 -0.93% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -0.0 over 8 days
  market over the window: BTC -0.42%, equal weight basket of 10 pairs +3.27%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 4.1 of 60, 55.9 days until the verdict
  so far: champion -2.44% (DD -7.61%, 38 fills) vs challenger3 -2.12% (DD -4.74%, 68 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.92% (usual 0.55, this window 0.76) vs challenger3 -2.17% (usual 0.05, this window 0.26); the rule compares on skill, daily edge t +0.2 over 5 days
  market over the window: BTC -0.96%, equal weight basket of 10 pairs +0.89%, basket max drawdown -5%, basket realised vol 57% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 3.3 of 60, 56.7 days until the verdict
  so far: champion -5.29% (DD -7.61%, 30 fills) vs challenger4 -1.31% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.01% (usual 0.55, this window 0.70) vs challenger4 -0.19% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +1.3 over 4 days
  market over the window: BTC -0.79%, equal weight basket of 10 pairs -2.35%, basket max drawdown -5%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,577.97 (started 10,000 at 2026-09-16 03:55Z), net +15.78% since start
- 24h -3.14%, 7d -1.57%, 30d +15.78%, max drawdown -7.61%
- fills 96 total, 55 in the last 7d
- costs 224.45 (fees 147.95 + slippage 76.49); gross pnl 1,802.42; cost coverage 8.03
- cash 8,784.43; positions: LINK 187.649
- last run 2026-09-29 06:29Z; halted today: False

last decisions (newest last):

- 2026-09-29 05:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.49% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 05:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.32% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 05:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.94% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 05:23Z LINK hold target 0.25 (held 0.24) — hold: weight change +0.010 below threshold 0.05 | stay long: 72h return +4.24% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-29 05:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.61% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 05:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.07% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 05:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.91% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 05:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.22% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 06:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.61% not above entry band +1.0%
- 2026-09-29 06:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.40% not above entry band +1.0%
- 2026-09-29 06:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.90% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 06:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.97% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 06:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.18% not above entry band +1.0%
- 2026-09-29 06:29Z LINK hold target 0.25 (held 0.24) — hold: weight change +0.009 below threshold 0.05 | stay long: 72h return +5.97% vs exit band -1.0% and price above 24h EMA; realised vol 1...
- 2026-09-29 06:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.64% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 06:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.71% not above entry band +1.0%
- 2026-09-29 06:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.98% not above entry band +1.0% and price below 24h EMA
- 2026-09-29 06:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.54% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (5 buy / 6 sell), traded 18,727, gross pnl +101.44, +108 bps per round trip, avg half spread 2.4 bps
- AVAX: 11 fills (5 buy / 6 sell), traded 18,801, gross pnl +665.50, +708 bps per round trip, avg half spread 1.1 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 15,017, gross pnl -37.42, -50 bps per round trip, avg half spread 1.7 bps
- DOT: 12 fills (7 buy / 5 sell), traded 13,246, gross pnl +261.75, +395 bps per round trip, avg half spread 3.1 bps
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 15 fills (8 buy / 7 sell), traded 24,437, gross pnl +1.18, +1 bps per round trip, avg half spread 2.8 bps, open 187.649
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-28 07:26Z buy DOT 595 @ 1.21426 fee 0.60 slip 0.30 (half spread 0.4 bps)
- 2026-09-28 08:27Z sell LINK 2,973 @ 13.6792 fee 2.97 slip 1.78 (half spread 4.0 bps)
- 2026-09-28 08:27Z sell DOT 2,970 @ 1.21149 fee 2.97 slip 1.49 (half spread 2.5 bps)
- 2026-09-28 12:29Z buy LTC 2,971 @ 72.2361 fee 2.97 slip 1.48 (half spread 1.4 bps)
- 2026-09-28 13:25Z buy LINK 2,952 @ 14.5956 fee 2.95 slip 1.48 (half spread 2.3 bps)
- 2026-09-28 14:27Z sell LINK 2,906 @ 14.3673 fee 2.91 slip 2.00 (half spread 4.9 bps)
- 2026-09-28 14:27Z sell LTC 2,862 @ 69.5802 fee 2.86 slip 1.43 (half spread 2.2 bps)
- 2026-09-29 00:29Z buy LINK 2,929 @ 15.6096 fee 2.93 slip 1.56 (half spread 3.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-29 06:29Z; halted today: False

last decisions (newest last):

- 2026-09-29 05:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-09-29 05:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.12 not below -2.0
- 2026-09-29 05:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.22 not below -2.0
- 2026-09-29 05:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.71 not below -2.0
- 2026-09-29 05:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-09-29 05:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.34 not below -2.0
- 2026-09-29 05:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.37 not below -2.0
- 2026-09-29 05:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.39 not below -2.0
- 2026-09-29 06:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.26 not below -2.0
- 2026-09-29 06:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.20 not below -2.0
- 2026-09-29 06:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.32 not below -2.0
- 2026-09-29 06:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.05 not below -2.0
- 2026-09-29 06:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.05 not below -2.0
- 2026-09-29 06:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.83 not below -2.0
- 2026-09-29 06:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0
- 2026-09-29 06:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.18 not below -2.0
- 2026-09-29 06:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.19 not below -2.0
- 2026-09-29 06:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0

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
- 24h +0.00%, 7d +0.00%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 0 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-29 06:29Z; halted today: False

last decisions (newest last):

- 2026-09-29 05:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 05:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.34e+04 not above 120h high 8.502e+04
- 2026-09-29 06:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2675 not above 120h high 2718
- 2026-09-29 06:29Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-29 06:29Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 11,268.34 (started 10,000 at 2026-09-16 23:20Z), net +12.68% since start
- 24h -1.48%, 7d -4.33%, 30d +12.68%, max drawdown -9.51%
- fills 117 total, 79 in the last 7d
- costs 294.76 (fees 193.45 + slippage 101.30); gross pnl 1,563.10; cost coverage 5.30
- cash -0.00; positions: ADA 9141.44, AVAX 212.774, DOT 752.629, LINK 126.153, LTC 25.2009, SOL 18.9043
- last run 2026-09-29 06:29Z; halted today: False

last decisions (newest last):

- 2026-09-29 05:23Z SOL hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: price 117.7 still above the 48h low 116.9; realised vol 54% -> weight 0.25
- 2026-09-29 05:23Z ADA hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: price 0.2429 still above the 48h low 0.2405; realised vol 87% -> weight 0.25
- 2026-09-29 05:23Z AVAX hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: price 10.46 still above the 48h low 10.23; realised vol 93% -> weight 0.25
- 2026-09-29 05:23Z LINK hold target 0.20 (held 0.25) — hold: weight change -0.046 below threshold 0.05 | stay long: price 14.75 still above the 48h low 13.57; realised vol 104% -> weight 0.25
- 2026-09-29 05:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.37 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-29 05:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-29 05:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.156 not above reaction high 1.162
- 2026-09-29 05:23Z LTC hold target 0.20 (held 0.15) — hold: weight change +0.047 below threshold 0.05 | stay long: price 67.81 still above the 48h low 67.57; realised vol 105% -> weight 0.25
- 2026-09-29 06:29Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.023e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-29 06:29Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2571 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-29 06:29Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: price 118.2 still above the 48h low 116.9; realised vol 54% -> weight 0.25
- 2026-09-29 06:29Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.033 below threshold 0.05 | stay long: price 0.2448 still above the 48h low 0.2405; realised vol 87% -> weight 0.25
- 2026-09-29 06:29Z AVAX hold target 0.17 (held 0.20) — hold: weight change -0.037 below threshold 0.05 | stay long: price 10.62 still above the 48h low 10.23; realised vol 93% -> weight 0.25
- 2026-09-29 06:29Z LINK sell target 0.17 (held 0.24) — stay long: price 14.87 still above the 48h low 13.57; realised vol 105% -> weight 0.25
- 2026-09-29 06:29Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.37 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-29 06:29Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-29 06:29Z DOT buy target 0.17 (held 0.00) — enter long: higher low 1.075 vs prior low 0.939 (+14.5%) then broke above the reaction high 1.162 at 1.165; realised vol 96% -> weight 0.25
- 2026-09-29 06:29Z LTC hold target 0.17 (held 0.15) — hold: weight change +0.014 below threshold 0.05 | stay long: price 68.05 still above the 48h low 67.57; realised vol 105% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 20 fills (10 buy / 10 sell), traded 40,395, gross pnl +84.68, +42 bps per round trip, avg half spread 2.3 bps, open 9141.44
- AVAX: 16 fills (7 buy / 9 sell), traded 24,842, gross pnl +753.22, +606 bps per round trip, avg half spread 1.6 bps, open 212.774
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 17 fills (8 buy / 9 sell), traded 28,876, gross pnl +7.65, +5 bps per round trip, avg half spread 3.0 bps, open 752.629
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 16 fills (8 buy / 8 sell), traded 26,835, gross pnl +319.43, +238 bps per round trip, avg half spread 3.0 bps, open 126.153
- LTC: 18 fills (9 buy / 9 sell), traded 33,530, gross pnl +118.39, +71 bps per round trip, avg half spread 2.1 bps, open 25.2009
- SOL: 12 fills (6 buy / 6 sell), traded 18,097, gross pnl +65.49, +72 bps per round trip, avg half spread 0.5 bps, open 18.9043
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

- equity 10,119.70 (started 10,000 at 2026-09-25 04:23Z), net +1.20% since start
- 24h +0.66%, 7d +1.27%, 30d +1.27%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 161.27; cost coverage 3.88
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-29 06:29Z; halted today: False

last decisions (newest last):

- 2026-09-29 05:23Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +11.95% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 05:23Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +21.20% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 05:23Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.010 below threshold 0.05 | stay long: 720h return +43.54% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 05:23Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.011 below threshold 0.05 | stay long: 720h return +29.72% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 05:23Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +6.67% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-29 05:23Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +9.62% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-29 05:23Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +38.13% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 05:23Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +38.78% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 06:29Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +6.76% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-29 06:29Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +8.92% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-09-29 06:29Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +12.48% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 06:29Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +21.81% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 06:29Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +45.38% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 06:29Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.011 below threshold 0.05 | stay long: 720h return +30.31% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-29 06:29Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +6.97% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-29 06:29Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +10.29% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 06:29Z DOT hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +38.25% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-29 06:29Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +38.91% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +37.67, +188 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +19.69, +434 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -1.25, -24 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -44.77, -869 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl -14.20, -93 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +2.24, +43 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +178.32, +879 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -32.21, -162 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -6.81, -57 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +22.58, +74 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1035 candles, 2026-08-17 03:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1035 candles, 2026-08-17 03:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1035 candles, 2026-08-17 03:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1035 candles, 2026-08-17 03:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- AVAX: live 1035 candles, 2026-08-17 03:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.2 bps
- LINK: live 1035 candles, 2026-08-17 03:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1007 candles, 2026-08-18 07:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1007 candles, 2026-08-18 07:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 1007 candles, 2026-08-18 07:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 1007 candles, 2026-08-18 07:00Z to 2026-09-29 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.8 bps
