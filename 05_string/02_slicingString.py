"""
Topic: Slicing String
Date: 2026-02-04
Concepts Covered:
- Slicing String
"""

# What is Slicing String?
# Ans: Slicing String is a way to extract a portion of a string.

# How to slice a string?
# Ans: String can be sliced using slicing operator.
#NOTE: The first character is at index 0.

# Example:
b = "Hello, World!"
print(b[2:5])

# Output:
# llo
#Note: The last index is not included in the slice.

# Slice from the start:
x = "Hello, World!"
print(x[:5])

# Output:
# Hello

# Slice to the end:
u = "Hello, Python"
print(u[7:])

# Output:
# Python

# Negative Slicing:
# Negative slicing is used to slice a string from the end.
# Example:

b = "Hello, Adnan!"
print(b[-1])

# Output:
# !

# Example 2:

x = "Welcome"

print(x[-4:])

# Output:
# come



