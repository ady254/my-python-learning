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
# why inheritance useful?
# 1. Code Reusability: Don't repeat the same code. Reuse the code from the parent class.
# 2. Saves Time: Don't write the same code again and again.
# 3. Saves Space: Don't store the same data again and again.

# Example:
class Vehicals:          # here Vehicals is called Parent class or Base class or Superclass
  def start(self):
    print("vehicals-start")

  def stop(self):
    print("vehicals-stop")

class Car(Vehicals):   # here Car is called Child class or Derived class or Subclass
  pass

car = Car()
car.start()         # python looks this methods in Car class first, if not found then look in Parent class, if it find, so it executes the inherited method.
car.stop()          # python looks this methods in Car class first, if not found then look in Parent class, if it find, so it executes the inherited method.

# the key mental model is:
# when u write car.start()
# python searches the :
#  1. Does Car class have start()/stop() method?
#        ↓
#       No
#        ↓
#  2. Does Vehicle class have start()/stop() method?
#        ↓
#       Yes
#        ↓
# Execute it
# this is called method lookup


# But if car have its own functioinality like car have ac but bike dont 
# for example:
class Vehicale:
  def start(self):
    print("We use the start button to start the vehicals")

  def stop(self):
    print("We use brake to stop the vehicals")

# car have its own feature like ac but bike dont have ac
# for that i create separate method in car class
class Car(Vehicals):
  def ac(self):
    print("Car have AC")

class Bike(Vehicale):
  pass



my_car = Car()
my_bike = Bike()

my_car.start()
my_car.stop()
my_car.ac()

my_bike.start()
my_bike.stop()

# What if parent class and child class have exact same name method?
# ans: Child class method overrides the parent class method.
# This is called method overriding
# When you call the method on an instance of the child class, Python executes the child's version of the method instead of the parent's.
# super() is used to call the parent class method or parent class attributes from the child class.

# lets understand inheritance with attributes
class Vehicale:
  def __init__(self, brand, speed):
    self.brand = brand
    self.speed = speed

class Car(Vehicale):
  def __init__(self, brand, model, speed):
    super().__init__(brand, speed)      # super() with out it u would write self.brand = brand, self.speed = speed (it will also work but it is verbose)
    self.model = model

my_car = Car("Audi", "A4", 240)
print(my_car.brand)
print(my_car.model)
print(my_car.speed)

# Note: Car is a Vehicale is called IS-A relationship. Inheritance is appropriate when this relationship makes senes
# Car IS-A Vehicle
# Bike IS-A Vehicle
# Dog IS-A Animal
# Manager IS-A Employee
# Note : Don't use inheritance just because two classes have some common code.
# A car has an engine but engine is not a car so this is not inheritance
# This IS-A relationship is called inheritance.
# This HAS-A relationship is called composition.


