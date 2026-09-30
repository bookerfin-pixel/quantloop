# quantloop summary — generated 2026-09-30 08:27Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 14.1 of 60, 45.9 days until the verdict
  so far: champion +14.33% (DD -8.58%, 100 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion +1.39% (usual 0.54, this window 0.72) vs challenger1 -5.91% (usual 0.37, this window 0.11); the rule compares on skill, daily edge t -0.7 over 15 days
  market over the window: BTC +9.69%, equal weight basket of 10 pairs +24.05%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 9.0 of 60, 51.0 days until the verdict
  so far: champion -0.49% (DD -8.58%, 62 fills) vs challenger2 -0.67% (DD -0.70%, 1 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.33% (usual 0.54, this window 0.73) vs challenger2 -1.65% (usual 0.29, this window 0.02); the rule compares on skill, daily edge t +0.1 over 10 days
  market over the window: BTC -0.58%, equal weight basket of 10 pairs +3.41%, basket max drawdown -7%, basket realised vol 61% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 5.2 of 60, 54.8 days until the verdict
  so far: champion -3.65% (DD -8.58%, 42 fills) vs challenger3 -2.13% (DD -4.74%, 79 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -4.27% (usual 0.55, this window 0.71) vs challenger3 -2.19% (usual 0.05, this window 0.41); the rule compares on skill, daily edge t +0.4 over 6 days
  market over the window: BTC -1.13%, equal weight basket of 10 pairs +1.13%, basket max drawdown -5%, basket realised vol 58% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 4.4 of 60, 55.6 days until the verdict
  so far: champion -6.48% (DD -8.58%, 34 fills) vs challenger4 -1.70% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.31% (usual 0.55, this window 0.66) vs challenger4 -0.68% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +1.5 over 5 days
  market over the window: BTC -0.96%, equal weight basket of 10 pairs -2.13%, basket max drawdown -5%, basket realised vol 59% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,433.47 (started 10,000 at 2026-09-16 03:55Z), net +14.33% since start
- 24h -2.38%, 7d -5.01%, 30d +14.33%, max drawdown -8.58%
- fills 100 total, 59 in the last 7d
- costs 241.98 (fees 159.44 + slippage 82.53); gross pnl 1,675.45; cost coverage 6.92
- cash 8,555.84; positions: AVAX 259.561
- last run 2026-09-30 08:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 07:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.69% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 07:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.92% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 07:27Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +1.50% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-30 07:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.07% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 07:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.92% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 07:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.09% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 07:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.78% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 07:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.48% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.78% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.62% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.57% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.20% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return -0.46% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-30 08:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.97% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.51% not above entry band +1.0%
- 2026-09-30 08:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.47% not above entry band +1.0% and price below 24h EMA
- 2026-09-30 08:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.52% not above entry band +1.0%
- 2026-09-30 08:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -7.24% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (5 buy / 6 sell), traded 18,727, gross pnl +101.44, +108 bps per round trip, avg half spread 2.4 bps
- AVAX: 12 fills (6 buy / 6 sell), traded 21,710, gross pnl +635.91, +586 bps per round trip, avg half spread 1.3 bps, open 259.561
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 15,017, gross pnl -37.42, -50 bps per round trip, avg half spread 1.7 bps
- DOT: 12 fills (7 buy / 5 sell), traded 13,246, gross pnl +261.75, +395 bps per round trip, avg half spread 3.1 bps
- ETH: 6 fills (3 buy / 3 sell), traded 11,261, gross pnl +3.43, +6 bps per round trip, avg half spread 0.1 bps
- LINK: 16 fills (8 buy / 8 sell), traded 27,177, gross pnl -50.81, -37 bps per round trip, avg half spread 2.6 bps
- LTC: 11 fills (4 buy / 7 sell), traded 19,507, gross pnl +493.24, +506 bps per round trip, avg half spread 2.0 bps
- SOL: 9 fills (5 buy / 4 sell), traded 12,708, gross pnl +33.54, +53 bps per round trip, avg half spread 0.5 bps
- XRP: 9 fills (4 buy / 5 sell), traded 14,637, gross pnl +174.70, +239 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-28 13:25Z buy LINK 2,952 @ 14.5956 fee 2.95 slip 1.48 (half spread 2.3 bps)
- 2026-09-28 14:27Z sell LINK 2,906 @ 14.3673 fee 2.91 slip 2.00 (half spread 4.9 bps)
- 2026-09-28 14:27Z sell LTC 2,862 @ 69.5802 fee 2.86 slip 1.43 (half spread 2.2 bps)
- 2026-09-29 00:29Z buy LINK 2,929 @ 15.6096 fee 2.93 slip 1.56 (half spread 3.3 bps)
- 2026-09-29 07:25Z buy AVAX 2,909 @ 11.2072 fee 2.91 slip 1.75 (half spread 4.0 bps)
- 2026-09-29 10:25Z buy ETH 2,945 @ 2714.73 fee 2.94 slip 1.47 (half spread 0.0 bps)
- 2026-09-29 18:28Z sell LINK 2,740 @ 14.6027 fee 2.74 slip 1.37 (half spread 0.0 bps)
- 2026-09-30 02:22Z sell ETH 2,896 @ 2670.19 fee 2.90 slip 1.45 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-30 08:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 07:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.08 not below -2.0
- 2026-09-30 07:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-09-30 07:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.74 not below -2.0
- 2026-09-30 07:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.84 not below -2.0
- 2026-09-30 07:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-09-30 07:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.60 not below -2.0
- 2026-09-30 07:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.23 not below -2.0
- 2026-09-30 07:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.02 not below -2.0
- 2026-09-30 08:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.60 not below -2.0
- 2026-09-30 08:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.47 not below -2.0
- 2026-09-30 08:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.17 not below -2.0
- 2026-09-30 08:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.24 not below -2.0
- 2026-09-30 08:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-09-30 08:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.82 not below -2.0
- 2026-09-30 08:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-09-30 08:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-09-30 08:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.45 not below -2.0
- 2026-09-30 08:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.03 not below -2.0

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

- equity 10,892.11 (started 10,000 at 2026-09-16 23:20Z), net +8.92% since start
- 24h -0.67%, 7d -0.67%, 30d +8.92%, max drawdown -3.54%
- fills 33 total, 1 in the last 7d
- costs 83.08 (fees 54.95 + slippage 28.13); gross pnl 975.19; cost coverage 11.74
- cash 8,221.54; positions: ETH 1.00083
- last run 2026-09-30 08:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 07:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 07:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 8.326e+04 not above 120h high 8.502e+04
- 2026-09-30 08:27Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: price 2674 still above 72h low 2640; realised vol 36% -> weight 0.25
- 2026-09-30 08:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-09-30 08:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 3 fills (2 buy / 1 sell), traded 5,380, gross pnl -12.20, -45 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -78.93, -195 bps per round trip, avg half spread 0.0 bps, open 1.00083
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)
- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)

## challenger3: swing_reversal (H3)

params: {"exit_hours": 48, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,267.31 (started 10,000 at 2026-09-16 23:20Z), net +12.67% since start
- 24h -2.44%, 7d -6.83%, 30d +12.67%, max drawdown -9.51%
- fills 128 total, 90 in the last 7d
- costs 303.85 (fees 199.47 + slippage 104.39); gross pnl 1,571.16; cost coverage 5.17
- cash 0.00; positions: ADA 9141.44, AVAX 212.774, DOT 1910.95, LINK 126.153, LTC 4.79236, SOL 18.9043
- last run 2026-09-30 08:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 07:27Z SOL hold target 0.20 (held 0.20) — hold: weight change +0.001 below threshold 0.05 | stay long: price 118.1 still above the 48h low 116.9; realised vol 55% -> weight 0.25
- 2026-09-30 07:27Z ADA hold target 0.20 (held 0.20) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.2427 still above the 48h low 0.2405; realised vol 88% -> weight 0.25
- 2026-09-30 07:27Z AVAX hold target 0.20 (held 0.21) — hold: weight change -0.010 below threshold 0.05 | stay long: price 11.1 still above the 48h low 10.23; realised vol 103% -> weight 0.25
- 2026-09-30 07:27Z LINK hold target 0.20 (held 0.16) — hold: weight change +0.040 below threshold 0.05 | stay long: price 14.32 still above the 48h low 13.57; realised vol 106% -> weight 0.25
- 2026-09-30 07:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.376 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-30 07:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-30 07:27Z DOT hold target 0.20 (held 0.20) — hold: weight change -0.004 below threshold 0.05 | stay long: price 1.193 still above the 48h low 1.151; realised vol 99% -> weight 0.25
- 2026-09-30 07:27Z LTC sell target 0.00 (held 0.03) — exit: closed 66.59 below the 48h low 66.82
- 2026-09-30 08:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.023e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-09-30 08:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2571 not a higher low vs prior low 2388 (need +10.0%)
- 2026-09-30 08:27Z SOL hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: price 118.4 still above the 48h low 116.9; realised vol 55% -> weight 0.25
- 2026-09-30 08:27Z ADA hold target 0.17 (held 0.20) — hold: weight change -0.032 below threshold 0.05 | stay long: price 0.2445 still above the 48h low 0.2405; realised vol 87% -> weight 0.25
- 2026-09-30 08:27Z AVAX hold target 0.17 (held 0.21) — hold: weight change -0.043 below threshold 0.05 | stay long: price 11.11 still above the 48h low 10.23; realised vol 103% -> weight 0.25
- 2026-09-30 08:27Z LINK hold target 0.17 (held 0.16) — hold: weight change +0.007 below threshold 0.05 | stay long: price 14.3 still above the 48h low 13.57; realised vol 106% -> weight 0.25
- 2026-09-30 08:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.376 not a higher low vs prior low 1.265 (need +10.0%)
- 2026-09-30 08:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.08471 not a higher low vs prior low 0.07876 (need +10.0%)
- 2026-09-30 08:27Z DOT hold target 0.17 (held 0.21) — hold: weight change -0.039 below threshold 0.05 | stay long: price 1.203 still above the 48h low 1.151; realised vol 99% -> weight 0.25
- 2026-09-30 08:27Z LTC buy target 0.17 (held 0.00) — enter long: higher low 56.68 vs prior low 50.28 (+12.7%) then broke above the reaction high 59.1 at 66.87; realised vol 103% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 20 fills (10 buy / 10 sell), traded 40,395, gross pnl +66.47, +33 bps per round trip, avg half spread 2.3 bps, open 9141.44
- AVAX: 16 fills (7 buy / 9 sell), traded 24,842, gross pnl +819.61, +660 bps per round trip, avg half spread 1.6 bps, open 212.774
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 6 fills (4 buy / 2 sell), traded 5,841, gross pnl -31.29, -107 bps per round trip, avg half spread 2.3 bps
- DOT: 18 fills (9 buy / 9 sell), traded 30,251, gross pnl +71.94, +48 bps per round trip, avg half spread 3.0 bps, open 1910.95
- ETH: 4 fills (2 buy / 2 sell), traded 5,454, gross pnl +82.93, +304 bps per round trip, avg half spread 0.1 bps
- LINK: 16 fills (8 buy / 8 sell), traded 26,835, gross pnl +244.60, +182 bps per round trip, avg half spread 3.0 bps, open 126.153
- LTC: 28 fills (14 buy / 14 sell), traded 38,169, gross pnl +104.13, +55 bps per round trip, avg half spread 2.0 bps, open 4.79236
- SOL: 12 fills (6 buy / 6 sell), traded 18,097, gross pnl +50.18, +55 bps per round trip, avg half spread 0.5 bps, open 18.9043
- XRP: 4 fills (2 buy / 2 sell), traded 4,131, gross pnl +102.92, +498 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-09-29 18:28Z sell LTC 330 @ 67.3913 fee 0.33 slip 0.17 (half spread 0.7 bps)
- 2026-09-29 19:24Z buy LTC 329 @ 67.6838 fee 0.33 slip 0.16 (half spread 1.5 bps)
- 2026-09-29 22:23Z sell LTC 327 @ 67.0814 fee 0.33 slip 0.16 (half spread 2.2 bps)
- 2026-09-29 23:21Z buy LTC 326 @ 67.0635 fee 0.33 slip 0.16 (half spread 1.5 bps)
- 2026-09-30 00:32Z sell LTC 324 @ 66.7216 fee 0.32 slip 0.16 (half spread 2.2 bps)
- 2026-09-30 01:24Z buy LTC 324 @ 67.3136 fee 0.32 slip 0.16 (half spread 3.0 bps)
- 2026-09-30 07:27Z sell LTC 321 @ 66.6916 fee 0.32 slip 0.16 (half spread 2.2 bps)
- 2026-09-30 08:27Z buy LTC 320 @ 66.7633 fee 0.32 slip 0.18 (half spread 3.7 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,079.28 (started 10,000 at 2026-09-25 04:23Z), net +0.79% since start
- 24h -1.93%, 7d +0.87%, 30d +0.87%, max drawdown -4.37%
- fills 23 total, 23 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 120.85; cost coverage 2.91
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-09-30 08:27Z; halted today: False

last decisions (newest last):

- 2026-09-30 07:27Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +14.90% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 07:27Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +24.04% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 07:27Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +53.76% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 07:27Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +26.93% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 07:27Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +9.37% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 07:27Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +12.37% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 07:27Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +44.10% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 07:27Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +36.88% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 08:27Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +6.48% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 08:27Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +9.55% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 08:27Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +14.98% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 08:27Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +24.66% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 08:27Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +53.87% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 08:27Z LINK hold target 0.10 (held 0.11) — hold: weight change -0.007 below threshold 0.05 | stay long: 720h return +26.94% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 08:27Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +9.26% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-09-30 08:27Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +13.29% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-09-30 08:27Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +44.68% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-09-30 08:27Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +37.54% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +29.57, +147 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +46.52, +1026 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -10.08, -194 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -51.27, -995 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +25.88, +169 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl -7.15, -137 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +133.64, +659 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -52.93, -266 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -13.72, -114 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +20.38, +67 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1061 candles, 2026-08-17 03:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1061 candles, 2026-08-17 03:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1061 candles, 2026-08-17 03:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1061 candles, 2026-08-17 03:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.8 bps
- AVAX: live 1061 candles, 2026-08-17 03:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.2 bps
- LINK: live 1061 candles, 2026-08-17 03:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 1033 candles, 2026-08-18 07:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1033 candles, 2026-08-18 07:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 1033 candles, 2026-08-18 07:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1033 candles, 2026-08-18 07:00Z to 2026-09-30 07:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.8 bps
