num = int(input('Enter a number: '))
a = b = 1
while True:
    c = a + b
    if c > num:
        print ('Not in the fibonacci series.')
        break
    elif c == num:
        print (f'{num} is in the fibonacci series.')
        break
    else:
        a = b
        b = c