#!/usr/bin/env python3
"""Check that every topic in docs/COVERAGE-CHECKLIST.md is present in the plugin.

For each table row: | ID | Topic | Src | File | Check term |
the script confirms the file exists and contains the check term (case-insensitive).

Usage (from the repository root):
    python scripts/verify_coverage.py
Exit code 0 = everything covered, 1 = something missing.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "knowtific-marketing-kit"
CHECKLIST = ROOT / "docs" / "COVERAGE-CHECKLIST.md"


def resolve(short):
    short = short.strip()
    if short.startswith("ref/"):
        return PLUGIN / "skills" / "marketing-coach" / "references" / short[4:]
    if short.startswith("skill/"):
        return PLUGIN / "skills" / short[6:] / "SKILL.md"
    if short.startswith("agent/"):
        return PLUGIN / "agents" / (short[6:] + ".md")
    return ROOT / short


def normalise(text):
    # Treat different dashes and quotes as the same so terms match reliably.
    return (
        text.lower()
        .replace("–", "-")
        .replace("—", "-")
        .replace("’", "'")
        .replace("×", "x")
    )


def main():
    rows = []
    for line in CHECKLIST.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 5 or not re.match(r"^[A-Z]{1,2}\d{2}$", cells[0]):
            continue
        rows.append(cells)

    missing_file, missing_term, ok = [], [], 0
    cache = {}
    for rid, topic, src, short, term in rows:
        path = resolve(short)
        if path not in cache:
            cache[path] = normalise(path.read_text(encoding="utf-8")) if path.exists() else None
        text = cache[path]
        if text is None:
            missing_file.append((rid, short))
        elif normalise(term) not in text:
            missing_term.append((rid, topic, short, term))
        else:
            ok += 1

    total = len(rows)
    print(f"Checked {total} topics: {ok} covered, {len(missing_term)} missing terms, {len(missing_file)} missing files")
    for rid, short in missing_file:
        print(f"  MISSING FILE  {rid}: {short}")
    for rid, topic, short, term in missing_term:
        print(f"  MISSING TERM  {rid}: '{term}' not in {short}  ({topic})")
    return 0 if not (missing_file or missing_term) else 1


if __name__ == "__main__":
    sys.exit(main())
