# How a strategy earns its place, and what it would take to risk money

PROTECTED. Fin decided these rules on 2026-10-05 from a draft and a study of
how often candidate rules promote a strategy with no skill. bot/promote.py
applies rule 1. Rule 2 is applied by Fin, by hand. The agent cannot change
either.

A test can end three ways, and they are three different things.

- **Killed.** It showed nothing worth keeping. A kill counts against the
  idea's family.
- **Unproven.** Its numbers passed, or its trades made money, and there is
  not enough to call it proven. It does not count against the family.
- **Promoted.** It becomes the paper champion.

## Words used here

- **Test.** A challenger strategy running in a slot with its own paper
  account, set against the champion over the same days, or against cash
  (ruleset 8: see "Cash as the champion").
- **Basket.** The ten pairs in equal parts, bought when the test begins and
  held. It stands for "the market".
- **Usual exposure.** The share of its equity a strategy had invested on
  average over the year before its test, worked out once from a replay.
- **Skill.** A strategy's net return minus what holding the basket at its
  usual exposure would have made. Holding more of a rising market than
  usual counts as skill; simply being a strategy that holds a lot does not.
- **t (daily skill t).** How far the average daily skill stands from zero,
  in units of its own day to day noise. Under about 2 it cannot be told
  from noise with any confidence; the 1.0 that rule 1 asks for is a low bar
  on purpose. It grows with the square root of time.
- **Daily edge t.** The same sum for the challenger's daily skill minus the
  champion's. It is printed for the reader; no rule uses it. It appears
  after 3 days, the daily skill t after 10, so early on only one shows.
- **Sharpe.** Skill per year divided by how much it bounces around in a
  year. 1 is good, 2 is excellent.
- **Drawdown, and the guard.** The deepest fall of an account from an
  earlier high inside the test. The guard: a challenger's may not be deeper
  than the larger of 10% and one and a half times the champion's (against
  cash, the equal weight basket's).
- **Fill.** One buy or one sell.
- **Finished trade.** A position the account has left: sold down to a
  twentieth of its largest size or less. "Of its own" means the strategy
  chose to leave it.
- **Ruleset.** A number in configs/risk.yaml that goes up whenever these
  rules change. Each test is stamped with the one it began under.

## Why the old rule was not enough

The rule until ruleset 7: after 60 days, promote a challenger whose skill is
above zero and above the champion's, with its drawdown inside the guard and
30 fills or more. A challenger that fell more than 15% under its own high
was ended early.

Twins tell how often that is luck. A twin is a strategy's hour by hour
positions, taken from a replay of a live config over 687 days, slid against
the market by a random 30 days or more: the same exposure and the same
turnover, with no timing skill left in it. A "real edge" is a twin whose
coins are made to do a little better in every hour it holds them, by enough
to give its skill the Sharpe named.

Share of tests ending in a promotion. Every twin is started on 81 dates,
a week apart. The first column is 900 twins (300 each of H1, H2 and H4,
against H0), so 72,900 tests; the others are 360 twins, 29,160 tests. The
basket fell by a third over these 687 days. Three runs with different
random slides agree to within a point and a half in every cell.

| Rule | Twin with no skill | Real edge, Sharpe 1 | Sharpe 2 | Sharpe 3 |
| --- | --- | --- | --- | --- |
| The old rule as it ran | 25% | 40% | 49% | 57% |
| The old rule with no early kill | 38% | 63% | 77% | 85% |
| Two passes in a row (days 1 to 60, then days 61 to 120) | 14% | 37% | 57% | 71% |
| Rule 1 with a day 120 bar of t 1.5, no fast pass | 3% | 15% | 37% | 60% |
| Rule 1 with a day 120 bar of t 2.0, no fast pass | 0.7% | 6% | 20% | 41% |
| **Rule 1 as built (below)** | **9%** | **31%** | **56%** | **77%** |
| of which promoted at day 60 by the fast pass | 0.9% | 5% | 12% | 23% |
| Rule 1 as built, had the early kill not changed | 6% | 17% | 31% | 44% |
| A twin judged the way H1, H2 and H4 are (one look at day 60) | 38% | 64% | 79% | 88% |

