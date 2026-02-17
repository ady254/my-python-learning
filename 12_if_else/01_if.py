"""
Topic: Python If Statement
Date: 2026-02-17
Concept Covered: If Statement
"""
# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


#These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# Example:
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Output:
b is greater than a


# Example 2:
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Output:
b is greater than a

#In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".


# Indentation
# Python relies on indentation (whitespace) to define code blocks. 
# The code inside an if statement must be indented.

if 10 > 5:
    print("10 is greater than 5")  # This line is indented, so it belongs to the if block
print("This line is not indented")  # This line is outside the if block

# Output:
10 is greater than 5
This line is not indented

# How If Statements Work
# The if statement checks if a condition is true. 
# If it is true, the code inside the if block is executed.
# If it is false, the code inside the if block is skipped.

# Example:
number = 15
if number > 0:
  print("The number is positive")

# Output:
The number is positive

#Note:  You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.

# Multiple Statements in If Block

# Example
# :
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# Output:
You are an adult
You can vote
You have full legal rights

# Using Variables in Conditions

is_logged_in = True
if is_logged_in:
  print("Welcome back!")

# Output:
Welcome back!

# Note: 
# Python can evaluate many types of values as True or False in an if statement.

# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.

# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).