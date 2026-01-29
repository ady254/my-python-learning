"""
Topic:  Data Types
Date: 2026-01-25
Concepts Covered:
- What is a Data Type?
- Bulit-in Data Types
- Creating Variables of Different Data Types

"""

# What is a Data Type?
# A data type is a classification of data that tells the compiler or interpreter how the programmer intends to use the data.

# Bulit-in Data Types
# 1. Numeric Data Types
#    - int: Integer (whole numbers)
#    - float: Floating-point number (decimal numbers)
#    - complex: Complex number (a + bj)

# 2. Text Data Type
#    - str: String (sequence of characters)

# 3. Boolean Data Type
#    - bool: Boolean (True or False)

# 4. Sequence Data Types
#    - list: Ordered, mutable sequence
#    - tuple: Ordered, immutable sequence
#    - range: Sequence of numbers

# 5. Mapping Data Type
#    - dict: Unordered, mutable collection of key-value pairs

# 6. Set Data Types
#    - set: Unordered, mutable collection of unique elements
#    - frozenset: Unordered, immutable collection of unique elements

# 7. Binary Data Types
#    - bytes: Immutable sequence of bytes
#    - bytearray: Mutable sequence of bytes
#    - memoryview: View of memory

# 8. None Type
#    - NoneType: Represents the absence of a value

# Example:
# Creating variables of different data types

age = 25              # int

height = 5.9          # float

complex_number = 2 + 3j  # complex

name = "Adnan"        # str

is_student = True     # bool

my_list = [1, 2, 3]   # list to create list use [] square brackets

my_tuple = (1, 2, 3)  # tuple to create tuple use () parentheses

my_dict = {"name": "Adnan", "age": 25}  # dict to create dict use {} curly brackets

my_set = {1, 2, 3}    # set

my_frozenset = frozenset({1, 2, 3})  # frozenset

my_bytes = b"Adnan"   # bytes

my_bytearray = bytearray(b"Adnan")  # bytearray

my_memoryview = memoryview(b"Adnan")  # memoryview

my_none = None        # NoneType
