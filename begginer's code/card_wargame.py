import random
my_score = 0
computer_score = 0
for i in range(3):
    # i draw a card
    card1 = random.randint(2, 14)
    print("User draws: ", end="")
    if card1 <= 10:
        print(card1)
    elif card1 == 11:
        print('J')
    elif card1 == 12:
        print('Q')
    elif card1 == 13:
        print('K')
    else: # card1 == 14:
        print('A')
    card2 = random.randint(2, 14)
    print("Computer draws: ", end="")
    if card2 <= 10:
        print(card2)
    elif card2 == 11:
        print('J')
    elif card2 == 12:
        print('Q')
    elif card1 == 13:
        print('K')
    else: # card1 == 14:
        print('A')
    if card1 < card2:
        print (f"Computer wins round {i+1}")
        computer_score += 1
    elif card1 > card2:
        print (f"User wins round {i+1}")
        my_score += 1
    else: print(f"Round {i+1} is a draw.")
print("="*50)
if my_score < computer_score: print("Computer wins!")
elif my_score > computer_score: print("User wins!")
else: print("It's a draw")
print("="*50)