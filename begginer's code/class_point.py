class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

pnt = Point(x = input('enter X value: '), y = input('enter Y value: '))
print(pnt)