# ==============================================================================
# ACU CSE 101: Week 01 Graded Challenge - The Way of the Program & Variables
# Think Python: Chapters 1 & 2
#
# GRADED INDEPENDENT CHALLENGE:
# Complete the 5 challenges below on your own.
# Run tests with the 'Run Tests' button or pytest to verify your solutions!
# ==============================================================================

import math  # noqa: F401

# ------------------------------------------------------------------------------
# Challenge 1: Interactive Temperature Converter
# Prompt the user to enter a temperature in Celsius (as a float),
# and calculate the corresponding temperature in Fahrenheit:
#   F = C * (9/5) + 32
#
# Task:
# 1. Ask user for input: float(input("Enter Celsius: "))
# 2. Calculate fahrenheit.
# 3. Print the result: print("Fahrenheit:", fahrenheit)
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 1 below:


# ------------------------------------------------------------------------------
# Challenge 2: Interactive Running Pace & Speed
# Think Python Exercise 1.2:
# Prompt the user for:
#   - Distance in kilometers (float)
#   - Race time in minutes (int)
#   - Race time in seconds (int)
#
# Task:
# 1. Read the 3 values using input() and type casting.
# 2. Calculate total seconds: (minutes * 60) + seconds.
# 3. Convert kilometers to miles (km / 1.61).
# 4. Calculate average speed in miles per hour: miles / (total_seconds / 3600.0).
# 5. Print both values:
#    print("Total seconds:", total_seconds)
#    print("Average speed (mph):", round(average_speed, 2))
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 2 below:


# ------------------------------------------------------------------------------
# Challenge 3: Interactive Bookstore Wholesale Cost
# Think Python Exercise 2.2:
# A bookstore orders copies of a textbook.
# - Cover price is 4.95, but bookstores get a 40% discount (they pay 60%).
# - Shipping costs .00 for the first copy, and bash.75 for each additional copy.
#
# Task:
# 1. Ask user for number of copies: int(input("Enter number of copies: "))
# 2. Calculate total wholesale cost:
#    discounted_price = 24.95 * 0.60 * copies
#    shipping = 3.00 + (0.75 * (copies - 1))
#    total_cost = discounted_price + shipping
# 3. Print the total:
#    print("Wholesale total:", round(total_cost, 2))
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 3 below:


# ------------------------------------------------------------------------------
# Challenge 4: Right Triangle Hypotenuse
# Prompt the user for the lengths of the two legs (a and b) of a right triangle,
# and calculate the hypotenuse c using the Pythagorean theorem:
#   c = sqrt(a^2 + b^2)
#
# Task:
# 1. Ask user for side a (float) and side b (float).
# 2. Calculate hypotenuse using math.sqrt().
# 3. Print the result:
#    print("Hypotenuse:", round(hypotenuse, 2))
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 4 below:


# ------------------------------------------------------------------------------
# Challenge 5: Formatted Item Receipt (String Operations & F-Strings)
# Practice string operations (concatenation, repetition, methods) and f-string
# formatting for precision and alignment.
#
# Task:
# 1. Prompt the user for:
#    - Item name (str): input("Enter item name: ")
#    - Unit price (float): float(input("Enter unit price: "))
#    - Quantity (int): int(input("Enter quantity: "))
# 2. Clean the item name:
#    - Strip any accidental whitespace: .strip()
#    - Format in title case: .title()
# 3. Calculate total cost: unit_price * quantity.
# 4. Print a formatted receipt:
#    - Print a border line of 30 equal signs: "=" * 30
#    - Print the item and quantity: f"Item: {item_name} (x{quantity})"
#    - Print the total cost formatted to 2 decimal places: f"Total: ${total_cost:.2f}"
#    - Print the closing border line of 30 equal signs: "=" * 30
# ------------------------------------------------------------------------------
# TODO: Write your code for Challenge 5 below:

