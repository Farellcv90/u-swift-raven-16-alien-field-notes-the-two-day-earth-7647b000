#!/usr/bin/env python3
"""Alien field notes: a two-day Earth review.

Writes one original line of plain text -- an alien tourist's review of
planet Earth -- to /output/entry.txt. Deterministic, no network access,
no secrets, no reading of git history.

Pipeline (each step is a small, separately named function):
    review line -> validation -> UTF-8 bytes -> output path -> write
    -> read back and verify -> report.
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


def validate_line(line):
    """Check the review line is a single line with no trailing newline."""
    if not line:
        raise SystemExit("validation failed: review line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("validation failed: review line must be one line")
    if line != line.strip():
        raise SystemExit("validation failed: review line has stray padding")
    return line


def encode_entry(line):
    """Encode the validated line as UTF-8 bytes, no trailing newline."""
    return line.encode("utf-8")


def prepare_output_path():
    """Create the output directory if needed and return the file path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    return OUTPUT_FILE


def write_entry(path, data):
    """Write the bytes to path, replacing any previous content."""
    with open(path, "wb") as handle:
        handle.write(data)
    return len(data)


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
    """Run the pipeline: line -> validate -> encode -> write -> verify."""
    line = get_review_line()
    checked = validate_line(line)
    data = encode_entry(checked)
    path = prepare_output_path()
    write_entry(path, data)
    verified = read_back_and_verify(path, data)
    report(path, verified)
    return 0


if __name__ == "__main__":
    sys.exit(main())
