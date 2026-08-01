# 5. Create a function that prints a multiplication table of 5.
n = 5
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

table(n)