"""
Topic: Python - Nested if
Date: 2026-02-18
Concept Covered:
- Nested if
"""

# Nested If statement:
# You can use an if statement inside another if statement. 
# This is called a nested if statement.

# Example:
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# Output:
# Above ten,
# and also above 20!

# Example 2:
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
# Output:
# Enter a number: 10
# The number is positive.

# How Nested If Works:
# 1. The outer if statement is checked first.
# 2. If the outer if statement is true, the inner if statement is checked.
# 3. If the outer if statement is false, the inner if statement is skipped.

# Multiple Levels of Nesting

# Note : You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.

# Example 3:
age = 25
is_student = True

if age >= 18: # Outer statement
    print("Adult")
    if is_student: # Inner statement
        print("Student discount applies")
    else:
        print("No student discount")
else:
    print("Minor")
# Output:
# Adult
# Student discount applies

# Nested If vs Logical Operators

# Example:
temp = 2
is_sunny = True

if temp > 20:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm but cloudy.")
else:
    print("It's cold outside.")
# Output:
# Perfect beach weather!

