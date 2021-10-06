i = 0
f = int(input('Enter the 1st number: '))
while i<9:
    s = int(input(f'Enter the {i+2} number: '))
    if s < 0: continue
    if s < f:
        print ('Not Sorted')
        break
    f=s
    i += 1
if s>=f: print('sorted')