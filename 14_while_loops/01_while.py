"""
Topic: Python- While loops
Date: 2026-02-21
Concept Covered:
- while loop
- break
- continue
"""

# While loop: With the while loop we can execute a set of statements as long as a condition is true.

# Example 1: 

i = 1
while i < 6:
    print(i)
    i += 1
# Output: 1 2 3 4 5

# Note: Remember to increment i, or else the loop will continue forever.

# break: With the break statement we can stop the loop even if the while condition is true:

# Example 2:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# Output: 1 2

# continue: With the continue statement we can stop the current iteration, and continue with the next:

# Example 3:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5

# else: With the else statement we can run a block of code once when the condition no longer is true:

# Example 4:

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# Output: 1 2 3 4 5 i is no longer less than 6

# Note: The else block will NOT be executed if the loop is stopped by a break statement.