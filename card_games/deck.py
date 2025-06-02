from random import shuffle

class Deck:
    def __init__(self):
        self.suits = ['s', 'c', 'h', 'd']
        self._court_str = ['J', 'Q', 'K', 'A']
        self._court_val = [i for i in range(11, 15)]
        self._nums_str = [str(n) for n in range(2, 11)]
        self._nums_val = [i for i in range(2, 11)]
        self._court_map = {f'{c}{s}':v for s in self.suits for c,v in zip(self._court_str, self._court_val)}
        self._nums_map = {f'{n}{s}':v for s in self.suits for n,v in zip(self._nums_str, self._nums_val)}
        self.value_map = {}
        self.value_map.update(self._court_map)
        self.value_map.update(self._nums_map)
        self.cards = list(self.value_map.keys())

    @property
    def deck_count(self) -> int:
        deck_count = len(self.cards)
        return deck_count
    
    def shuffle(self) -> None:
        shuffle(self.cards)

    def deal_card(self) -> str:
        if self.deck_count == 0:
            print('There are no more cards in the deck to deal.')
        else:
            card = self.cards.pop()
            return card
    
    def deal_cards(self, qty: str) -> list:
        if qty > self.deck_count:
            print('You cannot deal more cards than what is in the deck!')
        else:
            cards = [self.cards.pop() for i in range(qty)]
            return cards
        
    def card_value(self, card: str) -> int:
        card_value = self.value_map.get(card, "Card doesn't exist.")
        return card_value