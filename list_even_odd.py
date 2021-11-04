some_list = [1,4,7,12,19,22, 23, 26]
print([(str(i) + ' is even') if i%2 == 0 else (str(i) + " is odd") for i in some_list]) 