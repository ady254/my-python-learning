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

