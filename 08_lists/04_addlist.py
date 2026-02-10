"""
Topic: Add list items
Date: 10-02-2026
Concept Covered:
- append()
- insert()
- extend()
"""

# append(): Adds an item to the end of the list

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

# Output: [1, 2, 3, 4, 5, 6]

# insert(): Inserts an item at a specific position

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

# Output: [1, 2, 6, 3, 4, 5]

# extend(): Adds items from an iterable to the end of the list

my_list = [1, 2, 3, 4, 5]
my_list.extend([6, 7, 8])
print(my_list)

# Output: [1, 2, 3, 4, 5, 6, 7, 8]