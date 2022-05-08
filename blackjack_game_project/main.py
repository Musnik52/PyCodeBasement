from game_elements.decks import Decks
from game_elements.hands import Hands
from game_elements.chips import Chips


def make_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips you wanna bet? '))
        except:
            print('PLEASE PROVIDE A VALID INTEGER!')
        else:
            if chips.bet > chips.total:
                print('PLEASE PROVIDE A VALID CHIP-AMMOUNT THAT YOU HAVE!')
            else:
                break


def hit_me(deck, hand):
    hand.add(deck.deal())
    hand.ace_play()


def hit_stand(hand, deck, playing=True):
    while playing:
        decision = input('(h)hit or (s)stand? ')
        if decision[0].lower() == 'h':
            hit_me(deck, hand)
        elif decision[0].lower() == 's':
            print('Player stands.')
            playing = False
        else:
            print('invalid input - enter H or S')
            continue
        break
    return False

def show_part(player, dealer):
    # shows 1 card of the dealer's hand
    print(f"\nDealer's hand: {dealer.cards[1]} + HIDDEN")
    # shows the player's hand
    print(f"\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print(f'Value: {player.value}')


def show_all(player, dealer):
    # dealer's hand + value
    print(f"\nDealer's hand:", *dealer.cards, sep="\n")
    print(f'Value: {dealer.value}')
    # player's hand + value
    print(f"\nPlayer's hand:", *player.cards, sep="\n")
    print(f'Value: {player.value}')


def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win()


def player_loses(player, dealer, chips):
    print('Dealer wins! - Player over 21')
    chips.lose()


def dealer_wins(player, dealer, chips):
    print('Player loses!')
    chips.lose()


def dealer_loses(player, dealer, chips):
    print('Player wins! - Dealer over 21')
    chips.win()


def tie(player, dealer):
    print('Dealer & Player are both 21 - TIE!')


def main():

    player_chips = Chips()
    while True:
        print('Welcome to BLACK-21-JACK!')
        dealer_hand = Hands()
        player_hand = Hands()
        deck = Decks()
        deck.shuffle()
        for i in range(2):
            player_hand.add(deck.deal())
            dealer_hand.add(deck.deal())
        make_bet(player_chips)
        show_part(player_hand, dealer_hand)
        playing = True
        while playing:
            playing = hit_stand(player_hand, deck)
            show_part(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_loses(player_hand, dealer_hand, player_chips)
                break
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:  # or dealer_hand.value < 17
                hit_me(deck, dealer_hand)
            show_all(player_hand, dealer_hand)
            if dealer_hand.value > 21:
                dealer_loses(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                tie(player_hand, dealer_hand)
        print(f"\nPlayers's grand total is: {player_chips.total}")
        new_game = input("Wanna play again? y/n ")
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('BYE BYE!')
            break


main()
