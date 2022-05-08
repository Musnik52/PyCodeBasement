from game_elements.cards import Cards


class Hands:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add(self, new_card):
        self.cards.append(new_card)
        self.value += Cards.val_dict[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1

    def ace_play(self):
        while self.value > 21 and self.aces > 0:  # change ace from 11 to 1
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return f'The hand has {self.value}.'
