#!/usr/bin/env python3
"""The Sock Oracle: a one-sentence absurd invention pitch.

Writes a single sentence (164 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance -- the lonely sock -- to
/output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

PITCH = (
    "The Sock Oracle: a dryer that pairs your lonely socks by reading "
    "their emotional baggage, then sends them to couples therapy before "
    "it lets them back in the drawer."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()
