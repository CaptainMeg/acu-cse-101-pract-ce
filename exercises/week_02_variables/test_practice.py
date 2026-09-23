"""ACU CSE 101 - Automated Unit Tests for Week 02 Practice."""

import pytest

from exercises.week_02_variables.practice import (
    calculate_arrival_time,
    calculate_bookstore_cost,
    format_user_banner,
)


def test_calculate_bookstore_cost():
    assert calculate_bookstore_cost(0) == 0.0
    # 1 copy: 24.95 * 0.60 (14.97) + 3.00 = 17.97
    assert calculate_bookstore_cost(1) == pytest.approx(17.97)
    # 60 copies: 60 * 14.97 (898.20) + 3.00 + 59 * 0.75 (47.25) = 945.45
    assert calculate_bookstore_cost(60) == pytest.approx(945.45)


def test_calculate_arrival_time():
    # Start at 6:52 AM, run 1 mile easy (8m15s), 3 miles tempo (21m36s), 1 mile easy (8m15s)
    # Total run time = 38m6s -> Arrival = 7:30 AM
    hour, minute = calculate_arrival_time(6, 52, 2.0, 3.0)
    assert hour == 7
    assert minute == 30


def test_format_user_banner():
    banner = format_user_banner("PYTHON", 12, "=")
    assert len(banner) == 12
    assert "PYTHON" in banner
