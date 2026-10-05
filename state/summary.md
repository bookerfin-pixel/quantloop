# quantloop summary — generated 2026-10-05 21:32Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 19.7 of 60, 40.3 days until the verdict
  so far: champion +10.69% (DD -12.84%, 189 fills) vs challenger1 +4.09% (DD -1.00%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.72% (usual 0.54, this window 0.71) vs challenger1 -5.84% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.3 over 20 days
  market over the window: BTC +12.99%, equal weight basket of 10 pairs +26.77%, basket max drawdown -7%, basket realised vol 57% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 14.5 of 60, 45.5 days until the verdict
  so far: champion -3.67% (DD -12.84%, 151 fills) vs challenger2 -0.14% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.77% (usual 0.54, this window 0.72) vs challenger2 -1.78% (usual 0.29, this window 0.18); the rule compares on skill, daily edge t +0.6 over 15 days
  market over the window: BTC +2.41%, equal weight basket of 10 pairs +5.74%, basket max drawdown -7%, basket realised vol 57% annualised
- challenger3: idle (free for a hypothesis)
- challenger4: testing H4 since 2026-09-25 22:21Z, day 10.0 of 60, 50.0 days until the verdict
  so far: champion -9.46% (DD -12.84%, 123 fills) vs challenger4 +0.60% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.46% (usual 0.55, this window 0.67) vs challenger4 +0.60% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.5 over 10 days
  market over the window: BTC +2.03%, equal weight basket of 10 pairs -0.00%, basket max drawdown -5%, basket realised vol 53% annualised
- free slots: challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,068.64 (started 10,000 at 2026-09-16 03:55Z), net +10.69% since start
- 24h -0.50%, 7d -5.53%, 30d +10.69%, max drawdown -12.84%
- fills 189 total, 94 in the last 7d
- costs 436.63 (fees 289.04 + slippage 147.60); gross pnl 1,505.28; cost coverage 3.45
- cash 257.41; positions: ADA 5144.61, AVAX 126.098, BTC 0.0161348, DOGE 11700, DOT 1121.22, ETH 0.510098, LTC 19.7055, SOL 11.4701
- last run 2026-10-05 21:32Z; halted today: False

last decisions (newest last):

- 2026-10-05 20:00Z SOL hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z ADA sell target 0.20 (held 0.25) — replayed after a missed run | stay long: 72h return +11.08% vs exit band -1.0% and price above 24h EMA; realised vol 86% -> weight 0.25
- 2026-10-05 20:00Z AVAX hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z LINK hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z XRP hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z DOGE buy target 0.20 (held 0.00) — replayed after a missed run | enter long: 72h return +4.30% vs entry band +1.0% and price above 24h EMA; realised vol 58% -> weight 0.25
- 2026-10-05 20:00Z DOT sell target 0.20 (held 0.25) — replayed after a missed run | stay long: 72h return +5.85% vs exit band -1.0% and price above 24h EMA; realised vol 91% -> weight 0.25
- 2026-10-05 20:00Z LTC hold target 0.20 (held 0.25) — replayed after a missed run | hold: weight change -0.048 below threshold 0.05 | stay long: 72h return +2.01% vs exit band -1.0% and price...
- 2026-10-05 21:32Z BTC buy target 0.12 (held 0.00) — enter long: 72h return +1.58% vs entry band +1.0% and price above 24h EMA; realised vol 32% -> weight 0.25
- 2026-10-05 21:32Z ETH sell target 0.12 (held 0.25) — stay long: 72h return +1.91% vs exit band -1.0% and price above 24h EMA; realised vol 36% -> weight 0.25
- 2026-10-05 21:32Z SOL buy target 0.12 (held 0.00) — enter long: 72h return +2.45% vs entry band +1.0% and price above 24h EMA; realised vol 49% -> weight 0.25
- 2026-10-05 21:32Z ADA sell target 0.12 (held 0.20) — stay long: 72h return +12.61% vs exit band -1.0% and price above 24h EMA; realised vol 86% -> weight 0.25
- 2026-10-05 21:32Z AVAX buy target 0.12 (held 0.00) — enter long: 72h return +4.07% vs entry band +1.0% and price above 24h EMA; realised vol 85% -> weight 0.25
- 2026-10-05 21:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 21:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 21:32Z DOGE hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 72h return +4.74% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-05 21:32Z DOT sell target 0.12 (held 0.20) — stay long: 72h return +7.79% vs exit band -1.0% and price above 24h EMA; realised vol 91% -> weight 0.25
- 2026-10-05 21:32Z LTC sell target 0.12 (held 0.25) — stay long: 72h return +2.17% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 61% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 20 fills (9 buy / 11 sell), traded 29,223, gross pnl +132.96, +91 bps per round trip, avg half spread 2.2 bps, open 5144.61
- AVAX: 26 fills (11 buy / 15 sell), traded 45,116, gross pnl +535.38, +237 bps per round trip, avg half spread 1.2 bps, open 126.098
- BTC: 13 fills (6 buy / 7 sell), traded 15,471, gross pnl +130.80, +169 bps per round trip, avg half spread 0.2 bps, open 0.0161348
- DOGE: 19 fills (10 buy / 9 sell), traded 26,118, gross pnl -111.27, -85 bps per round trip, avg half spread 1.2 bps, open 11700
- DOT: 22 fills (11 buy / 11 sell), traded 27,712, gross pnl +187.46, +135 bps per round trip, avg half spread 2.6 bps, open 1121.22
- ETH: 15 fills (6 buy / 9 sell), traded 23,751, gross pnl +22.01, +19 bps per round trip, avg half spread 0.1 bps, open 0.510098
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 19 fills (8 buy / 11 sell), traded 31,577, gross pnl +561.73, +356 bps per round trip, avg half spread 2.0 bps, open 19.7055
- SOL: 19 fills (10 buy / 9 sell), traded 30,533, gross pnl +37.60, +25 bps per round trip, avg half spread 0.5 bps, open 11.4701
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-05 20:00Z buy DOGE 1,117 @ 0.0955048 fee 1.12 slip 0.56 (half spread 0.0 bps)
- 2026-10-05 21:32Z sell ETH 1,371 @ 2712.83 fee 1.37 slip 0.69 (half spread 0.3 bps)
- 2026-10-05 21:32Z sell ADA 841 @ 0.269034 fee 0.84 slip 0.42 (half spread 1.5 bps)
- 2026-10-05 21:32Z sell DOT 850 @ 1.23443 fee 0.85 slip 0.43 (half spread 0.4 bps)
- 2026-10-05 21:32Z sell LTC 1,360 @ 70.2249 fee 1.36 slip 0.68 (half spread 2.8 bps)
- 2026-10-05 21:32Z buy BTC 1,385 @ 85851.1 fee 1.39 slip 0.69 (half spread 0.0 bps)
- 2026-10-05 21:32Z buy SOL 1,385 @ 120.765 fee 1.39 slip 0.69 (half spread 0.4 bps)
- 2026-10-05 21:32Z buy AVAX 1,385 @ 10.985 fee 1.39 slip 0.69 (half spread 0.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,397.39 (started 10,000 at 2026-09-16 03:55Z), net +3.97% since start
- 24h +0.00%, 7d +1.05%, 30d +3.97%, max drawdown -1.00%
- fills 10 total, 2 in the last 7d
- costs 38.32 (fees 25.55 + slippage 12.77); gross pnl 435.71; cost coverage 11.37
- cash 10,397.39; positions: none
- last run 2026-10-05 21:32Z; halted today: False

last decisions (newest last):

- 2026-10-05 20:00Z SOL hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z +0.17 not below -2.0
- 2026-10-05 20:00Z ADA hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z +2.08 not below -2.0
- 2026-10-05 20:00Z AVAX hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z -0.26 not below -2.0
- 2026-10-05 20:00Z LINK hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z -0.94 not below -2.0
- 2026-10-05 20:00Z XRP hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z -0.21 not below -2.0
- 2026-10-05 20:00Z DOGE hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z +0.27 not below -2.0
- 2026-10-05 20:00Z DOT hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z +0.27 not below -2.0
- 2026-10-05 20:00Z LTC hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-10-05 21:32Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.42 not below -2.0
- 2026-10-05 21:32Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.96 not below -2.0
- 2026-10-05 21:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.39 not below -2.0
- 2026-10-05 21:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.48 not below -2.0
- 2026-10-05 21:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.14 not below -2.0
- 2026-10-05 21:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.86 not below -2.0
- 2026-10-05 21:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.09 not below -2.0
- 2026-10-05 21:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.41 not below -2.0
- 2026-10-05 21:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.78 not below -2.0
- 2026-10-05 21:32Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.24 not below -2.0

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

- equity 10,950.69 (started 10,000 at 2026-09-16 23:20Z), net +9.51% since start
- 24h -0.31%, 7d -0.14%, 30d +9.51%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,037.87; cost coverage 11.90
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-05 21:32Z; halted today: False

last decisions (newest last):

- 2026-10-05 20:00Z SOL hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 120.3 not above 120h high 123.5
- 2026-10-05 20:00Z ADA hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile ove...
- 2026-10-05 20:00Z AVAX hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile ove...
- 2026-10-05 20:00Z LINK hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile ove...
- 2026-10-05 20:00Z XRP hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.502 not above 120h high 1.542
- 2026-10-05 20:00Z DOGE hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile ove...
- 2026-10-05 20:00Z DOT hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile ove...
- 2026-10-05 20:00Z LTC hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile ove...
- 2026-10-05 21:32Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 8.577e+04 still above 72h low 8.444e+04; realised vol 32% -> weight 0.25
- 2026-10-05 21:32Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 2712 still above 72h low 2661; realised vol 36% -> weight 0.25
- 2026-10-05 21:32Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 120.6 not above 120h high 123.5
- 2026-10-05 21:32Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 21:32Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 21:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 21:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.505 not above 120h high 1.542
- 2026-10-05 21:32Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 21:32Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 21:32Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl +4.60, +11 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -33.05, -82 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 9,986.20 (started 10,000 at 2026-10-05 05:28Z), net -0.14% since start
- 24h -0.10%, 7d -0.10%, 30d -0.10%, max drawdown -1.48%
- fills 16 total, 16 in the last 7d
- costs 37.06 (fees 24.71 + slippage 12.35); gross pnl 23.26; cost coverage 0.63
- cash 232.23; positions: ADA 4641.5, AVAX 113.767, BTC 0.0145569, DOGE 10555.9, DOT 1011.57, ETH 0.460214, LTC 17.7784, SOL 10.3484
- last run 2026-10-05 21:32Z; halted today: False

last decisions (newest last):

- 2026-10-05 20:00Z SOL hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z ADA sell target 0.20 (held 0.25) — replayed after a missed run | stay long: 72h return +11.08% vs exit band -1.0% and price above 24h EMA; realised vol 86% -> weight 0.25
- 2026-10-05 20:00Z AVAX hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z LINK hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z XRP hold target 0.00 (held 0.00) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 20:00Z DOGE buy target 0.20 (held 0.00) — replayed after a missed run | enter long: 72h return +4.30% vs entry band +1.0% and price above 24h EMA; realised vol 58% -> weight 0.25
- 2026-10-05 20:00Z DOT sell target 0.20 (held 0.25) — replayed after a missed run | stay long: 72h return +5.85% vs exit band -1.0% and price above 24h EMA; realised vol 91% -> weight 0.25
- 2026-10-05 20:00Z LTC hold target 0.20 (held 0.25) — replayed after a missed run | hold: weight change -0.048 below threshold 0.05 | stay long: 72h return +2.01% vs exit band -1.0% and price...
- 2026-10-05 21:32Z BTC buy target 0.12 (held 0.00) — enter long: 72h return +1.58% vs entry band +1.0% and price above 24h EMA; realised vol 32% -> weight 0.25
- 2026-10-05 21:32Z ETH sell target 0.12 (held 0.25) — stay long: 72h return +1.91% vs exit band -1.0% and price above 24h EMA; realised vol 36% -> weight 0.25
- 2026-10-05 21:32Z SOL buy target 0.12 (held 0.00) — enter long: 72h return +2.45% vs entry band +1.0% and price above 24h EMA; realised vol 49% -> weight 0.25
- 2026-10-05 21:32Z ADA sell target 0.12 (held 0.20) — stay long: 72h return +12.61% vs exit band -1.0% and price above 24h EMA; realised vol 86% -> weight 0.25
- 2026-10-05 21:32Z AVAX buy target 0.12 (held 0.00) — enter long: 72h return +4.07% vs entry band +1.0% and price above 24h EMA; realised vol 85% -> weight 0.25
- 2026-10-05 21:32Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 21:32Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-10-05 21:32Z DOGE hold target 0.12 (held 0.10) — hold: weight change +0.024 below threshold 0.05 | stay long: 72h return +4.74% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-05 21:32Z DOT sell target 0.12 (held 0.20) — stay long: 72h return +7.79% vs exit band -1.0% and price above 24h EMA; realised vol 91% -> weight 0.25
- 2026-10-05 21:32Z LTC sell target 0.12 (held 0.25) — stay long: 72h return +2.17% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 61% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 3,769, gross pnl +20.21, +107 bps per round trip, avg half spread 1.4 bps, open 4641.5
- AVAX: 1 fills (1 buy / 0 sell), traded 1,250, gross pnl -0.00, -0 bps per round trip, avg half spread 0.5 bps, open 113.767
- BTC: 1 fills (1 buy / 0 sell), traded 1,250, gross pnl -0.00, -0 bps per round trip, avg half spread 0.0 bps, open 0.0145569
- DOGE: 1 fills (1 buy / 0 sell), traded 1,008, gross pnl +2.12, +42 bps per round trip, open 10555.9
- DOT: 3 fills (1 buy / 2 sell), traded 3,748, gross pnl +31.23, +167 bps per round trip, avg half spread 0.4 bps, open 1011.57
- ETH: 2 fills (1 buy / 1 sell), traded 3,721, gross pnl +3.78, +20 bps per round trip, avg half spread 0.3 bps, open 0.460214
- LTC: 4 fills (2 buy / 2 sell), traded 8,716, gross pnl -34.07, -78 bps per round trip, avg half spread 1.8 bps, open 17.7784
- SOL: 1 fills (1 buy / 0 sell), traded 1,250, gross pnl -0.00, -0 bps per round trip, avg half spread 0.4 bps, open 10.3484

last fills:

- 2026-10-05 20:00Z buy DOGE 1,008 @ 0.0955048 fee 1.01 slip 0.50 (half spread 0.0 bps)
- 2026-10-05 21:32Z sell ETH 1,237 @ 2712.83 fee 1.24 slip 0.62 (half spread 0.3 bps)
- 2026-10-05 21:32Z sell ADA 759 @ 0.269034 fee 0.76 slip 0.38 (half spread 1.5 bps)
- 2026-10-05 21:32Z sell DOT 767 @ 1.23443 fee 0.77 slip 0.38 (half spread 0.4 bps)
- 2026-10-05 21:32Z sell LTC 1,227 @ 70.2249 fee 1.23 slip 0.61 (half spread 2.8 bps)
- 2026-10-05 21:32Z buy BTC 1,250 @ 85851.1 fee 1.25 slip 0.62 (half spread 0.0 bps)
- 2026-10-05 21:32Z buy SOL 1,250 @ 120.765 fee 1.25 slip 0.62 (half spread 0.4 bps)
- 2026-10-05 21:32Z buy AVAX 1,250 @ 10.985 fee 1.25 slip 0.62 (half spread 0.5 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,315.13 (started 10,000 at 2026-09-25 04:23Z), net +3.15% since start
- 24h -0.21%, 7d +2.67%, 30d +3.23%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 356.70; cost coverage 8.58
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-05 21:32Z; halted today: False

last decisions (newest last):

- 2026-10-05 20:00Z SOL hold target 0.10 (held 0.10) — replayed after a missed run | hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +16.30% vs exit band -5.0% and pri...
- 2026-10-05 20:00Z ADA hold target 0.10 (held 0.11) — replayed after a missed run | hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +21.22% vs exit band -5.0% and pri...
- 2026-10-05 20:00Z AVAX hold target 0.10 (held 0.09) — replayed after a missed run | hold: weight change +0.009 below threshold 0.05 | stay long: 720h return +43.19% vs exit band -5.0% and pri...
- 2026-10-05 20:00Z LINK hold target 0.10 (held 0.10) — replayed after a missed run | hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +15.88% vs exit band -5.0% and pri...
- 2026-10-05 20:00Z XRP hold target 0.10 (held 0.10) — replayed after a missed run | hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +6.09% vs exit band -5.0% and pric...
- 2026-10-05 20:00Z DOGE hold target 0.10 (held 0.10) — replayed after a missed run | hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +5.10% vs exit band -5.0% and pric...
- 2026-10-05 20:00Z DOT hold target 0.10 (held 0.10) — replayed after a missed run | hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +33.55% vs exit band -5.0% and pri...
- 2026-10-05 20:00Z LTC hold target 0.10 (held 0.10) — replayed after a missed run | hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +29.14% vs exit band -5.0% and pri...
- 2026-10-05 21:32Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +7.55% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 21:32Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +9.46% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 21:32Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +16.82% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 21:32Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +22.93% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 21:32Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +44.74% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 21:32Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +16.02% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 21:32Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +6.37% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 21:32Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +5.47% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 21:32Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +35.00% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 21:32Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +30.22% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +129.74, +647 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +37.32, +823 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +23.33, +449 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -30.02, -582 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +45.64, +299 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +10.59, +204 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +107.50, +530 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -2.06, -10 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +8.13, +67 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +26.54, +87 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1194 candles, 2026-08-17 03:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1194 candles, 2026-08-17 03:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1194 candles, 2026-08-17 03:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1194 candles, 2026-08-17 03:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 1194 candles, 2026-08-17 03:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- LINK: live 1194 candles, 2026-08-17 03:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 1166 candles, 2026-08-18 07:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 1166 candles, 2026-08-18 07:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 1166 candles, 2026-08-18 07:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LTC: live 1166 candles, 2026-08-18 07:00Z to 2026-10-05 20:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
