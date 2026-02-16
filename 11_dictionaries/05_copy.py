"""
Topic: Copy Dictionaries
Date: 2026-02-16
Concept Covered: Copy Dictionaries

"""

# Example: copy a dictionary
# You cannot copy a dictionary by simply typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# Example: copy a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
}
mydict = thisdict.copy()
print(mydict)

# Output: 
# {'brand': 'Ford', 'model': 'Ecosport', 'year': 2022, 'color': 'brown'}

# Example: copy a dictionary using dict() constructor
thisdict = {
    "brand": "Ford",
    "model": "Ecosport",
    "year": 2022,
    "color": "brown"
}
mydict = dict(thisdict)
print(mydict)

# Output: 
# {'brand': 'Ford', 'model': 'Ecosport', 'year': 2022, 'color': 'brown'}