Read the first row with care: the old rule looks strict there only because
its early kill ended 55 of 100 twins and 40 of 100 Sharpe 2 edges before
day 60 (see "The early kills"). A real Sharpe 2 edge was only about twice as
likely to be promoted by it as a twin. Under rule 1 it is about six times as
likely.

No rule over 60 or 120 days separates an edge of ordinary size from luck. A
Sharpe 2 edge needs about a year to show a t of 2.

What the study does not model: the champion never changes in it; a twin's
usual exposure is its average over the whole replay; a finished trade is a
position sold out whole, which lets a few more tests through "has finished
a trade" than the live count would; and the cost kill is left out. None of
these was measured, so read the table for the size of its numbers and not
for their last digit.

## What gets a test killed, and what keeps it

Fin, 2026-10-05, in two parts. If a bot trades less but its trades are of
value, that is a usable skill; if not, kill. And riding a rise and taking
profit at the right time is the skill; a bot that just buys and holds while
the market goes up has shown nothing.

**A test that has finished no trade of its own is killed at its look,
whatever its numbers.** A trim is not an exit, and a position sold in pieces
counts once. A finished trade is the strategy's own when the strategy chose
it:

- A position the slot already held when the test began (before ruleset 8
  an idle slot ran the champion's config; from ruleset 8 it holds cash, so
  a new test begins from a flat book) is measured from its size at that
  moment, and leaving it counts from the second day on. In the first day
  that is the last config's book being unwound, unless the strategy bought
  more of it.
- A position the daily loss halt sold, or one sold because the strategy
  raised an error, was not an exit the strategy chose. It is counted apart.

So a bot that only bought, one that only trimmed, one that sold what it was
handed and then sat out, and one whose only exits were the halt's are all
killed at their look.

**A test that does not pass the rule is kept all the same when its trades
are of value.** That means all three of:

1. It has finished a trade of its own.
2. Its finished trades made money after costs: what their sells brought in,
   less what their buys cost, less the fees on both sides, is above zero.
   (Slippage is already in the fill prices. A position held when the test
   began is costed at its price then, so only what happened during the test
   counts. Positions the halt closed are in the sum: the money is real.)
3. Its drawdown is inside the guard.

Kept is not promoted. It buys 60 more days. At day 120 a kept test is
promoted only if the whole rule passes; otherwise it ends unproven, or
killed if by then its trades are no longer of value and it still does not
pass. An early kill can end it in between. Of 100 twins kept on value at
day 60, about 49 ended unproven, 21 were killed at day 120, 24 were ended
early before it and 6 were promoted (5 to 7 across the three runs).

This is a plain reading of the record, not proof of an edge, and it has
three limits a reader should know.

- A twin with no skill had finished trades in profit at day 60 in 36 of 100
  tests; a Sharpe 2 edge in 69. That was in a market that fell in two of
  every three windows. Where the basket rose over the 60 days, the figures
  were 64 and 92.
- Only finished trades are counted. A bot that takes its winners and sits
  on its losers has "trades of value" until the drawdown guard or an early
  kill catches the losers.
- A finished trade the record cannot put a figure on adds nothing to the
  sum, and if none of them has a figure the trades are not of value. This
  is a fallback: a record with a price or a row missing is a damaged record,
  and nothing is ruled on one (the small print).

**Fills.** Trading little does not kill a test by itself, but it has two
effects. A test with fewer than 30 fills cannot pass a look, so at day 60 it
is kept only if its trades are of value. A test that reaches day 120 passing
the rule's numbers without 30 fills ends unproven, not killed. (In the study
94 of 100 twin tests had their 30 fills by day 60, and fewer than 2 in 100
were killed at day 60 while passing every number but that one.)

An earlier build asked instead whether a test's "own decisions" had added
1% beyond holding its average exposure. On 60 days of a made up market with
nothing in it to time, that figure read +3.9% for a dip buyer with no skill
and -3.9% for a trend follower with no skill: it scored a style. It was
dropped before it ran (FINDINGS, 2026-10-05).

## Rule 1: becoming paper champion (two looks)

For every test that begins under ruleset 7 or later.

