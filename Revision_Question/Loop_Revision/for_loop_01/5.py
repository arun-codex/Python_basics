# Print the multiplication table of a given number.


n = int(input("Enter number to get multiplication table: "))

for i in range(1, 11):
    print(f"{n} X {i} : {n*i}")

    