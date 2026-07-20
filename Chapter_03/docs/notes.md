---
title: Strings Notes
chapter: 03
difficulty: ⭐⭐☆☆☆
study_time: 2 Hours
revision_time: 30 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Previous Chapter](../../Chapter_02/README.md) | 🏠 [Home](../../README.md) | [Next Chapter](../../Chapter_04/README.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 📝 Chapter 03 Notes: Strings

This is the core textbook for Chapter 03. Read this thoroughly before attempting practice problems.

---

## 1. What is a String?
A string is a sequence of characters enclosed in quotes. It can contain letters, numbers, spaces, or special symbols.

### Creating Strings
```python
# Single quotes
name = 'Arun'

# Double quotes (Useful if the string contains a single quote!)
sentence = "It's a beautiful day"

# Triple quotes (Useful for multi-line strings)
paragraph = '''This is a
multi-line string.'''
```

---

## 2. String Concatenation & F-Strings

### Concatenation (Joining Strings)
You can use the `+` operator to join two strings together.
```python
greeting = "Hello" + " " + "World"
```

### F-Strings (Formatted Strings)
F-strings are the modern, professional way to inject variables directly into a string. You put an `f` before the quotes and wrap variables in `{}`.
```python
name = "Arun"
age = 20
print(f"My name is {name} and I am {age} years old.") 
# Output: My name is Arun and I am 20 years old.
```
> **Quick Win:** Always use f-strings instead of concatenation. It prevents `TypeError`s when trying to add integers to strings!

---

## 3. String Slicing & Indexing

### Indexing (Extracting a single character)
Python strings are indexed starting at `0`.
```text
String:  P  Y  T  H  O  N
Index:   0  1  2  3  4  5
```
`"PYTHON"[0]` gives you `'P'`.

### Positive Slicing (Extracting a chunk)
Syntax: `string[start : stop]` (The `stop` index is **NOT** included!)
```python
word = "PYTHON"
print(word[1:4]) # Output: "YTH" (Indexes 1, 2, and 3)
```

### Negative Slicing
Python allows you to count backward from the end of the string starting at `-1`.
```text
String:   P   Y   T   H   O   N
Negative:-6  -5  -4  -3  -2  -1
```
`word[-1]` gives you the last character: `'N'`.

### The Step Argument
Syntax: `string[start : stop : step]`
```python
word = "PYTHON"
print(word[0:6:2]) # Output: "PTO" (Skips every second letter)

# PRO TIP: How to reverse a string in Python!
print(word[::-1])  # Output: "NOHTYP"
```

---

## 4. String Methods (Functions)

Strings come with built-in functions. They **do not modify the original string**; they return a *new* string.

- `len(str)`: Returns the length (number of characters) of the string.
- `str.endswith("xyz")`: Returns True if the string ends with "xyz".
- `str.count("a")`: Counts how many times "a" appears.
- `str.capitalize()`: Capitalizes the first letter of the string.
- `str.find("word")`: Returns the starting index of the first occurrence of "word". Returns `-1` if not found.
- `str.replace("old", "new")`: Replaces all occurrences of "old" with "new".

---

## 5. Escape Sequences

Sometimes you need to put special characters (like a new line) inside a string. You use a backslash `\` to "escape" the normal behavior.

- `\n` : Creates a new line.
- `\t` : Creates a tab (horizontal space).
- `\'` : Prints a single quote.
- `\\` : Prints a backslash.

```python
print("Hello\nWorld")
# Output:
# Hello
# World
```

---

## ⚠️ My Mistakes & Common Confusions
- **Mistake:** Assuming slicing includes the stop index. `word[0:3]` does NOT include index 3! It stops *before* 3.
- **Confusion:** String Immutability.
  - You **CANNOT** change a character inside an existing string. 
  - `name = "Arun"` 
  - `name[0] = "B"` will crash with a `TypeError`. Strings are immutable!
- **Mistake:** Forgetting the `f` in an f-string. `print("My name is {name}")` will literally just print "My name is {name}".

---
### Next Recommended Step
Now that you have read the theory, head over to the **[Cheat Sheet](./cheatsheet.md)** to lock in the syntax, or jump straight into **[Practice](./practice.md)**.
