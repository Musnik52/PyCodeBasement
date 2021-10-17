h = l = num = int(input('Enter a number.\nA negative number or 0 will end the program: '))
if num <= 0: print("You haven't entered a valid input yet.")
else:
    while num > 0:
        num = int(input('Enter a number.\nA negative number or 0 will end the program: '))
        if num > h: h = num
        elif 0 < num < l: l = num
    print(f'The highest value is {h} and the lowest is {l}')