"""ACU CSE 101 - Automated Unit Tests for Week 05 Practice."""

import math
import pytest
from exercises.week_05_iteration.practice import (
    collatz_sequence_length,
    is_prime,
    mysqrt,
)


def test_mysqrt():
    for val in [4.0, 9.0, 16.0, 25.0, 2.0, 0.5]:
        assert mysqrt(val) == pytest.approx(math.sqrt(val), abs=1e-6)
    assert mysqrt(0.0) == 0.0


def test_collatz_sequence_length():
    # 1 -> 0 steps
    assert collatz_sequence_length(1) == 0
    # 2 -> 1 (1 step)
    assert collatz_sequence_length(2) == 1
    # 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)
    assert collatz_sequence_length(6) == 8


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(29) is True
    assert is_prime(30) is False
