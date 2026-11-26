#!/usr/bin/env python3
"""The Moon Gets One Star — one-star review of the Moon, <= 120 chars.

Writes a single line to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The review line is set below.
REVIEW = "One star. Drags the entire ocean around twice a day and never once asked permission. Still expects compliments."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
