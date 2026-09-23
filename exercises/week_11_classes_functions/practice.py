"""ACU CSE 101: Week 11 Practice - Classes and Functions.

Think Python: Chapter 16
"""


class Time:
    """Represents the time of day.

    Attributes: hour, minute, second.
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second


def time_to_int(time: Time) -> int:
    """Convert Time object to total seconds since midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds: int) -> Time:
    """Convert total seconds since midnight to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    time.hour %= 24
    return time


def add_time(t1: Time, t2: Time) -> Time:
    """Pure function: Adds two Time objects and returns a new Time object."""
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment_time(time: Time, seconds: int) -> None:
    """Modifier function: Increments Time object in-place."""
    total_seconds = time_to_int(time) + seconds
    updated = int_to_time(total_seconds)
    time.hour = updated.hour
    time.minute = updated.minute
    time.second = updated.second
