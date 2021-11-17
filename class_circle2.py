class Circle():
    def __init__(self, r):
        self.r = r

    def __add__(self, other):
        if type(other) == int or type(other) == float: return Circle(self.r + other)
        if type(self) != type(other): return Circle(self.r)
        return Circle(self.r + other.r)

    def __sub__(self, other):
        if type(other) == int or type(other) == float: return Circle(self.r - other)
        if type(self) != type(other): return Circle(self.r)
        return Circle(self.r - other.r)

    def __mul__(self, other):
        if type(other) == int or type(other) == float: return Circle(self.r * other)
        if type(self) != type(other): return Circle(self.r)
        return Circle(self.r * other.r)

    def __eq__(self, other):
        if type(other) == int or type(other) == float: return self.r == other
        if type(self) != type(other): return False
        return self.r == other.r

    def __gt__(self, other):
        if type(other) == int or type(other) == float: return self.r > other
        if type(self) != type(other): return False
        return self.r > other.r

    def __repr__(self):
        return f'Circle({self.r})'

    def __str__(self):
        return f'Circle Radius: {self.r}'

c1 = Circle(3)
print('__str__',c1)
c2 = Circle(8.7)
_lst = [c2, c1]
_lst.sort()
print('Sorted: ', _lst)
print('__repr__', _lst)
print(c1, ">", c2, "=", c1>c2)
c3 = Circle(8.7)
print(c2, "==", c3, ':', c2==c3)
print(c2, '==', 8.7, ':', c2 ==8.7)
print(c1, '+', c3, ':',c1 + c3)