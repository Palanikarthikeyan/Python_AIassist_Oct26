class Person:
    def display(self):
        print("I am Person")

class Emp1(Person):
    def display(self):
        print("I am Emp1 - display")
        super().display()

class Emp2(Person):
    def display(self):
        print("I am Emp2 - display")
        super().display()

class Engineer(Emp1,Emp2):
    def __init__(self):
        print("This is Engineer class")
        
obj = Engineer()
obj.display()
print("\n\n")
print(Engineer.__mro__)