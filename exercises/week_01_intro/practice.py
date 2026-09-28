# ==============================================================================
# ACU CSE 101: Week 01 Guided Workshop - The Way of the Program & Variables
# Think Python: Chapters 1 & 2
#
# INSTRUCTOR & STUDENT IN-CLASS WORKSHOP:
# Follow along with your instructor/TA as we explore:
# 1. Using input() to read strings from the user
# 2. Converting user input with int() and float()
# 3. Cleaning user input with .strip()
# 4. Floating-point comparison pitfalls (math.isclose)
# 5. Exact decimal arithmetic for financial calculations (Decimal)
# 6. Multiple assignment & variable swapping (a, b = b, a)
# 7. Chained assignment (x = y = 50) and independent re-binding
# 8. String operations (+ concatenation, * repetition, len, methods)
# 9. String formatting for print() (f-string precision, alignment, sep & end)
# ==============================================================================

import math
from decimal import Decimal

# ------------------------------------------------------------------------------
# Part 1: Reading Text with input()
# input() pauses execution and waits for the user to type something.
# It ALWAYS returns the entered value as a string (str).
# ------------------------------------------------------------------------------
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to CSE 101.")


# ------------------------------------------------------------------------------
# Part 2: Integer Input & Type Conversion - int()
# If we need a whole number for arithmetic, convert the string using int().
# ------------------------------------------------------------------------------
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print(f"You will turn {age} years old in 2026.")


# ------------------------------------------------------------------------------
# Part 3: Float Input & Type Conversion - float()
# If the number has decimal places, convert the string using float().
# ------------------------------------------------------------------------------
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)


# ------------------------------------------------------------------------------
# Part 4: Cleaning Input with .strip()
# Users often type extra leading/trailing spaces. .strip() removes them.
# ------------------------------------------------------------------------------
student_id = input("Enter your student ID: ").strip()
print(f"Registered student ID: '{student_id}'")


# ------------------------------------------------------------------------------
# Part 5: Float Comparison Pitfall & math.isclose()
# In binary floating-point (IEEE 754), 0.1 and 0.2 cannot be represented
# exactly. 0.1 + 0.2 is actually 0.30000000000000004!
# ------------------------------------------------------------------------------
float_sum = 0.1 + 0.2
print("Is 0.1 + 0.2 == 0.3?", float_sum == 0.3)  # False!
print("Using math.isclose:", math.isclose(float_sum, 0.3))  # True!


# ------------------------------------------------------------------------------
# Part 6: Exact Financial Arithmetic with Decimal
# When calculating money or accounting figures, use Decimal.
# ------------------------------------------------------------------------------
exact_sum = Decimal("0.1") + Decimal("0.2")
print("Exact Decimal sum:", exact_sum)


# ------------------------------------------------------------------------------
# Part 7: Multiple Assignment & Variable Swapping
# Python allows unpacking multiple values and swapping in a single line.
# ------------------------------------------------------------------------------
a, b = 12, 34
a, b = b, a  # Swaps values cleanly!
print(f"Swapped: a={a}, b={b}")


# ------------------------------------------------------------------------------
# Part 8: Chained Assignment & Re-binding
# In Python, variables are names pointing to values, not linked equations.
# ------------------------------------------------------------------------------
x = y = 50
x = x + 10  # Only x changes, y stays 50!
print(f"Rebound: x={x}, y={y}")


# ------------------------------------------------------------------------------
# Part 9: String Operations (+, *, len, and string methods)
# Strings can be joined with +, repeated with *, and measured with len().
# Methods like .upper(), .lower(), and .title() return transformed copies.
# ------------------------------------------------------------------------------
first_name = "ada"
last_name = "lovelace"
full_name = (first_name + " " + last_name).title()
greeting_banner = "=" * 30

print(greeting_banner)
print("Full Name (title case):", full_name)
print("Uppercase version:", full_name.upper())
print("Character count:", len(full_name))
print(greeting_banner)


# ------------------------------------------------------------------------------
# Part 10: String Formatting for print() (f-strings, precision & print parameters)
# F-strings allow precision formatting (:.2f), column alignment (<, >),
# and print() supports custom separators (sep) and line endings (end).
# ------------------------------------------------------------------------------
product = "Textbook"
price = 49.9567
tax_rate = 0.08
quantity = 3
total = price * quantity

# 1. Precision & Percentages in f-strings:
print(f"Product: {product}")
print(f"Formatted Price: ${price:.2f}")  # Rounds to 2 decimal places: $49.96
print(f"Tax Rate: {tax_rate:.1%}")  # Formats as percentage: 8.0%
print(f"Total: ${total:.2f}")

# 2. Alignment & Column Widths:
# '<15' left-aligns in 15 chars; '>9.2f' right-aligns in 9 chars
print(f"{'Item':<15} | {'Qty':>4} | {'Subtotal':>10}")
print("-" * 35)
print(f"{product:<15} | {quantity:>4} | ${total:>9.2f}")

# 3. Custom print() separators (sep) and line endings (end):
print("Python", "CSE101", "Acibadem", sep=" :: ")
print("Saving progress", end="... ")
print("Done!")

