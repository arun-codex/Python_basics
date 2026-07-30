'''
3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
‘object.a = 0ʼ. Does this change the class attribute?

'''

class Demo:
    a = 4

o = Demo()
print(o.a) # Print the class attribut because instance attribute is not present 
o.a = 0 # instance attribute is set 
print(o.a)  # Print the instance attribut because instance attribute is present 
print(Demo.a)  # Print the class attribute 


