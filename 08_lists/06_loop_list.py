"""
Topic: Loop Lists
Date: 10-02-2026
Concept Covered:
- for loop
- while loop
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