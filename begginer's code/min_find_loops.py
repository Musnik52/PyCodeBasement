x = [[4, 8, 200],[4, 3000, -1], [5, 87, 12]]
l1=l2=None
for i in range(len(x)):
    for j in range(len(x[i])):
        if l2 == None: l2 = x[i][j]
        elif x[i][j] < l2: l2 = x[i][j]
    if l1 == None: l1 = l2
    elif l2 < l1: l1 = l2
print(l1)