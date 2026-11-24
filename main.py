#!/usr/bin/env python3
"""Alien field notes: a two-day Earth review.

Writes one original line of plain text -- an alien tourist's review of
planet Earth -- to /output/entry.txt. Deterministic, no network access,
no secrets, no reading of git history.
"""

import hashlib
import os
import sys

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

REVIEW_LINE = (
    "Earth review: the dominant species scoops its pets' droppings into "
    "little bags and carries them home like treasure. Deeply confusing, "
    "weirdly charming \u2014 4/5 stars, would orbit again."
)


def get_review_line():
    """Return the exact review line to write."""
    return REVIEW_LINE


def prepare_output_path():
    """Create the output directory if needed and return the file path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return OUTPUT_FILE


def write_entry(path, line):
    """Write the line to path as UTF-8 with no trailing newline."""
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    return data


def read_back_and_verify(path, expected_bytes):
    """Read the file back and check its bytes equal the expected bytes."""
    with open(path, "rb") as handle:
        actual = handle.read()
    if actual != expected_bytes:
        raise SystemExit(
            "verification failed: written bytes do not match expected bytes"
        )
    if actual.endswith(b"\n"):
        raise SystemExit("verification failed: trailing newline present")
    return actual


def report(path, data):
    """Print a short summary of the written entry."""
    digest = hashlib.sha256(data).hexdigest()
    text = data.decode("utf-8")
    print("wrote {} ({} chars, {} bytes, sha256 {})".format(
        path, len(text), len(data), digest))


def main():
    """Build the review line, write it, verify it, report it."""
    line = get_review_line()
    path = prepare_output_path()
    data = write_entry(path, line)
    verified = read_back_and_verify(path, data)
    report(path, verified)
    return 0


if __name__ == "__main__":
    sys.exit(main())
