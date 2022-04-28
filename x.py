def print_matrix(data): #O(4) == O(2*2) == O(n*m) == O(n^2)
    for i in range(len(data)): # O(2)
        for k in range(len(data[i])): # O(2)
            print(data[i][k])  

print_matrix([[1, 2], [3, 4]])  # size is 2*2 = 4
