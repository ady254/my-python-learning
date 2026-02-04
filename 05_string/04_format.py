"""
Topic: Format
Date: 2026-02-04
Concept Covered:
- Format
- f-string
- placeholders
- modifiers
"""


# age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
 # The above example shows error because we are trying to add string and integer
 # This how Python introduced format() method to solve this problem

# What is format?
# Answer: The format() method or f-string is used to format a string
# F-String was introduced in python 3.6, and is now preferred way of formatting strings

#  put an f in front of the string literal, and add curly brackets 
# {} as placeholders for variables and other operations.

# Example:
# Create an f-sting

age = 23
txt = f"My name is Adnan, I am {age} years old"
print(txt)

# output: My name is Adnan, I am 23 years old

# What is placeholders and Modifiers?
# Answer: Placeholders are the curly brackets {} and modifiers are the characters inside the curly brackets

# Example:
price = 59
txt = f" The price is {price:.2f} dollars"
print(txt)

# Output: The price is 59.00 dollars
# Here :.2f is a modifier that formats the price to 2 decimal places

# Example: Performing a math operation in the placeholder

txt = f"The price is {20 * 4} dollars"
print(txt)

# Output: The price is 80 dollars

# Example: Using multiple placeholders
name = "Adnan"
age = 23

txt = f"My name is {name}, I am {age} years old"
print(txt)

# Output: My name is Adnan, I am 23 years old
