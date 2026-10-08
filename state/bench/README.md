# The bench's league table

Last changed on 2026-10-08 at 02:34 UTC. The bench workflow (`python -m bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row says the day it was read on. bot/bench.py says how each figure is made.

```
config                         days      net  timing/yr  run/yr  costs/yr  left/yr      t  twins  luck  last 365     read on
H0 ts_momentum (champion)     1,821   -92.4%      +8.0%   +0.5%     58.3%   -49.8%   -3.3    71%   30%       25%  2026-10-08
H1 mean_reversion             1,818   -87.5%     -21.3%   -0.1%     16.7%   -38.0%   -2.7     7%   93%       66%  2026-10-08
H2 vol_breakout               1,761   +40.1%     +17.0%   +1.0%     10.5%    +7.4%   +0.6    91%   10%       70%  2026-10-08
H5 swing_reversal             1,808   +73.7%     +15.7%   +0.8%      4.0%   +12.6%   +1.6    99%    2%       28%  2026-10-08
H4 ts_momentum                1,798   +69.9%     +22.9%   +1.0%      9.0%   +14.9%   +1.0    96%    5%       81%  2026-10-08
Each config is read from the first hour it could decide to the end of the history on file when it was read; days is how long that is. Over the first row's 1,821 days the basket made -44.4%. net: what the config made after costs. timing/yr: the book as it last traded each pair, less its average twin, before costs, a year. run/yr: what letting positions run between trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the share of its twins it beats before costs (a book with no timing beats about half), over the whole run and over the last 365 days. luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck. n/a: the book could not be set against twins. In sample, all of it.
```

```
bench: H0 (ts_momentum), 1,821 days from 2021-10-13 to 2026-10-08, 10 pairs
  what it made: -92.4% after costs, with 0.59 of its equity invested on average. The basket (the pairs in equal parts) made -44.4%, and the middle one of its twins -95.4% after the same costs
  twins: before costs it beats 71% of 1,000 twins over the whole run and 25% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 392 separate ones, and among that many a book with no timing does as well as this about 30% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (18 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +8.0% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.5%. Costs take 58.3% a year, so -49.8% a year is left: a yearly Sharpe ratio of -1.49 and a t of -3.3, where a t under about 2 either way cannot be told from noise. At double costs -108.0% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (80 days) -7.3%, -22.2%, -3%, 29%; 2022 +63.4%, +3.7%, -76%, 95%; 2023 -5.0%, -57.6%, +140%, 41%; 2024 +15.2%, -43.1%, +85%, 69%; 2025 -10.4%, -71.6%, -39%, 39%; 2026 (280 days) -16.1%, -57.6%, -12%, 27%
  its best and worst days: of what is left, its 9 best days carry +15.3% a year and its 9 worst -11.3%
  half the coins (twins beaten on each half, halved two ways): 53%, 57%, 58%, 63%
  nearby settings (twins beaten with every number in params moved by up to 25%): 54%, 56%, 78%, 85%, 86%, 88%, against its own 71%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 475 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,337 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -1.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: cannot be told from luck. A book with no timing at all does as well about 30% of the time.
  Bench: timing +8.0% a year before costs over 1,821 days, which beats 71% of its twins (25% of them over the last 365 days), and a book with no timing does as well 30% of the time; letting positions run added 0.5% and costs took 58.3% a year, so -49.8% is left (Sharpe -1.49, t -3.3); ahead after costs in 1 of 6 years; nearby settings beat 54%, 56%, 78%, 85%, 86%, 88% of their twins; halves of the coins 53%, 57%, 58%, 63%. In sample.
```

```
bench: H1 (mean_reversion), 1,818 days from 2021-10-16 to 2026-10-08, 10 pairs
  what it made: -87.5% after costs, with 0.32 of its equity invested on average. The basket (the pairs in equal parts) made -49.8%, and the middle one of its twins -62.2% after the same costs
  twins: before costs it beats 7% of 1,000 twins over the whole run and 66% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 220 separate ones, and among that many a book with no timing does as well as this about 93% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (16 days, SOL) or as long again as the candles, whichever is longer
  what the timing is worth: -21.3% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, took 0.1%. Costs take 16.7% a year, so -38.0% a year is left: a yearly Sharpe ratio of -1.20 and a t of -2.7, where a t under about 2 either way cannot be told from noise. At double costs -54.7% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (77 days) -4.0%, -8.3%, -13%, 41%; 2022 -43.3%, -60.9%, -76%, 9%; 2023 -33.6%, -46.9%, +140%, 11%; 2024 -29.0%, -47.1%, +85%, 19%; 2025 +0.7%, -16.5%, -39%, 51%; 2026 (280 days) +3.3%, -9.9%, -12%, 57%
  its best and worst days: of what is left, its 9 best days carry +12.9% a year and its 9 worst -16.6%
  half the coins (twins beaten on each half, halved two ways): 4%, 4%, 6%, 16%
  nearby settings (twins beaten with every number in params moved by up to 25%): <1%, 2%, 4%, 4%, 6%, 6%, against its own 7%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 127 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,334 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 1% of them (the middle one: -0.6), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 1%; a fast pass at day 60 in 2%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -21.3% a year before costs over 1,818 days, which beats 7% of its twins (66% of them over the last 365 days), and a book with no timing does as well 93% of the time; letting positions run took 0.1% and costs took 16.7% a year, so -38.0% is left (Sharpe -1.20, t -2.7); ahead after costs in 0 of 6 years; nearby settings beat <1%, 2%, 4%, 4%, 6%, 6% of their twins; halves of the coins 4%, 4%, 6%, 16%. In sample.
```

```
bench: H2 (vol_breakout), 1,761 days from 2021-12-12 to 2026-10-08, 10 pairs
  what it made: +40.1% after costs, with 0.31 of its equity invested on average. The basket (the pairs in equal parts) made -41.9%, and the middle one of its twins -43.2% after the same costs
  twins: before costs it beats 91% of 1,000 twins over the whole run and 70% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 154 separate ones, and among that many a book with no timing does as well as this about 10% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (29 days, XRP) or as long again as the candles, whichever is longer
  what the timing is worth: +17.0% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 10.5% a year, so +7.4% a year is left: a yearly Sharpe ratio of +0.26 and a t of +0.6, where a t under about 2 either way cannot be told from noise. At double costs -3.1% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +21.6%, +11.1%, -76%, 72%; 2023 +10.8%, +0.9%, +140%, 68%; 2024 +20.9%, +15.0%, +85%, 76%; 2025 +16.0%, +5.5%, -39%, 72%; 2026 (280 days) +13.3%, +4.6%, -12%, 71%
  its best and worst days: of what is left, its 9 best days carry +12.4% a year and its 9 worst -9.4%
  half the coins (twins beaten on each half, halved two ways): 90%, 94%, 98%, >99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 85%, 86%, 86%, 94%, 96%, 96%, against its own 91%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 77 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,277 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 15% of them (the middle one: +0.1), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 15%; a fast pass at day 60 in 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: at double costs nothing is left.
  Bench: timing +17.0% a year before costs over 1,761 days, which beats 91% of its twins (70% of them over the last 365 days), and a book with no timing does as well 10% of the time; letting positions run added 1.0% and costs took 10.5% a year, so +7.4% is left (Sharpe +0.26, t +0.6); ahead after costs in 5 of 5 years; nearby settings beat 85%, 86%, 86%, 94%, 96%, 96% of their twins; halves of the coins 90%, 94%, 98%, >99%. In sample.
```

```
bench: H5 (swing_reversal), 1,808 days from 2021-10-26 to 2026-10-08, 10 pairs
  what it made: +73.7% after costs, with 0.09 of its equity invested on average. The basket (the pairs in equal parts) made -54.6%, and the middle one of its twins -22.9% after the same costs
  twins: before costs it beats 99% of 1,000 twins over the whole run and 28% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 136 separate ones, and among that many a book with no timing does as well as this about 2% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (17 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +15.7% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.8%. Costs take 4.0% a year, so +12.6% a year is left: a yearly Sharpe ratio of +0.74 and a t of +1.6, where a t under about 2 either way cannot be told from noise. At double costs +8.7% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (67 days) +16.8%, +15.6%, -21%, 95%; 2022 +1.5%, -1.0%, -76%, 52%; 2023 -12.5%, -17.2%, +140%, 27%; 2024 +43.4%, +39.9%, +85%, 97%; 2025 +39.2%, +37.7%, -39%, 99%; 2026 (280 days) -10.6%, -12.5%, -12%, 10%
  its best and worst days: of what is left, its 9 best days carry +10.2% a year and its 9 worst -8.7%
  half the coins (twins beaten on each half, halved two ways): 82%, 88%, 99%, 99%
  nearby settings (twins beaten with every number in params moved by up to 25%): 74%, 92%, 98%, 99%, >99%, >99%, against its own 99%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 20 fills in 60 days (a promotion needs 30); in 9% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,324 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 27% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 25%; a fast pass at day 60 in under 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: ahead of its average twin after costs in only 3 of 6 years; over the last 365 days it beats only 28% of its twins.
  Bench: timing +15.7% a year before costs over 1,808 days, which beats 99% of its twins (28% of them over the last 365 days), and a book with no timing does as well 2% of the time; letting positions run added 0.8% and costs took 4.0% a year, so +12.6% is left (Sharpe +0.74, t +1.6); ahead after costs in 3 of 6 years; nearby settings beat 74%, 92%, 98%, 99%, >99%, >99% of their twins; halves of the coins 82%, 88%, 99%, 99%. In sample.
```

```
bench: H4 (ts_momentum), 1,798 days from 2021-11-05 to 2026-10-08, 10 pairs
  what it made: +69.9% after costs, with 0.51 of its equity invested on average. The basket (the pairs in equal parts) made -57.1%, and the middle one of its twins -52.5% after the same costs
  twins: before costs it beats 96% of 1,000 twins over the whole run and 81% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 62 separate ones, and among that many a book with no timing does as well as this about 5% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (73 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +22.9% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 9.0% a year, so +14.9% a year is left: a yearly Sharpe ratio of +0.45 and a t of +1.0, where a t under about 2 either way cannot be told from noise. At double costs +5.8% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (57 days) -5.5%, -6.7%, -25%, 30%; 2022 +22.3%, +17.1%, -76%, 72%; 2023 +48.6%, +41.7%, +140%, 94%; 2024 +33.2%, +23.4%, +85%, 83%; 2025 -0.6%, -11.5%, -39%, 50%; 2026 (280 days) +14.7%, +9.2%, -12%, 69%
  its best and worst days: of what is left, its 9 best days carry +13.6% a year and its 9 worst -13.4%
  half the coins (twins beaten on each half, halved two ways): 91%, 95%, 96%, 98%
  nearby settings (twins beaten with every number in params moved by up to 25%): 83%, 85%, 88%, 92%, 96%, 96%, against its own 96%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 78 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,314 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 10% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 10%; a fast pass at day 60 in 3%
  Reading: it beats most of its twins, with something left after costs, in most years and at double costs; 4 of 4 halves of the coins and 6 of 6 nearby settings beat 75% of their own twins or more. Worth a slot on this evidence, all of which is in sample.
  Bench: timing +22.9% a year before costs over 1,798 days, which beats 96% of its twins (81% of them over the last 365 days), and a book with no timing does as well 5% of the time; letting positions run added 1.0% and costs took 9.0% a year, so +14.9% is left (Sharpe +0.45, t +1.0); ahead after costs in 4 of 6 years; nearby settings beat 83%, 85%, 88%, 92%, 96%, 96% of their twins; halves of the coins 91%, 95%, 96%, 98%. In sample.
```
