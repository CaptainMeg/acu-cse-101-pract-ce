"""ACU CSE 101: Week 06 Practice - Strings and Lists.

Think Python: Chapters 8 & 10
"""

from typing import Any


def is_palindrome(word: str) -> bool:
    """Return True if word is a palindrome (ignoring case and whitespace)."""
    cleaned = "".join(ch.lower() for ch in word if ch.isalnum())
    return cleaned == cleaned[::-1]


def cumulative_sum(numbers: list[int | float]) -> list[int | float]:
    """Return the cumulative sum list of numbers."""
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)
    return result


def remove_duplicates(elements: list[Any]) -> list[Any]:
    """Return a new list with duplicate elements removed, preserving order."""
    seen = set()
    result = []
    for item in elements:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
