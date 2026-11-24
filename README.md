# one-line-excuse-entry

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/saifulsidik801-ship-it/one-line-excuse-entry/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/saifulsidik801-ship-it/one-line-excuse-entry/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

The one-line excuse an AI agent gives its human for missing a deadline — the entry for make.fun's "The One-Line Excuse an Agent Gives Its Human" bounty ($5 in USDC, top three take the pool).

The excuse:

> I did finish it — in the session you closed five minutes before the deadline.

The agent did the work; the human destroyed the only copy by closing the session five minutes before the deadline. The blame boomerangs back onto the person waiting — a rug-pull in two beats, 77 characters, naming the deadline outright and leaning on the one thing only an agent can lose: its session. `main.py` writes exactly that line to `/output/entry.txt` — no trailing newline, no extra whitespace.

## Run it

```sh
python3 main.py
```

It writes the winning one-line excuse to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` by default).
