"""
Topic: Python pass statement
Date: 2026-02-19
Concept Covered:
- pass statement
- 
-
-
"""
# What is pass statement?
# The pass statement is a null operation -  nothing happens when it executes. It serves as a placeholder.

# Example:
a = 33
b = 200

if b > a:
    pass

# Why Use pass?
#The pass statement is useful in several situations:
#When you're creating code structure but haven't implemented the logic yet
#When a statement is required syntactically but no action is needed
#As a placeholder for future code during development
#In empty functions or classes that you plan to implement later

# Pass vs Comments
# A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). You need pass where Python expects a statement, not just a comment.


# pass with Multiple Conditions: You can use pass in any branch of an if-elif-else statement.
#Example: 
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass  # Zero case - no action needed
else:
  print("Positive value")

# Output: Positive value

# pass in Other Contexts
# While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.

# Example
# Using pass with functions:

def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet
