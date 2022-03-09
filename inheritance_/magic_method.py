
class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __iadd__(self, other):
        self.value += other.value
        return self.value

    def __isub__(self, other):
        self.value -= other.value
        return self.value

    def __imul__(self, other):
        self.value *= other.value
        return self.value

    def __idiv__(self, other):
        self.value /= other.value
        return self.value


class B:
    def __init__(self, value):
        self.value = value

    def __floordiv__(self, other):
        return self.value // other.value

    def __mod__(self, other):
        return self.value % other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


class C:
    def __init__(self, value):
        self.value = value

    def __pow__(self, power, modulo=None):
        return self.value ** power.value

    def __ipow__(self, other):
        self.value **= other.value
        return self.value

    def __ifloordiv__(self, other):
        self.value //= other.value
        return self.value

    def __imod__(self, other):
        self.value %= other.value
        return self.value


a = A(8)
b = B(120)
c = C(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b // a)
print(c ** a)
print(b < a)
print(b > a)
print(b >= a)
print(b <= a)
c **= a
print(c)
a += b
print(a)
a -= c
print(a)
a *= c
print(a)
a /= b
print(a)
c //= b
print(c)
c %= a
print(c)
