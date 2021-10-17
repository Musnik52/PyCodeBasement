f = int(input('Enter the 1st number: '))
for i in range(1,10):
    num = int(input(f'enter the next number: '))
    if num < f: 
        print ('Not sorted')
        break
    f = num
if num>=f: print('sorted')
