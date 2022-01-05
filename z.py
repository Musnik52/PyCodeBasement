class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def print_area(self):
        print(f' area = {self.get_area()}')

    def __str__(self):
        return f'[Rectangle] width: {self.width} height: {self.height} '+\
            f'area-{self.get_area()} | ' + super().__str__()