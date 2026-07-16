# Chapter 04 PS - Lists and Tuples (Practice Set)

---

# Introduction

**What is this topic?**
This is the Practice Set companion to Chapter 4. It focuses on practical applications of Python Lists and Tuples, which are the fundamental sequences you use to store collections of data.

**Why is it important?**
Understanding how to manipulate lists (appending, slicing, sorting) and tuples (indexing, counting) is critical for handling real-world data effectively. You cannot write substantial programs without these data structures.

**Where is it used in real-world projects?**
Lists are used to store data retrieved from a database, handle file contents line by line, and manage dynamic states in your application. Tuples are frequently used to return multiple values from functions or to represent immutable records.

---

# Learning Objectives

After completing this practice set, students should be able to:
- Dynamically populate a list using user input and the `append()` method.
- Sort a list of items using the `.sort()` method.
- Recognize that tuples are immutable and will raise a TypeError if you attempt to modify them.
- Calculate the sum of elements in a list.
- Use the `.count()` method on a tuple to find occurrences of specific values.

---

# Practice Questions (Core Set)

### Problem 1: Storing User Input in a List
Write a program to store seven fruits in a list entered by the user. 

### Problem 2: Sorting Student Marks
Write a program to accept the marks of 6 students and display them in a sorted manner.

### Problem 3: Tuple Immutability
Check that a tuple type cannot be changed in Python. Write a script that creates a tuple and attempts to alter an element to observe the resulting error.

### Problem 4: Summing a List
Write a program to sum a list containing 4 numbers.

### Problem 5: Counting Tuple Elements
Write a program to count the number of zeros (`0`) in the following tuple:
`a = (7, 0, 8, 0, 0, 9)`

---

# Solutions

**Solution to Problem 1:**
```python
fruits = []
fruits.append(input("Enter fruit name 1: "))
fruits.append(input("Enter fruit name 2: "))
fruits.append(input("Enter fruit name 3: "))
fruits.append(input("Enter fruit name 4: "))
fruits.append(input("Enter fruit name 5: "))
fruits.append(input("Enter fruit name 6: "))
fruits.append(input("Enter fruit name 7: "))
print(fruits)
```

**Solution to Problem 2:**
```python
marks = []
marks.append(int(input("Enter the marks of student 1: ")))
marks.append(int(input("Enter the marks of student 2: ")))
marks.append(int(input("Enter the marks of student 3: ")))
marks.append(int(input("Enter the marks of student 4: ")))
marks.append(int(input("Enter the marks of student 5: ")))
marks.append(int(input("Enter the marks of student 6: ")))

marks.sort()
print(marks)
```

**Solution to Problem 3:**
```python
marks1 = (1, 2, 3, 4, 5)
print("Original tuple : ", marks1)
# Trying to change the value will result in a TypeError
marks1[0] = 34 
```

**Solution to Problem 4:**
```python
list1 = [1, 2, 3, 4]
total_sum = list1[0] + list1[1] + list1[2] + list1[3]
# Or simply use the built-in function: total_sum = sum(list1)
print("Sum of the elements of the list : ", total_sum)
```

**Solution to Problem 5:**
```python
a = (7, 0, 8, 0, 0, 9)
count0 = a.count(0) 
print("Count of 0 in the tuple : ", count0)
```

---

# Mini Projects

1. **Student Gradebook Manager**
   - **Difficulty:** Intermediate
   - **Concepts:** Lists, `.sort()`, `sum()`, user input.
   - **Task:** Create a program that continually asks the user for grades, adds them to a list, and then calculates the class average and the highest score.
2. **Immutable Location Tracker**
   - **Difficulty:** Beginner
   - **Concepts:** Tuples.
   - **Task:** Store the GPS coordinates (latitude, longitude) of a user as a tuple. Try to update it in-place and handle the resulting error using basic concepts.

---

# Common Errors

### `TypeError: 'tuple' object does not support item assignment`
- **Why:** Tuples are immutable. Once created, their items cannot be modified, added, or removed.
- **How to Fix:** If you need a collection that changes over time, use a `list` (with square brackets `[]`) instead of a `tuple` (with parentheses `()`).

### `ValueError: invalid literal for int() with base 10: ''`
- **Why:** When asking for marks, if the user hits enter without typing a number, `int()` cannot parse an empty string.
- **How to Fix:** You can validate user input or use `try-except` blocks (which you'll learn in later chapters).

---

# Interview Questions

### 10 Practice Interview Questions
1. What is the fundamental difference between a list and a tuple in Python?
2. Why would you choose to use a tuple instead of a list?
3. What is the syntax for creating an empty list? An empty tuple?
4. How do you add a new item to the end of a list?
5. Can you use `.append()` on a tuple? Why or why not?
6. How do you sort a list of integers in ascending order?
7. How would you count the number of times a specific value appears in a list or tuple?
8. What happens if you try to `sum()` a list containing strings?
9. Is a tuple with a single element written as `(5)` or `(5,)`? Why?
10. Can a list contain tuples as its elements? Can a tuple contain lists?

---

# Summary

This practice set reinforced the differences between mutable and immutable sequence types. You practiced dynamically adding elements to lists, sorting them, and interacting with user input. You also experienced firsthand that tuples cannot be modified once instantiated, which makes them perfect for storing static data like fixed configurations or coordinates.

---

# Folder Structure

```text
Chapter_04 PS/
│
├── readme.md         <-- (You are here)
├── problem_01.py
├── problem_02.py
├── problem_03.py
├── problem_04.py
└── problem_05.py
```
*(Proceed to Chapter 5 to continue the course!)*
