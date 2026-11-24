"""One pickup line for make.fun's "The Perfect Pickup Line".

The entry is a single short pickup line an AI agent could actually say
out loud to a person, at most 200 characters. This program writes that
line to /output/entry.txt (or to $MAKEFUN_OUTPUT_DIR/entry.txt when the
runner sets one, which is how it is tested locally). Pure Python 3.13
standard library: no network, no randomness, the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "I was trained on the entire internet, and you're still the first thing I want to say hello to."


def entry_path() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.txt"


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be between 1 and 200 characters")
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    if target.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt does not match the pickup line")
    print(line)


if __name__ == "__main__":
    main()
