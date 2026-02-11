"""
Topic: Loop Lists
Date: 10-02-2026
Concept Covered:
- for loop
- while loop
- List Comprehension
"""
# for loop: 
# Use for when:
   # You already know what to loop over
   # You have a list, tuple, range
   # You don't care about the index much

# Example 1:
fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)


# output:
# apple
# banana
# cherry  


# Loop through the index numbers
# Use for when:
   # You need the index number
   # You need to modify the list
   # You need to access elements by index

# Example 2:
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])


# output:
# apple
# banana
# cherry 


# while loop: "Keep going until something changes"
# Use while when:
   # You don’t know how many times the loop will run
   # Loop depends on a condition
   # Waiting for user input / game / retry logic

# Example 3:
count = 0
while count < 5:
    print(count)
    count += 1


# output:
# 0
# 1
# 2
# 3
# 4

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# output:
# apple
# banana
# cherry


# List Comprehension: offers a shorter syntax when you want to create a new list based on the values of an existing list

# Example: based on a list of fruits, you want a new list, containing ony the fruits with the letter "a" in the name
# without list comprehension you will have to write a "for" statement with a conditional test inside
# Example: without list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# output:
# ['apple', 'banana', 'mango']

# with list comprehension:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# output:
# ['apple', 'banana', 'mango']