from rock_paper_scissors import rockpaperscissors
from guess_the_number import guess_number
from wordle import Wordle
from connect_four import ConnectFour
from tic_tac_toe import TicTacToe

while True:
    choice = input('''
    Welcome to Boris' Gamer-Emporium.
    Please select a game to play:
    ~===========================~
    | 1) Guess The Number!      |
    | 2) Rock, Paper, Scissors! |
    | 3) Wordle!                |
    | 4) Connect Four!          |
    | 5) Tic-Tac-Toe!           |
    |                           |
    | *) Insert any other       |
    |    input to quit.         |
    ~===========================~
    Your choice is: ''')
    if choice == '1':
        guess_number()
    elif choice == '2':
        rockpaperscissors()
    elif choice == '3':
        Wordle().play()
    elif choice == '4':
        ConnectFour().play()
    elif choice == '5':
        TicTacToe().play()
    else:
        print('Goodbye!')
        break
