from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def printname(self):
        print (f'The shape is: {self.name}')
    
    def __str__(self):
        return f'The shape: {self.name}'

class Rectangle(Shape):

    def __init__(self, w, h, name):
        super().__init__(name)
        self.w = w
        self.h = h

    def printarea(self):
        print(f'The area is: {self.w*self.h}')

    def __str__(self):
        return f'Rectangle:  Width: {self.w}, Height: {self.h} '+super().__str__()

class Triangle(Shape):

    def __init__(self, a, b, c, h, name):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def printarea(self):
        print(f'The area is: {self.b*self.h/2}')

    def __str__(self):
        return f'Triangle:  A: {self.a}, B: {self.b}, C:{self.c}, H: {self.h} '+super().__str__()

rec = Rectangle(10,5,'Reckie')
tri = Triangle(10,20,5,5,'Tria')
print(rec)
print(tri)
rec.printarea()
tri.printarea()