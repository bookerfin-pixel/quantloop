# quantloop summary — generated 2026-10-07 02:25Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 141 of the last 168 (2 of them replayed after a missed run)
- 27 hours in the last 7 days have no decision at all: the run never happened and was not replayed (longest gap 7.2 hours, ending 2026-10-04 12:25Z). Accounts held their books through those hours; every account shares the same gaps
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 20.9 of 60, 39.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion +6.20% (max drawdown -15.08%, 202 fills) vs challenger1 +4.09% (max drawdown -1.00%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -6.79% (usual 0.54, this window 0.74) vs challenger1 -4.87% (usual 0.37, this window 0.10); the rule compares on skill, daily edge t +0.07 over 21 days
  trades: its 5 finished trades made +3.98% of its starting equity after costs (5 won, 0 lost). Of value on today's numbers, which keeps a test that does not pass the rule (kept is not promoted)
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.96 over 21 days)
  fills: 10 in 20.9 days, 3 of them in the hour it began; at this pace about 23 by day 60, under the 30 a promotion there needs, and about 43 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be kept at day 60 on the value of its trades without passing the rule, the same as under its own rule. From there the two rules are one: 60 more days, and a promotion asks for a daily skill t of 1.0 over all 120 (its daily skill t is -0.96 so far)
  market over the window: BTC +11.25%, equal weight basket of 10 pairs +24.15%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 15.8 of 60, 44.2 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -7.57% (max drawdown -15.08%, 164 fills) vs challenger2 -1.73% (max drawdown -2.21%, 4 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -10.09% (usual 0.54, this window 0.75) vs challenger2 -3.06% (usual 0.29, this window 0.22); the rule compares on skill, daily edge t +0.91 over 16 days
  trades: its 2 finished trades made -1.73% of its starting equity after costs (0 won, 2 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -1.15 over 16 days)
  fills: 4 in 15.8 days; at this pace about 15 by day 60, under the 30 a promotion there needs, and about 30 by day 120. Short of them at day 60 it is kept only if its trades are of value, and then ruled on at day 120
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +2.23%, equal weight basket of 10 pairs +4.66%, basket max drawdown -7%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 1.2 of 60, 58.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -4.42% (max drawdown -4.82%, 13 fills) vs challenger3 -1.02% (max drawdown -1.27%, 9 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -3.15% (usual 0.55, this window 0.99) vs challenger3 -0.96% (usual 0.03, this window 0.10); the rule compares on skill
  trades: it has finished no trade of its own: none of its 9 fills closed a position it had bought or had chosen to keep, so the -1.02% it shows is not from an exit it chose. A test that has finished no trade of its own by its look is killed
  confidence: 10%, the starting figure for any idea (no reading of the daily skill t yet: fewer than 10 days, no market data for the window, or a daily skill that does not vary)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC -1.81%, equal weight basket of 10 pairs -2.31%, basket max drawdown -3%, basket realised vol 45% annualised
- challenger4: testing H4 since 2026-09-25 22:21Z, day 11.2 of 60, 48.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.13% (max drawdown -15.08%, 136 fills) vs challenger4 -3.24% (max drawdown -5.08%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.42% (usual 0.55, this window 0.73) vs challenger4 -2.62% (usual 0.48, this window 1.00); the rule compares on skill, daily edge t +2.52 over 11 days
  trades: it has finished no trade of its own: none of its 10 fills closed a position it had bought or had chosen to keep, so the -3.24% it shows is not from an exit it chose. A test that has finished no trade of its own by its look is killed
  confidence: 8% that this is a real edge (every idea starts at 10%; the daily skill t is -0.74 over 11 days)
  fills: 10 in 11.2 days, all of them in the hour it began; at this pace about 10 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  market over the window: BTC +0.58%, equal weight basket of 10 pairs -1.30%, basket max drawdown -5%, basket realised vol 52% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 10,620.24 (started 10,000 at 2026-09-16 03:55Z), net +6.20% since start
- 24h -3.68%, 7d -7.49%, 30d +6.20%, max drawdown -15.08%
- fills 202 total, 102 in the last 7d
- costs 456.70 (fees 302.41 + slippage 154.29); gross pnl 1,076.94; cost coverage 2.36
- cash -0.00; positions: AVAX 239.394, BTC 0.0317004, SOL 22.5836, XRP 1815.68
- last run 2026-10-07 02:24Z; halted today: False

last decisions (newest last):

- 2026-10-07 01:25Z SOL hold target 0.12 (held 0.13) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.35% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-07 01:25Z ADA hold target 0.12 (held 0.12) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +9.76% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-07 01:25Z AVAX hold target 0.12 (held 0.13) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +4.74% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-10-07 01:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.84% not above entry band +1.0%
- 2026-10-07 01:25Z XRP hold target 0.12 (held 0.12) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.66% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-07 01:25Z DOGE hold target 0.12 (held 0.10) — hold: weight change +0.025 below threshold 0.05 | stay long: 72h return +1.04% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-07 01:25Z DOT hold target 0.12 (held 0.12) — hold: weight change +0.003 below threshold 0.05 | stay long: 72h return +1.53% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-10-07 01:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.33% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 02:24Z BTC buy target 0.25 (held 0.13) — stay long: 72h return -0.50% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 33% -> weight 0.25
- 2026-10-07 02:24Z ETH sell target 0.00 (held 0.13) — exit: 72h return -1.40% fell below exit band -1.0%
- 2026-10-07 02:24Z SOL buy target 0.25 (held 0.13) — stay long: 72h return -0.96% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 47% -> weight 0.25
- 2026-10-07 02:24Z ADA sell target 0.00 (held 0.12) — exit: price more than 2.0% below 24h EMA
- 2026-10-07 02:24Z AVAX buy target 0.25 (held 0.13) — stay long: 72h return +2.42% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 68% -> weight 0.25
- 2026-10-07 02:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.74% not above entry band +1.0% and price below 24h EMA
- 2026-10-07 02:24Z XRP buy target 0.25 (held 0.13) — stay long: 72h return -0.80% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 44% -> weight 0.25
- 2026-10-07 02:24Z DOGE sell target 0.00 (held 0.10) — exit: 72h return -1.12% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-10-07 02:24Z DOT sell target 0.00 (held 0.12) — exit: 72h return -1.66% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-10-07 02:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.33% not above entry band +1.0% and price below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 21 fills (9 buy / 12 sell), traded 30,528, gross pnl +54.04, +35 bps per round trip, avg half spread 2.2 bps
- AVAX: 27 fills (12 buy / 15 sell), traded 46,375, gross pnl +551.08, +238 bps per round trip, avg half spread 1.3 bps, open 239.394
- BTC: 14 fills (7 buy / 7 sell), traded 16,777, gross pnl +99.27, +118 bps per round trip, avg half spread 0.2 bps, open 0.0317004
- DOGE: 20 fills (10 buy / 10 sell), traded 27,173, gross pnl -175.84, -129 bps per round trip, avg half spread 1.1 bps
- DOT: 23 fills (11 buy / 12 sell), traded 28,978, gross pnl +68.78, +47 bps per round trip, avg half spread 2.6 bps
- ETH: 16 fills (6 buy / 10 sell), traded 25,082, gross pnl -30.95, -25 bps per round trip, avg half spread 0.1 bps
- LINK: 22 fills (10 buy / 12 sell), traded 38,421, gross pnl -164.55, -86 bps per round trip, avg half spread 2.3 bps
- LTC: 22 fills (9 buy / 13 sell), traded 33,431, gross pnl +545.56, +326 bps per round trip, avg half spread 1.8 bps
- SOL: 20 fills (11 buy / 9 sell), traded 31,842, gross pnl +3.19, +2 bps per round trip, avg half spread 0.5 bps, open 22.5836
- XRP: 17 fills (9 buy / 8 sell), traded 23,807, gross pnl +126.36, +106 bps per round trip, avg half spread 0.5 bps, open 1815.68

last fills:

- 2026-10-07 02:24Z sell ETH 1,331 @ 2609.08 fee 1.33 slip 0.67 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell ADA 1,305 @ 0.2537 fee 1.31 slip 0.65 (half spread 3.0 bps)
- 2026-10-07 02:24Z sell DOGE 1,054 @ 0.0900946 fee 1.05 slip 0.53 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell DOT 1,265 @ 1.12864 fee 1.27 slip 0.63 (half spread 2.7 bps)
- 2026-10-07 02:24Z buy BTC 1,306 @ 83896.1 fee 1.31 slip 0.65 (half spread 0.0 bps)
- 2026-10-07 02:24Z buy SOL 1,309 @ 117.764 fee 1.31 slip 0.65 (half spread 0.4 bps)
- 2026-10-07 02:24Z buy AVAX 1,259 @ 11.1096 fee 1.26 slip 0.63 (half spread 1.8 bps)
- 2026-10-07 02:24Z buy XRP 1,310 @ 1.4578 fee 1.31 slip 0.65 (half spread 0.2 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 10,397.39 (started 10,000 at 2026-09-16 03:55Z), net +3.97% since start
- 24h +0.00%, 7d +1.05%, 30d +3.97%, max drawdown -1.00%
- fills 10 total, 2 in the last 7d
- costs 38.32 (fees 25.55 + slippage 12.77); gross pnl 435.71; cost coverage 11.37
- cash 10,397.39; positions: none
- last run 2026-10-07 02:24Z; halted today: False

last decisions (newest last):

- 2026-10-07 01:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.42 not below -2.0
- 2026-10-07 01:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.47 not below -2.0
- 2026-10-07 01:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.09 not below -2.0
- 2026-10-07 01:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.61 not below -2.0
- 2026-10-07 01:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-10-07 01:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.53 not below -2.0
- 2026-10-07 01:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.17 not below -2.0
- 2026-10-07 01:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.22 not below -2.0
- 2026-10-07 02:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.28 not below -2.0
- 2026-10-07 02:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.81 not below -2.0
- 2026-10-07 02:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.64 not below -2.0
- 2026-10-07 02:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-10-07 02:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.13 not below -2.0
- 2026-10-07 02:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.43 not below -2.0
- 2026-10-07 02:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.60 not below -2.0
- 2026-10-07 02:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.97 not below -2.0
- 2026-10-07 02:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.68 not below -2.0
- 2026-10-07 02:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.73 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 2 fills (1 buy / 1 sell), traded 5,128, gross pnl +130.41, +509 bps per round trip, avg half spread 2.2 bps
- BTC: 2 fills (1 buy / 1 sell), traded 5,027, gross pnl +50.93, +203 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 5,258, gross pnl +115.51, +439 bps per round trip, avg half spread 0.3 bps
- ETH: 2 fills (1 buy / 1 sell), traded 5,048, gross pnl +50.93, +202 bps per round trip, avg half spread 0.4 bps
- SOL: 2 fills (1 buy / 1 sell), traded 5,085, gross pnl +87.92, +346 bps per round trip, avg half spread 0.5 bps

last fills:

- 2026-09-16 05:21Z buy ADA 2,500 @ 0.195871 fee 2.50 slip 1.25
- 2026-09-16 09:22Z buy BTC 2,489 @ 75814.6 fee 2.49 slip 1.24
- 2026-09-17 09:23Z sell SOL 2,585 @ 100.565 fee 2.59 slip 1.29 (half spread 0.5 bps)
- 2026-09-17 13:23Z sell ETH 2,548 @ 2449.98 fee 2.55 slip 1.27 (half spread 0.4 bps)
- 2026-09-18 01:20Z sell ADA 2,628 @ 0.205888 fee 2.63 slip 1.31 (half spread 2.2 bps)
- 2026-09-18 03:21Z sell BTC 2,538 @ 77289.3 fee 2.54 slip 1.27 (half spread 0.0 bps)
- 2026-10-02 19:24Z buy DOGE 2,572 @ 0.0912463 fee 2.57 slip 1.29 (half spread 0.3 bps)
- 2026-10-04 18:21Z sell DOGE 2,685 @ 0.0952504 fee 2.69 slip 1.34 (half spread 0.3 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 10,776.16 (started 10,000 at 2026-09-16 23:20Z), net +7.76% since start
- 24h -1.39%, 7d -1.08%, 30d +7.76%, max drawdown -3.54%
- fills 36 total, 3 in the last 7d
- costs 95.13 (fees 62.99 + slippage 32.15); gross pnl 871.29; cost coverage 9.16
- cash 10,776.16; positions: none
- last run 2026-10-07 02:24Z; halted today: False

last decisions (newest last):

- 2026-10-07 01:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 120.6 not above 120h high 123.5
- 2026-10-07 01:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 01:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 01:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 14.01 not above 120h high 14.64
- 2026-10-07 01:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.498 not above 120h high 1.542
- 2026-10-07 01:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 01:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 01:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 02:24Z BTC sell target 0.00 (held 0.25) — exit: closed 8.437e+04 below 72h low 8.48e+04
- 2026-10-07 02:24Z ETH sell target 0.00 (held 0.24) — exit: closed 2657 below 72h low 2690
- 2026-10-07 02:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 119 not above 120h high 123.5
- 2026-10-07 02:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 02:24Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 02:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 13.69 not above 120h high 14.64
- 2026-10-07 02:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.476 not above 120h high 1.542
- 2026-10-07 02:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 02:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-10-07 02:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,891, gross pnl +44.81, +183 bps per round trip, avg half spread 2.0 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 5 fills (3 buy / 2 sell), traded 10,806, gross pnl -58.08, -108 bps per round trip, avg half spread 0.0 bps
- DOGE: 3 fills (2 buy / 1 sell), traded 2,949, gross pnl +28.53, +193 bps per round trip, avg half spread 1.1 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 2 fills (1 buy / 1 sell), traded 2,991, gross pnl +45.99, +308 bps per round trip, avg half spread 2.7 bps
- LTC: 4 fills (2 buy / 2 sell), traded 7,427, gross pnl +81.42, +219 bps per round trip, avg half spread 2.9 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 2 fills (1 buy / 1 sell), traded 1,189, gross pnl -19.18, -323 bps per round trip, avg half spread 0.3 bps

last fills:

- 2026-09-20 13:21Z sell BTC 2,683 @ 80427.1 fee 2.68 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell ETH 2,675 @ 2576.65 fee 2.67 slip 1.34 (half spread 0.0 bps)
- 2026-09-20 13:21Z sell AVAX 2,940 @ 10.5167 fee 2.94 slip 1.47 (half spread 2.9 bps)
- 2026-09-20 13:21Z sell LTC 2,669 @ 56.8865 fee 2.67 slip 1.34 (half spread 2.6 bps)
- 2026-09-29 12:30Z buy ETH 2,741 @ 2739.14 fee 2.74 slip 1.37 (half spread 0.1 bps)
- 2026-09-30 13:27Z buy BTC 2,737 @ 85327.3 fee 2.74 slip 1.37 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell BTC 2,689 @ 83812.2 fee 2.69 slip 1.34 (half spread 0.0 bps)
- 2026-10-07 02:24Z sell ETH 2,611 @ 2609.08 fee 2.61 slip 1.31 (half spread 0.0 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,907.96 (started 10,000 at 2026-10-05 05:28Z), net -0.92% since start
- 24h -1.02%, 7d -0.88%, 30d -0.88%, max drawdown -1.64%
- fills 25 total, 25 in the last 7d
- costs 55.56 (fees 37.00 + slippage 18.56); gross pnl -36.48; cost coverage -0.66
- cash 7,505.37; positions: AVAX 216.372
- last run 2026-10-07 02:24Z; halted today: False

last decisions (newest last):

- 2026-10-07 01:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 120.6 not a fresh close above reaction high 124.4
- 2026-10-07 01:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2673 not a fresh close above reaction high 0.2616
- 2026-10-07 01:25Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: price 11.61 still above the 48h low 10.85; realised vol 66% -> weight 0.25
- 2026-10-07 01:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 14.01 not a fresh close above reaction high 15.46
- 2026-10-07 01:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.498 not a fresh close above reaction high 1.638
- 2026-10-07 01:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09385 not a fresh close above reaction high 0.1039
- 2026-10-07 01:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.201 not a fresh close above reaction high 1.301
- 2026-10-07 01:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 69.05 not a fresh close above reaction high 74.29
- 2026-10-07 02:24Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.263e+04 not a higher low vs prior low 7.626e+04 (need +10.0%)
- 2026-10-07 02:24Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2640 not a higher low vs prior low 2426 (need +10.0%)
- 2026-10-07 02:24Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 119 not a fresh close above reaction high 124.4
- 2026-10-07 02:24Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.2602 not a fresh close above reaction high 0.2616
- 2026-10-07 02:24Z AVAX hold target 0.25 (held 0.24) — hold: weight change +0.008 below threshold 0.05 | stay long: price 11.34 still above the 48h low 10.85; realised vol 68% -> weight 0.25
- 2026-10-07 02:24Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 13.69 not a fresh close above reaction high 15.46
- 2026-10-07 02:24Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.476 not a fresh close above reaction high 1.638
- 2026-10-07 02:24Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 0.09174 not a fresh close above reaction high 0.1039
- 2026-10-07 02:24Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 1.158 not a fresh close above reaction high 1.301
- 2026-10-07 02:24Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: higher low confirmed but 68.28 not a fresh close above reaction high 74.29

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 3 fills (2 buy / 1 sell), traded 5,009, gross pnl -90.75, -362 bps per round trip, avg half spread 0.6 bps, open 216.372
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell ETH 1,250 @ 2715.8 fee 1.25 slip 0.63 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)
- 2026-10-06 15:25Z buy AVAX 2,503 @ 11.5663 fee 2.50 slip 1.25 (half spread 0.4 bps)

## challenger4: ts_momentum (H4)

params: {"ema_exit_buffer": 0.05, "ema_hours": 168, "entry_return": 0.05, "exit_return": -0.05, "lookback_hours": 720, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,921.57 (started 10,000 at 2026-09-25 04:23Z), net -0.78% since start
- 24h -3.37%, 7d -1.78%, 30d -0.71%, max drawdown -5.08%
- fills 23 total, 0 in the last 7d
- costs 41.57 (fees 27.64 + slippage 13.93); gross pnl -36.86; cost coverage -0.89
- cash 0.00; positions: ADA 4065.92, AVAX 85.9891, BTC 0.0123859, DOGE 10457.3, DOT 866.566, ETH 0.386879, LINK 75.3191, LTC 14.3894, SOL 8.53396, XRP 665.342
- last run 2026-10-07 02:24Z; halted today: False

last decisions (newest last):

- 2026-10-07 01:25Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.000 below threshold 0.05 | stay long: 720h return +13.63% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 01:25Z ADA hold target 0.10 (held 0.11) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +19.46% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 01:25Z AVAX hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +46.99% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 01:25Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +6.60% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 01:25Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +5.61% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 01:25Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +3.19% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 01:25Z DOT hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +17.36% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 01:25Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.003 below threshold 0.05 | stay long: 720h return +24.48% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 02:24Z BTC hold target 0.10 (held 0.10) — hold: weight change -0.005 below threshold 0.05 | stay long: 720h return +5.57% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 02:24Z ETH hold target 0.10 (held 0.10) — hold: weight change -0.002 below threshold 0.05 | stay long: 720h return +6.11% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 02:24Z SOL hold target 0.10 (held 0.10) — hold: weight change -0.001 below threshold 0.05 | stay long: 720h return +12.96% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 02:24Z ADA hold target 0.10 (held 0.10) — hold: weight change -0.004 below threshold 0.05 | stay long: 720h return +17.47% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 02:24Z AVAX hold target 0.10 (held 0.10) — hold: weight change +0.004 below threshold 0.05 | stay long: 720h return +44.90% vs exit band -5.0% and price above 168h EMA; realised vo...
- 2026-10-07 02:24Z LINK hold target 0.10 (held 0.10) — hold: weight change -0.003 below threshold 0.05 | stay long: 720h return +5.22% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 02:24Z XRP hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +4.93% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 02:24Z DOGE hold target 0.10 (held 0.10) — hold: weight change +0.005 below threshold 0.05 | stay long: 720h return +1.78% vs exit band -5.0% and price within 5.0% of 168h EMA; rea...
- 2026-10-07 02:24Z DOT hold target 0.10 (held 0.10) — hold: weight change +0.001 below threshold 0.05 | stay long: 720h return +17.28% vs exit band -5.0% and price within 5.0% of 168h EMA; re...
- 2026-10-07 02:24Z LTC hold target 0.10 (held 0.10) — hold: weight change +0.002 below threshold 0.05 | stay long: 720h return +25.56% vs exit band -5.0% and price within 5.0% of 168h EMA; re...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 3 fills (1 buy / 2 sell), traded 4,012, gross pnl +67.36, +336 bps per round trip, avg half spread 1.6 bps, open 4065.92
- AVAX: 1 fill (1 buy / 0 sell), traded 907, gross pnl +48.02, +1059 bps per round trip, avg half spread 0.5 bps, open 85.9891
- BTC: 1 fill (1 buy / 0 sell), traded 1,040, gross pnl -0.87, -17 bps per round trip, avg half spread 0.0 bps, open 0.0123859
- DOGE: 1 fill (1 buy / 0 sell), traded 1,031, gross pnl -87.73, -1702 bps per round trip, avg half spread 0.1 bps, open 10457.3
- DOT: 3 fills (2 buy / 1 sell), traded 3,055, gross pnl -46.09, -302 bps per round trip, avg half spread 2.5 bps, open 866.566
- ETH: 1 fill (1 buy / 0 sell), traded 1,040, gross pnl -29.57, -569 bps per round trip, avg half spread 0.0 bps, open 0.386879
- LINK: 3 fills (1 buy / 2 sell), traded 4,055, gross pnl +75.06, +370 bps per round trip, avg half spread 2.2 bps, open 75.3191
- LTC: 3 fills (1 buy / 2 sell), traded 3,985, gross pnl -39.98, -201 bps per round trip, avg half spread 1.9 bps, open 14.3894
- SOL: 3 fills (2 buy / 1 sell), traded 2,409, gross pnl -17.47, -145 bps per round trip, avg half spread 0.4 bps, open 8.53396
- XRP: 4 fills (2 buy / 2 sell), traded 6,103, gross pnl -5.59, -18 bps per round trip, avg half spread 0.7 bps, open 665.342

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

- BTC: live 1223 candles, 2026-08-17 03:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1223 candles, 2026-08-17 03:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1223 candles, 2026-08-17 03:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- ADA: live 1223 candles, 2026-08-17 03:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.9 bps
- AVAX: live 1223 candles, 2026-08-17 03:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.0 bps
- LINK: live 1223 candles, 2026-08-17 03:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.6 bps
- XRP: live 1195 candles, 2026-08-18 07:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.5 bps
- DOGE: live 1195 candles, 2026-08-18 07:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1195 candles, 2026-08-18 07:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- LTC: live 1195 candles, 2026-08-18 07:00Z to 2026-10-07 01:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
