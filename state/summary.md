# quantloop summary — generated 2026-10-02 14:27Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 16.4 of 60, 43.6 days until the verdict
  so far: champion +12.70% (DD -12.10%, 146 fills) vs challenger1 +3.01% (DD -1.00%, 8 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -2.05% (usual 0.54, this window 0.71) vs challenger1 -7.16% (usual 0.37, this window 0.09); the rule compares on skill, daily edge t -0.5 over 17 days
  market over the window: BTC +14.04%, equal weight basket of 10 pairs +27.42%, basket max drawdown -7%, basket realised vol 59% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 11.3 of 60, 48.7 days until the verdict
  so far: champion -1.92% (DD -12.10%, 108 fills) vs challenger2 +0.19% (DD -1.17%, 2 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -5.32% (usual 0.54, this window 0.72) vs challenger2 -1.61% (usual 0.29, this window 0.11); the rule compares on skill, daily edge t +0.4 over 12 days
  market over the window: BTC +3.36%, equal weight basket of 10 pairs +6.30%, basket max drawdown -7%, basket realised vol 60% annualised
- challenger3: testing H3 since 2026-09-25 03:21Z, day 7.5 of 60, 52.5 days until the verdict
  so far: champion -5.03% (DD -12.10%, 88 fills) vs challenger3 -0.92% (DD -4.74%, 111 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -7.15% (usual 0.55, this window 0.70) vs challenger3 -1.12% (usual 0.05, this window 0.59); the rule compares on skill, daily edge t +1.2 over 8 days
  market over the window: BTC +2.79%, equal weight basket of 10 pairs +3.87%, basket max drawdown -5%, basket realised vol 57% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 6.7 of 60, 53.3 days until the verdict
  so far: champion -7.81% (DD -12.10%, 80 fills) vs challenger4 +0.76% (DD -4.37%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -8.10% (usual 0.55, this window 0.66) vs challenger4 +0.50% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.6 over 7 days
  market over the window: BTC +2.97%, equal weight basket of 10 pairs +0.53%, basket max drawdown -5%, basket realised vol 58% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts; only the end of window rule counts

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 11,269.78 (started 10,000 at 2026-09-16 03:55Z), net +12.70% since start
- 24h +1.65%, 7d -7.16%, 30d +12.70%, max drawdown -12.10%
- fills 146 total, 82 in the last 7d
- costs 339.96 (fees 224.66 + slippage 115.29); gross pnl 1,609.74; cost coverage 4.74
- cash 2,498.66; positions: ADA 4960.19, BTC 0.0144486, DOGE 13064.2, DOT 1031.85, ETH 0.453545, LTC 17.8332, SOL 10.2566
- last run 2026-10-02 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-02 13:26Z SOL hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +1.38% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-02 13:26Z ADA hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +1.79% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-02 13:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.10% not above entry band +1.0%
- 2026-10-02 13:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.38% not above entry band +1.0%
- 2026-10-02 13:26Z XRP hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return -0.35% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-02 13:26Z DOGE hold target 0.12 (held 0.11) — hold: weight change +0.013 below threshold 0.05 | stay long: 72h return +1.34% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-02 13:26Z DOT hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +1.18% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-02 13:26Z LTC hold target 0.12 (held 0.11) — hold: weight change +0.014 below threshold 0.05 | stay long: 72h return +1.66% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-02 14:27Z BTC hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: 72h return +2.82% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-02 14:27Z ETH hold target 0.14 (held 0.11) — hold: weight change +0.033 below threshold 0.05 | stay long: 72h return +0.64% vs exit band -1.0% and price above 24h EMA; realised vol 3...
- 2026-10-02 14:27Z SOL hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: 72h return +0.87% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-10-02 14:27Z ADA hold target 0.14 (held 0.11) — hold: weight change +0.031 below threshold 0.05 | stay long: 72h return +1.44% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-10-02 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.50% not above entry band +1.0%
- 2026-10-02 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.07% not above entry band +1.0% and price below 24h EMA
- 2026-10-02 14:27Z XRP sell target 0.00 (held 0.11) — exit: 72h return -1.04% fell below exit band -1.0%
- 2026-10-02 14:27Z DOGE hold target 0.14 (held 0.11) — hold: weight change +0.031 below threshold 0.05 | stay long: 72h return +0.86% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-02 14:27Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.031 below threshold 0.05 | stay long: 72h return +1.11% vs exit band -1.0% and price above 24h EMA; realised vol 9...
- 2026-10-02 14:27Z LTC hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: 72h return +4.05% vs exit band -1.0% and price above 24h EMA; realised vol 6...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 15 fills (7 buy / 8 sell), traded 23,965, gross pnl +91.90, +77 bps per round trip, avg half spread 2.2 bps, open 4960.19
- AVAX: 22 fills (9 buy / 13 sell), traded 38,374, gross pnl +570.74, +297 bps per round trip, avg half spread 1.3 bps
- BTC: 8 fills (4 buy / 4 sell), traded 9,801, gross pnl +117.01, +239 bps per round trip, avg half spread 0.3 bps, open 0.0144486
- DOGE: 15 fills (8 buy / 7 sell), traded 21,003, gross pnl -19.57, -19 bps per round trip, avg half spread 1.2 bps, open 13064.2
- DOT: 16 fills (9 buy / 7 sell), traded 18,899, gross pnl +216.72, +229 bps per round trip, avg half spread 2.9 bps, open 1031.85
- ETH: 12 fills (5 buy / 7 sell), traded 18,418, gross pnl +48.01, +52 bps per round trip, avg half spread 0.1 bps, open 0.453545
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 12 fills (5 buy / 7 sell), traded 20,731, gross pnl +522.40, +504 bps per round trip, avg half spread 2.0 bps, open 17.8332
- SOL: 10 fills (6 buy / 4 sell), traded 13,939, gross pnl +53.90, +77 bps per round trip, avg half spread 0.5 bps, open 10.2566
- XRP: 14 fills (6 buy / 8 sell), traded 21,113, gross pnl +173.17, +164 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-02 03:24Z sell AVAX 614 @ 10.9795 fee 0.61 slip 0.31 (half spread 0.9 bps)
- 2026-10-02 03:24Z sell XRP 606 @ 1.50033 fee 0.61 slip 0.30 (half spread 0.6 bps)
- 2026-10-02 03:24Z sell DOGE 606 @ 0.094184 fee 0.61 slip 0.30 (half spread 0.0 bps)
- 2026-10-02 03:24Z buy SOL 1,231 @ 120.055 fee 1.23 slip 0.62 (half spread 0.4 bps)
- 2026-10-02 03:24Z buy DOT 1,231 @ 1.19335 fee 1.23 slip 0.62 (half spread 1.3 bps)
- 2026-10-02 03:24Z buy LTC 1,224 @ 68.6343 fee 1.22 slip 0.61 (half spread 1.5 bps)
- 2026-10-02 08:26Z sell AVAX 1,247 @ 11.1254 fee 1.25 slip 0.62 (half spread 0.9 bps)
- 2026-10-02 14:27Z sell XRP 1,254 @ 1.52952 fee 1.25 slip 0.63 (half spread 0.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,289.77 (started 10,000 at 2026-09-16 03:55Z), net +2.90% since start
- 24h +0.00%, 7d +0.00%, 30d +2.90%, max drawdown -1.00%
- fills 8 total, 0 in the last 7d
- costs 30.43 (fees 20.29 + slippage 10.14); gross pnl 320.20; cost coverage 10.52
- cash 10,289.77; positions: none
- last run 2026-10-02 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-02 13:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.54 not below -2.0
- 2026-10-02 13:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.31 not below -2.0
- 2026-10-02 13:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.17 not below -2.0
- 2026-10-02 13:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.64 not below -2.0
- 2026-10-02 13:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.56 not below -2.0
- 2026-10-02 13:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.55 not below -2.0
- 2026-10-02 13:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.67 not below -2.0
- 2026-10-02 13:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.41 not below -2.0
- 2026-10-02 14:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.38 not below -2.0
- 2026-10-02 14:27Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.83 not below -2.0
- 2026-10-02 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.32 not below -2.0
- 2026-10-02 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.04 not below -2.0
- 2026-10-02 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.80 not below -2.0
- 2026-10-02 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.53 not below -2.0
- 2026-10-02 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.28 not below -2.0
- 2026-10-02 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.33 not below -2.0
- 2026-10-02 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.65 not below -2.0
- 2026-10-02 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.78 not below -2.0

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

- equity 10,986.80 (started 10,000 at 2026-09-16 23:20Z), net +9.87% since start
- 24h +0.96%, 7d +0.19%, 30d +9.87%, max drawdown -3.54%
- fills 34 total, 2 in the last 7d
- costs 87.18 (fees 57.69 + slippage 29.49); gross pnl 1,073.98; cost coverage 12.32
- cash 5,481.58; positions: BTC 0.0320792, ETH 1.00083
- last run 2026-10-02 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-02 13:26Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 13:26Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z BTC hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: price 8.656e+04 still above 72h low 8.3e+04; realised vol 32% -> weight 0.25
- 2026-10-02 14:27Z ETH hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 2744 still above 72h low 2661; realised vol 37% -> weight 0.25
- 2026-10-02 14:27Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-02 14:27Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 4 fills (3 buy / 1 sell), traded 8,117, gross pnl +20.67, +51 bps per round trip, avg half spread 0.0 bps, open 0.0320792
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 4 fills (3 buy / 1 sell), traded 8,103, gross pnl -13.00, -32 bps per round trip, avg half spread 0.0 bps, open 1.00083
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

- equity 11,406.86 (started 10,000 at 2026-09-16 23:20Z), net +14.07% since start
- 24h +1.38%, 7d -0.92%, 30d +14.07%, max drawdown -9.51%
- fills 160 total, 111 in the last 7d
- costs 353.37 (fees 232.48 + slippage 120.89); gross pnl 1,760.23; cost coverage 4.98
- cash -0.00; positions: ADA 7552.28, DOGE 16991.3, DOT 1039.57, ETH 0.59806, LINK 117.602, LTC 23.3343, SOL 13.2807
- last run 2026-10-02 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-02 13:26Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: price 122.5 still above the 48h low 117.1; realised vol 59% -> weight 0.25
- 2026-10-02 13:26Z ADA hold target 0.14 (held 0.17) — hold: weight change -0.026 below threshold 0.05 | stay long: price 0.257 still above the 48h low 0.2425; realised vol 88% -> weight 0.25
- 2026-10-02 13:26Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.24 not above reaction high 11.55
- 2026-10-02 13:26Z LINK hold target 0.14 (held 0.15) — hold: weight change -0.005 below threshold 0.05 | stay long: price 14.44 still above the 48h low 14.18; realised vol 94% -> weight 0.25
- 2026-10-02 13:26Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.542 not above reaction high 1.638
- 2026-10-02 13:26Z DOGE hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.09715 still above the 48h low 0.09373; realised vol 63% -> weight 0.25
- 2026-10-02 13:26Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: price 1.224 still above the 48h low 1.162; realised vol 98% -> weight 0.25
- 2026-10-02 13:26Z LTC hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: price 69.88 still above the 48h low 66.15; realised vol 61% -> weight 0.25
- 2026-10-02 14:27Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.542e+04 (need +10.0%)
- 2026-10-02 14:27Z ETH hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: price 2744 still above the 48h low 2669; realised vol 37% -> weight 0.25
- 2026-10-02 14:27Z SOL hold target 0.14 (held 0.14) — hold: weight change +0.001 below threshold 0.05 | stay long: price 122 still above the 48h low 117.1; realised vol 58% -> weight 0.25
- 2026-10-02 14:27Z ADA hold target 0.14 (held 0.17) — hold: weight change -0.026 below threshold 0.05 | stay long: price 0.2555 still above the 48h low 0.2425; realised vol 88% -> weight 0.25
- 2026-10-02 14:27Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 11.1 not above reaction high 11.55
- 2026-10-02 14:27Z LINK hold target 0.14 (held 0.15) — hold: weight change -0.005 below threshold 0.05 | stay long: price 14.36 still above the 48h low 14.18; realised vol 94% -> weight 0.25
- 2026-10-02 14:27Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.532 not above reaction high 1.638
- 2026-10-02 14:27Z DOGE hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.09661 still above the 48h low 0.09373; realised vol 63% -> weight 0.25
- 2026-10-02 14:27Z DOT hold target 0.14 (held 0.11) — hold: weight change +0.032 below threshold 0.05 | stay long: price 1.223 still above the 48h low 1.162; realised vol 97% -> weight 0.25
- 2026-10-02 14:27Z LTC hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: price 71.13 still above the 48h low 66.15; realised vol 63% -> weight 0.25

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 23 fills (11 buy / 12 sell), traded 43,535, gross pnl +137.43, +63 bps per round trip, avg half spread 2.2 bps, open 7552.28
- AVAX: 18 fills (7 buy / 11 sell), traded 27,169, gross pnl +788.83, +581 bps per round trip, avg half spread 1.6 bps
- BTC: 4 fills (2 buy / 2 sell), traded 5,452, gross pnl +59.67, +219 bps per round trip, avg half spread 0.6 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 9,859, gross pnl +6.34, +13 bps per round trip, avg half spread 1.6 bps, open 16991.3
- DOT: 21 fills (10 buy / 11 sell), traded 33,825, gross pnl +55.14, +33 bps per round trip, avg half spread 2.7 bps, open 1039.57
- ETH: 8 fills (4 buy / 4 sell), traded 9,465, gross pnl +119.10, +252 bps per round trip, avg half spread 0.1 bps, open 0.59806
- LINK: 19 fills (9 buy / 10 sell), traded 30,334, gross pnl +246.28, +162 bps per round trip, avg half spread 2.7 bps, open 117.602
- LTC: 35 fills (18 buy / 17 sell), traded 43,924, gross pnl +187.18, +85 bps per round trip, avg half spread 1.9 bps, open 23.3343
- SOL: 16 fills (8 buy / 8 sell), traded 21,953, gross pnl +72.19, +66 bps per round trip, avg half spread 0.5 bps, open 13.2807
- XRP: 6 fills (3 buy / 3 sell), traded 6,959, gross pnl +88.07, +253 bps per round trip, avg half spread 0.6 bps

last fills:

- 2026-10-01 18:29Z buy LINK 1,690 @ 14.3682 fee 1.69 slip 0.84 (half spread 0.0 bps)
- 2026-10-02 03:24Z sell ADA 919 @ 0.248061 fee 0.92 slip 0.46 (half spread 2.7 bps)
- 2026-10-02 03:24Z buy SOL 917 @ 120.055 fee 0.92 slip 0.46 (half spread 0.4 bps)
- 2026-10-02 05:23Z sell ETH 640 @ 2729.06 fee 0.64 slip 0.32 (half spread 0.5 bps)
- 2026-10-02 05:23Z sell DOGE 643 @ 0.0960575 fee 0.64 slip 0.32 (half spread 0.9 bps)
- 2026-10-02 05:23Z sell LTC 686 @ 69.945 fee 0.69 slip 0.34 (half spread 2.9 bps)
- 2026-10-02 05:23Z buy SOL 694 @ 123.016 fee 0.69 slip 0.35 (half spread 0.4 bps)
- 2026-10-02 05:23Z buy DOT 1,271 @ 1.22286 fee 1.27 slip 0.64 (half spread 1.2 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,331.12 (started 10,000 at 2026-09-25 04:23Z), net +3.31% since start
- 24h +2.27%, 7d +1.20%, 30d +3.39%, max drawdown -4.37%
- fills 23 total, 12 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl 372.69; cost coverage 8.97
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-02 14:27Z; halted today: False

last decisions (newest last):

- 2026-10-02 13:26Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +25.49% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +32.53% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.008 below threshold 0.05 | stay long: 720h return +58.50% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +31.69% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +17.03% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +20.27% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +45.91% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 13:26Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +43.37% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +12.26% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +14.26% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +23.08% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +30.14% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z AVAX hold target 0.10 (held 0.09) — hold: weight change +0.007 below threshold 0.05 | stay long: 720h return +55.19% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +28.93% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +14.28% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +18.38% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +44.23% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-02 14:27Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +44.57% vs exit band -5.0% and price above 168h EMA; realised vo...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +70.54, +352 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fills (1 buy / 0 sell), traded 907, gross pnl +49.19, +1084 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +29.54, +568 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fills (1 buy / 0 sell), traded 1,031, gross pnl -21.77, -422 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl +31.43, +206 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fills (1 buy / 0 sell), traded 1,040, gross pnl +18.33, +353 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +135.73, +669 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -2.42, -12 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl +19.01, +158 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl +43.12, +141 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1115 candles, 2026-08-17 03:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.0 bps
- ETH: live 1115 candles, 2026-08-17 03:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.1 bps
- SOL: live 1115 candles, 2026-08-17 03:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- ADA: live 1115 candles, 2026-08-17 03:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.0 bps
- AVAX: live 1115 candles, 2026-08-17 03:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 1.1 bps
- LINK: live 1115 candles, 2026-08-17 03:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16762 candles from 2024-09-17; avg half spread last 7d 2.1 bps
- XRP: live 1087 candles, 2026-08-18 07:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOGE: live 1087 candles, 2026-08-18 07:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 0.5 bps
- DOT: live 1087 candles, 2026-08-18 07:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 2.3 bps
- LTC: live 1087 candles, 2026-08-18 07:00Z to 2026-10-02 13:00Z, missing hours in last 7d: 0; history 16790 candles from 2024-09-17; avg half spread last 7d 1.6 bps
