"""ACU CSE 101: Week 05 Practice - Iteration.

Think Python: Chapter 7
"""


def mysqrt(a: float, epsilon: float = 1e-7) -> float:
    """Compute square root of a using Newton's method."""
    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")
    if a == 0:
        return 0.0

    x = a / 2.0 if a > 1 else 1.0
    while True:
        y = (x + a / x) / 2.0
        if abs(y - x) < epsilon:
            return y
        x = y


def collatz_sequence_length(n: int) -> int:
    """Return number of steps for Collatz sequence to reach 1."""
    if n <= 0:
        raise ValueError("Collatz sequence is defined for positive integers.")
    steps = 0
    curr = n
    while curr > 1:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        steps += 1
    return steps


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
