# 5. Return the reverse of a number.

def reverse_of_num(n):
    result = 0
    while n > 0:
        last_digit = n % 10
        result = result * 10 + last_digit
        n //= 10
    return result

n = 12345
total = reverse_of_num(n)
print(total)
