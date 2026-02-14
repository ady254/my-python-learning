"""
Topic: Access Tuple Items
Date: 2026-02-14
Concept Covered: Access Tuple Items
- access tuple items 
- negative indexing
- range indexing
- range of negative indexing
- check if item exists
"""

# Access Tuple Items
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Example: Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# output: banana

# Negative Indexing
# Negative indexing means start from the end

# Example: Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# output: cherry

# Range Indexing
# You can specify a range of indexes by specifying where to start and where to end the range.
# The return value will be a new tuple with the specified items.

# Example: Range Indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# output: ('cherry', 'orange', 'kiwi')

# Note: The search will start at index 2 (included) and end at index 5 (not included)

# Example: This example returns the items from the "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Range of Negative Indexing
# Specify negative indexes if you want to start the search from the end of the tuple.

# Example: This example returns the items from index -4 (included) to index -1 (excluded):

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])

# output: ('cherry', 'orange', 'kiwi')

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword.

# Example: Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple")

# output: Yes, 'apple' is in the tuple

