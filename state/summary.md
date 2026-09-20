# quantloop summary — generated 2026-09-20 12:25Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 4.3 of 60, 55.7 days until the verdict
  so far: champion +9.32% (DD -3.54%, 28 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +6.01%, equal weight basket of 10 pairs +13.10%, basket realised vol 52% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,931.54 (started 10,000 at 2026-09-16 03:55Z), net +9.32% since start
- 24h +0.13%, 7d +9.32%, 30d +9.32%, max drawdown -3.54%
- fills 28 total, 28 in the last 7d
- costs 62.52 (fees 41.24 + slippage 21.27); gross pnl 994.06; cost coverage 15.90
- cash 10.51; positions: AVAX 279.519, BTC 0.0333537, ETH 1.03803, LTC 46.9242
- last run 2026-09-20 12:25Z; halted today: False

last decisions (newest last):

- 2026-09-20 11:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +29.72% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 11:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +7.89% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +5.31% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +5.64% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.015 below threshold 0.05 | stay long: 72h return +37.88% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +8.21% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +589.32, +1084 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 2 fills (2 buy / 0 sell), traded 2,697, gross pnl -15.81, -117 bps per round trip, avg half spread 0.0 bps, open 0.0333537
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 2 fills (2 buy / 0 sell), traded 2,687, gross pnl -12.88, -96 bps per round trip, avg half spread 0.0 bps, open 1.03803
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +86.34, +363 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-20 12:25Z; halted today: False

last decisions (newest last):

- 2026-09-20 11:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.16 not below -2.0
- 2026-09-20 11:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.10 not below -2.0
- 2026-09-20 11:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.83 not below -2.0
- 2026-09-20 11:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.94 not below -2.0
- 2026-09-20 11:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.38 not below -2.0
- 2026-09-20 11:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.33 not below -2.0
- 2026-09-20 11:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.71 not below -2.0
- 2026-09-20 11:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.45 not below -2.0
- 2026-09-20 12:25Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.53 not below -2.0
- 2026-09-20 12:25Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.05 not below -2.0
- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.25 not below -2.0
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.30 not below -2.0
- 2026-09-20 12:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.61 not below -2.0
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.12 not below -2.0
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.46 not below -2.0
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.49 not below -2.0
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.86 not below -2.0
- 2026-09-20 12:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.59 not below -2.0

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

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,931.54 (started 10,000 at 2026-09-16 23:20Z), net +9.32% since start
- 24h +0.13%, 7d +9.32%, 30d +9.32%, max drawdown -3.54%
- fills 28 total, 28 in the last 7d
- costs 62.52 (fees 41.24 + slippage 21.27); gross pnl 994.06; cost coverage 15.90
- cash 10.51; positions: AVAX 279.519, BTC 0.0333537, ETH 1.03803, LTC 46.9242
- last run 2026-09-20 12:25Z; halted today: False

last decisions (newest last):

- 2026-09-20 11:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +29.72% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 11:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +7.89% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +5.31% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +5.64% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.015 below threshold 0.05 | stay long: 72h return +37.88% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +8.21% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +589.32, +1084 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 2 fills (2 buy / 0 sell), traded 2,697, gross pnl -15.81, -117 bps per round trip, avg half spread 0.0 bps, open 0.0333537
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 2 fills (2 buy / 0 sell), traded 2,687, gross pnl -12.88, -96 bps per round trip, avg half spread 0.0 bps, open 1.03803
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +86.34, +363 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,931.54 (started 10,000 at 2026-09-16 23:20Z), net +9.32% since start
- 24h +0.13%, 7d +9.32%, 30d +9.32%, max drawdown -3.54%
- fills 28 total, 28 in the last 7d
- costs 62.52 (fees 41.24 + slippage 21.27); gross pnl 994.06; cost coverage 15.90
- cash 10.51; positions: AVAX 279.519, BTC 0.0333537, ETH 1.03803, LTC 46.9242
- last run 2026-09-20 12:25Z; halted today: False

last decisions (newest last):

- 2026-09-20 11:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: 72h return +29.72% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 11:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 11:20Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +7.89% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +5.31% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z ETH hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: 72h return +5.64% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 12:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z AVAX hold target 0.25 (held 0.26) — hold: weight change -0.015 below threshold 0.05 | stay long: 72h return +37.88% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 12:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 12:25Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: 72h return +8.21% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 6 fills (3 buy / 3 sell), traded 10,876, gross pnl +589.32, +1084 bps per round trip, avg half spread 1.2 bps, open 279.519
- BTC: 2 fills (2 buy / 0 sell), traded 2,697, gross pnl -15.81, -117 bps per round trip, avg half spread 0.0 bps, open 0.0333537
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 2 fills (2 buy / 0 sell), traded 2,687, gross pnl -12.88, -96 bps per round trip, avg half spread 0.0 bps, open 1.03803
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 3 fills (2 buy / 1 sell), traded 4,758, gross pnl +86.34, +363 bps per round trip, avg half spread 3.0 bps, open 46.9242
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell ADA 1,530 @ 0.222331 fee 1.53 slip 0.87 (half spread 3.7 bps)
- 2026-09-20 03:22Z buy AVAX 1,539 @ 9.64432 fee 1.54 slip 0.77 (half spread 1.6 bps)
- 2026-09-20 03:22Z sell LINK 1,517 @ 12.0917 fee 1.52 slip 0.92 (half spread 4.0 bps)
- 2026-09-20 03:22Z sell XRP 585 @ 1.38396 fee 0.58 slip 0.29 (half spread 0.5 bps)
- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 825 candles, 2026-08-17 03:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 825 candles, 2026-08-17 03:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 825 candles, 2026-08-17 03:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 825 candles, 2026-08-17 03:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- AVAX: live 825 candles, 2026-08-17 03:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.5 bps
- LINK: live 825 candles, 2026-08-17 03:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 797 candles, 2026-08-18 07:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 797 candles, 2026-08-18 07:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 797 candles, 2026-08-18 07:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 797 candles, 2026-08-18 07:00Z to 2026-09-20 11:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.7 bps
