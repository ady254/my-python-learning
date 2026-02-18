"""
Topic: Python Else Statement
Date:- 2026-02-18
Concept Covered:
- else keyword
- 
"""

# The Else keyword: The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

# Example:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Output:
#a is greater than b

# In this example: a is greater than b, so the else statement is executed.

# Else Without Elif
# Example:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Output:
# b is not greater than a
#Note : The else statement must come last. You cannot have an elif after than an else.

# Example: Checking even or odd numbers;
 number = 7
 if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Output: The number is odd

# Else as Fallback
#The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.

# Example: Validating user input:

username = "Adnan"

if len(username) > 0:
    print("Welcome, {username}!")
else:
    print("Error: Username cannot be empty")

# Output: Welcome, Adnan!







