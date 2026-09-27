# 📖 Week 01: The Way of the Program & Variables
**Think Python**: Chapters 1 & 2

Welcome to your first Python practice! In this module, you will practice writing basic Python expressions and printing values to the screen.

> [!NOTE]
> **No Functions Needed Yet!**  
> In Weeks 1 and 2, you do **not** need to define functions (`def`). Simply write your Python statements directly in `practice.py` and print your answers using `print(...)`. Functions will be introduced in Week 3!

---

## 🎯 Exercises

Open [`practice.py`](practice.py) and complete the three exercises:

### 1. Temperature Conversion
- Convert $37.0^\circ$ Celsius to Fahrenheit using:
  $$F = C \times \frac{9}{5} + 32$$
- Print your calculated answer with `print("Fahrenheit:", fahrenheit)`.

### 2. Seconds in a Time Interval (*Think Python 1.2*)
- Calculate how many seconds there are in **42 minutes and 42 seconds**.
- Print your calculated answer with `print("Total seconds:", total_seconds)`.

### 3. Volume of a Sphere (*Think Python 2.2*)
- Calculate the volume of a sphere with radius $r = 5.0$ using:
  $$V = \frac{4}{3} \pi r^3$$
- You can use `import math` and `math.pi`, or `3.141592653589793`.
- Print your answer with `print("Sphere volume:", volume)`.

---

## 🧪 Testing Your Code
Run the tests locally using the VS Code task **"🧪 Run Tests for Current Week"** or in the terminal:
```bash
pytest exercises/week_01_intro/test_practice.py
```
*(The automated test runner executes your script and checks what gets printed to standard output!)*

## 🚀 Submitting
When all tests pass, run **"🚀 Submit Current Week Practice"** from the VS Code Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
