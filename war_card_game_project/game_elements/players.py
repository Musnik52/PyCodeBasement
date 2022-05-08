class Players:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def add(self, new_cards):  # adding winnings to the deck
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def remove(self):  # removing a card to play with
        return self.cards.pop(0)

    def __str__(self):
        return f'Player - {self.name} has {len(self.cards)} cards.'
