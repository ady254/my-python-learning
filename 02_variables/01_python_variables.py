"""
Topic: Python Variables
Date: 2026-01-29
Concepts Covered:
- What is a Variable?
- Rules for Variable Names
- Creating a Variable
- Variable Naming Rules and Multi Words Variable Names

"""

# What is a Variable?
# A variable is a container for storing data values.
# In Python, we don't need to declare the type of a variable.
# Python automatically allocates memory for the variable based on the data type.

# Creating a Variable
# We can create a variable by assigning a value to it using the assignment operator (=).

# Variable Naming Rules
# 1. Variable names must start with a letter or an underscore (_).
# 2. Variable names cannot start with a number.
# 3. Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
# 4. Variable names are case-sensitive (age, Age, and AGE are different variables).
# 5. Variable names cannot be Python keywords (e.g., if, else, for, while, etc.).

# Example:
# Creating a variable
age = 25

# Printing the variable
print(age)

# Changing the value of a variable
age = 30
print(age)

# Variable Naming Rules Example:

# Valid variable names & Multi Words Variable Names

my_variable_name = "Adnan"          #snake case: Each word is separated by an underscore character:
myVariableName = "Ahmad"            #camel case: Each word starts with a capital letter except the first word:
MyVariableName = "Ahmad"            #pascal case: Each word starts with a capital letter

# Invalid variable names
# 1my_variable = 10  # Cannot start with a number
# my-variable = 20  # Cannot contain a hyphen
# my variable = 30  # Cannot contain a space
# for = 40  # Cannot be a keyword