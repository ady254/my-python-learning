"""
Topic: Python Encapsulation
Date: 2026-02-03
Concept Covered:
- What is Encapsulation?
- 
"""

# Think of encapsulation like a pill bottle - you can access the medicine through the cap, but you can't directly touch the pills inside. The bottle "encapsulates" (contains) the medicine safely!
# What is Encapsulation?
# Encapsulation = Bundling data (variables) and methods (functions) together inside a class, and controlling access to them.

# Real-World Examples:
# ATM Machine - You can withdraw money (method), but can't directly access the cash inside
# Coffee Machine - You press buttons (methods), but can't directly touch the internal parts
# Your Phone - You use the screen (methods), but can't directly access the internal chips

# Example:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # Public - anyone can see
        self.__balance = balance # Private - hidden (note the __)
    
    def show_balance(self):      # Public method to access private data
        print(f"Balance: ${self.__balance}")
    
    def deposit(self, amount):   # Controlled way to modify private data
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount!")

# Using the class
account = BankAccount("John", 1000)

# This works (public)
print(account.owner)  # John

# This works (public method)
account.show_balance()  # Balance: $1000
account.deposit(500)    # Deposited $500
account.show_balance()  # Balance: $1500

# This DOESN'T work (private - can't access directly)
# print(account.__balance)  # ERROR!
# account.__balance = 9999   # WON'T work!


# Access Levels in Python:
# 1. Public (Default) - Anyone can access

class Person:
    def __init__(self, name):
        self.name = name  # Public - can be accessed anywhere

person = Person("John")
print(person.name)  #  Works fine
person.name = "Mike"  # Can modify

# class Person:
    def __init__(self, name):
        self.name = name  # Public - can be accessed anywhere

person = Person("John")
print(person.name)  #  Works fine
person.name = "Mike"  #  Can modify

# 2. Protected (_single underscore) - "Please don't touch"

class Person:
    def __init__(self, name, age):
        self.name = name    # Public
        self._age = age      # Protected (convention: don't touch directly)

person = Person("John", 30)
print(person.name)   #  Fine
print(person._age)   #  Works but you're not supposed to!

# 3. Private (__double underscore) - Hidden from outside

class Person:
    def __init__(self, name, ssn):
        self.name = name        # Public
        self.__ssn = ssn         # Private - name mangling
    
    def get_ssn(self):          # Public method to access private data
        return f"***-**-{self.__ssn[-4:]}"

person = Person("John", "123-45-6789")
# print(person.__ssn)  # ERROR! Can't access directly
print(person.get_ssn())   # ***