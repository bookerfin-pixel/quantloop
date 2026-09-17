# quantloop summary — generated 2026-09-17 05:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.0 of 21, 20.0 days until the verdict
  so far: champion +0.05% (DD -0.15%, 1 fills) vs challenger1 +1.23% (DD -1.00%, 4 fills)
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,004.58 (started 10,000 at 2026-09-16 03:55Z), net +0.05% since start
- 24h +0.05%, 7d +0.05%, 30d +0.05%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 8.33; cost coverage 2.22
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 05:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 03:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-09-17 03:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.32% not above entry band +1.0%
- 2026-09-17 03:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-09-17 03:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.00% not above entry band +1.0%
- 2026-09-17 03:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.40% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 03:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.08% not above entry band +1.0%
- 2026-09-17 04:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.54% not above entry band +1.0%
- 2026-09-17 04:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.11% not above entry band +1.0%
- 2026-09-17 04:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.07% not above entry band +1.0%
- 2026-09-17 04:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.35% not above entry band +1.0%
- 2026-09-17 04:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.00% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 04:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.06% not above entry band +1.0%
- 2026-09-17 05:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.53% not above entry band +1.0%
- 2026-09-17 05:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.93% not above entry band +1.0%
- 2026-09-17 05:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.29% not above entry band +1.0%
- 2026-09-17 05:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.10% not above entry band +1.0%
- 2026-09-17 05:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.67% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 05:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.21% not above entry band +1.0%

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,111.27 (started 10,000 at 2026-09-16 03:55Z), net +1.11% since start
- 24h +1.41%, 7d +1.11%, 30d +1.11%, max drawdown -1.00%
- fills 4 total, 4 in the last 7d
- costs 14.98 (fees 9.99 + slippage 4.99); gross pnl 126.25; cost coverage 8.43
- cash 0.70; positions: ADA 12763.5, BTC 0.0328342, ETH 1.04017, SOL 25.7086
- last run 2026-09-17 05:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 03:22Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.21 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-17 03:22Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.28 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-17 03:22Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.004 below threshold 0.05 | stay long: z -0.95 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 03:22Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.73 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 03:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.32 not below -2.0
- 2026-09-17 03:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.95 not below -2.0
- 2026-09-17 04:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.15 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-17 04:23Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.11 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-17 04:23Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.68 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 04:23Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.61 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 04:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-09-17 04:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.95 not below -2.0
- 2026-09-17 05:22Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.05 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-17 05:22Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -0.95 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-17 05:22Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -0.68 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 05:22Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.53 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 05:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.23 not below -2.0
- 2026-09-17 05:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.91 not below -2.0

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,004.58 (started 10,000 at 2026-09-16 23:20Z), net +0.05% since start
- 24h +0.05%, 7d +0.05%, 30d +0.05%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 8.33; cost coverage 2.22
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 05:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 03:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-09-17 03:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.32% not above entry band +1.0%
- 2026-09-17 03:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-09-17 03:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.00% not above entry band +1.0%
- 2026-09-17 03:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.40% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 03:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.08% not above entry band +1.0%
- 2026-09-17 04:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.54% not above entry band +1.0%
- 2026-09-17 04:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.11% not above entry band +1.0%
- 2026-09-17 04:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.07% not above entry band +1.0%
- 2026-09-17 04:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.35% not above entry band +1.0%
- 2026-09-17 04:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.00% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 04:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.06% not above entry band +1.0%
- 2026-09-17 05:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.53% not above entry band +1.0%
- 2026-09-17 05:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.93% not above entry band +1.0%
- 2026-09-17 05:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.29% not above entry band +1.0%
- 2026-09-17 05:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.10% not above entry band +1.0%
- 2026-09-17 05:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.67% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 05:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.21% not above entry band +1.0%

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,004.58 (started 10,000 at 2026-09-16 23:20Z), net +0.05% since start
- 24h +0.05%, 7d +0.05%, 30d +0.05%, max drawdown -0.15%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl 8.33; cost coverage 2.22
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 05:22Z; halted today: False

last decisions (newest last):

- 2026-09-17 03:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-09-17 03:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.32% not above entry band +1.0%
- 2026-09-17 03:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.63% not above entry band +1.0%
- 2026-09-17 03:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.00% not above entry band +1.0%
- 2026-09-17 03:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.40% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 03:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.08% not above entry band +1.0%
- 2026-09-17 04:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.54% not above entry band +1.0%
- 2026-09-17 04:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.11% not above entry band +1.0%
- 2026-09-17 04:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.07% not above entry band +1.0%
- 2026-09-17 04:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.35% not above entry band +1.0%
- 2026-09-17 04:23Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.00% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 04:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.06% not above entry band +1.0%
- 2026-09-17 05:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.53% not above entry band +1.0%
- 2026-09-17 05:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.93% not above entry band +1.0%
- 2026-09-17 05:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.29% not above entry band +1.0%
- 2026-09-17 05:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.10% not above entry band +1.0%
- 2026-09-17 05:22Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.67% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-09-17 05:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.21% not above entry band +1.0%

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## Data

- BTC: 746 candles, 2026-08-17 03:00Z to 2026-09-17 04:00Z, missing hours in last 7d: 0
- ETH: 746 candles, 2026-08-17 03:00Z to 2026-09-17 04:00Z, missing hours in last 7d: 0
- SOL: 746 candles, 2026-08-17 03:00Z to 2026-09-17 04:00Z, missing hours in last 7d: 0
- ADA: 746 candles, 2026-08-17 03:00Z to 2026-09-17 04:00Z, missing hours in last 7d: 0
- AVAX: 746 candles, 2026-08-17 03:00Z to 2026-09-17 04:00Z, missing hours in last 7d: 0
- LINK: 746 candles, 2026-08-17 03:00Z to 2026-09-17 04:00Z, missing hours in last 7d: 0
