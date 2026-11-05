# quantloop summary — generated 2026-11-05 15:25Z

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

- challenger1: testing H1 since 2026-09-16 05:21Z, day 50.4 of 60, 9.6 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -19.79% (max drawdown -35.86%, 436 fills) vs challenger1 -4.30% (max drawdown -15.05%, 136 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -20.14% (usual 0.54, this window 0.52) vs challenger1 -4.55% (usual 0.37, this window 0.50); the rule compares on skill, daily edge t +0.97 over 50 days
  trades: its 45 finished trades made -4.42% of its starting equity after costs (28 won, 17 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.51 over 50 days)
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC +3.11%, equal weight basket of 10 pairs +0.66%, basket max drawdown -24%, basket realised vol 56% annualised
- challenger2: idle, holds cash (free for a hypothesis)
- challenger3: testing H5 since 2026-10-05 22:23Z, day 30.7 of 60, 29.3 days until the verdict (one look at day 60: promoted, killed, or kept 60 more days if its trades are of value and it does not pass)
  so far: champion -27.81% (max drawdown -28.11%, 247 fills) vs challenger3 -1.27% (max drawdown -1.52%, 10 fills)
  skill (net return minus the basket held at the strategy's usual exposure): champion -16.63% (usual 0.55, this window 0.39) vs challenger3 -0.70% (usual 0.03, this window 0.01); the rule compares on skill, daily edge t +3.02 over 31 days
  trades: its 1 finished trade made -1.27% of its starting equity after costs (0 won, 1 lost), and a test that does not pass the rule is kept only when they have made money
  confidence: 7% that this is a real edge (every idea starts at 10%; the daily skill t is -0.62 over 31 days)
  fills: 10 in 30.7 days, 8 of them in the hour it began; at this pace about 15 by day 120, under the 30 a promotion needs. Trading little does not end a test by itself: day 60 keeps a test whose trades are of value and kills one whose are not, and a test that is kept and still short of 30 fills at its verdict ends unproven, not promoted
  two look rule (measured, not applied to this test): on today's numbers it would be killed at day 60, the same as under its own rule
  against cash (measured, not applied to this test): by its one look rule, on today's numbers it would be killed at day 60, the same as against the champion
  market over the window: BTC -9.00%, equal weight basket of 10 pairs -20.36%, basket max drawdown -23%, basket realised vol 55% annualised
- challenger4: testing H6, judged against cash since 2026-10-15 23:10Z, day 20.7 of 120, 99.3 days until the verdict, first look at day 60 (two look rule)
  so far: cash +0.00% (holds nothing) vs challenger4 -5.87% (max drawdown -12.71%, 30 fills)
  skill (net return minus the basket held at the strategy's usual exposure): cash +0.00% (holds nothing) vs challenger4 -0.13% (usual 0.53, this window 0.91); the rule compares on skill, daily edge t +0.05 over 21 days
  judged against cash: its drawdown guard is set against the equal weight basket's worst fall in the window, -14.83% so far
  trades: its 9 finished trades made -6.54% of its starting equity after costs (2 won, 7 lost, 7 of them closed by the daily loss halt or a strategy error), and a test that does not pass the rule is kept only when they have made money
  confidence: 10% that this is a real edge (every idea starts at 10%; the daily skill t is +0.05 over 21 days)
  market over the window: BTC -5.01%, equal weight basket of 10 pairs -10.87%, basket max drawdown -15%, basket realised vol 52% annualised
- free slots: challenger2
- shadow: none (no promotion within the last window)
- interim readings are not verdicts. A test is ruled on at its looks, day 60 and day 120, and before them only by an early kill
- a finished trade is a position the account left (sold down to a twentieth or less); one of its own is one the strategy chose to leave, not one the daily loss halt sold. A test that has finished none of its own is killed at its look; one that does not pass the rule is kept when its finished trades made money after costs (PROMOTION.md)
- confidence is the chance the strategy has a real edge, from the t of its daily skill over the whole test so far. It moves slowly on purpose: 60 days of data cannot say much (PROMOTION.md)

## champion: ts_momentum (H0)

retired by Fin (configs/risk.yaml, retired_champions): the champion's title is cash now, not H0. This account runs H0 only as the yardstick for the tests judged against this account (H1 in challenger1, H5 in challenger3), and holds cash once they end

params: {"ema_exit_buffer": 0.02, "ema_hours": 24, "entry_return": 0.01, "exit_return": -0.01, "lookback_hours": 72, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 8,021.41 (started 10,000 at 2026-09-16 03:55Z), net -19.79% since start
- 24h -6.17%, 7d -12.51%, 30d -28.05%, max drawdown -35.86%
- fills 436 total, 73 in the last 7d
- costs 942.29 (fees 623.42 + slippage 318.87); gross pnl -1,036.30; cost coverage -1.10
- cash 4,005.18; positions: BTC 0.0260672, XRP 1592.49
- last run 2026-11-05 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 14:10Z SOL hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +1.15% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 14:10Z ADA hold target 0.11 (held 0.11) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +2.12% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 14:10Z AVAX hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +1.00% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 14:10Z LINK hold target 0.11 (held 0.11) — hold: weight change +0.002 below threshold 0.05 | stay long: 72h return +1.05% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 14:10Z XRP hold target 0.11 (held 0.11) — hold: weight change -0.001 below threshold 0.05 | stay long: 72h return +4.24% vs exit band -1.0% and price above 24h EMA; realised vol 5...
- 2026-11-05 14:10Z DOGE hold target 0.11 (held 0.11) — hold: weight change +0.000 below threshold 0.05 | stay long: 72h return +0.71% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.28% not above entry band +1.0% and price below 24h EMA
- 2026-11-05 14:10Z LTC hold target 0.11 (held 0.11) — hold: weight change +0.001 below threshold 0.05 | stay long: 72h return +0.29% vs exit band -1.0% and price within 2.0% of 24h EMA; reali...
- 2026-11-05 15:10Z BTC buy target 0.25 (held 0.11) — stay long: 72h return +0.60% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 41% -> weight 0.25
- 2026-11-05 15:10Z ETH sell target 0.00 (held 0.11) — exit: price more than 2.0% below 24h EMA
- 2026-11-05 15:10Z SOL sell target 0.00 (held 0.11) — exit: 72h return -1.40% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-11-05 15:10Z ADA sell target 0.00 (held 0.11) — exit: price more than 2.0% below 24h EMA
- 2026-11-05 15:10Z AVAX sell target 0.00 (held 0.11) — exit: price more than 2.0% below 24h EMA
- 2026-11-05 15:10Z LINK sell target 0.00 (held 0.11) — exit: 72h return -1.66% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-11-05 15:10Z XRP buy target 0.25 (held 0.11) — stay long: 72h return +2.31% vs exit band -1.0% and price within 2.0% of 24h EMA; realised vol 57% -> weight 0.25
- 2026-11-05 15:10Z DOGE sell target 0.00 (held 0.11) — exit: 72h return -1.17% fell below exit band -1.0% and price more than 2.0% below 24h EMA
- 2026-11-05 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: 72h return -0.67% not above entry band +1.0% and price below 24h EMA
- 2026-11-05 15:10Z LTC sell target 0.00 (held 0.11) — exit: 72h return -1.33% fell below exit band -1.0% and price more than 2.0% below 24h EMA

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 36 fills (16 buy / 20 sell), traded 45,961, gross pnl -172.72, -75 bps per round trip, avg half spread 2.2 bps
- AVAX: 52 fills (24 buy / 28 sell), traded 85,193, gross pnl +92.15, +22 bps per round trip, avg half spread 1.5 bps
- BTC: 42 fills (24 buy / 18 sell), traded 58,203, gross pnl -126.11, -43 bps per round trip, avg half spread 0.1 bps, open 0.0260672
- DOGE: 39 fills (19 buy / 20 sell), traded 49,043, gross pnl -313.08, -128 bps per round trip, avg half spread 1.0 bps
- DOT: 47 fills (22 buy / 25 sell), traded 69,133, gross pnl -174.48, -50 bps per round trip, avg half spread 2.3 bps
- ETH: 44 fills (21 buy / 23 sell), traded 58,174, gross pnl -136.29, -47 bps per round trip, avg half spread 0.2 bps
- LINK: 49 fills (25 buy / 24 sell), traded 81,140, gross pnl -448.58, -111 bps per round trip, avg half spread 2.1 bps
- LTC: 45 fills (21 buy / 24 sell), traded 60,527, gross pnl +373.93, +124 bps per round trip, avg half spread 1.6 bps
- SOL: 40 fills (21 buy / 19 sell), traded 60,786, gross pnl -147.60, -49 bps per round trip, avg half spread 0.5 bps
- XRP: 42 fills (21 buy / 21 sell), traded 55,264, gross pnl +16.50, +6 bps per round trip, avg half spread 0.4 bps, open 1592.49

last fills:

- 2026-11-05 15:10Z sell SOL 892 @ 91.0345 fee 0.89 slip 0.45 (half spread 1.1 bps)
- 2026-11-05 15:10Z sell ADA 885 @ 0.185668 fee 0.89 slip 0.54 (half spread 4.1 bps)
- 2026-11-05 15:10Z sell AVAX 889 @ 8.37432 fee 0.89 slip 0.66 (half spread 5.4 bps)
- 2026-11-05 15:10Z sell LINK 875 @ 10.9274 fee 0.87 slip 0.75 (half spread 6.6 bps)
- 2026-11-05 15:10Z sell DOGE 891 @ 0.0728598 fee 0.89 slip 0.45 (half spread 2.8 bps)
- 2026-11-05 15:10Z sell LTC 889 @ 53.1884 fee 0.89 slip 0.44 (half spread 2.8 bps)
- 2026-11-05 15:10Z buy BTC 1,100 @ 77074.5 fee 1.10 slip 0.55 (half spread 0.0 bps)
- 2026-11-05 15:10Z buy XRP 1,100 @ 1.26162 fee 1.10 slip 0.55 (half spread 2.3 bps)

## challenger1: mean_reversion (H1)

params: {"entry_z": 2.0, "exit_z": 0.5, "max_weight": 0.25, "target_vol_annual": 0.3, "vol_lookback_hours": 168, "window_hours": 240}

- equity 9,558.75 (started 10,000 at 2026-09-16 03:55Z), net -4.41% since start
- 24h +0.00%, 7d +0.09%, 30d -8.07%, max drawdown -15.05%
- fills 136 total, 31 in the last 7d
- costs 261.24 (fees 172.15 + slippage 89.09); gross pnl -180.02; cost coverage -0.69
- cash 9,558.75; positions: none
- last run 2026-11-05 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.42 not below -2.0
- 2026-11-05 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.20 not below -2.0
- 2026-11-05 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.13 not below -2.0
- 2026-11-05 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.19 not below -2.0
- 2026-11-05 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.95 not below -2.0
- 2026-11-05 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.29 not below -2.0
- 2026-11-05 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.84 not below -2.0
- 2026-11-05 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.50 not below -2.0
- 2026-11-05 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.35 not below -2.0
- 2026-11-05 15:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.75 not below -2.0
- 2026-11-05 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.12 not below -2.0
- 2026-11-05 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.00 not below -2.0
- 2026-11-05 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.61 not below -2.0
- 2026-11-05 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -0.90 not below -2.0
- 2026-11-05 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z +0.09 not below -2.0
- 2026-11-05 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.26 not below -2.0
- 2026-11-05 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.16 not below -2.0
- 2026-11-05 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: z -1.37 not below -2.0

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

## challenger2: cash (cash)

params: {}

- equity 10,000.00 (started 10,000 at 2026-11-05 15:25Z), net +0.00% since start
- 24h n/a, 7d n/a, 30d n/a, max drawdown 0.00%
- fills 0 total, 0 in the last 7d
- costs 0.00 (fees 0.00 + slippage 0.00); gross pnl 0.00; cost coverage n/a
- cash 10,000.00; positions: none
- last run 2026-11-05 15:25Z; halted today: False

last decisions (newest last):

- 2026-11-05 15:25Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing
- 2026-11-05 15:25Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | cash: holds nothing

## challenger3: swing_reversal (H5)

params: {"exit_hours": 48, "fresh_cross": true, "max_weight": 0.25, "min_higher_low": 0.1, "recent_hours": 240, "target_vol_annual": 0.3, "vol_lookback_hours": 168}

- equity 9,883.62 (started 10,000 at 2026-10-05 05:28Z), net -1.16% since start
- 24h +0.00%, 7d +0.00%, 30d -1.23%, max drawdown -1.89%
- fills 26 total, 0 in the last 7d
- costs 59.13 (fees 39.38 + slippage 19.75); gross pnl -57.25; cost coverage -0.97
- cash 9,883.62; positions: none
- last run 2026-11-05 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-05 14:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2015 (need +10.0%)
- 2026-11-05 14:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-05 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-05 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-05 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-05 14:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.005 (need +10.0%)
- 2026-11-05 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)
- 2026-11-05 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 7.604e+04 not a higher low vs prior low 7.948e+04 (need +10.0%)
- 2026-11-05 15:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 2191 not a higher low vs prior low 2299 (need +10.0%)
- 2026-11-05 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 90.75 not a higher low vs prior low 99.66 (need +10.0%)
- 2026-11-05 15:10Z ADA hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.1849 not a higher low vs prior low 0.2015 (need +10.0%)
- 2026-11-05 15:10Z AVAX hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 8.186 not a higher low vs prior low 8.773 (need +10.0%)
- 2026-11-05 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 10.49 not a higher low vs prior low 11.3 (need +10.0%)
- 2026-11-05 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 1.207 not a higher low vs prior low 1.259 (need +10.0%)
- 2026-11-05 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.07307 not a higher low vs prior low 0.07566 (need +10.0%)
- 2026-11-05 15:10Z DOT hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 0.8971 not a higher low vs prior low 1.005 (need +10.0%)
- 2026-11-05 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: low 52.57 not a higher low vs prior low 55.7 (need +10.0%)

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

- equity 9,409.40 (started 10,000 at 2026-10-13 17:26Z), net -5.91% since start
- 24h -4.47%, 7d -3.34%, 30d -5.91%, max drawdown -12.71%
- fills 30 total, 12 in the last 7d
- costs 62.94 (fees 40.22 + slippage 22.72); gross pnl -527.66; cost coverage -8.38
- cash 2,517.83; positions: ADA 12106.8, AVAX 276.724, DOT 2516.14
- last run 2026-11-05 15:10Z; halted today: False

last decisions (newest last):

- 2026-11-05 14:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.61 not below -2.0
- 2026-11-05 14:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.006 below threshold 0.05 | stay long: ratio to BTC z -1.25 vs 720h mean (entry -2.0, exit -0.25); vol 71% -> weigh...
- 2026-11-05 14:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.000 below threshold 0.05 | stay long: ratio to BTC z -1.08 vs 720h mean (entry -2.0, exit -0.25); vol 74% -> weigh...
- 2026-11-05 14:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -0.93 not below -2.0
- 2026-11-05 14:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.22 not below -2.0
- 2026-11-05 14:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.12 not below -2.0
- 2026-11-05 14:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.005 below threshold 0.05 | stay long: ratio to BTC z -1.66 vs 720h mean (entry -2.0, exit -0.25); vol 87% -> weigh...
- 2026-11-05 14:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.37 not below -2.0
- 2026-11-05 15:10Z BTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: BTC is the yardstick and is not held
- 2026-11-05 15:10Z ETH hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.56 not below -2.0
- 2026-11-05 15:10Z SOL hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.80 not below -2.0
- 2026-11-05 15:10Z ADA hold target 0.25 (held 0.24) — hold: weight change +0.011 below threshold 0.05 | stay long: ratio to BTC z -1.37 vs 720h mean (entry -2.0, exit -0.25); vol 73% -> weigh...
- 2026-11-05 15:10Z AVAX hold target 0.25 (held 0.25) — hold: weight change +0.004 below threshold 0.05 | stay long: ratio to BTC z -1.08 vs 720h mean (entry -2.0, exit -0.25); vol 75% -> weigh...
- 2026-11-05 15:10Z LINK hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.15 not below -2.0
- 2026-11-05 15:10Z XRP hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z +0.11 not below -2.0
- 2026-11-05 15:10Z DOGE hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.28 not below -2.0
- 2026-11-05 15:10Z DOT hold target 0.25 (held 0.25) — hold: weight change +0.003 below threshold 0.05 | stay long: ratio to BTC z -1.54 vs 720h mean (entry -2.0, exit -0.25); vol 87% -> weigh...
- 2026-11-05 15:10Z LTC hold target 0.00 (held 0.00) — hold: weight change +0.000 below threshold 0.05 | flat: ratio to BTC z -1.47 not below -2.0

by pair (gross pnl at last mark, bps per round trip = gross / half of traded notional):

- ADA: 4 fills (3 buy / 1 sell), traded 5,091, gross pnl -196.82, -773 bps per round trip, avg half spread 3.3 bps, open 12106.8
- AVAX: 4 fills (3 buy / 1 sell), traded 5,003, gross pnl -77.05, -308 bps per round trip, avg half spread 3.5 bps, open 276.724
- DOGE: 3 fills (1 buy / 2 sell), traded 4,846, gross pnl -151.45, -625 bps per round trip, avg half spread 1.4 bps
- DOT: 5 fills (3 buy / 2 sell), traded 5,904, gross pnl +3.54, +12 bps per round trip, avg half spread 3.9 bps, open 2516.14
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

- BTC: live 1932 candles, 2026-08-17 03:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.0 bps
- ETH: live 1932 candles, 2026-08-17 03:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42610 candles from 2021-10-06; avg half spread last 7d 0.1 bps
- SOL: live 1932 candles, 2026-08-17 03:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 0.6 bps
- ADA: live 1932 candles, 2026-08-17 03:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 2.0 bps
- AVAX: live 1932 candles, 2026-08-17 03:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42609 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- LINK: live 1932 candles, 2026-08-17 03:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42608 candles from 2021-10-06; avg half spread last 7d 1.8 bps
- XRP: live 1904 candles, 2026-08-18 07:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 27145 candles from 2023-07-13; avg half spread last 7d 0.2 bps
- DOGE: live 1904 candles, 2026-08-18 07:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 0.5 bps
- DOT: live 1904 candles, 2026-08-18 07:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.5 bps
- LTC: live 1904 candles, 2026-08-18 07:00Z to 2026-11-05 14:00Z, missing hours in last 7d: 0; history 42636 candles from 2021-10-06; avg half spread last 7d 1.6 bps
