i = 0
sum = 0
while i <10:
    num = int(input(f'Enter {i+1} number: '))
    if num < 0: continue
    if num == sum:
        print(num)
        break
    sum += num
    i += 1
if num != sum: print('Not found')
