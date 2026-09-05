# Abstraction abc  ---> hiding the unnecessary info from the user
# example IN ATM user don't sees

#→ connect to bank server
#→ connect to bank server
#→ authenticate account
#→ check balance
#→ check transaction limits
#→ update database
#→ generate transaction record
#→ return money

# they just withdraw(5000) thats it 

# therefore, Abstraction means exposing the important interface while hiding unnecessary implementation details.

# then, what was ENCAPSULATION --> MEANS --> Encapsulation is about controlling access; (self.__balance) abstraction is about exposing only what the user needs to know.

# real life car example when u drive a CAR You
 #↓
#steering wheel
#accelerator
#brake
#gear
# ↓
#Car
# but, You don't need to understand:

#fuel injection
#combustion
#pistons
#crankshaft
#transmission internals
#ECU

#You interact with a simple interface:

#start()
#accelerate()
#brake()

#The complex implementation stays hidden.

#That's abstraction.

# How Do We Implement abstraction in Python?
# for that, Python provides the "abc" module called "Abstact Base Class"

# for example: from abc import ABC, abstractmethod
# then: class Animal(ABC):
          #   @abstractmethod
          #   def speak(self):
          #       pass
# we created an abstract class
# What does the @abstractmethod mean? means--> "Any concrete child class must provide an implementation of this method"
# why we need that?  suppose we're building a payment system--> you know every payment method must have pay(), but you don't know how the payment method implements it
# for example: Credit Card -> card network , UPI -> upi system , PayPal -> paypal api , --> Bank Transfer -> banking network

# so we can define:
from abc import ABC, abstractmethod     

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass
# we basically saying --> Every payment type must provide pay() method
# then create a concrete classes

class CreditCard(Payment):
    def pay(self, amount):                  # implemented the abstract method into child class
        print("Paid", amount, "using credit card")

class UPI(Payment):
    def pay(self, amount):              # implemented the abstract method into child class
        print("Paid", amount, "using UPI")

credit_card = CreditCard()
upi = UPI()
# both work here because we use pay() implemented
# but here's the interesting part
#payment = Payment()
#python won't allow it 
#TypeError: Can't instantiate abstract class Payment -> because Payment contains an abstract method and doesn't provide the actual implementation
#the child must implement the abstract method

# but 
class CreditCard(Payment):
    pass             
# this will not work because--> child doesn't implement the Payment class method i.e. is pay()
# The parent defines:

# WHAT must exist

#The child defines:
#HOW it works

#That's a very important way to explain abstraction.

# Example for of notifications

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print("Sending email:", message)
class SMS(Notification):
    def send(self, message):
        print("Sending SMS:", message)

class PushNotification(Notification):
    def send(self, message):
        print("Sending Push notification:", message)

notifications = [
    Email(),
    SMS(),
    PushNotification()

]

for notification in notifications:
    notification.send("Hello, Adnan this side")


# the above example is the combination of abstraction + polymorphism
# the above example also states that the application doesn't need to know --> is this email? , is this sms? is this push?
# it only cares the Notification must have send(), then polymorphism handles the different implementations
# Abstraction --> defines common contract --> Polymorphism --> different implementations --> these concepts work together



# Interview bite:

# Can an abstract class have normal methods?
# ans: Yes!
# example:

from abc import ABC, abstractmethod

class Payment(ABC):
    def validate_amount(self, amount):
        if amount <= 0:
            return False
        return True

# here validate_amount() has an implementation

# Abstract classes can also have __init__ --> yes!
#example

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):

        self.name = name

    @abstractmethod
    def speak(self):
        pass

#child

class Dog(Animal):

    def speak(self):
        print(self.name, "braks")

dog = Dog("Bruno")
dog.speak()

# the flow is:
# Dog.__init__ inherited --> Animal.__init__() --> self.name = "Bruno" then dog.speak()
# output: Bruno braks



# One real software example

from abc import ABC, abstractmethod

class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

class ProviderA(LLMProvider):
    def generate(self, prompt):
        pass

class ProviderB(LLMProvider):
    def generate(self, prompt):
        pass


def ask_model(model, prompt):
    return provider.generate(prompt)


# Abstraction + polymorhism
