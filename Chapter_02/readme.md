# Chapter 02 - Python Variables and Data Types

---

# Introduction

**What is this topic?**
This chapter introduces the fundamental building blocks of any program: **Variables** and **Data Types**. A variable is a named container that holds data in memory. Data types define the *kind* of data that variable holds (like whole numbers, text, or true/false values).

**Why is it important?**
You cannot write a useful program without storing and manipulating data. Variables allow your code to be dynamic. Instead of writing a calculator that only ever adds `2 + 2`, you use variables to add `a + b`, where `a` and `b` can be anything the user inputs.

**Why should every Python developer learn it?**
Unlike languages like C++ or Java, Python is dynamically typed. It figures out the data type for you. However, you must still deeply understand data types to avoid crashing your program by doing impossible operations (like adding a word to a number).

**Where is it used in real-world projects?**
- **Variables:** Used everywhere to store user input, database records, file paths, and mathematical results.
- **Data Types:** Used to ensure forms are filled out correctly (e.g., ensuring an age is an Integer, not a String).

**Industry use cases:**
- **Web Development:** Storing a logged-in user's name in a string variable.
- **Data Science:** Converting text data (Strings) into numerical data (Integers/Floats) so machine learning models can process it.
- **Game Development:** Keeping track of a player's health in a float variable (`health = 95.5`).

---

# Learning Objectives

After completing this chapter, students should be able to:
- Understand how to declare variables and follow Python's naming conventions.
- Identify and differentiate between basic data types (`int`, `float`, `str`, `bool`, `None`).
- Use Python's built-in `type()` function to inspect data.
- Perform operations using arithmetic and comparison operators.
- Take user input using `input()` and perform typecasting to solve beginner problems.

---

# Theory

