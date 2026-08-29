# A final example combining almost everything example 

from abc import ABC, abstractmethod

class Payment(ABC):       # class

    company = "My Bank"                # class attribute

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder      # instance attribute 
        self.__balance = balance                   # encapsulation

    @property                     # property
    def balance(self):
        return self.__balance

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    @abstractmethod               # abstraction

    def pay(self, amount):
        pass


class UPI(Payment):                  # inheritance class UPI(Payment)

    def pay(self, amount):                  #pay() polymorphism
        if amount <= self.balance:
            print("Paid", amount, "using UPI")

        else:
            print("Insufficient balance")

class CreditCard(Payment):

    def pay(self, amount):
        if amount <= self.balance:
            print("Paid", amount, "using Credit Card")

        else:
            print("Insufficient balance")

upi = UPI("Adnan", 10000)
card = CreditCard("Ahmad", 20000)

upi.pay(2000)
card.pay(5000)
