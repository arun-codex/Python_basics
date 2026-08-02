# 4. Return the sum of digits of a number.

def digits_of_num(n):
    sum = 0
    while(n > 0):
        sum  = sum + n % 10
        n = n // 10
    return sum

n = 541
total = digits_of_num(n)
print(total)
