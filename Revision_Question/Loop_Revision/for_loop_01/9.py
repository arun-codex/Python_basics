# Count how many even numbers are present between 1 and 100.
even = []

for i in range(1,101):
    if i % 2 == 0 :
        even.append(i)

print(len(even))