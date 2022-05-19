import random


def players(players=""):  # Choose who are the players
    players = input(
        'Enter wanted players:\n1-human V human\n2-human V com\n')
    while players not in ['1', '2']:  # input loop
        players = input(
            'Enter wanted players:\n1-human V human\n2-human V com\n')
    return players  # returns players indication


def display(grid):  # grid display
    for i in range(3):
        print(f'{" ".join(grid[i])}\n')


def invalid_input(grid):  # valid input loop
    display(grid)  # grid display
    inp = input('Invalid input, try again: ')
    return inp


def enter(grid, inp, p, player):  # incorporate input
    while inp not in grid[0] and inp not in grid[1] and inp not in grid[2]:  # valid input loop
        if player == '2' and p == 'O':
            inp = str(random.randint(1, 9))
        else:
            inp = invalid_input(grid)
    for i in range(3):  # check where to input
        for j in range(3):
            if inp == grid[i][j]:
                grid[i][j] = p  # enter player choice
    display(grid)  # grid display
    return grid  # returns updated grid


def status(grid):  # check if 1=win, 2=draw or 0=game continues
    strgrid = "".join(grid[0]) + "".join(grid[1]) + \
        "".join(grid[2])  # list to string
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]:
        return 1  # if win diagonally
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] or grid[0][i] == grid[1][i] == grid[2][i]:
            return 1  # if win horizontally or vertically
    if strgrid.isalpha():
        return 2  # if draw
    return 0  # if game con


def game1(player):  # the play
    p = 'O'  # player coice initial (to be switched)
    grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]  # the grid
    display(grid)  # display grid
    while player == '1' or player == '2':  # playing 2 humans or human V computer)
        p = 'X' if p == 'O' else 'O'  # switch X/O player
        if player == '1' or (player == '2' and p == 'X'):
            # player chooses a free space
            inp = input(f"Player {p} - PLAY! Coose an empty space: ")
        elif player == '2' and p == 'O':
            print('Computer plays O')
            inp = str(random.randint(1, 9))  # random computer coice
        grid = enter(grid, inp, p, player)  # incorporating player choice
        fin = status(grid)  # check if win, draw or continue
        if fin > 0:
            break  # exits if draw or win
    return p, grid, fin  # returns last player, updated grid, and game status


def ending(a1, a2, a3):  # final message
    if a2 == 2:
        print("It's a draw!")  # draw
    else:
        print(f'Player {a1} wins!')  # player wins
    display(a3)  # grid display
    inp = input('Another round? y/n: ')
    while inp != 'y' and inp != 'n':
        inp = input('Another round? y/n: ')  # another round question
    return inp


def main():  # main function
    while True:  # loop for another round
        player = players()  # who plays?
        winner, grid, fin = game1(player)  # gets winner/final grid/win or draw
        # final message and another round suggestion
        conti = ending(winner, fin, grid)
        if conti == 'n':
            break  # no more rounds


main()  # main function call
