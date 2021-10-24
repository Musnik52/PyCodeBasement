def get_c_area(radius):
    return 3.14*radius**2

def get_c_hekef(radius):
    return 2*3.14*radius

def get_r_area(width, hight):
    return width*hight

def get_r_hekef(width, hight):
    return 2*(width + hight)

r = float(input('Enter radius: '))
w = int(input('Enter width: '))
h = int(input('Enter hight: '))
print (f"The circle's area is {get_c_area(r)}\nand it's hekef is {get_c_hekef(r)}")
print (f"The ractangle's area is {get_r_area(w, h)}\nand it's hekef is {get_r_hekef(w, h)}")