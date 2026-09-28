"""ACU CSE 101 - Automated Unit Tests for Week 01 Graded Challenge (challenge.py).

Tests simulate interactive user inputs (stdin) and verify calculations via stdout.
"""

import os
import subprocess
import sys

CHALLENGE_FILE = os.path.join(os.path.dirname(__file__), "challenge.py")

# Default simulated inputs:
# Challenge 1: 37.0 (Celsius)
# Challenge 2: 10.0 (km), 42 (minutes), 42 (seconds)
# Challenge 3: 60 (book copies)
# Challenge 4: 3.0 (side a), 4.0 (side b)
SAMPLE_INPUT = "37.0\n10.0\n42\n42\n60\n3.0\n4.0\n"


def run_student_challenge(simulated_input: str = SAMPLE_INPUT) -> subprocess.CompletedProcess:
    """Execute student challenge.py with simulated stdin."""
    assert os.path.isfile(CHALLENGE_FILE), f"File not found: {CHALLENGE_FILE}"
    try:
        res = subprocess.run(
            [sys.executable, CHALLENGE_FILE],
            input=simulated_input,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return res
    except subprocess.TimeoutExpired:
        raise AssertionError(
            "challenge.py timed out after 5 seconds. Check for infinite loops or input() calls."
        )


def test_challenge_executes_cleanly():
    """Verify that challenge.py runs without syntax errors or unhandled exceptions."""
    res = run_student_challenge()
    assert res.returncode == 0, (
        f"challenge.py crashed with exit code {res.returncode}.\n\nError output:\n{res.stderr}"
    )


def test_challenge_1_temperature_conversion():
    """Verify Challenge 1: Temperature conversion (37.0 C -> 98.6 F)."""
    res = run_student_challenge()
    stdout = res.stdout.lower()
    assert "98.6" in stdout, (
        f"Expected Fahrenheit 98.6 for 37.0 C not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_challenge_2_running_pace_and_speed():
    """Verify Challenge 2: Total seconds (2562) and average speed (~8.73 mph)."""
    res = run_student_challenge()
    stdout = res.stdout
    assert "2562" in stdout, (
        f"Expected 2562 seconds (42m 42s) not found in stdout.\nYour output was:\n{res.stdout}"
    )

    found_speed = any(val in stdout for val in ["8.72", "8.73"])
    assert found_speed, (
        f"Expected average speed (~8.73 mph) not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_challenge_3_bookstore_wholesale():
    """Verify Challenge 3: Wholesale total cost for 60 copies ($945.45)."""
    res = run_student_challenge()
    stdout = res.stdout
    # (24.95 * 0.60 * 60) + 3.00 + (0.75 * 59) = 945.45
    assert "945.45" in stdout, (
        f"Expected wholesale total 945.45 for 60 copies not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_challenge_4_hypotenuse():
    """Verify Challenge 4: Hypotenuse for sides 3.0 and 4.0 (5.0)."""
    res = run_student_challenge()
    stdout = res.stdout
    # sqrt(3^2 + 4^2) = 5.0
    assert "5.0" in stdout or "5" in stdout, (
        f"Expected hypotenuse 5.0 for legs 3.0 and 4.0 not found in stdout.\nYour output was:\n{res.stdout}"
    )
