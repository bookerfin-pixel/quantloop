# quantloop summary — generated 2026-11-04 22:10Z

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

- challenger1: testing H1 since 2026-09-16 05:21Z, day 49.7 of 60, 10.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -15.38% (max drawdown -34.03%, 425 fills) vs challenger1 -4.30% (max drawdown -15.05%, 136 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -17.28% (usual 0.54, this window 0.52) vs challenger1 -5.62% (usual 0.37, this window 0.50); the rule compares on skill, daily edge t +0.78 over 50 days
  trades: its 45 finished trades made -4.42% of its starting equity after costs (28 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.67 over 50 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +5.70%, equal weight basket of 10 pairs +3.53%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 44.6 of 60, 15.4 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -26.35% (max drawdown -34.03%, 387 fills) vs challenger2 -12.59% (max drawdown -13.80%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -19.68% (usual 0.54, this window 0.49) vs challenger2 -9.05% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +1.45 over 45 days
  trades: its 11 finished trades made -11.67% of its starting equity after costs (0 won, 11 lost, 4 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 4% that this is a real edge (every idea starts at 10%; the daily skill t is -1.69 over 45 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -2.87%, equal weight basket of 10 pairs -12.37%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 30.0 of 60, 30.0 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -23.84% (max drawdown -26.06%, 236 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -13.91% (usual 0.55, this window 0.38) vs challenger3 -0.76% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.82 over 30 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.70 over 30 days)
  fills: 10 in 30.0 days, 8 of them in the hour it began; at this pace about 16 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -6.71%, equal weight basket of 10 pairs -18.10%, basket max drawdown -23%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 20.0 of 120, 100.0 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -2.42% (max drawdown -12.71%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +1.98% (usual 0.53, this window 0.92); the rule compares on skill, daily edge t +0.37 over 20 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -14.83% so far
  trades: its 9 finished trades made -6.54% of its starting equity after costs (2 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 11% that this is a real edge (every idea starts at 10%; the daily skill t is +0.37 over 20 days)
  market over the window: BTC -2.62%, equal weight basket of 10 pairs -8.33%, basket max drawdown -15%, basket realised vol 51% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,462.04 (started 10,000 at 2026-09-16 03:55Z), net -15.38% since start
- 24h +0.70%, 7d -8.09%, 30d -23.84%, max drawdown -34.03%
- fills 425 total, 80 in the last 7d
- costs 926.29 (fees 613.17 + slippage 313.12); gross pnl -611.67; cost coverage -0.66
- cash -0.00; positions: ADA 4768.78, AVAX 106.147, BTC 0.0118015, DOGE 12234.7, DOT 979.607, ETH 0.389481, LTC 16.713, SOL 9.79557, XRP 720.804
- last run 2026-11-04 22:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 21:10Z SOL hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.57% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-04 21:10Z ADA hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.13% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-04 21:10Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.99% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-04 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.06% not above entry band +1.0%
- 2026-11-04 21:10Z XRP hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +4.35% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-04 21:10Z DOGE hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +1.98% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-04 21:10Z DOT hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.68% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-04 21:10Z LTC hold target 0.11 (held 0.11) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +1.12% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-04 22:10Z BTC hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +3.06% vs exit band -1.0% and price above 24h EMA; realised vol 4...
- 2026-11-04 22:10Z ETH hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +6.86% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-04 22:10Z SOL hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.45% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-04 22:10Z ADA hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.46% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-04 22:10Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +1.20% vs exit band -1.0% and price above 24h EMA; realised vol 7...
- 2026-11-04 22:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.71% not above entry band +1.0%
- 2026-11-04 22:10Z XRP hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +4.35% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-04 22:10Z DOGE hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +2.08% vs exit band -1.0% and price above 24h EMA; realised vol 6...
- 2026-11-04 22:10Z DOT hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +0.94% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-04 22:10Z LTC hold target 0.11 (held 0.11) — hold: weight change -0.000 below threshold 0.05 | stay long: 72h return +1.30% vs exit band -1.0% and price above 24h EMA; realised vol 6...

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 35 fills (16 buy / 19 sell), traded 45,076, gross pnl -118.19, -52 bps per round trip, avg half spread 2.1 bps, open 4768.78
- AVAX: 51 fills (24 buy / 27 sell), traded 84,304, gross pnl +133.49, +32 bps per round trip, avg half spread 1.4 bps, open 106.147
- BTC: 41 fills (23 buy / 18 sell), traded 57,103, gross pnl -86.87, -30 bps per round trip, avg half spread 0.1 bps, open 0.0118015
- DOGE: 38 fills (19 buy / 19 sell), traded 48,152, gross pnl -262.57, -109 bps per round trip, avg half spread 0.9 bps, open 12234.7
- DOT: 46 fills (22 buy / 24 sell), traded 68,210, gross pnl -155.14, -45 bps per round trip, avg half spread 2.3 bps, open 979.607
- ETH: 43 fills (21 buy / 22 sell), traded 57,282, gross pnl -85.09, -30 bps per round trip, avg half spread 0.2 bps, open 0.389481
- LINK: 47 fills (24 buy / 23 sell), traded 79,344, gross pnl -403.27, -102 bps per round trip, avg half spread 2.0 bps
- LTC: 44 fills (21 buy / 23 sell), traded 59,638, gross pnl +424.82, +142 bps per round trip, avg half spread 1.6 bps, open 16.713
- SOL: 39 fills (21 buy / 18 sell), traded 59,894, gross pnl -108.18, -36 bps per round trip, avg half spread 0.5 bps, open 9.79557
- XRP: 41 fills (20 buy / 21 sell), traded 54,165, gross pnl +49.34, +18 bps per round trip, avg half spread 0.4 bps, open 720.804

last fills:

- 2026-11-04 16:10Z sell ETH 491 @ 2439.32 fee 0.49 slip 0.25 (half spread 0.0 bps)
- 2026-11-04 16:10Z sell AVAX 466 @ 8.95021 fee 0.47 slip 0.25 (half spread 3.4 bps)
- 2026-11-04 16:10Z sell XRP 472 @ 1.31809 fee 0.47 slip 0.24 (half spread 0.0 bps)
- 2026-11-04 16:10Z sell DOGE 475 @ 0.0776543 fee 0.48 slip 0.24 (half spread 2.1 bps)
- 2026-11-04 16:10Z sell DOT 461 @ 0.969865 fee 0.46 slip 0.23 (half spread 0.5 bps)
- 2026-11-04 16:10Z buy SOL 951 @ 97.0635 fee 0.95 slip 0.48 (half spread 0.5 bps)
- 2026-11-04 16:10Z buy ADA 951 @ 0.199379 fee 0.95 slip 0.48 (half spread 2.7 bps)
- 2026-11-04 16:10Z buy LTC 945 @ 56.5483 fee 0.95 slip 0.47 (half spread 1.8 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,558.75 (started 10,000 at 2026-09-16 03:55Z), net -4.41% since start
- 24h +4.10%, 7d +0.66%, 30d -8.07%, max drawdown -15.05%
- fills 136 total, 32 in the last 7d
- costs 261.24 (fees 172.15 + slippage 89.09); gross pnl -180.02; cost coverage -0.69
- cash 9,558.75; positions: none
- last run 2026-11-04 22:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.66 not below -2.0
- 2026-11-04 21:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.06 not below -2.0
- 2026-11-04 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.44 not below -2.0
- 2026-11-04 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.14 not below -2.0
- 2026-11-04 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.93 not below -2.0
- 2026-11-04 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-11-04 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.41 not below -2.0
- 2026-11-04 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.08 not below -2.0
- 2026-11-04 22:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.97 not below -2.0
- 2026-11-04 22:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.67 not below -2.0
- 2026-11-04 22:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.66 not below -2.0
- 2026-11-04 22:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.07 not below -2.0
- 2026-11-04 22:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.39 not below -2.0
- 2026-11-04 22:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.16 not below -2.0
- 2026-11-04 22:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.94 not below -2.0
- 2026-11-04 22:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.22 not below -2.0
- 2026-11-04 22:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.36 not below -2.0
- 2026-11-04 22:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.18 not below -2.0

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

- equity 9,584.89 (started 10,000 at 2026-09-16 23:20Z), net -4.15% since start
- 24h -1.05%, 7d -6.62%, 30d -12.53%, max drawdown -14.48%
- fills 62 total, 14 in the last 7d
- costs 182.35 (fees 119.83 + slippage 62.52); gross pnl -232.76; cost coverage -1.28
- cash -0.00; positions: ADA 11910, DOGE 31289.3, DOT 2468.32, XRP 1875.19
- last run 2026-11-04 22:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 21:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: price 0.196 still above 72h low 0.1849; realised vol 73% -> weight 0.25
- 2026-11-04 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 21:10Z XRP hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: price 1.303 still above 72h low 1.241; realised vol 56% -> weight 0.25
- 2026-11-04 21:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.07669 still above 72h low 0.07307; realised vol 61% -> weight 0.25
- 2026-11-04 21:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.9557 still above 72h low 0.92; realised vol 88% -> weight 0.25
- 2026-11-04 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 22:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 22:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 22:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 22:10Z ADA hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: price 0.1968 still above 72h low 0.1849; realised vol 73% -> weight 0.25
- 2026-11-04 22:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 22:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 22:10Z XRP hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: price 1.303 still above 72h low 1.241; realised vol 56% -> weight 0.25
- 2026-11-04 22:10Z DOGE hold target 0.25 (held 0.25) — hold: weight change -0.001 below threshold 0.05 | stay long: price 0.07679 still above 72h low 0.07307; realised vol 61% -> weight 0.25
- 2026-11-04 22:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 0.9568 still above 72h low 0.92; realised vol 88% -> weight 0.25
- 2026-11-04 22:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 6 fills (3 buy / 3 sell), traded 12,452, gross pnl -133.99, -215 bps per round trip, avg half spread 1.6 bps, open 11910
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 10 fills (5 buy / 5 sell), traded 21,231, gross pnl -174.17, -164 bps per round trip, avg half spread 0.0 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 16,720, gross pnl -243.48, -291 bps per round trip, avg half spread 1.3 bps, open 31289.3
- DOT: 4 fills (2 buy / 2 sell), traded 7,654, gross pnl +142.96, +374 bps per round trip, avg half spread 4.4 bps, open 2468.32
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 5 fills (3 buy / 2 sell), traded 7,935, gross pnl -94.34, -238 bps per round trip, avg half spread 2.9 bps
- LTC: 6 fills (3 buy / 3 sell), traded 12,367, gross pnl -84.66, -137 bps per round trip, avg half spread 2.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 7 fills (4 buy / 3 sell), traded 13,945, gross pnl -188.09, -270 bps per round trip, avg half spread 0.1 bps, open 1875.19

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
- last run 2026-11-04 22:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-04 21:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2031 (need +10.0%)
- 2026-11-04 21:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-04 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-04 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-04 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-04 21:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-11-04 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)
- 2026-11-04 22:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.604e+04 not a higher low vs prior low 7.97e+04 (need +10.0%)
- 2026-11-04 22:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2303 (need +10.0%)
- 2026-11-04 22:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-04 22:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2031 (need +10.0%)
- 2026-11-04 22:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-04 22:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-04 22:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-04 22:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-04 22:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-11-04 22:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)

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

- equity 9,754.39 (started 10,000 at 2026-10-13 17:26Z), net -2.46% since start
- 24h +2.07%, 7d +0.69%, 30d -2.46%, max drawdown -12.71%
- fills 30 total, 12 in the last 7d
- costs 62.94 (fees 40.22 + slippage 22.72); gross pnl -182.67; cost coverage -2.90
- cash 2,517.83; positions: ADA 12106.8, AVAX 276.724, DOT 2516.14
- last run 2026-11-04 22:10Z; halted today: False

last decisions (newest last):

- 2026-11-04 21:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.94 not below -2.0
- 2026-11-04 21:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: ratio to BTC z -1.28 vs 720h mean (entry -2.0, exit -0.25); vol 73% -> weigh...
- 2026-11-04 21:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.08 vs 720h mean (entry -2.0, exit -0.25); vol 78% -> weigh...
- 2026-11-04 21:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.16 not below -2.0
- 2026-11-04 21:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.19 not below -2.0
- 2026-11-04 21:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.98 not below -2.0
- 2026-11-04 21:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.61 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-04 21:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.15 not below -2.0
- 2026-11-04 22:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-04 22:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.76 not below -2.0
- 2026-11-04 22:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.98 not below -2.0
- 2026-11-04 22:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.005 below threshold 0.05 | stay long: ratio to BTC z -1.24 vs 720h mean (entry -2.0, exit -0.25); vol 73% -> weigh...
- 2026-11-04 22:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.11 vs 720h mean (entry -2.0, exit -0.25); vol 78% -> weigh...
- 2026-11-04 22:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.18 not below -2.0
- 2026-11-04 22:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.22 not below -2.0
- 2026-11-04 22:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.98 not below -2.0
- 2026-11-04 22:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: ratio to BTC z -1.61 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-04 22:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.12 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (3 buy / 1 sell), traded 5,091, gross pnl -58.38, -229 bps per round trip, avg half spread 3.3 bps, open 12106.8
- AVAX: 4 fills (3 buy / 1 sell), traded 5,003, gross pnl +30.74, +123 bps per round trip, avg half spread 3.5 bps, open 276.724
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 5 fills (3 buy / 2 sell), traded 5,904, gross pnl +102.29, +347 bps per round trip, avg half spread 3.9 bps, open 2516.14
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

- BTC: live 1915 candles, 2026-08-17 03:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1915 candles, 2026-08-17 03:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1915 candles, 2026-08-17 03:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 1915 candles, 2026-08-17 03:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.1 bps
- AVAX: live 1915 candles, 2026-08-17 03:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LINK: live 1915 candles, 2026-08-17 03:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 1887 candles, 2026-08-18 07:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1887 candles, 2026-08-18 07:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1887 candles, 2026-08-18 07:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1887 candles, 2026-08-18 07:00Z to 2026-11-04 21:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
