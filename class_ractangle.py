class Ractangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_area(self):
        return f'The surface area is {self.width} X {self.length} = {self.length*self.width}'
    
    def __len__(self):
        return self.width
        
    def __str__(self):
        return f'Width: {self.width}, Length: {self.length}'

rac = Ractangle(width = int(input('Enter width: ')), length = int(input('Enter length: ')))
print(rac)
print(rac.calc_area())
print('Length: ', len(rac))