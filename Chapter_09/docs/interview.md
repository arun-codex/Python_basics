# 🎤 Interview & Exam Prep: File I/O

← [Back to Chapter Dashboard](../README.md)

## Theory Questions

**Q1. What is the purpose of the `with` statement in Python File I/O?**
- **A:** The `with` statement ensures that the file is automatically closed after the block of code inside it is executed, even if an exception occurs. It provides cleaner code and better resource management.

**Q2. Explain the difference between "w" and "a" modes.**
- **A:** Both modes are for writing to a file. However, `"w"` (write) will truncate (erase) the file before writing, whereas `"a"` (append) will add new data to the end of the existing file without erasing it.

**Q3. What happens if you try to open a non-existent file in "r" mode? What about "w" mode?**
- **A:** Opening a non-existent file in `"r"` mode will raise a `FileNotFoundError`. Opening a non-existent file in `"w"` mode will create the file automatically.

## Coding Questions

**Q4. Write a function that takes a filename as an argument and returns the number of lines in that file.**
```python
def count_lines(filename):
    try:
        with open(filename, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0
```

## Output Questions

**Q5. What is the output?**
```python
with open("test.txt", "w") as f:
    f.write("A")
with open("test.txt", "w") as f:
    f.write("B")
with open("test.txt", "r") as f:
    print(f.read())
```
- **Answer:** `B`. The second `open` call with `"w"` mode overwrites the file containing `"A"`.

## HR/Behavioral Questions (Technical)
- **Q:** Describe a time you had to process a large amount of data from files. How did you handle memory constraints?
  - **A:** *(Example)* Instead of using `f.readlines()` which loads the entire file into memory at once, I iterated over the file line-by-line using `for line in f:` which is memory efficient.
