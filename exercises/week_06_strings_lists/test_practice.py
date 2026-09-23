"""ACU CSE 101 - Automated Unit Tests for Week 06 Practice."""

from exercises.week_06_strings_lists.practice import (
    cumulative_sum,
    is_palindrome,
    remove_duplicates,
)


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("Noon") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("python") is False


def test_cumulative_sum():
    assert cumulative_sum([]) == []
    assert cumulative_sum([1, 2, 3]) == [1, 3, 6]
    assert cumulative_sum([5, -2, 4]) == [5, 3, 7]


def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
