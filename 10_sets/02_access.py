"""
Topic: Accessing items in a set
Date: 2026-02-14
Concept Covered:
- Accessing items in a set
"""
# Accessing items in a set
# Sets are unordered, so we cannot access items using index
# We can access items using for loop

# Example:
thisset = {"apple", "manogo", "grapes"}
for x in thisset:
    print(x)
# Output: apple, manogo, grapes (in any order)

# We can also use in operator to check if an item exists in a set
# Example:
thisset = {"apple", "manogo", "grapes"}
if "manogo" in thisset:
    print("manogo is in the set")
# Output: manogo is in the set

# Note: once the set is created, you cannot change the items in the set
# But you can add or remove items from the set