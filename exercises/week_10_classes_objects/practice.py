"""ACU CSE 101: Week 10 Practice - Classes and Objects.

Think Python: Chapter 15
"""

import math


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y


class Rectangle:
    """Represents a rectangle.

    Attributes: width, height, corner (Point of bottom-left).
    """

    def __init__(self, corner: Point, width: float, height: float):
        self.corner = corner
        self.width = width
        self.height = height


def distance_between_points(p1: Point, p2: Point) -> float:
    """Compute the Euclidean distance between two Point objects."""
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)


def find_center(rect: Rectangle) -> Point:
    """Return a Point representing the center of the rectangle."""
    center_x = rect.corner.x + (rect.width / 2.0)
    center_y = rect.corner.y + (rect.height / 2.0)
    return Point(center_x, center_y)
