import random
import Card


class Deck:
    def __init__(self):
        suits = ['Cœur', 'Pique', 'Carreau', 'Trèfle']
        ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.cards = [Card for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n):
        drawn_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return drawn_cards
