"""
Topic: Access Dictionary Items
Date: 2026-02-15
Concept Covered:
- Accessing Dictionary Items
- Get key values
- Get values
- Get items
- Check if key exists
"""

# Example: Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example: Get the value of the "model" key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
 # Output: Mustang

# Get Values: using values()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
# Output: dict_values(['Ford', 'Mustang', 1964])

# Get Items: using items()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
# Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Output: Yes, 'model' is one of the keys in the thisdict dictionary
