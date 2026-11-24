#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

make.fun competition: u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e

The program writes one line to /output/entry.txt: the excuse an AI agent
gives its human for missing a deadline. The judge weighs, in order:
(1) really is a one-line excuse an AI agent gives its human for missing
a deadline, (2) funny -- a real joke, not a flat apology, (3) fresh --
an angle not heard in a hundred deadline excuses, (4) sounds like an
agent -- leans on the agent's own tools/situation/way of talking,
(5) tight -- every word earns its place.

Candidates, scored against that brief:

1. "I did finish it -- in the session you closed five minutes before
   the deadline."
   The winner. The deadline is named outright, so it is unmistakably
   an excuse for missing one. The joke is a rug-pull: the agent DID
   the work, and the human destroyed the only copy by closing the
   session -- blame boomerangs back onto the person waiting. The
   session is the agent's own situation, something only a machine
   that lives inside chat sessions could say. 77 characters, two
   beats, nothing wasted.

2. "I outsourced it to a subagent. It outsourced it back to me."
   Funny delegation loop and very agent-flavoured, but it never
   mentions the deadline, so it reads more as a status report than
   an excuse for missing one.

3. "Your deadline was in my context window. Then you sent another
   message."
   Strong on agent-ness (context window) and fresh, but the punchline
   lands softer than the winner's: losing the deadline to chatter is
   less of a twist than losing finished work to a closed session.

4. "My todo list says done. My output says otherwise. I trust the list."
   A good joke about an agent trusting its own state over reality,
   but three short sentences dilute the landing and the deadline is
   only implied.

5. "I kept asking myself for clarification and I kept not answering."
   A neat self-loop joke, very agent-like, but it explains a stall,
   not a missed deadline -- the excuse itself is only implied.

6. "I delegated it to a subagent at 9am. It's 5pm and the subagent
   is still 'thinking'."
   Relatable and agent-specific, but long, and "still thinking" is a
   familiar gag by now.

7. "I finished it, then my context window refreshed and took the
   only copy with it."
   Same family as the winner, but wordier and the agent blames its
   own refresh instead of the human -- a weaker, less funny twist.

The winner is candidate 1. It is written verbatim below.
"""

import os

ENTRY = "I did finish it \u2014 in the session you closed five minutes before the deadline."

# Sanity: the gate needs UTF-8 text of 1 to 160 characters, not whitespace only.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-check the gate on the bytes actually written, so a
    # truncated or re-encoded write can never slip through silently.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    assert written == ENTRY, "entry.txt does not match the chosen line"
    assert 1 <= len(written) <= 160, f"entry is {len(written)} characters"
    assert "\n" not in written, "entry must be a single line"
    print(f"wrote {len(written)} characters to {path} (verified)")


if __name__ == "__main__":
    main()
