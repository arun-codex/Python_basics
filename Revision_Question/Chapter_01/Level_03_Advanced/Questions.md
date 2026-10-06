# Chapter 01 — Level 03: Advanced

## Reasoning, Debugging & Code Analysis

1. Find and fix the conceptual mistake:

    import math
    math.sqrt = 25
    print(math.sqrt(25))

2. Explain why import requests does not install the requests package.
3. A program runs import random followed by random.randint(1, 10). Explain what can and cannot be predicted about the output.
4. Compare import math with from math import sqrt. What changed?
5. Why is pip install requests a package-management operation rather than Python syntax?
6. A beginner says: “Every function needs to be imported.” Explain why this is incorrect.
7. Debug:

    import math
    result = math.sqrt(100)
    # print(result)

Why does the program produce no visible output?
8. Explain the difference between a module, a function inside a module, and a package.
9. What happens conceptually if Python cannot find requests when import requests is executed?
10. Explain why comments are useful for humans but normally irrelevant to Python's runtime execution.