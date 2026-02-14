"""
Topic: Python - Join sets
Date: 2026-02-14
Concept Covered:
- union() method
- intersection() method
- difference() method
- symmetric_difference() method
"""

# union() method: the union() method returns a new set with all items from both sets

# Example:
set1 = {1, 2, 3}
set2 = {"a", "b", "c"}

set3 = set1.union(set2)
print(set3)

# Example 2:
# using | operator instead of union() method

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# join multiple sets
# All the joining methods can be used to join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena", "Smith"}
set4 = {"python", "java", "c++"}

myset = set1.union(set2, set3, set4)
print(myset)
# Output: {1, 2, 3, 'a', 'b', 'c', 'John', 'Elena', 'Smith', 'python', 'java', 'c++'}

# You can also use | operator to join multiple sets
myset = set1 | set2 | set3 | set4
print(myset)
# Output: {1, 2, 3, 'a', 'b', 'c', 'John', 'Elena', 'Smith', 'python', 'java', 'c++'}

# Join a set and a tuple
# use union() method

# Example:
x = {"java", "python", "c++"}
y = ("c", "c++", "java")

z = x.union(y)
print(z)
# Output: {'java', 'python', 'c++', 'c'}

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# intersection() method: the intersection() method returns a new set with items that are common to both sets

# Example:
set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set3 = set1.intersection(set2)
print(set3)
# Output: {'apple'}
# You can also use & operator instead of intersection() method, and you will get the same result

set3 = set1 & set2
print(set3)
# Output: {'apple'}

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the  intersection() method.

# intersection_update() method: the intersection_update() method removes all items from the original set that are not present in the other set(s)

# Example:
set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set1.intersection_update(set2)
print(set1)
# Output: {'apple'}

# You can also use &= operator instead of intersection_update() method, and you will get the same result

set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set1 &= set2
print(set1)
# Output: {'apple'}

# Note: The &= operator only allows you to join sets with sets, and not with other data types like you can with the  intersection_update() method.

# difference() method: the difference() method returns a new set with items that are present in the first set but not in the second set

# Example:
set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set3 = set1.difference(set2)
print(set3)
# Output: {'banana', 'orange'}

# You can also use - operator instead of difference() method, and you will get the same result

set3 = set1 - set2
print(set3)
# Output: {'banana', 'orange'}

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the  difference() method.

# difference_update() method: the difference_update() method removes all items from the original set that are present in the other set(s)

# Example:
set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set1.difference_update(set2)
print(set1)
# Output: {'banana', 'orange'}

# You can also use -= operator instead of difference_update() method, and you will get the same result

set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set1 -= set2
print(set1)
# Output: {'banana', 'orange'}
    
# Note: The -= operator only allows you to join sets with sets, and not with other data types like you can with the  difference_update() method.

# symmetric_difference() method: the symmetric_difference() method returns a new set with items that are present in either of the sets, but not in both

# Example:
set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set3 = set1.symmetric_difference(set2)
print(set3)
# Output: {'banana', 'orange', 'kiwi', 'mango'}

# You can also use ^ operator instead of symmetric_difference() method, and you will get the same result

set3 = set1 ^ set2
print(set3)
# Output: {'banana', 'orange', 'kiwi', 'mango'}

# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the  symmetric_difference() method.

# symmetric_difference_update() method: the symmetric_difference_update() method removes all items from the original set that are present in the other set(s)

# Example:
set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set1.symmetric_difference_update(set2)
print(set1)
# Output: {'banana', 'orange', 'kiwi', 'mango'}

# You can also use ^= operator instead of symmetric_difference_update() method, and you will get the same result

set1 = {"apple", "banana", "orange"}
set2 = {"apple", "kiwi", "mango"}

set1 ^= set2
print(set1)
# Output: {'banana', 'orange', 'kiwi', 'mango'}

# Note: The ^= operator only allows you to join sets with sets, and not with other data types like you can with the  symmetric_difference_update() method.
