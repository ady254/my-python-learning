# Instance Attributes vs Class Attributes

# Instance attributes --> Object's data
# Class attributes --> Class's data
# Methods : Intance methods --> Object's behavior
         #   Class methods --> Class's behavior
        #   Static methods --> Class's behavior

# Example of instance attributes

class Student:
    college = "Jamia Hamdard"     # Class attribute

    def __init__(self, name, age,):
        self.name = name
        self.age = age 
        


    def study(self):      # Instance method: we can modify the object data using instance method
        print(self.name, "is studying in", self.college)

student1 = Student("Adnan", 20)
student2 = Student("Ahmad", 22, )
student2.college = "DU"  # changes college on student2 only not on student1 
                        
student1.study()
student2.study()
# Output here is:
# Adnan is studing in Jamia Hamdard
# Ahmad is studing in DU




#here self.name and self.age are instance attributes of each individual object. These are called instance attributes.

#Example of Instance methods can modify the object's data:

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):   # instance method
        self.balance += amount
account = BankAccount(2000)
account.deposit(500)

