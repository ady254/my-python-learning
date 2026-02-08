"""
Topic: Membership Operators
Date: 2026-02-08
Concept Covered:
- Membership Operators
"""

# Membership Operators: are used to check if a value is present in a sequence (like a list, tuple, string, or set) and return a boolean value (True or False).

# Types of membership operators:
# 1. In (in)
# 2. Not in (not in)

# Example:
list = [1, 2, 3, 4, 5]
print(1 in list)  # True
print(6 in list)  # False
print(1 not in list)  # False
print(6 not in list)  # True

# Output:
# True
# False
# False
# True

# Example: 
fruits = ["apple", "mango", "cherry"]

print("pineapple" not in fruits)

# Output:
# True
