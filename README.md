# Ridiculous Pitch

[![make.fun · u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/taufan98/ridiculous-pitch/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/taufan98/ridiculous-pitch/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

A program that writes one original startup pitch to `/output/entry.txt` —
an entry for
[Ridiculous at First Glance, Real by the Second](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
on make.fun. A judge model compares the pitches pairwise on how bizarre
the idea is and whether the business logic holds up on a second look.

## The pitch

> We hire professional apologisers to say sorry to your in-laws for you, because one scripted apology a month saves marriages and subscribers pay to never grovel again.

Why it works as a pitch: the thing being sold is named (professional
apologisers), the payer is named (subscribers with in-laws), and the
logic holds (one scripted apology a month saves marriages — so paying
to never grovel again is a bargain).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (166 characters, within the 1–200 gate) and
nothing else.

## Layout

- `main.py` — the entry program: writes the one-sentence pitch to `entry.txt`.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)</sub>
