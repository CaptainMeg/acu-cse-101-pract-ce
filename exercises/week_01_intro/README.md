# 📖 Week 01: The Way of the Program & Variables
**Think Python**: Chapters 1 & 2

Welcome to your first Python practice! In this module, you will practice writing basic Python expressions and printing values to the screen.

> [!NOTE]
> **No Functions Needed Yet!**  
> In Weeks 1 and 2, you do **not** need to define functions (`def`). Simply write your Python statements directly in `practice.py` and print your answers using `print(...)`. Functions will be introduced in Week 3!

---

## 💡 Important Concepts for This Week

### 1. The Floating-Point Precision Pitfall
In decimal (base-10), numbers like $0.1$ ($1/10$) and $0.2$ ($2/10$) are exact.  
However, computers store floating-point numbers in **binary (base-2)** using the IEEE 754 standard. In binary, $0.1$ and $0.2$ are infinite repeating fractions (just like $1/3 = 0.3333...$ in decimal)!

When added together in Python:
```python
0.1 + 0.2
# 0.30000000000000004

0.1 + 0.2 == 0.3
# False!
```

#### How to compare floats safely:
Never use `==` to compare floating-point calculations! Instead, use `math.isclose`:
```python
import math

math.isclose(0.1 + 0.2, 0.3)
# True
```

#### Exact decimal arithmetic (Money & Finance):
When calculating monetary amounts or accounting data where even a fraction of a cent matters, use Python's built-in `decimal` module:
```python
from decimal import Decimal

Decimal("0.1") + Decimal("0.2")
# Decimal('0.3') -> Exact!
```

---

### 2. Variable Assignment Patterns & Re-binding

#### Multiple Assignment & Swapping:
Python allows you to assign multiple variables simultaneously:
```python
a, b = 12, 34
```
You can swap two variables in a single step without needing a temporary variable:
```python
a, b = b, a
# a is now 34, and b is now 12!
```
*How it works*: Python evaluates the entire right-hand side (`b, a`) first into a temporary tuple, and then unpacks the values into `a` and `b`.

#### Chained Assignment:
You can initialize multiple variables to the same value:
```python
x = y = 50
```

#### Variable Re-binding (Variables are Labels, not Equations!):
In algebra, $y = x$ means $y$ always equals $x$.  
In programming, `=` means **assignment** (attaching a name tag to a value):
```python
x = 10
y = x  # y now refers to the value 10
x = 20  # x is rebound to 20, but y is STILL 10!
```

---

## 🎯 Exercises

Open [`practice.py`](practice.py) and complete the exercises:

### 1. Temperature Conversion
- Convert $37.0^\circ$ Celsius to Fahrenheit using:
  $$F = C \times \frac{9}{5} + 32$$
- Print your calculated answer with: `print("Fahrenheit:", fahrenheit)`.

### 2. Float Comparison Pitfall & `math.isclose`
- Calculate `float_sum = 0.1 + 0.2`.
- Check if it is close to `0.3` using `math.isclose(float_sum, 0.3)`.
- Print the result: `print("Float isclose:", is_close_result)`.

### 3. Exact Decimal Arithmetic
- Import `Decimal` and add `Decimal("0.1") + Decimal("0.2")`.
- Print the result: `print("Exact Decimal sum:", decimal_sum)`.

### 4. Multiple Assignment & Swapping
- Start with `a, b = 12, 34`.
- Swap them in a single statement: `a, b = b, a`.
- Print the result: `print(f"Swapped: a={a}, b={b}")`.

### 5. Chained Assignment & Re-binding
- Start with `x = y = 50`.
- Reassign `x = x + 10`.
- Print both: `print(f"Rebound: x={x}, y={y}")`.

### 6. Time Interval & Running Speed (*Think Python 1.2*)
- Calculate total seconds in 42 minutes and 42 seconds ($2562$).
- If you run 10 km in that time, calculate average speed in miles per hour ($1\text{ mile} = 1.61\text{ km}$).
- Print both:
  ```python
  print("Total seconds:", total_seconds)
  print("Average speed (mph):", average_speed)
  ```

### 7. Geometric Calculations (*Think Python 2.2*)
- Calculate the volume of a sphere with radius $r = 5.0$ ($V = \frac{4}{3} \pi r^3$) using `math.pi`.
- Calculate the hypotenuse $c$ of a right triangle with legs $a = 3.0$ and $b = 4.0$ ($c = \sqrt{a^2 + b^2}$) using `math.sqrt`.
- Print both:
  ```python
  print("Sphere volume:", volume)
  print("Hypotenuse:", hypotenuse)
  ```

---

## 🧪 Checking Your Answers (No Terminal Required!)

You can check whether your answers are correct with a single mouse click:

1. **Option A: Bottom Status Bar Button (Easiest)**
   - Look at the blue bar at the bottom of your VS Code window.
   - Click the **`Run Tests`** button!
   - A drawer will slide open showing which exercises passed or what needs fixing.

2. **Option B: The 🧪 Testing Tab in the Left Sidebar**
   - Click the **🧪 (Flask/Beaker) icon** in the left sidebar.
   - Click the **▶️ Run Tests** button at the top.
   - Your tests will light up **Green (✅)** or **Red (❌)** right next to each exercise name.

3. **Option C: See What Your Code Prints**
   - Click the **`Play`** button in the bottom status bar, or click the **▶️ (Play Button)** in the top-right corner of your editor window.

---

## 🚀 Submitting Your Practice
When all your checks turn green, click the **`Submit`** button in the bottom status bar to submit your solutions for TA review!
