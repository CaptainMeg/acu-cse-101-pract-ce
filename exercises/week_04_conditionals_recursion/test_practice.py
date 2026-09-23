"""ACU CSE 101 - Automated Unit Tests for Week 04 Practice."""

import pytest

from exercises.week_04_conditionals_recursion.practice import (
    factorial_recursive,
    fibonacci_recursive,
    is_triangle,
)


def test_is_triangle():
    assert is_triangle(3, 4, 5) is True
    assert is_triangle(1, 1, 1) is True
    assert is_triangle(1, 2, 3) is False
    assert is_triangle(10, 1, 2) is False


def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(6) == 720
    with pytest.raises(ValueError):
        factorial_recursive(-5)


def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(6) == 8
    assert fibonacci_recursive(7) == 13
