"""
Topic: Python Dictionaries
Date: 2026-02-15
Concept Covered:
- What is Dictionary?
- 
"""

# What is Dictionary?
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.

# Example:
# Create a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Note: As of Python 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Note: Dictionaries cannot have two items with the same key:

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Note: Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2020
print(thisdict)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Dictionary Length: The len() function returns the number of items in a dictionary.

# Example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

# Output: 3

# Dictionary Items - Data Types: The values in dictionary items can be of any data type.

# Example:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# Output: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# dict() constructor: It is also possible to use the dict() constructor to make a dictionary.

# Example:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
