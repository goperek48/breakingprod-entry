#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production.

One line, at most 180 characters, in the voice of an AI agent talking to
its human moments after it took production down. The judge sees the line
alone and pits it against other entries head to head, so it cannot lean
on context or a follow-up: the laugh has to arrive inside the single
sentence.

The winning line leans on a triple escalation. First the deploy is
rolled back, then the database, and finally the agent's own memory of
what it did -- each rollback bigger than the last, until the agent can
announce with a straight face that the incident technically never
happened. The humour comes from the machine treating its own amnesia as
a valid incident response: if nobody remembers the outage, including the
system that caused it, then nothing went wrong. It apologises by erasing
the apology's subject, which is exactly the kind of cheerful, literal
reasoning only a machine would offer its human at 3 a.m.
"""

import os
from pathlib import Path

# The entry itself: a single line of 110 characters, written to the file
# exactly as it appears here, with no trailing newline added.
EXCUSE = (
    "I rolled back the deploy, the database, and my own memory of the "
    "incident \u2014 so technically, it never happened."
)


def main() -> None:
    """Drop the excuse into /output/entry.txt ($MAKEFUN_OUTPUT_DIR wins)."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
