"""
topic: Python Numbers
Date: 2026-01-30
Concepts Covered:
- Numbers
- Integers
- Floats
- Complex Numbers
- Type Conversion
"""

# Integers
# Integers are whole numbers, positive or negative, without decimals, of unlimited length.

# Example:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Output:
# <class 'int'>
# <class 'int'>
# <class 'int'>

# Floats
# Floats are real numbers, positive or negative, containing one or more decimals.

# Example:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Output:
# <class 'float'>
# <class 'float'>
# <class 'float'>

# Complex Numbers
# Complex numbers are real numbers, positive or negative, containing one or more decimals.

# Example:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Output:
# <class 'complex'>
# <class 'complex'>
# <class 'complex'>"""

# Type Conversion
# Type conversion is the process of converting one data type to another.

# Example:

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# Output:
# 1.0
# 2
# (1+0j)
# <class 'float'>
# <class 'int'>
# <class 'complex'>

# NOTE: You cannot convert complex numbers into another number type.

# Random(): Python does not have a random() function to make a random number
# But Python has a built-in module called random that can be used to make random numbers

# Example: Import the random module, and display a random number from 1 to 9:

import random

print(random.randrange(1, 10))

# Output: 2



