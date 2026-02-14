"""
Topic: Python - Loop Tuple
Date: 2026-02-14
Concept Covered:
- for loop
- loop through the index number
- while loop
"""

# for loop: You can loop through the tuple items by using a for loop.

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

# Output:
# apple
# banana
# cherry

# Loop through the index numbers: You can loop through the tuple items by using the index numbers.
# Use the range() and len() functions to create a suitable iterable.

# Example: Print all items by referring to their index number:

thistuple = ("apple", "mango", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# Output:
# apple
# mango
# cherry

# While loop: You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple and then start the range from 0 and end at the length of the tuple.

# Example: Print all items by referring to their index number:

thistuple = ("apple", "mango", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

# Output:
# apple
# mango
# cherry




 
