# Write a program to find the sum of first n natural numbers using while loop
n = int(input("Enter n number: "))

i = 1
total = 0

while i <= n:
    total += i
    i +=1
print(f"The sum of {n} natural numbers is : {total}")



