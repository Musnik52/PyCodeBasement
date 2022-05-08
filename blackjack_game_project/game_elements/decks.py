import random
from game_elements.cards import Cards


class Decks:

    def __init__(self):
        self.cards = []
        #creating a 52 card standart deck
        for suit in Cards.suits:
            for rank in Cards.ranks:
                created_card = Cards(suit, rank)
                self.cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        deck = ''
        for card in self.cards:
            deck += f'\n{str(card)}' 
        return f'The deck has: {deck}'
