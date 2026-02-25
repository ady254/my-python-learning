"""
Topic: Args and Kwargs
Date: 2026-02-25
Concept Covered: 
- Args and Kwargs
"""

# Arbitrary Arguments- *args
# - If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# Example:
def my_function(*Bikes):
    print("I have a " + Bikes[2])

my_function("Avenger", "BMW", "Yamaha RD350")

# Output: I have a Yamaha RD350

# What is *args?
# -  *args parameter allows a function to accept any number of positional arguments.
# -  Inside the function, args becomes a tuple containing all the passed arguments:

# Example:
def my_function(*args):
    print("Type", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

# Output:
# Type <class 'tuple'>
# First argument: Emil
# Second argument: Tobias
# All arguments: ('Emil', 'Tobias', 'Linus')

# Using *args with Regular Arguments
# You can combine regular parameters with *args.
# Regular parameters must come before *args:

# Example:
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Adnan", "Ahmad", "Python", "FAST API")

# Output:
# Hello Adnan
# Hello Ahmad
# Hello Python
# Hello FAST API

# Practical Example: A function that calculates the sum of any numbers of values:

def my_funciton(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3, 4))
print(my_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(my_function(5))

# Output:
# 10
# 55
# 5

# Arbitrary Keyword Arguments- **kwargs
# - If you do not know how many keyword arguments that will be passed into your function, add a ** before the parameter name in the function definition.

# Example: Using **kwargs to accept any number of keyword arguments:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Adnan", lname = "Ahmad")

# Output:
# His last name is Ahmad

# What is **kwargs?
# - **kwargs allows a function to accept any number of keyword arguments.
# - Inside the function, kwargs becomes a dictionary containing all the passed keyword arguments:

# Example:
def my_function(**kwargs):
    print("Type", type(kwargs))
    print("First argument:", kwargs["fname"])
    print("Second argument:", kwargs["lname"])
    print("All arguments:", kwargs)

my_function(fname = "Adnan", lname = "Ahmad")

# Output:
# Type <class 'dict'>
# First argument: Adnan
# Second argument: Ahmad
# All arguments: {'fname': 'Adnan', 'lname': 'Ahmad'}


# Combining *args and **kwargs
#You can use both *args and **kwargs in the same function.

#The order must be:

#regular parameters
#*args
#**kwargs

# Example:
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Output:
# Title: User Info
# Positional arguments: ('Emil', 'Tobias')
# Keyword arguments: {'age': 25, 'city': 'Oslo'}

# Unpacking Arguments
# - You can unpack a list or tuple into positional arguments using *.
# - You can unpack a dictionary into keyword arguments using **.

# Example:
def my_function(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_function(*my_list)

# Output:
# 1 2 3

