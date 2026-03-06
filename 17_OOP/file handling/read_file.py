"""
Topic: python file handling
"""

# Python has several functions for creating, reading, updating, and deleting files.

# 1. Open a file
# The open() function opens a file and returns a file object. 
# The file object has methods for reading, writing, and modifying files.

# Syntax: open(file, mode)
# file: The path to the file.
# mode: A string that specifies the mode in which the file is opened.

# Common modes:
# 'r' - Read (default)
# 'w' - Write
# 'a' - Append
# 'x' - Create
# 'b' - Binary mode
# 't' - Text mode (default)

# Example:
file = open("file.txt", "r")
print(file.read())  # Read the entire file
file.close()  # Close the file

# 2. Read a file
# There are several ways to read a file:
# read() - Reads the entire file
# readline() - Reads one line at a time
# readlines() - Reads all lines into a list

# Example:
file = open("file.txt", "r")
print(file.read())  # Read the entire file
file.close()

file = open("file.txt", "r")
print(file.readline())  # Read one line
file.close()

file = open("file.txt", "r")
print(file.readlines())  # Read all lines into a list
file.close()

# 3. Write to a file
# There are several ways to write to a file:
# write() - Writes a string to the file
# writelines() - Writes a list of strings to the file

# Example:
file = open("file.txt", "w")
file.write("Hello World")  # Write a string
file.close()

file = open("file.txt", "w")
file.writelines(["Hello", "World"])  # Write a list of strings
file.close()

# 4. Append to a file
# The append() method appends a string to the end of the file.

# Example:
file = open("file.txt", "a")
file.write("Hello World")  # Append a string
file.close()

# 5. Delete a file
# The remove() method deletes a file.

# Example:
import os
os.remove("file.txt")  # Delete the file

