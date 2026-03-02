"""
Topic: Python Inheritance
Date: 2026-03-02
Concpet Covered:
- Inheritance
"""

# What is python inheritance?
#  Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Example: Create  Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Adnan", "Ahmad")
x.printname()
 # Output: Adnan Ahmad
 

