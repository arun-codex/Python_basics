# Find the sum of numbers from 1 to n.

n = int(input("Enter number to get sum: "))
total = 0

for i in range(1,n+1):
    total = total + i
print(f"Sum of {n} is: {total}")