### Variables
Think of your computer's RAM (Memory) as a massive warehouse full of empty boxes. 
When you create a variable, you are doing three things:
1. Finding an empty box.
2. Putting a piece of data inside it.
3. Writing a label (the variable's name) on the outside of the box so you can find it later.

### Data Types
Data types tell Python what *can* and *cannot* be done with a box's contents.
- **Integer (`int`)**: Whole numbers. You can do math with them.
- **Float (`float`)**: Decimal numbers. You can do math with them.
- **String (`str`)**: Text. You cannot do math with text (though you can concatenate it).
- **Boolean (`bool`)**: Represents Truth (`True` or `False`). Essential for logic.
- **NoneType (`None`)**: A special type representing the complete absence of a value (an empty box).

### Operators
Operators are symbols that perform actions on variables.
- **Arithmetic:** `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `%` (modulo - gets remainder).
- **Comparison:** `==` (equals), `!=` (not equals), `>` (greater than).
- **Logical:** `and`, `or`, `not`.

---

# Syntax

```python
age = 25
name = "Arun"
is_admin = True
```
- `age`: The identifier (variable name).
- `=`: The assignment operator. It assigns the value on the right to the variable on the left.
- `25`: The data (an integer) stored in the variable.

---

# Concepts Covered

- [x] Variable Declaration
- [x] Variable Naming Rules
- [x] Data Types (`int`, `float`, `str`, `bool`, `None`)
- [x] Type Checking (`type()`)
- [x] Typecasting (Converting types)
- [x] Arithmetic Operators
- [x] Comparison Operators
- [x] User Input (`input()`)

---

# Important Functions

### 1. `type()`
- **Purpose:** Returns the data type of the variable or value passed to it.
- **Syntax:** `type(object)`
- **Parameters:** Any object or variable.
- **Return Value:** A class representing the type.
- **Example:** `print(type(42))`
- **Output:** `<class 'int'>`
- **Common Mistakes:** Trying to use it to change a type (e.g., `type(x) = int`). It only *checks* the type.
- **Interview Tips:** Essential for debugging `TypeError` issues.

### 2. `input()`
- **Purpose:** Pauses program execution to allow the user to type text into the terminal.
- **Syntax:** `input(prompt)`
- **Parameters:** `prompt` (Optional String) - The text shown to the user.
- **Return Value:** A `str` (String) representing what the user typed.
- **Example:** `name = input("Enter name: ")`
- **Output:** (Waits for input)
- **Common Mistakes:** Forgetting that `input()` ALWAYS returns a string. If you need a number, you must typecast it.

### 3. Typecasting Functions (`int()`, `float()`, `str()`, `bool()`)
- **Purpose:** Converts data from one type to another.
- **Example:** `age = int("25")` converts a string to an integer.

---

# Methods

(Basic data types like Integers don't have many heavily used methods, but Strings do. String methods are covered extensively in Chapter 3).

---

# Memory Visualization

Unlike languages where variables are fixed memory locations holding values, in Python, **variables are pointers** (references).

```python
a = 10
b = 10
```
In memory:
Python creates an integer object `10`.
Variable `a` points to `10`.
Variable `b` points to the *exact same* `10`.

```text
a -----> [ Object: int(10) ] <----- b
```

If you do `a = 20`, Python creates a NEW integer object `20` and moves `a`'s pointer to it. `b` still points to `10`.

---

# Internal Working

Python uses a memory management system with a private heap. All objects (variables) are stored in this heap. Python manages this automatically using **Reference Counting** and a **Garbage Collector**. When a variable's reference count drops to zero (meaning no labels point to that box anymore), the garbage collector automatically deletes the object to free up RAM.

When you evaluate `10 + 5.5`, Python internally converts the integer `10` to a float `10.0` before adding them, returning a float `15.5`. This is called **implicit type conversion**.

---

# Code Examples

### 20 Beginner Examples

```python
# 1. Integer variable
age = 25

# 2. Float variable
price = 19.99

# 3. String variable
name = "Arun"

# 4. Boolean variable
is_student = True

# 5. None variable
score = None

# 6. Printing a variable
print(age)

# 7. Checking type of integer
print(type(age)) # <class 'int'>

# 8. Checking type of float
print(type(price)) # <class 'float'>

# 9. Checking type of boolean
print(type(is_student)) # <class 'bool'>

# 10. Addition operator
total = 10 + 5

# 11. Subtraction operator
diff = 10 - 5

# 12. Multiplication operator
prod = 10 * 5

# 13. Division operator (Always returns float)
div = 10 / 2 # 5.0

# 14. Modulo operator (Returns remainder)
rem = 10 % 3 # 1

# 15. Comparison (Equals)
print(10 == 10) # True

# 16. Comparison (Greater than)
print(10 > 5) # True

# 17. Logical AND
print(True and False) # False

# 18. Logical OR
print(True or False) # True

# 19. Taking basic input
# user_name = input("Enter name: ")

# 20. Reassigning a variable
age = 26
```

### 10 Intermediate Examples

```python
# 1. Floor division (Returns integer part of division)
floor_div = 10 // 3 # 3

# 2. Exponentiation (Power)
power = 2 ** 3 # 8

# 3. Typecasting String to Integer
num_str = "100"
num_int = int(num_str)

# 4. Typecasting Integer to String
age = 25
age_str = str(age)

# 5. Typecasting Float to Integer (Truncates decimal)
price = 19.99
price_int = int(price) # 19

# 6. Typecasting Integer to Boolean
# 0 is False, any other number is True
print(bool(0)) # False
print(bool(1)) # True

# 7. Taking integer input safely
# user_age = int(input("Enter your age: "))

# 8. Multiple assignment
a, b, c = 1, 2, 3

# 9. Swapping variables without a temporary variable
a, b = b, a

# 10. Chaining comparison operators
x = 5
print(1 < x < 10) # True
```

### 5 Advanced Examples

```python
# 1. Using the id() function to see memory addresses
x = 10
print(id(x))

# 2. Demonstrating variable interning (small integers share the same memory)
a = 256
b = 256
print(a is b) # True (Checks memory address, not just value)

# 3. Bitwise operators (manipulating data at bit level)
print(5 & 3) # Bitwise AND -> Output: 1

# 4. Complex number data type
c = 3 + 4j
print(type(c)) # <class 'complex'>

# 5. Using sys.getsizeof to check memory footprint of data types
import sys
print(sys.getsizeof(0)) # Typically 24 bytes on 64-bit systems
```

---

# Practice Questions

### 10 Beginner Problems
1. Create a variable `a` with value 10 and print it.
2. Create a variable with a float and print its type.
3. Write a program to add two hardcoded numbers and print the result.
4. Write a program to find the remainder when 15 is divided by 4.
5. Create a boolean variable `is_raining` and set it to False.
6. Compare if 5 is greater than 3 and print the result.
7. Compare if 10 is equal to 10.0 and print the result.
8. Create a variable holding the string "Python" and print its type.
9. Ask the user for their name using `input()` and print it.
10. Reassign an integer variable to a string variable and print it.

### 10 Intermediate Problems
1. Write a program to find the average of two numbers entered by the user.
2. Ask the user for a number, typecast it to an integer, square it, and print the result.
3. Ask the user for two numbers and print `True` if the first is greater than the second, else `False`.
4. Swap the values of two variables `x` and `y` using multiple assignment.
5. Write a program that divides a user's input by 2 using floor division `//`.
6. Convert a boolean `True` to an integer and print the result.
7. Convert an empty string `""` to a boolean and print the result.
8. Demonstrate the difference between `/` and `//` in Python.
9. Write a program to calculate the area of a rectangle (length and width from user input).
10. Calculate the cube of a number entered by the user.

### 10 Advanced Problems
1. Write a program to calculate compound interest given Principal, Rate, and Time inputs.
2. Check if a number inputted by a user is even or odd using the modulo `%` operator.
3. Prove that small integers are cached in Python using the `is` operator and the `id()` function.
4. Use bitwise operators to multiply a number by 2 (Left shift `<<`).
5. Extract the last digit of an integer using the modulo operator.
6. Reverse a two-digit integer using math operators (`//` and `%`).
7. Write a script that deliberately throws a `ValueError` during typecasting.
8. Calculate the memory size of an integer, a float, and a boolean using the `sys` module.
9. Implement a logic gate (like XOR) using basic `and`, `or`, `not` operators.
10. Write a program to convert Celsius to Fahrenheit based on user input.

---

# Solutions

**Intermediate Problem 1 (Average):**
```python
# Taking input and casting to float so we can handle decimals
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Parentheses ensure addition happens before division (BODMAS/PEMDAS)
average = (num1 + num2) / 2
print("The average is:", average)
```

**Advanced Problem 2 (Even or Odd):**
```python
num = int(input("Enter a number: "))
# Any even number divided by 2 has a remainder of 0
is_even = (num % 2 == 0)
print("Is the number even?", is_even)
```

---

# Mini Projects

1. **Simple Calculator**
   - **Difficulty:** Beginner
   - **Skills Learned:** Variables, Operators, Typecasting.
   - **Concepts Used:** Input two numbers and output their sum, diff, prod, and div.
2. **Age Calculator**
   - **Difficulty:** Beginner
   - **Skills Learned:** User input, basic subtraction.
   - **Concepts Used:** Input birth year, subtract from current year.
3. **Tip Calculator**
   - **Difficulty:** Intermediate
   - **Skills Learned:** Floats, Percentages.
   - **Concepts Used:** Calculate 15% tip on a restaurant bill input.
4. **Temperature Converter**
   - **Difficulty:** Intermediate
   - **Skills Learned:** Arithmetic formulas.
   - **Concepts Used:** Celsius to Fahrenheit conversion.
5. **BMI Calculator**
   - **Difficulty:** Intermediate
   - **Skills Learned:** Exponents `**`, Division `/`.
   - **Concepts Used:** weight / (height ** 2).
6. **Currency Converter**
   - **Difficulty:** Intermediate
   - **Skills Learned:** Constants, Multiplication.
   - **Concepts Used:** Hardcoded exchange rate applied to user input.
7. **Distance Formula**
   - **Difficulty:** Advanced
   - **Skills Learned:** Importing `math`, square roots.
   - **Concepts Used:** Calculate distance between (x1, y1) and (x2, y2).
8. **Seconds to HH:MM:SS**
   - **Difficulty:** Advanced
   - **Skills Learned:** Modulo `%`, Floor Division `//`.
   - **Concepts Used:** Convert a massive integer of seconds into hours, minutes, and remaining seconds.
9. **Salary Breakdown**
   - **Difficulty:** Advanced
   - **Skills Learned:** Multiple calculations, chaining operations.
   - **Concepts Used:** Gross pay minus various tax percentages to get net pay.
10. **Data Type Inspector**
    - **Difficulty:** Intermediate
    - **Skills Learned:** `type()`, `id()`.
    - **Concepts Used:** A script that takes a hardcoded value, prints its type, its memory address, and its boolean representation.

---

# Common Errors

### `TypeError`
- **Why:** You tried to perform an operation on incompatible data types.
- **When:** `print("Age: " + 25)`
- **How to Fix:** Typecast the integer to a string: `print("Age: " + str(25))`

### `ValueError`
- **Why:** You passed a value of the correct type to a function, but the value is inappropriate.
- **When:** `int("Arun")` (You can't turn letters into a base-10 integer).
- **How to Fix:** Ensure strings contain only digits before passing them to `int()`.

### `SyntaxError`
- **Why:** Invalid variable naming or grammatical mistakes.
- **When:** `1st_name = "Arun"` (Variables cannot start with numbers).
- **How to Fix:** Rename to `first_name`.

---

# Best Practices

- **Naming Conventions:** Use `snake_case` for variable names (e.g., `user_age`, `total_price`). Do not use camelCase in Python for variables.
- **Meaningful Names:** Avoid names like `x` and `y` unless doing coordinate math. Use descriptive names like `customer_id`.
- **Constants:** Python doesn't have true constants, but by convention, we use ALL_CAPS for variables that shouldn't change (e.g., `PI = 3.14159`).
- **PEP 8:** Put a space around operators. `x = 5 + 3` is correct. `x=5+3` is poor style.

---

# Performance Tips

- **Memory Usage:** Python integers have arbitrary precision (they can be infinitely large, limited only by your RAM). This makes them slightly slower and heavier in memory than C-integers, but you never suffer from "Integer Overflow" bugs.
- **Optimization:** If you are doing massive mathematical operations (like 3D graphics or huge datasets), do not use raw Python `float` and `int` types in loops. Use the `NumPy` library.

---

# Real World Applications

- **Game Development:** `health -= damage` to calculate HP loss.
- **Web Development:** Storing form data in variables before saving to a database.
- **Finance:** Using Floats (or ideally the `decimal` module for precision) to calculate interest rates and balances.
- **Automation:** Using Booleans (`True`/`False`) as flags to determine if a task finished successfully or failed.

---

# Interview Questions

### 20 Beginner Questions
1. What is a variable?
2. What are the rules for naming variables in Python?
3. What is an integer?
4. What is a float?
5. How do you check the data type of a variable?
6. Is Python case-sensitive regarding variables?
7. What is typecasting?
8. What does `input()` always return?
9. What is the difference between `=` and `==`?
10. What does the modulo `%` operator do?
11. How do you square a number in Python?
12. Can a variable name start with a number?
13. What is a boolean?
14. What are the two boolean values?
15. What does the `and` operator do?
16. How do you divide two numbers and get an integer result?
17. How do you divide two numbers and get a float result?
18. What is string concatenation?
19. How do you write a multi-word variable name according to PEP 8?
20. What is a `SyntaxError`?

### 20 Intermediate Questions
1. Explain dynamic typing vs static typing. Is Python statically typed?
2. What happens if you try to `int("10.5")`?
3. How do you swap two variables without a third temporary variable?
4. What is the output of `bool("")`?
5. What is the output of `bool("False")`?
6. Explain the difference between the `is` operator and `==`.
7. What does the `id()` function do?
8. Why does `0.1 + 0.2` not exactly equal `0.3` in Python?
9. What is multiple assignment and give an example.
10. How are variables stored in memory in Python?
11. What is reference counting?
12. What is garbage collection?
13. What is the output of `10 // 3`?
14. Can you use reserved keywords (like `if`, `def`) as variable names?
15. What is the `None` type?
16. Explain implicit vs explicit type conversion.
17. What is an assignment operator besides `=`? (e.g., `+=`).
18. How do you evaluate the truthiness of an integer? (0 is False, rest are True).
19. How does Python handle infinitely large integers?
20. Why shouldn't you use built-in function names like `list` or `str` as variable names?

### 20 Advanced Questions
1. Explain Integer Interning in CPython. Which integers are cached by default?
2. How does the `id()` of immutable types change upon reassignment?
3. What is the `sys.getrefcount()` function used for?
4. Explain how bitwise operators work under the hood.
5. Why is the `decimal` module preferred over `float` in financial applications?
6. What is the Global Interpreter Lock (GIL) and does it affect variable assignment?
7. Explain variable shadowing.
8. What are `__dunder__` variables?
9. How do you unpack an iterable into variables using the `*` operator?
10. How does the `type()` function differ from `isinstance()`?
11. What are complex numbers in Python and how do you access the real and imaginary parts?
12. How does `math.isclose()` help with floating-point inaccuracy?
13. Write a Python script to prove that variables are references, not values.
14. How do you create an alias for a variable?
15. What happens at the C level when Python garbage collects a variable?
16. What is a memory leak in Python and how can variables cause it?
17. Explain the concept of strong vs weak typing.
18. Can you change the type of an object in memory directly?
19. What is the `hex()`, `oct()`, and `bin()` function used for?
20. How do you enforce static typing hints in Python 3?

---

# Interview Answers (Selected)

**Q: Explain dynamic typing vs static typing. Is Python statically typed?**
**A:** Python is **dynamically typed**. You do not need to declare the variable type (like `int x = 5` in C). Python infers the type at runtime based on the assigned value. You can also reassign a variable to a different type later (`x = "Hello"`).

**Q: Why does `0.1 + 0.2` not exactly equal `0.3`?**
**A:** This is due to floating-point arithmetic. Computers represent decimals in binary base-2 fractions. Many decimal fractions cannot be represented exactly in binary, leading to tiny rounding errors (e.g., `0.30000000000000004`).

**Q: What is Integer Interning?**
**A:** In CPython, small integers from `-5` to `256` are pre-allocated when Python starts. When you assign `a = 10` and `b = 10`, they point to the exact same object in memory to save space and speed up execution.

---

# Cheat Sheet

| Topic | Syntax | Example | Output | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Variables** | `name = value` | `age = 20` | Stores 20 | Use snake_case |
| **Integer** | `int` | `x = 5` | `5` | Whole numbers |
| **Float** | `float` | `y = 3.14` | `3.14` | Decimals |
| **String** | `str` | `s = "Hi"` | `Hi` | Text in quotes |
| **Boolean** | `bool` | `b = True` | `True` | `True` or `False` |
| **Input** | `input(prompt)`| `name = input()`| Gets string | ALWAYS returns str |
| **Type Check**| `type(x)` | `type(5)` | `<class 'int'>`| Returns data type |
| **Cast Int** | `int(x)` | `int("5")` | `5` | Casts str to int |

---

# Mind Map

```text
Chapter 2: Variables & Data Types
├── Variables
│   ├── Naming Rules (No numbers at start)
│   ├── snake_case
│   └── Memory Pointers (References)
├── Data Types
│   ├── Numbers (int, float, complex)
│   ├── Text (str)
│   ├── Logic (bool)
│   └── Null (NoneType)
├── Operators
│   ├── Arithmetic (+, -, *, /, //, %, **)
│   ├── Assignment (=, +=, -=)
│   └── Comparison (==, !=, >, <)
└── Utility
    ├── input()
    ├── type()
    └── Typecasting (int(), float(), str())
```

---

# Summary

Variables and data types form the bedrock of programming. You learned how to create variables, follow proper naming conventions, and utilize Python's primary data types (`int`, `float`, `str`, `bool`, `None`). You also learned how to manipulate these using operators and how to take input from a user, allowing you to build dynamic, interactive scripts.

---

# Key Takeaways

- Variables are created the moment you assign a value to them using `=`.
- Variable names cannot start with a number or contain spaces.
- `type()` is your best friend for checking what kind of data you are working with.
- `input()` always returns a string. You must use typecasting like `int()` if you want to do math with the input.
- Python variables are references (pointers) to objects in memory.

---

# Resources

- **Official Python Documentation:** [docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
- **Relevant PEPs:** PEP 8 (Style Guide for Naming Conventions)
- **Books:** "Python Crash Course"
- **Practice Websites:** HackerRank (Basic Operations)

---

# Folder Structure

```text
Chapter_02/
│
├── readme.md               <-- (You are here)
├── 01_Variables.py         
├── 02_datatypes.py         
├── 03_rule_variables.py    
├── 04_operators.py         
└── notes.txt               
```

---

# Progress Tracker

- [x] Theory
- [x] Examples
- [x] Exercises
- [x] Mini Project
- [x] Interview Questions
- [x] Cheat Sheet
- [x] Mind Map

---

# Revision Notes

- **Variable:** Container for data. `age = 20`.
- **Naming:** Must start with a letter or `_`. Only alphanumeric and `_`. Case-sensitive.
- **Types:**
  - `int`: `5`
  - `float`: `5.5`
  - `str`: `"Hello"`
  - `bool`: `True` / `False`
- **Operators:** `/` is float division (returns decimal), `//` is floor division (returns integer), `%` is modulo (remainder), `**` is exponent.
- **Conversion:** `int("10")` makes it a number. `str(10)` makes it text.

---

# Cheat Sheet Table

*(Refer to the comprehensive table in the Cheat Sheet section above)*

---

# Common Interview Programs

**1. Swap Two Variables**
```python
a = 10
b = 20
a, b = b, a # Pythonic way to swap without a temp variable
```
*Explanation:* Python creates a tuple on the right side and unpacks it into the variables on the left, swapping their references seamlessly.

**2. Check Even or Odd**
```python
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
*Explanation:* The modulo `%` operator returns the remainder. Any even number divided by 2 has a remainder of 0.

---

# Challenge Problems

1. Given an integer of seconds, calculate the hours, minutes, and seconds.
2. Given a 3-digit number, calculate the sum of its digits using only math operators (no string slicing).
3. Find the minimum number of currency notes required to form a given amount using `/` and `%`.
4. Swap three variables `a, b, c = b, c, a`.
5. Prove floating-point inaccuracy by writing a script that prints the boolean result of `0.1 + 0.2 == 0.3`.

---

# Assignments

1. Write a script that asks the user for their weight in pounds and converts it to kilograms.
2. Write a script that demonstrates every single arithmetic operator using variables `x = 10` and `y = 3`.
3. Try to use a Python keyword (`def` or `if`) as a variable name. Observe the error.
4. Calculate the area of a circle. Prompt the user for the radius and use `3.14159` for Pi.
5. Create variables of all 4 main types. Print the variable, and on the next line print its type.

---

# Frequently Asked Questions (FAQs)

**Q: Why do I get a TypeError when adding text and numbers?**
A: Python is strongly typed. It refuses to guess what you mean when you try to add `"Apples"` and `5`. You must explicitly cast the number to a string using `str(5)`.

**Q: Can I change a variable's type?**
A: Yes. Because Python is dynamically typed, `x = 5` followed immediately by `x = "Hello"` is perfectly legal. The variable `x` just points to a new object.

---

# Keywords

- **Variable:** Identifier used to store values.
- **Data Type:** Classification that dictates what operations can be performed on the data.
- **Operator:** Symbol that tells the compiler to perform a specific mathematical or logical manipulation.
- **Typecasting:** Converting data from one type to another.

---

# Glossary

- **Dynamic Typing:** The interpreter assigns a type to variables at runtime based on their value.
- **Identifier:** The user-defined name of a variable, function, or class.
- **Boolean:** A binary variable, having two possible values called "true" and "false".

---

# Notes

- **Warning:** `input()` returns a string. If the user types `5`, it is `"5"`. If you do `input() + input()`, typing `5` and `5` will yield `"55"`, not `10`! You must use `int(input())`.
- **Best Practice:** Keep variable names descriptive. Code is read much more often than it is written.

---

# Do's and Don'ts

| ✅ Do | ❌ Don't |
| :--- | :--- |
| Use `snake_case` (e.g. `first_name`) | Use CamelCase for variables (e.g. `firstName`) |
| Use `int(input())` when expecting numbers | Assume `input()` gives you a number |
| Keep names descriptive | Use single letter names like `x`, `y`, `z` (unless mathematical) |

---

# Revision Checklist

- [ ] I can create variables.
- [ ] I know the rules for naming variables.
- [ ] I understand `int`, `float`, `str`, and `bool`.
- [ ] I can check types using `type()`.
- [ ] I can cast types using `int()` and `str()`.
- [ ] I know the difference between `/`, `//`, and `%`.

---

# Quick Quiz

1. Which is a valid variable name?
   - A) `1st_place`
   - B) `first-place`
   - C) `first_place`
2. What does `10 % 3` output?
   - A) 3
   - B) 1
   - C) 3.33
3. What data type is `False`?
   - A) String
   - B) Boolean
   - C) Integer

*(Answers: 1: C, 2: B, 3: B)*

---

# Flash Cards

**Q:** What function checks the data type?
**A:** `type()`

**Q:** What operator returns the remainder of a division?
**A:** Modulo `%`

**Q:** Are Python variables dynamically typed or statically typed?
**A:** Dynamically typed.

---

# Next Chapter

In the next chapter, we will explore **Strings** in depth. You will learn how to manipulate text, slice it into pieces, format it beautifully, and use powerful built-in string methods!
