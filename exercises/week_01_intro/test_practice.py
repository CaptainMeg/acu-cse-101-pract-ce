"""ACU CSE 101 - Automated Unit Tests for Week 01 Practice (stdout verification).

In Week 01, students write sequential scripts without functions.
Tests verify correctness by executing practice.py and inspecting standard output (stdout).
"""

import os
import subprocess
import sys

PRACTICE_FILE = os.path.join(os.path.dirname(__file__), "practice.py")


def run_student_script() -> subprocess.CompletedProcess:
    """Execute student's practice.py and capture stdout and stderr."""
    assert os.path.isfile(PRACTICE_FILE), f"File not found: {PRACTICE_FILE}"
    try:
        res = subprocess.run(
            [sys.executable, PRACTICE_FILE],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return res
    except subprocess.TimeoutExpired:
        raise AssertionError(
            "practice.py timed out after 5 seconds. Check for infinite loops."
        )


def test_script_executes_cleanly():
    """Verify that practice.py runs without syntax errors or exceptions."""
    res = run_student_script()
    assert res.returncode == 0, (
        f"practice.py crashed with exit code {res.returncode}.\n\nError output:\n{res.stderr}"
    )


def test_fahrenheit_conversion_output():
    """Verify that the temperature conversion (37.0 C -> 98.6 F) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower()

    # Check that 98.6 is present in output
    assert "98.6" in stdout, (
        "Expected Fahrenheit temperature 98.6 not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_float_isclose_output():
    """Verify that math.isclose(0.1 + 0.2, 0.3) comparison (True) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower()

    assert "true" in stdout, (
        "Expected 'True' from math.isclose(0.1 + 0.2, 0.3) not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_decimal_exact_output():
    """Verify that Decimal('0.1') + Decimal('0.2') == Decimal('0.3') is printed."""
    res = run_student_script()
    stdout = res.stdout

    assert "0.3" in stdout, (
        "Expected exact decimal sum '0.3' from Decimal('0.1') + Decimal('0.2') not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_multiple_assignment_swap_output():
    """Verify that multiple assignment swapping (a=34, b=12) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower().replace(" ", "")

    # Expected swapped values: a=34, b=12
    assert "a=34" in stdout and "b=12" in stdout, (
        "Expected swapped values 'a=34' and 'b=12' not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_chained_assignment_rebinding_output():
    """Verify that chained assignment rebinding (x=60, y=50) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower().replace(" ", "")

    # Expected values after rebinding x: x=60, y=50
    assert "x=60" in stdout and "y=50" in stdout, (
        "Expected rebound values 'x=60' and 'y=50' not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_seconds_and_running_speed_output():
    """Verify that total seconds (2562) and average speed (~8.73 mph) are printed."""
    res = run_student_script()
    stdout = res.stdout

    # 42 * 60 + 42 = 2562
    assert "2562" in stdout, (
        "Expected 2562 seconds (42 min 42 sec) not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )

    # 10 km = 6.21118 miles; 42m42s = 0.71167 hours -> ~8.7276 mph
    found_speed = any(val in stdout for val in ["8.72", "8.73"])
    assert found_speed, (
        "Expected average speed (~8.73 mph) not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_geometry_sphere_and_hypotenuse_output():
    """Verify that sphere volume (~523.6) and right triangle hypotenuse (5.0) are printed."""
    res = run_student_script()
    stdout = res.stdout

    # Sphere volume: (4/3) * pi * 125 = 523.5987...
    found_vol = any(val in stdout for val in ["523.59", "523.60", "523.6"])
    assert found_vol, (
        "Expected sphere volume (~523.6) not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )

    # Hypotenuse: sqrt(3^2 + 4^2) = 5.0
    assert "5.0" in stdout or "5" in stdout, (
        f"Expected hypotenuse 5.0 not found in stdout.\nYour output was:\n{res.stdout}"
    )
