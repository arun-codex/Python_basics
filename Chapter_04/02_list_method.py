friends = ["Apple", "Banana", "Cherry", 5, 345.06, False, "Aakash", "Rohan", "Sam"]

print(friends[0])


friends.append("Arun")
print(friends) 

l1 = [1, 34, 62, 2, 66, 6, 11]

# l1.sort()
# l1.reverse()
# l1.insert(3,333333)  # insert 333333 at index 3 and shift elements to the right 

value = l1.pop(3)  # remove element at index 3 and return it
print(value)
print(l1)
