
class ConnectFour:

    def __init__(self, height=6, width=7):
        self.height = height
        self.width = width
        self.board = [[' ']*width for row in range(height)]

    def draw_board(self):
        print([str(i+1) for i in range(self.width)], end="\n\n")
        for row in self.board:
            print(row)

    def column(self, i):
        return[row[i] for row in self.board]

    def row(self, i):
        return self.board[i]

    def diagonal(self):
        diagonals = []
        for i in range(self.height + self.width - 1):
            diag1, diag2 = [], []
            for j in range(max(i - self.height + 1, 0), min(i + 1, self.height)):
                diag1.append(self.board[self.height - i + j - 1][j])
                diag2.append(self.board[i - j][j])
            diagonals.append(diag1)
            diagonals.append(diag2)
        return diagonals

    def token_insert(self, player, column):
        if " " not in self.column(column):
            return False
        row = self.height - 1
        while self.board[row][column] != " ":
            row -= 1
        self.board[row][column] = player
        return True

    def winner_check(self):
        four_row = (["0", "0", "0", "0"], ["1", "1", "1", "1"])
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.row(row)[col: col + 4] in four_row:
                    return True
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.column(col)[row: row + 4] in four_row:
                    return True
        for diag in self.diagonal():
            for i, _ in enumerate(diag):
                if diag[i:i + 4] in four_row:
                    return True
        return False

    def play(self):
        player = '0'
        while True:
            self.draw_board()
            ok = False
            while not ok or col > 7:
                col = int(input(f'Player {player} - Choose now: ')) - 1
                ok = self.token_insert(player, col)
            if self.winner_check():
                self.draw_board()
                print(f'Player {player} WINS!')
                break
            player = '1' if player == '0' else '0'
