"""
Topic: Assign Multiple Values
Date: 2026-01-29
Concepts Covered:
- Assigning multiple values to multiple variables
- Assigning the one value to multiple variables
- What is unpacking?
"""

# Python allows you to assign values to multiple variables in a single line.

# Assigning multiple values to multiple variables

x, y, z = 10, 20, 30
print(x, y, z)

# Assigning the one value to multiple variables
# NOTE: Make sure the number of variables is equal to the number of values, otherwise it will give an error.
# Example: x, y, z = 10, 20, 30, 40 (This will give an error).

# Assigning the one value to multiple variables

x = y = z = 10
print(x, y, z)

x = y = z = "Orange"
print(x,y,z)

# What is unpacking?
# Unpacking is the process of assigning the values of an iterable (like a list or tuple) to variables.

# Example of unpacking

my_list = [10, 20, 30]
x, y, z = my_list
print(x, y, z)