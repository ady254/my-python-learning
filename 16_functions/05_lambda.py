"""
Topic: Python Lambda
Date: 2026-02-27
Concept Covered: 
- Lambda
"""

# What is lambda function?
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression

# Example: Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# Output:
# 15

# Lambda functions can take any number of arguments:

# Example: Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

# Output:
# 30

# Why Use Lambda Functions?
#  The power of lambda is better shown when you use them as an anonymous function inside another function.

# Example: 
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Output: 22

# use the same function definition to make both functions, in the same program:
# Example:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Output: 
# 22
# 33

# Use lambda functions when an anonymous function is required for a short period of time.

# Lambda functions are commonly used with built-in functions like:
# map()
# filter()
# sorted()

# Using Lambda with map()

# Example: Double all numbers in a list:

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Output: [2, 4, 6, 8, 10]

# Using filter()

# filter out even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# using sorted()

students = [("Adnan", 19), ("Python", 33), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#Output:  [('Python', 33), ('Adnan', 19), ('Linus', 28)]



