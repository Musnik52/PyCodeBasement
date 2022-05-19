from random import randint

def guess_number():
    print('Welcome to - GUESS THE NUMBER!')
    limit = int(input('What is the max limit of the number you wish to guess? '))
    num = randint(0, limit)
    guess_count = 0
    while True:
        try:
            guess_attempt = int(input(f'Guess the number between 0 and {limit}: '))
            guess_count += 1
            if guess_attempt == num:
                print(f'Congratulations! The number was indeed {guess_attempt}.\nYou tried to guess that {guess_count} time(s)')
                break
            elif guess_attempt < num:
                print('Too low!')
                continue
            else:
                print('Too high!')
                continue
        except:
            print('Ivalid input! That still counts as a try. Please provide a number.')
            guess_count += 1
            continue