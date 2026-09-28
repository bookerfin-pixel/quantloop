# quantloop summary — generated 2026-09-28 06:31Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 12.0 of 60, 48.0 days until the verdict
  so far: champion +19.54% (DD -6.75%, 86 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +6.56% (usual 0.54, this window 0.78) vs challenger1 -5.94% (usual 0.37, this window 0.13); the rule compares on skill, daily edge t -1.3 over 13 days
  market over the window: BTC +9.57%, equal weight basket of 10 pairs +24.12%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 6.9 of 60, 53.1 days until the verdict
  so far: champion +4.04% (DD -6.75%, 48 fills) vs challenger2 +0.00% (DD 0.00%, 0 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +2.11% (usual 0.54, this window 0.85) vs challenger2 -1.02% (usual 0.29, this window 0.00); the rule compares on skill, daily edge t -0.5 over 7 days
  market over the window: BTC -0.69%, equal weight basket of 10 pairs +3.57%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 3.1 of 60, 56.9 days until the verdict
  so far: champion +0.73% (DD -4.42%, 28 fills) vs challenger3 -0.65% (DD -1.24%, 5 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +0.10% (usual 0.55, this window 0.96) vs challenger3 -0.72% (usual 0.05, this window 0.06); the rule compares on skill, daily edge t -0.2 over 4 days
  market over the window: BTC -1.24%, equal weight basket of 10 pairs +1.17%, basket max drawdown -3%, basket realised vol 48% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 2.3 of 60, 57.7 days until the verdict
  so far: champion -2.22% (DD -4.42%, 20 fills) vs challenger4 -1.96% (DD -3.64%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -1.06% (usual 0.55, this window 0.95) vs challenger4 -0.95% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +0.2 over 3 days
  market over the window: BTC -1.06%, equal weight basket of 10 pairs -2.11%, basket max drawdown -3%, basket realised vol 45% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,953.86 (started 10,000 at 2026-09-16 03:55Z), net +19.54% since start
- 24h -3.58%, 7d +4.63%, 30d +19.54%, max drawdown -6.75%
- fills 86 total, 48 in the last 7d
- costs 187.23 (fees 123.80 + slippage 63.43); gross pnl 2,141.09; cost coverage 11.44
- cash 4,746.13; positions: DOT 1961.34, LINK 173.707, SOL 20.2823
- last run 2026-09-28 06:31Z; halted today: False

last decisions (newest last):

- 2026-09-28 05:24Z SOL hold target 0.20 (held 0.20) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +3.08% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 05:24Z ADA hold target 0.20 (held 0.20) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +0.62% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 05:24Z AVAX hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +4.39% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 05:24Z LINK hold target 0.20 (held 0.20) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +4.42% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.38% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 05:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.75% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 05:24Z DOT hold target 0.20 (held 0.20) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +9.37% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-09-28 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.21% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 06:31Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.20% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 06:31Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.06% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 06:31Z SOL hold target 0.25 (held 0.20) — hold: weight change +0.049 below threshold 0.05 | stay long: 72h return +2.29% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 06:31Z ADA sell target 0.00 (held 0.20) — exit: price more than 2.0% below 24h EMA
- 2026-09-28 06:31Z AVAX sell target 0.00 (held 0.20) — exit: price more than 2.0% below 24h EMA
- 2026-09-28 06:31Z LINK hold target 0.25 (held 0.20) — hold: weight change +0.049 below threshold 0.05 | stay long: 72h return +3.14% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 06:31Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.90% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 06:31Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.87% not above entry band +1.0% and price below 24h EMA
- 2026-09-28 06:31Z DOT hold target 0.25 (held 0.20) — hold: weight change +0.049 below threshold 0.05 | stay long: 72h return +8.02% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-28 06:31Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.00% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (5 buy / 6 sell), traded 18,727, gross pnl +101.44, +108 bps per round trip, avg half spread 2.4 bps
- AVAX: 11 fills (5 buy / 6 sell), traded 18,801, gross pnl +665.50, +708 bps per round trip, avg half spread 1.1 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 15,017, gross pnl -37.42, -50 bps per round trip, avg half spread 1.7 bps
- DOT: 10 fills (6 buy / 4 sell), traded 9,681, gross pnl +290.94, +601 bps per round trip, avg half spread 3.4 bps, open 1961.34
- ETH: 4 fills (2 buy / 2 sell), traded 5,420, gross pnl +48.83, +180 bps per round trip, avg half spread 0.2 bps
- LINK: 10 fills (5 buy / 5 sell), traded 12,080, gross pnl +198.66, +329 bps per round trip, avg half spread 2.4 bps, open 173.707
- LTC: 9 fills (3 buy / 6 sell), traded 13,674, gross pnl +599.56, +877 bps per round trip, avg half spread 2.1 bps
- SOL: 8 fills (5 buy / 3 sell), traded 10,311, gross pnl +39.22, +76 bps per round trip, avg half spread 0.5 bps, open 20.2823
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-28 03:24Z sell DOGE 1,721 @ 0.0946707 fee 1.72 slip 0.86 (half spread 0.0 bps)
- 2026-09-28 03:24Z buy SOL 642 @ 120.1 fee 0.64 slip 0.32 (half spread 0.8 bps)
- 2026-09-28 03:24Z buy ADA 660 @ 0.252543 fee 0.66 slip 0.33 (half spread 2.8 bps)
- 2026-09-28 03:24Z buy AVAX 846 @ 10.7839 fee 0.85 slip 0.42 (half spread 0.5 bps)
- 2026-09-28 03:24Z buy LINK 667 @ 14.0236 fee 0.67 slip 0.37 (half spread 3.6 bps)
- 2026-09-28 03:24Z buy DOT 658 @ 1.23887 fee 0.66 slip 0.33 (half spread 2.8 bps)
- 2026-09-28 06:31Z sell ADA 2,368 @ 0.245465 fee 2.37 slip 1.18 (half spread 1.9 bps)
- 2026-09-28 06:31Z sell AVAX 2,383 @ 10.5512 fee 2.38 slip 1.19 (half spread 0.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-28 06:31Z; halted today: False

last decisions (newest last):

- 2026-09-28 05:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.85 not below -2.0
- 2026-09-28 05:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.58 not below -2.0
- 2026-09-28 05:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.36 not below -2.0
- 2026-09-28 05:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.22 not below -2.0
- 2026-09-28 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.05 not below -2.0
- 2026-09-28 05:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.09 not below -2.0
- 2026-09-28 05:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.63 not below -2.0
- 2026-09-28 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.08 not below -2.0
- 2026-09-28 06:31Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.17 not below -2.0
- 2026-09-28 06:31Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-09-28 06:31Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.66 not below -2.0
- 2026-09-28 06:31Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.38 not below -2.0
- 2026-09-28 06:31Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.28 not below -2.0
- 2026-09-28 06:31Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.09 not below -2.0
- 2026-09-28 06:31Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.13 not below -2.0
- 2026-09-28 06:31Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.13 not below -2.0
- 2026-09-28 06:31Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.37 not below -2.0
- 2026-09-28 06:31Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.11 not below -2.0

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
- last run 2026-09-28 06:31Z; halted today: False

last decisions (newest last):

- 2026-09-28 05:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 2651 not above 120h high 2757
- 2026-09-28 06:31Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-28 06:31Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

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

- equity 11,437.14 (started 10,000 at 2026-09-16 23:20Z), net +14.37% since start
- 24h -0.65%, 7d +0.11%, 30d +14.37%, max drawdown -7.05%
- fills 54 total, 16 in the last 7d
- costs 122.98 (fees 80.99 + slippage 41.99); gross pnl 1,560.12; cost coverage 12.69
- cash 8,584.56; positions: DOT 2325.6
- last run 2026-09-28 06:31Z; halted today: False

last decisions (newest last):

- 2026-09-28 05:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 105.3 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-28 05:24Z ADA buy target 0.25 (held 0.00) — enter long: higher low 0.2122 vs prior low 0.191 (+11.1%) then broke above the reaction high 0.2163 at 0.2495; realised vol 79% -> weight...
- 2026-09-28 05:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.869 not a higher low vs prior low 7.197 (need +10.0%)
- 2026-09-28 05:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.72 not a higher low vs prior low 10.66 (need +10.0%)
- 2026-09-28 05:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.317 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-28 05:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08409 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-28 05:24Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 1.25 still above the 48h low 1.204; realised vol 94% -> weight 0.25
- 2026-09-28 05:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 54.75 not a higher low vs prior low 50.28 (need +10.0%)
- 2026-09-28 06:31Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.743e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-28 06:31Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2478 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-28 06:31Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 105.3 not a higher low vs prior low 96.43 (need +10.0%)
- 2026-09-28 06:31Z ADA sell target 0.00 (held 0.25) — exit: closed 0.2469 below the 48h low 0.2495
- 2026-09-28 06:31Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.869 not a higher low vs prior low 7.197 (need +10.0%)
- 2026-09-28 06:31Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 11.72 not a higher low vs prior low 10.66 (need +10.0%)
- 2026-09-28 06:31Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.317 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-28 06:31Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08409 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-28 06:31Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 1.238 still above the 48h low 1.204; realised vol 95% -> weight 0.25
- 2026-09-28 06:31Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 54.81 not a higher low vs prior low 50.28 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 9 fills (4 buy / 5 sell), traded 19,233, gross pnl +86.79, +90 bps per round trip, avg half spread 2.3 bps
- AVAX: 8 fills (3 buy / 5 sell), traded 13,906, gross pnl +728.79, +1048 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 6 fills (3 buy / 3 sell), traded 8,299, gross pnl +183.56, +442 bps per round trip, avg half spread 3.1 bps, open 2325.6
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 4 fills (2 buy / 2 sell), traded 5,855, gross pnl +90.07, +308 bps per round trip, avg half spread 2.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 7,523, gross pnl +177.57, +472 bps per round trip, avg half spread 2.3 bps
- SOL: 4 fills (2 buy / 2 sell), traded 5,298, gross pnl +79.10, +299 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-23 14:23Z sell XRP 1,531 @ 1.51841 fee 1.53 slip 0.77 (half spread 1.9 bps)
- 2026-09-23 14:23Z sell DOGE 1,415 @ 0.0938014 fee 1.42 slip 1.32 (half spread 7.3 bps)
- 2026-09-23 14:23Z sell LTC 1,466 @ 60.04 fee 1.47 slip 0.73 (half spread 1.7 bps)
- 2026-09-27 14:20Z buy DOT 2,878 @ 1.23757 fee 2.88 slip 1.44 (half spread 0.4 bps)
- 2026-09-28 03:24Z buy ADA 2,878 @ 0.252543 fee 2.88 slip 1.44 (half spread 2.8 bps)
- 2026-09-28 04:24Z sell ADA 2,853 @ 0.250408 fee 2.85 slip 1.43 (half spread 0.0 bps)
- 2026-09-28 05:24Z buy ADA 2,865 @ 0.246416 fee 2.87 slip 1.61 (half spread 3.6 bps)
- 2026-09-28 06:31Z sell ADA 2,854 @ 0.245465 fee 2.85 slip 1.43 (half spread 1.9 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,053.02 (started 10,000 at 2026-09-25 04:23Z), net +0.53% since start
- 24h -2.90%, 7d +0.61%, 30d +0.61%, max drawdown -3.64%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 94.59; cost coverage 2.28
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-28 06:31Z; halted today: False

last decisions (newest last):

- 2026-09-28 05:24Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +15.48% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 05:24Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +24.01% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 05:24Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.010 below threshold 0.05 | stay long: 720h return +46.35% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 05:24Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +22.90% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 05:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.89% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 05:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +10.83% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-28 05:24Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +48.16% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 05:24Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +44.39% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 06:31Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +7.13% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 06:31Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +8.69% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 06:31Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +14.50% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 06:31Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +22.61% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 06:31Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.010 below threshold 0.05 | stay long: 720h return +45.37% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 06:31Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +21.83% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 06:31Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +6.79% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 06:31Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +9.73% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-28 06:31Z DOT hold target 0.10 (held 0.11) — hold: weight change -0.006 below threshold 0.05 | stay long: 720h return +46.74% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-28 06:31Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +44.69% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +33.86, +169 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +0.95, +21 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -10.40, -200 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -57.79, -1121 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +38.32, +251 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -14.94, -287 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +96.89, +478 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +8.30, +42 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -10.56, -88 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +9.97, +33 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1011 candles, 2026-08-17 03:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1011 candles, 2026-08-17 03:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1011 candles, 2026-08-17 03:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1011 candles, 2026-08-17 03:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.9 bps
- AVAX: live 1011 candles, 2026-08-17 03:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1011 candles, 2026-08-17 03:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 983 candles, 2026-08-18 07:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 983 candles, 2026-08-18 07:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.8 bps
- DOT: live 983 candles, 2026-08-18 07:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 983 candles, 2026-08-18 07:00Z to 2026-09-28 05:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.9 bps
