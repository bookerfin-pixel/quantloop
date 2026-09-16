You are running as the daily research agent for quantloop. CLAUDE.md is loaded; follow its daily procedure exactly.

Today's run, in order:

1. Read state/summary.md, LEDGER.md, hypotheses/backlog.md and the newest file in notes/. Run `gh pr list --state closed --limit 5` and, for any PR closed in the last few days by the gate, `gh pr view <n> --comments` to read why.
2. Determine whether the challenger slot is idle or testing (it is stated at the top of state/summary.md; `python -m bot.slot` confirms it).
3. If testing: do the review described in CLAUDE.md, write notes/<today>.md, update hypotheses/backlog.md if you have a real idea, and commit. Do not change configs/challenger.yaml or bot/strategy.py unless you found a bug that does not confound the running test.
4. If idle: write one ledger entry, make the one change, add tests if you added strategy code, run `python -m pytest tests -q` and `python -m bot.backtest --config configs/challenger.yaml`, put the metrics in the ledger entry, remove the idea from the backlog, and commit with first line `H<n>: <title>`.
5. Before committing, run `git diff --name-only origin/main` and confirm nothing listed in PROTECTED.txt appears. If it does, revert that file with `git checkout origin/main -- <path>`.
6. Commit with `git add -A && git commit -m "<message>"`. Do not push; the workflow pushes and opens the PR. If you made no changes at all, say so in one line and stop.

Finish with a short plain English summary of what you did and why.
