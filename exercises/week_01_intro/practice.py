"""ACU CSE 101: Week 01 Practice - The Way of the Program & Variables.

Think Python: Chapters 1 & 2
"""

import math


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit.

    Formula: F = C * (9/5) + 32
    """
    # TODO: Implement formula and return the result
    return (celsius * 9 / 5) + 32


def calculate_total_seconds(hours: int, minutes: int, seconds: int) -> int:
    """Convert hours, minutes, and seconds into total seconds."""
    # TODO: Implement total seconds calculation
    return hours * 3600 + minutes * 60 + seconds


def compute_sphere_volume(radius: float) -> float:
    """Compute the volume of a sphere given its radius."""
    # TODO: Implement volume: (4/3) * pi * (r^3)
    return (4 / 3) * math.pi * (radius**3)
