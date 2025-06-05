from deck import Deck
from collections import Counter
from pprint import pprint

class War:
    def __init__(self, deck: Deck, players: list) -> None:
        self.deck = deck
        self.battle_cards = []
        self.players = players
        self.battle_round = 1
        # Holds the cards being battled or moved to the war pool
        self.battle_pool = {}
        self.war_pool = []
        self.war_players = []
        # Holds leftover cards when deck not evenly divisible by player count
        self.leftovers = []
        self.war_start = False

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

        def regular_battle(self, war_start):
            print(f'BATTLE ROUND {self.battle_round} ********')
            print()

            # Set the players, depending on if game is in a war iteration
            if war_start:
                players = self.war_players
            else:
                players = self.players

            for player in players:
                if player.hand_count == 0:
                    print(f'>> {player.name} has no more troops and has been eliminated')

                else:
                    played_card = player.play_card()
                    self.battle_cards.append(played_card)

                    print(f'>> {player.name} played {played_card}')

                    # Build the battle pool
                    self.battle_pool[played_card] = {
                        'player': player,
                        'card_value': self.deck.card_value(played_card)
                    }

                    # TESTING: SHOW THE BATTLE POOL
                    pprint(self.battle_pool)
                    print()

                # Determine winner
                battle_card_values = [v['card_value'] for v in self.battle_pool.values()]
                battle_card_counter = Counter(battle_card_values)
                max_card_value = max(battle_card_counter.keys())
                winning_cards = [card for card in self.battle_cards if self.deck.card_value(card) == max_card_value]
                winners = [self.battle_pool[card]['player'] for card in winning_cards]
                winner_count = len(winners)

                # TESTING
                print('## Battle card counter:', battle_card_counter)
                print('## Max card value:', max_card_value)
                print('## Winning card(s):', winning_cards)
                print('## Winners:', winners)
                print('## Winner count:', winner_count)
                print()

                # If winner is clear, assign the spoils and reset internals
                if winner_count == 1:
                    winner = winners[0]
                    winner.take_cards(self.battle_cards)

                    print(f'{winner} has taken the battle spoils:')
                    print(self.battle_pool)
                    print()

                    if self.war_pool:
                        winner.take_cards(self.war_pool)

                        print(f'{winner} has taken the war spoils:')
                        print(self.war_pool)
                        print()

                    # Reset internal game data and iterate round
                    self.battle_pool = {}
                    self.battle_cards = []
                    self.war_pool = []
                    self.war_players = []
                    self.war_start = False
                    self.battle_round += 1

                # If multiple winners, prep internals for war
                else:
                    print('>> WAR HAS BEEN DECLARED!')
                    print()

                    # Add all winners to the war players list
                    self.war_players.extend(winners)

                    # Check to ensure war players have enough troops for war
                    for player in self.war_players:
                        hand_count = player.hand_count
                        if hand_count <= 3:
                            self.war_players.remove(player)
                            self.players.remove(player)
                            self.war_pool.extend(player.play_cards(hand_count))
                            print(f'>> {player.name} does not have enough troops for war and has been eliminated!')
                            print()

                    # Check to ensure there are still enough players for war
                    if len(self.war_players) == 1:
                        ...

        regular_battle(self, self.war_start)