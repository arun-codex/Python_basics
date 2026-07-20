---
title: Lists and Tuples Notes
chapter: 04
difficulty: ⭐⭐⭐☆☆
study_time: 2 Hours
revision_time: 30 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Previous Chapter](../../Chapter_03/README.md) | 🏠 [Home](../../README.md) | [Next Chapter](../../Chapter_05/README.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 📝 Chapter 04 Notes: Lists & Tuples

This is the core textbook for Chapter 04. Read this thoroughly before attempting practice problems.

---

## 1. Introduction to Lists

### What is a List?
A list is a container that can store a sequence of values. Unlike variables which hold one item, a list can hold 10, 100, or a million items.

### Creating a List
Lists are created using square brackets `[]`. The items inside are separated by commas.
```python
fruits = ["Apple", "Banana", "Cherry"]
```

### Lists can hold ANY Data Type
A single list can hold strings, integers, floats, and booleans all at the same time.
```python
mixed_list = ["Arun", 20, 5.11, True]
```

---

## 2. Accessing & Slicing Lists

You access elements in a list exactly the same way you access characters in a string: **Zero-Based Indexing**.

```python
fruits = ["Apple", "Banana", "Cherry", "Date"]
print(fruits[0])   # Output: Apple
print(fruits[-1])  # Output: Date (Last item)

# Slicing works identically to strings!
print(fruits[1:3]) # Output: ['Banana', 'Cherry']
```

---

## 3. The Superpower of Lists: Mutability

**Strings are Immutable.** You cannot change a character in a string.
**Lists are Mutable.** You CAN change an item in a list!

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Blueberry"

print(fruits) # Output: ['Apple', 'Blueberry', 'Cherry']
```
> This is a massive concept. We completely overwrote index 1 ("Banana") with a new value.

---

## 4. List Methods (Functions)

Because lists are mutable, many list methods modify the original list **in-place** (they don't return a new list; they physically alter the one in memory).

Assume `l1 = [1, 8, 7, 2, 21, 15]`

- `l1.sort()`: Sorts the list in ascending order. (Modifies `l1`).
- `l1.reverse()`: Reverses the list. (Modifies `l1`).
- `l1.append(8)`: Adds `8` to the **end** of the list.
- `l1.insert(3, 8)`: Inserts `8` at index `3`. Pushes everything else to the right.
- `l1.pop(2)`: Removes and returns the item at index `2`.
- `l1.remove(21)`: Searches for the value `21` and removes the *first* occurrence of it.

---

## 5. Introduction to Tuples

### What is a Tuple?
A Tuple is exactly like a list, but with one major difference: **Tuples are Immutable.** Once you create a tuple, you can never change, add, or remove items from it.

### Creating a Tuple
Tuples are created using parentheses `()`.
```python
t = (1, 2, 4, 5)
```
> **Warning:** Creating a tuple with a single item requires a comma! `t = (1,)`. If you just write `t = (1)`, Python thinks it's a math expression and makes it an integer.

### Why use Tuples?
If they do less than lists, why use them? Because they are immutable, they are faster and safer. If you have data that should *never* change (like days of the week, or coordinates on a map), store it in a Tuple to prevent accidental bugs.

### Tuple Methods
Because they are immutable, tuples only have two main methods:
- `t.count(1)`: Returns the number of times `1` appears in the tuple.
- `t.index(5)`: Returns the index of the first occurrence of `5`.

---

## ⚠️ My Mistakes & Common Confusions
- **Mistake:** Trying to modify a string like a list (`name[0] = 'X'`). This fails!
- **Mistake:** Trying to modify a tuple like a list (`t[0] = 5`). This fails!
- **Confusion:** `append()` vs `insert()`. `append` always goes to the very end. `insert` goes exactly where you tell it to go.
- **Trap:** Forgetting the comma in a single-item tuple: `t = (1)`.

---
### Next Recommended Step
Now that you have read the theory, head over to the **[Cheat Sheet](./cheatsheet.md)** to lock in the syntax, or jump straight into **[Practice](./practice.md)**.
