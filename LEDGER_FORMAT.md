# Ledger entry format

PROTECTED. gate/check_ledger.py enforces this. Copy the block, fill every
line, keep the field names exactly. What a field says starts on the field's
own line or on the line straight under it, and may run over several lines
(figures one to a line, indented or as a list); a blank line or the next
field ends it.

```
## H<n>: <short title>
- Date: YYYY-MM-DD
- Hypothesis: one or two sentences stating a mechanism in the market, not a parameter value. "Trends that survive a pullback continue" is a hypothesis. "lookback 96 instead of 72" is not.
- Change: exactly what changed in configs/challenger<k>.yaml and/or bot/strategy.py.
- Why it should work: the reason, in plain English, with the cost arithmetic. Say what size of move the signal is chasing and how that compares to the ~30 bps round trip.
- Expected gross bps per round trip: <number first>, then how you got it. Below 60 the gate rejects the entry, because 30 bps of cost leaves no room for being wrong.
- Kill criteria: what result in the prospective window would prove the hypothesis wrong. promote.py applies the standard rule regardless; this line is for the next reader to judge whether the standard rule was even the right question.
- Differs from running tests: one line on what this test will tell us that the tests in the other slots will not (omit when the other slots are idle).
- Backtest: the metrics from `python -m bot.backtest --config configs/challenger<k>.yaml --gate`: total return, max drawdown, n_trades, finished_trades, closed_by_halt_or_error, windows_with_no_finished_trade, cost drag per year, and the skill line (net return against the exposure matched basket, with the quarter by quarter figures). Backtests here are sanity, not evidence; a negative skill figure does not fail the gate, but say what you make of it.
- Bench: the last line of `python -m bot.bench --config configs/challenger<k>.yaml --quick`, the one that begins `Bench:`, as printed, then what you make of it. It is in sample like the backtest: it can show that an idea has nothing, never that it has something. If the reading could not be taken, begin this line `not taken:` and say why in a few words (`not taken: it ran out of its 30 minutes`); the gate takes the bench's own line or that, and nothing else.
- Status: testing
```

`<n>` is one more than the highest existing H number. `hypothesis: H<n>` in
the slot config you changed (configs/challenger<k>.yaml) must match, and a
pull request changes one slot only.

Verdicts are appended by bot/promote.py under `## Results` and the Status
line is flipped to `promoted`, `killed` (it finished no trade of its own, or
it did not pass and its trades were not of value, or an early kill ended
it; the Rule line says which), or `unproven` (kept to day 120 and short of
a promotion; see PROMOTION.md), or to `voided` when Fin ended the test
because its code or data was broken (not a verdict on the idea). A `###
First look H<n>: passed` or `kept on value` block at day 60 is not a
verdict; the Status stays `testing`. A `superseded` block says a
promotion's guard ended early because another promotion followed it. Do not
edit those by hand.
