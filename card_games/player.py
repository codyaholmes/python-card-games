import uuid

class Player:
    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()
        self.hand = []
        self.score = 0

    def __str__(self) -> str:
        return f'{self.name[:2]} (ID {str(self.id)[:3]})'
    
    def __repr__(self) -> str:
        return f'{self.name[:2]} (ID {str(self.id)[:3]})'
        # return f'Player(name={self.name}, id={str(self.id.int)}...)'
    
    @property
    def hand_count(self) -> int:
        hand_count = len(self.hand)
        return hand_count
    
    def take_card(self, card: str) -> None:
        self.hand.append(card)

    def take_cards(self, cards: list) -> None:
        self.hand.extend(cards)

    def play_card(self) -> str:
        if self.hand_count == 0:
            print(f'{self.name} has no cards to play!')
        else:
            card_played = self.hand.pop(0)
            return card_played

    def play_cards(self, qty: list) -> list:
        if len(self.hand) == 0:
            print(f'{self.name} has no cards to play!')
        elif len(self.hand) < qty:
            print(f'{self.name} cannot play more cards than they have!')
        else:
            cards_played: list = [self.hand.pop(0) for i in range(qty)]
            return cards_played
