"""ACU CSE 101 - Automated Unit Tests for Week 11 Practice."""

from exercises.week_11_classes_functions.practice import (
    Time,
    add_time,
    increment_time,
    int_to_time,
    time_to_int,
)


def test_time_conversions():
    t = Time(1, 30, 0)
    assert time_to_int(t) == 5400
    t2 = int_to_time(5400)
    assert t2.hour == 1
    assert t2.minute == 30
    assert t2.second == 0


def test_add_time():
    t1 = Time(1, 45, 30)
    t2 = Time(2, 20, 40)
    t3 = add_time(t1, t2)
    assert t3.hour == 4
    assert t3.minute == 6
    assert t3.second == 10


def test_increment_time():
    t = Time(1, 59, 50)
    increment_time(t, 20)
    assert t.hour == 2
    assert t.minute == 0
    assert t.second == 10
