i = k = 0
num = total = above = 0
while True:
    num = int(input('Enter a Number. Entering "0" will end the program: '))
    if num == 0:
        print('You have entered a 0.\nEnd of program')
        break
    if num > 77:
        above += num
        i += 1
    total += num
    k += 1
    print(f'So far you have entered {k} numbers in total, and the sum of them is {total}\nand {i} numbers above 77, and the sum of them is {above}')