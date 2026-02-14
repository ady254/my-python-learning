"""
Topic: Python- Add Set Items
Date: 2026-02-14
Concept Covered:
- add() method
- update() method
"""
# add() method
# Use the add() method to add an item to a set

# Example:
thisset = {"apple", "manogo", "grapes"}
thisset.add("orange")
print(thisset)
# Output: {'apple', 'manogo', 'grapes', 'orange'}

# update() method
# Use the update() method to add multiple items to a set

# Example:
thisset = {"apple", "manogo", "grapes"}
thisset.update(["orange", "mango", "kiwi"])
print(thisset)
# Output: {'apple', 'manogo', 'grapes', 'orange', 'mango', 'kiwi'}
