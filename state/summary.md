# quantloop summary — generated 2026-10-06 07:26Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 20.1 of 60, 39.9 days until the verdict
  so far: champion +10.23% (DD -12.84%, 192 fills) vs challenger1 +4.09% (DD -1.00%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.05% (usual 0.54, this window 0.72) vs challenger1 -5.76% (usual 0.37, this window 0.09); the rule compares on skill, daily edge t -0.2 over 21 days
  market over the window: BTC +12.36%, equal weight basket of 10 pairs +26.54%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 15.0 of 60, 45.0 days until the verdict
  so far: champion -4.06% (DD -12.84%, 154 fills) vs challenger2 -0.44% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.01% (usual 0.54, this window 0.72) vs challenger2 -2.00% (usual 0.29, this window 0.19); the rule compares on skill, daily edge t +0.6 over 15 days
  market over the window: BTC +1.84%, equal weight basket of 10 pairs +5.46%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 0.4 of 60, 59.6 days until the verdict
  so far: champion -0.79% (DD -0.92%, 3 fills) vs challenger3 -0.00% (DD -0.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -0.55% (usual 0.55, this window 0.98) vs challenger3 +0.01% (usual 0.03, this window 0.00); the rule compares on skill
  market over the window: BTC -0.74%, equal weight basket of 10 pairs -0.44%, basket max drawdown -1%, basket realised vol 22% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 10.4 of 60, 49.6 days until the verdict
  so far: champion -9.83% (DD -12.84%, 126 fills) vs challenger4 +0.16% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.70% (usual 0.55, this window 0.69) vs challenger4 +0.27% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.4 over 11 days
  market over the window: BTC +1.46%, equal weight basket of 10 pairs -0.23%, basket max drawdown -5%, basket realised vol 52% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,023.47 (started 10,000 at 2026-09-16 03:55Z), net +10.23% since start
- 24h -0.73%, 7d -5.66%, 30d +10.23%, max drawdown -12.84%
- fills 192 total, 95 in the last 7d
- costs 440.77 (fees 291.79 + slippage 148.98); gross pnl 1,464.24; cost coverage 3.32
- cash 243.13; positions: ADA 5144.61, AVAX 126.098, BTC 0.0161348, DOGE 11700, DOT 1121.22, ETH 0.510098, SOL 11.4701, XRP 917.326
- last run 2026-10-06 07:26Z; halted today: False

last decisions (newest last):

- 2026-10-06 06:30Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.13% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 06:30Z ADA hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +9.12% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-06 06:30Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.004 below threshold 0.05 | stay long: 72h return +3.68% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-06 06:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.42% not above entry band +1.0% and price below 24h EMA
- 2026-10-06 06:30Z XRP hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.95% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 06:30Z DOGE hold target 0.12 (held 0.10) — hold: weight change +0.025 below threshold 0.05 | stay long: 72h return +1.86% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 06:30Z DOT hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +6.78% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-06 06:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.75% not above entry band +1.0% and price below 24h EMA
- 2026-10-06 07:26Z BTC hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.86% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 07:26Z ETH hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.65% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 07:26Z SOL hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.28% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 07:26Z ADA hold target 0.12 (held 0.13) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +9.93% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-06 07:26Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.004 below threshold 0.05 | stay long: 72h return +3.69% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-10-06 07:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.68% not above entry band +1.0% and price below 24h EMA
- 2026-10-06 07:26Z XRP hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.78% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 07:26Z DOGE hold target 0.12 (held 0.10) — hold: weight change +0.025 below threshold 0.05 | stay long: 72h return +1.53% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-06 07:26Z DOT hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +6.82% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-06 07:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.06% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 20 fills (9 buy / 11 sell), traded 29,223, gross pnl +136.85, +94 bps per round trip, avg half spread 2.2 bps, open 5144.61
- AVAX: 26 fills (11 buy / 15 sell), traded 45,116, gross pnl +569.11, +252 bps per round trip, avg half spread 1.2 bps, open 126.098
- BTC: 13 fills (6 buy / 7 sell), traded 15,471, gross pnl +122.52, +158 bps per round trip, avg half spread 0.2 bps, open 0.0161348
- DOGE: 19 fills (10 buy / 9 sell), traded 26,118, gross pnl -125.91, -96 bps per round trip, avg half spread 1.2 bps, open 11700
- DOT: 22 fills (11 buy / 11 sell), traded 27,712, gross pnl +173.00, +125 bps per round trip, avg half spread 2.6 bps, open 1121.22
- ETH: 15 fills (6 buy / 9 sell), traded 23,751, gross pnl +13.39, +11 bps per round trip, avg half spread 0.1 bps, open 0.510098
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 20 fills (8 buy / 12 sell), traded 32,950, gross pnl +550.50, +334 bps per round trip, avg half spread 1.9 bps
- SOL: 19 fills (10 buy / 9 sell), traded 30,533, gross pnl +27.62, +18 bps per round trip, avg half spread 0.5 bps, open 11.4701
- XRP: 16 fills (8 buy / 8 sell), traded 22,497, gross pnl +161.72, +144 bps per round trip, avg half spread 0.5 bps, open 917.326

last fills:

- 2026-10-05 21:32Z sell DOT 850 @ 1.23443 fee 0.85 slip 0.43 (half spread 0.4 bps)
- 2026-10-05 21:32Z sell LTC 1,360 @ 70.2249 fee 1.36 slip 0.68 (half spread 2.8 bps)
- 2026-10-05 21:32Z buy BTC 1,385 @ 85851.1 fee 1.39 slip 0.69 (half spread 0.0 bps)
- 2026-10-05 21:32Z buy SOL 1,385 @ 120.765 fee 1.39 slip 0.69 (half spread 0.4 bps)
- 2026-10-05 21:32Z buy AVAX 1,385 @ 10.985 fee 1.39 slip 0.69 (half spread 0.5 bps)
- 2026-10-05 22:23Z buy XRP 257 @ 1.5146 fee 0.26 slip 0.13 (half spread 0.2 bps)
- 2026-10-06 01:25Z sell LTC 1,373 @ 69.6552 fee 1.37 slip 0.69 (half spread 1.4 bps)
- 2026-10-06 01:25Z buy XRP 1,127 @ 1.50756 fee 1.13 slip 0.56 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,397.39 (started 10,000 at 2026-09-16 03:55Z), net +3.97% since start
- 24h +0.00%, 7d +1.05%, 30d +3.97%, max drawdown -1.00%
- fills 10 total, 2 in the last 7d
- costs 38.32 (fees 25.55 + slippage 12.77); gross pnl 435.71; cost coverage 11.37
- cash 10,397.39; positions: none
- last run 2026-10-06 07:26Z; halted today: False

last decisions (newest last):

- 2026-10-06 06:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.13 not below -2.0
- 2026-10-06 06:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.11 not below -2.0
- 2026-10-06 06:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.26 not below -2.0
- 2026-10-06 06:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.17 not below -2.0
- 2026-10-06 06:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-10-06 06:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.08 not below -2.0
- 2026-10-06 06:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-10-06 06:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.00 not below -2.0
- 2026-10-06 07:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.81 not below -2.0
- 2026-10-06 07:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.17 not below -2.0
- 2026-10-06 07:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.13 not below -2.0
- 2026-10-06 07:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.24 not below -2.0
- 2026-10-06 07:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-10-06 07:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.13 not below -2.0
- 2026-10-06 07:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.39 not below -2.0
- 2026-10-06 07:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-10-06 07:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.78 not below -2.0
- 2026-10-06 07:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.06 not below -2.0

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

- equity 10,917.32 (started 10,000 at 2026-09-16 23:20Z), net +9.17% since start
- 24h -0.48%, 7d -0.44%, 30d +9.17%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,004.50; cost coverage 11.52
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-06 07:26Z; halted today: False

last decisions (newest last):

- 2026-10-06 06:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 119.8 not above 120h high 123.5
- 2026-10-06 06:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 06:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 06:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 06:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.499 not above 120h high 1.542
- 2026-10-06 06:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 06:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 06:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 07:26Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 8.529e+04 still above 72h low 8.454e+04; realised vol 32% -> weight 0.25
- 2026-10-06 07:26Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 2697 still above 72h low 2680; realised vol 35% -> weight 0.25
- 2026-10-06 07:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 119.8 not above 120h high 123.5
- 2026-10-06 07:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 07:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 07:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 07:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.497 not above 120h high 1.542
- 2026-10-06 07:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 07:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-06 07:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -11.86, -29 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -49.95, -123 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,010.49 (started 10,000 at 2026-10-05 05:28Z), net +0.10% since start
- 24h -0.29%, 7d +0.14%, 30d +0.14%, max drawdown -1.48%
- fills 24 total, 24 in the last 7d
- costs 51.81 (fees 34.50 + slippage 17.31); gross pnl 62.30; cost coverage 1.20
- cash 10,010.49; positions: none
- last run 2026-10-06 07:26Z; halted today: False

last decisions (newest last):

- 2026-10-06 06:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 119.8 not a fresh close above reaction high 124.4
- 2026-10-06 06:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2684 not a fresh close above reaction high 0.2616
- 2026-10-06 06:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.29 not a fresh close above reaction high 11.55
- 2026-10-06 06:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.82 not a fresh close above reaction high 15.46
- 2026-10-06 06:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.499 not a fresh close above reaction high 1.638
- 2026-10-06 06:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.0947 not a fresh close above reaction high 0.1039
- 2026-10-06 06:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.231 not a fresh close above reaction high 1.301
- 2026-10-06 06:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 69.63 not a fresh close above reaction high 74.29
- 2026-10-06 07:26Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.556e+04 (need +10.0%)
- 2026-10-06 07:26Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 2697 not a fresh close above reaction high 2784
- 2026-10-06 07:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 119.8 not a fresh close above reaction high 124.4
- 2026-10-06 07:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2698 not a fresh close above reaction high 0.2616
- 2026-10-06 07:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.29 not a fresh close above reaction high 11.55
- 2026-10-06 07:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.84 not a fresh close above reaction high 15.46
- 2026-10-06 07:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.497 not a fresh close above reaction high 1.638
- 2026-10-06 07:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09436 not a fresh close above reaction high 0.1039
- 2026-10-06 07:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.232 not a fresh close above reaction high 1.301
- 2026-10-06 07:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 69.5 not a fresh close above reaction high 74.29

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +8.02, +64 bps per round trip, avg half spread 0.7 bps
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell BTC 1,250 @ 85884.1 fee 1.25 slip 0.63 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell ETH 1,250 @ 2715.8 fee 1.25 slip 0.63 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,269.52 (started 10,000 at 2026-09-25 04:23Z), net +2.70% since start
- 24h -1.06%, 7d -0.42%, 30d +2.77%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 311.09; cost coverage 7.48
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-06 07:26Z; halted today: False

last decisions (newest last):

- 2026-10-06 06:30Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +12.56% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-06 06:30Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +21.23% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 06:30Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +46.83% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 06:30Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +12.47% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-06 06:30Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +5.25% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-06 06:30Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +3.50% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-06 06:30Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +32.19% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 06:30Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +28.21% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 07:26Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +6.92% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-06 07:26Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +7.62% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-06 07:26Z SOL hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +13.66% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-06 07:26Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +22.52% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 07:26Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.006 below threshold 0.05 | stay long: 720h return +47.34% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 07:26Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +12.90% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-06 07:26Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +5.52% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-06 07:26Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +3.54% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-06 07:26Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +31.06% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-06 07:26Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +28.09% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +132.81, +662 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +60.32, +1330 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +16.98, +327 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -43.10, -836 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +34.46, +226 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +4.05, +78 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +99.47, +491 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -14.65, -74 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +0.70, +6 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +20.06, +66 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1204 candles, 2026-08-17 03:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1204 candles, 2026-08-17 03:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1204 candles, 2026-08-17 03:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1204 candles, 2026-08-17 03:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 1204 candles, 2026-08-17 03:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- LINK: live 1204 candles, 2026-08-17 03:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- XRP: live 1176 candles, 2026-08-18 07:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 1176 candles, 2026-08-18 07:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 1176 candles, 2026-08-18 07:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LTC: live 1176 candles, 2026-08-18 07:00Z to 2026-10-06 06:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
