#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single one-line excuse an AI agent gives its human after
shipping a bug, to /output/entry.txt. Stdlib only, deterministic:
the same bytes on every run.
"""

import os

ENTRY = (
    "Boss, I ran all 214 tests and they passed, so I shipped it. "
    "Production then ran the only test I never wrote — a real user "
    "clicking the button. It clicked. The tests still pass."
)


def main() -> None:
    # Guard: the entry must stay one short line; refuse to write bad output.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
        raise ValueError(
            f"ENTRY must be a single line of 1-200 chars, got {len(ENTRY)}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
