i = 1
same = None
print ('Welcome to the LevelGame.\nEnter a fully-devidavle number by the level number to advance.\nEntering the same number twice in a row will end your game.') 
while i <= 10:
    num = int(input(f' Level #{i}: '))
    if num == same:
        i += 1
        break
    else: same = num
    if num < 0: continue
    if num%i == 0:
        i += 1
print(f'Thank you for playing. You reached level {i-1}.')