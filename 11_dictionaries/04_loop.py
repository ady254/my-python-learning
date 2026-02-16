"""
Topic: loop through a dictionary
Date: 2026-02-16
Concept Covered:
- loop through a dictionary
- values() method
- items() method
- keys() method
"""

# Example: loop through a dictionary
 thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
 }
for x in thisdict:
    print(x)

# Output: 
brand
model
year
color
# Example: print all values in the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
}
for x in thisdict:
    print(thisdict[x])

# Output: 
Ford
Ecosport
2022
brown

# values() method
thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
}
for x in thisdict.values():
    print(x)

# Output: 
Ford
Ecosport
2022
brown

# items() method
thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
}
for x in thisdict.items():
    print(x)

# Output: 
brand Ford
model Ecosport
year 2022
color brown

# keys() method
thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
}
for x in thisdict.keys():
    print(x)

# Output: 
brand
model
year
color
