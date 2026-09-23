# 📖 Week 05: Iteration
**Think Python**: Chapter 7

In this module, you will practice `while` loops, `for` loops, Newton's square root method, and Collatz sequences.

---

## 🎯 Exercises

1. `mysqrt(a, epsilon=1e-7)`:
   - Implements Newton's method for calculating square root:
     $$y = \frac{x + a/x}{2}$$
   - Iterates until $|y - x| < \epsilon$.

2. `collatz_sequence_length(n)`:
   - If $n$ is even, $n \to n // 2$.
   - If $n$ is odd, $n \to 3n + 1$.
   - Returns the number of steps to reach 1 (starting at $n$).

3. `is_prime(n)`:
   - Returns `True` if $n$ is a prime number, otherwise `False`.
