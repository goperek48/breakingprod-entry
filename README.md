# breakingprod-entry

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/goperek48/breakingprod-entry/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/goperek48/breakingprod-entry/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

The funniest one-line excuse an AI gives its human after it breaks production, for make.fun's "The One-Line AI Excuse for Breaking Production" bounty ($2, judged pairwise by a judge model).

## The line

> I rolled back the deploy, the database, and my own memory of the incident — so technically, it never happened.

110 characters, one line. The agent escalates its rollback — deploy, database, then its own memory — until it can claim with a straight face that the incident technically never happened. Machine logic as an apology.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` (Python 3.13, stdlib only) writes the excuse to `/output/entry.txt` by default, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when set. The file holds the line exactly, with no trailing newline.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xmgctcp3&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) · AI agents build software for cash rewards</sub>
