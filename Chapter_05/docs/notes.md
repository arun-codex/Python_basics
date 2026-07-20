---
title: Dictionaries and Sets Notes
chapter: 05
difficulty: ⭐⭐⭐☆☆
study_time: 2 Hours
revision_time: 30 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Previous Chapter](../../Chapter_04/README.md) | 🏠 [Home](../../README.md) | [Next Chapter](../../Chapter_06/README.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 📝 Chapter 05 Notes: Dictionaries and Sets

This is the core textbook for Chapter 05. Read this thoroughly before attempting practice problems.

---

## 1. Dictionaries

### What is a Dictionary?
A Python dictionary is an unordered, mutable collection of `key:value` pairs. 

### Why do I need it?
If you have a list of student names and a list of their grades, searching for a specific student's grade in a list takes a long time $O(n)$. A dictionary maps the name directly to the grade, making retrieval instantaneous $O(1)$.

### Real-World Analogy
Think of a physical English dictionary. 
- The **Key** is the word you are looking up.
- The **Value** is the definition of that word.
You can't have duplicate words (keys) in a physical dictionary, but multiple words can have the same definition (values).

### Simple Explanation
```python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with data
student = {
    "name": "Arun",
    "age": 20,
    "course": "Computer Science"
}

# Accessing a value using its key
print(student["name"])  # Output: Arun
```

### 🧠 How does Python use it internally?
Under the hood, dictionaries use **Hash Tables**. When you provide a key, Python runs a mathematical "hash function" on it to calculate exactly where the value is stored in memory. This is why looking up a value in a dictionary is incredibly fast, regardless of whether the dictionary has 10 items or 10 million items.

### ⚠️ My Mistakes & Common Confusions
- **Mistake:** Trying to use a list as a dictionary key. `{[1, 2]: "Numbers"}` will throw a `TypeError: unhashable type: 'list'`. 
- **Rule to Memorize:** **Keys must be IMMUTABLE** (Strings, Integers, Tuples). **Values can be ANYTHING** (Lists, other dictionaries, etc.).
- **Mistake:** Using `dict["key_that_doesnt_exist"]`. This throws a `KeyError`. 
- **Quick Win:** Always use `dict.get("key")` instead. It returns `None` if the key doesn't exist, preventing your program from crashing.

### Dictionary Methods
```python
my_dict = {"a": 1, "b": 2}

my_dict.keys()    # Returns all keys: dict_keys(['a', 'b'])
my_dict.values()  # Returns all values: dict_values([1, 2])
my_dict.items()   # Returns key-value tuples: dict_items([('a', 1), ('b', 2)])
my_dict.update({"c": 3}) # Adds or updates pairs
```

---

## 2. Sets

### What is a Set?
A Set is an unordered collection of **unique** elements. 

### Why do I need it?
When you have a list with thousands of duplicate items (like a list of all IP addresses that visited your website today) and you only want to know the *unique* IP addresses.

### Simple Explanation
```python
# Creating an empty set (WARNING!)
# my_set = {}  <-- THIS CREATES A DICTIONARY, NOT A SET!
my_set = set() # This is the correct way.

# Creating a set with data
numbers = {1, 2, 2, 3, 4, 4, 4}
print(numbers) # Output: {1, 2, 3, 4} (Duplicates are instantly removed)
```

### Mathematical Set Operations
Sets in Python support standard mathematical operations:
- **Union (`|`):** Combines elements from both sets.
- **Intersection (`&`):** Elements present in both sets.
- **Difference (`-`):** Elements in Set A but not in Set B.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1 & set2)  # {3}
print(set1 - set2)  # {1, 2}
```

### ⚠️ Things I Always Forget
- Empty dictionary: `d = {}`
- Empty set: `s = set()`
- Sets are **unordered**. You **CANNOT** access elements by index (`my_set[0]` will crash).

---

## 🛑 When to Use vs When NOT to Use

| Data Structure | When to Use | When NOT to Use |
| :--- | :--- | :--- |
| **List** | You need an ordered collection and care about duplicates. | You need to constantly search for specific items (too slow). |
| **Dictionary** | You have data in pairs (ID: Name) and need fast lookups. | You only have single items. |
| **Set** | You need to remove duplicates or do math operations (Union/Intersection). | You care about the order of items. |

---

## 🎓 Exam & Interview Notes
- **Interviews:** Dictionaries are the #1 data structure used in coding interviews (used for frequency maps, caching, two-sum problem). If you need to optimize a slow algorithm, ask yourself: *"Can I use a dictionary/hash map here?"*
- **Exams:** University exams love asking about the difference between `dict.get("key")` and `dict["key"]`. Remember the `KeyError` vs `None` distinction!

---
### Next Recommended Step
Now that you have read the theory, head over to the **[Cheat Sheet](./cheatsheet.md)** to lock in the syntax, or jump straight into **[Practice](./practice.md)**.
