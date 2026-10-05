# quantloop summary — generated 2026-10-05 18:30Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 22 of the last 24, 141 of the last 168
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 19.5 of 60, 40.5 days until the verdict
  so far: champion +10.23% (DD -12.84%, 177 fills) vs challenger1 +4.09% (DD -1.00%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.57% (usual 0.54, this window 0.71) vs challenger1 -5.43% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.2 over 20 days
  market over the window: BTC +12.54%, equal weight basket of 10 pairs +25.66%, basket max drawdown -7%, basket realised vol 57% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 14.4 of 60, 45.6 days until the verdict
  so far: champion -4.06% (DD -12.84%, 139 fills) vs challenger2 -0.27% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.67% (usual 0.54, this window 0.71) vs challenger2 -1.65% (usual 0.29, this window 0.17); the rule compares on skill, daily edge t +0.6 over 15 days
  market over the window: BTC +2.00%, equal weight basket of 10 pairs +4.84%, basket max drawdown -7%, basket realised vol 57% annualised
- challenger3: idle (free for a hypothesis)
- challenger4: testing H4 since 2026-09-25 22:21Z, day 9.8 of 60, 50.2 days until the verdict
  so far: champion -9.83% (DD -12.84%, 111 fills) vs challenger4 -0.16% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.35% (usual 0.55, this window 0.67) vs challenger4 +0.26% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.4 over 10 days
  market over the window: BTC +1.62%, equal weight basket of 10 pairs -0.88%, basket max drawdown -5%, basket realised vol 53% annualised
- free slots: challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,023.45 (started 10,000 at 2026-09-16 03:55Z), net +10.23% since start
- 24h -0.15%, 7d -5.92%, 30d +10.23%, max drawdown -12.84%
- fills 177 total, 82 in the last 7d
- costs 412.17 (fees 272.72 + slippage 139.44); gross pnl 1,435.62; cost coverage 3.48
- cash 5,521.91; positions: ADA 10369.5, LTC 39.0687
- last run 2026-10-05 18:30Z; halted today: False

last decisions (newest last):

- 2026-10-05 17:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.30% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +4.90% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-05 17:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.38% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.75% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.53% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.99% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.83% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.78% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.80% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.28% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +5.69% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-05 18:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.55% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.84% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.10% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.22% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.31% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z LTC buy target 0.25 (held 0.00) — enter long: 72h return +1.41% vs entry band +1.0% and price above 24h EMA; realised vol 61% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 18 fills (9 buy / 9 sell), traded 27,823, gross pnl +93.91, +68 bps per round trip, avg half spread 2.2 bps, open 10369.5
- AVAX: 25 fills (10 buy / 15 sell), traded 43,731, gross pnl +535.38, +245 bps per round trip, avg half spread 1.3 bps
- BTC: 12 fills (5 buy / 7 sell), traded 14,086, gross pnl +130.80, +186 bps per round trip, avg half spread 0.2 bps
- DOGE: 18 fills (9 buy / 9 sell), traded 25,001, gross pnl -113.62, -91 bps per round trip, avg half spread 1.2 bps
- DOT: 19 fills (10 buy / 9 sell), traded 23,558, gross pnl +152.85, +130 bps per round trip, avg half spread 2.7 bps
- ETH: 13 fills (5 buy / 8 sell), traded 19,627, gross pnl +17.81, +18 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 18 fills (8 buy / 10 sell), traded 30,218, gross pnl +572.28, +379 bps per round trip, avg half spread 1.9 bps, open 39.0687
- SOL: 18 fills (9 buy / 9 sell), traded 29,148, gross pnl +37.60, +26 bps per round trip, avg half spread 0.5 bps
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-05 05:28Z sell SOL 1,561 @ 120.075 fee 1.56 slip 0.78 (half spread 0.4 bps)
- 2026-10-05 05:28Z sell AVAX 1,556 @ 10.8821 fee 1.56 slip 0.78 (half spread 1.4 bps)
- 2026-10-05 05:28Z sell DOGE 1,390 @ 0.0950154 fee 1.39 slip 0.70 (half spread 0.1 bps)
- 2026-10-05 05:28Z sell DOT 1,743 @ 1.20735 fee 1.74 slip 0.87 (half spread 2.1 bps)
- 2026-10-05 05:28Z buy ADA 1,092 @ 0.266556 fee 1.09 slip 0.55 (half spread 1.2 bps)
- 2026-10-05 05:28Z buy LTC 1,206 @ 69.6898 fee 1.21 slip 0.60 (half spread 0.7 bps)
- 2026-10-05 16:27Z sell LTC 2,772 @ 69.89 fee 2.77 slip 1.39 (half spread 2.1 bps)
- 2026-10-05 18:30Z buy LTC 2,757 @ 70.5653 fee 2.76 slip 1.38 (half spread 1.4 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,397.39 (started 10,000 at 2026-09-16 03:55Z), net +3.97% since start
- 24h +0.00%, 7d +1.05%, 30d +3.97%, max drawdown -1.00%
- fills 10 total, 2 in the last 7d
- costs 38.32 (fees 25.55 + slippage 12.77); gross pnl 435.71; cost coverage 11.37
- cash 10,397.39; positions: none
- last run 2026-10-05 18:30Z; halted today: False

last decisions (newest last):

- 2026-10-05 17:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-10-05 17:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.97 not below -2.0
- 2026-10-05 17:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.09 not below -2.0
- 2026-10-05 17:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.16 not below -2.0
- 2026-10-05 17:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.70 not below -2.0
- 2026-10-05 17:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-10-05 17:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.43 not below -2.0
- 2026-10-05 17:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0
- 2026-10-05 18:30Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.09 not below -2.0
- 2026-10-05 18:30Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.63 not below -2.0
- 2026-10-05 18:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.02 not below -2.0
- 2026-10-05 18:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.89 not below -2.0
- 2026-10-05 18:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-10-05 18:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.05 not below -2.0
- 2026-10-05 18:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.50 not below -2.0
- 2026-10-05 18:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.17 not below -2.0
- 2026-10-05 18:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.54 not below -2.0
- 2026-10-05 18:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.52 not below -2.0

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

- equity 10,936.45 (started 10,000 at 2026-09-16 23:20Z), net +9.36% since start
- 24h -0.03%, 7d -0.27%, 30d +9.36%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,023.64; cost coverage 11.74
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-05 18:30Z; halted today: False

last decisions (newest last):

- 2026-10-05 17:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 17:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 17:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 17:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 17:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.492 not above 120h high 1.542
- 2026-10-05 17:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 17:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 17:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 8.542e+04 still above 72h low 8.424e+04; realised vol 33% -> weight 0.25
- 2026-10-05 18:30Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 2705 still above 72h low 2661; realised vol 37% -> weight 0.25
- 2026-10-05 18:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.496 not above 120h high 1.542
- 2026-10-05 18:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-05 18:30Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -3.77, -9 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -38.91, -96 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 9,945.40 (started 10,000 at 2026-10-05 05:28Z), net -0.55% since start
- 24h -0.51%, 7d -0.51%, 30d -0.51%, max drawdown -1.48%
- fills 4 total, 4 in the last 7d
- costs 14.98 (fees 9.99 + slippage 4.99); gross pnl -39.62; cost coverage -2.64
- cash 4,975.67; positions: ADA 9378.9, LTC 35.248
- last run 2026-10-05 18:30Z; halted today: False

last decisions (newest last):

- 2026-10-05 17:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.30% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +4.90% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-05 17:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.38% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.75% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.53% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.99% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 17:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.83% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.78% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.80% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.28% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +5.69% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-05 18:30Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.55% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.84% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.10% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.22% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.31% not above entry band +1.0% and price below 24h EMA
- 2026-10-05 18:30Z LTC buy target 0.25 (held 0.00) — enter long: 72h return +1.41% vs entry band +1.0% and price above 24h EMA; realised vol 61% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -15.06, -120 bps per round trip, avg half spread 1.2 bps, open 9378.9
- LTC: 3 fills (2 buy / 1 sell), traded 7,489, gross pnl -24.56, -66 bps per round trip, avg half spread 1.4 bps, open 35.248

last fills:

- 2026-10-05 05:28Z buy ADA 2,500 @ 0.266556 fee 2.50 slip 1.25 (half spread 1.2 bps)
- 2026-10-05 11:25Z buy LTC 2,514 @ 70.6503 fee 2.51 slip 1.26 (half spread 0.7 bps)
- 2026-10-05 16:27Z sell LTC 2,487 @ 69.89 fee 2.49 slip 1.24 (half spread 2.1 bps)
- 2026-10-05 18:30Z buy LTC 2,487 @ 70.5653 fee 2.49 slip 1.24 (half spread 1.4 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,237.56 (started 10,000 at 2026-09-25 04:23Z), net +2.38% since start
- 24h -0.21%, 7d +1.29%, 30d +2.45%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 279.13; cost coverage 6.71
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-05 18:30Z; halted today: False

last decisions (newest last):

- 2026-10-05 17:24Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +15.62% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 17:24Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +21.43% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 17:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +44.32% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 17:24Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +15.57% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 17:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +5.38% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-05 17:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +7.35% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 17:24Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +31.24% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 17:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.000 below threshold 0.05 | stay long: 720h return +29.55% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 18:30Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +6.69% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 18:30Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +9.02% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 18:30Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +15.07% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 18:30Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +19.38% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-05 18:30Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.009 below threshold 0.05 | stay long: 720h return +42.69% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 18:30Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +14.63% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 18:30Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +4.89% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-05 18:30Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +0.84% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-05 18:30Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +30.61% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-05 18:30Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +28.65% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +112.04, +558 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +29.11, +642 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +20.10, +387 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -39.26, -762 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +19.12, +125 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +8.32, +160 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +103.22, +509 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +1.83, +9 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +2.33, +19 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +22.32, +73 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1191 candles, 2026-08-17 03:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1191 candles, 2026-08-17 03:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1191 candles, 2026-08-17 03:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1191 candles, 2026-08-17 03:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 1191 candles, 2026-08-17 03:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.1 bps
- LINK: live 1191 candles, 2026-08-17 03:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- XRP: live 1163 candles, 2026-08-18 07:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 1163 candles, 2026-08-18 07:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- DOT: live 1163 candles, 2026-08-18 07:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 2.2 bps
- LTC: live 1163 candles, 2026-08-18 07:00Z to 2026-10-05 17:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
