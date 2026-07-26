cities = ["delhi", "gurgaon", "noida", "pune"]
heros = ["thor", "ironman", "captain amerika", "saktima"]


print(heros[0], end="")
print(heros[1])

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print_list(heros)

