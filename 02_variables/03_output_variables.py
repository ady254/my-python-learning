"""
Topic: Output Variables
Date: 2026-01-29
Concepts Covered:
- Outputting variables
"""

# Outputting variables
# We can output variables using the print() function.

# Example:

x = "Python is awesome"
print(x)

# Output: Python is awesome
# We use print() function to output variables.

#Now, We will see how to output multiple variables.

# Example:

x = "Python"
y = "is"
z = "awesome"

print(x, y, z)

# Output: Python is awesome
# to print multiple variables, we use comma separated values in the print() function.
# By default, print() function adds a space between the values.

# Now, we will see how to print values using + operator.

# Example:

x = "Python"
y = "is"
z = "awesome"

print(x + y + z)

# Output: Pythonisawesome
# to print multiple variables, we use + operator to concatenate the values.
# By default, + operator adds no space between the values.

# Now, we will see how to print values using + operator with spaces.

# Example:

x = "Python"
y = "is"
z = "awesome"

print(x + " " + y + " " + z)

#OR
x = "Python "
y = "is "
z = "awesome "

print(x + y + z)

# Output: Python is awesome
# to print multiple variables, we use + operator to concatenate the values.
# By default, + operator adds no space between the values.
# To add space between the values, we use " " in the print() function.  

# here, + operator also works as a mathematical operator.

# Example:

x = 10
y = 5

print(x + y)

# Output: 15
# here, + operator works as a mathematical operator.

# NOTE: We cannot use + operator to concatenate strings and numbers.

# Example:

x = "Car"
y = 5
print(x + y)

# Output: TypeError: can only concatenate str (not "int") to str
# here, + operator cannot concatenate strings and numbers.