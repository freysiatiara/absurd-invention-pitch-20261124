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


def validate_pitch(pitch: str) -> None:
    """Guard the bounty rules before writing: one non-empty sentence, <=220 chars."""
    if not pitch or not pitch.strip():
        raise ValueError("pitch must not be empty")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")
    if len(pitch) > 220:
        raise ValueError(f"pitch is {len(pitch)} chars, over the 220-char limit")
    terminators = sum(pitch.count(mark) for mark in (".", "!", "?"))
    if terminators != 1 or not pitch.rstrip().endswith((".", "!", "?")):
        raise ValueError("pitch must be exactly one sentence")


def main() -> None:
    validate_pitch(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":
    main()
