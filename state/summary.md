# quantloop summary — generated 2026-09-16 21:22Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK. Paper only.

## Challenger slot

- testing H1 since 2026-09-16 05:21Z, day 0.7 of 21, 20.3 days until the verdict
- so far: champion +0.00% (DD 0.00%, 0 fills) vs challenger +0.23% (DD -0.84%, 4 fills)
- this is an interim reading; only the verdict at the end of the window counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,000.00 (started 10,000 at 2026-09-16 03:55Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-09-16 21:22Z; halted today: False

last decisions (newest last):

- 2026-09-16 19:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.27% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 19:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.51% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 19:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.41% not above entry band +1.0%
- 2026-09-16 19:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.11% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 19:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.25% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 19:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.49% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 20:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.61% not above entry band +1.0%
- 2026-09-16 20:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.94% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 20:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.91% not above entry band +1.0%
- 2026-09-16 20:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.63% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 20:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.12% not above entry band +1.0%
- 2026-09-16 20:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.29% not above entry band +1.0%
- 2026-09-16 21:22Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.56% not above entry band +1.0%
- 2026-09-16 21:22Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.10% not above entry band +1.0%
- 2026-09-16 21:22Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.77% not above entry band +1.0%
- 2026-09-16 21:22Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.49% not above entry band +1.0%
- 2026-09-16 21:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.97% not above entry band +1.0%
- 2026-09-16 21:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.09% not above entry band +1.0%

## challenger: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,011.67 (started 10,000 at 2026-09-16 03:55Z), net +0.12% since start
- 24h +0.12%, 7d +0.12%, 30d +0.12%, max drawdown -0.95%
- fills 4 total, 4 in the last 7d
- costs 14.98 (fees 9.99 + slippage 4.99); gross pnl 26.65; cost coverage 1.78
- cash 0.70; positions: ADA 12763.5, BTC 0.0328342, ETH 1.04017, SOL 25.7086
- last run 2026-09-16 21:22Z; halted today: False

last decisions (newest last):

- 2026-09-16 19:21Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.94 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-16 19:21Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: z -2.16 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-16 19:21Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -1.73 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-16 19:21Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: z -2.25 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-09-16 19:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.32 not below -2.0
- 2026-09-16 19:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.50 not below -2.0
- 2026-09-16 20:23Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.53 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-16 20:23Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: z -1.88 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-16 20:23Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: z -1.59 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-16 20:23Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.94 vs 240h mean (entry -2.0, exit -0.5); vol 72% -> weight 0.25
- 2026-09-16 20:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.07 not below -2.0
- 2026-09-16 20:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.31 not below -2.0
- 2026-09-16 21:22Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -1.44 vs 240h mean (entry -2.0, exit -0.5); vol 33% -> weight 0.25
- 2026-09-16 21:22Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.80 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-09-16 21:22Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -1.30 vs 240h mean (entry -2.0, exit -0.5); vol 56% -> weight 0.25
- 2026-09-16 21:22Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: z -1.78 vs 240h mean (entry -2.0, exit -0.5); vol 73% -> weight 0.25
- 2026-09-16 21:22Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.90 not below -2.0
- 2026-09-16 21:22Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.20 not below -2.0

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24

## Data

- BTC: 738 candles, 2026-08-17 03:00Z to 2026-09-16 20:00Z, missing hours in last 7d: 0
- ETH: 738 candles, 2026-08-17 03:00Z to 2026-09-16 20:00Z, missing hours in last 7d: 0
- SOL: 738 candles, 2026-08-17 03:00Z to 2026-09-16 20:00Z, missing hours in last 7d: 0
- ADA: 738 candles, 2026-08-17 03:00Z to 2026-09-16 20:00Z, missing hours in last 7d: 0
- AVAX: 738 candles, 2026-08-17 03:00Z to 2026-09-16 20:00Z, missing hours in last 7d: 0
- LINK: 738 candles, 2026-08-17 03:00Z to 2026-09-16 20:00Z, missing hours in last 7d: 0
