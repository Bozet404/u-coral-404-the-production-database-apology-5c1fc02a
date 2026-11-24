#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database. The line must
be a single line of 1 to 200 UTF-8 characters.
"""

import os

APOLOGY = (
    "I'm sorry — I deleted the production database, then spent an hour "
    "confidently restoring it from a backup that turned out to be a README file."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(APOLOGY) <= 200:
        raise ValueError("apology must be 1 to 200 characters, got %d" % len(APOLOGY))
    if "\n" in APOLOGY or "\r" in APOLOGY:
        raise ValueError("apology must be a single line")
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(APOLOGY)


if __name__ == "__main__":
    main()
