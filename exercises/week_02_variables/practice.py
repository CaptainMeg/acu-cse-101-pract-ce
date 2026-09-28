# ==============================================================================
# ACU CSE 101: Week 02 Practice - Variables, Expressions and Statements
# Think Python: Chapter 2
#
# Instructions:
# - Write your code below each exercise description.
# - You do NOT need to write any functions (def) yet!
# - Create variables, perform the calculations, and print your answers.
# ==============================================================================

# ------------------------------------------------------------------------------
# Exercise 1: Wholesale Bookstore Cost
# Think Python Exercise 2.2, Question 2:
# "Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#  Shipping costs $3 for the first copy and 75 cents for each additional copy.
#  What is the total wholesale cost for 60 copies?"
#
# Task:
# 1. Define cover_price = 24.95, discount = 0.40, copies = 60
# 2. Calculate the discounted book cost.
# 3. Calculate shipping: $3.00 for 1st copy + $0.75 for each additional 59 copies.
# 4. Print total wholesale cost (should be around $945.45), for example:
#    print("Bookstore cost:", total_cost)
# ------------------------------------------------------------------------------
cover_price = 24.95
discount = 0.40
discounted_price = cover_price * (1 - discount)
num_copies = 60

total_book_cost = num_copies * discounted_price
shipping_cost = 3.00 + (num_copies - 1) * 0.75
total_wholesale_cost = total_book_cost + shipping_cost

print("Bookstore cost:", round(total_wholesale_cost, 2))


# ------------------------------------------------------------------------------
# Exercise 2: Running Pace & Breakfast Arrival Time
# Think Python Exercise 2.2, Question 3:
# "If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
#  then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
#  what time do I get home for breakfast?"
#
# Task:
# 1. Easy pace is 8 min 15 sec per mile (run for 2 miles total = 16 min 30 sec).
# 2. Tempo pace is 7 min 12 sec per mile (run for 3 miles total = 21 min 36 sec).
# 3. Start time is 6 hours, 52 minutes.
# 4. Calculate total run seconds and find the arrival hour and minute.
# 5. Print the arrival time in HH:MM format (7:30 or 07:30), for example:
#    print("Arrival time:", f"{arrival_hour:02d}:{arrival_minute:02d}")
# ------------------------------------------------------------------------------
start_total_sec = (6 * 3600) + (52 * 60)
easy_sec = 2 * ((8 * 60) + 15)
tempo_sec = 3 * ((7 * 60) + 12)
total_run_sec = easy_sec + tempo_sec

end_total_sec = start_total_sec + total_run_sec
arrival_hour = int(end_total_sec // 3600) % 24
arrival_min = int((end_total_sec % 3600) // 60)

print("Arrival time:", f"{arrival_hour:02d}:{arrival_min:02d}")


# ------------------------------------------------------------------------------
# Exercise 3: User Display Banner
# String repetition & formatting practice:
# Create a banner with the title "PYTHON CSE 101" centered in a 30-character
# line surrounded by "=" characters.
#
# Task:
# 1. title = "PYTHON CSE 101"
# 2. Format with center(30, "=") or string operators.
# 3. Print the banner, for example:
#    print("Banner:", banner)
# ------------------------------------------------------------------------------
title = "PYTHON CSE 101"
banner = title.center(30, "=")
print("Banner:", banner)
