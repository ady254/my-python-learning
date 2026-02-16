"""
Topic: Python Change Dictionary Items & Add Dictionary Items & Remove Dictionary Items
Date: 2026-02-16
Concept Covered:
- Change values
- Update Dictionary
- Add Dictionary Items
- Remove Dictionary Items
"""

# Example: Change values
thisdict = {
    "brand": "Yamaha"
    "model": "rx100"
    "year": 1994
}
thisdict["year"] = 2000
print(thisdict)
# Output: {'brand': 'Yamaha', 'model': 'rx100', 'year': 2000}

# Example: Update Dictionary
thisdict = {
    "brand": "Yamaha"
    "model": "rx100"
    "year": 1994
}
thisdict.update({"year": 2000})
print(thisdict)
# Output: {'brand': 'Yamaha', 'model': 'rx100', 'year': 2000}

# Example: Add Dictionary Items
thisdict = {
    "brand": "Yamaha"
    "model": "rx100"
    "year": 1994
}
thisdict["color"] = "red"
print(thisdict)
# Output: {'brand': 'Yamaha', 'model': 'rx100', 'year': 1994, 'color': 'red'}

# Example: update Dictionary using update()
thisdict = {
    "brand": "Yamaha"
    "model": "rx100"
    "year": 1994
}
thisdict.update({"year": 2000})
print(thisdict)
# Output: {'brand': 'Yamaha', 'model': 'rx100', 'year': 2000}


# Remove Dictionary Items
# Example: using pop()
thisdict = {
    "brand": "yamaha"
    "model": "rx100"
    "year": 1994
}
thisdict.pop("year")
print(thisdict)
# Output: {'brand': 'yamaha', 'model': 'rx100'}

# Example: using popitem(): remove the last inserted item 
thisdict = {
    "brand": "yamaha"
    "model": "rx100"
    "year": 1994
}
thisdict.popitem()
print(thisdict)
# Output: {'brand': 'yamaha', 'model': 'rx100'}

# Example: using del keyword: remove the item with the specified key name
thisdict = {
    "brand": "yamaha"
    "model": "rx100"
    "year": 1994
}
del thisdict["model"]
print(thisdict)
# Output: {'brand': 'yamaha', 'year': 1994}
