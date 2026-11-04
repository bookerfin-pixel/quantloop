# quantloop summary — generated 2026-11-04 15:11Z

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

- challenger1: testing H1 since 2026-09-16 05:21Z, day 49.4 of 60, 10.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -13.82% (max drawdown -34.03%, 416 fills) vs challenger1 -4.15% (max drawdown -15.05%, 135 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -15.79% (usual 0.54, this window 0.51) vs challenger1 -5.51% (usual 0.37, this window 0.51); the rule compares on skill, daily edge t +0.68 over 49 days
  trades: its 44 finished trades made -4.45% of its starting equity after costs (27 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 6% that this is a real edge (every idea starts at 10%; the daily skill t is -0.63 over 49 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +4.50%, equal weight basket of 10 pairs +3.66%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger2: testing H2 since 2026-09-21 08:24Z, day 44.3 of 60, 15.7 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -25.00% (max drawdown -34.03%, 378 fills) vs challenger2 -11.07% (max drawdown -12.34%, 29 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -18.36% (usual 0.54, this window 0.49) vs challenger2 -7.55% (usual 0.29, this window 0.15); the rule compares on skill, daily edge t +1.45 over 44 days
  trades: its 11 finished trades made -11.67% of its starting equity after costs (0 won, 11 lost, 4 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 4% that this is a real edge (every idea starts at 10%; the daily skill t is -1.45 over 44 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -3.98%, equal weight basket of 10 pairs -12.30%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger3: testing H5 since 2026-10-05 22:23Z, day 29.7 of 60, 30.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -22.44% (max drawdown -26.06%, 227 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -12.54% (usual 0.55, this window 0.37) vs challenger3 -0.76% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +2.38 over 30 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.70 over 30 days)
  fills: 10 in 29.7 days, 8 of them in the hour it began; at this pace about 16 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -7.77%, equal weight basket of 10 pairs -18.03%, basket max drawdown -23%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 19.7 of 120, 100.3 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -0.60% (max drawdown -12.71%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 +3.76% (usual 0.53, this window 0.92); the rule compares on skill, daily edge t +0.61 over 20 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -14.83% so far
  trades: its 9 finished trades made -6.54% of its starting equity after costs (2 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 11% that this is a real edge (every idea starts at 10%; the daily skill t is +0.61 over 20 days)
  market over the window: BTC -3.73%, equal weight basket of 10 pairs -8.26%, basket max drawdown -15%, basket realised vol 51% annualised
- free slots: none
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H2 in challenger2, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,617.83 (started 10,000 at 2026-09-16 03:55Z), net -13.82% since start
- 24h +2.62%, 7d -5.46%, 30d -22.49%, max drawdown -34.03%
- fills 416 total, 74 in the last 7d
- costs 917.72 (fees 607.47 + slippage 310.26); gross pnl -464.44; cost coverage -0.51
- cash -0.00; positions: AVAX 158.229, BTC 0.017838, DOGE 18355.5, DOT 1455.41, ETH 0.590884, XRP 1079.06
- last run 2026-11-04 15:11Z; halted today: False

last decisions (newest last):

- 2026-11-04 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -2.11% not above entry band +1.0%
- 2026-11-04 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.89% not above entry band +1.0% and price below 24h EMA
- 2026-11-04 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.99% not above entry band +1.0%
- 2026-11-04 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -3.65% not above entry band +1.0%
- 2026-11-04 14:10Z XRP hold target 0.25 (held 0.25) — hold: weight change -0.002 below threshold 0.05 | stay long: 72h return +2.30% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-04 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.18% not above entry band +1.0%
- 2026-11-04 14:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +0.21% vs exit band -1.0% and price above 24h EMA; realised vol 8...
- 2026-11-04 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -1.88% not above entry band +1.0%
- 2026-11-04 15:11Z BTC buy target 0.17 (held 0.00) — enter long: 72h return +1.69% vs entry band +1.0% and price above 24h EMA; realised vol 40% -> weight 0.25
- 2026-11-04 15:11Z ETH sell target 0.17 (held 0.26) — stay long: 72h return +4.75% vs exit band -1.0% and price above 24h EMA; realised vol 50% -> weight 0.25
- 2026-11-04 15:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.21% not above entry band +1.0%
- 2026-11-04 15:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.99% not above entry band +1.0%
- 2026-11-04 15:11Z AVAX buy target 0.17 (held 0.00) — enter long: 72h return +1.06% vs entry band +1.0% and price above 24h EMA; realised vol 77% -> weight 0.25
- 2026-11-04 15:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.39% not above entry band +1.0%
- 2026-11-04 15:11Z XRP sell target 0.17 (held 0.25) — stay long: 72h return +5.07% vs exit band -1.0% and price above 24h EMA; realised vol 57% -> weight 0.25
- 2026-11-04 15:11Z DOGE buy target 0.17 (held 0.00) — enter long: 72h return +1.19% vs entry band +1.0% and price above 24h EMA; realised vol 61% -> weight 0.25
- 2026-11-04 15:11Z DOT sell target 0.17 (held 0.25) — stay long: 72h return +2.52% vs exit band -1.0% and price above 24h EMA; realised vol 90% -> weight 0.25
- 2026-11-04 15:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return +0.05% not above entry band +1.0%

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 34 fills (15 buy / 19 sell), traded 44,125, gross pnl -108.35, -49 bps per round trip, avg half spread 2.1 bps
- AVAX: 50 fills (24 buy / 26 sell), traded 83,838, gross pnl +173.06, +41 bps per round trip, avg half spread 1.4 bps, open 158.229
- BTC: 40 fills (23 buy / 17 sell), traded 56,617, gross pnl -84.06, -30 bps per round trip, avg half spread 0.1 bps, open 0.017838
- DOGE: 37 fills (19 buy / 18 sell), traded 47,677, gross pnl -249.76, -105 bps per round trip, avg half spread 0.9 bps, open 18355.5
- DOT: 45 fills (22 buy / 23 sell), traded 67,748, gross pnl -122.37, -36 bps per round trip, avg half spread 2.4 bps, open 1455.41
- ETH: 42 fills (21 buy / 21 sell), traded 56,791, gross pnl -82.25, -29 bps per round trip, avg half spread 0.2 bps, open 0.590884
- LINK: 47 fills (24 buy / 23 sell), traded 79,344, gross pnl -403.27, -102 bps per round trip, avg half spread 2.0 bps
- LTC: 43 fills (20 buy / 23 sell), traded 58,693, gross pnl +429.16, +146 bps per round trip, avg half spread 1.6 bps
- SOL: 38 fills (20 buy / 18 sell), traded 58,943, gross pnl -89.47, -30 bps per round trip, avg half spread 0.5 bps
- XRP: 40 fills (20 buy / 20 sell), traded 53,692, gross pnl +72.86, +27 bps per round trip, avg half spread 0.4 bps, open 1079.06

last fills:

- 2026-11-04 01:10Z sell AVAX 2,047 @ 8.37331 fee 2.05 slip 1.02 (half spread 3.0 bps)
- 2026-11-04 11:10Z buy DOT 2,104 @ 0.965193 fee 2.10 slip 1.18 (half spread 3.6 bps)
- 2026-11-04 15:11Z sell ETH 841 @ 2431.78 fee 0.84 slip 0.45 (half spread 3.3 bps)
- 2026-11-04 15:11Z sell XRP 755 @ 1.33173 fee 0.75 slip 0.38 (half spread 0.4 bps)
- 2026-11-04 15:11Z sell DOT 715 @ 0.986702 fee 0.71 slip 0.69 (half spread 7.6 bps)
- 2026-11-04 15:11Z buy BTC 1,438 @ 80620.8 fee 1.44 slip 0.72 (half spread 0.0 bps)
- 2026-11-04 15:11Z buy AVAX 1,438 @ 9.08882 fee 1.44 slip 1.24 (half spread 6.6 bps)
- 2026-11-04 15:11Z buy DOGE 1,431 @ 0.0779875 fee 1.43 slip 0.79 (half spread 3.5 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,574.49 (started 10,000 at 2026-09-16 03:55Z), net -4.26% since start
- 24h +4.53%, 7d +2.05%, 30d -7.91%, max drawdown -15.05%
- fills 135 total, 32 in the last 7d
- costs 257.66 (fees 169.76 + slippage 87.90); gross pnl -167.85; cost coverage -0.65
- cash 7,178.19; positions: SOL 24.5749
- last run 2026-11-04 15:11Z; halted today: False

last decisions (newest last):

- 2026-11-04 14:10Z SOL hold target 0.20 (held 0.16) — hold: weight change +0.036 below threshold 0.05 | stay long: z -1.23 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-11-04 14:10Z ADA hold target 0.20 (held 0.16) — hold: weight change +0.036 below threshold 0.05 | stay long: z -1.05 vs 240h mean (entry -2.0, exit -0.5); vol 70% -> weight 0.25
- 2026-11-04 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.02 not below -2.0
- 2026-11-04 14:10Z LINK hold target 0.20 (held 0.20) — hold: weight change -0.000 below threshold 0.05 | stay long: z -0.82 vs 240h mean (entry -2.0, exit -0.5); vol 79% -> weight 0.25
- 2026-11-04 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-11-04 14:10Z DOGE hold target 0.20 (held 0.17) — hold: weight change +0.035 below threshold 0.05 | stay long: z -0.96 vs 240h mean (entry -2.0, exit -0.5); vol 58% -> weight 0.25
- 2026-11-04 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.56 not below -2.0
- 2026-11-04 14:10Z LTC hold target 0.20 (held 0.17) — hold: weight change +0.033 below threshold 0.05 | stay long: z -0.87 vs 240h mean (entry -2.0, exit -0.5); vol 70% -> weight 0.25
- 2026-11-04 15:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.35 not below -2.0
- 2026-11-04 15:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +2.05 not below -2.0
- 2026-11-04 15:11Z SOL buy target 0.25 (held 0.17) — stay long: z -0.59 vs 240h mean (entry -2.0, exit -0.5); vol 61% -> weight 0.25
- 2026-11-04 15:11Z ADA sell target 0.00 (held 0.17) — flat: z -0.23 not below -0.5
- 2026-11-04 15:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.81 not below -2.0
- 2026-11-04 15:11Z LINK sell target 0.00 (held 0.20) — flat: z +0.61 not below -0.5
- 2026-11-04 15:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +1.38 not below -2.0
- 2026-11-04 15:11Z DOGE sell target 0.00 (held 0.17) — flat: z +0.11 not below -0.5
- 2026-11-04 15:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.17 not below -2.0
- 2026-11-04 15:11Z LTC sell target 0.00 (held 0.17) — flat: z +0.00 not below -0.5

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 12 fills (6 buy / 6 sell), traded 15,571, gross pnl -19.51, -25 bps per round trip, avg half spread 1.9 bps
- AVAX: 14 fills (8 buy / 6 sell), traded 16,832, gross pnl +143.39, +170 bps per round trip, avg half spread 1.5 bps
- BTC: 10 fills (6 buy / 4 sell), traded 13,232, gross pnl +77.24, +117 bps per round trip, avg half spread 0.1 bps
- DOGE: 15 fills (8 buy / 7 sell), traded 20,951, gross pnl -86.40, -82 bps per round trip, avg half spread 0.7 bps
- DOT: 10 fills (5 buy / 5 sell), traded 12,757, gross pnl -383.72, -602 bps per round trip, avg half spread 2.4 bps
- ETH: 15 fills (7 buy / 8 sell), traded 21,275, gross pnl +123.89, +116 bps per round trip, avg half spread 0.3 bps
- LINK: 17 fills (10 buy / 7 sell), traded 18,950, gross pnl +224.22, +237 bps per round trip, avg half spread 1.8 bps
- LTC: 15 fills (8 buy / 7 sell), traded 17,855, gross pnl +76.53, +86 bps per round trip, avg half spread 1.3 bps
- SOL: 15 fills (10 buy / 5 sell), traded 19,326, gross pnl -100.92, -104 bps per round trip, avg half spread 0.5 bps, open 24.5749
- XRP: 12 fills (6 buy / 6 sell), traded 13,015, gross pnl -222.60, -342 bps per round trip, avg half spread 0.7 bps

last fills:

- 2026-11-04 08:10Z buy LTC 1,264 @ 54.7374 fee 1.26 slip 0.63 (half spread 1.8 bps)
- 2026-11-04 09:03Z sell DOT 1,528 @ 0.94961 fee 1.53 slip 0.79 (half spread 3.2 bps)
- 2026-11-04 09:03Z buy LINK 518 @ 11.1277 fee 0.52 slip 0.26 (half spread 1.8 bps)
- 2026-11-04 15:11Z sell ADA 1,596 @ 0.199799 fee 1.60 slip 1.02 (half spread 4.4 bps)
- 2026-11-04 15:11Z sell LINK 1,941 @ 11.7126 fee 1.94 slip 1.69 (half spread 6.7 bps)
- 2026-11-04 15:11Z sell DOGE 1,586 @ 0.0779019 fee 1.59 slip 0.87 (half spread 3.5 bps)
- 2026-11-04 15:11Z sell LTC 1,597 @ 56.7216 fee 1.60 slip 0.80 (half spread 1.8 bps)
- 2026-11-04 15:11Z buy SOL 814 @ 97.5588 fee 0.81 slip 0.41 (half spread 1.0 bps)

## challenger2: vol_breakout (H2)

params: {"breakout_hours": 120, "compression_hours": 168, "exit_hours": 72, "lookback_hours": 1440, "max_weight": 0.25, "squeeze_memory_hours": 72, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "vol_percentile": 0.25}

- equity 9,752.14 (started 10,000 at 2026-09-16 23:20Z), net -2.48% since start
- 24h +0.68%, 7d -4.61%, 30d -10.78%, max drawdown -13.03%
- fills 61 total, 15 in the last 7d
- costs 178.79 (fees 117.45 + slippage 61.33); gross pnl -69.08; cost coverage -0.39
- cash 2,376.97; positions: DOGE 31289.3, DOT 2468.32, XRP 1875.19
- last run 2026-11-04 15:11Z; halted today: False

last decisions (newest last):

- 2026-11-04 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.1897 not above 120h high 0.1961
- 2026-11-04 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 14:10Z XRP hold target 0.25 (held 0.25) — hold: weight change +0.002 below threshold 0.05 | stay long: price 1.281 still above 72h low 1.241; realised vol 53% -> weight 0.25
- 2026-11-04 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.07475 not above 120h high 0.07612
- 2026-11-04 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.9521 not above 120h high 0.9753
- 2026-11-04 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 15:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 15:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 15:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 15:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: squeezed but 0.1951 not above 120h high 0.1961
- 2026-11-04 15:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 15:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h
- 2026-11-04 15:11Z XRP hold target 0.25 (held 0.26) — hold: weight change -0.006 below threshold 0.05 | stay long: price 1.315 still above 72h low 1.241; realised vol 57% -> weight 0.25
- 2026-11-04 15:11Z DOGE buy target 0.25 (held 0.00) — enter long: squeeze in last 72h (168h vol at or below its own 25% percentile over 1440h) then broke above 120h high 0.07612 at 0.0766; re...
- 2026-11-04 15:11Z DOT buy target 0.25 (held 0.00) — enter long: squeeze in last 72h (168h vol at or below its own 25% percentile over 1440h) then broke above 120h high 0.9753 at 0.9756; rea...
- 2026-11-04 15:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 168h vol not at or below its own 25% percentile over 1440h in the last 72h

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 5 fills (2 buy / 3 sell), traded 10,078, gross pnl -109.42, -217 bps per round trip, avg half spread 1.4 bps
- AVAX: 7 fills (3 buy / 4 sell), traded 13,815, gross pnl +637.82, +923 bps per round trip, avg half spread 1.4 bps
- BTC: 10 fills (5 buy / 5 sell), traded 21,231, gross pnl -174.17, -164 bps per round trip, avg half spread 0.0 bps
- DOGE: 10 fills (6 buy / 4 sell), traded 16,720, gross pnl -214.66, -257 bps per round trip, avg half spread 1.3 bps, open 31289.3
- DOT: 4 fills (2 buy / 2 sell), traded 7,654, gross pnl +204.79, +535 bps per round trip, avg half spread 4.4 bps, open 2468.32
- ETH: 5 fills (3 buy / 2 sell), traded 10,714, gross pnl -136.94, -256 bps per round trip, avg half spread 0.0 bps
- LINK: 5 fills (3 buy / 2 sell), traded 7,935, gross pnl -94.34, -238 bps per round trip, avg half spread 2.9 bps
- LTC: 6 fills (3 buy / 3 sell), traded 12,367, gross pnl -84.66, -137 bps per round trip, avg half spread 2.7 bps
- SOL: 2 fills (1 buy / 1 sell), traded 2,993, gross pnl +42.14, +282 bps per round trip, avg half spread 0.5 bps
- XRP: 7 fills (4 buy / 3 sell), traded 13,945, gross pnl -139.63, -200 bps per round trip, avg half spread 0.1 bps, open 1875.19

last fills:

- 2026-10-29 19:10Z buy DOGE 509 @ 0.0791227 fee 0.51 slip 0.25 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell BTC 1,984 @ 78979.6 fee 1.98 slip 0.99 (half spread 0.0 bps)
- 2026-10-29 21:10Z sell LINK 2,401 @ 11.1222 fee 2.40 slip 1.58 (half spread 4.6 bps)
- 2026-10-29 21:10Z sell DOGE 2,412 @ 0.0759279 fee 2.41 slip 1.40 (half spread 3.8 bps)
- 2026-10-29 21:10Z sell LTC 2,386 @ 55.3789 fee 2.39 slip 1.34 (half spread 3.6 bps)
- 2026-11-04 11:10Z buy XRP 2,422 @ 1.29136 fee 2.42 slip 1.21 (half spread 0.0 bps)
- 2026-11-04 15:11Z buy DOGE 2,440 @ 0.0779875 fee 2.44 slip 1.34 (half spread 3.5 bps)
- 2026-11-04 15:11Z buy DOT 2,440 @ 0.988598 fee 2.44 slip 2.34 (half spread 7.6 bps)

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.47%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-04 15:11Z; halted today: False

last decisions (newest last):

- 2026-11-04 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-04 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2031 (need +10.0%)
- 2026-11-04 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-04 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-04 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-04 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-04 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-11-04 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)
- 2026-11-04 15:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.604e+04 not a higher low vs prior low 7.97e+04 (need +10.0%)
- 2026-11-04 15:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2303 (need +10.0%)
- 2026-11-04 15:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-04 15:11Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2031 (need +10.0%)
- 2026-11-04 15:11Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-04 15:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-04 15:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-04 15:11Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-04 15:11Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.016 (need +10.0%)
- 2026-11-04 15:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)

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

- equity 9,936.30 (started 10,000 at 2026-10-13 17:26Z), net -0.64% since start
- 24h +4.10%, 7d +3.99%, 30d -0.64%, max drawdown -12.71%
- fills 30 total, 12 in the last 7d
- costs 62.94 (fees 40.22 + slippage 22.72); gross pnl -0.75; cost coverage -0.01
- cash 2,517.83; positions: ADA 12106.8, AVAX 276.724, DOT 2516.14
- last run 2026-11-04 15:11Z; halted today: False

last decisions (newest last):

- 2026-11-04 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.91 not below -2.0
- 2026-11-04 14:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.011 below threshold 0.05 | stay long: ratio to BTC z -1.43 vs 720h mean (entry -2.0, exit -0.25); vol 70% -> weigh...
- 2026-11-04 14:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -0.92 vs 720h mean (entry -2.0, exit -0.25); vol 76% -> weigh...
- 2026-11-04 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.18 not below -2.0
- 2026-11-04 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.00 not below -2.0
- 2026-11-04 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.06 not below -2.0
- 2026-11-04 14:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.001 below threshold 0.05 | stay long: ratio to BTC z -1.38 vs 720h mean (entry -2.0, exit -0.25); vol 88% -> weigh...
- 2026-11-04 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.16 not below -2.0
- 2026-11-04 15:11Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-04 15:11Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.48 not below -2.0
- 2026-11-04 15:11Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.62 not below -2.0
- 2026-11-04 15:11Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: ratio to BTC z -1.22 vs 720h mean (entry -2.0, exit -0.25); vol 73% -> weigh...
- 2026-11-04 15:11Z AVAX hold target 0.25 (held 0.25) — hold: weight change -0.003 below threshold 0.05 | stay long: ratio to BTC z -0.79 vs 720h mean (entry -2.0, exit -0.25); vol 77% -> weigh...
- 2026-11-04 15:11Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.66 not below -2.0
- 2026-11-04 15:11Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.54 not below -2.0
- 2026-11-04 15:11Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.75 not below -2.0
- 2026-11-04 15:11Z DOT hold target 0.25 (held 0.25) — hold: weight change -0.000 below threshold 0.05 | stay long: ratio to BTC z -1.20 vs 720h mean (entry -2.0, exit -0.25); vol 90% -> weigh...
- 2026-11-04 15:11Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.95 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (3 buy / 1 sell), traded 5,091, gross pnl -25.56, -100 bps per round trip, avg half spread 3.3 bps, open 12106.8
- AVAX: 4 fills (3 buy / 1 sell), traded 5,003, gross pnl +116.80, +467 bps per round trip, avg half spread 3.5 bps, open 276.724
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 5 fills (3 buy / 2 sell), traded 5,904, gross pnl +165.32, +560 bps per round trip, avg half spread 3.9 bps, open 2516.14
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

- BTC: live 1908 candles, 2026-08-17 03:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1908 candles, 2026-08-17 03:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1908 candles, 2026-08-17 03:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 1908 candles, 2026-08-17 03:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 1908 candles, 2026-08-17 03:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.7 bps
- LINK: live 1908 candles, 2026-08-17 03:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 1880 candles, 2026-08-18 07:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1880 candles, 2026-08-18 07:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1880 candles, 2026-08-18 07:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1880 candles, 2026-08-18 07:00Z to 2026-11-04 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
