import random
guess = 1
num = random.randint(1,100)
unum = int(input("Welcome to Rando-Bingo! Guess the lucky number: "))
while unum != num:
    if unum < num: print('Too low!')
    else: print('Too high!')
    guess += 1
    unum = int(input('Try again: '))
print(f'Rando - BINGO! You had to guess {guess} times.')