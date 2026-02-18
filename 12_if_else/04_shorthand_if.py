"""
Topic: Python shorthand if
Date: 2026-02-18
Concept Covered:
- Short hand if
- Shorthand if with else
"""
# Shorthand if
# If you have a simple if statement with only one line of code, you can write it on the same line as the if statement.

age = 20

if age >= 18: print("You are an adult")

# Output: You are an adult
#Note : You still need the colon : after the condition

# Shorthand if with else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

a = 2
b = 330
print("A") if a > b else print("B")

# Output: B
# This is called a conditional expression (sometimes known as a "ternary operator").

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

age1 = 17
age2 = 18

bigger = age1 if age1 > age2 else age2
print(bigger)

# Output: 18

# When to use shorthand if:
# Shorthand if statements and ternary operators should be used when:
# - The condition and actions are simple
# - It improves code readability
# - You want to make a quick assignment based on a condition
