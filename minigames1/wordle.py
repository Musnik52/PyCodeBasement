from random import choice
from rich import print

with open('minigames1\words.txt') as f:
    words = list(f.read().split())


class Wordle:

    def __init__(self):
        self.word = choice(words)
        self.guesses = 0
        self.guess_dict = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
            5: [" "]*5}

    def board(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("="*17)

    def user_input(self):
        user_guess = input('Try to guess the 5-letter word: ').lower()
        while len(user_guess) != 5:
            user_guess = input('FIVE - V - 5-letter word, please: ').lower()
        for i, c in enumerate(user_guess):
            if c in self.word:
                c = f'[green]{c}[/]' if c == self.word[i] else f'[yellow]{c}[/]'
            self.guess_dict[self.guesses][i] = c
        self.guesses += 1
        return user_guess

    def play(self):
        while True:
            self.board()
            user_guess = self.user_input()
            if user_guess == self.word:
                self.board()
                print(f'You are correct! the word is indeed {self.word}.')
                break
            if self.guesses > 5:
                self.board()
                print(f'You lose! the word was {self.word}.')
                break
