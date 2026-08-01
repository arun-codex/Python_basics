# 2. Return the largest of three numbers.

def largest_of_three(a,b,c):
    if a == b == c:
        return "All numbers are equal."
    elif a > b and a > c:
        return f"{a} is largest."
    elif b > a and b > c:
        return f"{b} is largest."
    else:
        return f"{c} is largest."

a = 5
b = 6
c = 7
largest = largest_of_three(a,b,c)
print(largest)