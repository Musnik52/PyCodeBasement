n = int(input('Enter a number: '))
total = 0
for i in range(n+1):
    print(2**i)
    total += (2**i)
print('=\n',total)