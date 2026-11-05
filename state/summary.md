# quantloop summary — generated 2026-11-05 13:10Z

Cost model: fee 10 bps + slippage 5 bps per side (~30 bps per round trip). Pairs: BTC, ETH, SOL, ADA, AVAX, LINK, XRP, DOGE, DOT, LTC. Paper only.

## Runs

- hours on record: 24 of the last 24, 168 of the last 168
- no hour in the last 7 days is without a decision
- this is the loop's own record. Missing candles are a different thing and are listed under Data; a clean Data section says nothing about whether the bot ran

## Fill cap

- since 2026-10-29 (today and the 7 UTC days before it): no buy stopped by the cap; a pair filled 4 times or more in one UTC day on 8 pair days (the cap is 4 fills in one pair in one UTC day)
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

- challenger1: testing H1 since 2026-09-16 05:21Z, day 50.3 of 60, 9.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -16.39% (max drawdown -34.03%, 427 fills) vs challenger1 -4.30% (max drawdown -15.05%, 136 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -17.82% (usual 0.54, this window 0.52) vs challenger1 -5.29% (usual 0.37, this window 0.50); the rule compares on skill, daily edge t +0.83 over 50 days
  trades: its 45 finished trades made -4.42% of its starting equity after costs (28 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.62 over 50 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +4.94%, equal weight basket of 10 pairs +2.65%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 45.2 of 60, 14.8 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -27.24% (max drawdown -34.03%, 389 fills) vs challenger2 -13.74% (max drawdown -14.17%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -20.16% (usual 0.54, this window 0.50) vs challenger2 -10.00% (usual 0.29, this window 0.17); the rule compares on skill, daily edge t +1.41 over 45 days
  trades: its 11 finished trades made -11.67% of its starting equity after costs (0 won, 11 lost, 4 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 4% that this is a real edge (every idea starts at 10%; the daily skill t is -1.75 over 45 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.57%, equal weight basket of 10 pairs -13.10%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 30.6 of 60, 29.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -24.76% (max drawdown -26.06%, 238 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -14.45% (usual 0.55, this window 0.39) vs challenger3 -0.74% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.96 over 31 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.68 over 31 days)
  fills: 10 in 30.6 days, 8 of them in the hour it began; at this pace about 15 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -7.38%, equal weight basket of 10 pairs -18.78%, basket max drawdown -23%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 20.6 of 120, 99.4 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -3.58% (max drawdown -12.71%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +1.22% (usual 0.53, this window 0.91); the rule compares on skill, daily edge t +0.25 over 21 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -14.83% so far
  trades: its 9 finished trades made -6.54% of its starting equity after costs (2 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 10% that this is a real edge (every idea starts at 10%; the daily skill t is +0.25 over 21 days)
  market over the window: BTC -3.32%, equal weight basket of 10 pairs -9.09%, basket max drawdown -15%, basket realised vol 51% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,360.69 (started 10,000 at 2026-09-16 03:55Z), net -16.39% since start
- 24h +0.19%, 7d -6.87%, 30d -24.74%, max drawdown -34.03%
- fills 427 total, 64 in the last 7d
- costs 929.06 (fees 615.01 + slippage 314.04); gross pnl -710.26; cost coverage -0.76
- cash -0.00; positions: ADA 4768.78, AVAX 106.147, BTC 0.0118015, DOGE 12234.7, ETH 0.389481, LINK 80.0549, LTC 16.713, SOL 9.79557, XRP 720.804
- last run 2026-11-05 13:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 12:10Z SOL hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.65% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-05 12:10Z ADA hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +3.80% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-05 12:10Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +2.22% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-05 12:10Z LINK hold target 0.11 (held 0.11) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +2.31% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-05 12:10Z XRP hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +5.48% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-05 12:10Z DOGE hold target 0.11 (held 0.11) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +2.01% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-05 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: price below 24h EMA
- 2026-11-05 12:10Z LTC hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +1.66% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-05 13:10Z BTC hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +2.44% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z ETH hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +4.77% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z SOL hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +1.35% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z ADA hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.56% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.91% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z LINK hold target 0.11 (held 0.11) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +1.14% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z XRP hold target 0.11 (held 0.11) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +4.39% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z DOGE hold target 0.11 (held 0.11) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.94% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 13:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.33% not above entry band +1.0% and price below 24h EMA
- 2026-11-05 13:10Z LTC hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.57% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 35 fills (16 buy / 19 sell), traded 45,076, gross pnl -126.58, -56 bps per round trip, avg half spread 2.1 bps, open 4768.78
- AVAX: 51 fills (24 buy / 27 sell), traded 84,304, gross pnl +123.99, +29 bps per round trip, avg half spread 1.4 bps, open 106.147
- BTC: 41 fills (23 buy / 18 sell), traded 57,103, gross pnl -97.11, -34 bps per round trip, avg half spread 0.1 bps, open 0.0118015
- DOGE: 38 fills (19 buy / 19 sell), traded 48,152, gross pnl -276.96, -115 bps per round trip, avg half spread 0.9 bps, open 12234.7
- DOT: 47 fills (22 buy / 25 sell), traded 69,133, gross pnl -174.48, -50 bps per round trip, avg half spread 2.3 bps
- ETH: 43 fills (21 buy / 22 sell), traded 57,282, gross pnl -99.19, -35 bps per round trip, avg half spread 0.2 bps, open 0.389481
- LINK: 48 fills (25 buy / 23 sell), traded 80,265, gross pnl -409.81, -102 bps per round trip, avg half spread 2.0 bps, open 80.0549
- LTC: 44 fills (21 buy / 23 sell), traded 59,638, gross pnl +407.27, +137 bps per round trip, avg half spread 1.6 bps, open 16.713
- SOL: 39 fills (21 buy / 18 sell), traded 59,894, gross pnl -106.90, -36 bps per round trip, avg half spread 0.5 bps, open 9.79557
- XRP: 41 fills (20 buy / 21 sell), traded 54,165, gross pnl +49.51, +18 bps per round trip, avg half spread 0.4 bps, open 720.804

last fills:

- 2026-11-04 16:10Z sell XRP 472 @ 1.31809 fee 0.47 slip 0.24 (half spread 0.0 bps)
- 2026-11-04 16:10Z sell DOGE 475 @ 0.0776543 fee 0.48 slip 0.24 (half spread 2.1 bps)
- 2026-11-04 16:10Z sell DOT 461 @ 0.969865 fee 0.46 slip 0.23 (half spread 0.5 bps)
- 2026-11-04 16:10Z buy SOL 951 @ 97.0635 fee 0.95 slip 0.48 (half spread 0.5 bps)
- 2026-11-04 16:10Z buy ADA 951 @ 0.199379 fee 0.95 slip 0.48 (half spread 2.7 bps)
- 2026-11-04 16:10Z buy LTC 945 @ 56.5483 fee 0.95 slip 0.47 (half spread 1.8 bps)
- 2026-11-05 06:10Z sell DOT 923 @ 0.942379 fee 0.92 slip 0.46 (half spread 0.5 bps)
- 2026-11-05 06:10Z buy LINK 921 @ 11.5086 fee 0.92 slip 0.46 (half spread 2.6 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,558.75 (started 10,000 at 2026-09-16 03:55Z), net -4.41% since start
- 24h +4.02%, 7d +1.51%, 30d -8.07%, max drawdown -15.05%
- fills 136 total, 31 in the last 7d
- costs 261.24 (fees 172.15 + slippage 89.09); gross pnl -180.02; cost coverage -0.69
- cash 9,558.75; positions: none
- last run 2026-11-05 13:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.09 not below -2.0
- 2026-11-05 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.29 not below -2.0
- 2026-11-05 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.41 not below -2.0
- 2026-11-05 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.55 not below -2.0
- 2026-11-05 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.33 not below -2.0
- 2026-11-05 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.23 not below -2.0
- 2026-11-05 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.48 not below -2.0
- 2026-11-05 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.08 not below -2.0
- 2026-11-05 13:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.56 not below -2.0
- 2026-11-05 13:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.66 not below -2.0
- 2026-11-05 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.43 not below -2.0
- 2026-11-05 13:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.14 not below -2.0
- 2026-11-05 13:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.02 not below -2.0
- 2026-11-05 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.17 not below -2.0
- 2026-11-05 13:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.89 not below -2.0
- 2026-11-05 13:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.30 not below -2.0
- 2026-11-05 13:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.09 not below -2.0
- 2026-11-05 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.52 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 12 fills (6 buy / 6 sell), traded 15,571, gross pnl -19.51, -25 bps per round trip, avg half spread 1.9 bps
- AVAX: 14 fills (8 buy / 6 sell), traded 16,832, gross pnl +143.39, +170 bps per round trip, avg half spread 1.5 bps
- BTC: 10 fills (6 buy / 4 sell), traded 13,232, gross pnl +77.24, +117 bps per round trip, avg half spread 0.1 bps
- DOGE: 15 fills (8 buy / 7 sell), traded 20,951, gross pnl -86.40, -82 bps per round trip, avg half spread 0.7 bps
- DOT: 10 fills (5 buy / 5 sell), traded 12,757, gross pnl -383.72, -602 bps per round trip, avg half spread 2.4 bps
- ETH: 15 fills (7 buy / 8 sell), traded 21,275, gross pnl +123.89, +116 bps per round trip, avg half spread 0.3 bps
- LINK: 17 fills (10 buy / 7 sell), traded 18,950, gross pnl +224.22, +237 bps per round trip, avg half spread 1.8 bps
- LTC: 15 fills (8 buy / 7 sell), traded 17,855, gross pnl +76.53, +86 bps per round trip, avg half spread 1.3 bps
- SOL: 16 fills (10 buy / 6 sell), traded 21,709, gross pnl -113.08, -104 bps per round trip, avg half spread 0.5 bps
- XRP: 12 fills (6 buy / 6 sell), traded 13,015, gross pnl -222.60, -342 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-11-04 09:03Z sell DOT 1,528 @ 0.94961 fee 1.53 slip 0.79 (half spread 3.2 bps)
- 2026-11-04 09:03Z buy LINK 518 @ 11.1277 fee 0.52 slip 0.26 (half spread 1.8 bps)
- 2026-11-04 15:11Z sell ADA 1,596 @ 0.199799 fee 1.60 slip 1.02 (half spread 4.4 bps)
- 2026-11-04 15:11Z sell LINK 1,941 @ 11.7126 fee 1.94 slip 1.69 (half spread 6.7 bps)
- 2026-11-04 15:11Z sell DOGE 1,586 @ 0.0779019 fee 1.59 slip 0.87 (half spread 3.5 bps)
- 2026-11-04 15:11Z sell LTC 1,597 @ 56.7216 fee 1.60 slip 0.80 (half spread 1.8 bps)
- 2026-11-04 15:11Z buy SOL 814 @ 97.5588 fee 0.81 slip 0.41 (half spread 1.0 bps)
- 2026-11-04 16:10Z sell SOL 2,383 @ 96.9665 fee 2.38 slip 1.19 (half spread 0.5 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 9,458.63 (started 10,000 at 2026-09-16 23:20Z), net -5.41% since start
- 24h -2.09%, 7d -6.07%, 30d -13.67%, max drawdown -14.84%
- fills 62 total, 14 in the last 7d
- costs 182.35 (fees 119.83 + slippage 62.52); gross pnl -359.02; cost coverage -1.97
- cash -0.00; positions: ADA 11910, DOGE 31289.3, DOT 2468.32, XRP 1875.19
- last run 2026-11-05 13:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 12:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 0.1978 still above 72h low 0.1849; realised vol 70% -> weight 0.25
- 2026-11-05 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 12:10Z XRP hold target 0.25 (held 0.26) — hold: weight change -0.008 below threshold 0.05 | stay long: price 1.317 still above 72h low 1.241; realised vol 55% -> weight 0.25
- 2026-11-05 12:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.0768 still above 72h low 0.07307; realised vol 60% -> weight 0.25
- 2026-11-05 12:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: price 0.9507 still above 72h low 0.92; realised vol 86% -> weight 0.25
- 2026-11-05 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 13:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 13:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 13:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: price 0.1951 still above 72h low 0.1849; realised vol 71% -> weight 0.25
- 2026-11-05 13:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-05 13:10Z XRP hold target 0.25 (held 0.26) — hold: weight change -0.009 below threshold 0.05 | stay long: price 1.304 still above 72h low 1.241; realised vol 56% -> weight 0.25
- 2026-11-05 13:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.07587 still above 72h low 0.07307; realised vol 60% -> weight 0.25
- 2026-11-05 13:10Z DOT hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: price 0.9334 still above 72h low 0.92; realised vol 87% -> weight 0.25
- 2026-11-05 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 6 fills (3 buy / 3 sell), traded 12,452, gross pnl -154.94, -249 bps per round trip, avg half spread 1.6 bps, open 11910
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 10 fills (5 buy / 5 sell), traded 21,231, gross pnl -174.17, -164 bps per round trip, avg half spread 0.0 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 16,720, gross pnl -280.27, -335 bps per round trip, avg half spread 1.3 bps, open 31289.3
- DOT: 4 fills (2 buy / 2 sell), traded 7,654, gross pnl +73.97, +193 bps per round trip, avg half spread 4.4 bps, open 2468.32
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 5 fills (3 buy / 2 sell), traded 7,935, gross pnl -94.34, -238 bps per round trip, avg half spread 2.9 bps
- LTC: 6 fills (3 buy / 3 sell), traded 12,367, gross pnl -84.66, -137 bps per round trip, avg half spread 2.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 7 fills (4 buy / 3 sell), traded 13,945, gross pnl -187.64, -269 bps per round trip, avg half spread 0.1 bps, open 1875.19

last fills:

- 2026-10-29 21:10Z sell BTC 1,984 @ 78979.6 fee 1.98 slip 0.99 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell LINK 2,401 @ 11.1222 fee 2.40 slip 1.58 (half spread 4.6 bps)
- 2026-10-29 21:10Z sell DOGE 2,412 @ 0.0759279 fee 2.41 slip 1.40 (half spread 3.8 bps)
- 2026-10-29 21:10Z sell LTC 2,386 @ 55.3789 fee 2.39 slip 1.34 (half spread 3.6 bps)
- 2026-11-04 11:10Z buy XRP 2,422 @ 1.29136 fee 2.42 slip 1.21 (half spread 0.0 bps)
- 2026-11-04 15:11Z buy DOGE 2,440 @ 0.0779875 fee 2.44 slip 1.34 (half spread 3.5 bps)
- 2026-11-04 15:11Z buy DOT 2,440 @ 0.988598 fee 2.44 slip 2.34 (half spread 7.6 bps)
- 2026-11-04 16:10Z buy ADA 2,375 @ 0.199379 fee 2.37 slip 1.19 (half spread 2.7 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.27%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-05 13:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-05 12:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2015 (need +10.0%)
- 2026-11-05 12:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-05 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-05 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-05 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-05 12:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.005 (need +10.0%)
- 2026-11-05 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)
- 2026-11-05 13:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.604e+04 not a higher low vs prior low 7.948e+04 (need +10.0%)
- 2026-11-05 13:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2300 (need +10.0%)
- 2026-11-05 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-05 13:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2015 (need +10.0%)
- 2026-11-05 13:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-05 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-05 13:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-05 13:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-05 13:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.005 (need +10.0%)
- 2026-11-05 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)

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

- equity 9,638.00 (started 10,000 at 2026-10-13 17:26Z), net -3.62% since start
- 24h +0.56%, 7d +1.49%, 30d -3.62%, max drawdown -12.71%
- fills 30 total, 12 in the last 7d
- costs 62.94 (fees 40.22 + slippage 22.72); gross pnl -299.06; cost coverage -4.75
- cash 2,517.83; positions: ADA 12106.8, AVAX 276.724, DOT 2516.14
- last run 2026-11-05 13:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 12:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.54 not below -2.0
- 2026-11-05 12:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: ratio to BTC z -1.16 vs 720h mean (entry -2.0, exit -0.25); vol 70% -> weigh...
- 2026-11-05 12:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.11 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-11-05 12:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.95 not below -2.0
- 2026-11-05 12:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.20 not below -2.0
- 2026-11-05 12:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.03 not below -2.0
- 2026-11-05 12:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: ratio to BTC z -1.64 vs 720h mean (entry -2.0, exit -0.25); vol 86% -> weigh...
- 2026-11-05 12:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.33 not below -2.0
- 2026-11-05 13:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-05 13:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.72 not below -2.0
- 2026-11-05 13:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.63 not below -2.0
- 2026-11-05 13:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: ratio to BTC z -1.23 vs 720h mean (entry -2.0, exit -0.25); vol 71% -> weigh...
- 2026-11-05 13:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.13 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-11-05 13:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.95 not below -2.0
- 2026-11-05 13:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.14 not below -2.0
- 2026-11-05 13:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.13 not below -2.0
- 2026-11-05 13:10Z DOT hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: ratio to BTC z -1.77 vs 720h mean (entry -2.0, exit -0.25); vol 87% -> weigh...
- 2026-11-05 13:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.38 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (3 buy / 1 sell), traded 5,091, gross pnl -79.68, -313 bps per round trip, avg half spread 3.3 bps, open 12106.8
- AVAX: 4 fills (3 buy / 1 sell), traded 5,003, gross pnl +5.97, +24 bps per round trip, avg half spread 3.5 bps, open 276.724
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 5 fills (3 buy / 2 sell), traded 5,904, gross pnl +31.97, +108 bps per round trip, avg half spread 3.9 bps, open 2516.14
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

- BTC: live 1930 candles, 2026-08-17 03:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1930 candles, 2026-08-17 03:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1930 candles, 2026-08-17 03:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 1930 candles, 2026-08-17 03:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 1930 candles, 2026-08-17 03:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LINK: live 1930 candles, 2026-08-17 03:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 1902 candles, 2026-08-18 07:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1902 candles, 2026-08-18 07:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1902 candles, 2026-08-18 07:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.4 bps
- LTC: live 1902 candles, 2026-08-18 07:00Z to 2026-11-05 12:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.6 bps
