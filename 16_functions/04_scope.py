"""
Topic: Python Scope
Date: 2026-02-26
Concept Covered: 
- Scope

"""

#  What is Scope?
# - A variable is only available from inside the region it is created. This is called scope.

# What is Local Scope?
# -A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Example:

#A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

# Output:
# 300

# Whatis Global Scope?
# - A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Example:

x = 100

def myfunc():
  print(x)

myfunc()

print(x)

# Output:
# 100
# 100

# Global Keyword: The global keyword makes the variable global

# Example:
#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 100

myfunc()

print(x)

#Output:
# 100