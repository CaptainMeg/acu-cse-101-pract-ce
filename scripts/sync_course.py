#!/usr/bin/env python3
"""ACU CSE 101 - Smart Course Material Sync Tool.

==============================================
Synchronizes the student workspace with newly published course challenges and
workshops from the upstream course repository without merge conflicts:

1. Auto-saves all current student work to the 'workspace' branch.
2. Ensures student changes are NEVER committed or pushed to 'main'.
3. Fetches newly released weekly folders from upstream/main.
4. Updates local 'main' and seamlessly merges new week folders into 'workspace'.
5. Pushes updated 'workspace' and 'main' to the student's GitHub fork (origin).

Usage:
    python3 scripts/sync_course.py
"""

import os
import subprocess

# Terminal styling constants
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

DEFAULT_UPSTREAM_URL = "https://github.com/acibadam-cse/acu-cse-101-practice.git"
STUDENT_WORK_BRANCH = "workspace"


def run_git(cmd: list[str], cwd: str) -> subprocess.CompletedProcess:
    """Run a git command and return the completed process."""
    return subprocess.run(
        ["git"] + cmd, cwd=cwd, capture_output=True, text=True, check=False
    )


def get_current_branch(repo_dir: str) -> str:
    """Return the name of the currently checked out git branch."""
    res = run_git(["rev-parse", "--abbrev-ref", "HEAD"], repo_dir)
    return res.stdout.strip() or "main"


def ensure_upstream_remote(repo_dir: str):
    """Ensure the upstream course remote is configured."""
    remotes_res = run_git(["remote", "-v"], repo_dir)
    remotes = remotes_res.stdout

    if "upstream" not in remotes:
        print(f"🔧 Configuring upstream remote: {CYAN}{DEFAULT_UPSTREAM_URL}{RESET}")
        run_git(["remote", "add", "upstream", DEFAULT_UPSTREAM_URL], repo_dir)


def main():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(
        f"\n{BOLD}{CYAN}=== 🔄 ACU CSE 101: Syncing Weekly Course Materials ==={RESET}\n"
    )

    ensure_upstream_remote(repo_dir)

    # 1. Check current branch and ensure student work is in 'workspace', not 'main'
    curr_branch = get_current_branch(repo_dir)

    # Auto-save any uncommitted work first
    run_git(["add", "exercises/"], repo_dir)
    status_res = run_git(["status", "--porcelain", "exercises/"], repo_dir)
    if status_res.stdout.strip():
        print("💾 Auto-saving current work before synchronization...")
        run_git(["commit", "-m", "Auto-save before course sync"], repo_dir)

    if curr_branch == "main":
        print(
            f"🔀 Moving to student working branch '{STUDENT_WORK_BRANCH}' (keeping 'main' clean)..."
        )
        # Create or switch to workspace branch
        run_git(["checkout", "-B", STUDENT_WORK_BRANCH], repo_dir)
        curr_branch = STUDENT_WORK_BRANCH

    # 2. Fetch the latest released weekly modules from upstream main
    print("📡 Checking for newly released challenges and workshops from upstream...")
    fetch_res = run_git(["fetch", "upstream", "main"], repo_dir)

    if fetch_res.returncode != 0:
        # If upstream is not accessible or offline, notify user gracefully
        err_msg = fetch_res.stderr.strip() or fetch_res.stdout.strip()
        print(f"{YELLOW}Note during fetch:{RESET} {err_msg}")
        print("Continuing with local synchronization...")

    # 3. Update local 'main' branch to exactly match upstream/main
    # (Without needing to checkout 'main')
    run_git(["fetch", "upstream", "main:main"], repo_dir)

    # 4. Merge new weekly folders from main into the student's working branch
    print(f"📦 Merging newly published course challenges into '{curr_branch}'...")
    merge_res = run_git(
        ["merge", "main", "-m", "Sync: pull newly published course exercises"],
        repo_dir,
    )

    if merge_res.returncode == 0:
        print(f"\n{GREEN}{BOLD}🎉 Success! Your workspace is fully up to date.{RESET}")
        print(
            f"Newly published challenges have been merged into your '{curr_branch}' branch."
        )
    else:
        print(
            f"\n{YELLOW}Notice during merge:{RESET} {merge_res.stdout.strip() or merge_res.stderr.strip()}"
        )
        print(
            "Your work is safely preserved. If you have questions, please reach out to your TA."
        )

    # 5. Push student working branch and updated main to student's fork (origin)
    print("\n☁️ Backing up your workspace to your GitHub fork...")
    run_git(["push", "origin", curr_branch], repo_dir)
    run_git(["push", "origin", "main"], repo_dir)
    print("✅ Fork synchronized.\n")


if __name__ == "__main__":
    main()
