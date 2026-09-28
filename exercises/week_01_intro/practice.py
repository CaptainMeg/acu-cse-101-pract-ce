# ==============================================================================
# ACU CSE 101: Week 01 Practice - The Way of the Program & Variables
# Think Python: Chapters 1 & 2
#
# Instructions:
# - Write your code below each exercise description.
# - You do NOT need to write any functions (def) yet!
# - Simply create variables and use print(...) to display your answers.
# ==============================================================================

import math  # noqa: F401
from decimal import Decimal  # noqa: F401

# ------------------------------------------------------------------------------
# Exercise 1: Temperature Conversion
# Convert 37.0 degrees Celsius to Fahrenheit using the formula:
#   Fahrenheit = Celsius * (9/5) + 32
#
# Task:
# 1. Use the variable `celsius` given below.
# 2. Calculate the temperature in Fahrenheit.
# 3. Print the result containing both the label and value, for example:
#    print("Fahrenheit:", fahrenheit)
# ------------------------------------------------------------------------------
celsius = 37.0
# TODO: Calculate fahrenheit and print your answer below:


# ------------------------------------------------------------------------------
# Exercise 2: Float Comparison Pitfall & math.isclose
# In Python (and IEEE 754 floating-point arithmetic), numbers like 0.1 and 0.2
# cannot be represented exactly in binary (base-2).
# As a result: 0.1 + 0.2 evaluates to 0.30000000000000004, so:
#   0.1 + 0.2 == 0.3  ->  False!
#
# Task:
# 1. Calculate the sum of 0.1 and 0.2.
# 2. Compare the sum with 0.3 using `math.isclose(sum_val, 0.3)`.
# 3. Print the result:
#    print("Float isclose:", is_close_result)
# ------------------------------------------------------------------------------
float_sum = 0.1 + 0.2
# TODO: Use math.isclose to compare float_sum with 0.3, and print the result:


# ------------------------------------------------------------------------------
# Exercise 3: Exact Decimal Arithmetic (Money & Finance)
# When exact decimal precision is required (such as financial transactions),
# Python provides the `Decimal` class from the `decimal` module.
#
# Task:
# 1. Add Decimal("0.1") and Decimal("0.2").
# 2. Print the exact result:
#    print("Exact Decimal sum:", decimal_sum)
# ------------------------------------------------------------------------------
# TODO: Compute Decimal("0.1") + Decimal("0.2") and print the result:


# ------------------------------------------------------------------------------
# Exercise 4: Multiple Assignment & Variable Swapping
# Python allows assigning multiple variables in a single line:
#   a, b = 12, 34
# It also allows swapping their values without needing a temporary variable:
#   a, b = b, a
#
# Task:
# 1. Use the variables `a` and `b` initialized below.
# 2. Swap their values in a single statement: a, b = b, a
# 3. Print the swapped values:
#    print(f"Swapped: a={a}, b={b}")
# ------------------------------------------------------------------------------
a, b = 12, 34
# TODO: Swap a and b in a single statement, then print them:


# ------------------------------------------------------------------------------
# Exercise 5: Chained Assignment & Re-binding Order
# You can assign the same initial value to multiple variables at once:
#   x = y = 50
# In Python, variables are names pointing to values. Reassigning `x` does NOT
# change `y`!
#
# Task:
# 1. Start with the chained assignment: x = y = 50
# 2. Re-assign `x` by adding 10 to it (x = x + 10).
# 3. Print both variables to observe what happened:
#    print(f"Rebound: x={x}, y={y}")
# ------------------------------------------------------------------------------
x = y = 50
# TODO: Add 10 to x, and print both x and y:


# ------------------------------------------------------------------------------
# Exercise 6: Seconds in a Time Interval & Running Average Speed
# Think Python Exercise 1.2:
# "How many seconds are there in 42 minutes 42 seconds?
#  If you run a 10 kilometer race in 42 minutes 42 seconds,
#  what is your average speed in miles per hour?" (Hint: 1 mile = 1.61 km)
#
# Task:
# 1. Calculate total seconds in 42 minutes and 42 seconds.
# 2. Convert 10 kilometers to miles (10.0 / 1.61).
# 3. Convert total time to hours (total_seconds / 3600).
# 4. Calculate average speed (miles / hours).
# 5. Print both:
#    print("Total seconds:", total_seconds)
#    print("Average speed (mph):", average_speed)
# ------------------------------------------------------------------------------
minutes = 42
seconds = 42
kilometers = 10.0
km_per_mile = 1.61
# TODO: Calculate total_seconds and average_speed, then print both:


# ------------------------------------------------------------------------------
# Exercise 7: Geometric Calculations (Sphere Volume & Hypotenuse)
# Think Python Exercise 2.2:
# 1. Volume of a sphere with radius 5.0:  V = (4/3) * pi * r^3
# 2. Hypotenuse of a right triangle with legs a=3.0, b=4.0: c = sqrt(a^2 + b^2)
#
# Task:
# 1. Calculate the sphere volume using `math.pi` and `** 3`.
# 2. Calculate the hypotenuse using `math.sqrt(...)`.
# 3. Print both:
#    print("Sphere volume:", volume)
#    print("Hypotenuse:", hypotenuse)
# ------------------------------------------------------------------------------
radius = 5.0
side_a = 3.0
side_b = 4.0
# TODO: Calculate volume and hypotenuse, then print both:
