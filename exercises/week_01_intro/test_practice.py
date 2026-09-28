"""ACU CSE 101 - Automated Unit Tests for Week 01 Guided Workshop (practice.py).

Tests verify interactive input handling and concept demonstrations via stdout.
"""

import os
import subprocess
import sys

PRACTICE_FILE = os.path.join(os.path.dirname(__file__), "practice.py")
SAMPLE_INPUT = "Ada\n2006\n37.0\n2601001\n"


def run_student_script(simulated_input: str = SAMPLE_INPUT) -> subprocess.CompletedProcess:
    """Execute student practice.py with simulated input and capture stdout."""
    assert os.path.isfile(PRACTICE_FILE), f"File not found: {PRACTICE_FILE}"
    try:
        res = subprocess.run(
            [sys.executable, PRACTICE_FILE],
            input=simulated_input,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return res
    except subprocess.TimeoutExpired:
        raise AssertionError(
            "practice.py timed out after 5 seconds. Check for infinite loops or input() calls."
        )


def test_script_executes_cleanly():
    """Verify that practice.py runs without syntax errors or exceptions."""
    res = run_student_script()
    assert res.returncode == 0, (
        f"practice.py crashed with exit code {res.returncode}.\n\nError output:\n{res.stderr}"
    )


def test_greeting_and_name_output():
    """Verify that input() name greeting is printed."""
    res = run_student_script()
    stdout = res.stdout.lower()
    assert "ada" in stdout, (
        f"Expected user name Ada in welcome output.\nYour output was:\n{res.stdout}"
    )


def test_birth_year_age_output():
    """Verify that age calculation from birth year is printed."""
    res = run_student_script()
    stdout = res.stdout
    assert "20" in stdout, (
        f"Expected calculated age 20 in output.\nYour output was:\n{res.stdout}"
    )


def test_fahrenheit_conversion_output():
    """Verify that the temperature conversion (37.0 C -> 98.6 F) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower()
    assert "98.6" in stdout, (
        f"Expected Fahrenheit temperature 98.6 not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_float_isclose_output():
    """Verify that math.isclose(0.1 + 0.2, 0.3) comparison (True) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower()
    assert "true" in stdout, (
        f"Expected True from math.isclose(0.1 + 0.2, 0.3) not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_decimal_exact_output():
    """Verify that Decimal(0.1) + Decimal(0.2) == Decimal(0.3) is printed."""
    res = run_student_script()
    stdout = res.stdout
    assert "0.3" in stdout, (
        f"Expected exact decimal sum 0.3 from Decimal(0.1) + Decimal(0.2) not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_multiple_assignment_swap_output():
    """Verify that multiple assignment swapping (a=34, b=12) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower().replace(" ", "")
    assert "a=34" in stdout and "b=12" in stdout, (
        f"Expected swapped values a=34 and b=12 not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_chained_assignment_rebinding_output():
    """Verify that chained assignment rebinding (x=60, y=50) is printed."""
    res = run_student_script()
    stdout = res.stdout.lower().replace(" ", "")
    assert "x=60" in stdout and "y=50" in stdout, (
        f"Expected rebound values x=60 and y=50 not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_string_operations_output():
    """Verify string operations: concatenation, repetition, len, and case transformations."""
    res = run_student_script()
    stdout = res.stdout
    assert "Ada Lovelace" in stdout, (
        f"Expected 'Ada Lovelace' in title case output.\nYour output was:\n{res.stdout}"
    )
    assert "ADA LOVELACE" in stdout, (
        f"Expected 'ADA LOVELACE' in uppercase output.\nYour output was:\n{res.stdout}"
    )
    assert "12" in stdout, (
        f"Expected character count 12 in output.\nYour output was:\n{res.stdout}"
    )
    assert "=" * 30 in stdout, (
        f"Expected border banner of 30 '=' characters.\nYour output was:\n{res.stdout}"
    )


def test_string_formatting_and_print_output():
    """Verify f-string precision (:.2f, :.1%), sep, and end print parameters."""
    res = run_student_script()
    stdout = res.stdout
    assert "49.96" in stdout, (
        f"Expected formatted price 49.96 (from 49.9567 rounded) in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "8.0%" in stdout, (
        f"Expected formatted percentage 8.0% in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "Python :: CSE101 :: Acibadem" in stdout, (
        f"Expected custom separator 'Python :: CSE101 :: Acibadem' in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "Saving progress... Done!" in stdout, (
        f"Expected 'Saving progress... Done!' with custom end parameter.\nYour output was:\n{res.stdout}"
    )

