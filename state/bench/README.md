# The bench's league table

Last changed on 2026-10-19 at 00:54 UTC. The bench workflow (`python -m bot.bench --all --save`) writes it again only when a reading or a line under `Not read` changes; each row says the day it was read on. bot/bench.py says how each figure is made.

```
config                         days      net  timing/yr  run/yr  costs/yr  left/yr      t  twins  luck  last 365     read on
H0 ts_momentum (champion)     1,832   -93.2%      +8.3%   +0.5%     58.3%   -49.5%   -3.3    69%   31%       22%  2026-10-19
H1 mean_reversion             1,829   -88.8%     -22.7%   -0.1%     16.8%   -39.5%   -2.8     6%   95%       52%  2026-10-19
H2 vol_breakout               1,772   +40.1%     +17.8%   +1.0%     10.5%    +8.3%   +0.7    92%    9%       66%  2026-10-19
H5 swing_reversal             1,819   +73.7%     +15.6%   +0.8%      3.9%   +12.5%   +1.6    99%    1%       22%  2026-10-19
H6 relative_reversion         1,806   -72.4%     -10.7%   +0.1%      8.5%   -19.0%   -1.3    28%   72%       75%  2026-10-15
Each config is read from the first hour it could decide to the end of the history on file when it was read; days is how long that is. Over the first row's 1,832 days the basket made -50.2%. net: what the config made after costs. timing/yr: the book as it last traded each pair, less its average twin, before costs, a year. run/yr: what letting positions run between trades added, which a twin does not do. costs/yr: what its fills took. left/yr: timing plus run less costs. t: of what is left, day by day; under about 2 either way cannot be told from noise. twins: the share of its twins it beats before costs (a book with no timing beats about half), over the whole run and over the last 365 days. luck: how often a book with no timing does as well among its twins as this one did; over 10%, it cannot be told from luck. n/a: the book could not be set against twins. In sample, all of it.
```

```
bench: H0 (ts_momentum), 1,832 days from 2021-10-13 to 2026-10-18, 10 pairs
  what it made: -93.2% after costs, with 0.58 of its equity invested on average. The basket (the pairs in equal parts) made -50.2%, and the middle one of its twins -95.8% after the same costs
  twins: before costs it beats 69% of 1,000 twins over the whole run and 22% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 364 separate ones, and among that many a book with no timing does as well as this about 31% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (18 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +8.3% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.5%. Costs take 58.3% a year, so -49.5% a year is left: a yearly Sharpe ratio of -1.48 and a t of -3.3, where a t under about 2 either way cannot be told from noise. At double costs -107.7% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (80 days) -6.4%, -21.4%, -3%, 32%; 2022 +64.3%, +4.6%, -76%, 95%; 2023 -4.8%, -57.4%, +140%, 42%; 2024 +19.0%, -39.3%, +85%, 71%; 2025 -11.1%, -72.4%, -39%, 40%; 2026 (291 days) -19.3%, -62.6%, -22%, 24%
  its best and worst days: of what is left, its 9 best days carry +15.4% a year and its 9 worst -11.3%
  half the coins (twins beaten on each half, halved two ways): 48%, 58%, 58%, 59%
  nearby settings (twins beaten with every number in params moved by up to 25%): 52%, 58%, 74%, 76%, 83%, 83%, against its own 69%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 474 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,348 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -1.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: cannot be told from luck. A book with no timing at all does as well about 31% of the time.
  Bench: timing +8.3% a year before costs over 1,832 days, which beats 69% of its twins (22% of them over the last 365 days), and a book with no timing does as well 31% of the time; letting positions run added 0.5% and costs took 58.3% a year, so -49.5% is left (Sharpe -1.48, t -3.3); ahead after costs in 1 of 6 years; nearby settings beat 52%, 58%, 74%, 76%, 83%, 83% of their twins; halves of the coins 48%, 58%, 58%, 59%. In sample.
```

```
bench: H1 (mean_reversion), 1,829 days from 2021-10-16 to 2026-10-18, 10 pairs
  what it made: -88.8% after costs, with 0.32 of its equity invested on average. The basket (the pairs in equal parts) made -55.0%, and the middle one of its twins -62.6% after the same costs
  twins: before costs it beats 6% of 1,000 twins over the whole run and 52% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 239 separate ones, and among that many a book with no timing does as well as this about 95% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (16 days, SOL) or as long again as the candles, whichever is longer
  what the timing is worth: -22.7% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, took 0.1%. Costs take 16.8% a year, so -39.5% a year is left: a yearly Sharpe ratio of -1.25 and a t of -2.8, where a t under about 2 either way cannot be told from noise. At double costs -56.3% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (77 days) -3.5%, -7.8%, -13%, 41%; 2022 -43.7%, -61.2%, -76%, 12%; 2023 -34.4%, -47.6%, +140%, 9%; 2024 -30.2%, -48.3%, +85%, 17%; 2025 +1.9%, -15.4%, -39%, 52%; 2026 (291 days) -3.7%, -17.8%, -22%, 42%
  its best and worst days: of what is left, its 9 best days carry +12.6% a year and its 9 worst -16.3%
  half the coins (twins beaten on each half, halved two ways): 2%, 3%, 6%, 12%
  nearby settings (twins beaten with every number in params moved by up to 25%): 2%, 3%, 4%, 4%, 5%, 7%, against its own 6%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 128 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,345 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 1% of them (the middle one: -0.6), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 1%; a fast pass at day 60 in 2%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -22.7% a year before costs over 1,829 days, which beats 6% of its twins (52% of them over the last 365 days), and a book with no timing does as well 95% of the time; letting positions run took 0.1% and costs took 16.8% a year, so -39.5% is left (Sharpe -1.25, t -2.8); ahead after costs in 0 of 6 years; nearby settings beat 2%, 3%, 4%, 4%, 5%, 7% of their twins; halves of the coins 2%, 3%, 6%, 12%. In sample.
```

```
bench: H2 (vol_breakout), 1,772 days from 2021-12-12 to 2026-10-18, 10 pairs
  what it made: +40.1% after costs, with 0.31 of its equity invested on average. The basket (the pairs in equal parts) made -48.0%, and the middle one of its twins -47.0% after the same costs
  twins: before costs it beats 92% of 1,000 twins over the whole run and 66% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 154 separate ones, and among that many a book with no timing does as well as this about 9% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (29 days, XRP) or as long again as the candles, whichever is longer
  what the timing is worth: +17.8% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 1.0%. Costs take 10.5% a year, so +8.3% a year is left: a yearly Sharpe ratio of +0.30 and a t of +0.7, where a t under about 2 either way cannot be told from noise. At double costs -2.2% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2022 +20.7%, +10.2%, -76%, 73%; 2023 +11.5%, +1.6%, +140%, 69%; 2024 +21.0%, +15.1%, +85%, 78%; 2025 +16.5%, +6.0%, -39%, 72%; 2026 (291 days) +17.4%, +8.8%, -22%, 76%
  its best and worst days: of what is left, its 9 best days carry +12.3% a year and its 9 worst -9.3%
  half the coins (twins beaten on each half, halved two ways): 84%, 95%, 98%, 100%
  nearby settings (twins beaten with every number in params moved by up to 25%): 88%, 88%, 88%, 93%, 95%, 96%, against its own 92%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 77 fills in 60 days (a promotion needs 30); it finished a trade of its own in every 60 day window
  had a test begun on each day from a year into the run (1,288 windows of 120 days, which overlap: about 11 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 15% of them (the middle one: +0.1), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 15%; a fast pass at day 60 in 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: at double costs nothing is left.
  Bench: timing +17.8% a year before costs over 1,772 days, which beats 92% of its twins (66% of them over the last 365 days), and a book with no timing does as well 9% of the time; letting positions run added 1.0% and costs took 10.5% a year, so +8.3% is left (Sharpe +0.30, t +0.7); ahead after costs in 5 of 5 years; nearby settings beat 88%, 88%, 88%, 93%, 95%, 96% of their twins; halves of the coins 84%, 95%, 98%, 100%. In sample.
```

