---
title: Strings Practice
chapter: 03
difficulty: ⭐⭐☆☆☆
study_time: 1 Hour
revision_time: 20 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Cheat Sheet](./cheatsheet.md) | 🏠 [Home](../../README.md) | [Interview](./interview.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🏋️ Chapter 03 Practice: Strings

*Before writing any code, try to solve these in your head or on paper.*

---

## 🔍 Level 1: Output Prediction (Warm-up)
*Do not run this code. Predict the output.*

**Problem 1.1**
```python
word = "DEVELOPER"
print(word[2:5])
```
> **Concept Tested:** Positive String Slicing.
> **Expected Solution:** `"VEL"` (Indexes 2, 3, and 4. Remember, index 5 is NOT included!)

**Problem 1.2**
```python
word = "DEVELOPER"
print(word[-3:])
```
> **Concept Tested:** Negative String Slicing.
> **Expected Solution:** `"PER"` (Starts at the 3rd to last character and goes to the end).

---

## 🐛 Level 2: Find the Error
*Identify and fix the bug in the following snippets.*

**Problem 2.1**
```python
name = "Arun"
name[0] = "B"
print(name)
```
> **Common Mistake:** Strings are immutable! You cannot change a character by index. Throws a `TypeError`.
> **Fix:** `name = "B" + name[1:]` (Result: "Brun")

**Problem 2.2**
```python
age = 20
print("I am {age} years old.")
```
> **Common Mistake:** Forgetting the `f` prefix for f-strings. This will literally print "I am {age} years old."
> **Fix:** `print(f"I am {age} years old.")`

---

## 💻 Level 3: Coding Questions

### 🟢 Easy
**Q3.1: Length Checker**
- **Task:** Ask the user to input a sentence. Print out the length of the sentence.

### 🟡 Medium
**Q3.2: Formal Name Formatter**
- **Task:** Ask the user to input their first name and last name in all lowercase. Use string methods to capitalize the first letter of both names, and print them out using an f-string.

### 🔴 Hard
**Q3.3: The Replacer**
- **Task:** Ask the user to input a paragraph of text. Then, ask them for a word they want to replace, and the new word they want to replace it with. Print the modified paragraph.
- **Expected Approach:** Use the `str.replace(old, new)` method!

---
### Next Recommended Step
Check out the **[Interview Prep](./interview.md)** page to see how frequently strings are used in coding interviews!
