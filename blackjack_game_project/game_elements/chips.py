class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

    def __str__(self):
        return f'The total is: {self.total}'
