"""
Topic: Python Function Arguments
Date: 2026-02-24
Concept Covered: 
- function arguments
- Parameters vs Arguments
- Number of Arguments
- Default Parameters
- Keyword Arguments
- Positional Arguments
- Mixing Positional and Keyword Arguments
- Parsing Different Data Types
- Return Values
- Returning Different Data Types
- Positional-Only Arguments
- Keyword-Only Arguments
- Combining Positional-Only and Keyword-Only
"""

# Function arguments:
# - arguments are the values that are passed to a function

# Example:
def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Output:
# EmilRefsnes
# TobiasRefsnes
# LinusRefsnes

# Parameters vs Arguments:
# - Parameters are the variables that are used to pass values to a function
# - Arguments are the values that are passed to a function

# Example:
def my_function(name): # name  is a parameter
    print("Hello", name)

my_function("Adnan") # Adnan is an argument

# Output:
# Hello Adnan

# Number of Arguments:
# - The number of arguments that a function can take is defined by the number of parameters it has

# Example:
def my_function(name, age):
    print(name, age)

my_function("Adnan", 19)

# Output:
# Adnan 19

# If your function expects 2 arguments, you must call it with exactly 2 arguments.
# my_function("Adnan", 19, "Male") # This will raise an error


# Default Parameters:
# - Default parameters are parameters that have a default value

# Example:
def my_function(name = "Adnan"):
    print("Hello", name)

my_function("Emil")
my_function()
my_function("Tobias")
my_function("Linus")

# Output:
# Hello Emil
# Hello Adnan
# Hello Tobias
# Hello Linus


# Example:

def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Output:
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

# Keyword Arguments:
# - You can send arguments with the key = value syntax
# - The order of the arguments does not matter
# - The phrase Keyword Arguments is often shortened to kwargs in Python documentation.


def my_function(animal, name):
    print("I have a", animal)
    print("My animal's name is", name)

my_function(animal = "dog", name = "Buddy")

# Output:
# I have a dog
# My animal's name is Buddy

# Positional Arguments:
# - Positional arguments are arguments that are passed to a function based on their position
# - Positional arguments must be in the correct order

# Example:
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

# Output:
# I have a dog
# My dog's name is Buddy

# Mixing Positional and Keyword Arguments:
# - You can mix positional and keyword arguments

# Example:
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 10)

# Output:
# I have a 10 year old dog named Buddy

# Parsing Different Data Types:
# - You can pass different data types to a function

# Example:
def my_function(fruits):
    for fruits in fruits:
        print(fruit)

my_funtion = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Output:
# apple
# banana
# cherry

# Return Values:
# - Functions can return values using the return statement:

# Example:
def my_function(x):
    return x + y

result = my_function(5, 3)
print(result)

# Output:
# 8

# Returning Different Data Types
# - Functions can return any data type, including lists, tuples, dictionaries, and more.

# Example: A function that returns a list:

def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])

# Output:
# apple
# banana

# Positional-Only Arguments:
# - You can specify that a function can have ONLY positional arguments.
# - To specify positional-only arguments, add , / after the arguments:

# Example:
def my_function(name, /):
    print("Hello", name)

my_function("Adnan")

# Output:
# Hello Adnan

# Keyword-Only Arguments: To specify that a function can have only keyword arguments, add *, before the arguments:

# Example:
def my_function(*, name):
  print("Hello", name)

my_function(name = "Ahmad")

# Output:
# Hello Ahmad

# Combining Positional-Only and Keyword-Only
# - Arguments before / are positional-only, and arguments after * are keyword-only:

# Example:
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 25)
print(result)

# Output:
# 55





