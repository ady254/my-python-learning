"""
Topic: Python Change Dictionary Items & Add Dictionary Items
Date: 2026-02-16
Concept Covered:
- Change values
- Update Dictionary
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



    