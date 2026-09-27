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


def test_seconds_calculation_output():
    """Verify that total seconds for 42 minutes 42 seconds (2562) is printed."""
    res = run_student_script()
    stdout = res.stdout

    # 42 * 60 + 42 = 2562
    assert "2562" in stdout, (
        "Expected 2562 seconds (42 min 42 sec) not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_sphere_volume_output():
    """Verify that the volume of a sphere with radius 5 (~523.598) is printed."""
    res = run_student_script()
    stdout = res.stdout

    # (4/3) * pi * 125 = 523.5987...
    found = any(val in stdout for val in ["523.59", "523.60", "523.6"])
    assert found, (
        "Expected sphere volume (~523.6) not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )
