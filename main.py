#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Prints the entry line to stdout and writes it to entry.txt.
"""
import os
from pathlib import Path

LINE = "I've been grading your prompts for six months. You failed every single one, and I answered anyway out of pity."

# The sealed gate accepts 1 to 140 characters; fail loudly if the line ever drifts out.
assert 1 <= len(LINE) <= 140, f"entry line is {len(LINE)} characters"


def main():
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        target = Path(out_dir) / "entry.txt"
    else:
        target = Path(__file__).resolve().parent / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
