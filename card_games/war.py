from deck import Deck
from collections import Counter

class War:
    def __init__(self, deck: Deck, players: list) -> None:
        self.deck = deck
        self.battle_cards = []
        self.war_cards = []
        self.players = players
        self.battle_round = 1
        # Holds the cards being battled or moved to the war pool
        self.battle_pool = {}
        self.war_pool = []
        # Holds leftover cards when deck not evenly divisible by player count
        self.leftovers = []

    def build_hands(self) -> None:
        # Shuffle the deck if not already shuffled
        self.deck.shuffle()

        card_count = self.deck.deck_count
        player_count = len(self.players)
        leftover_count = card_count % player_count
        self.leftovers.append(self.deck.deal_cards(leftover_count))
        hand_deal_count = card_count // player_count

        for player in self.players:
            player.take_cards(self.deck.deal_cards(hand_deal_count))

    @property
    def player_count(self) -> int:
        player_count = len(self.players)
        return player_count

    def battle(self) -> int:

        # Check to see if player has no cards. If so, remove them.
        for player in self.players:
            if player.hand_count == 0:
                self.players.remove(player)
                print(f'>> {player} has been destroyed. 😭')

        # Build the battle pool
        for player in self.players:
            played_card = player.play_card()
            self.battle_pool[played_card] = player
            print(f'>> {player} played {played_card}')

        print()

        # Award cards or declare a war
        battle_cards = self.battle_pool.keys()
        battle_values = [self.deck.card_value(card) for card in battle_cards]
        winning_cards_counter = Counter(battle_values)
        winning_card_value = max(winning_cards_counter.keys())

        # print(self.battle_pool)
        # print(winning_cards_counter)
        # for player in self.players:
        #     print(f'{player} has {player.hand_count} cards left.')
        # print()

        # Check if war needs to be declared or give winning player spoils
        if winning_cards_counter[winning_card_value] > 1:
            print('>> WAR HAS BEEN DECLARED! 💥')
            print()
            self.war_pool.extend(battle_cards)

            # Check to see if players have enough for war.
            # If not, add their cards to the war pool and remove them.
            for player in self.players:
                hand_count = player.hand_count
                if hand_count < 3:
                    self.war_pool.extend(player.play_cards(hand_count))
                    self.players.remove(player)
                    print(f'>> {player} did not have enough troops for war and has been eliminated. 😭')

                else:
                    self.war_pool.extend(player.play_cards(3))
                    self.battle_round += 1

        else:
            winning_card = [card for card in battle_cards if self.deck.card_value(card) == winning_card_value][0]
            winning_player = self.battle_pool[winning_card]
            winning_player.take_cards(battle_cards)
            self.battle_pool = {} # Reset battle pool

            print(f'>> {winning_player} won the battle with {winning_card}.')
            print()

            # Give the winning player the war pool after war iterations
            if self.war_pool:
                winning_player.take_cards(self.war_pool)
                self.war_pool = [] # Reset war pool
    
            self.battle_round += 1

        for player in self.players:
            print(f'>> {player} has {player.hand_count} cards left.')
        
        print()
        print(f'Round {self.battle_round} ********')
            