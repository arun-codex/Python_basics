'''
4. Add a static method in problem 2, to greet the user with hello

'''

'''
2. Write a class
“Calculator” capable of finding square, cube and square root of a number

'''

class Calculator:
    def __init__ (self, n):
        self.n = n

    def squre(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squreroot(self):
        print(f"The squareroot is {self.n**1/2}")   

    @staticmethod
    def hello():
        print("Hello there!") 

a = Calculator(4)
a.hello()
a.squre()
a.cube()
a.squreroot()

