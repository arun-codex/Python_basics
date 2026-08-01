# 1. Return the smaller of two numbers.

def smaller_of_two(a,b):
    if a == b:
        return f"{a} and {b} both are equal."
    elif a < b:
        return f"{a} is smaller than {b}"
    else:
        return f"{b} is smaller than {a}"

a = 5
b = 6
smaller = smaller_of_two(a,b)
print(smaller)