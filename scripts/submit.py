#!/usr/bin/env python3
"""ACU CSE 101 - Student Practice Submission Launcher.

===================================================
Runs local test suites and prepares a clean submission branch and Pull Request
to the upstream course repository.

Usage:
    python3 scripts/submit.py
    python3 scripts/submit.py --week week_01_intro
    python3 scripts/submit.py --test-only
"""

import argparse
import glob
import os
import subprocess
import sys

# Terminal styling constants
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def get_available_weeks(repo_dir: str) -> list[str]:
    """Discover all exercise week folders."""
    exercises_dir = os.path.join(repo_dir, "exercises")
    if not os.path.isdir(exercises_dir):
        return []
    weeks = [
        os.path.basename(d)
        for d in sorted(glob.glob(os.path.join(exercises_dir, "week_*")))
        if os.path.isdir(d)
    ]
    return weeks


def select_week(repo_dir: str, requested_week: str | None) -> str:
    """Select the target week via argument or interactive menu."""
    available = get_available_weeks(repo_dir)
    if not available:
        print(
            f"{RED}Error: No week directories found in exercises/{RESET}",
            file=sys.stderr,
        )
        sys.exit(1)

    if requested_week:
        # Match exact or partial
        for w in available:
            if requested_week == w or requested_week in w:
                return w
        print(
            f"{RED}Error: Week '{requested_week}' not found in {available}{RESET}",
            file=sys.stderr,
        )
        sys.exit(1)

    if len(available) == 1:
        return available[0]

    print(f"\n{BOLD}{CYAN}=== Select Week to Test / Submit ==={RESET}")
    for idx, w in enumerate(available, 1):
        print(f"  [{idx}] {w}")

    while True:
        try:
            choice = input(f"\nEnter choice [1-{len(available)}]: ").strip()
            if not choice:
                return available[0]
            val = int(choice)
            if 1 <= val <= len(available):
                return available[val - 1]
            print(
                f"{YELLOW}Please enter a number between 1 and {len(available)}.{RESET}"
            )
        except (ValueError, KeyboardInterrupt):
            print("\nAborted.")
            sys.exit(0)


def run_tests(repo_dir: str, week: str) -> bool:
    """Executes pytest for the specified week."""
    test_file = os.path.join("exercises", week, "test_practice.py")
    full_path = os.path.join(repo_dir, test_file)

    if not os.path.isfile(full_path):
        print(f"{RED}Error: Test file not found: {test_file}{RESET}", file=sys.stderr)
        return False

    print(f"\n{BOLD}{CYAN}🧪 Running Automated Tests for {week}...{RESET}\n")

    res = subprocess.run(
        [sys.executable, "-m", "pytest", "-v", test_file],
        cwd=repo_dir,
        check=False,
    )
    return res.returncode == 0


def get_current_branch(repo_dir: str) -> str:
    """Return the name of the currently checked out git branch."""
    try:
        res = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        return res.stdout.strip() or "main"
    except OSError:
        return "main"


def ensure_committed(repo_dir: str):
    """Ensure all current work in exercises is committed."""
    curr_branch = get_current_branch(repo_dir)
    if curr_branch == "main":
        subprocess.run(
            ["git", "checkout", "-B", "workspace"],
            cwd=repo_dir,
            check=False,
        )
        print("🔀 Switched to 'workspace' branch to keep 'main' clean.")

    subprocess.run(["git", "add", "exercises/"], cwd=repo_dir, check=False)
    status = subprocess.run(
        ["git", "status", "--porcelain", "exercises/"],
        cwd=repo_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    if status.stdout.strip():
        subprocess.run(
            ["git", "commit", "-m", "Pre-submission snapshot"],
            cwd=repo_dir,
            check=False,
        )


def handle_submission(repo_dir: str, week: str):
    """Creates a submission branch and opens or pushes the pull request."""
    ensure_committed(repo_dir)

    original_branch = get_current_branch(repo_dir)
    if original_branch == "main":
        subprocess.run(
            ["git", "checkout", "-B", "workspace"], cwd=repo_dir, check=False
        )
        original_branch = "workspace"

    branch_name = f"submit/{week}"
    print(f"\n{BOLD}{CYAN}🚀 Preparing Submission Branch: {branch_name}{RESET}")

    # Switch to / create branch
    subprocess.run(["git", "checkout", "-B", branch_name], cwd=repo_dir, check=False)

    # Push to origin
    print("📡 Pushing submission branch to your GitHub fork...")
    push_res = subprocess.run(
        ["git", "push", "-u", "origin", branch_name, "--force"],
        cwd=repo_dir,
        capture_output=True,
        text=True,
        check=False,
    )

    if push_res.returncode != 0:
        print(
            f"{YELLOW}Note on push:{RESET} {push_res.stderr.strip() or push_res.stdout.strip()}"
        )

    # Attempt to create PR using GitHub CLI (gh)
    print("\n📬 Opening Pull Request to Course Repository...")
    pr_title = f"Submission: {week}"
    pr_body = f"Automated submission for `{week}`.\n\nAll local unit tests passed successfully."

    pr_res = subprocess.run(
        [
            "gh",
            "pr",
            "create",
            "--title",
            pr_title,
            "--body",
            pr_body,
            "--head",
            branch_name,
            "--base",
            "main",
        ],
        cwd=repo_dir,
        capture_output=True,
        text=True,
        check=False,
    )

    if pr_res.returncode == 0:
        pr_url = pr_res.stdout.strip()
        print(f"\n{GREEN}{BOLD}🎉 Submission Successful!{RESET}")
        print(f"🔗 Pull Request: {CYAN}{pr_url}{RESET}")
        print(
            "Your Teaching Assistants will review your submission and automated tests will grade it."
        )
    else:
        # Fallback if gh CLI is unauthenticated or PR already exists
        err_msg = pr_res.stderr.strip()
        if "already exists" in err_msg:
            print(
                f"\n{GREEN}{BOLD}✅ Existing PR updated with your latest changes!{RESET}"
            )
        else:
            print(f"\n{YELLOW}{BOLD}Branch '{branch_name}' pushed successfully!{RESET}")
            print(
                "To finish creating your Pull Request, visit your GitHub repository page and click 'Compare & Pull Request'."
            )

    # Return back to working branch
    print(f"\n↩️  Returning to working branch '{original_branch}'...")
    subprocess.run(["git", "checkout", original_branch], cwd=repo_dir, check=False)


def main():
    parser = argparse.ArgumentParser(
        description="ACU CSE 101 - Test Runner & Submission Launcher"
    )
    parser.add_argument(
        "--week",
        help="Target week to test/submit (e.g., 'week_01_intro')",
    )
    parser.add_argument(
        "--test-only",
        action="store_true",
        help="Only run tests without creating a submission branch",
    )

    args = parser.parse_args()
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    target_week = select_week(repo_dir, args.week)
    passed = run_tests(repo_dir, target_week)

    if not passed:
        print(f"\n{RED}{BOLD}❌ Some tests failed.{RESET}")
        print(
            f"{YELLOW}Please review the test failures above, fix your code, and run submission again.{RESET}\n"
        )
        sys.exit(1)

    print(f"\n{GREEN}{BOLD}✅ All tests for {target_week} PASSED!{RESET}")

    if args.test_only:
        print("Test run completed.")
        sys.exit(0)

    handle_submission(repo_dir, target_week)


if __name__ == "__main__":
    main()