```
bench: H5 (swing_reversal), 1,819 days from 2021-10-26 to 2026-10-18, 10 pairs
  what it made: +73.7% after costs, with 0.09 of its equity invested on average. The basket (the pairs in equal parts) made -59.4%, and the middle one of its twins -23.0% after the same costs
  twins: before costs it beats 99% of 1,000 twins over the whole run and 22% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 147 separate ones, and among that many a book with no timing does as well as this about 1% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (17 days, ETH) or as long again as the candles, whichever is longer
  what the timing is worth: +15.6% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.8%. Costs take 3.9% a year, so +12.5% a year is left: a yearly Sharpe ratio of +0.74 and a t of +1.6, where a t under about 2 either way cannot be told from noise. At double costs +8.6% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (67 days) +16.3%, +15.1%, -21%, 95%; 2022 +1.3%, -1.1%, -76%, 50%; 2023 -12.5%, -17.3%, +140%, 28%; 2024 +43.3%, +39.9%, +85%, 98%; 2025 +39.0%, +37.5%, -39%, over 99%; 2026 (291 days) -9.6%, -11.6%, -22%, 10%
  its best and worst days: of what is left, its 9 best days carry +10.1% a year and its 9 worst -8.7%
  half the coins (twins beaten on each half, halved two ways): 82%, 94%, >99%, 100%
  nearby settings (twins beaten with every number in params moved by up to 25%): 78%, 90%, 99%, 99%, 100%, 100%, against its own 99%
  the clock: nothing in its code names it, and its targets do not move with it (asked at 24 hours of the history, with the clock moved three ways)
  under rule 1: about 20 fills in 60 days (a promotion needs 30); in 9% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,335 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 27% of them (the middle one: +0.2), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 25%; a fast pass at day 60 in under 1%
  Reading: it beats most of its twins over the whole run, with something left after costs. Weak spots: ahead of its average twin after costs in only 3 of 6 years; over the last 365 days it beats only 22% of its twins.
  Bench: timing +15.6% a year before costs over 1,819 days, which beats 99% of its twins (22% of them over the last 365 days), and a book with no timing does as well 1% of the time; letting positions run added 0.8% and costs took 3.9% a year, so +12.5% is left (Sharpe +0.74, t +1.6); ahead after costs in 3 of 6 years; nearby settings beat 78%, 90%, 99%, 99%, 100%, 100% of their twins; halves of the coins 82%, 94%, >99%, 100%. In sample.
```

```
bench: H6 (relative_reversion), 1,806 days from 2021-11-05 to 2026-10-15, 10 pairs
  what it made: -72.4% after costs, with 0.48 of its equity invested on average. The basket (the pairs in equal parts) made -59.8%, and the middle one of its twins -55.9% after the same costs
  twins: before costs it beats 28% of 1,000 twins over the whole run and 75% over the last 365 days. A twin is the same book slid 30 days or more later: the same positions on the same coins for as long, with nothing left of when they were taken. A book with no timing beats about half. Twins slid a few days apart are nearly one book: these are worth about 88 separate ones, and among that many a book with no timing does as well as this about 72% of the time. No twin holds what the book took in the 180 days after the hour in hand: the 90 days of candles a strategy is handed, and then the longest it was in any one pair (63 days, DOT) or as long again as the candles, whichever is longer
  what the timing is worth: -10.7% a year before costs, the book as it last traded each pair less its average twin. Letting positions run between trades, which a twin does not, added 0.1%. Costs take 8.5% a year, so -19.0% a year is left: a yearly Sharpe ratio of -0.58 and a t of -1.3, where a t under about 2 either way cannot be told from noise. At double costs -27.5% is left
  by year (timing before costs, what is left after them, the basket, twins beaten): 2021 (57 days) +7.1%, +5.7%, -25%, 66%; 2022 -4.6%, -13.8%, -76%, 44%; 2023 -17.8%, -24.0%, +140%, 28%; 2024 -21.0%, -31.2%, +85%, 28%; 2025 -44.7%, -53.3%, -39%, 10%; 2026 (288 days) +28.2%, +22.7%, -18%, 90%
  its best and worst days: of what is left, its 9 best days carry +11.9% a year and its 9 worst -17.9%
  half the coins (twins beaten on each half, halved two ways): 22%, 32% (2 could not be replayed)
  nearby settings (twins beaten with every number in params moved by up to 25%): 26%, 31%, 33%, 38%, 42%, 60%, against its own 28%
  the clock: its code names the candles' time column or asks the time. With the clock moved (by 27, 54, 81, 108, 135, 162 hours) it beats 34%, 42%, 48%, 57%, 66%, 93% of its twins, against its own 28%
  under rule 1: about 55 fills in 60 days (a promotion needs 30); in 1% of 60 day windows it finished no trade of its own, and a test that began in one of those is killed at its look (0% of 120 day windows)
  had a test begun on each day from a year into the run (1,322 windows of 120 days, which overlap: about 12 fit end to end): its daily skill t, as the live rule takes it, was 1.0 or more at day 120 in 2% of them (the middle one: -0.5), and it had all three counts a promotion asks for (a trade of its own by day 60, 30 fills, that t) in 2%; a fast pass at day 60 in 0%
  Reading: no sign of timing. Before costs, most of its own twins did better: the same positions, taken at other times.
  Bench: timing -10.7% a year before costs over 1,806 days, which beats 28% of its twins (75% of them over the last 365 days), and a book with no timing does as well 72% of the time; letting positions run added 0.1% and costs took 8.5% a year, so -19.0% is left (Sharpe -0.58, t -1.3); ahead after costs in 2 of 6 years; nearby settings beat 26%, 31%, 33%, 38%, 42%, 60% of their twins; halves of the coins 22%, 32% (2 could not be replayed). In sample.
```
