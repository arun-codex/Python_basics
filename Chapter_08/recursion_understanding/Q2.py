# Write a recursive function to calculate the sum of first n natural numbers.
n = int(input("Enter a Number: "))


def sum_n(n):
    if n == 1:
        return 1
    return sum_n(n - 1) + n


print(sum_n(n))
