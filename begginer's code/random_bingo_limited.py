import random

def game(round):
    num = random.randint(1,100)
    guess = 1
    unum = int(input(f"Welcome to round {round+1} of Rando-Bingo! Guess the lucky number: "))
    while unum != num:
        if unum < num: print('Too low!')
        else: print('Too high!')
        guess += 1
        unum = int(input('Try again: '))
    print(f'Rando - BINGO! You had to guess {guess} times.')
    return guess

y = 0
for i in range(3):
    x = game(i)
    if x < y or y == 0: y = x
print(f'The least number of guesses was: {y}')