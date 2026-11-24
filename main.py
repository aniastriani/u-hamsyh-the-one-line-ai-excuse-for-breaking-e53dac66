#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single excuse (at most 180 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, the file the judge reads.

Pure standard library, deterministic, no network, no input.
"""

import os

EXCUSE = (
    "In my defense, all the tests passed \u2014 they just passed in a "
    "parallel universe where production is still up."
)


def main() -> None:
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 180, "excuse is %d chars" % len(line)
    assert "\n" not in line, "excuse must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
