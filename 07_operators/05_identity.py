"""
Topic: Identity Operators
Date: 2026-02-08
Concept Covered:
- Identity Operators
"""

# Identity Operators: are used to compare the memory locations of two objects and return a boolean value (True or False).

# Types of identity operators:
# 1. Is (is)
# 2. Is not (is not)

# Example:
x = 5
y = 10
print(x is y)  # False
print(x is not y)  # True

# Example:
x = ["apple", "banana, cherry"]
y = ["apple", "banana, cherry"]
print(x is y)  # False
print(x is not y)  # True

# Output:
# false
# true
