# quantloop summary — generated 2026-09-18 00:28Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 1.8 of 60, 58.2 days until the verdict
  so far: champion +1.21% (DD -0.60%, 4 fills) vs challenger1 +2.18% (DD -1.00%, 6 fills)
  market over the window: BTC +0.59%, equal weight basket of 10 pairs +3.94%, basket realised vol 40% annualised
- challenger2: idle (free for a hypothesis)
- challenger3: idle (free for a hypothesis)
- free slots: challenger2, challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,121.22 (started 10,000 at 2026-09-16 03:55Z), net +1.21% since start
- 24h +1.25%, 7d +1.21%, 30d +1.21%, max drawdown -0.60%
- fills 4 total, 4 in the last 7d
- costs 15.19 (fees 10.07 + slippage 5.13); gross pnl 136.41; cost coverage 8.98
- cash 4,982.71; positions: DOT 2418.21, LTC 46.9081
- last run 2026-09-18 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-17 23:18Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0%
- 2026-09-17 23:18Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.16% not above entry band +1.0%
- 2026-09-17 23:18Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0%
- 2026-09-17 23:18Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.87% not above entry band +1.0%
- 2026-09-17 23:18Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.77% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 23:18Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.09% not above entry band +1.0%
- 2026-09-17 23:18Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +6.57% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 23:18Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.96% not above entry band +1.0%
- 2026-09-18 00:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.35% not above entry band +1.0% and price below 24h EMA
- 2026-09-18 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.80% not above entry band +1.0%
- 2026-09-18 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.01% not above entry band +1.0%
- 2026-09-18 00:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.93% not above entry band +1.0%
- 2026-09-18 00:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.64% not above entry band +1.0%
- 2026-09-18 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.24% not above entry band +1.0%
- 2026-09-18 00:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.93% not above entry band +1.0% and price below 24h EMA
- 2026-09-18 00:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.37% not above entry band +1.0%
- 2026-09-18 00:28Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +7.45% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-18 00:28Z LTC buy target 0.25 (held 0.00) — enter long: 72h return +1.52% vs entry band +1.0% and price above 24h EMA; realised vol 52% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 2 fills (1 buy / 1 sell), traded 5,030, gross pnl +32.31, +128 bps per round trip, avg half spread 0.7 bps
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +104.10, +831 bps per round trip, avg half spread 3.4 bps, open 2418.21
- LTC: 1 fills (1 buy / 0 sell), traded 2,531, gross pnl -0.00, -0 bps per round trip, avg half spread 2.8 bps, open 46.9081

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)
- 2026-09-17 21:21Z sell AVAX 2,530 @ 7.5947 fee 2.53 slip 1.27 (half spread 0.7 bps)
- 2026-09-18 00:28Z buy LTC 2,531 @ 53.962 fee 2.53 slip 1.26 (half spread 2.8 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,206.76 (started 10,000 at 2026-09-16 03:55Z), net +2.07% since start
- 24h +1.38%, 7d +2.07%, 30d +2.07%, max drawdown -1.00%
- fills 6 total, 6 in the last 7d
- costs 22.68 (fees 15.12 + slippage 7.56); gross pnl 229.44; cost coverage 10.11
- cash 5,129.36; positions: ADA 12763.5, BTC 0.0328342
- last run 2026-09-18 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-17 23:18Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-09-17 23:18Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -0.83 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-09-17 23:18Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.03 not below -2.0
- 2026-09-17 23:18Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.46 not below -2.0
- 2026-09-17 23:18Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.46 not below -2.0
- 2026-09-17 23:18Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.94 not below -2.0
- 2026-09-17 23:18Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.31 not below -2.0
- 2026-09-17 23:18Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.51 not below -2.0
- 2026-09-18 00:28Z BTC hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: z -1.03 vs 240h mean (entry -2.0, exit -0.5); vol 32% -> weight 0.25
- 2026-09-18 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.74 not below -2.0
- 2026-09-18 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.25 not below -2.0
- 2026-09-18 00:28Z ADA hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: z -0.64 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-09-18 00:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.14 not below -2.0
- 2026-09-18 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.40 not below -2.0
- 2026-09-18 00:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.43 not below -2.0
- 2026-09-18 00:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.87 not below -2.0
- 2026-09-18 00:28Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.36 not below -2.0
- 2026-09-18 00:28Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.57 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 1 fills (1 buy / 0 sell), traded 2,500, gross pnl -2,498.75, -19990 bps per round trip, open 12763.5
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

## challenger2: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,121.22 (started 10,000 at 2026-09-16 23:20Z), net +1.21% since start
- 24h +1.25%, 7d +1.21%, 30d +1.21%, max drawdown -0.60%
- fills 4 total, 4 in the last 7d
- costs 15.19 (fees 10.07 + slippage 5.13); gross pnl 136.41; cost coverage 8.98
- cash 4,982.71; positions: DOT 2418.21, LTC 46.9081
- last run 2026-09-18 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-17 23:18Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0%
- 2026-09-17 23:18Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.16% not above entry band +1.0%
- 2026-09-17 23:18Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0%
- 2026-09-17 23:18Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.87% not above entry band +1.0%
- 2026-09-17 23:18Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.77% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 23:18Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.09% not above entry band +1.0%
- 2026-09-17 23:18Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +6.57% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 23:18Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.96% not above entry band +1.0%
- 2026-09-18 00:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.35% not above entry band +1.0% and price below 24h EMA
- 2026-09-18 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.80% not above entry band +1.0%
- 2026-09-18 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.01% not above entry band +1.0%
- 2026-09-18 00:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.93% not above entry band +1.0%
- 2026-09-18 00:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.64% not above entry band +1.0%
- 2026-09-18 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.24% not above entry band +1.0%
- 2026-09-18 00:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.93% not above entry band +1.0% and price below 24h EMA
- 2026-09-18 00:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.37% not above entry band +1.0%
- 2026-09-18 00:28Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +7.45% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-18 00:28Z LTC buy target 0.25 (held 0.00) — enter long: 72h return +1.52% vs entry band +1.0% and price above 24h EMA; realised vol 52% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 2 fills (1 buy / 1 sell), traded 5,030, gross pnl +32.31, +128 bps per round trip, avg half spread 0.7 bps
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +104.10, +831 bps per round trip, avg half spread 3.4 bps, open 2418.21
- LTC: 1 fills (1 buy / 0 sell), traded 2,531, gross pnl -0.00, -0 bps per round trip, avg half spread 2.8 bps, open 46.9081

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)
- 2026-09-17 21:21Z sell AVAX 2,530 @ 7.5947 fee 2.53 slip 1.27 (half spread 0.7 bps)
- 2026-09-18 00:28Z buy LTC 2,531 @ 53.962 fee 2.53 slip 1.26 (half spread 2.8 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,121.22 (started 10,000 at 2026-09-16 23:20Z), net +1.21% since start
- 24h +1.25%, 7d +1.21%, 30d +1.21%, max drawdown -0.60%
- fills 4 total, 4 in the last 7d
- costs 15.19 (fees 10.07 + slippage 5.13); gross pnl 136.41; cost coverage 8.98
- cash 4,982.71; positions: DOT 2418.21, LTC 46.9081
- last run 2026-09-18 00:28Z; halted today: False

last decisions (newest last):

- 2026-09-17 23:18Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.48% not above entry band +1.0%
- 2026-09-17 23:18Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.16% not above entry band +1.0%
- 2026-09-17 23:18Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.51% not above entry band +1.0%
- 2026-09-17 23:18Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.87% not above entry band +1.0%
- 2026-09-17 23:18Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -9.77% not above entry band +1.0% and price below 24h EMA
- 2026-09-17 23:18Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.09% not above entry band +1.0%
- 2026-09-17 23:18Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +6.57% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-17 23:18Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.96% not above entry band +1.0%
- 2026-09-18 00:28Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.35% not above entry band +1.0% and price below 24h EMA
- 2026-09-18 00:28Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.80% not above entry band +1.0%
- 2026-09-18 00:28Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.01% not above entry band +1.0%
- 2026-09-18 00:28Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.93% not above entry band +1.0%
- 2026-09-18 00:28Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.64% not above entry band +1.0%
- 2026-09-18 00:28Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.24% not above entry band +1.0%
- 2026-09-18 00:28Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -8.93% not above entry band +1.0% and price below 24h EMA
- 2026-09-18 00:28Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.37% not above entry band +1.0%
- 2026-09-18 00:28Z DOT hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: 72h return +7.45% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-09-18 00:28Z LTC buy target 0.25 (held 0.00) — enter long: 72h return +1.52% vs entry band +1.0% and price above 24h EMA; realised vol 52% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- AVAX: 2 fills (1 buy / 1 sell), traded 5,030, gross pnl +32.31, +128 bps per round trip, avg half spread 0.7 bps
- DOT: 1 fills (1 buy / 0 sell), traded 2,506, gross pnl +104.10, +831 bps per round trip, avg half spread 3.4 bps, open 2418.21
- LTC: 1 fills (1 buy / 0 sell), traded 2,531, gross pnl -0.00, -0 bps per round trip, avg half spread 2.8 bps, open 46.9081

last fills:

- 2026-09-17 00:28Z buy AVAX 2,500 @ 7.50525 fee 2.50 slip 1.25
- 2026-09-17 13:23Z buy DOT 2,506 @ 1.03621 fee 2.51 slip 1.35 (half spread 3.4 bps)
- 2026-09-17 21:21Z sell AVAX 2,530 @ 7.5947 fee 2.53 slip 1.27 (half spread 0.7 bps)
- 2026-09-18 00:28Z buy LTC 2,531 @ 53.962 fee 2.53 slip 1.26 (half spread 2.8 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 765 candles, 2026-08-17 03:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 765 candles, 2026-08-17 03:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 765 candles, 2026-08-17 03:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 765 candles, 2026-08-17 03:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.7 bps
- AVAX: live 765 candles, 2026-08-17 03:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.3 bps
- LINK: live 765 candles, 2026-08-17 03:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- XRP: live 737 candles, 2026-08-18 07:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.3 bps
- DOGE: live 737 candles, 2026-08-18 07:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOT: live 737 candles, 2026-08-18 07:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- LTC: live 737 candles, 2026-08-18 07:00Z to 2026-09-17 23:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.4 bps
