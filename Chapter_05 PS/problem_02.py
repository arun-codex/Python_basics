# Write a program to input eight numbers from the user and display all the unique numbers (once) 
s = set()

s.add(int(input("Enter number 1: ")))
s.add(int(input("Enter number 2: ")))
s.add(int(input("Enter number 3: ")))
s.add(int(input("Enter number 4: ")))
s.add(int(input("Enter number 5: ")))
s.add(int(input("Enter number 6: ")))
s.add(int(input("Enter number 7: ")))
s.add(int(input("Enter number 8: ")))

print(s)

# Output should not be in order and duplicate numbers are not allowed
