#!/usr/bin/env python3
"""ACU CSE 101 - Course Material Sync Tool.

========================================
Syncs the student's local fork with the upstream course repository so students
receive newly released weekly workshops and exercises cleanly.

Usage:
    python3 scripts/sync_course.py
"""

import os
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

DEFAULT_UPSTREAM_URL = "https://github.com/acibadam-cse/acu-cse-101-practice.git"


def run_git(cmd: list[str], cwd: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git"] + cmd, cwd=cwd, capture_output=True, text=True, check=False
    )


def ensure_upstream_remote(repo_dir: str):
    """Ensure that upstream remote exists; if not, add it."""
    remotes_res = run_git(["remote", "-v"], repo_dir)
    remotes = remotes_res.stdout

    if "upstream" not in remotes:
        print(f"🔧 Configuring upstream remote: {DEFAULT_UPSTREAM_URL}")
        run_git(["remote", "add", "upstream", DEFAULT_UPSTREAM_URL], repo_dir)


def main():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"\n{BOLD}{CYAN}=== Syncing with Upstream Course Materials ==={RESET}\n")

    ensure_upstream_remote(repo_dir)

    # 1. Commit any dirty local changes to preserve student work
    run_git(["add", "exercises/"], repo_dir)
    status_res = run_git(["status", "--porcelain", "exercises/"], repo_dir)
    if status_res.stdout.strip():
        print("💾 Auto-saving current work before syncing...")
        run_git(["commit", "-m", "Auto-save before course sync"], repo_dir)

    # 2. Fetch from upstream
    print("📡 Fetching latest updates from upstream course repository...")
    fetch_res = run_git(["fetch", "upstream", "main"], repo_dir)
    if fetch_res.returncode != 0:
        print(
            f"{YELLOW}Warning during fetch:{RESET} {fetch_res.stderr.strip() or fetch_res.stdout.strip()}"
        )

    # 3. Merge upstream/main into current branch
    print("🔀 Merging new exercises into your workspace...")
    merge_res = run_git(["merge", "upstream/main", "--no-edit"], repo_dir)

    if merge_res.returncode == 0:
        print(f"\n{GREEN}{BOLD}🎉 Course materials successfully synchronized!{RESET}")
        print("You now have the latest workshops, exercises, and test suites ready.")
    else:
        print(
            f"\n{YELLOW}Note on merge:{RESET} {merge_res.stdout.strip() or merge_res.stderr.strip()}"
        )
        print(
            "Your work is safely preserved. If you see conflict markers, contact your TA for quick assistance."
        )


if __name__ == "__main__":
    main()
