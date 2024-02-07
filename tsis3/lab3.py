Python Functions
ex1
def my_function():
    print("Hello from a function")

ex2
def my_function():
    print("Hello from a function")
my_function()

ex3
def my_function(fname, lname):
  print(fname)

ex4
def my_function(x):
     return x+5
ex5
def my_function(*kids):
    print("The youngest child is " + kids[2])

ex6
def my_function(**kid):
    print("His last name is " + kid["lname"])

Python Lambda
ex1
x = lambda a:a

Python Classes and Objects
ex1
Class MyClass:
    x = 5
ex2
class MyClass:
    x = 5
p1 = MyClass()

ex3
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

ex4
class Person:
def __init__(self, name, age):
    self.name = name
    self.age = age

Python Inheritance
ex1
class Student(Person)

ex2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()