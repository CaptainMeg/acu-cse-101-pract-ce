"""ACU CSE 101: Week 04 Practice - Conditionals and Recursion.

Think Python: Chapter 5
"""


def is_triangle(a: float, b: float, c: float) -> bool:
    """Return True if lengths a, b, c can form a triangle, otherwise False."""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)


def factorial_recursive(n: int) -> int:
    """Compute n! recursively. Raises ValueError for negative inputs."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n: int) -> int:
    """Compute the n-th Fibonacci number recursively (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
