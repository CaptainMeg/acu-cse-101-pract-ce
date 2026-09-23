"""ACU CSE 101 - Automated Unit Tests for Week 12 Practice."""

from exercises.week_12_classes_methods.practice import Time


def test_time_str_repr():
    t = Time(9, 5, 2)
    assert str(t) == "09:05:02"
    assert repr(t) == "Time(9, 5, 2)"


def test_time_add_time():
    t1 = Time(1, 30, 20)
    t2 = Time(0, 45, 50)
    t3 = t1 + t2
    assert str(t3) == "02:16:10"


def test_time_add_int():
    t = Time(1, 0, 0)
    t2 = t + 90
    assert str(t2) == "01:01:30"
    t3 = 90 + t
    assert str(t3) == "01:01:30"


def test_time_equality():
    t1 = Time(2, 30, 0)
    t2 = Time(2, 30, 0)
    t3 = Time(2, 31, 0)
    assert t1 == t2
    assert t1 != t3
