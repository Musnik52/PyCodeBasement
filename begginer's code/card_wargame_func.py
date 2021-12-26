import random
import time

def print_card(card):
    if card <=10: print(card)
    elif card == 11:
        print('J')
    elif card == 12:
        print('Q')
    elif card == 13:
        print('K')
    else: # card1 == 14:
        print('A')

my_score = 0
computer_score = 0
while my_score < 5 and computer_score <5:
    u_card = random.randint(2,14)
    c_card = random.randint(2,14)
    print('User card: ', end="")
    print_card(u_card)
    time.sleep(1)
    print('Computer card: ', end="")
    print_card(c_card)
    time.sleep(1)
    if c_card < u_card:
        print("User wins")
        my_score += 1
    elif c_card > u_card:
        print ("Computer wins")
        computer_score += 1
    else: print("it's a draw")
print("-"*50)
if my_score == 5: print("User wins")
else: print("Computer wins")
print("-"*50)