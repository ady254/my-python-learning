"""
Topic: Nestes Dictionaries
Date: 2026-02-16
Concept Covered: Nestes Dictionaries

"""

# Example: nested dictionaries
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

# Output: 
# {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# Example: access items in nested dictionaries
print(myfamily["child2"]["name"])

# Output: 
# Tobias