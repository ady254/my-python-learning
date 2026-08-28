"""
Topic: Python Encapsulation
Date: 2026-02-03
Concept Covered:
- What is Encapsulation?
- 
"""

# Think of encapsulation like a pill bottle - you can access the medicine through the cap, but you can't directly touch the pills inside. The bottle "encapsulates" (contains) the medicine safely!
# What is Encapsulation?
# Encapsulation is the practice of bundling data and methods together, while controlling how data can be accessed or modified.
# Real-World Examples:
# ATM Machine - You can withdraw money (method), but can't directly access the cash inside
# Coffee Machine - You press buttons (methods), but can't directly touch the internal parts
# Your Phone - You use the screen (methods), but can't directly access the internal chips

# Example:
class BankAccount:
    def __init__(self, balance):
        self.balance = balance     # public attribute:  self.balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(2000)
#account.deposit(1000)
#print(account.balance)
#account.deposit(-2000)
#print(account.balance)
# output : 3000
# anyone with that object can access it 

# Protected _name
class Student:
    def __init__(self, name):
        self._name = name

# the single underscore: is a convention it means:
# this is a intended for internal/proctected use. please don't access it directly unless you know what you're doing
# python actually allow it but python does not enforce _name as private

# why we need that _name single underscore name
# desigining for safe inheritance
# When you want a subclass to inherit and modify the behavior of a parent class
# Subclass need parent access, if we make parent attributes as private using double underscore then,python applies a mechanism called "name mangling" i.e. is parent attribute becomes __className__name
#  to prevent this we use _name single underscores to protect those attribute and all access from child classes


# Interview point of view:
#Don't say:
#"Python has completely private variables."
# instead
# Python doesn't enforce strict private variables in the same way as some languages. 
# A double underscore triggers name mangling, which makes accidental access and name conflicts less likely.

# WHY WOULD WE HIDE DATA ?
# simple example would be
class BankAccount:
    def __init__(self):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

#amount = BankAccount(500)
#amount.deposit(-500)  # anyone can access data and manipulate 

#output:0

# So the better approch is:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

# now externally no can access directly
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount

account = BankAccount(2000)
account.deposit(500)   # this accept
#account.deposit(-500)   # not allowed 
#print(account.balance)     # this gave us: AttributeError: 'BankAccount' object has no attribute 'balance'
# python behind the scene is _BankAccount__balance to restrict direct external access point of encapsulation
# to access it we need to use GETTER AND SETTER METHOD to safely retrun the balance.

# GETTER MEHTOD
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(2000)
#print(account.get_balance())    # remember ()
# output: 2000
# with help of GETTER METHOD WE RETURN BALANCE SAFELY

# Setter Method:
# with help of SETTER METHOD WE CAN MODIFY THE PRIVATE DATA
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_deposit(self, amount):    # using setter method we deposit the amount into private attribute
        if amount > 0:
            self.__balance += amount

account = BankAccount(2000)
account.set_deposit(500)
#print(account.get_balance())    # remember() this

# output: 2500

# but we write above code much cleaner way like this

#instead of we write  account.set_deposit() and account.get_balance
# Python provide us @ decorator to write the above code much cleaner way
# using @property

class Student:
    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age
student = Student(20)
print(student.age)                 # here we only use .age not round bracket



    