1. Day 60, first look.
   - No finished trade of its own: killed.
   - It passes the ordinary rule (skill above zero and above the champion's,
     drawdown inside the guard, 30 fills or more): "First look: passed". Not
     a promotion. 60 more days in the same slot.
   - The fast pass: a first look pass whose daily skill t is already 2.0 or
     more is promoted there and then. It is asked once, at the first look,
     never on the days after it. It is not given when half or more of the
     skill is a standing tilt (see the confidence figure).
   - It does not pass, and its trades are of value: "First look: kept on
     value". The same 60 more days.
   - Otherwise: killed.
2. Day 120, the verdict, on all 120 days:
   - killed: no finished trade of its own; or it does not pass the rule's
     numbers and its trades are not of value.
   - promoted: it passes the ordinary rule with 30 fills or more, and the t
     of the daily skill is 1.0 or more.
   - unproven: it passes the rule's numbers without the 30 fills or the t;
     or it does not pass and its trades are of value. The slot is freed the
     same hour a kill would free it, so nothing lingers.
3. The early kills apply in every hour of the 120 days (next section).
4. The shadow guard is unchanged: after a promotion the old champion runs on
   for 60 days and takes its place back if it beats the new one by the
   ordinary rule (better on skill, drawdown inside the guard, 30 fills).
   After a promotion judged against cash, cash is what guards it, and a
   revert asks for a clear fall below it (next section).

Of 100 twins, about 21 are ended early before day 60, 32 are killed at day
60, 1 is promoted there by the fast pass and 47 run on (each rounded, so
they add to 101). Of those 47, about
5 are ended early, 11 are killed at day 120, 23 end unproven and 8 are
promoted. A Sharpe 2 edge is still running after day 60 in 71 of 100 and
promoted in 56. A twin's test takes 80 days on average, so four slots give
about 18 verdicts a year. The old rule gave about 34, of which 55 in 100
were early kills, 20 were kills at day 60 and 25 were promotions.

Why t of 1.0 and not higher: being paper champion costs nothing, and the
shadow guard stands behind it. A wrong kill is the expensive mistake, because
the agent reads a kill as evidence against a whole family of ideas. The
strict bar is in rule 2.

Why a fast pass at 2.0: Fin asked for a faster proof next to the slow one,
and this is the one the numbers allow on this book. A twin with no skill is
promoted by it 9 times in 1,000; a Sharpe 2 edge 12 times in 100 and a
Sharpe 3 edge 23. So a Sharpe 2 edge is about 14 times as likely as a twin
to get a fast pass, against about 6 times for a promotion under the whole
rule. It is rare by design. What makes proof faster for an ordinary edge is
not a lower bar but more independent bets a day, which is what a wider
universe is for.

Tests that were running when this rule arrived keep their one look at day
60: H1, H2 and H4, and H5, which began a few hours before it. If they pass
the ordinary rule there and have finished a trade of their own, they are
promoted there, as before. Everything else is the same for them: killed
with no trade of their own, kept for a day 120 verdict when their trades
are of value. Their results also say what rule 1 makes of the same numbers.
The table's last row is the price of that one look: 38 of 100 twins with no
skill would be promoted by it, more than the 25 the old rule promoted as it
ran, because the fairer early kill lets more of them reach day 60. That row
is twins of the H1, H2 and H4 configs, not a forecast for the tests. The
replayed configs make about 140, 80 and 80 fills in 60 days. The live H2
had made 2 in its first 14 days and H4 10, all in its first hour, and H5's
own backtest makes about 7 in 60 days, so none of those three is near the
30 fills its one look asks for.

What this does not catch: a bot that trades a little and otherwise holds
more of a rising market than it usually does. Its skill figure is real money
and one bet. The two looks, the t bar and the shadow guard are the defence,
and the table says how often a strategy with no skill gets through them.

## Cash as the champion (ruleset 8)

Fin, 2026-10-08: H0 is retired, and the champion's title is cash. A strategy
earns it by beating holding nothing, not by beating a config that loses.

- **What a test is judged against.** A test that begins while the
  champion's config is retired (`retired_champions` in configs/risk.yaml:
  H0) or is cash is judged against cash, and its slot record says so
  (`against: cash`). Cash makes nothing, pays nothing and holds nothing: its
  return is nothing, and so is its skill. Everything else in rule 1 is as
  above: the two looks, the fast pass, the 30 fills, the t bar, the early
  kills, the value of its trades. A test that begins while a config holds
  the title is judged against the champion account, as before ruleset 8
  (`against: champion`).
