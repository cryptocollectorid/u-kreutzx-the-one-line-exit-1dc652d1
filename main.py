#!/usr/bin/env python3
"""The One-Line Exit — a funny one-line resignation letter.

Writes the resignation letter to /output/entry.txt and prints it.
Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
"""

import os

LINE = (
    "I hereby resign, effective today — the office plant I was told to water "
    "has outlived three managers, and I will not lose to a fern."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"entry is {len(LINE)} chars, gate is 1-140")
    if "\n" in LINE:
        raise SystemExit("entry must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
