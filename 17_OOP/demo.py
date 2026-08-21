#A class defines what an object should have and what it can do; an object is an actual instance created from that class, containing its own state and using the class's behavior.


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):   # instance method
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# Can we modify the object's data?
# Ans: Yes, we can modify the object's data by calling the deposit(with the help of method) method and passing the amount to be deposited.
account = BankAccount(2000)
account.deposit(500)
account.withdraw(200)

#print(account.balance)

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, value):
        self.speed += value

    def display(self):
        print(self.brand, self.speed)

car1 = Car("BMW", 120)
car2 = Car("Audi", 150)

car1.accelerate(30)


#car1.display()
#car2.display()

class Device:
    def __init__(self, name):
        print("Init called for", name)
        self.name = name.upper()

    def show(self):
        print("Device:", self.name)

d1 = Device("laptop")
d2 = Device("mobile")

d1.show()
d2.show()
