# Chapter 02 — Level 02: Intermediate

## Variables, Data Types, Operators & Input

1. Predict the output:
   
   ```python
   x = 10
   y = 3
   print(x + y)
   print(x / y)
   print(x % y)
   print(x // y)
   ```

2. Predict the exact `type()` output for variables containing an int, float, str, bool, and None.

3. Explain why this causes an error and fix it:
   
   ```python
   age = input("Enter your age: ")
   print(age + 5)
   ```

4. Predict the output and type:
   
   ```python
   x = "10"
   y = int(x)
   print(y + 5)
   print(type(y))
   ```

5. Find and fix the error:
   
   ```python
   age = 20
   if age = 20:
       print("Correct")
   ```

6. Predict the three Boolean outputs:
   
   ```python
   age = 22
   print(age > 18)
   print(age == 22)
   print(age < 18)
   ```

7. Predict the output:
   
   ```python
   age = 22
   has_id = True
   print(age >= 18 and has_id)
   print(age >= 18 or has_id)
   print(not has_id)
   ```

8. From these assignments, identify every valid Python variable name:
   
   ```python
   user_name = "Arun"
   user-name = "Arun"
   2user = "Arun"
   user2 = "Arun"
   _User = "Arun"
   user name = "Arun"
   ```

9. Write a small calculator that accepts two integers and prints addition, subtraction, multiplication, division, and remainder.

10. Write a program that accepts a name and age and prints whether the person is an adult. Treat age 18 as adult.

### Revision Status

**Attempted:** Questions 1–8, 9, and 10 were previously recorded as attempted; the latest live session specifically reviewed Questions 7 and 8.

**Latest answers — 2026-10-09:**
- **Question 7:** All three logical-operator outputs correct: `True`, `True`, `False`.
- **Question 8:** Partially correct. Correctly identified `name` and `user_name` as valid, and correctly recognized that `2score` cannot start with a digit. Needs correction on `_age` (valid; leading underscores are allowed), and `class` (invalid because it is a reserved keyword). Also needs to identify hyphens as invalid in variable names.

**Still to complete:** Correct the variable-naming rules, then do a short mixed challenge and confidence check.

**Result:** Level 02 — In Progress. Revision paused at the user's request; resume later.
