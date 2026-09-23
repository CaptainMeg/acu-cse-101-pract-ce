# 📖 Week 12: Classes and Methods
**Think Python**: Chapter 17

In this module, you will practice object-oriented methods, dunder methods (`__init__`, `__str__`, `__repr__`), and operator overloading (`__add__`, `__eq__`).

---

## 🎯 Exercises

1. Enhance `Time` class with:
   - `__init__(self, hour, minute, second)`
   - `__str__(self)`: Formatted string `HH:MM:SS`.
   - `print_time(self)`: Method to print time string.
   - `__add__(self, other)`: Overload `+` operator to add two `Time` objects or add integer seconds to a `Time` object (type dispatch).
   - `__eq__(self, other)`: Equality comparison.
