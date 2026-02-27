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



