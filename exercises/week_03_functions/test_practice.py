"""ACU CSE 101 - Automated Unit Tests for Week 03 Practice."""

import pytest
from exercises.week_03_functions.practice import (
    do_twice,
    hypotenuse,
    right_justify,
)


def test_right_justify():
    res = right_justify("monty", width=70)
    assert len(res) == 70
    assert res.endswith("monty")
    assert res.startswith(" ")


def test_do_twice():
    counter = []

    def append_val(x):
        counter.append(x)
        return len(counter)

    final_len = do_twice(append_val, "apple")
    assert len(counter) == 2
    assert final_len == 2


def test_hypotenuse():
    assert hypotenuse(3.0, 4.0) == pytest.approx(5.0)
    assert hypotenuse(5.0, 12.0) == pytest.approx(13.0)
