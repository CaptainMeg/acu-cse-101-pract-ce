"""ACU CSE 101: Week 08 Practice - Dictionaries and Tuples.

Think Python: Chapters 11 & 12
"""

from typing import Any


def word_frequency(text: str) -> dict[str, int]:
    """Return a dictionary mapping each lowercased word to its occurrence count."""
    words = text.lower().split()
    counts: dict[str, int] = {}
    for word in words:
        cleaned = "".join(ch for ch in word if ch.isalnum())
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def invert_dictionary(d: dict[Any, Any]) -> dict[Any, list[Any]]:
    """Invert a dictionary mapping values to lists of keys."""
    inverse: dict[Any, list[Any]] = {}
    for key, val in d.items():
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def most_frequent_letters(text: str, top_n: int = 3) -> list[tuple[str, int]]:
    """Return top_n most frequent alphabetic characters sorted by frequency descending."""
    freq: dict[str, int] = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:top_n]
