# 10. Create a function that prints whether a number is even or odd.

def even_odd(n):
    if n < 0:
        print(f"{n} is negative number.")
    elif n % 2 == 0 :
        print(f"{n} is even number.")
    else:
        print(f"{n} is odd number.")

n = -1

even_odd(n)
        