"""
Topic: Python Classes and Object
Date: 2026-03-1
Concept Covered:
- Classes
- Object
"""

# What is python classes/objects?
# Python is an object oriented programming language.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# Example: Create a Class
from _frozen_importlib_external import NamespaceLoader
class MyClass:
    x = 5

print(MyClass)

# Output: <class '__main__.MyClass'>

# Create Object:
class MyClass()
     x = 5

p1 = MyClass()
print(p1.x)

# Output: 

# Delete Object : del keyword to delete objects

# Example:
Class Person:
  def ___init__(self, name, age):
    self.name = name
    self.age = age
     
    def myfunc(self):
      print("Hello my name is " + self.name)

p1 = person("John", 36)

del p1

print(p1)

# Output:
# NameError: 'p1' is not defined

# Multiple Objects: You can create multiple object from the same class

# Example:

class MyClass():
    x = 5

p1 = MyClass()
p2 = My Class()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Output:
# 5
# 5
# 5

# Note: Each object is independent and has its own copy of the class properties




