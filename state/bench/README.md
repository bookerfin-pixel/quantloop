# The bench's league table

Last changed on 2026-10-13 at 22:19 UTC. The bench workflow (`python -m bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row says the day it was read on. bot/bench.py says how each figure is made.

```
config                         days      net  timing/yr  run/yr  costs/yr  left/yr      t  twins  luck  last 365     read on
H0 ts_momentum (champion)     1,825   -92.3%      +8.6%   +0.5%     58.2%   -49.1%   -3.3    73%   28%       19%  2026-10-11
H1 mean_reversion             1,822   -88.0%     -22.3%   -0.1%     16.7%   -39.1%   -2.8     6%   94%       68%  2026-10-11
H2 vol_breakout               1,765   +40.1%     +16.5%   +1.0%     10.5%    +7.0%   +0.5    89%   11%       59%  2026-10-11
H5 swing_reversal             1,812   +73.7%     +15.5%   +0.8%      3.9%   +12.4%   +1.6    99%    2%       18%  2026-10-11
Each config is read from the first hour it could decide to the end of the history on file when it was read; days is how long that is. Over the first row's 1,825 days the basket made -44.5%. net: what the config made after costs. timing/yr: the book as it last traded each pair, less its average twin, before costs, a year. run/yr: what letting positions run between trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the share of its twins it beats before costs (a book with no timing beats about half), over the whole run and over the last 365 days. luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck. n/a: the book could not be set against twins. In sample, all of it.
```

```
bench: H0 (ts_momentum), 1,825 days from 2021-10-13 to 2026-10-11, 10 pairs
  what it made: -92.3% after costs, with 0.59 of its equity invested on average. The basket (the pairs in equal parts) made -44.5%, and the middle one of its twins -95.4% after the same costs
  twins: before costs it beats 73% of 1,000 twins over the whole run and 19% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 392 separate ones, and among that many a book with no timing does as well as this about 28% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (18 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +8.6% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.5%. Costs take 58.2% a year, so -49.1% a year is left: a yearly Sharpe ratio of -1.47 and a t of -3.3, where a t under about 2 either way cannot be told from noise. At double costs -107.2% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (80 days) -7.3%, -22.2%, -3%, 29%; 2022 +64.0%, +4.3%, -76%, 95%; 2023 -5.0%, -57.5%, +140%, 42%; 2024 +17.3%, -41.0%, +85%, 69%; 2025 -11.0%, -72.2%, -39%, 39%; 2026 (284 days) -14.8%, -56.6%, -12%, 28%
  its best and worst days: of what is left, its 9 best days carry +15.2% a year and its 9 worst -11.3%
  half the coins (twins beaten on each half, halved two ways): 49%, 57%, 58%, 64%
  nearby settings (twins beaten with every number in params moved by up to 25%): 55%, 56%, 74%, 82%, 84%, 86%, against its own 73%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 474 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,341 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -1.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: cannot be told from luck. A book with no timing at all does as well about 28% of the time.
  Bench: timing +8.6% a year before costs over 1,825 days, which beats 73% of its twins (19% of them over the last 365 days), and a book with no timing does as well 28% of the time; letting positions run added 0.5% and costs took 58.2% a year, so -49.1% is left (Sharpe -1.47, t -3.3); ahead after costs in 1 of 6 years; nearby settings beat 55%, 56%, 74%, 82%, 84%, 86% of their twins; halves of the coins 49%, 57%, 58%, 64%. In sample.
```

```
bench: H1 (mean_reversion), 1,822 days from 2021-10-16 to 2026-10-11, 10 pairs
  what it made: -88.0% after costs, with 0.32 of its equity invested on average. The basket (the pairs in equal parts) made -49.8%, and the middle one of its twins -62.2% after the same costs
  twins: before costs it beats 6% of 1,000 twins over the whole run and 68% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 236 separate ones, and among that many a book with no timing does as well as this about 94% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (16 days, SOL) or as long again as the candles, whichever is longer
  what the timing is worth: -22.3% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, took 0.1%. Costs take 16.7% a year, so -39.1% a year is left: a yearly Sharpe ratio of -1.23 and a t of -2.8, where a t under about 2 either way cannot be told from noise. At double costs -55.8% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (77 days) -3.5%, -7.9%, -13%, 41%; 2022 -43.9%, -61.5%, -76%, 10%; 2023 -34.0%, -47.2%, +140%, 10%; 2024 -30.2%, -48.3%, +85%, 18%; 2025 +0.6%, -16.6%, -39%, 50%; 2026 (284 days) -0.1%, -13.7%, -12%, 50%
  its best and worst days: of what is left, its 9 best days carry +12.7% a year and its 9 worst -16.5%
  half the coins (twins beaten on each half, halved two ways): 2%, 4%, 4%, 10%
  nearby settings (twins beaten with every number in params moved by up to 25%): 0%, 2%, 3%, 4%, 4%, 4%, against its own 6%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 127 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,338 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 1% of them (the middle one: -0.6), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 1%; a fast pass at day 60 in 2%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -22.3% a year before costs over 1,822 days, which beats 6% of its twins (68% of them over the last 365 days), and a book with no timing does as well 94% of the time; letting positions run took 0.1% and costs took 16.7% a year, so -39.1% is left (Sharpe -1.23, t -2.8); ahead after costs in 0 of 6 years; nearby settings beat 0%, 2%, 3%, 4%, 4%, 4% of their twins; halves of the coins 2%, 4%, 4%, 10%. In sample.
```

```
bench: H2 (vol_breakout), 1,765 days from 2021-12-12 to 2026-10-11, 10 pairs
  what it made: +40.1% after costs, with 0.31 of its equity invested on average. The basket (the pairs in equal parts) made -42.0%, and the middle one of its twins -41.8% after the same costs
  twins: before costs it beats 89% of 1,000 twins over the whole run and 59% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 152 separate ones, and among that many a book with no timing does as well as this about 11% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (29 days, XRP) or as long again as the candles, whichever is longer
  what the timing is worth: +16.5% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 10.5% a year, so +7.0% a year is left: a yearly Sharpe ratio of +0.25 and a t of +0.5, where a t under about 2 either way cannot be told from noise. At double costs -3.6% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +20.7%, +10.3%, -76%, 72%; 2023 +11.0%, +1.0%, +140%, 68%; 2024 +19.9%, +13.9%, +85%, 76%; 2025 +16.2%, +5.6%, -39%, 71%; 2026 (284 days) +12.8%, +4.2%, -12%, 70%
  its best and worst days: of what is left, its 9 best days carry +12.3% a year and its 9 worst -9.3%
  half the coins (twins beaten on each half, halved two ways): 86%, 96%, 98%, 99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 84%, 84%, 92%, 93%, 94%, 95%, against its own 89%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 77 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,281 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 15% of them (the middle one: +0.1), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 15%; a fast pass at day 60 in 1%
  Reading: cannot be told from luck. A book with no timing at all does as well about 11% of the time.
  Bench: timing +16.5% a year before costs over 1,765 days, which beats 89% of its twins (59% of them over the last 365 days), and a book with no timing does as well 11% of the time; letting positions run added 1.0% and costs took 10.5% a year, so +7.0% is left (Sharpe +0.25, t +0.5); ahead after costs in 5 of 5 years; nearby settings beat 84%, 84%, 92%, 93%, 94%, 95% of their twins; halves of the coins 86%, 96%, 98%, 99%. In sample.
```

```
bench: H5 (swing_reversal), 1,812 days from 2021-10-26 to 2026-10-11, 10 pairs
  what it made: +73.7% after costs, with 0.09 of its equity invested on average. The basket (the pairs in equal parts) made -54.7%, and the middle one of its twins -22.4% after the same costs
  twins: before costs it beats 99% of 1,000 twins over the whole run and 18% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 140 separate ones, and among that many a book with no timing does as well as this about 2% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (17 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +15.5% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.8%. Costs take 3.9% a year, so +12.4% a year is left: a yearly Sharpe ratio of +0.73 and a t of +1.6, where a t under about 2 either way cannot be told from noise. At double costs +8.5% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (67 days) +16.5%, +15.3%, -21%, 95%; 2022 +1.2%, -1.2%, -76%, 49%; 2023 -12.5%, -17.3%, +140%, 26%; 2024 +43.6%, +40.1%, +85%, 98%; 2025 +39.0%, +37.4%, -39%, 99%; 2026 (284 days) -10.6%, -12.6%, -12%, 8%
  its best and worst days: of what is left, its 9 best days carry +10.2% a year and its 9 worst -8.7%
  half the coins (twins beaten on each half, halved two ways): 84%, 92%, 98%, >99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 74%, 88%, 97%, 98%, 98%, 98%, against its own 99%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 20 fills in 60 days (a promotion needs 30); in 9% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,328 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 27% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 25%; a fast pass at day 60 in under 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: ahead of its average twin after costs in only 3 of 6 years; over the last 365 days it beats only 18% of its twins.
  Bench: timing +15.5% a year before costs over 1,812 days, which beats 99% of its twins (18% of them over the last 365 days), and a book with no timing does as well 2% of the time; letting positions run added 0.8% and costs took 3.9% a year, so +12.4% is left (Sharpe +0.73, t +1.6); ahead after costs in 3 of 6 years; nearby settings beat 74%, 88%, 97%, 98%, 98%, 98% of their twins; halves of the coins 84%, 92%, 98%, >99%. In sample.
```
