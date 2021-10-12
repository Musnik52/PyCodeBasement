num = int(input('Enter a number: '))
a = b = 1
while True:
    c = a + b
    if c > num:
        print (f'{c} is the next bigger fibonacci number.')
        break
    else:
        a = b
        b = c