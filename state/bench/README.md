# The bench's league table

Last changed on 2026-11-02 at 09:17 UTC. The bench workflow (`python -m bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row says the day it was read on. bot/bench.py says how each figure is made.

```
config                         days      net  timing/yr  run/yr  costs/yr  left/yr      t  twins  luck  last 365     read on
H0 ts_momentum (champion)     1,847   -93.8%      +7.0%   +0.5%     58.2%   -50.7%   -3.4    70%   31%       24%  2026-11-02
H1 mean_reversion             1,844   -88.8%     -21.6%   -0.1%     16.8%   -38.6%   -2.7     5%   95%       62%  2026-11-02
H2 vol_breakout               1,787   +24.4%     +15.6%   +1.0%     10.5%    +6.0%   +0.5    89%   11%       57%  2026-11-02
H5 swing_reversal             1,834   +73.7%     +15.5%   +0.8%      3.9%   +12.4%   +1.6    99%    2%       21%  2026-11-02
H6 relative_reversion         1,820   -75.2%     -11.6%   +0.2%      8.5%   -19.9%   -1.4    26%   75%       76%  2026-10-30
Each config is read from the first hour it could decide to the end of the history on file when it was read; days is how long that is. Over the first row's 1,847 days the basket made -53.2%. net: what the config made after costs. timing/yr: the book as it last traded each pair, less its average twin, before costs, a year. run/yr: what letting positions run between trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the share of its twins it beats before costs (a book with no timing beats about half), over the whole run and over the last 365 days. luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck. n/a: the book could not be set against twins. In sample, all of it.
```

```
bench: H0 (ts_momentum), 1,847 days from 2021-10-13 to 2026-11-02, 10 pairs
  what it made: -93.8% after costs, with 0.58 of its equity invested on average. The basket (the pairs in equal parts) made -53.2%, and the middle one of its twins -96.2% after the same costs
  twins: before costs it beats 70% of 1,000 twins over the whole run and 24% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 359 separate ones, and among that many a book with no timing does as well as this about 31% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (18 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +7.0% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.5%. Costs take 58.2% a year, so -50.7% a year is left: a yearly Sharpe ratio of -1.53 and a t of -3.4, where a t under about 2 either way cannot be told from noise. At double costs -108.7% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (80 days) -7.7%, -22.6%, -3%, 29%; 2022 +64.4%, +4.7%, -76%, 96%; 2023 -4.3%, -56.9%, +140%, 44%; 2024 +17.4%, -40.9%, +85%, 70%; 2025 -9.6%, -70.8%, -39%, 39%; 2026 -24.7%, -70.0%, -26%, 17%
  its best and worst days: of what is left, its 9 best days carry +15.1% a year and its 9 worst -11.1%
  half the coins (twins beaten on each half, halved two ways): 52%, 60%, 64%, 66%
  nearby settings (twins beaten with every number in params moved by up to 25%): 52%, 57%, 72%, 78%, 82%, 83%, against its own 70%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 473 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,363 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -1.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: cannot be told from luck. A book with no timing at all does as well about 31% of the time.
  Bench: timing +7.0% a year before costs over 1,847 days, which beats 70% of its twins (24% of them over the last 365 days), and a book with no timing does as well 31% of the time; letting positions run added 0.5% and costs took 58.2% a year, so -50.7% is left (Sharpe -1.53, t -3.4); ahead after costs in 1 of 6 years; nearby settings beat 52%, 57%, 72%, 78%, 82%, 83% of their twins; halves of the coins 52%, 60%, 64%, 66%. In sample.
```

```
bench: H1 (mean_reversion), 1,844 days from 2021-10-16 to 2026-11-02, 10 pairs
  what it made: -88.8% after costs, with 0.32 of its equity invested on average. The basket (the pairs in equal parts) made -57.7%, and the middle one of its twins -65.5% after the same costs
  twins: before costs it beats 5% of 1,000 twins over the whole run and 62% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 238 separate ones, and among that many a book with no timing does as well as this about 95% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (16 days, SOL) or as long again as the candles, whichever is longer
  what the timing is worth: -21.6% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, took 0.1%. Costs take 16.8% a year, so -38.6% a year is left: a yearly Sharpe ratio of -1.22 and a t of -2.7, where a t under about 2 either way cannot be told from noise. At double costs -55.3% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (77 days) -3.0%, -7.4%, -13%, 43%; 2022 -44.6%, -62.1%, -76%, 8%; 2023 -35.5%, -48.7%, +140%, 8%; 2024 -30.5%, -48.6%, +85%, 18%; 2025 +3.1%, -14.1%, -39%, 53%; 2026 +1.2%, -13.9%, -26%, 52%
  its best and worst days: of what is left, its 9 best days carry +12.6% a year and its 9 worst -16.3%
  half the coins (twins beaten on each half, halved two ways): 4%, 4%, 9%, 12%
  nearby settings (twins beaten with every number in params moved by up to 25%): 2%, 2%, 3%, 4%, 6%, 6%, against its own 5%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 129 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,360 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 1% of them (the middle one: -0.6), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 1%; a fast pass at day 60 in 2%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -21.6% a year before costs over 1,844 days, which beats 5% of its twins (62% of them over the last 365 days), and a book with no timing does as well 95% of the time; letting positions run took 0.1% and costs took 16.8% a year, so -38.6% is left (Sharpe -1.22, t -2.7); ahead after costs in 0 of 6 years; nearby settings beat 2%, 2%, 3%, 4%, 6%, 6% of their twins; halves of the coins 4%, 4%, 9%, 12%. In sample.
```

```
bench: H2 (vol_breakout), 1,787 days from 2021-12-12 to 2026-11-02, 10 pairs
  what it made: +24.4% after costs, with 0.31 of its equity invested on average. The basket (the pairs in equal parts) made -51.1%, and the middle one of its twins -47.5% after the same costs
  twins: before costs it beats 89% of 1,000 twins over the whole run and 57% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 155 separate ones, and among that many a book with no timing does as well as this about 11% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (29 days, XRP) or as long again as the candles, whichever is longer
  what the timing is worth: +15.6% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 10.5% a year, so +6.0% a year is left: a yearly Sharpe ratio of +0.22 and a t of +0.5, where a t under about 2 either way cannot be told from noise. At double costs -4.5% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +21.3%, +10.8%, -76%, 72%; 2023 +10.2%, +0.2%, +140%, 67%; 2024 +22.0%, +16.0%, +85%, 78%; 2025 +16.1%, +5.5%, -39%, 72%; 2026 +7.6%, -1.7%, -26%, 62%
  its best and worst days: of what is left, its 9 best days carry +12.4% a year and its 9 worst -9.3%
  half the coins (twins beaten on each half, halved two ways): 88%, 98%, 98%, >99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 80%, 83%, 88%, 94%, 94%, 96%, against its own 89%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 77 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,303 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 15% of them (the middle one: +0.1), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 15%; a fast pass at day 60 in 1%
  Reading: cannot be told from luck. A book with no timing at all does as well about 11% of the time.
  Bench: timing +15.6% a year before costs over 1,787 days, which beats 89% of its twins (57% of them over the last 365 days), and a book with no timing does as well 11% of the time; letting positions run added 1.0% and costs took 10.5% a year, so +6.0% is left (Sharpe +0.22, t +0.5); ahead after costs in 4 of 5 years; nearby settings beat 80%, 83%, 88%, 94%, 94%, 96% of their twins; halves of the coins 88%, 98%, 98%, >99%. In sample.
```

```
bench: H5 (swing_reversal), 1,834 days from 2021-10-26 to 2026-11-02, 10 pairs
  what it made: +73.7% after costs, with 0.09 of its equity invested on average. The basket (the pairs in equal parts) made -61.8%, and the middle one of its twins -22.0% after the same costs
  twins: before costs it beats 99% of 1,000 twins over the whole run and 21% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 147 separate ones, and among that many a book with no timing does as well as this about 2% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (17 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +15.5% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.8%. Costs take 3.9% a year, so +12.4% a year is left: a yearly Sharpe ratio of +0.73 and a t of +1.6, where a t under about 2 either way cannot be told from noise. At double costs +8.5% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (67 days) +16.8%, +15.5%, -21%, 96%; 2022 +1.5%, -1.0%, -76%, 50%; 2023 -12.1%, -16.8%, +140%, 25%; 2024 +43.2%, +39.7%, +85%, 98%; 2025 +38.3%, +36.8%, -39%, over 99%; 2026 -9.9%, -11.8%, -26%, 10%
  its best and worst days: of what is left, its 9 best days carry +10.1% a year and its 9 worst -8.6%
  half the coins (twins beaten on each half, halved two ways): 84%, 94%, 98%, 99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 70%, 89%, 98%, 98%, 99%, 100%, against its own 99%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 20 fills in 60 days (a promotion needs 30); in 9% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,350 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 26% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 25%; a fast pass at day 60 in under 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: ahead of its average twin after costs in only 3 of 6 years; over the last 365 days it beats only 21% of its twins.
  Bench: timing +15.5% a year before costs over 1,834 days, which beats 99% of its twins (21% of them over the last 365 days), and a book with no timing does as well 2% of the time; letting positions run added 0.8% and costs took 3.9% a year, so +12.4% is left (Sharpe +0.73, t +1.6); ahead after costs in 3 of 6 years; nearby settings beat 70%, 89%, 98%, 98%, 99%, 100% of their twins; halves of the coins 84%, 94%, 98%, 99%. In sample.
```

```
bench: H6 (relative_reversion), 1,820 days from 2021-11-05 to 2026-10-30, 10 pairs
  what it made: -75.2% after costs, with 0.49 of its equity invested on average. The basket (the pairs in equal parts) made -64.5%, and the middle one of its twins -56.3% after the same costs
  twins: before costs it beats 26% of 1,000 twins over the whole run and 76% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 91 separate ones, and among that many a book with no timing does as well as this about 75% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (63 days, DOT) or as long again as the candles, whichever is longer
  what the timing is worth: -11.6% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.2%. Costs take 8.5% a year, so -19.9% a year is left: a yearly Sharpe ratio of -0.61 and a t of -1.4, where a t under about 2 either way cannot be told from noise. At double costs -28.4% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (57 days) +7.0%, +5.5%, -25%, 67%; 2022 -5.4%, -14.7%, -76%, 42%; 2023 -18.8%, -25.1%, +140%, 25%; 2024 -19.8%, -30.0%, +85%, 30%; 2025 -45.6%, -54.3%, -39%, 9%; 2026 +24.6%, +19.0%, -28%, 85%
  its best and worst days: of what is left, its 9 best days carry +11.7% a year and its 9 worst -17.7%
  half the coins (twins beaten on each half, halved two ways): 20%, 24% (2 could not be replayed)
  nearby settings (twins beaten with every number in params moved by up to 25%): 21%, 28%, 30%, 34%, 37%, 48%, against its own 26%
  the clock: its code names the candles' time column or asks the time. With the clock moved (by 27, 54, 81, 108, 135, 162 hours) it beats 28%, 36%, 44%, 48%, 60%, 91% of its twins, against its own 26%
  under rule 1: about 55 fills in 60 days (a promotion needs 30); in 1% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,336 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -0.5), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -11.6% a year before costs over 1,820 days, which beats 26% of its twins (76% of them over the last 365 days), and a book with no timing does as well 75% of the time; letting positions run added 0.2% and costs took 8.5% a year, so -19.9% is left (Sharpe -0.61, t -1.4); ahead after costs in 2 of 6 years; nearby settings beat 21%, 28%, 30%, 34%, 37%, 48% of their twins; halves of the coins 20%, 24% (2 could not be replayed). In sample.
```
