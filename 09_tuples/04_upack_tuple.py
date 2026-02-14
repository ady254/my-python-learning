"""
Topic: Python - Unpack Tuples
Date: 2026-02-14
Concept Covered:
- Unpacking Tuples
- Unpacking with Asterisk
"""

# Unpacking Tuples: 
# When we create a tuple, we normally assign values to variables. This is called "Packing" a tuple

# Example: Packing a tuple 
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple 
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Output: 
# apple
# banana
# cherry

# Unpacking with Asterisk: 
# If the number of variables is less than the number of values, 
# you can add an asterisk (*) to the variable name and the values will be assigned to the variable as a list:

# Example: Unpacking with asterisk 
fruits = ("apple", "banana", "cherry", "orange", "mango")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Output: 
# apple
# banana
# ['cherry', 'orange', 'mango']
