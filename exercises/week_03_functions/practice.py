"""ACU CSE 101: Week 03 Practice - Functions.

Think Python: Chapter 3
"""

from collections.abc import Callable
import math
from typing import Any


def right_justify(s: str, width: int = 70) -> str:
    """Return string s justified with leading spaces so the last character is at column width."""
    spaces_needed = max(0, width - len(s))
    return (" " * spaces_needed) + s


def do_twice(func: Callable[[Any], Any], val: Any) -> Any:
    """Call func(val) twice and return the final result."""
    func(val)
    return func(val)


def hypotenuse(a: float, b: float) -> float:
    """Compute the length of the hypotenuse given legs a and b."""
    return math.sqrt(a**2 + b**2)
