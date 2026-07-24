
# 9. Reverse a given number.
# Example:
# Input: 12345
# Output: 54321

n = 12345
rev = 0

while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)


