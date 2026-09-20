# quantloop summary — generated 2026-09-20 16:21Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 4.5 of 60, 55.5 days until the verdict
  so far: champion +12.72% (DD -3.54%, 36 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  market over the window: BTC +6.55%, equal weight basket of 10 pairs +15.51%, basket max drawdown -4%, basket realised vol 52% annualised
- challenger2: testing H2 since 2026-09-20 13:21Z, day 0.1 of 60, 59.9 days until the verdict
  so far: champion +2.64% (DD 0.00%, 8 fills) vs challenger2 +0.00% (DD 0.00%, 4 fills)
  market over the window: BTC +0.43%, equal weight basket of 10 pairs +1.82%, basket max drawdown 0%
- challenger3: idle (free for a hypothesis)
- free slots: challenger3
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,271.56 (started 10,000 at 2026-09-16 03:55Z), net +12.72% since start
- 24h +1.48%, 7d +12.72%, 30d +12.72%, max drawdown -3.54%
- fills 36 total, 36 in the last 7d
- costs 77.52 (fees 51.21 + slippage 26.30); gross pnl 1,349.08; cost coverage 17.40
- cash 1,298.45; positions: ADA 6238.97, AVAX 125.195, BTC 0.0174035, DOT 91.027, ETH 0.539165, LINK 114.186, LTC 24.4122, XRP 1008.59
- last run 2026-09-20 16:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 15:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z AVAX hold target 0.25 (held 0.28) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +42.84% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 15:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.010 below threshold 0.05 | stay long: 72h return +7.55% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 16:21Z BTC sell target 0.12 (held 0.24) — stay long: 72h return +5.45% vs exit band -1.0% and price above 24h EMA; realised vol 35% -> weight 0.25
- 2026-09-20 16:21Z ETH sell target 0.12 (held 0.24) — stay long: 72h return +5.83% vs exit band -1.0% and price above 24h EMA; realised vol 45% -> weight 0.25
- 2026-09-20 16:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 16:21Z ADA buy target 0.12 (held 0.00) — enter long: 72h return +11.05% vs entry band +1.0% and price above 24h EMA; realised vol 78% -> weight 0.25
- 2026-09-20 16:21Z AVAX sell target 0.12 (held 0.28) — stay long: 72h return +50.21% vs exit band -1.0% and price above 24h EMA; realised vol 114% -> weight 0.25
- 2026-09-20 16:21Z LINK buy target 0.12 (held 0.00) — enter long: 72h return +8.99% vs entry band +1.0% and price above 24h EMA; realised vol 62% -> weight 0.25
- 2026-09-20 16:21Z XRP buy target 0.12 (held 0.00) — enter long: 72h return +6.45% vs entry band +1.0% and price above 24h EMA; realised vol 82% -> weight 0.25
- 2026-09-20 16:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 16:21Z DOT buy target 0.12 (held 0.00) — enter long: 72h return +4.08% vs entry band +1.0% and price above 24h EMA; realised vol 87% -> weight 0.25
- 2026-09-20 16:21Z LTC sell target 0.12 (held 0.24) — stay long: 72h return +7.24% vs exit band -1.0% and price above 24h EMA; realised vol 55% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 6,302, gross pnl +44.81, +142 bps per round trip, avg half spread 2.3 bps, open 6238.97
- AVAX: 7 fills (3 buy / 4 sell), traded 12,613, gross pnl +844.66, +1339 bps per round trip, avg half spread 1.3 bps, open 125.195
- BTC: 3 fills (2 buy / 1 sell), traded 3,989, gross pnl +6.52, +33 bps per round trip, avg half spread 0.0 bps, open 0.0174035
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 4 fills (2 buy / 2 sell), traded 5,316, gross pnl +204.79, +771 bps per round trip, avg half spread 4.0 bps, open 91.027
- ETH: 3 fills (2 buy / 1 sell), traded 3,991, gross pnl +29.52, +148 bps per round trip, avg half spread 0.0 bps, open 0.539165
- LINK: 3 fills (2 buy / 1 sell), traded 4,401, gross pnl +45.99, +209 bps per round trip, avg half spread 2.6 bps, open 114.186
- LTC: 4 fills (2 buy / 2 sell), traded 6,057, gross pnl +121.30, +401 bps per round trip, avg half spread 2.5 bps, open 24.4122
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 3 fills (2 buy / 1 sell), traded 2,600, gross pnl -19.18, -148 bps per round trip, avg half spread 0.3 bps, open 1008.59

last fills:

- 2026-09-20 16:21Z sell BTC 1,292 @ 80987.8 fee 1.29 slip 0.65 (half spread 0.0 bps)
- 2026-09-20 16:21Z sell ETH 1,304 @ 2614.16 fee 1.30 slip 0.65 (half spread 0.0 bps)
- 2026-09-20 16:21Z buy ADA 1,411 @ 0.22613 fee 1.41 slip 0.72 (half spread 3.1 bps)
- 2026-09-20 16:21Z sell AVAX 1,737 @ 11.2564 fee 1.74 slip 0.87 (half spread 1.8 bps)
- 2026-09-20 16:21Z buy LINK 1,411 @ 12.3554 fee 1.41 slip 0.71 (half spread 2.4 bps)
- 2026-09-20 16:21Z buy XRP 1,411 @ 1.3988 fee 1.41 slip 0.71 (half spread 0.4 bps)
- 2026-09-20 16:21Z buy DOT 102 @ 1.12492 fee 0.10 slip 0.08 (half spread 5.8 bps)
- 2026-09-20 16:21Z sell LTC 1,300 @ 57.7361 fee 1.30 slip 0.65 (half spread 0.9 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +2.90%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 8 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-09-20 16:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 15:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.14 not below -2.0
- 2026-09-20 15:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.27 not below -2.0
- 2026-09-20 15:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +3.80 not below -2.0
- 2026-09-20 15:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.29 not below -2.0
- 2026-09-20 15:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0
- 2026-09-20 15:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.47 not below -2.0
- 2026-09-20 15:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.77 not below -2.0
- 2026-09-20 15:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.44 not below -2.0
- 2026-09-20 16:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.70 not below -2.0
- 2026-09-20 16:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.49 not below -2.0
- 2026-09-20 16:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.27 not below -2.0
- 2026-09-20 16:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.59 not below -2.0
- 2026-09-20 16:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +4.33 not below -2.0
- 2026-09-20 16:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.77 not below -2.0
- 2026-09-20 16:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.68 not below -2.0
- 2026-09-20 16:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.76 not below -2.0
- 2026-09-20 16:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.02 not below -2.0
- 2026-09-20 16:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.72 not below -2.0

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

- equity 10,965.71 (started 10,000 at 2026-09-16 23:20Z), net +9.66% since start
- 24h -1.28%, 7d +9.66%, 30d +9.66%, max drawdown -3.54%
- fills 32 total, 32 in the last 7d
- costs 78.97 (fees 52.21 + slippage 26.76); gross pnl 1,044.68; cost coverage 13.23
- cash 10,965.71; positions: none
- last run 2026-09-20 16:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 15:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 828 candles, need 1610
- 2026-09-20 15:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 828 candles, need 1610
- 2026-09-20 15:20Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 828 candles, need 1610
- 2026-09-20 15:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 828 candles, need 1610
- 2026-09-20 15:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 800 candles, need 1610
- 2026-09-20 15:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 800 candles, need 1610
- 2026-09-20 15:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 800 candles, need 1610
- 2026-09-20 15:20Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 800 candles, need 1610
- 2026-09-20 16:21Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 829 candles, need 1610
- 2026-09-20 16:21Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 829 candles, need 1610
- 2026-09-20 16:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 829 candles, need 1610
- 2026-09-20 16:21Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 829 candles, need 1610
- 2026-09-20 16:21Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 829 candles, need 1610
- 2026-09-20 16:21Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 829 candles, need 1610
- 2026-09-20 16:21Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 801 candles, need 1610
- 2026-09-20 16:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 801 candles, need 1610
- 2026-09-20 16:21Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 801 candles, need 1610
- 2026-09-20 16:21Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: only 801 candles, need 1610

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 3 fills (2 buy / 1 sell), traded 5,380, gross pnl -12.20, -45 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 3 fills (2 buy / 1 sell), traded 5,361, gross pnl -9.44, -35 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 03:22Z sell DOGE 1,488 @ 0.0859724 fee 1.49 slip 0.74 (half spread 1.7 bps)
- 2026-09-20 03:22Z buy LTC 1,143 @ 57.4537 fee 1.14 slip 0.57 (half spread 2.6 bps)
- 2026-09-20 04:22Z buy BTC 1,491 @ 80368.4 fee 1.49 slip 0.75 (half spread 0.0 bps)
- 2026-09-20 04:22Z buy ETH 2,440 @ 2581.92 fee 2.44 slip 1.22 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)

## challenger3: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,271.56 (started 10,000 at 2026-09-16 23:20Z), net +12.72% since start
- 24h +1.48%, 7d +12.72%, 30d +12.72%, max drawdown -3.54%
- fills 36 total, 36 in the last 7d
- costs 77.52 (fees 51.21 + slippage 26.30); gross pnl 1,349.08; cost coverage 17.40
- cash 1,298.45; positions: ADA 6238.97, AVAX 125.195, BTC 0.0174035, DOT 91.027, ETH 0.539165, LINK 114.186, LTC 24.4122, XRP 1008.59
- last run 2026-09-20 16:21Z; halted today: False

last decisions (newest last):

- 2026-09-20 15:20Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z AVAX hold target 0.25 (held 0.28) — hold: weight change -0.028 below threshold 0.05 | stay long: 72h return +42.84% vs exit band -1.0% and price above 24h EMA; realised vol ...
- 2026-09-20 15:20Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 15:20Z LTC hold target 0.25 (held 0.24) — hold: weight change +0.010 below threshold 0.05 | stay long: 72h return +7.55% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-09-20 16:21Z BTC sell target 0.12 (held 0.24) — stay long: 72h return +5.45% vs exit band -1.0% and price above 24h EMA; realised vol 35% -> weight 0.25
- 2026-09-20 16:21Z ETH sell target 0.12 (held 0.24) — stay long: 72h return +5.83% vs exit band -1.0% and price above 24h EMA; realised vol 45% -> weight 0.25
- 2026-09-20 16:21Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 16:21Z ADA buy target 0.12 (held 0.00) — enter long: 72h return +11.05% vs entry band +1.0% and price above 24h EMA; realised vol 78% -> weight 0.25
- 2026-09-20 16:21Z AVAX sell target 0.12 (held 0.28) — stay long: 72h return +50.21% vs exit band -1.0% and price above 24h EMA; realised vol 114% -> weight 0.25
- 2026-09-20 16:21Z LINK buy target 0.12 (held 0.00) — enter long: 72h return +8.99% vs entry band +1.0% and price above 24h EMA; realised vol 62% -> weight 0.25
- 2026-09-20 16:21Z XRP buy target 0.12 (held 0.00) — enter long: 72h return +6.45% vs entry band +1.0% and price above 24h EMA; realised vol 82% -> weight 0.25
- 2026-09-20 16:21Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-09-20 16:21Z DOT buy target 0.12 (held 0.00) — enter long: 72h return +4.08% vs entry band +1.0% and price above 24h EMA; realised vol 87% -> weight 0.25
- 2026-09-20 16:21Z LTC sell target 0.12 (held 0.24) — stay long: 72h return +7.24% vs exit band -1.0% and price above 24h EMA; realised vol 55% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (2 buy / 2 sell), traded 6,302, gross pnl +44.81, +142 bps per round trip, avg half spread 2.3 bps, open 6238.97
- AVAX: 7 fills (3 buy / 4 sell), traded 12,613, gross pnl +844.66, +1339 bps per round trip, avg half spread 1.3 bps, open 125.195
- BTC: 3 fills (2 buy / 1 sell), traded 3,989, gross pnl +6.52, +33 bps per round trip, avg half spread 0.0 bps, open 0.0174035
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 4 fills (2 buy / 2 sell), traded 5,316, gross pnl +204.79, +771 bps per round trip, avg half spread 4.0 bps, open 91.027
- ETH: 3 fills (2 buy / 1 sell), traded 3,991, gross pnl +29.52, +148 bps per round trip, avg half spread 0.0 bps, open 0.539165
- LINK: 3 fills (2 buy / 1 sell), traded 4,401, gross pnl +45.99, +209 bps per round trip, avg half spread 2.6 bps, open 114.186
- LTC: 4 fills (2 buy / 2 sell), traded 6,057, gross pnl +121.30, +401 bps per round trip, avg half spread 2.5 bps, open 24.4122
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 3 fills (2 buy / 1 sell), traded 2,600, gross pnl -19.18, -148 bps per round trip, avg half spread 0.3 bps, open 1008.59

last fills:

- 2026-09-20 16:21Z sell BTC 1,292 @ 80987.8 fee 1.29 slip 0.65 (half spread 0.0 bps)
- 2026-09-20 16:21Z sell ETH 1,304 @ 2614.16 fee 1.30 slip 0.65 (half spread 0.0 bps)
- 2026-09-20 16:21Z buy ADA 1,411 @ 0.22613 fee 1.41 slip 0.72 (half spread 3.1 bps)
- 2026-09-20 16:21Z sell AVAX 1,737 @ 11.2564 fee 1.74 slip 0.87 (half spread 1.8 bps)
- 2026-09-20 16:21Z buy LINK 1,411 @ 12.3554 fee 1.41 slip 0.71 (half spread 2.4 bps)
- 2026-09-20 16:21Z buy XRP 1,411 @ 1.3988 fee 1.41 slip 0.71 (half spread 0.4 bps)
- 2026-09-20 16:21Z buy DOT 102 @ 1.12492 fee 0.10 slip 0.08 (half spread 5.8 bps)
- 2026-09-20 16:21Z sell LTC 1,300 @ 57.7361 fee 1.30 slip 0.65 (half spread 0.9 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 829 candles, 2026-08-17 03:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 829 candles, 2026-08-17 03:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.2 bps
- SOL: live 829 candles, 2026-08-17 03:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- ADA: live 829 candles, 2026-08-17 03:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- AVAX: live 829 candles, 2026-08-17 03:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.5 bps
- LINK: live 829 candles, 2026-08-17 03:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.2 bps
- XRP: live 801 candles, 2026-08-18 07:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.4 bps
- DOGE: live 801 candles, 2026-08-18 07:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.6 bps
- DOT: live 801 candles, 2026-08-18 07:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- LTC: live 801 candles, 2026-08-18 07:00Z to 2026-09-20 15:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.7 bps
