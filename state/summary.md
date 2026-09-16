# quantloop summary — generated 2026-09-16 23:20Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 0.7 of 21, 20.3 days until the verdict
  so far: champion +0.00% (DD 0.00%, 0 fills) vs challenger1 +0.33% (DD -1.00%, 4 fills)
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,000.00 (started 10,000 at 2026-09-16 03:55Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-09-16 23:20Z; halted today: False

last decisions (newest last):

- 2026-09-16 21:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-16 21:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.10% not above entry band +1.0%
- 2026-09-16 21:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.77% not above entry band +1.0%
- 2026-09-16 21:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.49% not above entry band +1.0%
- 2026-09-16 21:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.97% not above entry band +1.0%
- 2026-09-16 21:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.09% not above entry band +1.0%
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

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,022.03 (started 10,000 at 2026-09-16 03:55Z), net +0.22% since start
- 24h +0.22%, 7d +0.22%, 30d +0.22%, max drawdown -1.00%
- fills 4 total, 4 in the last 7d
- costs 14.98 (fees 9.99 + slippage 4.99); gross pnl 37.01; cost coverage 2.47
- cash 0.70; positions: ADA 12763.5, BTC 0.0328342, ETH 1.04017, SOL 25.7086
- last run 2026-09-16 23:20Z; halted today: False

last decisions (newest last):

- 2026-09-16 21:22Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.44 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-16 21:22Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.80 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-16 21:22Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -1.30 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-16 21:22Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.78 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-16 21:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.90 not below -2.0
- 2026-09-16 21:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.20 not below -2.0
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

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,000.00 (started 10,000 at 2026-09-16 23:20Z), net +0.00% since start
- 24h n/a, 7d n/a, 30d n/a, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-09-16 23:20Z; halted today: False

last decisions (newest last):

- 2026-09-16 23:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.39% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.40% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.95% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.73% not above entry band +1.0%
- 2026-09-16 23:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.60% not above entry band +1.0% and price below 24h EMA

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,000.00 (started 10,000 at 2026-09-16 23:20Z), net +0.00% since start
- 24h n/a, 7d n/a, 30d n/a, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-09-16 23:20Z; halted today: False

last decisions (newest last):

- 2026-09-16 23:20Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.39% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.40% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.95% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 23:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.73% not above entry band +1.0%
- 2026-09-16 23:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.60% not above entry band +1.0% and price below 24h EMA

## Data

- BTC: 740 candles, 2026-08-17 03:00Z to 2026-09-16 22:00Z, missing hours in last 7d: 0
- ETH: 740 candles, 2026-08-17 03:00Z to 2026-09-16 22:00Z, missing hours in last 7d: 0
- SOL: 740 candles, 2026-08-17 03:00Z to 2026-09-16 22:00Z, missing hours in last 7d: 0
- ADA: 740 candles, 2026-08-17 03:00Z to 2026-09-16 22:00Z, missing hours in last 7d: 0
- AVAX: 740 candles, 2026-08-17 03:00Z to 2026-09-16 22:00Z, missing hours in last 7d: 0
- LINK: 740 candles, 2026-08-17 03:00Z to 2026-09-16 22:00Z, missing hours in last 7d: 0
