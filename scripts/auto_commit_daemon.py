#!/usr/bin/env python3
"""ACU CSE 101 - Background Auto-Commit Watcher Daemon.

=====================================================
Monitors the exercises/ directory and automatically creates git commits
whenever students edit and save their code, removing the need for manual
git commands.
"""

import datetime
import os
import subprocess
import sys
import time

WATCH_INTERVAL_SECONDS = 3.0


def is_git_repo(repo_dir: str) -> bool:
    """Check if the directory is a valid git repository."""
    try:
        res = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        return res.returncode == 0 and res.stdout.strip() == "true"
    except OSError:
        return False


def get_git_status(repo_dir: str) -> list[str]:
    """Return a list of changed/untracked files in the repository."""
    try:
        res = subprocess.run(
            ["git", "status", "--porcelain", "exercises/"],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode != 0:
            return []
        lines = [line.strip() for line in res.stdout.splitlines() if line.strip()]
        return lines
    except OSError:
        return []


def perform_auto_commit(repo_dir: str, changed_lines: list[str]) -> bool:
    """Stages and commits changes in exercises/."""
    try:
        # 1. Stage exercises/
        subprocess.run(
            ["git", "add", "exercises/"],
            cwd=repo_dir,
            capture_output=True,
            check=False,
        )

        # 2. Extract changed file names for commit message
        file_names = []
        for line in changed_lines:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                file_names.append(os.path.basename(parts[1]))

        summary = ", ".join(file_names[:3])
        if len(file_names) > 3:
            summary += f" and {len(file_names) - 3} more"

        now_str = (
            datetime.datetime.now(datetime.timezone.utc)
            .astimezone()
            .strftime("%Y-%m-%d %H:%M:%S")
        )
        commit_msg = f"Auto-save: {summary} ({now_str})"

        # 3. Commit
        res = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        return res.returncode == 0
    except OSError:
        return False


def main():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # If git user is not configured, set default course identity
    try:
        name_check = subprocess.run(
            ["git", "config", "user.name"],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        if not name_check.stdout.strip():
            subprocess.run(
                ["git", "config", "user.name", "CSE 101 Student"],
                cwd=repo_dir,
                check=False,
            )
            subprocess.run(
                ["git", "config", "user.email", "student@cse101.acibadam.edu.tr"],
                cwd=repo_dir,
                check=False,
            )
    except OSError:
        pass

    print(f"👀 Auto-commit daemon started for: {repo_dir}/exercises")

    while True:
        try:
            if is_git_repo(repo_dir):
                changed = get_git_status(repo_dir)
                if changed:
                    success = perform_auto_commit(repo_dir, changed)
                    if success:
                        current_time = (
                            datetime.datetime.now(datetime.timezone.utc)
                            .astimezone()
                            .strftime("%H:%M:%S")
                        )
                        print(f"💾 [{current_time}] Auto-saved changes.")
            time.sleep(WATCH_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("\n🛑 Auto-commit daemon stopped.")
            sys.exit(0)
        except OSError:
            time.sleep(WATCH_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
