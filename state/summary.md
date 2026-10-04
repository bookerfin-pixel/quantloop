# quantloop summary — generated 2026-10-04 18:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 18.5 of 60, 41.5 days until the verdict
  so far: champion +10.55% (DD -12.84%, 162 fills) vs challenger1 +4.09% (DD -1.00%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.25% (usual 0.54, this window 0.71) vs challenger1 -5.42% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t -0.3 over 19 days
  market over the window: BTC +12.38%, equal weight basket of 10 pairs +25.64%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 13.4 of 60, 46.6 days until the verdict
  so far: champion -3.79% (DD -12.84%, 124 fills) vs challenger2 -0.41% (DD -1.54%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.38% (usual 0.54, this window 0.72) vs challenger2 -1.78% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +0.6 over 14 days
  market over the window: BTC +1.86%, equal weight basket of 10 pairs +4.80%, basket max drawdown -7%, basket realised vol 58% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 9.6 of 60, 50.4 days until the verdict
  so far: champion -6.85% (DD -12.84%, 104 fills) vs challenger3 -3.08% (DD -6.86%, 124 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.15% (usual 0.55, this window 0.70) vs challenger3 -3.21% (usual 0.05, this window 0.61); the rule compares on skill, daily edge t +0.9 over 10 days
  market over the window: BTC +1.29%, equal weight basket of 10 pairs +2.39%, basket max drawdown -5%, basket realised vol 54% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 8.8 of 60, 51.2 days until the verdict
  so far: champion -9.57% (DD -12.84%, 96 fills) vs challenger4 -0.33% (DD -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -9.08% (usual 0.55, this window 0.67) vs challenger4 +0.10% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.3 over 9 days
  market over the window: BTC +1.47%, equal weight basket of 10 pairs -0.90%, basket max drawdown -5%, basket realised vol 55% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,054.70 (started 10,000 at 2026-09-16 03:55Z), net +10.55% since start
- 24h +1.13%, 7d -10.68%, 30d +10.55%, max drawdown -12.84%
- fills 162 total, 84 in the last 7d
- costs 379.70 (fees 251.08 + slippage 128.62); gross pnl 1,434.40; cost coverage 3.78
- cash -0.00; positions: AVAX 243.024, BTC 0.0259262, DOT 1443.5, LTC 31.0999, SOL 18.2266
- last run 2026-10-04 18:21Z; halted today: False

last decisions (newest last):

- 2026-10-04 12:25Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.78% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-04 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.53% not above entry band +1.0%
- 2026-10-04 12:25Z AVAX hold target 0.25 (held 0.24) — hold: weight change +0.008 below threshold 0.05 | stay long: 72h return -0.42% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-04 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.99% not above entry band +1.0%
- 2026-10-04 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.41% not above entry band +1.0%
- 2026-10-04 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.53% not above entry band +1.0%
- 2026-10-04 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.38% not above entry band +1.0%
- 2026-10-04 12:25Z LTC hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +5.80% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-04 18:21Z BTC sell target 0.20 (held 0.25) — stay long: 72h return +0.51% vs exit band -1.0% and price above 24h EMA; realised vol 32% -> weight 0.25
- 2026-10-04 18:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.06% not above entry band +1.0%
- 2026-10-04 18:21Z SOL sell target 0.20 (held 0.25) — stay long: 72h return +2.65% vs exit band -1.0% and price above 24h EMA; realised vol 53% -> weight 0.25
- 2026-10-04 18:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.99% not above entry band +1.0%
- 2026-10-04 18:21Z AVAX hold target 0.20 (held 0.24) — hold: weight change -0.043 below threshold 0.05 | stay long: 72h return +0.97% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-04 18:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.24% not above entry band +1.0%
- 2026-10-04 18:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.13% not above entry band +1.0%
- 2026-10-04 18:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.68% not above entry band +1.0%
- 2026-10-04 18:21Z DOT buy target 0.20 (held 0.00) — enter long: 72h return +1.00% vs entry band +1.0% and price above 24h EMA; realised vol 94% -> weight 0.25
- 2026-10-04 18:21Z LTC sell target 0.20 (held 0.26) — stay long: 72h return +4.90% vs exit band -1.0% and price above 24h EMA; realised vol 64% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 16 fills (7 buy / 9 sell), traded 25,153, gross pnl +17.39, +14 bps per round trip, avg half spread 2.3 bps
- AVAX: 23 fills (10 buy / 13 sell), traded 41,072, gross pnl +561.39, +273 bps per round trip, avg half spread 1.3 bps, open 243.024
- BTC: 10 fills (5 buy / 5 sell), traded 11,868, gross pnl +123.40, +208 bps per round trip, avg half spread 0.2 bps, open 0.0259262
- DOGE: 16 fills (8 buy / 8 sell), traded 22,194, gross pnl -88.11, -79 bps per round trip, avg half spread 1.2 bps
- DOT: 18 fills (10 buy / 8 sell), traded 21,815, gross pnl +141.81, +130 bps per round trip, avg half spread 2.7 bps, open 1443.5
- ETH: 13 fills (5 buy / 8 sell), traded 19,627, gross pnl +17.81, +18 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 14 fills (6 buy / 8 sell), traded 22,867, gross pnl +599.03, +524 bps per round trip, avg half spread 2.0 bps, open 31.0999
- SOL: 16 fills (9 buy / 7 sell), traded 26,953, gross pnl +53.06, +39 bps per round trip, avg half spread 0.5 bps, open 18.2266
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-03 07:25Z buy SOL 2,736 @ 119.365 fee 2.74 slip 1.37 (half spread 0.4 bps)
- 2026-10-03 14:32Z sell SOL 2,738 @ 119.425 fee 2.74 slip 1.37 (half spread 0.4 bps)
- 2026-10-03 19:02Z buy SOL 2,735 @ 119.855 fee 2.73 slip 1.37 (half spread 0.4 bps)
- 2026-10-03 19:02Z buy AVAX 2,698 @ 11.1005 fee 2.70 slip 1.35 (half spread 0.9 bps)
- 2026-10-04 18:21Z sell BTC 554 @ 85265.1 fee 0.55 slip 0.28 (half spread 0.0 bps)
- 2026-10-04 18:21Z sell SOL 557 @ 121.284 fee 0.56 slip 0.28 (half spread 0.4 bps)
- 2026-10-04 18:21Z sell LTC 626 @ 71.0794 fee 0.63 slip 0.31 (half spread 2.1 bps)
- 2026-10-04 18:21Z buy DOT 1,733 @ 1.2009 fee 1.73 slip 0.87 (half spread 2.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,397.39 (started 10,000 at 2026-09-16 03:55Z), net +3.97% since start
- 24h +0.57%, 7d +1.05%, 30d +3.97%, max drawdown -1.00%
- fills 10 total, 2 in the last 7d
- costs 38.32 (fees 25.55 + slippage 12.77); gross pnl 435.71; cost coverage 11.37
- cash 10,397.39; positions: none
- last run 2026-10-04 18:21Z; halted today: False

last decisions (newest last):

- 2026-10-04 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.88 not below -2.0
- 2026-10-04 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.79 not below -2.0
- 2026-10-04 12:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.40 not below -2.0
- 2026-10-04 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.17 not below -2.0
- 2026-10-04 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.49 not below -2.0
- 2026-10-04 12:25Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.005 below threshold 0.05 | stay long: z -0.87 vs 240h mean (entry -2.0, exit -0.5); vol 64% -> weight 0.25
- 2026-10-04 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.30 not below -2.0
- 2026-10-04 12:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.74 not below -2.0
- 2026-10-04 18:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.39 not below -2.0
- 2026-10-04 18:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.61 not below -2.0
- 2026-10-04 18:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.99 not below -2.0
- 2026-10-04 18:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.30 not below -2.0
- 2026-10-04 18:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.54 not below -2.0
- 2026-10-04 18:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.14 not below -2.0
- 2026-10-04 18:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.38 not below -2.0
- 2026-10-04 18:21Z DOGE sell target 0.00 (held 0.26) — flat: z +0.25 not below -0.5
- 2026-10-04 18:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.35 not below -2.0
- 2026-10-04 18:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.71 not below -2.0

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

- equity 10,921.07 (started 10,000 at 2026-09-16 23:20Z), net +9.21% since start
- 24h +0.28%, 7d -0.41%, 30d +9.21%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,008.25; cost coverage 11.56
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-04 18:21Z; halted today: False

last decisions (newest last):

- 2026-10-04 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 12:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 8.53e+04 still above 72h low 8.424e+04; realised vol 32% -> weight 0.25
- 2026-10-04 18:21Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: price 2702 still above 72h low 2661; realised vol 37% -> weight 0.25
- 2026-10-04 18:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-04 18:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl -11.45, -28 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -46.61, -115 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,157.47 (started 10,000 at 2026-09-16 23:20Z), net +11.57% since start
- 24h +1.60%, 7d -3.54%, 30d +11.57%, max drawdown -11.53%
- fills 173 total, 123 in the last 7d
- costs 385.97 (fees 254.00 + slippage 131.97); gross pnl 1,543.44; cost coverage 4.00
- cash 2,694.66; positions: LINK 199.564, LTC 39.8619, SOL 23.1038
- last run 2026-10-04 18:21Z; halted today: False

last decisions (newest last):

- 2026-10-04 12:25Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 121.2 still above the 48h low 117.7; realised vol 54% -> weight 0.25
- 2026-10-04 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2452 not above reaction high 0.2599
- 2026-10-04 12:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 10.99 not above reaction high 11.55
- 2026-10-04 12:25Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 14.09 still above the 48h low 13.56; realised vol 93% -> weight 0.25
- 2026-10-04 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.499 not above reaction high 1.638
- 2026-10-04 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09346 not above reaction high 0.1039
- 2026-10-04 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.192 not above reaction high 1.218
- 2026-10-04 12:25Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: price 71.17 still above the 48h low 68.46; realised vol 63% -> weight 0.25
- 2026-10-04 18:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-04 18:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 2702 not above reaction high 2784
- 2026-10-04 18:21Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 121.5 still above the 48h low 117.7; realised vol 53% -> weight 0.25
- 2026-10-04 18:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2477 not above reaction high 0.2616
- 2026-10-04 18:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.05 not above reaction high 11.55
- 2026-10-04 18:21Z LINK hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: price 14.16 still above the 48h low 13.56; realised vol 92% -> weight 0.25
- 2026-10-04 18:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.501 not above reaction high 1.638
- 2026-10-04 18:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.0955 not above reaction high 0.1039
- 2026-10-04 18:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.191 not above reaction high 1.218
- 2026-10-04 18:21Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: price 71.07 still above the 48h low 68.46; realised vol 64% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 24 fills (11 buy / 13 sell), traded 45,344, gross pnl +23.98, +11 bps per round trip, avg half spread 2.3 bps
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 11 fills (6 buy / 5 sell), traded 11,408, gross pnl -82.80, -145 bps per round trip, avg half spread 1.5 bps
- DOT: 23 fills (11 buy / 12 sell), traded 36,196, gross pnl -57.11, -32 bps per round trip, avg half spread 2.7 bps
- ETH: 9 fills (4 buy / 5 sell), traded 11,060, gross pnl +79.28, +143 bps per round trip, avg half spread 0.1 bps
- LINK: 25 fills (12 buy / 13 sell), traded 42,245, gross pnl +292.94, +139 bps per round trip, avg half spread 2.7 bps, open 199.564
- LTC: 36 fills (19 buy / 17 sell), traded 45,054, gross pnl +253.33, +112 bps per round trip, avg half spread 1.9 bps, open 39.8619
- SOL: 17 fills (9 buy / 8 sell), traded 23,112, gross pnl +97.25, +84 bps per round trip, avg half spread 0.5 bps, open 23.1038
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

- equity 10,219.77 (started 10,000 at 2026-09-25 04:23Z), net +2.20% since start
- 24h +1.23%, 7d -1.26%, 30d +2.27%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 261.34; cost coverage 6.29
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-04 18:21Z; halted today: False

last decisions (newest last):

- 2026-10-04 12:25Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +16.45% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 12:25Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +10.83% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-04 12:25Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +46.61% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 12:25Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +17.10% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-04 12:25Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +3.30% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-04 12:25Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +6.50% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-04 12:25Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +35.39% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-04 12:25Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +38.71% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +7.33% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-04 18:21Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +10.46% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +19.96% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z ADA hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +17.11% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +50.54% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +22.05% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +7.68% vs exit band -5.0% and price above 168h EMA; realised vol...
- 2026-10-04 18:21Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +13.51% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-04 18:21Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +39.18% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-04 18:21Z LTC hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +41.40% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +43.51, +217 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +43.94, +969 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +17.14, +330 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -33.79, -656 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +15.53, +102 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +5.34, +103 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +123.05, +607 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl +10.24, +51 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +13.59, +113 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +22.78, +75 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1167 candles, 2026-08-17 03:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1167 candles, 2026-08-17 03:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1167 candles, 2026-08-17 03:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1167 candles, 2026-08-17 03:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- AVAX: live 1167 candles, 2026-08-17 03:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1167 candles, 2026-08-17 03:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 1139 candles, 2026-08-18 07:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1139 candles, 2026-08-18 07:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 1139 candles, 2026-08-18 07:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- LTC: live 1139 candles, 2026-08-18 07:00Z to 2026-10-04 17:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
