from deck import Deck
from player import Player
from war import War

from pprint import pprint


def main():
    # Make deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Add players
    cody = Player('Cody')
    yasmin = Player('Yasmin')
    izaiah = Player('Izaiah')

    # Build war game
    war = War(deck, cody, yasmin, izaiah)
    war.build_hands()

    # for player in war.players:
    #     print(player.name, player.hand)
    #     print(player.hand_count)

    war.battle()

if __name__ == '__main__':
    main()