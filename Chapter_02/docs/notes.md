---
title: Variables & Data Types Notes
chapter: 02
difficulty: ⭐☆☆☆☆
study_time: 1.5 Hours
revision_time: 20 Minutes
interview_importance: Medium
exam_importance: High
---

← [Previous Chapter](../../Chapter_01/README.md) | 🏠 [Home](../../README.md) | [Next Chapter](../../Chapter_03/README.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 📝 Chapter 02 Notes: Variables & Data Types

This is the core textbook for Chapter 02. Read this thoroughly before attempting practice problems.

---

## 1. Variables

### What is a Variable?
A variable is a container used to store data values.

### Real-World Analogy
Think of your computer's RAM (Memory) as a massive warehouse full of empty boxes. A variable is simply taking a piece of data (like the number `20`), putting it in one of those boxes, and writing a label on the box (like `age`). Later, when you want the number `20`, you just ask Python to go find the box labeled `age`.

### Rules for Naming Variables (MEMORIZE THESE)
1. Must start with a letter (A-Z, a-z) or an underscore `_`.
2. CANNOT start with a number. (`1name` is invalid. `name1` is valid).
3. Can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, and _). No spaces!
4. Variables are case-sensitive (`age`, `Age`, and `AGE` are three completely different variables).
5. Cannot be a Python keyword (e.g., you cannot name a variable `import` or `print`).

---

## 2. Data Types

Data types tell Python what *kind* of data is stored in the variable so it knows what operations can be performed on it.

| Data Type | Description | Example |
| :--- | :--- | :--- |
| **Integer (int)** | Whole numbers (positive or negative) | `a = 5` |
| **Float (float)** | Decimal numbers | `b = 3.14` |
| **String (str)** | Text, surrounded by quotes | `c = "Arun"` |
| **Boolean (bool)**| True or False (Must be capitalized!) | `d = True` |
| **NoneType (None)**| Represents the absence of a value | `e = None` |

---

## 3. Operators

Operators are special symbols that carry out arithmetic or logical computation.

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division (Always returns a float, e.g., `4/2 = 2.0`)
- `%` Modulo (Returns the remainder, e.g., `5%2 = 1`)

### Assignment Operators
- `=` Assigns a value (`x = 5`)
- `+=` Adds and assigns (`x += 3` is the same as `x = x + 3`)

### Comparison Operators (Always return a Boolean)
- `==` Equals
- `!=` Not equals
- `>` Greater than
- `<` Less than

### Logical Operators
- `and` (True if both are true)
- `or` (True if at least one is true)
- `not` (Reverses the result)

---

## 4. `type()` and Typecasting

### The `type()` function
If you ever forget what is inside a box, use the `type()` function to ask Python!
```python
a = 5
print(type(a)) # Output: <class 'int'>
```

### Typecasting (Type Conversion)
You can convert one data type into another. This is crucial when taking user input.
```python
a = "5"      # This is a string!
b = int(a)   # Now b is the integer 5
print(b + 2) # Output: 7
```

---

## 5. User Input

The `input()` function allows the user to type something in the terminal.
**CRITICAL RULE:** `input()` ALWAYS returns a string, even if the user types a number!

```python
age = input("Enter your age: ") # If I type 20, age is "20" (string)
age = int(age)                  # Convert to integer so we can do math
print(age + 1)                  # 21
```

---

## ⚠️ My Mistakes & Common Confusions
- **Mistake:** Trying to add a string and an integer. `print("Arun" + 5)` will crash with a `TypeError`. You have to cast it: `print("Arun" + str(5))`
- **Mistake:** Forgetting that `5 / 2` results in a float `2.5`. If I need an integer, I should use floor division `5 // 2` which results in `2`.
- **Confusion:** `=` vs `==`. 
  - `a = 5` means "Put 5 inside the box named a".
  - `a == 5` means "Is the thing inside the box named a equal to 5? True or False?"

---
### Next Recommended Step
Now that you have read the theory, head over to the **[Cheat Sheet](./cheatsheet.md)** to lock in the syntax, or jump straight into **[Practice](./practice.md)**.
