"""ACU CSE 101 - Automated Unit Tests for Week 08 Practice."""

from exercises.week_08_dictionaries_tuples.practice import (
    invert_dictionary,
    most_frequent_letters,
    word_frequency,
)


def test_word_frequency():
    text = "Hello world hello python world"
    freq = word_frequency(text)
    assert freq["hello"] == 2
    assert freq["world"] == 2
    assert freq["python"] == 1


def test_invert_dictionary():
    d = {"a": 1, "b": 2, "c": 1}
    inv = invert_dictionary(d)
    assert set(inv[1]) == {"a", "c"}
    assert inv[2] == ["b"]


def test_most_frequent_letters():
    text = "banana"
    top = most_frequent_letters(text, top_n=2)
    assert top[0] == ("a", 3)
    assert top[1] == ("n", 2)
