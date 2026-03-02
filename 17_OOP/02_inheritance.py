"""
Topic: Python Inheritance
Date: 2026-03-02
Concpet Covered:
- Inheritance
"""
# Imagine inheritance like passing down traits from parents to children. Just like you might inherit your parent's eye color or height, a class can inherit properties from another class!
# What is python inheritance?
#  Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Example: Create  Parent class
class Person:  # This is our PARENT class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Adnan", "Ahmad")
x.printname()
 # Output: Adnan Ahmad
 

# Create a child class: To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# Example: 
class Student(Person):  # This is our CHILD class - notice Person in parentheses
  pass  # "pass" means we're not adding anything new yet

# Student now has everything Person has !
student1 = Student("Adnan", "Ahmad")
student1.printname() 

# Output: Adnan Ahmad

# Using super() the easy way!

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)  # super() automatically calls the parent class

    # Add our own property
    self.student_id = "12345"

  def show_student(self):
    print(f"student: {self.firstname} {self.lastname}, ID: {self.student_id}")



