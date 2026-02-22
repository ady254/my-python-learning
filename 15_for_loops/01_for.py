"""
Topic: Python For Loops
Date: 2026-02-22
Concept Covered:
- for loop
- range() function
- break statement
- continue statement
- pass statement
- nested for loop
- for loop with else statement
"""

# for loop:
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

# Example 1:
fruits = ["apple", "orange", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# orange
# banana
# cherry

# The range function: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example 2:
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# The break statement: The break statement is used to exit a loop.

# Example 3:
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# The continue statement: The continue statement is used to skip the current iteration of a loop.

# Example 4:
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4

# The pass statement: The pass statement is used to do nothing when a statement is required syntactically, but no action is needed.

# Example 5:

for x in [0, 1, 2]:
  pass


# Nested for loop: A nested for loop is a for loop inside another for loop.

# Example 6:

#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# Output:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry