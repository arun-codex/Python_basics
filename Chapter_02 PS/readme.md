# Chapter 02 PS - Variables & Data Types (Practice Set)

---

# Introduction

**What is this topic?**
This is the Practice Set companion to Chapter 2. This folder contains hands-on exercises designed to drill your understanding of Variables, Data Types, Typecasting, and basic Operators in Python.

**Why is it important?**
Mathematical and logical operations are the core of any algorithm. If you cannot confidently take user input, convert it to the correct type, and manipulate it, you cannot build functional software.

---

# Learning Objectives

After completing this practice set, students should be able to:
- Safely take input from a user using `input()`.
- Identify when to typecast `str` to `int` or `float`.
- Apply arithmetic operators (`+`, `-`, `/`, `%`, `**`).
- Use comparison operators to evaluate boolean logic.

---

# Practice Questions (Core Set)

### Problem 1: Addition
Write a Python program to add two hardcoded numbers and print the result.

### Problem 2: Remainder (Modulo)
Write a Python program to find the remainder when a number is divided by `z` (assume `z` is 2). Use the modulo operator.

### Problem 3: Type Checking Input
Check the type of the variable assigned using `input()`. Print it out to prove that `input()` always returns a string.

### Problem 4: Comparison Operator
Use comparison operators to find out whether a given variable `a` is greater than `b` or not. Take `a = 34` and `b = 80`.

### Problem 5: Average of Two Numbers
Write a Python program to find the average of two numbers entered by the user.

### Problem 6: Calculate Square
Write a Python program to calculate the square of a number entered by the user.

---

# Solutions

**Solution to Problem 3:**
```python
user_input = input("Enter anything: ")
# Even if the user types a number, it will print <class 'str'>
print(type(user_input))
```

**Solution to Problem 5:**
```python
# Taking input and immediately casting it to integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Parentheses are required because division has higher precedence than addition
average = (num1 + num2) / 2
print("The average is:", average)
```

**Solution to Problem 6:**
```python
num = int(input("Enter a number to square: "))
# The ** operator is used for exponents
square = num ** 2
print("The square of", num, "is", square)
```

---

# Mini Projects

1. **Tip Calculator**
   - **Difficulty:** Beginner
   - **Task:** Ask user for bill amount, typecast to float, multiply by `1.20` to get a 20% tip, and print the total.
2. **Even or Odd Checker**
   - **Difficulty:** Beginner
   - **Task:** Ask user for number, use `% 2`, and output a boolean (`True` if even).

---

# Common Errors

### `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
- **Why:** You took input (which is a string) and tried to add it to a hardcoded integer.
- **How to Fix:** `user_num = int(input("Enter number: "))`

---

# Interview Questions

### 10 Practice Interview Questions
1. Why does `input("Enter age:") + 5` cause a crash?
2. What operator is used to find the remainder of a division?
3. How do you square a number without importing the `math` module?
4. What is the difference between `/` and `//`?
5. Write a script to swap two variables on a whiteboard.
6. What will `type(3.14)` output?
7. How do you convert a float to an integer? What happens to the decimal?
8. What is the result of `34 > 80`?
9. Is `age` the same variable as `Age` in Python?
10. What does the `**` operator do?

---

# Folder Structure

```text
Chapter_02 PS/
│
├── readme.md         <-- (You are here)
├── Problem_1.py
├── Problem_2.py
├── Problem_3.py
├── Problem_4.py
├── Problem_5.py
└── Problem_6.py
```
*(Proceed to Chapter 3 to continue the course!)*
