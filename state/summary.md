# quantloop summary — generated 2026-11-04 06:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-28 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 8 pair days (the cap is 4 fills in one pair in one UTC day)
- champion, AVAX, 2026-11-02: 4 fills (buy 00:10, sell 02:10, buy 07:10, sell 18:10); no buy stopped
- champion, DOT, 2026-11-02: 4 fills (buy 00:10, sell 02:10, buy 07:10, sell 13:10); no buy stopped
- champion, BTC, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 16:10, sell 21:10); no buy stopped
- champion, DOGE, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 11:10, sell 21:10); no buy stopped
- champion, ETH, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 16:10, sell 21:10); no buy stopped
- champion, LINK, 2026-10-29: 5 fills (buy 02:10, sell 03:10, buy 11:10, buy 16:10, sell 21:10); no buy stopped
- champion, LTC, 2026-10-29: 4 fills (buy 02:10, buy 04:10, sell 11:10, sell 21:10); no buy stopped
- champion, XRP, 2026-10-29: 4 fills (buy 02:10, sell 04:10, buy 16:10, sell 21:10); no buy stopped
- times are UTC, and a pair day is one pair on one UTC day in one account. At the cap no more buys go through in that pair until the next UTC day; sells always do. A buy the strategy still wants an hour later is stopped, and counted, again. A slot is read from the hour its test began, and a slot with no test is left out: it holds cash (before ruleset 8 it ran the champion's config). The champion's lines from before a promotion, a revert or a retirement are the config it had then
- how to read a line: that many fills in one coin in one day is in and out more than once, or one position built or cut in steps. A stopped buy is one of three things. A top up of a position it held is the strategy resizing what it keeps, often in several pairs at once when one pair enters or leaves the book. An entry from flat is a whipsaw when, after each exit, the strategy's own decisions said flat because its entry condition failed, until a later entry fired on a new reading. It is a loop when the strategy buys back within an hour or two of selling, the entry naming the same signal as the one before, often lower than it just sold. The first two are costs the idea carries, not bugs. A new strategy's first buy, stopped by the old config's fills that day, is none of the three and needs nothing doing. The account's decisions.csv and trades.csv show which. Every one of those fills paid costs

## Challenger slots

- challenger1: testing H1 since 2026-09-16 05:21Z, day 49.0 of 60, 11.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -16.50% (max drawdown -34.03%, 409 fills) vs challenger1 -8.23% (max drawdown -15.05%, 126 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -16.71% (usual 0.54, this window 0.51) vs challenger1 -8.38% (usual 0.37, this window 0.50); the rule compares on skill, daily edge t +0.57 over 49 days
  trades: its 38 finished trades made -2.61% of its starting equity after costs (24 won, 14 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 5% that this is a real edge (every idea starts at 10%; the daily skill t is -1.15 over 49 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +2.36%, equal weight basket of 10 pairs +0.39%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 43.9 of 60, 16.1 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -27.33% (max drawdown -34.03%, 371 fills) vs challenger2 -11.67% (max drawdown -12.10%, 26 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -19.20% (usual 0.54, this window 0.49) vs challenger2 -7.36% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +1.65 over 44 days
  trades: its 11 finished trades made -11.67% of its starting equity after costs (0 won, 11 lost, 4 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 4% that this is a real edge (every idea starts at 10%; the daily skill t is -1.41 over 44 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -5.94%, equal weight basket of 10 pairs -15.06%, basket max drawdown -24%, basket realised vol 55% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 29.3 of 60, 30.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -24.85% (max drawdown -26.06%, 220 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -13.54% (usual 0.55, this window 0.37) vs challenger3 -0.69% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.76 over 29 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.62 over 29 days)
  fills: 10 in 29.3 days, 8 of them in the hour it began; at this pace about 16 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -9.66%, equal weight basket of 10 pairs -20.60%, basket max drawdown -23%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 19.3 of 120, 100.7 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -4.45% (max drawdown -12.71%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +1.43% (usual 0.53, this window 0.92); the rule compares on skill, daily edge t +0.30 over 19 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -14.83% so far
  trades: its 9 finished trades made -6.54% of its starting equity after costs (2 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 10% that this is a real edge (every idea starts at 10%; the daily skill t is +0.30 over 19 days)
  market over the window: BTC -5.70%, equal weight basket of 10 pairs -11.14%, basket max drawdown -15%, basket realised vol 50% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,350.12 (started 10,000 at 2026-09-16 03:55Z), net -16.50% since start
- 24h -0.25%, 7d -9.34%, 30d -24.81%, max drawdown -34.03%
- fills 409 total, 77 in the last 7d
- costs 903.57 (fees 598.75 + slippage 304.82); gross pnl -746.31; cost coverage -0.83
- cash 4,110.13; positions: ETH 0.936612, XRP 1645.81
- last run 2026-11-04 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.26% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.56% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.09% not above entry band +1.0%
- 2026-11-04 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.51% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 05:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.67% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-04 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.89% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.49% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -4.52% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.18% not above entry band +1.0%
- 2026-11-04 06:10Z ETH hold target 0.25 (held 0.26) — hold: weight change -0.007 below threshold 0.05 | stay long: 72h return +1.05% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-11-04 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.12% not above entry band +1.0%
- 2026-11-04 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.69% not above entry band +1.0%
- 2026-11-04 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.92% not above entry band +1.0%
- 2026-11-04 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -5.55% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 06:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.71% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-04 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.51% not above entry band +1.0%
- 2026-11-04 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.93% not above entry band +1.0%
- 2026-11-04 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.79% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 34 fills (15 buy / 19 sell), traded 44,125, gross pnl -108.35, -49 bps per round trip, avg half spread 2.1 bps
- AVAX: 49 fills (23 buy / 26 sell), traded 82,399, gross pnl +173.06, +42 bps per round trip, avg half spread 1.3 bps
- BTC: 39 fills (22 buy / 17 sell), traded 55,179, gross pnl -84.06, -30 bps per round trip, avg half spread 0.1 bps
- DOGE: 36 fills (18 buy / 18 sell), traded 46,245, gross pnl -249.77, -108 bps per round trip, avg half spread 0.8 bps
- DOT: 43 fills (21 buy / 22 sell), traded 64,930, gross pnl -172.50, -53 bps per round trip, avg half spread 2.2 bps
- ETH: 41 fills (21 buy / 20 sell), traded 55,950, gross pnl -218.11, -78 bps per round trip, avg half spread 0.1 bps, open 0.936612
- LINK: 47 fills (24 buy / 23 sell), traded 79,344, gross pnl -403.27, -102 bps per round trip, avg half spread 2.0 bps
- LTC: 43 fills (20 buy / 23 sell), traded 58,693, gross pnl +429.16, +146 bps per round trip, avg half spread 1.6 bps
- SOL: 38 fills (20 buy / 18 sell), traded 58,943, gross pnl -89.47, -30 bps per round trip, avg half spread 0.5 bps
- XRP: 39 fills (20 buy / 19 sell), traded 52,938, gross pnl -23.01, -9 bps per round trip, avg half spread 0.4 bps, open 1645.81

last fills:

- 2026-11-02 07:10Z buy AVAX 1,192 @ 8.56778 fee 1.19 slip 0.60 (half spread 1.8 bps)
- 2026-11-02 07:10Z buy DOT 1,169 @ 0.952726 fee 1.17 slip 0.58 (half spread 1.6 bps)
- 2026-11-02 13:10Z sell DOT 2,094 @ 0.936981 fee 2.09 slip 1.05 (half spread 0.5 bps)
- 2026-11-02 18:10Z sell AVAX 2,093 @ 8.38281 fee 2.09 slip 1.05 (half spread 2.4 bps)
- 2026-11-03 07:10Z sell BTC 2,092 @ 76355.9 fee 2.09 slip 1.05 (half spread 0.0 bps)
- 2026-11-03 13:10Z buy AVAX 2,101 @ 8.5958 fee 2.10 slip 1.05 (half spread 1.7 bps)
- 2026-11-03 13:10Z buy XRP 2,101 @ 1.27664 fee 2.10 slip 1.05 (half spread 0.0 bps)
- 2026-11-04 01:10Z sell AVAX 2,047 @ 8.37331 fee 2.05 slip 1.02 (half spread 3.0 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,166.29 (started 10,000 at 2026-09-16 03:55Z), net -8.34% since start
- 24h +1.72%, 7d -2.98%, 30d -11.84%, max drawdown -15.05%
- fills 126 total, 27 in the last 7d
- costs 238.05 (fees 157.38 + slippage 80.66); gross pnl -595.66; cost coverage -2.50
- cash -0.00; positions: ADA 7989.12, BTC 0.0196627, DOGE 20354.8, DOT 1609.07, LINK 119.245, LTC 5.0679, SOL 16.2339
- last run 2026-11-04 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 05:10Z SOL hold target 0.14 (held 0.16) — hold: weight change -0.021 below threshold 0.05 | stay long: z -1.50 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-11-04 05:10Z ADA hold target 0.14 (held 0.17) — hold: weight change -0.022 below threshold 0.05 | stay long: z -1.37 vs 240h mean (entry -2.0, exit -0.5); vol 70% -> weight 0.25
- 2026-11-04 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.81 not below -2.0
- 2026-11-04 05:10Z LINK hold target 0.14 (held 0.14) — hold: weight change -0.001 below threshold 0.05 | stay long: z -1.63 vs 240h mean (entry -2.0, exit -0.5); vol 80% -> weight 0.25
- 2026-11-04 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.20 not below -2.0
- 2026-11-04 05:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -1.37 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-11-04 05:10Z DOT hold target 0.14 (held 0.16) — hold: weight change -0.022 below threshold 0.05 | stay long: z -1.18 vs 240h mean (entry -2.0, exit -0.5); vol 88% -> weight 0.25
- 2026-11-04 05:10Z LTC none target 0.14 (held 0.03) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...
- 2026-11-04 06:10Z BTC hold target 0.14 (held 0.17) — hold: weight change -0.024 below threshold 0.05 | stay long: z -0.76 vs 240h mean (entry -2.0, exit -0.5); vol 39% -> weight 0.25
- 2026-11-04 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.05 not below -2.0
- 2026-11-04 06:10Z SOL hold target 0.14 (held 0.16) — hold: weight change -0.021 below threshold 0.05 | stay long: z -1.38 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-11-04 06:10Z ADA hold target 0.14 (held 0.17) — hold: weight change -0.022 below threshold 0.05 | stay long: z -1.03 vs 240h mean (entry -2.0, exit -0.5); vol 71% -> weight 0.25
- 2026-11-04 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.54 not below -2.0
- 2026-11-04 06:10Z LINK hold target 0.14 (held 0.14) — hold: weight change -0.000 below threshold 0.05 | stay long: z -1.41 vs 240h mean (entry -2.0, exit -0.5); vol 80% -> weight 0.25
- 2026-11-04 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.03 not below -2.0
- 2026-11-04 06:10Z DOGE hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -1.09 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-11-04 06:10Z DOT hold target 0.14 (held 0.17) — hold: weight change -0.023 below threshold 0.05 | stay long: z -0.98 vs 240h mean (entry -2.0, exit -0.5); vol 88% -> weight 0.25
- 2026-11-04 06:10Z LTC none target 0.14 (held 0.03) — waits for cash: the book is fully invested and no position is far enough above its target to trim, so this buy fills when an exit or a bi...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 11 fills (6 buy / 5 sell), traded 13,975, gross pnl -101.67, -146 bps per round trip, avg half spread 1.6 bps, open 7989.12
- AVAX: 14 fills (8 buy / 6 sell), traded 16,832, gross pnl +143.39, +170 bps per round trip, avg half spread 1.5 bps
- BTC: 9 fills (6 buy / 3 sell), traded 11,694, gross pnl +67.15, +115 bps per round trip, avg half spread 0.1 bps, open 0.0196627
- DOGE: 14 fills (8 buy / 6 sell), traded 19,366, gross pnl -156.23, -161 bps per round trip, avg half spread 0.5 bps, open 20354.8
- DOT: 9 fills (5 buy / 4 sell), traded 11,229, gross pnl -396.67, -706 bps per round trip, avg half spread 2.3 bps, open 1609.07
- ETH: 15 fills (7 buy / 8 sell), traded 21,275, gross pnl +123.89, +116 bps per round trip, avg half spread 0.3 bps
- LINK: 15 fills (9 buy / 6 sell), traded 16,491, gross pnl +109.81, +133 bps per round trip, avg half spread 1.5 bps, open 119.245
- LTC: 13 fills (7 buy / 6 sell), traded 14,995, gross pnl +16.33, +22 bps per round trip, avg half spread 1.2 bps, open 5.0679
- SOL: 14 fills (9 buy / 5 sell), traded 18,512, gross pnl -179.08, -193 bps per round trip, avg half spread 0.5 bps, open 16.2339
- XRP: 12 fills (6 buy / 6 sell), traded 13,015, gross pnl -222.60, -342 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-11-02 03:10Z buy SOL 543 @ 95.0225 fee 0.54 slip 0.27 (half spread 0.5 bps)
- 2026-11-02 03:10Z buy ADA 523 @ 0.193087 fee 0.52 slip 0.26 (half spread 2.0 bps)
- 2026-11-02 03:10Z buy XRP 520 @ 1.25517 fee 0.52 slip 0.26 (half spread 0.4 bps)
- 2026-11-02 03:10Z buy DOGE 538 @ 0.0757849 fee 0.54 slip 0.27 (half spread 0.0 bps)
- 2026-11-02 03:10Z buy DOT 491 @ 0.955778 fee 0.49 slip 0.25 (half spread 2.1 bps)
- 2026-11-03 13:10Z sell XRP 1,567 @ 1.27537 fee 1.57 slip 0.78 (half spread 0.0 bps)
- 2026-11-04 02:10Z buy LINK 1,295 @ 10.8566 fee 1.29 slip 0.65 (half spread 1.3 bps)
- 2026-11-04 02:10Z buy LTC 270 @ 53.2166 fee 0.27 slip 0.13 (half spread 1.9 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 9,686.16 (started 10,000 at 2026-09-16 23:20Z), net -3.14% since start
- 24h +0.00%, 7d -5.91%, 30d -11.52%, max drawdown -12.80%
- fills 58 total, 13 in the last 7d
- costs 166.60 (fees 110.15 + slippage 56.45); gross pnl -147.24; cost coverage -0.88
- cash 9,686.16; positions: none
- last run 2026-11-04 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.188 not above 120h high 0.1961
- 2026-11-04 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.27 not above 120h high 1.284
- 2026-11-04 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07413 not above 120h high 0.07631
- 2026-11-04 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9329 not above 120h high 0.9753
- 2026-11-04 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.1902 not above 120h high 0.1961
- 2026-11-04 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 1.275 not above 120h high 1.284
- 2026-11-04 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.0746 not above 120h high 0.07631
- 2026-11-04 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9395 not above 120h high 0.9753
- 2026-11-04 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 10 fills (5 buy / 5 sell), traded 21,231, gross pnl -174.17, -164 bps per round trip, avg half spread 0.0 bps
- DOGE: 9 fills (5 buy / 4 sell), traded 14,280, gross pnl -214.67, -301 bps per round trip, avg half spread 1.0 bps
- DOT: 3 fills (1 buy / 2 sell), traded 5,213, gross pnl +204.79, +786 bps per round trip, avg half spread 3.4 bps
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 5 fills (3 buy / 2 sell), traded 7,935, gross pnl -94.34, -238 bps per round trip, avg half spread 2.9 bps
- LTC: 6 fills (3 buy / 3 sell), traded 12,367, gross pnl -84.66, -137 bps per round trip, avg half spread 2.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 6 fills (3 buy / 3 sell), traded 11,524, gross pnl -217.79, -378 bps per round trip, avg half spread 0.1 bps

last fills:

- 2026-10-29 16:10Z buy LINK 1,086 @ 11.9832 fee 1.09 slip 0.54 (half spread 2.1 bps)
- 2026-10-29 19:10Z sell XRP 2,485 @ 1.28014 fee 2.48 slip 1.24 (half spread 0.0 bps)
- 2026-10-29 19:10Z buy LINK 1,458 @ 11.6425 fee 1.46 slip 0.73 (half spread 2.2 bps)
- 2026-10-29 19:10Z buy DOGE 509 @ 0.0791227 fee 0.51 slip 0.25 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell BTC 1,984 @ 78979.6 fee 1.98 slip 0.99 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell LINK 2,401 @ 11.1222 fee 2.40 slip 1.58 (half spread 4.6 bps)
- 2026-10-29 21:10Z sell DOGE 2,412 @ 0.0759279 fee 2.41 slip 1.40 (half spread 3.8 bps)
- 2026-10-29 21:10Z sell LTC 2,386 @ 55.3789 fee 2.39 slip 1.34 (half spread 3.6 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.57%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-04 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-04 05:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2034 (need +10.0%)
- 2026-11-04 05:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.79 (need +10.0%)
- 2026-11-04 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.38 (need +10.0%)
- 2026-11-04 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-04 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-04 05:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.029 (need +10.0%)
- 2026-11-04 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)
- 2026-11-04 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.604e+04 not a higher low vs prior low 7.97e+04 (need +10.0%)
- 2026-11-04 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2303 (need +10.0%)
- 2026-11-04 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-04 06:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2034 (need +10.0%)
- 2026-11-04 06:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.79 (need +10.0%)
- 2026-11-04 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.38 (need +10.0%)
- 2026-11-04 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-04 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-04 06:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.029 (need +10.0%)
- 2026-11-04 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (1 buy / 3 sell), traded 5,039, gross pnl +41.46, +165 bps per round trip, avg half spread 2.1 bps
- AVAX: 4 fills (2 buy / 2 sell), traded 7,389, gross pnl -111.53, -302 bps per round trip, avg half spread 0.7 bps
- BTC: 2 fills (1 buy / 1 sell), traded 2,500, gross pnl +1.73, +14 bps per round trip, avg half spread 0.0 bps
- DOGE: 2 fills (1 buy / 1 sell), traded 2,020, gross pnl +5.22, +52 bps per round trip, avg half spread 0.0 bps
- DOT: 4 fills (1 buy / 3 sell), traded 4,992, gross pnl +26.47, +106 bps per round trip, avg half spread 1.2 bps
- ETH: 3 fills (1 buy / 2 sell), traded 4,971, gross pnl +5.15, +21 bps per round trip, avg half spread 0.1 bps
- LTC: 5 fills (2 buy / 3 sell), traded 9,964, gross pnl -33.72, -68 bps per round trip, avg half spread 1.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,506, gross pnl +7.97, +64 bps per round trip, avg half spread 0.4 bps

last fills:

- 2026-10-05 22:23Z sell SOL 1,256 @ 121.414 fee 1.26 slip 0.63 (half spread 0.4 bps)
- 2026-10-05 22:23Z sell ADA 1,270 @ 0.273597 fee 1.27 slip 0.69 (half spread 3.5 bps)
- 2026-10-05 22:23Z sell AVAX 1,256 @ 11.0445 fee 1.26 slip 0.63 (half spread 0.9 bps)
- 2026-10-05 22:23Z sell DOGE 1,012 @ 0.0959034 fee 1.01 slip 0.51 (half spread 0.0 bps)
- 2026-10-05 22:23Z sell DOT 1,244 @ 1.22973 fee 1.24 slip 0.62 (half spread 2.0 bps)
- 2026-10-05 22:23Z sell LTC 1,249 @ 70.2449 fee 1.25 slip 0.62 (half spread 1.4 bps)
- 2026-10-06 15:25Z buy AVAX 2,503 @ 11.5663 fee 2.50 slip 1.25 (half spread 0.4 bps)
- 2026-10-07 22:22Z sell AVAX 2,381 @ 11.0025 fee 2.38 slip 1.19 (half spread 0.9 bps)

## challenger4: relative_reversion (H6)

params: {"entry_z": 2.0, "exit_z": 0.25, "max_weight": 0.25, "ratio_hours": 720, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,550.95 (started 10,000 at 2026-10-13 17:26Z), net -4.49% since start
- 24h +1.50%, 7d -1.06%, 30d -4.49%, max drawdown -12.71%
- fills 30 total, 12 in the last 7d
- costs 62.94 (fees 40.22 + slippage 22.72); gross pnl -386.11; cost coverage -6.13
- cash 2,517.83; positions: ADA 12106.8, AVAX 276.724, DOT 2516.14
- last run 2026-11-04 06:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 05:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.79 not below -2.0
- 2026-11-04 05:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.010 below threshold 0.05 | stay long: ratio to BTC z -1.40 vs 720h mean (entry -2.0, exit -0.25); vol 70% -> weigh...
- 2026-11-04 05:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.05 vs 720h mean (entry -2.0, exit -0.25); vol 75% -> weigh...
- 2026-11-04 05:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.32 not below -2.0
- 2026-11-04 05:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.12 not below -2.0
- 2026-11-04 05:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.95 not below -2.0
- 2026-11-04 05:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: ratio to BTC z -1.53 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-04 05:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.44 not below -2.0
- 2026-11-04 06:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-04 06:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.26 not below -2.0
- 2026-11-04 06:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.80 not below -2.0
- 2026-11-04 06:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.010 below threshold 0.05 | stay long: ratio to BTC z -1.31 vs 720h mean (entry -2.0, exit -0.25); vol 71% -> weigh...
- 2026-11-04 06:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.01 vs 720h mean (entry -2.0, exit -0.25); vol 76% -> weigh...
- 2026-11-04 06:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.31 not below -2.0
- 2026-11-04 06:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.10 not below -2.0
- 2026-11-04 06:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.90 not below -2.0
- 2026-11-04 06:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.49 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-04 06:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.28 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (3 buy / 1 sell), traded 5,091, gross pnl -150.07, -590 bps per round trip, avg half spread 3.3 bps, open 12106.8
- AVAX: 4 fills (3 buy / 1 sell), traded 5,003, gross pnl -29.31, -117 bps per round trip, avg half spread 3.5 bps, open 276.724
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 5 fills (3 buy / 2 sell), traded 5,904, gross pnl +50.59, +171 bps per round trip, avg half spread 3.9 bps, open 2516.14
- ETH: 4 fills (1 buy / 3 sell), traded 4,854, gross pnl -141.72, -584 bps per round trip, avg half spread 1.1 bps
- LINK: 2 fills (1 buy / 1 sell), traded 4,797, gross pnl +245.83, +1025 bps per round trip, avg half spread 2.6 bps
- SOL: 4 fills (1 buy / 3 sell), traded 4,837, gross pnl -118.93, -492 bps per round trip, avg half spread 0.5 bps
- XRP: 4 fills (1 buy / 3 sell), traded 4,888, gross pnl -91.04, -373 bps per round trip, avg half spread 1.7 bps

last fills:

- 2026-10-29 21:10Z sell XRP 1,331 @ 1.24739 fee 1.33 slip 0.93 (half spread 5.0 bps)
- 2026-10-29 21:10Z sell DOGE 1,583 @ 0.0759279 fee 1.58 slip 0.92 (half spread 3.8 bps)
- 2026-10-29 21:10Z sell DOT 954 @ 0.926415 fee 0.95 slip 1.07 (half spread 9.2 bps)
- 2026-10-30 00:10Z buy AVAX 2,277 @ 8.22864 fee 2.28 slip 1.15 (half spread 3.0 bps)
- 2026-10-30 00:10Z buy LINK 2,277 @ 10.5579 fee 2.28 slip 1.27 (half spread 3.6 bps)
- 2026-10-30 00:10Z buy DOT 2,277 @ 0.904981 fee 2.28 slip 1.34 (half spread 3.9 bps)
- 2026-10-30 01:10Z buy ADA 2,268 @ 0.187329 fee 2.27 slip 1.65 (half spread 5.3 bps)
- 2026-10-31 18:10Z sell LINK 2,520 @ 11.6859 fee 2.52 slip 1.26 (half spread 1.5 bps)

## Data

live candles (Kraken, grows hourly) and history (Coinbase backfill, for backtests):

- BTC: live 1899 candles, 2026-08-17 03:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1899 candles, 2026-08-17 03:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1899 candles, 2026-08-17 03:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 1899 candles, 2026-08-17 03:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 1899 candles, 2026-08-17 03:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- LINK: live 1899 candles, 2026-08-17 03:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 1871 candles, 2026-08-18 07:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1871 candles, 2026-08-18 07:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1871 candles, 2026-08-18 07:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LTC: live 1871 candles, 2026-08-18 07:00Z to 2026-11-04 05:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
