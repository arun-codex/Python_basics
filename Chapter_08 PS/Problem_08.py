# Write a python function to print multiplication table of a given number.

n = 5

def multi(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        i +=1
multi(6)
