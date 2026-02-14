"""
Topic: Python Tuples
Date: 2026-02-14
Concept Covered: Tuples
"""

# Tuple: Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable, and allow duplicate values
# Tuples are written with round brackets
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Example: Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# output: ('apple', 'banana', 'cherry')

# Ordered: Tuples are ordered, meaning that the items have a defined order, and that order will not change.
# Unchangeable: Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates: Tuples allow duplicate values means, the same item can appear more than once in a tuple.

# Tuple Length: To determine how many items a tuple has, use the len() function.

# Example: Print the number of items in the tuple
thistuple = ("apple", "mango", "cherry")
print(len(thistuple))

# output: 3

# Create a tuple with one item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example: Create a tuple with one item
thistuple = ("apple",)
print(type(thistuple))

# output: <class 'tuple'>

# Tuple Items - Data Types
# Tuple items can be of any data type

# Example: String, int and boolean data types
thistuple = ("apple", 3.14, True)
print(thistuple)

# output: ('apple', 3.14, True)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# Example: Using the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))         # note the double round-brackets
print(thistuple)

# output: ('apple', 'banana', 'cherry')

 # Major difference between lists and tuples

 # Lists are written with square brackets
 # Tuples are written with round brackets

 # Lists are changeable, meaning that we can modify, add, and remove items in a list after it has been created.
 # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
 
 # Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
 # Tuple items are ordered, meaning that the items have a defined order, and that order will not change.
 # tuple is immutable means, we cannot change, add or remove items after the tuple has been created.