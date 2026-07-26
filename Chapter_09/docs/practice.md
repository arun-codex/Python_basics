# 🏋️ Practice Problems: File I/O

← [Back to Chapter Dashboard](../README.md)

## Warm-up

**1. Create a File**
- **Difficulty:** ⭐☆☆☆☆
- **Concept Tested:** Write Mode
- **Expected Time:** 2 mins
- **Task:** Create a script that writes the text "Python is awesome" to a file named `awesome.txt`.
- **Hint:** Use the `with open(...) as f:` syntax and `"w"` mode.
- **Common Mistake:** Forgetting the quotes around the filename or mode.

## Easy

**2. Read and Print**
- **Difficulty:** ⭐⭐☆☆☆
- **Concept Tested:** Read Mode
- **Expected Time:** 3 mins
- **Task:** Write a script to read `awesome.txt` and print its contents to the console.
- **Hint:** Use `f.read()`.
- **Common Mistake:** Trying to read from a file opened in `"w"` mode.

## Medium

**3. Append Data**
- **Difficulty:** ⭐⭐⭐☆☆
- **Concept Tested:** Append Mode
- **Expected Time:** 5 mins
- **Task:** Append the text "I am learning File I/O" to `awesome.txt` on a new line.
- **Hint:** Use `"a"` mode. Remember to add `\n` at the beginning of your string.
- **Common Mistake:** Using `"w"` mode, which will erase the previous text.

## Output Prediction

**4. What will this print?**
- **Difficulty:** ⭐⭐☆☆☆
- **Concept Tested:** File Position
- **Expected Time:** 3 mins
- **Task:** Predict the output of the following code (assuming `log.txt` contains "Line 1\nLine 2\nLine 3").
```python
with open("log.txt", "r") as f:
    line1 = f.readline()
    print(line1.strip())
    line2 = f.readline()
    print(line2.strip())
```
- **Answer:**
```
Line 1
Line 2
```
- **Common Mistake:** Forgetting that `readline()` moves the cursor forward each time it's called.

## Find Error

**5. Debug the Code**
- **Difficulty:** ⭐⭐☆☆☆
- **Concept Tested:** File Modes
- **Expected Time:** 3 mins
- **Task:** Find the error in this code snippet.
```python
with open("data.txt", "w") as f:
    content = f.read()
    print(content)
```
- **Answer:** The file is opened in `"w"` (write) mode, but the code attempts to `read()` from it. It should be opened in `"r"` mode, or `"w+"` mode if both are needed.

## Challenge

**6. Log File Parser**
- **Difficulty:** ⭐⭐⭐⭐☆
- **Concept Tested:** Readlines and String Manipulation
- **Expected Time:** 15 mins
- **Task:** Write a script that reads a log file (`server.log`). Find how many times the word "ERROR" appears in the file.
- **Hint:** You can use `f.read().split()` or iterate line by line and use the `in` keyword.
- **Common Mistake:** Case sensitivity. Convert the line to uppercase before checking, or just search for the exact case.
