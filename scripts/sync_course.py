#!/usr/bin/env python3
"""ACU CSE 101 - Smart Course Material Sync Tool.

==============================================
Synchronizes the student workspace with newly published course challenges and
workshops from the upstream course repository without merge conflicts:

1. Auto-saves all current student work to the 'workspace' branch.
2. Ensures student changes are NEVER committed or pushed to 'main'.
3. Fetches newly released weekly folders from upstream/main.
4. Updates local 'main' from the canonical course repository and merges it into
   'workspace'.
5. Pushes the updated student workspace to the student's GitHub fork (origin).

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

DEFAULT_UPSTREAM_URL = os.environ.get(
    "COURSE_UPSTREAM_URL", "https://github.com/Krr0ptioN/acu-cse-101-pract-ce.git"
)
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
    remote_res = run_git(["remote", "get-url", "upstream"], repo_dir)
    if remote_res.returncode != 0:
        print(f"🔧 Configuring upstream remote: {CYAN}{DEFAULT_UPSTREAM_URL}{RESET}")
        run_git(["remote", "add", "upstream", DEFAULT_UPSTREAM_URL], repo_dir)
    elif remote_res.stdout.strip() != DEFAULT_UPSTREAM_URL:
        print(f"🔧 Updating course remote: {CYAN}{DEFAULT_UPSTREAM_URL}{RESET}")
        run_git(["remote", "set-url", "upstream", DEFAULT_UPSTREAM_URL], repo_dir)


def switch_to_workspace(repo_dir: str) -> str:
    """Switch to the persistent student branch without resetting it."""
    current_branch = get_current_branch(repo_dir)
    if current_branch != "main":
        return current_branch

    workspace_exists = run_git(
        ["show-ref", "--verify", "--quiet", f"refs/heads/{STUDENT_WORK_BRANCH}"],
        repo_dir,
    ).returncode == 0
    command = ["checkout", STUDENT_WORK_BRANCH] if workspace_exists else ["checkout", "-b", STUDENT_WORK_BRANCH]
    checkout_res = run_git(command, repo_dir)
    if checkout_res.returncode != 0:
        raise RuntimeError(checkout_res.stderr.strip() or "Unable to open the student workspace.")
    return STUDENT_WORK_BRANCH


def main():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(
        f"\n{BOLD}{CYAN}=== 🔄 ACU CSE 101: Syncing Weekly Course Materials ==={RESET}\n"
    )

    ensure_upstream_remote(repo_dir)

    # 1. Ensure student work is in 'workspace', not 'main', before auto-saving.
    try:
        curr_branch = switch_to_workspace(repo_dir)
    except RuntimeError as error:
        print(f"{RED}Unable to prepare your workspace:{RESET} {error}")
        return

    # Auto-save any uncommitted work first
    run_git(["add", "exercises/"], repo_dir)
    status_res = run_git(["status", "--porcelain", "exercises/"], repo_dir)
    if status_res.stdout.strip():
        print("💾 Auto-saving current work before synchronization...")
        run_git(["commit", "-m", "Auto-save before course sync"], repo_dir)

    # 2. Fetch the latest released weekly modules from upstream main
    print("📡 Checking for newly released challenges and workshops from upstream...")
    fetch_res = run_git(["fetch", "upstream", "main"], repo_dir)

    if fetch_res.returncode != 0:
        # If upstream is not accessible or offline, notify user gracefully
        err_msg = fetch_res.stderr.strip() or fetch_res.stdout.strip()
        print(f"{YELLOW}Note during fetch:{RESET} {err_msg}")
        print("Continuing with local synchronization...")

    # 3. Update local 'main' from the course copy without checking it out.
    update_main_res = run_git(["branch", "-f", "main", "upstream/main"], repo_dir)
    if update_main_res.returncode != 0:
        print(
            f"{RED}Unable to update the course materials:{RESET} "
            f"{update_main_res.stderr.strip() or update_main_res.stdout.strip()}"
        )
        return

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

    # 5. Push only the student's workspace. The canonical course main remains
    # the source of future updates and is never overwritten in the student's fork.
    print("\n☁️ Backing up your workspace to your GitHub fork...")
    run_git(["push", "origin", curr_branch], repo_dir)
    print("✅ Fork synchronized.\n")


if __name__ == "__main__":
    main()
