from game_elements.decks import Decks
from game_elements.players import Players


def main():
    # setting the player's card-decks
    player_one = Players('Boris')
    player_two = Players('Emil')
    game_deck = Decks()
    game_deck.shuffle()
    for i in range(26):
        player_one.add(game_deck.deal())
        player_two.add(game_deck.deal())
    game_flow = True
    war_round = 0
    while game_flow:
        # preventing infinite loop
        war_round += 1
        if war_round > 10000:
            print('TIE!')
            war_flow = False
            break
        war_flow = True
        print(f'Round {war_round} - FIGHT!')
        if len(player_one.cards) == 0:  # P1 loses/ P2 wins
            print(f'{player_one.name} loses - {player_two.name} wins!')
            game_flow = False
            break
        if len(player_two.cards) == 0:  # P1 wins/ P2 loses
            print(f'{player_two.name} loses - {player_one.name} wins!')
            game_flow = False
            break
        player_one_deck = []
        player_one_deck.append(player_one.remove())
        player_two_deck = []
        player_two_deck.append(player_two.remove())
        while war_flow:
            if player_one_deck[-1].value < player_two_deck[-1].value:  # P1 loses/ P2 wins
                print(
                    f'{player_one.name}: {player_one_deck[-1]}\n{player_two.name}: {player_two_deck[-1]}\n{player_two.name} wins this round.')
                player_two.add(player_one_deck)
                player_two.add(player_two_deck)
                war_flow = False
                break
            elif player_one_deck[-1].value > player_two_deck[-1].value:  # P1 wins/ P2 loses
                print(
                    f'{player_one.name}: {player_one_deck[-1]}\n{player_two.name}: {player_two_deck[-1]}\n{player_one.name} wins this round.')
                player_one.add(player_one_deck)
                player_one.add(player_two_deck)
                war_flow = False
                break
            else:
                print(
                    f'{player_one.name}: {player_one_deck[-1]}\n{player_two.name}: {player_two_deck[-1]}\nWAR! HUH! YEAH...WHAT IS IT GOOD FOR?')
                if len(player_one.cards) < 5:
                    print(  # P1 loses/ P2 wins
                        f'{player_one.name} cannot declare war! {player_two.name} wins!')
                    game_flow = False
                    break
                elif len(player_two.cards) < 5:
                    print(  # P1 wins/ P2 loses
                        f'{player_two.name} cannot declare war! {player_one.name} wins!')
                    game_flow = False
                    break
                else:
                    for i in range(5):
                        player_one_deck.append(player_one.remove())
                        player_two_deck.append(player_two.remove())


if __name__ == "__main__":
    main()
