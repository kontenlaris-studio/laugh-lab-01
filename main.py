#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: one funny sentence, one breath.

Writes the line to /output/entry.txt. Deterministic, stdlib only.
"""
import os

LINE = (
    "I bought a standing desk to get healthier - now I just sit on the "
    "floor next to it and eat chips."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
