---
title: Variables & Data Types Practice
chapter: 02
difficulty: ⭐☆☆☆☆
study_time: 1 Hour
revision_time: 20 Minutes
interview_importance: Medium
exam_importance: High
---

← [Cheat Sheet](./cheatsheet.md) | 🏠 [Home](../../README.md) | [Interview](./interview.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🏋️ Chapter 02 Practice: Variables & Data Types

*Before writing any code, try to solve these in your head or on paper.*

---

## 🔍 Level 1: Output Prediction (Warm-up)
*Do not run this code. Predict the output.*

**Problem 1.1**
```python
a = "5"
b = "10"
print(a + b)
```
> **Concept Tested:** String concatenation vs Integer addition.
> **Expected Solution:** `"510"` (Because they are strings, Python joins the text together. It does not do math!).

**Problem 1.2**
```python
x = 10
x += 5
print(x == 15)
```
> **Concept Tested:** Assignment operators and Comparison operators.
> **Expected Solution:** `True` (x becomes 15, and `15 == 15` is True).

---

## 🐛 Level 2: Find the Error
*Identify and fix the bug in the following snippets.*

**Problem 2.1**
```python
1_number = 10
print(1_number)
```
> **Common Mistake:** Variables cannot start with a number. Throws a `SyntaxError`.
> **Fix:** `number_1 = 10`

**Problem 2.2**
```python
# Goal: Get user's age and add 5 to it
age = input("Enter your age: ")
print(age + 5)
```
> **Common Mistake:** `input()` always returns a string. You cannot add a string and an integer (`TypeError`).
> **Fix:** `age = int(input("Enter your age: "))`

---

## 💻 Level 3: Coding Questions

### 🟢 Easy
**Q3.1: Greeting App**
- **Task:** Write a Python program that asks the user for their name and then prints `"Good Afternoon, [name]"`.

### 🟡 Medium
**Q3.2: Type Checker**
- **Task:** Write a Python program to define variables holding an integer, a float, a string, and a boolean. Use the `type()` function to print out the type of each variable.

### 🔴 Hard (Timed Challenge: 10 Mins)
**Q3.3: Average Calculator**
- **Task:** Ask the user to input two numbers. Calculate and print the average of those two numbers.
- **Expected Approach:** Take two inputs, `int()` or `float()` cast them, add them together, divide by 2, and print.
- **Common Mistake:** Forgetting PEMDAS! `a + b / 2` will divide `b` by 2 first. You must use `(a + b) / 2`.

---
### Next Recommended Step
Check out the **[Interview Prep](./interview.md)** page to see how tricky variables can get in exams and interviews!
