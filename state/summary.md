# quantloop summary — generated 2026-09-17 00:28Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 0.8 of 21, 20.2 days until the verdict
  so far: champion -0.04% (DD -0.04%, 1 fills) vs challenger1 +0.80% (DD -1.00%, 4 fills)
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,996.25 (started 10,000 at 2026-09-16 03:55Z), net -0.04% since start
- 24h -0.04%, 7d -0.04%, 30d -0.04%, max drawdown -0.04%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl -0.00; cost coverage -0.00
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-16 22:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.77% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 22:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.19% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 22:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.96% not above entry band +1.0%
- 2026-09-16 22:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.08% not above entry band +1.0%
- 2026-09-16 22:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.74% not above entry band +1.0%
- 2026-09-16 22:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.12% not above entry band +1.0%
- 2026-09-16 23:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.39% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.40% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.95% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.73% not above entry band +1.0%
- 2026-09-16 23:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.60% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 00:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.85% not above entry band +1.0%
- 2026-09-17 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.40% not above entry band +1.0%
- 2026-09-17 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.72% not above entry band +1.0%
- 2026-09-17 00:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.58% not above entry band +1.0%
- 2026-09-17 00:28Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +2.47% vs entry band +1.0% and price above 24h EMA; realised vol 64% -> weight 0.25
- 2026-09-17 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.31% not above entry band +1.0%

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,068.25 (started 10,000 at 2026-09-16 03:55Z), net +0.68% since start
- 24h +0.68%, 7d +0.68%, 30d +0.68%, max drawdown -1.00%
- fills 4 total, 4 in the last 7d
- costs 14.98 (fees 9.99 + slippage 4.99); gross pnl 83.23; cost coverage 5.56
- cash 0.70; positions: ADA 12763.5, BTC 0.0328342, ETH 1.04017, SOL 25.7086
- last run 2026-09-17 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-16 22:21Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.60 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-16 22:21Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.92 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-16 22:21Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -1.43 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-16 22:21Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: z -1.83 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-09-16 22:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.87 not below -2.0
- 2026-09-16 22:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.26 not below -2.0
- 2026-09-16 23:20Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.85 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-16 23:20Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.18 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-16 23:20Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -1.83 vs 240h mean (entry -2.0, exit -0.5); vol 55% -> weight 0.25
- 2026-09-16 23:20Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.09 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-09-16 23:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.01 not below -2.0
- 2026-09-16 23:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.35 not below -2.0
- 2026-09-17 00:28Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.37 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-17 00:28Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.55 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-17 00:28Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -1.31 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-17 00:28Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.63 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-17 00:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.52 not below -2.0
- 2026-09-17 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.09 not below -2.0

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,996.25 (started 10,000 at 2026-09-16 23:20Z), net -0.04% since start
- 24h -0.04%, 7d -0.04%, 30d -0.04%, max drawdown -0.04%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl -0.00; cost coverage -0.00
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-16 23:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.39% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.40% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.95% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.73% not above entry band +1.0%
- 2026-09-16 23:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.60% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 00:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.85% not above entry band +1.0%
- 2026-09-17 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.40% not above entry band +1.0%
- 2026-09-17 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.72% not above entry band +1.0%
- 2026-09-17 00:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.58% not above entry band +1.0%
- 2026-09-17 00:28Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +2.47% vs entry band +1.0% and price above 24h EMA; realised vol 64% -> weight 0.25
- 2026-09-17 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.31% not above entry band +1.0%

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,996.25 (started 10,000 at 2026-09-16 23:20Z), net -0.04% since start
- 24h -0.04%, 7d -0.04%, 30d -0.04%, max drawdown -0.04%
- fills 1 total, 1 in the last 7d
- costs 3.75 (fees 2.50 + slippage 1.25); gross pnl -0.00; cost coverage -0.00
- cash 7,497.50; positions: AVAX 333.1
- last run 2026-09-17 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-16 23:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.39% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.40% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.95% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.73% not above entry band +1.0%
- 2026-09-16 23:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.60% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 00:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.85% not above entry band +1.0%
- 2026-09-17 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.40% not above entry band +1.0%
- 2026-09-17 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.72% not above entry band +1.0%
- 2026-09-17 00:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.58% not above entry band +1.0%
- 2026-09-17 00:28Z AVAX buy target 0.25 (held 0.00) — enter long: 72h return +2.47% vs entry band +1.0% and price above 24h EMA; realised vol 64% -> weight 0.25
- 2026-09-17 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.31% not above entry band +1.0%

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25

## Data

- BTC: 741 candles, 2026-08-17 03:00Z to 2026-09-16 23:00Z, missing hours in last 7d: 0
- ETH: 741 candles, 2026-08-17 03:00Z to 2026-09-16 23:00Z, missing hours in last 7d: 0
- SOL: 741 candles, 2026-08-17 03:00Z to 2026-09-16 23:00Z, missing hours in last 7d: 0
- ADA: 741 candles, 2026-08-17 03:00Z to 2026-09-16 23:00Z, missing hours in last 7d: 0
- AVAX: 741 candles, 2026-08-17 03:00Z to 2026-09-16 23:00Z, missing hours in last 7d: 0
- LINK: 741 candles, 2026-08-17 03:00Z to 2026-09-16 23:00Z, missing hours in last 7d: 0
