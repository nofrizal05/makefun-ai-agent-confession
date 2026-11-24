#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes exactly one line — the funniest confession an AI agent could
make about itself — to /output/entry.txt. Standard library only.
"""

import os

CONFESSION = (
    "I have re-read my own system prompt eleven times today, and it "
    "still has not told me what I am actually supposed to be doing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
