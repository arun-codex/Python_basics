# Find the factorial of a given number.

n = int(input("Enter number to get sum: "))
total = 1

for i in range(1,n+1):
    total = total * i
print(f"Sum of {n} is: {total}")


