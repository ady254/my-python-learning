"""
Topic: Remove list items
Date: 10-02-2026
Concept Covered:
- remove()
- pop()
- del
- clear()
"""

# remove(): Removes the first occurrence of a value

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)

# Output: [1, 2, 4, 5]

# pop(): Removes an item at a specific position

my_list = [1, 2, 3, 4, 5]
my_list.pop(2)
print(my_list)

# Output: [1, 2, 4, 5]

# del: Removes an item at a specific position

my_list = [1, 2, 3, 4, 5]
del my_list[2]
print(my_list)

# Output: [1, 2, 4, 5]

# clear(): Removes all items from the list

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

# Output: []
