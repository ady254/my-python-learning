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

# Copy method: copy() method creates a copy of the list

# Example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
newlist = thislist.copy()
print(newlist)

# Output:
['orange', 'mango', 'kiwi', 'pineapple', 'banana']

# Join method: join() method joins the elements of a list into a string

# Example:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
newlist = " ".join(thislist)
print(newlist)

# Output:
orange mango kiwi pineapple banana

# Use the slice Operator
# Copy of a list by using the : (slice) operator.

# Example: 
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Output:
['apple', 'banana', 'cherry']

# Join list --- There are two ways to join lists:

# 1. Using the join() method
# 2. Using the + operator

# Example: 
list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "mango", "kiwi"]
newlist = list1 + list2
print(newlist)

# Output:
['apple', 'banana', 'cherry', 'orange', 'mango', 'kiwi']

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# example:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Output:
['a', 'b', 'c', 1, 2, 3]

# Example: Using extend() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)

print(list1)

# Output:
['a', 'b', 'c', 1, 2, 3]