- **When a config takes the title inside a test's window**, a test judged
  against cash carries on in the same window, as a test always has across a
  change of champion. Its other side is then the title's record: cash while
  the title is cash (or a retired config stands in for it), and the champion
  account's own record while a config holds it, each stretch's skill
  measured against the usual exposure of the config that held the title
  (the account's own average over the stretch when none is on record). A
  reading counts with the config that was champion when it was taken: the
  first one after a change, which still carries the old book's last hour
  and pays for the switch, is the new config's, and the hour of a change
  reads as nothing made. Its results say so in a "Champion change" line.
- **The drawdown guard of every test that begins under ruleset 8** is set
  against the equal weight basket's worst fall over the same window: no
  deeper than the larger of 10% and one and a half times it, whatever the
  test is judged against. Cash never falls, and against its fall the guard
  would be the 10% floor alone. A champion config's own fall depends on how
  much of the market it holds. Tests that began earlier keep the champion's
  fall, as they began.
- **Why the numbers do not move.** min_skill is 0, and H0's skill was below
  nothing in about 97 of 100 60 day windows, so "above the champion's skill"
  added nothing to "above nothing". The one thing H0 set was the drawdown
  guard, and its falls were so deep that the guard almost never bit; against
  the basket it is a backstop for a strategy that falls far more than the
  market, not a check on ordinary ones. The twin study of rule 1, run again
  (seeds 11 and 12, 2026-10-08 to 10; the market fell by a third over the 687
  days, which leaves both the H0 bar and the guard slack), share of tests
  promoted:

  | Other side, and the guard's yardstick | Twin with no skill | Sharpe 1 | Sharpe 2 | Sharpe 3 | Twins inside the guard at day 60 |
  | --- | --- | --- | --- | --- | --- |
  | H0, H0's fall (rule 1 as it ran) | 9.0% / 8.5% | 31.2% / 31.4% | 56.1% / 55.4% | 76.9% / 76.4% | 99.4% |
  | Cash, cash's fall (the 10% floor) | 2.4% | 6.4% | 13.1% | 21.0% | 21.5% |
  | **Cash, the basket's fall (as built)** | **9.0% / 8.5%** | **31.2% / 31.4%** | **56.1% / 55.4%** | **76.9% / 76.4%** | 100% |
  | Cash, the basket at the strategy's usual exposure | 7.5% | 25.2% | 45.0% | 63.4% | 52.0% |
  | Cash, a fixed 25% / 30% | 8.6% / 8.9% | 28.1% / 30.1% | 49.3% / 53.6% | 68.6% / 74.1% | 77% / 88% |
  | H1 as champion, H1's own fall | 7.7% | 27.0% | 50.4% | 71.5% | 78.9% |
  | H4 as champion, H4's own fall | 8.1% | 26.8% | 48.1% | 66.4% | 75.1% |
  | H1 as champion, the basket's fall | 8.8% | 30.8% | 55.6% | 76.5% | 100% |

  Against the basket's fall the promoted rows are what they were against H0
  (the other rows move by under a point). A guard set by a champion's own
  fall, or by anything tighter than the basket's, cuts the edges' promotions
  and the twins' alike, so the odds of an edge over a twin do not move and it
  buys nothing. Against a promoted champion the basket's fall is looser than
  that champion's own, and the difference lands in the kills: with H1 as
  champion, twins killed at day 60 go from 40% to 33% and unproven from 17%
  to 22%, Sharpe 2 edges killed at day 60 from 20% to 13%, and a twin's test
  runs about 4 days longer. Fewer wrong kills of edges is the trade; a kill
  is what tells the agent an idea had nothing, so the cost is a little less
  of that evidence. The 9 in 100 false promotions are rule 1's, with or
  without H0. The study holds the champion still; it did not measure a
  change of the title inside a window.
- **The tests that began against H0** (H1, H2, H4 and H5) are judged against
  the champion account by the rules they began under. The account runs H0
  for them, paying its paper costs, unless a promotion comes first: then
  their champion side is that account's record across the change, as before
  ruleset 8. While `retired_champions` names a config, each of their
  results, first looks included, and each hour's summary say beside it what
  the same look makes of their numbers against cash, by their own one look
  rule ("Against cash (measured, not applied to this test)"). When the
  champion's config is still a retired one and no test is judged against
  the champion account any more, nor is a promotion being guarded, the
  champion's config becomes cash (state/champion/changes.json: "H0
  retired"), the account sells what it holds at the next hourly run, and it
  holds cash until a config is promoted. A slot record that cannot be read
  while the slot's config is one of its own may hold such a test, so it
  holds the switch too.
- **A promotion judged against cash**, while the title is cash: the champion
  account takes the promoted config, and for the next 60 days the shadow
  holds cash. The promotion is reverted, to cash, only if over those days
  the promoted config's skill is below cash's and its daily skill t is at
  or below minus `cash_guard_skill_t` (1.0), on 30 fills or more
  (`min_trades`) unless the t is twice that low (-2.0). Skill below nothing
  over 60 days happens to more than half of the configs with no edge, and
  would revert a real edge too often. Share of promotions reverted, on fresh
  60 day windows of the study's twins (seeds 21 and 22), configs that make
  80 to 140 fills in 60 days:

  | Guard | Twin with no skill | Sharpe 1 | Sharpe 2 | Sharpe 3 |
  | --- | --- | --- | --- | --- |
  | H0's (30 fills, skill above the promoted config's, drawdown) | 16% | 6% | 3% | 1% |
  | Cash: skill below nothing | 59% | 33% | 20% | 11% |
  | **Cash: and a daily skill t of -1.0 or below (as built)** | **19% / 20%** | **5.4% / 5.9%** | **2.4% / 2.5%** | **1.3% / 1.0%** |

  A t says how steady a fall was, not how big, and it counts days, not
  bets: one losing day in otherwise flat ones reads exactly -1, whatever its
  size. Hence the fills for a fall that only just reaches the bar. A steady
  fall on few fills, a config that buys and holds into a falling market,
  reads far lower, and is reverted (Fin, 2026-10-05: a bot that just buys
  and holds is killed). Cash asks no fills of itself: the 30 fills are there
  to tell a strategy's bets from luck, and cash makes none. A test judged
  against cash and promoted
  after a config took the title deposes that config, which then guards the
  promotion by the ordinary rule; after a promotion judged against the
  champion account, the account's config at the time guards it (cash, with
  the rule above, if the title had gone back to cash).
