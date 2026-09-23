"""ACU CSE 101 - Automated Unit Tests for Week 01 Practice."""

import math

import pytest

from exercises.week_01_intro.practice import (
    calculate_total_seconds,
    compute_sphere_volume,
    convert_celsius_to_fahrenheit,
)


def test_convert_celsius_to_fahrenheit():
    assert convert_celsius_to_fahrenheit(0.0) == pytest.approx(32.0)
    assert convert_celsius_to_fahrenheit(100.0) == pytest.approx(212.0)
    assert convert_celsius_to_fahrenheit(37.0) == pytest.approx(98.6)
    assert convert_celsius_to_fahrenheit(-40.0) == pytest.approx(-40.0)


def test_calculate_total_seconds():
    assert calculate_total_seconds(0, 0, 0) == 0
    assert calculate_total_seconds(1, 0, 0) == 3600
    assert calculate_total_seconds(0, 1, 30) == 90
    assert calculate_total_seconds(2, 45, 15) == 9915


def test_compute_sphere_volume():
    assert compute_sphere_volume(0.0) == pytest.approx(0.0)
    assert compute_sphere_volume(5.0) == pytest.approx((4 / 3) * math.pi * 125)
    assert compute_sphere_volume(1.0) == pytest.approx(4.18879, rel=1e-3)
