---
title: Lists and Tuples Practice
chapter: 04
difficulty: ⭐⭐⭐☆☆
study_time: 1 Hour
revision_time: 20 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Cheat Sheet](./cheatsheet.md) | 🏠 [Home](../../README.md) | [Interview](./interview.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🏋️ Chapter 04 Practice: Lists & Tuples

*Before writing any code, try to solve these in your head or on paper.*

---

## 🔍 Level 1: Output Prediction (Warm-up)
*Do not run this code. Predict the output.*

**Problem 1.1**
```python
l = [10, 20, 30]
l.append(40)
l.insert(1, 15)
print(l)
```
> **Concept Tested:** List methods mutating the list in place.
> **Expected Solution:** `[10, 15, 20, 30, 40]` (15 is inserted at index 1, pushing 20 to the right).

**Problem 1.2**
```python
t = (5, 10, 15)
t[0] = 100
print(t)
```
> **Concept Tested:** Tuple Immutability.
> **Expected Solution:** Crashes with `TypeError`. Tuples do not support item assignment!

---

## 🐛 Level 2: Find the Error
*Identify and fix the bug in the following snippets.*

**Problem 2.1**
```python
l1 = [5, 2, 9, 1]
l2 = l1.sort()
print(l2)
```
> **Common Mistake:** `.sort()` modifies the list in-place and returns `None`. `l2` is now `None`!
> **Fix:**
> ```python
> l1.sort()
> print(l1)
> ```

---

## 💻 Level 3: Coding Questions

### 🟢 Easy
**Q3.1: Fruit Basket**
- **Task:** Ask the user to input 4 of their favorite fruits one by one. Store them in a list and print the list.

### 🟡 Medium
**Q3.2: Student Marks**
- **Task:** Create a list of 6 random student marks (integers). Use a list method to sort the marks in ascending order, and print the sorted list.

### 🔴 Hard
**Q3.3: Tuple Immutability Trick**
- **Task:** You have a tuple `t = (10, 20, 30)`. You realize you made a mistake and need to change `20` to `25`. Write a script to "change" this tuple.
- **Expected Approach:** You cannot change a tuple directly. You must cast it to a list: `l = list(t)`, modify the list `l[1] = 25`, and then cast it back `t = tuple(l)`.

---
### Next Recommended Step
Lists are the bread and butter of technical interviews. See exactly how they are tested in **[Interview Prep](./interview.md)**.