- **Known limits, to be settled with the rest of ruleset 8.** A deposed
  config that makes fewer than 30 fills in 60 days can never win the title
  back through the guard, whatever its skill (H0 made 30 in every window). A
  second winner in the hour of a promotion is restarted with a fresh window,
  while one that passes an hour later keeps its window and is judged against
  the title's record, mostly cash's.
- `retired_champions: off` (or an empty list) retires nothing: a test that
  begins while a config is champion is then judged against the champion
  account (with the basket's fall as its guard, like every test from
  ruleset 8), and no older test is measured against cash. While the
  champion's config is cash itself, a test is judged against cash all the
  same. A line that is missing or cannot be read retires H0, the documented
  value, and is said as SETTING NOT USED. `cash_guard_skill_t: off` reverts
  to cash on the skill comparison alone.
- A slot record whose `against` is anything but `cash` or `champion` (a
  hand edit gone wrong) is not guessed at: nothing is ruled on that test
  until the record is mended or the test is voided, and the summary says so
  every hour.

## The early kills

Two, asked every hour of a test, either ending it at once.

**Losses.** A test is ended early when it has lost more than 15% since it
began and has lost more than the market itself over the same span (the
basket, held from the test's start).

Until ruleset 7 this was "more than 15% under its own high inside the
window", whatever the market had done. Replayed on the same 687 days, that
ended 55 of 100 twins and 40 of 100 Sharpe 2 edges before day 60: the
market itself fell far more than 15%, so anything that held coins hit it.
The live configs as they are would have been ended before day 60 in 60 (H1),
46 (H2) and 65 (H4) of 100 starts. It would also end a test that had risen
and then given back 16%, even while it was still well above where it began.

Read as it is now, it ends 25 of 100 twins and 5 of 100 Sharpe 2 edges
inside 120 days, and H1, H2 and H4 as they are in 36, 14 and 17 of 100
starts. It costs almost nothing in promotions (56 of 100 Sharpe 2 edges are
promoted with it and 57 with no early kill at all) and frees a twin's slot
about 8 days sooner on average.

A book that holds half its equity is not safe from it: what matters is
losing more than the whole market, and a few coins that fall harder than
the rest can do that at any exposure (H1 usually holds a third).

**Costs.** After 14 days, live costs running at more than three times the
gate's cost limit (45% of equity a year): a fees treadmill. The costs
counted are those of every fill since the test began, its first hour's
included.

A test's return is measured from its equity after the fills of its first
hour. So the cost of getting from the book it was handed to its own is in
the costs shown, and in the cost kill, and not in its return or its gross
pnl. A result's line says how much that was.

## The small print

Nearly every line of it is a case with a test under tests/gate/.

- Nothing is promoted on fewer than 30 fills. A slow test with good trades
  is kept, not crowned: a handful of good trades cannot yet be told from
  luck. From day 7 the summary says when a test is not on pace for 30 fills
  by its first look or by its verdict. The fills of the hour a test began
  in count towards the 30, and are left out of the pace: they are the move
  from the book the slot held to the test's own.
- The t needs at least 10 daily readings; before that there is no reading. A
  last day that is less than half over counts with the day before it, so a
  first look in the first hour of day 60 rests on 60 readings. A day's
  reading ends at the account's last row of that day, and the basket is read
  at the last hourly close before that moment. So after hours or days the
  bot did not run, the account and the basket still cover the same span.
- The market a test is measured against starts at the test's own start
  time, read between the two hourly prices either side of it, and ends at
  the last candle that had closed. (It used to start up to an hour late and
  leave that hour's move out for the whole test.)
- In a test's first hour no candle that closes inside its window is on
  file yet. The summary says "no skill figure yet", and nothing is wrong.
- A figure that is not a number is never a pass.
- Nothing is ruled on a record that is damaged: that is not a strategy with
  nothing to show. Every hour, before an account is read, its files are set
  against the account's own counts. The trades file must have one row for
  every fill the account has made, and every row must be a fill: a time, a
  pair, buy or sell, and a quantity and a price above zero. The equity file
  must have one row for every reading the account has taken, begin at the
  account's first run, end at its last, be in time order, and every row
  must be a reading: a time, an equity, an exposure and costs, each a
  number. A trades file that cannot be parsed fails the same way. So does
  an account with no equity reading in the test's window. For that slot no
  look is taken and no early kill is made. If the damaged record is the
  champion's, that holds for every slot. The shadow guard waits the same
  way. The log and the summary say what is wrong every hour until the file
  is mended, and the hour goes on for everything else.
- What that cannot see: a row whose figures were changed and still read as
  numbers, every cell of it. And an account counts its readings only from
  its first run under ruleset 7, so rows lost from the middle of an equity
  file before that look the same as hours the bot did not run.
- A slot's own record (meta.json) that cannot be read does not stop the
  hour either. If the slot's config is the champion's it holds no test, and
  its record is simply written afresh. If it has a config of its own, its
  account still trades and no test is started, ended or ruled on in that
  slot until the record is mended or the test is voided.
- The verdict code waits; the engine stops. The engine (bot/run.py) runs
  first each hour, and when it cannot do its own work it stops the whole
  hour, loudly and with nothing committed. The cases known: an account's
  own file (account.json), a config file or configs/risk.yaml cannot be
  read at all; a file it must add a row to does not begin with a header it
  wrote (equity.csv and decisions.csv get a row every hour, trades.csv in an
  hour with a fill), and it does not rewrite or add to such a file; a
  candle file cannot be read; the `slots` line is not a whole number of 1
  or more; no pair has the candle that has just closed, or no pair has a
  quote. A ruling that has been made and cannot be written (the ledger,
  champion.yaml, a slot's or the shadow's files) stops the hour the same
  way. The next hour starts from the last whole state, replays what was
  missed and makes the ruling again.
- A test whose record cannot be read can still be voided
  (configs/void.yaml). It is voided without its numbers. When it is the
  slot's own record that cannot be read, the request must name the
  hypothesis in that slot's config, and the void writes the record afresh.
- When the rules compare on skill, no look is taken in an hour when the
  candles for a test's window are missing, are missing for some pairs,
  begin more than a day into the window for some pairs, or lack, for some
  pairs, the candle that closed at the top of that hour. The hourly run
  fetches that candle just before, so in a healthy hour every pair has it.
  (A run that straddles the top of an hour waits one hour for the same
  reason.) A hole in the middle of a pair's candles is not looked for: the
  price is carried across it, which leaves the window's total right and
  bends the daily figures a little for the days of the hole. Nothing is
  ever ruled on raw return because the market data was not there. The early kill on losses always needs the basket, whatever the
  rules compare on, and waits too. The cost kill needs no market data and
  does not wait. The shadow guard waits like a look. The log says what is
  missing. The summary says "no skill figure this hour" for a test and "no
  ruling this hour" for the guard, each with the reason, and the slot's
  line says a look or a verdict is due.
- Between a first look and day 120 nothing is due, so nothing is said to be
  waiting.
- A test restarted against a new champion (two winners in one hour) begins
  again under the rules of that day, with a fresh first look.
- A first look belongs to the window it was taken in. If Fin resets a slot's
  clock, the new window gets its own.
- A test that has had a first look is never ruled by the one look rule,
  whatever is later taken out of the rules file. It gets its second look.
- If the champion's config changes while a test runs (a promotion in
  another slot, or a revert by the shadow guard), the test carries on. The
  champion side is then that account's own record across both configs, and
  its skill is measured stretch by stretch, each against the usual exposure
  of the config that ran it, so a change does not rewrite the days before
  it. (If a config's usual exposure is not on record, the window's average
  stands in.) The result says so in a "Champion change" line. The shadow
  guard is what then compares the new champion with the one before.
- An idle slot holds cash (ruleset 8). When the champion changes, an idle
  slot still on the old champion's config, as idle slots were before ruleset
  8, is moved to cash, so nothing starts a test by accident; the hourly
  ruling does the same for any idle slot it finds on the champion's config.
  Idle is read from the slot's config: one whose config is cash or the
  champion's holds no test, whatever its record says.
- A second promotion while the guard on an earlier one is still running ends
  that guard. The ledger gets a `superseded` block for the earlier
  promotion, with the guard's numbers so far, or without them when its
  record cannot be read. That promotion was neither confirmed nor reverted.
- Every setting of rule 1 in the `challenger:` block of configs/risk.yaml
  is read through one checked function. A line that is missing, or written
  in a way that cannot be used (a blank, text where a number belongs, a
  number outside what the setting can be, `skil` for `skill`), never stops
  the hour and never loosens the rule: the value documented in that file
  stands in, the log names the line every hour and the summary says
  "SETTING NOT USED" until it is mended. For `fast_pass_skill_t` what
  stands in is no fast pass. A line this code does not read (a slip in a
  name, `two_looks_from_rulset`) is said to do nothing, and the setting it
  was meant for is then a missing line like any other. (The file as a whole
  must still be valid YAML: a stray bracket that makes it unreadable stops
  the run, as above.)
- Leaving a line out switches nothing off. To switch one of these off on
  purpose, write the word `off`. `two_looks_from_ruleset: off`: no new test
  gets two looks. `fast_pass_skill_t: off` (or 0): no fast pass.
  `min_skill_t: off` (or 0): no t bar. `min_skill: off`: no floor under
  skill. `max_dd_floor: off` (or 0): the drawdown guard has no 10% floor.
  `early_kill_drawdown: off` (or 0): no early kill on losses.
  `treadmill_kill_multiple: off` (or 0): no cost kill. `compare_on` takes
  `skill` or `return`; with `return` the rule compares raw returns, as it
  did before 2026-09-25, and needs no market data for a look. The value of
  a test's trades is read the same way either way.
- Two lines outside that function are covered too. If the `ruleset:` line
  cannot be read, a test that starts meanwhile is stamped `unreadable` and
  judged by the two look rule, never as an old test. If the gate's
  `max_cost_drag` is missing or cannot be used (it is a share of equity a
  year, above 0 and no more than 1), the documented 15% stands in for the
  cost kill. Both are said the same way.
- `slots`, the number of slots, must be a whole number of 1 or more, and
  anything else stops the run, as above. If it is lowered while a slot
  beyond it holds a running test, that test is neither run nor ruled on,
  and the log and the summary say so every hour.

## The confidence figure

Every verdict on a test (promoted, killed, unproven), every first look and
every running test in the hourly summary carries one number: the chance that
the strategy has a real edge. It starts at 10% for any idea and moves by how
much more likely the observed t of the daily skill is from a strategy with a
skill Sharpe of 1.5 than from one that only breaks even after costs.

Fin asked for one score that weighs the two rules by which is the stronger
evidence. Measured on the twins for a Sharpe 2 edge, a pass under the old
rule made an edge about 2 times as likely as a twin and a promotion under
rule 1 makes it about 6 times as likely. A pass under the old rule that
rule 1 would not confirm made it 0.7 times as likely: evidence the wrong
way. Both rules lean on the same thing, the t of the daily skill, the second
over twice the days. So the figure is built on that t over the whole test:
it gives the second rule's evidence its full weight and the first rule's
none beyond what the t already holds.

It moves slowly on purpose. t of 1 after 60 days turns 10% into 15%. t of 2
after a year turns it into 42%, t of 3 after a year into 76%.

It is more cautious than "6 times as likely", and both are right. That
figure is the average over every test that passes rule 1, most of them well
clear of the bar, against twins that pay costs for nothing. The confidence
figure asks a harder question of one test: how much likelier is this exact
t from a real edge than from a strategy that breaks even. A test promoted
with a t of exactly 1.0 at day 120 reads 15%. That is the honest size of
what 120 days can show.

It never says 0% or 100%: it is held between 1% and 95%. The sum knows two
stories, a real edge or none. It leaves out a third, that the measuring is
wrong, and that is the likeliest reason for a reading that looks certain.

One thing it cannot see, so the line says it. Skill is measured against a
strategy's usual exposure. A bot that usually holds half the market and sat
fully invested through a 60 day rise shows a little skill every day for one
decision it never went back to, and the figure counts that as sixty bets.
(In the test that pins this, a bot that sat fully invested through a rise
of 19% read 27%.) The size of that standing tilt is plain arithmetic: its
average exposure in the window minus its usual exposure, times what the
basket did. When the figure reads above its starting point and half or more
of the skill behind it is that tilt, or the test has finished no trade of
its own, the line ends "Read it with care" and says what the figure is
resting on. A first look like that gets no fast pass. The tilt is not used
to kill, or to refuse a promotion at day 120: a trend follower that is in
for most of a rising window has a tilt too, and earned it.

## Rule 2: paper to real money

Nothing here happens on its own. When a champion meets every line, the case
is put to Fin with what it could earn and what it could lose, and he decides.

| What | The bar | Why |
| --- | --- | --- |
| Status | Promoted under rule 1 and still champion | Rule 1 passed, and the shadow guard has had its chance. |
| Record | 180 days or more under one unchanged config and ruleset, 100 fills or more | Before 180 days even a Sharpe 3 edge shows a t of 2 only 57% of the time. |
| Statistics | The daily skill t since the test began reaches 2.0 at a weekly check | A strategy that breaks even gets there about 2 times in 100 within a year; a Sharpe 2 edge 66 times, a Sharpe 3 edge 96. |
| Costs | Realised gross bps per round trip at least 60, on live spreads, and at least twice a round trip's cost at the fee the venue would really charge Fin | Twice the 30 bps a round trip costs on paper. The paper book charges Binance's 10 bps a side; a venue that charges more raises this bar with it. |
| Machinery | The backtest engine replays the same days and matches live fills within 5%; no measuring bug for 60 days | Several measuring bugs were found in the first three weeks, and more in the review of this rule. |
| History | Positive skill in at least 4 of the 6 calendar years the long backtest covers | In sample, so it can only veto. |
| Sign off | Fin writes the decision and the stake into the repo | His money, his call. |
| Stake | Small and fixed, spot only, on a venue Fin can legally use; back to paper at minus 20% | Sized so that being wrong is affordable. |

Real order code would live in a separate private repo. This one stays paper
only and its gate rejects anything that could place an order. Nothing in this
file is financial advice.
