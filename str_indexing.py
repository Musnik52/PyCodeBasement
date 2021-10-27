x = 'hello world!'
z =[]
for i in range(len(x)):
    if x[i] == 'o': z.append(i)
print(f' The first "o" is in index {z[0]}, the other one is in index {z[1]}')
print(x[:z[0]+1])
print(x[z[1]:])
print(f'{x[:4]}{x[6]}{x[8:]}')