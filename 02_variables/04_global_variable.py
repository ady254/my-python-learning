"""
topic: Python Global Variables
Date: 2023-01-29
Concepts Covered:
- Global Variables
"""

# Global Variables
# Global variables are variables that are defined outside of a function and can be used by any function in the program.

# Example:

x = "Python"
def myfunc():
    print("I love " + x)

myfunc()

# Output: I love Python
# here, x is a global variable and can be used by any function in the program.

# Local Variables
# Local variables are variables that are defined inside a function and can only be used by the function in which they are defined.

# Example:

def myfunc():
    x = "Python"
    print("I love " + x)

myfunc()

# Output: I love Python
# here, x is a local variable and can only be used by the function in which it is defined.

# Global Keyword
# To create a global variable inside a function, we use the global keyword.

# Example:

def myfunc():
    global x
    x = "Python"

myfunc()

print(x)

# Output: Python
# here, x is a global variable and can be used by any function in the program.

# Example 2:

x = "awesome"

def myfunc():
    x = "Python"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# Output: 
# Python is Python
# Python is awesome
# here, x is a global variable and can be used by any function in the program.
