# 🎓 ACU CSE 101: Introduction to Programming — Practice & Workshops

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Krr0ptioN/acu-cse-101-pract-ce)

Welcome to the official student practice workspace for **CSE 101: Introduction to Programming** at **Acıbadem University (2026 Academic Year)**.

This repository is aligned with the textbook **_Think Python_ by Allen B. Downey** and configured for instant, zero-setup programming in **GitHub Codespaces**.

---

## Quickstart (Get Coding in 2 Minutes)

### Step 1: Fork this Repository
Click the **Fork** button at the top-right of this repository page to create your personal copy under your GitHub account.

### Step 2: Open in GitHub Codespaces
In your forked repository, click the green **Code** button, select the **Codespaces** tab, and click **Create codespace on main**.
*(Everything is pre-installed for you: Python 3.12, VS Code extensions, test runners, and auto-save).*

### Step 3: Start Coding & Check
1. Open the current week's folder in the left sidebar: [`exercises/week_01_intro/practice.py`](exercises/week_01_intro/practice.py).
2. Write your code and calculations directly in `practice.py`.
3. Use the **`$(checklist) Course Tasks`** menu on the left side of the bottom status bar:
   - **`Run Tests`** checks your answers.
   - **`Submit`** sends your practice work to the TAs after your tests pass.
   - **`Sync Course`** downloads newly released weekly exercises.
   - **`Play`** runs the Python file currently open in the editor.

---


## 📅 Course Curriculum & Progressive Weekly Releases

Exercises are released progressively week by week. Each week's challenge folder is kept in an independent release module:

| Week | Directory | Think Python Chapters | Topic Summary | Status |
|:---:|:---|:---|:---|:---:|
| **01** | [`exercises/week_01_intro/`](exercises/week_01_intro/) | Ch. 1 & 2 | The Way of the Program & Basic Arithmetic | **Released** |
| **02** | `exercises/week_02_variables/` | Ch. 2 | Variables, Expressions and Statements | *Weekly Release* |
| **03** | `exercises/week_03_functions/` | Ch. 3 | Functions, Parameters and Return Values | *Weekly Release* |
| **04** | `exercises/week_04_conditionals_recursion/` | Ch. 5 | Conditionals, Booleans & Recursion | *Weekly Release* |
| **05** | `exercises/week_05_iteration/` | Ch. 7 | Iteration, Loops, Newton's Square Root | *Weekly Release* |
| **06** | `exercises/week_06_strings_lists/` | Ch. 8 & 10 | Strings, Indexing, Slicing & Lists | *Weekly Release* |
| **07** | *Midterm I Review* | Ch. 1–10 | Comprehensive Practice Review | *In Class* |
| **08** | `exercises/week_08_dictionaries_tuples/` | Ch. 11 & 12 | Dictionaries and Tuples | *Weekly Release* |
| **09** | `exercises/week_09_files/` | Ch. 14 | File Reading, Writing and Exceptions | *Weekly Release* |
| **10** | `exercises/week_10_classes_objects/` | Ch. 15 | Classes, Objects and 2D Geometry | *Weekly Release* |
| **11** | `exercises/week_11_classes_functions/` | Ch. 16 | Classes, Time and Pure Functions | *Weekly Release* |
| **12** | `exercises/week_12_classes_methods/` | Ch. 17 | Object-Oriented Methods & Operator Overloading | *Weekly Release* |
| **13** | `exercises/week_13_inheritance/` | Ch. 18 | Inheritance & Card Deck Polymorphism | *Weekly Release* |
| **14** | *Midterm II Review* | Ch. 11–18 | Comprehensive OOP & Data Structures Review | *In Class* |
| **15** | *Final Project Prep* | All | Course Synthesis & Final Project | *In Class* |

---

## 🔄 Keeping Your Workspace Synced (Conflict-Free)

When course instructors publish a new weekly challenge, sync it into your workspace with zero merge conflicts:

1. Open the **`$(checklist) Course Tasks`** menu on the left side of the bottom status bar.
2. Choose **`Sync Course`**.
   *(Alternatively, run `python3 scripts/sync_course.py` in the terminal).*

This preserves your Week 1 work on `workspace` and adds newly published weeks there. A GitHub fork or an already-running Codespace does not update by itself. If a sync changes the devcontainer configuration, use **Codespaces: Rebuild Container** after the sync to apply the container update.
