"""ACU CSE 101: Week 09 Practice - Files and Exceptions.

Think Python: Chapter 14
"""

import os


def count_lines_and_words(filepath: str) -> tuple[int, int]:
    """Return tuple (line_count, word_count) for the file at filepath."""
    if not os.path.isfile(filepath):
        return 0, 0

    lines = 0
    words = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            lines += 1
            words += len(line.split())
    return lines, words


def find_lines_with_keyword(filepath: str, keyword: str) -> list[str]:
    """Return list of lines in file containing keyword (case-insensitive)."""
    if not os.path.isfile(filepath):
        return []

    matches = []
    kw_lower = keyword.lower()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if kw_lower in line.lower():
                matches.append(line.rstrip())
    return matches


def safe_read_number_file(filepath: str) -> float:
    """Read numbers from file lines, sum valid numbers, and skip invalid lines."""
    if not os.path.isfile(filepath):
        return 0.0

    total = 0.0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if not line_str:
                continue
            try:
                val = float(line_str)
                total += val
            except ValueError:
                continue
    return total
