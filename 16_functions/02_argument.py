"""
Topic: Python Function Arguments
Date: 2026-02-24
Concept Covered: 
- function arguments
-
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

