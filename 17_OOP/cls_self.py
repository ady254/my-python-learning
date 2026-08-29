"""
Instance method
Class method
Static method
"""

# Instance method -> modify the object's attribute 

# Example:

class Student:

    def __init__(self, name):
        self.name = name


    def study(self):     # here def study(self) --> is the instance variable
        print(self.name, "is studing")

#student1 = Student("Adnan")
#student1.study()      # why? because it works with a particular object
# Instance method : works with object -> self


# Class Methods: works with class -> cls
# @classmethod = a way to change class attributes.

#That's too narrow.

# Think:

# @classmethod = a method whose first automatic argument is the class (cls) instead of an object (self).

# Because of that, it can naturally work with class-level data and can also be used for alternative constructors.
class Student:
    college = "Jamia hamdard"


    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studing", self.college)
    @classmethod
    def change_college(cls, new_college): # 
        cls.college = new_college

student1 = Student("Adnan")
student2 = Student("Ahmad")
Student.change_college("DU")   # class method changes the college on the class

student1.study()
student2.study()



# Real life Example:
# suppose a company name is XYZ technologies  and it changes to ABC technologies. number of employees is 10,000


# Approch 1. specificly change for each employee:

class Emp:
    def __init__(self, name):
        self.name = name
        self.company = "XYZ technologies"

emp1 = Emp("Adnan")
emp2 = Emp("Ahmad")
emp3 = Emp("John")


emp1.company = "ABC technologies"
emp2.company = "ABC technologies"
emp3.company = "ABC technologies"

# Approch 2. using class method

class Emp:
    company = "XYZ technologies"

    def __init__(self, name):
        self.name = name

    def print_emp(self):
        print(f"Name: {self.name}, Company: {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
emp1 = Emp("Adnan")
emp2 = Emp("Ahmad")
emp3 = Emp("Zurez")
Emp.change_company("ABC technologies")
emp1.print_emp()
emp2.print_emp()
emp3.print_emp()


# Static Method : work with the class but does not modify the object's attribute nor the class's attribute 

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

print(Calculator.add(10, 20))


#| Type            | First parameter | Works with |
#| --------------- | --------------- | ---------- |
#| Instance method | `self`          | Object     |
#| Class method    | `cls`           | Class      |
#| Static method   | None            | Neither    |

# How do you decide which one to use?
# Does this method need data from a specific object?  use self
# Does this method need to modify/access class-level data?  use cls, class 
# Does this method need neither object nor class data? use @staticmethod
 # complete Example:
class Student:

    college = "Jamia Hamdard"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        print(self.name, self.age)

    # Class method
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18




# Note:Instance assignment affects one object.
# Class assignment affects the class, and objects without their own value see the class's value.