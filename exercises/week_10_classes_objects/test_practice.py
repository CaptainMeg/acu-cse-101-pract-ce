"""ACU CSE 101 - Automated Unit Tests for Week 10 Practice."""

import pytest
from exercises.week_10_classes_objects.practice import (
    Point,
    Rectangle,
    distance_between_points,
    find_center,
)


def test_distance_between_points():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert distance_between_points(p1, p2) == pytest.approx(5.0)

    p3 = Point(1, 1)
    p4 = Point(1, 1)
    assert distance_between_points(p3, p4) == pytest.approx(0.0)


def test_find_center():
    corner = Point(0, 0)
    box = Rectangle(corner, 100, 200)
    center = find_center(box)
    assert center.x == 50.0
    assert center.y == 100.0
