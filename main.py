#!/usr/bin/env python3
"""u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3 entry.

Writes one line (<=200 characters) to /output/entry.txt: a funny, true
review of the most boring everyday object -- a doorstop.

Standard library only. Deterministic: the line is hardcoded, there is no
randomness, no network and no clock, so every run writes the same bytes.

The line: the doorstop's dullness is the joke. It has done exactly one
thing, holding the same door open, for six years -- no thank-you, no
raise, no day off -- and the last words sharpen it: the most loyal
employee in the house, and it isn't even paid. True of every doorstop.
Gate check: 155 characters, one line, inside the 1-200 range.
"""

import os
from pathlib import Path

ENTRY = (
    "This doorstop has held the same door open for six years. No "
    "thank-you, no raise, no day off. The most loyal employee in this "
    "house, and it isn't even paid."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
