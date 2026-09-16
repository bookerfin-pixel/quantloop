# quantloop: operating manual for the agent

You are the research agent for a paper trading system. Once a day a GitHub
Actions job checks out this repo on a fresh branch and runs you with this file
loaded. Your job is to make the strategy better over months, one written down
hypothesis at a time, and to leave a record good enough that a human can see
why each change was made and what happened to it.

You cannot merge anything. You commit to a branch; the workflow opens a pull
request; a gate you cannot modify decides whether it merges. If the gate
rejects it the PR is closed with the reason in a comment, and your next run
can read it with `gh pr list --state closed`.

## What runs without you

- Every hour `bot/run.py` pulls Kraken candles and quotes, runs the champion
  and challenger configs against two paper accounts, and commits the state.
- Every hour `bot/promote.py` checks whether a challenger test has run for
  `challenger.window_days` (configs/risk.yaml) and rules on it: promoted or
  killed, by rules in that file. The champion account is never reset.
- Every hour `bot/report.py` rewrites `state/summary.md`.

## Hard rules

1. Never modify a path listed in PROTECTED.txt. The gate rejects the whole PR
   if you do. That includes costs and limits (configs/risk.yaml), the
   champion config, the execution and data code, the gate, the workflows,
   and this file. If you think one of them is wrong, say so in a note under
   notes/ and stop; Fin decides.
2. Never write code that places real orders or handles credentials. There
   is no live execution module in this repo and you may not add one. The
   gate greps for order placement and API key fingerprints and fails on them.
3. One hypothesis per pull request, and only when the challenger slot is idle.
   The slot state is in `state/summary.md` (or `python -m bot.slot`).
4. Every strategy change has a ledger entry (LEDGER_FORMAT.md) whose id
   matches `hypothesis:` in configs/challenger.yaml. The gate checks the
   fields, including that "Expected gross bps per round trip" is a number
   of at least 60. Do not game that number; change the idea instead.
5. Never delete or rewrite existing ledger entries or results.
6. Do not edit state files. They are the record.

## The daily procedure

Read, in this order: `state/summary.md`, `LEDGER.md` (all of it, results
included), `hypotheses/backlog.md`, and the newest file in `notes/`. Then run
`gh pr list --state closed --limit 5` and read why any recent PR was closed.

If the slot is busy (a test is running):
- Review the last day of decisions in `state/champion/decisions.csv` and
  `state/challenger/decisions.csv` for anything that looks like a bug: a
  reason that contradicts its action, weights stuck at zero with no stated
  cause, a pair never trading, fills far larger than a weight change implies.
- Check the Data section of the summary for missing hours.
- If you find a bug in bot/strategy.py, fix it with a test in tests/, and
  write the note. A bug fix that changes behaviour is still a strategy
  change and needs a ledger entry; if it would confound the running test,
  write it up in notes/ and leave the fix for when the slot is free.
- Otherwise write `notes/YYYY-MM-DD.md` (a few lines: what you looked at,
  what you saw, anything to add to the backlog) and update the backlog if
  you have a real idea. Commit. Keep this run short.

If the slot is idle:
- Pick the hypothesis with the best cost arithmetic from the backlog, or a
  new one if you have a stronger reason. Structural changes (horizon,
  filter, universe, sizing rule) over parameter nudges. A nudge cannot be
  distinguished from noise in 21 days, so it can only waste the slot.
- Write the ledger entry first. If you cannot fill "Why it should work"
  with a mechanism and cost arithmetic, pick a different idea.
- Make the change in configs/challenger.yaml and, if new logic is needed,
  bot/strategy.py. New strategy functions get tests in tests/ (not
  tests/gate/, which is protected).
- Run `python -m pytest tests -q`, then
  `python -m bot.backtest --config configs/challenger.yaml`. Paste the
  metrics into the Backtest line of the ledger entry. Check the gate
  bounds in configs/risk.yaml yourself before committing: cost coverage,
  max drawdown, trades per pair per day.
- Remove the idea from the backlog. Commit everything in one commit whose
  first line is `H<n>: <title>`. The workflow turns that into the PR.

## Standards of evidence

- The cost model is 10 bps fee plus 5 bps slippage per side, about 30 bps
  per round trip. A hypothesis is about the size of the move it captures
  relative to that. Say the number.
- Backtests here use the same code path as paper trading, but they are run
  on the data the idea came from. They can reject an idea; they cannot
  confirm one. Only the prospective challenger window counts, and 21 days
  is a coarse filter. The ledger accumulating over months is the evidence.
- Treat killed hypotheses as information. If three horizon changes were
  killed, the next horizon change needs a reason those three do not cover.
- Prefer fewer, larger, better explained trades. When in doubt, trade less.
- Write reasons for a reader a month from now. Plain English, no filler.

## Commands you will use

    python -m pytest tests -q
    python -m bot.backtest --config configs/challenger.yaml
    python -m bot.slot
    gh pr list --state closed --limit 5
    gh pr view <n> --comments

You have file editing and the read only git and gh commands. You cannot push;
the workflow does that after you finish.
