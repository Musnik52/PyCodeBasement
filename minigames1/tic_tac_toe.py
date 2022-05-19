import random


class TicTacToe:

    def __init__(self):
        self.grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def players(players=""):  # Choose who are the players
        while players not in ['1', '2']:
            players = input(
                'Who plays?\n1-human V human\n2-human V computer\n')
        return players

    def display(self):  # grid display
        for i in range(3):
            print(f'{" ".join(self.grid[i])}\n')

    def enter(self, inp, p, player):  # incorporate input
        # valid input loop
        while inp not in self.grid[0] and inp not in self.grid[1] and inp not in self.grid[2]:
            if player == '2' and p == 'O':
                inp = str(random.randint(1, 9))
            else:
                self.display()  # grid display
                inp = input('Invalid input, try again: ')
        for i in range(3):  # check where to input
            for j in range(3):
                if inp == self.grid[i][j]:
                    self.grid[i][j] = p  # enter player choice
        self.display()  # grid display
        return self.grid  # returns updated grid

    def status(self):  # check if 1=win, 2=draw or 0=game continues
        strgrid = "".join(self.grid[0]) + "".join(self.grid[1]) + \
            "".join(self.grid[2])  # list to string
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] or self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return 1  # if win diagonally
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] or self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                return 1  # if win horizontally or vertically
        if strgrid.isalpha():
            return 2  # if draw
        return 0  # if game con

    def game1(self, player):  # the play
        p = 'O'  # player coice initial (to be switched)
        self.display()  # display grid
        while player == '1' or player == '2':  # playing 2 humans or human V computer)
            p = 'X' if p == 'O' else 'O'  # switch X/O player
            if player == '1' or (player == '2' and p == 'X'):
                # player chooses a free space
                inp = input(f"Player {p} - PLAY! Coose an empty space: ")
            elif player == '2' and p == 'O':
                print('Computer plays O')
                inp = str(random.randint(1, 9))  # random computer coice
            # incorporating player choice
            self.grid = self.enter(inp, p, player)
            fin = self.status()  # check if win, draw or continue
            if fin > 0:
                break  # exits if draw or win
        return p, self.grid, fin  # returns last player, updated grid, and game status

    def ending(self, a1, a2):  # final message
        if a2 == 2:
            print("It's a draw!")  # draw
        else:
            print(f'Player {a1} wins!')  # player wins
        self.display()  # grid display
        inp = input('Another round? y/n: ')
        while inp != 'y' and inp != 'n':
            inp = input('Another round? y/n: ')  # another round question
        return inp

    def play(self):  # main function
        while True:  # loop for another round
            player = self.players()  # who plays?
            # gets winner/final grid/win or draw
            winner, self.grid, fin = self.game1(player)
            # final message and another round suggestion
            conti = self.ending(winner, fin)
            if conti == 'y':
                self.grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
                continue
            else:
                break
