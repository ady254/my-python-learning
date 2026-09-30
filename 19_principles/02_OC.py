# 2. Open/Closed Principle
# A class should be open for extension but closed for modification.

# Suppose:
def calculate_payment(method, amount):

    if method == "stripe":
        # Stripe logic
        pass

    elif method == "razorpay":
        # Razorpay logic
        pass

    elif method == "paypal":
        # PayPal logic
        pass


# works
# But imagine you add:
# And each of them has a different logic for calculating the payment.
# You would have to add each of them to the if-else statement.
# This is not a good solution because you are modifying the existing code.
# You are breaking the open/closed principle.
# You are not open for extension because you are modifying the existing code.

#Razorpay
#PayPal
#Adyen
#Checkout.com
#STC Pay

# better:
# create a common interface
from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass

class StripeProvider(PaymentProvider):

    def pay(self, amount: float):
        print("Stripe payment")


class RazorpayProvider(PaymentProvider):

    def pay(self, amount: float):
        print("Razorpay payment")

class PaymentService:

    def __init__(self, provider: PaymentProvider):
        self.provider = provider

    def process(self, amount):
        return self.provider.pay(amount)

# adding  Paypal
class PayPalProvider(PaymentProvider):

    def pay(self, amount: float):
        print("PayPal payment")

#PaymentService is not changinng here
# that's the key idea for open/close principle

