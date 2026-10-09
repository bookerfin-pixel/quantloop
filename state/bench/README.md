# The bench's league table

Last changed on 2026-10-09 at 23:23 UTC. The bench workflow (`python -m bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row says the day it was read on. bot/bench.py says how each figure is made.

```
config                         days      net  timing/yr  run/yr  costs/yr  left/yr      t  twins  luck  last 365     read on
H0 ts_momentum (champion)     1,823   -92.4%      +8.6%   +0.5%     58.2%   -49.1%   -3.3    73%   27%       32%  2026-10-09
H1 mean_reversion             1,820   -88.4%     -22.4%   -0.1%     16.7%   -39.3%   -2.8     5%   95%       58%  2026-10-09
H2 vol_breakout               1,763   +40.1%     +16.8%   +1.0%     10.5%    +7.2%   +0.6    88%   12%       72%  2026-10-09
H5 swing_reversal             1,810   +73.7%     +15.7%   +0.8%      3.9%   +12.6%   +1.7    99%    2%       28%  2026-10-09
H4 ts_momentum                1,800   +58.9%     +22.1%   +1.0%      9.1%   +14.0%   +0.9    96%    6%       79%  2026-10-09
Each config is read from the first hour it could decide to the end of the history on file when it was read; days is how long that is. Over the first row's 1,823 days the basket made -46.5%. net: what the config made after costs. timing/yr: the book as it last traded each pair, less its average twin, before costs, a year. run/yr: what letting positions run between trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the share of its twins it beats before costs (a book with no timing beats about half), over the whole run and over the last 365 days. luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck. n/a: the book could not be set against twins. In sample, all of it.
```

```
bench: H0 (ts_momentum), 1,823 days from 2021-10-13 to 2026-10-09, 10 pairs
  what it made: -92.4% after costs, with 0.59 of its equity invested on average. The basket (the pairs in equal parts) made -46.5%, and the middle one of its twins -95.6% after the same costs
  twins: before costs it beats 73% of 1,000 twins over the whole run and 32% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 391 separate ones, and among that many a book with no timing does as well as this about 27% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (18 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +8.6% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.5%. Costs take 58.2% a year, so -49.1% a year is left: a yearly Sharpe ratio of -1.47 and a t of -3.3, where a t under about 2 either way cannot be told from noise. At double costs -107.2% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (80 days) -7.7%, -22.7%, -3%, 29%; 2022 +63.6%, +3.9%, -76%, 96%; 2023 -4.9%, -57.4%, +140%, 43%; 2024 +16.0%, -42.3%, +85%, 68%; 2025 -9.7%, -70.9%, -39%, 41%; 2026 (282 days) -14.1%, -55.6%, -16%, 29%
  its best and worst days: of what is left, its 9 best days carry +15.3% a year and its 9 worst -11.3%
  half the coins (twins beaten on each half, halved two ways): 46%, 59%, 60%, 62%
  nearby settings (twins beaten with every number in params moved by up to 25%): 54%, 58%, 74%, 84%, 84%, 87%, against its own 73%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 474 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,339 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -1.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: cannot be told from luck. A book with no timing at all does as well about 27% of the time.
  Bench: timing +8.6% a year before costs over 1,823 days, which beats 73% of its twins (32% of them over the last 365 days), and a book with no timing does as well 27% of the time; letting positions run added 0.5% and costs took 58.2% a year, so -49.1% is left (Sharpe -1.47, t -3.3); ahead after costs in 1 of 6 years; nearby settings beat 54%, 58%, 74%, 84%, 84%, 87% of their twins; halves of the coins 46%, 59%, 60%, 62%. In sample.
```

```
bench: H1 (mean_reversion), 1,820 days from 2021-10-16 to 2026-10-09, 10 pairs
  what it made: -88.4% after costs, with 0.32 of its equity invested on average. The basket (the pairs in equal parts) made -51.6%, and the middle one of its twins -62.6% after the same costs
  twins: before costs it beats 5% of 1,000 twins over the whole run and 58% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 223 separate ones, and among that many a book with no timing does as well as this about 95% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (16 days, SOL) or as long again as the candles, whichever is longer
  what the timing is worth: -22.4% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, took 0.1%. Costs take 16.7% a year, so -39.3% a year is left: a yearly Sharpe ratio of -1.24 and a t of -2.8, where a t under about 2 either way cannot be told from noise. At double costs -56.0% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (77 days) -3.5%, -7.9%, -13%, 41%; 2022 -43.8%, -61.4%, -76%, 10%; 2023 -34.4%, -47.6%, +140%, 11%; 2024 -29.2%, -47.3%, +85%, 19%; 2025 +0.8%, -16.5%, -39%, 50%; 2026 (282 days) -1.7%, -15.2%, -16%, 48%
  its best and worst days: of what is left, its 9 best days carry +12.8% a year and its 9 worst -16.5%
  half the coins (twins beaten on each half, halved two ways): 4%, 4%, 6%, 16%
  nearby settings (twins beaten with every number in params moved by up to 25%): 2%, 4%, 4%, 6%, 6%, 6%, against its own 5%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 127 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,336 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 1% of them (the middle one: -0.6), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 1%; a fast pass at day 60 in 2%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -22.4% a year before costs over 1,820 days, which beats 5% of its twins (58% of them over the last 365 days), and a book with no timing does as well 95% of the time; letting positions run took 0.1% and costs took 16.7% a year, so -39.3% is left (Sharpe -1.24, t -2.8); ahead after costs in 0 of 6 years; nearby settings beat 2%, 4%, 4%, 6%, 6%, 6% of their twins; halves of the coins 4%, 4%, 6%, 16%. In sample.
```

```
bench: H2 (vol_breakout), 1,763 days from 2021-12-12 to 2026-10-09, 10 pairs
  what it made: +40.1% after costs, with 0.31 of its equity invested on average. The basket (the pairs in equal parts) made -44.1%, and the middle one of its twins -42.4% after the same costs
  twins: before costs it beats 88% of 1,000 twins over the whole run and 72% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 153 separate ones, and among that many a book with no timing does as well as this about 12% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (29 days, XRP) or as long again as the candles, whichever is longer
  what the timing is worth: +16.8% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 10.5% a year, so +7.2% a year is left: a yearly Sharpe ratio of +0.26 and a t of +0.6, where a t under about 2 either way cannot be told from noise. At double costs -3.3% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +20.6%, +10.1%, -76%, 72%; 2023 +10.9%, +1.0%, +140%, 69%; 2024 +20.4%, +14.4%, +85%, 75%; 2025 +16.2%, +5.6%, -39%, 72%; 2026 (282 days) +14.0%, +5.3%, -16%, 72%
  its best and worst days: of what is left, its 9 best days carry +12.4% a year and its 9 worst -9.4%
  half the coins (twins beaten on each half, halved two ways): 88%, 92%, 95%, 99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 82%, 84%, 88%, 94%, 96%, 96%, against its own 88%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 77 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,279 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 15% of them (the middle one: +0.1), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 15%; a fast pass at day 60 in 1%
  Reading: cannot be told from luck. A book with no timing at all does as well about 12% of the time.
  Bench: timing +16.8% a year before costs over 1,763 days, which beats 88% of its twins (72% of them over the last 365 days), and a book with no timing does as well 12% of the time; letting positions run added 1.0% and costs took 10.5% a year, so +7.2% is left (Sharpe +0.26, t +0.6); ahead after costs in 5 of 5 years; nearby settings beat 82%, 84%, 88%, 94%, 96%, 96% of their twins; halves of the coins 88%, 92%, 95%, 99%. In sample.
```

```
bench: H5 (swing_reversal), 1,810 days from 2021-10-26 to 2026-10-09, 10 pairs
  what it made: +73.7% after costs, with 0.09 of its equity invested on average. The basket (the pairs in equal parts) made -56.3%, and the middle one of its twins -22.8% after the same costs
  twins: before costs it beats 99% of 1,000 twins over the whole run and 28% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 138 separate ones, and among that many a book with no timing does as well as this about 2% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (17 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +15.7% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.8%. Costs take 3.9% a year, so +12.6% a year is left: a yearly Sharpe ratio of +0.74 and a t of +1.7, where a t under about 2 either way cannot be told from noise. At double costs +8.7% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (67 days) +16.6%, +15.3%, -21%, 95%; 2022 +1.7%, -0.8%, -76%, 51%; 2023 -12.5%, -17.2%, +140%, 27%; 2024 +43.5%, +40.1%, +85%, 97%; 2025 +38.8%, +37.3%, -39%, over 99%; 2026 (282 days) -10.1%, -12.0%, -16%, 10%
  its best and worst days: of what is left, its 9 best days carry +10.2% a year and its 9 worst -8.7%
  half the coins (twins beaten on each half, halved two ways): 84%, 91%, 97%, 98%
  nearby settings (twins beaten with every number in params moved by up to 25%): 73%, 88%, 98%, 98%, 98%, 98%, against its own 99%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 20 fills in 60 days (a promotion needs 30); in 9% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,326 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 27% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 25%; a fast pass at day 60 in under 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: ahead of its average twin after costs in only 3 of 6 years; over the last 365 days it beats only 28% of its twins.
  Bench: timing +15.7% a year before costs over 1,810 days, which beats 99% of its twins (28% of them over the last 365 days), and a book with no timing does as well 2% of the time; letting positions run added 0.8% and costs took 3.9% a year, so +12.6% is left (Sharpe +0.74, t +1.7); ahead after costs in 3 of 6 years; nearby settings beat 73%, 88%, 98%, 98%, 98%, 98% of their twins; halves of the coins 84%, 91%, 97%, 98%. In sample.
```

```
bench: H4 (ts_momentum), 1,800 days from 2021-11-05 to 2026-10-09, 10 pairs
  what it made: +58.9% after costs, with 0.51 of its equity invested on average. The basket (the pairs in equal parts) made -58.7%, and the middle one of its twins -53.2% after the same costs
  twins: before costs it beats 96% of 1,000 twins over the whole run and 79% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 62 separate ones, and among that many a book with no timing does as well as this about 6% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (73 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +22.1% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 9.1% a year, so +14.0% a year is left: a yearly Sharpe ratio of +0.42 and a t of +0.9, where a t under about 2 either way cannot be told from noise. At double costs +5.0% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (57 days) -5.7%, -6.9%, -25%, 30%; 2022 +22.3%, +17.1%, -76%, 74%; 2023 +48.7%, +41.7%, +140%, 94%; 2024 +33.5%, +23.6%, +85%, 83%; 2025 -0.3%, -11.1%, -39%, 51%; 2026 (282 days) +10.7%, +4.9%, -16%, 63%
  its best and worst days: of what is left, its 9 best days carry +13.6% a year and its 9 worst -13.3%
  half the coins (twins beaten on each half, halved two ways): 92%, 92%, 95%, 98%
  nearby settings (twins beaten with every number in params moved by up to 25%): 86%, 87%, 90%, 92%, 93%, 96%, against its own 96%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 78 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,316 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 10% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 10%; a fast pass at day 60 in 3%
  Reading: it beats most of its twins, with something left after costs, in most years and at double costs; 4 of 4 halves of the coins and 6 of 6 nearby settings beat 75% of their own twins or more. Worth a slot on this evidence, all of which is in sample.
  Bench: timing +22.1% a year before costs over 1,800 days, which beats 96% of its twins (79% of them over the last 365 days), and a book with no timing does as well 6% of the time; letting positions run added 1.0% and costs took 9.1% a year, so +14.0% is left (Sharpe +0.42, t +0.9); ahead after costs in 4 of 6 years; nearby settings beat 86%, 87%, 90%, 92%, 93%, 96% of their twins; halves of the coins 92%, 92%, 95%, 98%. In sample.
```
