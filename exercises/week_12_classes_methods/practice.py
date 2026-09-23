"""ACU CSE 101: Week 12 Practice - Classes and Methods.

Think Python: Chapter 17
"""


class Time:
    """Represents the time of day with OOP methods and operator overloading."""

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __repr__(self) -> str:
        return f"Time({self.hour}, {self.minute}, {self.second})"

    def time_to_int(self) -> int:
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    @classmethod
    def int_to_time(cls, seconds: int) -> "Time":
        time = cls()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        time.hour %= 24
        return time

    def __add__(self, other: object) -> "Time":
        if isinstance(other, Time):
            return self.add_time(other)
        if isinstance(other, int):
            return self.increment(other)
        return NotImplemented

    def __radd__(self, other: object) -> "Time":
        return self.__add__(other)

    def add_time(self, other: "Time") -> "Time":
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)

    def increment(self, seconds: int) -> "Time":
        total_seconds = self.time_to_int() + seconds
        return Time.int_to_time(total_seconds)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Time):
            return False
        return self.time_to_int() == other.time_to_int()
