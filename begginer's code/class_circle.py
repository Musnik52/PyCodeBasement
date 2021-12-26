class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def calc_hekef(self):
        return 2*self.pi*self.radius

    def calc_area(self):
        return self.pi*self.radius**2

    def __str__(self):
        return f'Radius: {self.radius}, area:{self.calc_area()}, circumfrence: {self.calc_hekef()}'

circ = Circle(radius = int(input('Enter radius: ')), pi = 3.1415)
print(circ)