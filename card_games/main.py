from deck import Deck
from player import Player
from war import War


def main():
    # Make deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Add players
    player_count = int(input('How many players? '))
    
    players = []
    for i in range(player_count):
        player_name = input(f"Enter player {i+1}'s name: ")
        player = Player(player_name)
        players.append(player)

    print()

    # Build war game
    war = War(deck, players)
    war.build_hands()

    print(f'Round 1 ********')

    while True:
        war.battle()

        # Check for winner
        if war.player_count == 1:
            winning_player = war.players[0]
            total_rounds = war.battle_round
            print(f'{winning_player} has won the war after {total_rounds} battles! 🏆')
            break

        response = input("Play another round? (y/n) ").lower()
        if response == 'y':
            continue
        else:
            break

if __name__ == '__main__':
    main()