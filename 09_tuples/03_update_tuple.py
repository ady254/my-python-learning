"""
Topic: Python Update Tuples
Date: 2026-02-14
Concept Covered:
- How to change tuple values?
- Add items to a tuple
- Remove items from a tuple
- add tuple to another tuple
"""

# How to change tuple values?
# Tuples are immutable, so we cannot change them directly.
# We can convert the tuple to a list, change it, and then convert it back to a tuple.

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)
my_list[0] = 10
my_tuple = tuple(my_list)
print(my_tuple)

# Output: (10, 2, 3, 4, 5) 

# Add items to a tuple
# We can add items to a tuple by converting it to a list, adding items, and then converting it back to a tuple.

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)
my_list.append(6)
my_tuple = tuple(my_list)
print(my_tuple)

# Output: (1, 2, 3, 4, 5, 6)

# Remove items from a tuple
# We can remove items from a tuple by converting it to a list, removing items, and then converting it back to a tuple.

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)
my_list.remove(3)
my_tuple = tuple(my_list)
print(my_tuple)

# Output: (1, 2, 4, 5)

# Add tuple to another tuple
# We can add tuple to another tuple by converting it to a list, adding items, and then converting it back to a tuple.

my_tuple = (1, 2, 3, 4, 5)
my_tuple2 = (6, 7, 8, 9, 10)

my_list = list(my_tuple)
my_list.extend(my_tuple2)
my_tuple = tuple(my_list)
print(my_tuple)

# Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
