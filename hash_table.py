# What is hash table?
# A hash table is a data structure that stores data using a hash function so that we can performs operations like
# insert, search, delete...

# What is hash function?
# A hash function converts the key into a number eg: "adnan" 17 and then this table insert into a hash table at some position


# What is hash map?
# hash map = map a key to a value
# eg: marks = {
#       key < -- "adnan": 90   --> value
#       key <--"aman": 85    --> value
# }

# In python we called it dict its bult in hash map like data structure

# What is hash set?
# stores unique values for fast membership checking
# eg: nums = {10, 20, 30, 40}
# if 30 in nums: print(found)
# there is no key value
# just membership 
# real world exmaple when u entered in a clg library they only notice your enrollement not ur name coz if we go with name then same students exits which contain dupilcates
# In python: A set is a collection which is unordered, unchangeable*, and unindexed.

# Note: Python uses curly brackets {} both sets and dictionaries; dict key-value separated by colon; set contain unique element separated by commas
# {} creat an empty dictionary for set() for explict make empty coz set comes after dict in python langauge

# PROBLEM WITH HASH TABLE 
# hash collision : when two different keyd end up wanting the same hash table location

# to overcome this problem we use 2 approch
# 1. Separate Chaining 
# 2. Open addressing: Python uses mathematical formula to quickly jump to a nearby alternate slot in a sequence