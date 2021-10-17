i = 0
while i<10:
    temp = int(input(f'Enter {i+1} temp: '))
    if 40<temp or temp<-5:
        print('Incorrect Data')
        break
    i += 1
if i == 10: print ('Correct')