from deck import Deck
from collections import Counter

class War:
    def __init__(self, deck: Deck, *players):
        self.deck = deck
        self.battle_cards = []
        self.war_cards = []
        self.players = players

        # Holds leftover cards when deck not evenly divisible by player count
        self.leftovers = []

    def build_hands(self):
        # Shuffle the deck if not already shuffled
        self.deck.shuffle()

        card_count = self.deck.deck_count
        player_count = len(self.players)
        leftover_count = card_count % player_count
        self.leftovers.append(self.deck.deal_cards(leftover_count))
        hand_deal_count = card_count // player_count

        for player in self.players:
            player.take_cards(self.deck.deal_cards(hand_deal_count))

    def battle(self):
        # Holds the cards being battled
        battle_pool = {}
        war_pool = []
        tied_players = []

        # Build the battle pool
        for player in self.players:
            played_card = player.play_card()

            if player.hand_count == 0:
                self.players.remove(player)
                print(f'{player} has been destroyed.')
            else:
                battle_pool[played_card] = player
                print(f'{player} played [ {played_card} ]')

        # Award cards or declare a war
        battle_cards = battle_pool.keys()
        battle_values = [self.deck.card_value(card) for card in battle_cards]
        winning_cards_counter = Counter(battle_values)
        winning_card_value = max(winning_cards_counter.keys())

        print(battle_pool)
        print(winning_cards_counter)
        print(winning_card_value)

        if winning_cards_counter[winning_card_value] > 1:
            print('WAR HAS BEEN DECLARED!')
        else:
            battle_pool = {}
            print('Award card here.')
    