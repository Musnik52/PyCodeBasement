from random import randint

min_num = int(input('Enter MIN number: '))
max_num = int(input('Enter MAX number: '))

print('Invalid input, bye!' if max_num < min_num else randint(min_num, max_num))