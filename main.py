#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes the single word this entry would erase from the dictionary
forever to /output/entry.txt, exactly as the program/v1 harness expects.
"""

import os

WORD = "delete"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The sealed scorer only accepts UTF-8 text of 1-77 chars, not
    # only whitespace; refuse to write anything that would fail it.
    assert 1 <= len(WORD) <= 77 and WORD.strip(), "word fails the gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
