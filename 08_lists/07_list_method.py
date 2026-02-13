"""
Topic: Type list
Date: 2026-02-13
Concept Covered:
- Sort method
- Copy method
- Join method
"""

# sort() method
# sort() method sorts the list in ascending order
# Note: The sort() method is case sensitive--  returns error if list contains both upper and lower case letters

# Example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Output:
['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Output:
[23, 50, 65, 82, 100]

# sort in descending order

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Output:
[100, 82, 65, 50, 23]

# Customize Sort Function: ustomize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first)

# Example:
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

# Output:
[50, 65, 23, 82, 100]


