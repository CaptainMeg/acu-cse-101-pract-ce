# 📖 Week 01: The Way of the Program & Variables
**Think Python**: Chapters 1 & 2

Welcome to your first Python practice! In this module, you will practice writing basic Python expressions, reading interactive user input with `input()`, and printing values to the screen.

> [!NOTE]
> **Two Files in this Module:**
> 1. [`practice.py`](practice.py): **In-Class Guided Workshop**. Follow along with your instructor/TA to explore `input()`, type casting, and variable mechanics.
> 2. [`challenge.py`](challenge.py): **Independent Graded Homework**. Complete these 5 challenges on your own for your course grade!

---

## 💡 Important Concepts for This Week

### 1. Reading User Input with `input()`
The `input()` function pauses execution and waits for the user to type something in the terminal:
```python
name = input("Enter your name: ")
```

> [!IMPORTANT]
> `input()` **ALWAYS returns a string (`str`)**, even if the user types numbers like `42` or `3.14`!

If you try to do math with a raw `input()` string:
```python
age = input("Enter age: ")
next_year = age + 1  # ❌ TypeError: can only concatenate str to str!
```

#### Converting Inputs: `int()` and `float()`
To perform math, you must convert the string into a numeric type:
- **`int(input(...))`**: Converts to a whole number.
  ```python
  birth_year = int(input("Enter birth year: "))
  ```
- **`float(input(...))`**: Converts to a decimal number.
  ```python
  celsius = float(input("Enter temperature: "))
  ```
- **`.strip()`**: Removes accidental leading or trailing whitespace.
  ```python
  student_id = input("Enter ID: ").strip()
  ```

---

### 2. The Floating-Point Precision Pitfall
In decimal (base-10), numbers like $0.1$ and $0.2$ are exact.  
However, computers store floating-point numbers in **binary (base-2)** using IEEE 754. In binary, $0.1$ and $0.2$ are infinite repeating fractions!

When added together in Python:
```python
0.1 + 0.2
# 0.30000000000000004

0.1 + 0.2 == 0.3
# False!
```

#### Safe float comparison: `math.isclose`
Never use `==` to compare floating-point calculations! Instead, use `math.isclose`:
```python
import math

math.isclose(0.1 + 0.2, 0.3)  # True!
```

#### Exact decimal arithmetic for money: `Decimal`
For monetary transactions or financial calculations:
```python
from decimal import Decimal

Decimal("0.1") + Decimal("0.2")  # Decimal('0.3') -> Exact!
```

---

### 3. Variable Assignment Patterns & Re-binding

#### Multiple Assignment & Swapping:
Assign multiple variables in a single line, or swap them without a temporary variable:
```python
a, b = 12, 34
a, b = b, a  # a is now 34, b is now 12!
```

#### Chained Assignment & Re-binding:
```python
x = y = 50
x = x + 10  # Only x changes to 60; y is STILL 50!
```

---

### 4. String Operations & Formatting for `print()`

#### String Operations (`+`, `*`, `len`):
- **Concatenation (`+`)**: Joins strings together without extra spaces:
  ```python
  greeting = "Hello, " + "Ada!"  # "Hello, Ada!"
  ```
- **Repetition (`*`)**: Multiplies a string by an integer to repeat it:
  ```python
  border = "=" * 30  # "=============================="
  ```
- **Length (`len()`)**: Returns the count of characters (including spaces):
  ```python
  len("Python")  # 6
  ```
- **Common String Methods**:
  - `name.strip()`: Removes leading and trailing spaces.
  - `name.lower()`: Converts to lowercase (`"ada"`).
  - `name.upper()`: Converts to uppercase (`"ADA"`).
  - `name.title()`: Capitalizes each word (`"Ada Lovelace"`).

#### String Formatting with F-Strings:
Prefix strings with `f` (e.g. `f"..."`) to interpolate variables and control display formatting:
- **Floating-point precision (`:.2f`)**:
  ```python
  price = 19.999
  print(f"${price:.2f}")  # $20.00 (rounded to 2 decimal places)
  ```
