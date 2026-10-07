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
    wide/           research data, written once a day by its own job (bot/wide.py,
                    .github/workflows/wide.yml) and read by no account and by nothing
                    in the hourly loop. See below
    bench/          what each config in use shows on all the history on file, set
                    against its own twins: <hypothesis>.json, one reading each, and
                    README.md, the league table with every reading in words, the day
                    each was read on, and a line for any config that could not be
                    read. Written by its own job (bot/bench.py,
                    .github/workflows/bench.yml) when a proposal merges and once a
                    day besides, for readings that are missing, a week old, or taken
                    before the config or the code it runs last changed. Nothing in
                    the hourly loop reads it, no strategy may, and no rule leans on
                    it. All of it is in sample

## wide/

Daily data on the coins beyond the ten the bot trades, to find out on real
data whether there is anything in them before any machinery is built for it.
`python -m bot.wide` says what the last run did. A line about something
that went wrong begins with FAILED, one about a last run more than 30 hours
old (or no run at all) with STALE, and one about a slip in configs/wide.yaml
with SETTING NOT USED.

    universe.json        the list: every coin that has been among the most traded USD
                         pairs on Kraken on a day the collector's run went through
                         (the top `top_n`, 100 as shipped, of those that traded at
                         least `min_usd_volume` and are not a dollar token), with the
                         UTC day it joined (`since`) and the moment (`joined_at`). A
                         coin that has joined stays on the list for good. When Kraken
                         stops listing its dollar pair, or Fin adds it to `exclude`,
                         it is marked (`listed` false, `unlisted_since`) and its
                         candles end there; its file is kept. If the name comes back
                         it is taken for the same coin and its candles go on; `gaps`
                         keeps each stretch it was away ([from, back]), because a
                         name that returns is not always the coin that left. Money,
                         dollar and gold tokens and wrapped copies are left out
                         (configs/wide.yaml)
    daily/<COIN>.csv     one row per closed UTC day the venue has a candle for: time
                         (the day's first second), open, high, low, close, vwap,
                         volume (in coins), count (trades), source. Days can be
                         missing: Coinbase leaves out a day with no trade, and a
                         stretch longer than 720 days in which the collector did not
                         run leaves a hole nothing fills (`wide.panel()` shows a
                         missing day as no value). Kraken serves its newest 720
                         days; older rows are Coinbase's (`source` says which), taken
                         only when the two venues' closes agree on the days both have. In a
                         Coinbase row vwap is the mean of the high, the low and the
                         close, and count is 0: Coinbase gives neither. On a day with
                         no trade Kraken's vwap is 0
    quotes/<YEAR>.csv    one reading a day per coin: best bid and ask, last price, 24
                         hour volume in coins and in dollars, the 24 hour vwap and
                         trade count, half the spread in bps, and the coin's rank by
                         dollars traded that day
    funding/<SYMBOL>.csv Kraken's perpetual futures, one row per UTC day: hours (how
                         many hourly readings the day has; a reading counts in the
                         day its time stamp falls in), relative_sum (the share of a
                         position's value a long paid a short that day; negative when
                         the short paid) and absolute_sum (the same in dollars per
                         contract). Research only: the bot cannot hold a future
    deepen.json          which coins Coinbase was asked about for older history, and
                         what came of it. A coin it does not list, or has no candles
                         for, is asked about once more by the next day's run, and
                         then not again for three months
    status.json          the last run: counts, the pairs that failed and why, the
                         listed coins Kraken gave no bid and ask for, the settings not
                         used at the time, and whether GitHub's runners could read
                         Binance's public market data that day

Two things to know before believing a study on it. First, the list begins
the day the collector first ran. Candles from before a coin's `since` date
are the past of a coin that was alive and busy on that date, so anything
measured over those years is measured on the survivors and flatters buying
and holding them. The day of `since` itself began before the coin joined.
From the day after `since` a coin is on the list whatever becomes of it, and
that is where a study with no hindsight starts. Second, a quote is one
reading a day, taken about 00:40 UTC (12:40 when the first run of the day
was dropped; `time` says when); spreads at other hours can be wider.
