# quantloop summary — generated 2026-09-16 07:23Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK. Paper only.

## Challenger slot

- testing H1 since 2026-09-16 05:21Z, day 0.1 of 21, 20.9 days until the verdict
- so far: champion +0.00% (DD 0.00%, 0 fills) vs challenger -0.24% (DD -0.24%, 3 fills)
- this is an interim reading; only the verdict at the end of the window counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,000.00 (started 10,000 at 2026-09-16 03:55Z), net +0.00% since start
- 24h +0.00%, 7d +0.00%, 30d +0.00%, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-09-16 07:23Z; halted today: False

last decisions (newest last):

- 2026-09-16 05:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.80% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 05:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.66% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 05:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.43% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 05:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.63% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 05:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.03% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 05:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.66% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 06:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.80% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 06:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.63% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 06:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.58% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 06:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -6.03% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 06:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.59% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 06:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.98% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 07:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.49% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 07:23Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.29% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 07:23Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.83% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 07:23Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.40% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 07:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.97% not above entry band +1.0% and price below 24h EMA
- 2026-09-16 07:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.67% not above entry band +1.0% and price below 24h EMA

## challenger: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,964.93 (started 10,000 at 2026-09-16 03:55Z), net -0.35% since start
- 24h -0.35%, 7d -0.35%, 30d -0.35%, max drawdown -0.35%
- fills 3 total, 3 in the last 7d
- costs 11.25 (fees 7.50 + slippage 3.75); gross pnl -23.83; cost coverage -2.12
- cash 2,492.50; positions: ADA 12763.5, ETH 1.04017, SOL 25.7086
- last run 2026-09-16 07:23Z; halted today: False

last decisions (newest last):

- 2026-09-16 05:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.96 not below -2.0
- 2026-09-16 05:21Z ETH buy target 0.25 (held 0.00) — enter long: z -2.51 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-09-16 05:21Z SOL buy target 0.25 (held 0.00) — enter long: z -2.23 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-09-16 05:21Z ADA buy target 0.25 (held 0.00) — enter long: z -2.24 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-09-16 05:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.27 not below -2.0
- 2026-09-16 05:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.69 not below -2.0
- 2026-09-16 06:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.85 not below -2.0
- 2026-09-16 06:28Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.37 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-09-16 06:28Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.23 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-09-16 06:28Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.21 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-09-16 06:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.24 not below -2.0
- 2026-09-16 06:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.63 not below -2.0
- 2026-09-16 07:23Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.80 not below -2.0
- 2026-09-16 07:23Z ETH hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.36 vs 240h mean (entry -2.0, exit -0.5); vol 59% -> weight 0.25
- 2026-09-16 07:23Z SOL hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: z -2.12 vs 240h mean (entry -2.0, exit -0.5); vol 57% -> weight 0.25
- 2026-09-16 07:23Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: z -2.17 vs 240h mean (entry -2.0, exit -0.5); vol 74% -> weight 0.25
- 2026-09-16 07:23Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.24 not below -2.0
- 2026-09-16 07:23Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.75 not below -2.0

last fills:

- 2026-09-16 05:21Z buy ETH 2,500 @ 2403.45 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy SOL 2,500 @ 97.2436 fee 2.50 slip 1.25
- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25

## Data

- BTC: 724 candles, 2026-08-17 03:00Z to 2026-09-16 06:00Z, missing hours in last 7d: 0
- ETH: 724 candles, 2026-08-17 03:00Z to 2026-09-16 06:00Z, missing hours in last 7d: 0
- SOL: 724 candles, 2026-08-17 03:00Z to 2026-09-16 06:00Z, missing hours in last 7d: 0
- ADA: 724 candles, 2026-08-17 03:00Z to 2026-09-16 06:00Z, missing hours in last 7d: 0
- AVAX: 724 candles, 2026-08-17 03:00Z to 2026-09-16 06:00Z, missing hours in last 7d: 0
- LINK: 724 candles, 2026-08-17 03:00Z to 2026-09-16 06:00Z, missing hours in last 7d: 0
