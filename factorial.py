num = int(input('Enter a number: '))
k = i = 1
while i < num:
    k *= (i+1)
    i += 1
print(f'{num} factorial is {k}')