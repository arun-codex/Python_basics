
# 8. Count the number of digits in a given number.
# Example:
# Input: 12345
# Output: 5


number = 12345
count = 0
while number != 0:
    number = number // 10
    count = count + 1
print(count)
