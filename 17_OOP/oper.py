# Operator Overloading 

#example:
a = 4
b = 8

c = a + b 
#c = int.__add__(a, b)        # for convient we use c = a + b, otherwise developer dont use python we they code c = int.__add__(a, b)
#print(c)                         # here + operand
#print(c)

a = "4"
b = "8"
#d = a + b # here same operand but different result --- means + operator show polymorphism the output 48 



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
     def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

p1 = Point(2, 4)
p2 = Point(4, 5)
p3 = p1 + p2

