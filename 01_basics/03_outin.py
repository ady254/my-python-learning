"""
Topic: Python Output/Input
Date: 2026-01-27
Concepts Covered:
- Python Text
- Python Numbers

"""

#Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:

print("Hello, World!")
print('Hello, World!')

#Python will give an error:
print(Hello, World!)
# this will cause an error

#Print Without a New Line

#If you want to print multiple words on the same line, you can use the end parameter:
print("Hello", end=" ")
print("World!")

print("Hello World!", end=" ")
print("I will print on the same line.")

#output:
Hello World! I will print on the same line.

#NOTE:Note that we add a space after end=" " for better readability.
 




 """
 Print Numbers


"""""
# You can  print many numbers using print() function
# However, unlike text, we don't put numbers inside double quotes:

print(2)
print(2006)
print(50000)

#You can also do math inside the print() function:

print(2 + 2)
print(2006 - 1)
print(50000 * 2)
print(50000 / 2)

#output:
4
2005
100000
25000.0