"""
Topic: Python Logical Operators
Date: 2026-02-18
Concept Covered:
- and 
- or
- not
"""

# Python Logical Operators are used to combine conditional statemnets. Python has three logical operators

# and- returns true if both statements are true
# or- returns true if one of the statements is true
# not- reverses the result, returns false if the result is true


# The "and" keyword is a logical operator, and is used to combine conditional statements
# Both conditions must be true for the statement to be true
# Example 1: and operator
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")
# Output: Both conditions are true

# The "or" keyword is a logical operator, and is used to combine conditional statements
# At least one of the conditions must be true for the statement to be true
# Example 1: or operator
a = 200
b = 33
c = 500
if a > b or c > a:
    print("At least one of the conditions is true")
# Output: At least one of the conditions is true


#Combining Multiple Operators
# You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.

# Example: Combining and, or, and not:
age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("You get a discount!")
# Output: You get a discount!