- **Percentage formatting (`:.1%`)**:
  ```python
  tax = 0.08
  print(f"Tax: {tax:.1%}")  # Tax: 8.0%
  ```
- **Field alignment and width**:
  - `<15`: Left-align in 15 spaces.
  - `>8`: Right-align in 8 spaces.
  ```python
  print(f"{'Notebook':<15} | ${13.50:>8.2f}")
  ```

#### `print()` Keyword Arguments: `sep` and `end`:
- **`sep` (Separator)**: Changes what is printed between multiple arguments (default is space `" "`):
  ```python
  print("Python", "CSE101", "Acibadem", sep=" :: ")
  # Output: Python :: CSE101 :: Acibadem
  ```
- **`end` (Ending)**: Changes the ending character (default is newline `\n`):
  ```python
  print("Processing", end="... ")
  print("Done!")
  # Output: Processing... Done!
  ```

---

## 🏆 Graded Homework Challenges: `challenge.py`

Open [`challenge.py`](challenge.py) and solve these 5 challenges on your own:

### Challenge 1: Interactive Temperature Converter
- Prompt user for Celsius (float): `float(input("Enter Celsius: "))`
- Convert to Fahrenheit: $F = C \times \frac{9}{5} + 32$
- Print: `print("Fahrenheit:", fahrenheit)`

### Challenge 2: Interactive Running Pace & Speed (*Think Python 1.2*)
- Prompt user for:
  - Distance in kilometers (float)
  - Race time in minutes (int)
  - Race time in seconds (int)
- Calculate total seconds and average speed in miles per hour ($1\text{ mile} = 1.61\text{ km}$).
- Print:
  ```python
  print("Total seconds:", total_seconds)
  print("Average speed (mph):", round(average_speed, 2))
  ```

### Challenge 3: Interactive Bookstore Wholesale Cost (*Think Python 2.2*)
- Prompt user for number of copies: `int(input("Enter number of copies: "))`
- Books cost $24.95 with 40% discount ($14.97 per copy).
- Shipping is $3.00 for the first copy, and $0.75 for each additional copy.
- Calculate and print total cost: `print("Wholesale total:", round(total_cost, 2))`

### Challenge 4: Right Triangle Hypotenuse
- Prompt user for side $a$ and side $b$ (as floats).
- Calculate hypotenuse $c = \sqrt{a^2 + b^2}$ using `math.sqrt(...)`.
- Print: `print("Hypotenuse:", round(hypotenuse, 2))`

### Challenge 5: Formatted Item Receipt (String Operations & F-Strings)
- Prompt user for:
  - Item name (`input("Enter item name: ")`)
  - Unit price (`float(input("Enter unit price: "))`)
  - Quantity (`int(input("Enter quantity: "))`)
- Clean item name using `.strip().title()`.
- Calculate total cost (`unit_price * quantity`).
- Print the formatted receipt:
  ```python
  print("=" * 30)
  print(f"Item: {item_name} (x{quantity})")
  print(f"Total: ${total_cost:.2f}")
  print("=" * 30)
  ```

---

## 🧪 Checking Your Answers (No Terminal Required!)

You can check whether your answers are correct with a single mouse click:

1. **Option A: Bottom Status Bar Button (Easiest)**
   - Look at the blue bar at the bottom of your VS Code window.
   - Click the **`Run Tests`** button!
   - A drawer will slide open showing which challenges passed or what needs fixing.

2. **Option B: The 🧪 Testing Tab in the Left Sidebar**
   - Click the **🧪 (Flask/Beaker) icon** in the left sidebar.
   - Click the **▶️ Run Tests** button at the top.
   - Your tests will light up **Green (✅)** or **Red (❌)** right next to each test.

3. **Option C: Run Your Script Interactively**
   - Click the **`Play`** button in the bottom status bar, or click the **▶️ (Play Button)** in the top-right corner of your editor window to test typing inputs yourself!

---

## 🚀 Submitting Your Practice
When all your checks turn green, click the **`Submit`** button in the bottom status bar to submit your solutions for TA review!
