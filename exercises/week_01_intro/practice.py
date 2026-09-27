# ==============================================================================
# ACU CSE 101: Week 01 Practice - The Way of the Program & Variables
# Think Python: Chapters 1 & 2
#
# Instructions:
# - Write your code below each exercise description.
# - You do NOT need to write any functions (def) yet!
# - Simply create variables and use print(...) to display your answers.
# ==============================================================================

import math

# ------------------------------------------------------------------------------
# Exercise 1: Temperature Conversion
# Convert 37.0 degrees Celsius to Fahrenheit using the formula:
#   Fahrenheit = Celsius * (9/5) + 32
#
# Task:
# 1. Create a variable `celsius` with the value 37.0
# 2. Calculate the temperature in Fahrenheit.
# 3. Print the result containing both the label and value, for example:
#    print("Fahrenheit:", fahrenheit)
# ------------------------------------------------------------------------------
celsius = 37.0
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)


# ------------------------------------------------------------------------------
# Exercise 2: Seconds in a Time Interval
# Think Python Exercise 1.2, Question 1:
# "How many seconds are there in 42 minutes 42 seconds?"
#
# Task:
# 1. Create variables for minutes (42) and seconds (42).
# 2. Calculate the total number of seconds.
# 3. Print the result, for example:
#    print("Total seconds:", total_seconds)
# ------------------------------------------------------------------------------
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds
print("Total seconds:", total_seconds)


# ------------------------------------------------------------------------------
# Exercise 3: Volume of a Sphere
# Think Python Exercise 2.2, Question 1:
# "The volume of a sphere with radius r is (4/3) * pi * r^3.
#  What is the volume of a sphere with radius 5?"
#
# Task:
# 1. Create a variable `radius` with the value 5.0
# 2. Calculate the volume using math.pi (or 3.141592653589793).
# 3. Print the result, for example:
#    print("Sphere volume:", volume)
# ------------------------------------------------------------------------------
radius = 5.0
volume = (4 / 3) * math.pi * (radius**3)
print("Sphere volume:", volume)
