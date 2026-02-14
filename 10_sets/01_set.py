"""
Topic: Python - Sets
Date: 2026-02-14
Concept Covered:
- What is a set?
- len() function
- set() constructor
"""
# What is set?
# Sets are used to store multiple items in a single variable
# Sets are unordered, unindexed, and do not allow duplicate values
# Sets are mutable, meaning they can be changed
# Set are written with curly brackets {}

# Creating a set
my_set = {"apple", "banana", "cherry"}
print(my_set)

# Unordered means- that the items in a set do not have a defined order
# Unchangeable means- that the items in a set cannot be changed
# Duplicates are not allowed
# Note: In set "True" and "1" are considered as same value
# Note: In set "False" and "0" are considered as same value

# Get the length of a set
# use len() function

# Example:
thisset = {"apple", "manogo", "grapes"}
print(len(thisset))
# Output: 3

# set() constructor
# use set() function to create a set

# Example:
thisset = set(("apple", "manogo", "grapes")) # Note the double parentheses
print(thisset)
# Output: {'apple', 'manogo', 'grapes'}
