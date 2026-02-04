"""
topic: Escape Characters
Date: 2026-02-04
concept covered: 
-Escape Character

"""

# What is Escape character and why we use? 
# Answer: To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

 txt = "We are the so-called "Vikings" from the north."
 # Output: SyntaxError: invalid syntax

 # To fix this problem we use escape character:

 txt = "We are the so-called \"Vikings\" from the north."
 print(txt)
 # Output: We are the so-called "Vikings" from the north.
