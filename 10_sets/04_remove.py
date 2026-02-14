"""
Topic: Python- Remove Set Items
Date: 2026-02-14
Concept Covered:
- remove() method
- discard() method
- pop() method
- clear() method
- del keyword
"""
# remove() method
# Use the remove() method to remove an item from a set

# Example:
thisset = {"apple", "manogo", "grapes"}
thisset.remove("manogo")
print(thisset)
# Output: {'apple', 'grapes'}

# discard() method
# Use the discard() method to remove an item from a set

# Example:
thisset = {"apple", "manogo", "grapes"}
thisset.discard("manogo")
print(thisset)
# Output: {'apple', 'grapes'}
# Note: If the item remove does not exist, remove() will raise an error, but discard() will not.

# pop() method
# Use the pop() method to remove an item from a set

# Example:
thisset = {"apple", "manogo", "grapes"}
thisset.pop()
print(thisset)
# Output: {'apple', 'grapes'} (in any order)

# clear() method
# Use the clear() method to remove all items from a set

# Example:
thisset = {"apple", "manogo", "grapes"}
thisset.clear()
print(thisset)
# Output: set()

# del keyword
# Use the del keyword to remove an item from a set

# Example:
thisset = {"apple", "manogo", "grapes"}
del thisset
print(thisset)
# Output: set() (the set is deleted)

# Note: del keyword will delete the set, not just remove an item.