"""
Topic:Python Functions
Date: 2026-02-22
Concept: Functions
"""
# What is a function?
# A function is a block of code that performs a specific task.
# A function can return data as a result.
# A function helps avoiding code repetition.

# Why use functions?
# 1. Reusability
# 2. Modularity
# 3. Code Organization

# How to define a function?
def my_function():
    print("Hello, World!")

# How to call a function?
my_function()

# Function Parameters
# A parameter is a variable that is used to pass data into a function.
def my_function(name):
    print("Hello, " + name)

my_function("John")

# Function Arguments
# An argument is a value that is passed into a function.
def my_function(name):
    print("Hello, " + name)

my_function("John")

# Fuction names
# Function names follow the same rules as variable names in Python:
# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# Return Values
# Functions can send data back to the code that called them using the return statement.

# When a function reaches a return statement, it stops executing and sends the result back:

# A function that returns a value:

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# Output:
# Hello from a function