"""
Topic: Python Elif statement
Date: 2026-02-18
Concept Covered:
- Elif keyword
- Multiple Elif Statements
- when to use elif
"""
# The Elif keyword: The eilf keyword is python's way of saying "if the pervious conditions were not true, then try this condition"
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

# Example:
a = 33
b = 33

if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")

# Output:
# a and b are equal

# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

# Multiple Elif Statements:
# You can have multiple elif statements in a row.

# Example:
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

# Output:
# Grade: C

# In this example the first condition is not true, but the elif condition is true, so we print to screen that "Grade: C".

# When to Use Elif

# Example:
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

# Output:
# Wednesday

# In this example the first condition is not true, but the elif condition is true, so we print to screen that "Wednesday".