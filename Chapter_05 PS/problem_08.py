# If languages of two friends are same; what will happen to the program in problem 6?


friends = {}

name = input("Enter your name : ")
language = input("Enter your favourate language : ")
friends[name] = language

name = input("Enter your name : ")
language = input("Enter your favourate language : ")
friends[name] = language

name = input("Enter your name : ")
language = input("Enter your favourate language : ")
friends[name] = language

name = input("Enter your name : ")
language = input("Enter your favourate language : ")
friends[name] = language

print(friends) 


# if two or more friends enter same language then the later one will not overwrite the previous one because key is name not language 