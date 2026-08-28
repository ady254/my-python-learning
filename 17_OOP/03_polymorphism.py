"""
Topic: Python Polymorphism
Date: 2026-03-02
Concept Covered:
- What is polymorphism?
"""
# Think of polymorphism like a TV remote - the "power" button does different things for different devices (TV, soundbar, DVD player), but you press it the same way!
# What is Polymorphism?
# Poly = many
# Morphism = forms
# So polymorphism means "many forms" - the same thing behaving differently in different situations!

# Method 1: Polymorphism with same interface/method call
# - Different classes, same method names:

# for example:
class CreditCard:
    def pay(self, amount):
        print("Paid", amount ,"using Credit card")
class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class PayPal:
    def pay(self, amount):
        print("Paid", amount, "using paypal")

payments_process = [
    CreditCard(),
    UPI(),
    PayPal()

]
for payment_process in payments_process:
    payment_process.pay(1000)

class Duck:
    def speak(self):
        print("quck")

class Dog:
    def speak(self):
        print("bark")

class Cat:
    def speak(self):
        print("meow")
animals =[
    Duck(),
    Dog(),
    Cat()
]
for animal in animals:
    animal.speak()

# above all are same method  so python cares: "Does this object have a speak() method that I can call?" Yes , thats a ducking typing
# for example we have totally different class
class Duck:
    def speak(self):
        print("quck")

class Human:
    def speak(self):
        print("hello")
class Robot:
    def speak(self):
        print("beep")

things = [
    Duck(),
    Human(),
    Robot()
]

for thing in things:
    thing.speak()
# in this exmaple python only cares "Does this object have a speak() method that I can call?" which discuss above

# Polymorphism through inheritance
class Payment:
    def pay(self, amount):
        print("processing payment")

class CreditCard(Payment):

    def pay(self, amount):
       
        print("Paid using credit card")

class UPI(Payment):

    def pay(self, amount):
        print("Paid using UPI")

payments = [
    CreditCard(),
    UPI()
]
for payment in payments:
    payment.pay(1000)

# output: 
#Paid using credit card
#Paid using UPI

# each child overrides pay()
# this is Runtime polymorphism through method overridding