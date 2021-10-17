print('Welcome to "The Hangman"')
lh = h = rh = b = ll = rl = " "
ans = ['c','C','o','f','f','i','n']
answer = ['C','_','_','_','i','_']
wl = []
while rl != "\ ":
    print('\nHe who makes me - does not want me.')
    print('He who wants me - does not need me.')
    print('He who needs me - does not know it.')
    print(f'Answer: {answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]}')
    print(f'         ___________ ')
    print(f'         ||         |')
    print(f'         ||         |')
    print(f'         ||       {lh} {h} {rh}')
    print(f'         ||         {b}')
    print(f'         ||        {ll} {rl} ')
    print(f'         ||')
    print(f'         ||')
    print(f'====================')
    print(f'Wrong letters: {wl} ')
    guess = input('Enter a letter: ')
    if guess not in ans:
        wl.append(guess)
        if h == "O":
            if b == '|':
                if rh == "/":
                    if lh == '\ ':
                        if ll == '/':
                            rl = '\ '
                        ll = '/'
                    lh = '\ '
                rh = '/'
            b = '|'
        h = 'O'
    else:
        if guess == 'o': answer[1] = 'o'
        elif guess == 'f':
            answer[2] = 'f'
            answer[3] = 'f'
        elif guess == 'i': answer[4] = 'i'
        elif guess == 'n': answer[5] = 'n'
    if answer == ans:
        print('You Win!')
        break
if rl == '\ ': 
    print('He who makes me - does not want me.')
    print('He who wants me - does not need me.')
    print('He who needs me - does not know it.')
    print(f'Answer: {answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]}')
    print(f'         ___________ ')
    print(f'         ||         |')
    print(f'         ||         |')
    print(f'         ||       {lh} {h} {rh}')
    print(f'         ||         {b}')
    print(f'         ||        {ll} {rl} ')
    print(f'         ||')
    print(f'         ||')
    print(f'====================')
    print('GAME OVER')