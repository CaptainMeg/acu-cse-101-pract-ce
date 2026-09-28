"""ACU CSE 101 - Automated Unit Tests for Week 01 Graded Challenge (challenge.py).

Tests simulate interactive user inputs (stdin) and verify calculations via stdout.
"""

import os
import subprocess
import sys

CHALLENGE_FILE = os.path.join(os.path.dirname(__file__), "challenge.py")

# Default simulated inputs:
# Challenge 1: 100.0 (EUR), 1.10 (rate)
# Challenge 2: 7 (students), 3 (pizzas), 8 (slices per pizza)
# Challenge 3: 5.0 (sphere radius)
# Challenge 4: "Rock", "Paper", "Scissors" (Cup items)
# Challenge 5: "  grace hopper  ", "computer science", "fellow" (badge inputs)
SAMPLE_INPUT = "100.0\n1.10\n7\n3\n8\n5.0\nRock\nPaper\nScissors\n  grace hopper  \ncomputer science\nfellow\n"


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


def test_challenge_1_currency_converter():
    """Verify Challenge 1: Travel Currency Converter (EUR 100 @ 1.10 -> $110 gross, $2.20 fee, $107.80 net)."""
    res = run_student_challenge()
    stdout = res.stdout
    assert "110.00" in stdout, (
        f"Expected Gross USD '110.00' not found in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "2.20" in stdout, (
        f"Expected Fee '2.20' not found in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "107.80" in stdout, (
        f"Expected Net USD '107.80' not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_challenge_2_pizza_party_slices():
    """Verify Challenge 2: Pizza Party (7 students, 3 pizzas of 8 -> 24 total, 3 each, 3 leftover)."""
    res = run_student_challenge()
    stdout = res.stdout
    assert "24" in stdout, (
        f"Expected total slices '24' not found in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "3" in stdout, (
        f"Expected slices per student '3' not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_challenge_3_sphere_geometry():
    """Verify Challenge 3: Sphere Geometry for radius 5.0 (Volume 523.60, Surface Area 314.16)."""
    res = run_student_challenge()
    stdout = res.stdout
    assert "523.60" in stdout or "523.6" in stdout, (
        f"Expected Sphere Volume '523.60' not found in stdout.\nYour output was:\n{res.stdout}"
    )
    assert "314.16" in stdout, (
        f"Expected Sphere Surface Area '314.16' not found in stdout.\nYour output was:\n{res.stdout}"
    )


def test_challenge_4_three_cup_shell_game():
    """Verify Challenge 4: 3-Cup Shell Game cyclic shift (Scissors -> Rock -> Paper)."""
    res = run_student_challenge()
    stdout = res.stdout
    assert "Scissors -> Rock -> Paper" in stdout, (
        f"Expected cyclic rotation 'Scissors -> Rock -> Paper' using sep=' -> ' not found.\nYour output was:\n{res.stdout}"
    )


def test_challenge_5_event_badge():
    """Verify Challenge 5: Event Badge with border, title case, uppercase dept, and length."""
    res = run_student_challenge()
    stdout = res.stdout
    assert "#" * 32 in stdout, (
        f"Expected border line of 32 '#' characters ('#' * 32) not found.\nYour output was:\n{res.stdout}"
    )
    assert "Grace Hopper" in stdout, (
        f"Expected title-cased name 'Grace Hopper' not found.\nYour output was:\n{res.stdout}"
    )
    assert "COMPUTER SCIENCE" in stdout, (
        f"Expected uppercase department 'COMPUTER SCIENCE' not found.\nYour output was:\n{res.stdout}"
    )
    assert "Fellow" in stdout, (
        f"Expected title-cased role 'Fellow' not found.\nYour output was:\n{res.stdout}"
    )
    assert "12" in stdout, (
        f"Expected name length '12' not found in badge output.\nYour output was:\n{res.stdout}"
    )


