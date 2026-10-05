# state

Written by the hourly workflow. Do not edit by hand and never in a PR.

Each account's files are kept in step. account.json counts every fill the
account has made (`n_trades`) and every reading it has taken
(`equity_rows`, kept from an account's first run under ruleset 7).
trades.csv has one row for each fill, and every row is a fill. equity.csv
has one row for each reading, from the account's first run to its last, in
time order. Every hour bot/promote.py sets the files against those counts,
and rules on nothing for an account whose files have lost rows, hold a row
that is not a fill, or cannot be read; the summary says which file until it
is mended (PROMOTION.md, the small print). bot/paper.py does not rewrite or
add to a file whose first line is not a header it wrote: the hourly run
stops instead, as it does for an account.json that cannot be read.

    champion/       account.json, decisions.csv, trades.csv, equity.csv, and
                    changes.json: every change of the champion's config (when,
                    from, to, promotion or revert, the new config's usual exposure)
    challenger<k>/  the same four files, plus meta.json (slot status, test start,
                    ruleset, first look, usual exposures)
    shadow/         the deposed champion's account while a promotion is guarded
    candles/        one CSV per pair, hourly, grows every run
    history/        about five years of hourly candles per pair, fetched once
    archive/        challenger accounts from finished tests, one folder per hypothesis
    summary.md      what the agent reads first each day
