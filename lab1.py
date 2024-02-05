Python Syntax
ex1
print("Hello World")

ex2
if 5 > 2:
   print('YES')

Python comments
ex1
#This is a comment
ex2
"""
This is a comment
written in
more than just one line
"""

Python variables
ex1
carname = "Volvo"

ex2
x = 50

ex3
x = 5
y = 10
print(x + y)

ex4
x = 5
y = 10
z = x + y
print(z)

ex5
x,y,z = "Orange", "Banana", "Cherry"

ex6
x = y = z = "Orange"

ex7
def myfunc():
   global x
   x = "fantastic"


Data types
ex 1
x = 5
print(type(x))
int

ex2
x = "Hello World"
print(type(x))
str

ex3
x = 20.5
print(type(x))
float

ex4
x = ["apple", "banana", "cherry"]
print(type(x))
list

ex5
x = ("apple", "banana", "cherry")
print(type(x))
tuple

ex6
x = {"name" : "John", "age" : 36}
print(type(x))
dict

ex7
x = True
print(type(x))
bool



Python Numbers
ex1
x = 5
x = float(x)

ex2
x = 5.5
x = int(x)

ex3
x = 5
x = complex(x)

String
ex1
x = "Hello World"
print(len(x))

ex2
txt = "Hello World"
x = txt[0]

ex3
txt = "Hello World"
x = txt[2:5]

ex4
txt = " Hello World "
x = txt.strip()

ex5
txt = "Hello World"
txt = txt.upper()

ex6
txt = "Hello World"
txt = txt.lower()

ex7
txt = "Hello World"
txt = txt.replace('H', 'J')

ex8
age = 36
txt = f"My name is John, and I am
{age}"
print(txt.format(age))


Booleans
ex1
print(10 > 9)
False

ex2
print(10 == 9)
False

ex3
print(10 < 9)
True

ex4
print(bool("abc"))
True

ex5
print(bool(0))
False


Python operators
ex1
print(10*5)

ex2
print(10 /2)

ex3
fruits = ["apple", "banana"]
if "apple"  in fruits:
    print("Yes, apple is a fruit!")

ex4
if 5 != 10:
   print("5 and 10 is not equal")

ex5
if 5 == 10 or 4 == 4:
   print("At least one of the statements is true")

Python if...else
ex1
a = 50
b = 10
if a > b:
    print("Hello World")

ex2
a = 50
b = 10
if a != b:
    print("Hello World")

ex3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

ex4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

ex5
if a == b and c == d:
    print("Hello")

ex6
if a == b or c == d:
    print("Hello")

ex7
if 5 > 2:
    print('YES')

ex8
a = 2
b = 5
print("YES")  if a== b else print("NO")

ex9
a = 2
b = 50
c = 2
if a == c or b==c:
    print("YES")
