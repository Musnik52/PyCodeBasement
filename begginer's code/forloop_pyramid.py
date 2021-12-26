a =int(input('Enter 1st number: '))
b =int(input('Enter 2nd number: '))
for i in range(min(a,b),max(a,b)):
    print(i)
for j in range(max(a,b),min(a,b)-1,-1):
    print(j)