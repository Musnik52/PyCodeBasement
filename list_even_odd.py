some_list = [1,4,7,12,19,22, 23, 26]
print([(str(some_list[i]) + ' is even') if some_list[i]%2 == 0 else (str(some_list[i]) + " is odd") for i in range(len(some_list))]) 