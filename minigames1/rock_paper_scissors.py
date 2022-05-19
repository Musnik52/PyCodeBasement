from random import choice


def rockpaperscissors():
    print("Let's play - ROCK - PAPER - SCISSORS!")
    r, p, s = 'rock', 'paper', 'scissors'
    tools = [r, p, s]
    win_count = 0
    while True:
        user_choice = input(f'Choose {r}, {p} or {s} -> ').lower()
        computer_choice = choice(tools)
        if user_choice not in tools or user_choice == computer_choice:
            print(
                f'You chose {user_choice}, and the computer chose {computer_choice} - Choose again!')
            continue
        elif (user_choice == r and computer_choice == s) or (user_choice == s and computer_choice == p) or (user_choice == p and computer_choice == r):
            print(f'You win! {user_choice} beats {computer_choice}.')
            win_count += 1
        else:
            print(f'You lose! {user_choice} loses to {computer_choice}.')
            win_count = win_count - 1 if win_count > 0 else 0
        print(f'Total score: {win_count}')
        one_more = input('Wanna go again?\n(y/n) ').lower()
        if one_more == 'y':
            continue
        else:
            print('Goodbye!')
            break
