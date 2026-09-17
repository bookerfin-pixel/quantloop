# Ledger

Every hypothesis this system has tested, with its verdict. The agent adds a
`## H<n>` entry before a test starts (format in LEDGER_FORMAT.md) and
bot/promote.py appends the verdict under `## Results`. Nothing is deleted. A
killed idea is evidence, and the next agent run reads it before proposing.

## Prior evidence

Not tests run here, but the reasons this system is shaped the way it is. They
come from Fin's first bot (2025, real money, Binance spot, seven pairs).

### P1: short horizon mean reversion could not pay Binance fees
- It was built for 20 to 22 bps moves. Realised gross edge on short horizon
  mean reversion came in at single digit bps per trade against roughly 22 bps
  of round trip cost. The direction was often right; the size of the move was
  not. Costs killed it, not the signal.
- Carried here as: the cost coverage gate, the trades per day cap, and the
  "Expected gross bps per round trip" line every hypothesis must fill in.

### P2: machinery built before validation starved itself
- Kelly sizing needed 40+ closed trades, the transaction cost model needed
  fill samples, the ML model needed 500+ labelled observations. The risk gates
  skipped nearly every candidate trade, so none of that ever calibrated.
- Carried here as: a small bot, one change at a time, a minimum fill count
  before any verdict, and no component that needs data the system is not
  yet producing.

## H0: baseline, slow time series momentum, long or flat
- Date: 2026-09-16
- Hypothesis: a 72 hour momentum signal with an EMA filter and entry/exit bands on six majors catches multi day trends often enough that a 30 bps round trip is small next to the average move captured.
- Change: seed configuration (configs/champion.yaml), strategy `ts_momentum`.
- Why it should work: trend persistence over days is the most replicated effect in crypto returns, and the bands hold turnover near 0.3 fills per pair per day so the strategy is not on a costs treadmill.
- Expected gross bps per round trip: 150
- Kill criteria: none. This is the champion; it is only replaced by a challenger that beats it in a prospective test.
- Backtest: first 23 days of real Kraken data (2026-08-24 to 2026-09-16, a choppy, falling window): total return -6.1%, max drawdown -10.8%, 110 fills (0.80 per pair per day, max 5 in one pair in one day), gross pnl -300, costs 311, cost coverage -0.96. On this window the baseline would fail its own gate on churn and cost coverage. It is the floor the first challenger has to beat, not evidence of edge.
- Status: champion

## H1: mean reversion at ten times the horizon P1 killed
- Date: 2026-09-16
- Hypothesis: after a genuine multi-day capitulation (price 2 standard deviations below its own trailing 10 day mean), crypto majors and large alts revert back toward that mean more often than they continue falling, because the move being faded is a dislocation building up over days, not hourly noise a short horizon version would be chasing.
- Change: configs/challenger.yaml switches the challenger to the existing `mean_reversion` strategy (bot/strategy.py unchanged) with window_hours: 240 (10 days), entry_z: 2.0, exit_z: 0.5, vol_lookback_hours: 168, target_vol_annual: 0.30, max_weight: 0.25, on all six pairs. The backlog's version of this idea restricted it to BTC and ETH only; I dropped that restriction because at a 2.0-2.5 sigma, 240 hour trigger those two pairs alone produced only 3 fills in a 20 day backtest, nowhere near the 20-fill minimum challenger.window_days needs to reach a verdict. All six pairs together produced 22.
- Why it should work: P1's short horizon mean reversion was chasing single digit bps moves against ~22 bps of Binance cost — the direction was often right, the size was not. At a 240 hour window the same z-score gap is a much bigger price move: BTC and ETH's own trailing 10 day dispersion (std/mean) has run about 1.5% recently, SOL and AVAX 2-3%, ADA and LINK 4-4.5%. The 1.5 sigma gap between entry (z -2.0) and exit (z -0.5) times that dispersion is the expected price move back toward the mean, so even the calmest pairs are chasing several times the round trip cost.
- Expected gross bps per round trip: 225, from (entry_z - exit_z) x BTC/ETH's own trailing 10 day std/mean (~1.5%) = 1.5 x 1.5% = 225 bps. That is the conservative end: the four noisier pairs imply 300-675 bps by the same arithmetic.
- Kill criteria: the standard rule (net return does not beat champion, or drawdown exceeds 1.5x champion's) killing this would mean the P1 problem — a small real edge relative to cost — survives even at ten times the horizon. A verdict of "killed: too few fills" would mean something different: not that the mechanism is wrong, but that a >=2 sigma event on a 240h window across six pairs is too rare to clear min_trades in 21 days, which is a statement about the test design, not the hypothesis; if that happens, the next attempt at this family should lower entry_z rather than repeat this one.
- Backtest: last ~20 days of real Kraken data (2026-08-27 to 2026-09-16, the same choppy, falling window H0 was tested on): total return +3.9%, max drawdown -2.8%, 22 fills (0.18 per pair per day, max 2 in one pair in one day), gross pnl 458.8, costs 69.69, cost coverage 6.58. This is the window where H0's long-only trend following lost money (cost coverage -0.96); a bounce buyer doing well here is partly because the window was falling, so treat this as a plausibility pass, not evidence — the prospective window is the real test. Two momentum-family variants tried against this same data first, a realised-vol regime filter and a widened-band 168h version of ts_momentum, both made cost coverage worse than H0, not better (-6.88 and -4.75); neither is proposed here for that reason.
- Status: testing
- Note (2026-09-17, Fin): universe widened from 6 to 10 pairs (XRP, DOGE, DOT, LTC added) and the test window extended from 21 to 60 days while this test was on day 1. Both apply to the champion and the challenger alike, so the paired comparison stays fair, but the entry above was written for six pairs and a 21 day window. Verdict now due around 2026-11-15.
