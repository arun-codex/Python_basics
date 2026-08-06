def divisible5(n):
    if n % 5 == 0:
        return True
    return False


a = [1, 2,345, 33, 56565, 10, 125, 873,8739]

f = list(filter(divisible5,a))
print(f)

