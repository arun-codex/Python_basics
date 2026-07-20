---
title: Dictionaries and Sets Practice
chapter: 05
difficulty: ⭐⭐⭐☆☆
study_time: 2 Hours
revision_time: 20 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Cheat Sheet](./cheatsheet.md) | 🏠 [Home](../../README.md) | [Interview](./interview.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🏋️ Chapter 05 Practice: Dictionary and Sets

*Before writing any code, try to solve these in your head or on paper.*

---

## 🔍 Level 1: Output Prediction (Warm-up)
*Do not run this code. Predict the output.*

**Problem 1.1**
```python
d = {"a": 1, "b": 2, "a": 3}
print(d["a"])
```
> **Concept Tested:** Dictionary Key Overwriting.
> **Expected Solution:** `3` (Keys must be unique; the last assignment overwrites previous ones).

**Problem 1.2**
```python
s = {1, 2, 2, 3}
print(len(s))
```
> **Concept Tested:** Set Uniqueness.
> **Expected Solution:** `3` (The set automatically drops the duplicate `2`).

---

## 🐛 Level 2: Find the Error
*Identify and fix the bug in the following snippets.*

**Problem 2.1**
```python
# Goal: Create an empty set and add the number 5
my_set = {}
my_set.add(5)
```
> **Common Mistake:** `{}` creates an empty dictionary, not an empty set. `add()` is a set method, so this throws an `AttributeError`.
> **Fix:** `my_set = set()`

**Problem 2.2**
```python
# Goal: Map coordinates to a location
locations = {
    [10, 20]: "Home"
}
```
> **Common Mistake:** Lists are mutable and cannot be used as dictionary keys. Throws `TypeError: unhashable type: 'list'`.
> **Fix:** Use a tuple instead: `(10, 20): "Home"`.

---

## 💻 Level 3: Coding Questions

### 🟢 Easy
**Q3.1: Dictionary Lookup**
- **Task:** Create a dictionary of 3 Hindi words with their English translations. Ask the user to input a Hindi word and print the English translation.
- **Hint:** Use `.get()` so the program doesn't crash if they type a wrong word!

### 🟡 Medium
**Q3.2: Unique Numbers**
- **Task:** Ask the user to input 5 numbers (they might input duplicates). Print the total number of *unique* numbers they entered.
- **Concept:** Converting a list to a set.

### 🔴 Hard (Timed Challenge: 15 Mins)
**Q3.3: Word Frequency Counter**
- **Task:** Given a string `"apple banana apple orange banana apple"`, write a script to count how many times each word appears.
- **Expected Approach:** Split the string into a list. Loop through the list. If the word is already in a dictionary, increment its value by 1. If it's not, set its value to 1.
- **Time Complexity:** $O(n)$

---
### Next Recommended Step
Did you struggle with the Word Frequency Counter? That is a classic interview question! Check out the **[Interview Prep](./interview.md)** page to see how companies ask it.
