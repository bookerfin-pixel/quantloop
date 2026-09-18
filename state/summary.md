# quantloop summary — generated 2026-09-18 02:23Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.9 of 60, 58.1 days until the verdict
  so far: champion +2.09% (DD -0.60%, 5 fills) vs challenger1 +2.85% (DD -1.00%, 7 fills)
  market over the window: BTC +1.01%, equal weight basket of 10 pairs +5.25%, basket realised vol 40% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,209.37 (started 10,000 at 2026-09-16 03:55Z), net +2.09% since start
- 24h +2.05%, 7d +2.09%, 30d +2.09%, max drawdown -0.60%
- fills 5 total, 5 in the last 7d
- costs 19.02 (fees 12.62 + slippage 6.40); gross pnl 228.39; cost coverage 12.01
- cash 2,426.86; positions: AVAX 332.035, DOT 2418.21, LTC 46.9081
- last run 2026-09-18 02:23Z; halted today: False

last decisions (newest last):

- 2026-09-18 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.11% not above entry band +1.0%
- 2026-09-18 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-18 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.84% not above entry band +1.0%
- 2026-09-18 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.30% not above entry band +1.0%
- 2026-09-18 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.43% not above entry band +1.0%
- 2026-09-18 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.35% not above entry band +1.0%
- 2026-09-18 01:20Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.010 below threshold 0.05 | stay long: 72h return +10.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 01:20Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +3.27% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 02:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.57% not above entry band +1.0%
- 2026-09-18 02:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.36% not above entry band +1.0%
- 2026-09-18 02:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.15% not above entry band +1.0%
- 2026-09-18 02:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.82% not above entry band +1.0%
- 2026-09-18 02:23Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +1.96% vs entry band +1.0% and price above 24h EMA; realised vol 62% -> weight 0.25
- 2026-09-18 02:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.57% not above entry band +1.0%
- 2026-09-18 02:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0%
- 2026-09-18 02:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.67% not above entry band +1.0%
- 2026-09-18 02:23Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +11.38% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 02:23Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +3.16% vs exit band -1.0% and price above 24h EMA; realised vol 5...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 3 fills (2 buy / 1 sell), traded 7,583, gross pnl +32.31, +85 bps per round trip, avg half spread 1.0 bps, open 332.035
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +179.43, +1432 bps per round trip, avg half spread 3.4 bps, open 2418.21
- LTC: 1 fills (1 buy / 0 sell), traded 2,531, gross pnl +16.65, +132 bps per round trip, avg half spread 2.8 bps, open 46.9081

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)
- 2026-09-17 21:21Z sell AVAX 2,530 @ 7.5947 fee 2.53 slip 1.27 (half spread 0.7 bps)
- 2026-09-18 00:28Z buy LTC 2,531 @ 53.962 fee 2.53 slip 1.26 (half spread 2.8 bps)
- 2026-09-18 02:23Z buy AVAX 2,553 @ 7.68984 fee 2.55 slip 1.28 (half spread 1.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,273.42 (started 10,000 at 2026-09-16 03:55Z), net +2.73% since start
- 24h +1.80%, 7d +2.73%, 30d +2.73%, max drawdown -1.00%
- fills 7 total, 7 in the last 7d
- costs 26.63 (fees 17.75 + slippage 8.87); gross pnl 300.04; cost coverage 11.27
- cash 7,754.58; positions: BTC 0.0328342
- last run 2026-09-18 02:23Z; halted today: False

last decisions (newest last):

- 2026-09-18 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-09-18 01:20Z ADA sell target 0.00 (held 0.26) — flat: z -0.36 not below -0.5
- 2026-09-18 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.30 not below -2.0
- 2026-09-18 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.31 not below -2.0
- 2026-09-18 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.34 not below -2.0
- 2026-09-18 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.84 not below -2.0
- 2026-09-18 01:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.64 not below -2.0
- 2026-09-18 01:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.94 not below -2.0
- 2026-09-18 02:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: z -0.69 vs 240h mean (entry -2.0, exit -0.5); vol 32% -> weight 0.25
- 2026-09-18 02:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.50 not below -2.0
- 2026-09-18 02:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.71 not below -2.0
- 2026-09-18 02:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.25 not below -2.0
- 2026-09-18 02:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.55 not below -2.0
- 2026-09-18 02:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.07 not below -2.0
- 2026-09-18 02:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.23 not below -2.0
- 2026-09-18 02:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.64 not below -2.0
- 2026-09-18 02:23Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.72 not below -2.0
- 2026-09-18 02:23Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.09 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 1 fills (1 buy / 0 sell), traded 2,489, gross pnl -2,488.07, -19990 bps per round trip, open 0.0328342
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

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,209.37 (started 10,000 at 2026-09-16 23:20Z), net +2.09% since start
- 24h +2.05%, 7d +2.09%, 30d +2.09%, max drawdown -0.60%
- fills 5 total, 5 in the last 7d
- costs 19.02 (fees 12.62 + slippage 6.40); gross pnl 228.39; cost coverage 12.01
- cash 2,426.86; positions: AVAX 332.035, DOT 2418.21, LTC 46.9081
- last run 2026-09-18 02:23Z; halted today: False

last decisions (newest last):

- 2026-09-18 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.11% not above entry band +1.0%
- 2026-09-18 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-18 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.84% not above entry band +1.0%
- 2026-09-18 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.30% not above entry band +1.0%
- 2026-09-18 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.43% not above entry band +1.0%
- 2026-09-18 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.35% not above entry band +1.0%
- 2026-09-18 01:20Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.010 below threshold 0.05 | stay long: 72h return +10.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 01:20Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +3.27% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 02:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.57% not above entry band +1.0%
- 2026-09-18 02:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.36% not above entry band +1.0%
- 2026-09-18 02:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.15% not above entry band +1.0%
- 2026-09-18 02:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.82% not above entry band +1.0%
- 2026-09-18 02:23Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +1.96% vs entry band +1.0% and price above 24h EMA; realised vol 62% -> weight 0.25
- 2026-09-18 02:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.57% not above entry band +1.0%
- 2026-09-18 02:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0%
- 2026-09-18 02:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.67% not above entry band +1.0%
- 2026-09-18 02:23Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +11.38% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 02:23Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +3.16% vs exit band -1.0% and price above 24h EMA; realised vol 5...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 3 fills (2 buy / 1 sell), traded 7,583, gross pnl +32.31, +85 bps per round trip, avg half spread 1.0 bps, open 332.035
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +179.43, +1432 bps per round trip, avg half spread 3.4 bps, open 2418.21
- LTC: 1 fills (1 buy / 0 sell), traded 2,531, gross pnl +16.65, +132 bps per round trip, avg half spread 2.8 bps, open 46.9081

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)
- 2026-09-17 21:21Z sell AVAX 2,530 @ 7.5947 fee 2.53 slip 1.27 (half spread 0.7 bps)
- 2026-09-18 00:28Z buy LTC 2,531 @ 53.962 fee 2.53 slip 1.26 (half spread 2.8 bps)
- 2026-09-18 02:23Z buy AVAX 2,553 @ 7.68984 fee 2.55 slip 1.28 (half spread 1.3 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,209.37 (started 10,000 at 2026-09-16 23:20Z), net +2.09% since start
- 24h +2.05%, 7d +2.09%, 30d +2.09%, max drawdown -0.60%
- fills 5 total, 5 in the last 7d
- costs 19.02 (fees 12.62 + slippage 6.40); gross pnl 228.39; cost coverage 12.01
- cash 2,426.86; positions: AVAX 332.035, DOT 2418.21, LTC 46.9081
- last run 2026-09-18 02:23Z; halted today: False

last decisions (newest last):

- 2026-09-18 01:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.11% not above entry band +1.0%
- 2026-09-18 01:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.81% not above entry band +1.0%
- 2026-09-18 01:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.84% not above entry band +1.0%
- 2026-09-18 01:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.30% not above entry band +1.0%
- 2026-09-18 01:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.43% not above entry band +1.0%
- 2026-09-18 01:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.35% not above entry band +1.0%
- 2026-09-18 01:20Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.010 below threshold 0.05 | stay long: 72h return +10.68% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 01:20Z LTC hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +3.27% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-09-18 02:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.57% not above entry band +1.0%
- 2026-09-18 02:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.36% not above entry band +1.0%
- 2026-09-18 02:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.15% not above entry band +1.0%
- 2026-09-18 02:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.82% not above entry band +1.0%
- 2026-09-18 02:23Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +1.96% vs entry band +1.0% and price above 24h EMA; realised vol 62% -> weight 0.25
- 2026-09-18 02:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.57% not above entry band +1.0%
- 2026-09-18 02:23Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.28% not above entry band +1.0%
- 2026-09-18 02:23Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.67% not above entry band +1.0%
- 2026-09-18 02:23Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.013 below threshold 0.05 | stay long: 72h return +11.38% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-18 02:23Z LTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +3.16% vs exit band -1.0% and price above 24h EMA; realised vol 5...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 3 fills (2 buy / 1 sell), traded 7,583, gross pnl +32.31, +85 bps per round trip, avg half spread 1.0 bps, open 332.035
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +179.43, +1432 bps per round trip, avg half spread 3.4 bps, open 2418.21
- LTC: 1 fills (1 buy / 0 sell), traded 2,531, gross pnl +16.65, +132 bps per round trip, avg half spread 2.8 bps, open 46.9081

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)
- 2026-09-17 21:21Z sell AVAX 2,530 @ 7.5947 fee 2.53 slip 1.27 (half spread 0.7 bps)
- 2026-09-18 00:28Z buy LTC 2,531 @ 53.962 fee 2.53 slip 1.26 (half spread 2.8 bps)
- 2026-09-18 02:23Z buy AVAX 2,553 @ 7.68984 fee 2.55 slip 1.28 (half spread 1.3 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 767 candles, 2026-08-17 03:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 767 candles, 2026-08-17 03:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 767 candles, 2026-08-17 03:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 767 candles, 2026-08-17 03:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.7 bps
- AVAX: live 767 candles, 2026-08-17 03:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 767 candles, 2026-08-17 03:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 739 candles, 2026-08-18 07:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.3 bps
- DOGE: live 739 candles, 2026-08-18 07:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 739 candles, 2026-08-18 07:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 739 candles, 2026-08-18 07:00Z to 2026-09-18 01:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.5 bps
