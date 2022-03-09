import math


class Square:
    def area(self, x):
        print(x * x)


class Circle(Square):
    def area(self, x):
        print(math.pi * x * x)


s = Square()
s.area(4)
c = Circle()
c.area(3)
