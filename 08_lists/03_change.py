"""
Topic: Change list items
"""

# Change list items, referring to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Output:
# ['apple', 'blackcurrant', 'cherry']

# Change list items, referring to the index number
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant", "orange"]
print(thislist)

# Output:
# ['apple', 'blackcurrant', 'orange', 'cherry']
