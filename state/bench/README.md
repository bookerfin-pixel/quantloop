# The bench's league table

Last changed on 2026-10-30 at 02:15 UTC. The bench workflow (`python -m bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row says the day it was read on. bot/bench.py says how each figure is made.

```
config                         days      net  timing/yr  run/yr  costs/yr  left/yr      t  twins  luck  last 365     read on
H0 ts_momentum (champion)     1,840   -93.4%      +7.9%   +0.5%     58.2%   -49.8%   -3.4    70%   30%       27%  2026-10-26
H1 mean_reversion             1,837   -88.6%     -22.5%   -0.1%     16.8%   -39.4%   -2.8     6%   95%       63%  2026-10-26
H2 vol_breakout               1,780   +33.7%     +16.8%   +1.0%     10.5%    +7.3%   +0.6    91%   10%       64%  2026-10-26
H5 swing_reversal             1,827   +73.7%     +15.5%   +0.8%      3.9%   +12.4%   +1.6    99%    1%       26%  2026-10-26
H6 relative_reversion         1,820   -75.2%     -11.6%   +0.2%      8.5%   -19.9%   -1.4    26%   75%       76%  2026-10-30
Each config is read from the first hour it could decide to the end of the history on file when it was read; days is how long that is. Over the first row's 1,840 days the basket made -51.5%. net: what the config made after costs. timing/yr: the book as it last traded each pair, less its average twin, before costs, a year. run/yr: what letting positions run between trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the share of its twins it beats before costs (a book with no timing beats about half), over the whole run and over the last 365 days. luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck. n/a: the book could not be set against twins. In sample, all of it.
```

```
bench: H0 (ts_momentum), 1,840 days from 2021-10-13 to 2026-10-26, 10 pairs
  what it made: -93.4% after costs, with 0.58 of its equity invested on average. The basket (the pairs in equal parts) made -51.5%, and the middle one of its twins -96.0% after the same costs
  twins: before costs it beats 70% of 1,000 twins over the whole run and 27% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 387 separate ones, and among that many a book with no timing does as well as this about 30% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (18 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +7.9% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.5%. Costs take 58.2% a year, so -49.8% a year is left: a yearly Sharpe ratio of -1.50 and a t of -3.4, where a t under about 2 either way cannot be told from noise. At double costs -107.9% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (80 days) -7.6%, -22.5%, -3%, 28%; 2022 +63.8%, +4.1%, -76%, 95%; 2023 -3.7%, -56.3%, +140%, 44%; 2024 +19.3%, -38.9%, +85%, 74%; 2025 -10.6%, -71.9%, -39%, 39%; 2026 (299 days) -21.6%, -65.7%, -23%, 21%
  its best and worst days: of what is left, its 9 best days carry +15.1% a year and its 9 worst -11.2%
  half the coins (twins beaten on each half, halved two ways): 48%, 56%, 57%, 60%
  nearby settings (twins beaten with every number in params moved by up to 25%): 56%, 59%, 66%, 78%, 79%, 84%, against its own 70%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 473 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,356 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -1.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: cannot be told from luck. A book with no timing at all does as well about 30% of the time.
  Bench: timing +7.9% a year before costs over 1,840 days, which beats 70% of its twins (27% of them over the last 365 days), and a book with no timing does as well 30% of the time; letting positions run added 0.5% and costs took 58.2% a year, so -49.8% is left (Sharpe -1.50, t -3.4); ahead after costs in 1 of 6 years; nearby settings beat 56%, 59%, 66%, 78%, 79%, 84% of their twins; halves of the coins 48%, 56%, 57%, 60%. In sample.
```

```
bench: H1 (mean_reversion), 1,837 days from 2021-10-16 to 2026-10-26, 10 pairs
  what it made: -88.6% after costs, with 0.32 of its equity invested on average. The basket (the pairs in equal parts) made -56.1%, and the middle one of its twins -62.0% after the same costs
  twins: before costs it beats 6% of 1,000 twins over the whole run and 63% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 231 separate ones, and among that many a book with no timing does as well as this about 95% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (16 days, SOL) or as long again as the candles, whichever is longer
  what the timing is worth: -22.5% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, took 0.1%. Costs take 16.8% a year, so -39.4% a year is left: a yearly Sharpe ratio of -1.24 and a t of -2.8, where a t under about 2 either way cannot be told from noise. At double costs -56.1% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (77 days) -3.4%, -7.8%, -13%, 41%; 2022 -45.5%, -63.1%, -76%, 8%; 2023 -34.7%, -48.0%, +140%, 9%; 2024 -30.8%, -48.9%, +85%, 18%; 2025 +0.9%, -16.4%, -39%, 52%; 2026 (299 days) +0.6%, -13.9%, -23%, 49%
  its best and worst days: of what is left, its 9 best days carry +12.6% a year and its 9 worst -16.3%
  half the coins (twins beaten on each half, halved two ways): 2%, 4%, 10%, 16%
  nearby settings (twins beaten with every number in params moved by up to 25%): 2%, 4%, 4%, 5%, 5%, 6%, against its own 6%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 128 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,353 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 1% of them (the middle one: -0.6), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 1%; a fast pass at day 60 in 2%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -22.5% a year before costs over 1,837 days, which beats 6% of its twins (63% of them over the last 365 days), and a book with no timing does as well 95% of the time; letting positions run took 0.1% and costs took 16.8% a year, so -39.4% is left (Sharpe -1.24, t -2.8); ahead after costs in 0 of 6 years; nearby settings beat 2%, 4%, 4%, 5%, 5%, 6% of their twins; halves of the coins 2%, 4%, 10%, 16%. In sample.
```

```
bench: H2 (vol_breakout), 1,780 days from 2021-12-12 to 2026-10-26, 10 pairs
  what it made: +33.7% after costs, with 0.31 of its equity invested on average. The basket (the pairs in equal parts) made -49.3%, and the middle one of its twins -44.1% after the same costs
  twins: before costs it beats 91% of 1,000 twins over the whole run and 64% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 155 separate ones, and among that many a book with no timing does as well as this about 10% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (29 days, XRP) or as long again as the candles, whichever is longer
  what the timing is worth: +16.8% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 10.5% a year, so +7.3% a year is left: a yearly Sharpe ratio of +0.26 and a t of +0.6, where a t under about 2 either way cannot be told from noise. At double costs -3.2% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +21.0%, +10.5%, -76%, 72%; 2023 +10.1%, +0.2%, +140%, 67%; 2024 +21.8%, +15.8%, +85%, 76%; 2025 +16.3%, +5.7%, -39%, 72%; 2026 (299 days) +13.7%, +4.7%, -23%, 71%
  its best and worst days: of what is left, its 9 best days carry +12.3% a year and its 9 worst -9.2%
  half the coins (twins beaten on each half, halved two ways): 84%, 96%, 98%, >99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 86%, 86%, 88%, 92%, 95%, 97%, against its own 91%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 77 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,296 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 15% of them (the middle one: +0.1), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 15%; a fast pass at day 60 in 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: at double costs nothing is left.
  Bench: timing +16.8% a year before costs over 1,780 days, which beats 91% of its twins (64% of them over the last 365 days), and a book with no timing does as well 10% of the time; letting positions run added 1.0% and costs took 10.5% a year, so +7.3% is left (Sharpe +0.26, t +0.6); ahead after costs in 5 of 5 years; nearby settings beat 86%, 86%, 88%, 92%, 95%, 97% of their twins; halves of the coins 84%, 96%, 98%, >99%. In sample.
```

```
bench: H5 (swing_reversal), 1,827 days from 2021-10-26 to 2026-10-26, 10 pairs
  what it made: +73.7% after costs, with 0.09 of its equity invested on average. The basket (the pairs in equal parts) made -60.4%, and the middle one of its twins -23.4% after the same costs
  twins: before costs it beats 99% of 1,000 twins over the whole run and 26% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 148 separate ones, and among that many a book with no timing does as well as this about 1% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (17 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +15.5% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.8%. Costs take 3.9% a year, so +12.4% a year is left: a yearly Sharpe ratio of +0.74 and a t of +1.6, where a t under about 2 either way cannot be told from noise. At double costs +8.5% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (67 days) +16.6%, +15.3%, -21%, 96%; 2022 +1.0%, -1.5%, -76%, 49%; 2023 -12.1%, -16.9%, +140%, 25%; 2024 +43.3%, +39.8%, +85%, 98%; 2025 +38.7%, +37.2%, -39%, 99%; 2026 (299 days) -9.7%, -11.7%, -23%, 10%
  its best and worst days: of what is left, its 9 best days carry +10.1% a year and its 9 worst -8.6%
  half the coins (twins beaten on each half, halved two ways): 82%, 92%, 100%, 100%
  nearby settings (twins beaten with every number in params moved by up to 25%): 68%, 92%, >99%, >99%, >99%, 100%, against its own 99%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 20 fills in 60 days (a promotion needs 30); in 9% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,343 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 26% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 25%; a fast pass at day 60 in under 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: ahead of its average twin after costs in only 3 of 6 years; over the last 365 days it beats only 26% of its twins.
  Bench: timing +15.5% a year before costs over 1,827 days, which beats 99% of its twins (26% of them over the last 365 days), and a book with no timing does as well 1% of the time; letting positions run added 0.8% and costs took 3.9% a year, so +12.4% is left (Sharpe +0.74, t +1.6); ahead after costs in 3 of 6 years; nearby settings beat 68%, 92%, >99%, >99%, >99%, 100% of their twins; halves of the coins 82%, 92%, 100%, 100%. In sample.
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
