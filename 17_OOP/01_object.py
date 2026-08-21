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
class MyClass:
     x = 5

p1 = MyClass()
print(p1.x)

# Output: 

# Delete Object : del keyword to delete objects

# Example:
class Person:
  def ___init__(self, name, age):
    self.name = name
    self.age = age
     
    def myfunc(self):
      print("Hello my name is " + self.name)

p1 = p1erson("John", 36)

del p1

print(p1)

# Output:
# NameError: 'p1' is not defined

# Multiple Objects: You can create multiple object from the same class

# Example:

class MyClass():
    x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Output:
# 5
# 5
# 5

# Note: Each object is independent and has its own copy of the class properties




class Laptop:
   def __init__(self, brand, ram):
      self.brand = brand
      self.ram = ram

lap1 = Laptop("Dell", "16GB",)
lap2 = Laptop("HP", "8GB")

print(lap1.brand, lap1.ram)
print(lap2.brand, lap2.ram)

class Student:
   def __init__(self, name, age, branch, college):
      self.name = name
      self.age = age
      self.branch = branch

      def study(self):
           print(self.name, "is studying")
      

Student1 = Student("ADNAN", 20, "CSE", "Jamia Hamdard")
Student1.study()


Student2 = Student("AKI", 21, "ECE", "Jamia Hamdard")
Student2.study()
