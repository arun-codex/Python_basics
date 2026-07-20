---
title: Modules, Comments & pip Practice
chapter: 01
difficulty: ⭐☆☆☆☆
study_time: 30 Minutes
revision_time: 10 Minutes
interview_importance: Low
exam_importance: Medium
---

← [Cheat Sheet](./cheatsheet.md) | 🏠 [Home](../../README.md) | [Interview](./interview.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🏋️ Chapter 01 Practice: Modules, Comments & pip

*These problems are designed to get you comfortable with writing and executing scripts.*

---

## 🔍 Level 1: Find the Error
*Identify and fix the bug in the following snippets.*

**Problem 1.1**
```python
# Print a simple greeting
print "Hello World"
```
> **Common Mistake:** Using Python 2 syntax. In Python 3, `print` is a function and requires parentheses.
> **Fix:** `print("Hello World")`

**Problem 1.2**
```python
// This is a comment
print("Learning Python!")
```
> **Common Mistake:** Using C/Java syntax for comments. Python does not use `//`.
> **Fix:** `# This is a comment`

---

## 💻 Level 2: Coding Questions

### 🟢 Easy
**Q2.1: Print a Poem**
- **Task:** Write a Python program to print "Twinkle Twinkle Little Star" using a single print statement.
- **Hint:** Use multi-line strings `'''` or `"""` inside the `print()` function.

### 🟡 Medium
**Q2.2: The OS Module**
- **Task:** Write a Python program that uses the built-in `os` module to print all the contents of a specific directory.
- **Expected Approach:** You need to `import os` and use the `os.listdir()` function.

### 🔴 External Module Challenge
**Q2.3: Text to Speech**
- **Task:** Install an external module called `pyttsx3` using `pip`. Then, write a script that makes Python speak a sentence out loud!
- **Hint:** Read the documentation for `pyttsx3` on Google if you don't know how to use it. This teaches you how to read external module docs!

---
### Next Recommended Step
Did you figure out how to import the `os` module? Good! Let's look at how exams test this material in **[Interview & Exam Prep](./interview.md)**.
