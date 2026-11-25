#!/usr/bin/env python3
"""Midnight Fridge Roast — entry writer.

Writes the chosen one-line roast of a smart fridge that locks after
midnight to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then verifies the written bytes match exactly.

The entry is a fixed constant, 106 characters, one line. Why this line:
the judge weighs, first, a one-line roast of a smart fridge refusing
to open after midnight; second, a real joke with a surprising turn;
third, tightness; fourth, the midnight refusal itself as the target.
The bouncer image makes the petty rule the joke — the fridge, not the
owner, enforces a curfew — and the punchline turns on the leftovers
themselves ("filed a restraining order"), which is the surprise: the
food the fridge guards has legally barred its own owner. The quoted
bouncer line reads aloud like something said at the door, which the
brief asks for, and nothing in the line grumbles about smart homes in
general. The gate requires UTF-8 text of 1-200 characters, not only
whitespace, so this program validates length, single-line shape and
whitespace content before writing anything.
"""

import os
import sys

ENTRY = (
    "My fridge locks at midnight like a bouncer: 'Not tonight, mate "
    "\u2014 the leftovers filed a restraining order.'"
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank.

    Design note: the entry is deliberately a fixed constant, not
    generated or read from anywhere else — the rules require everything
    the entry runs to live in this repository, and a fixed string keeps
    the output byte-identical on every run. The trailing-whitespace
    check below guards the punchline: the judge reads the entry exactly
    as written, so a stray space or newline at the end would be part
    of the text and could dull the final words ("restraining order.").
    """
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside 1-200 chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # One strip check covers both ends: a padded entry would also fail
    # the read-back comparison, but rejecting it here keeps the failure
    # message about the gate, not about the write.
    if text != text.strip() or text.strip() == "":
        raise ValueError("entry must not be only whitespace or padded")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written bytes differ from entry")
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
