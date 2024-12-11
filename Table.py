from Deck import Deck
from treys import Evaluator


class Table:
    def __init__(self):
        self.community_cards = []
        self.pot = 0
        self.players = []
        self.deck = Deck()

    def add_community_cards(self, cards):
        self.community_cards.extend(cards)

    def collect_bets(self):
        #TODO
        pass

    def deal_to_players(self):
        for player in self.players:
            if player.is_active:
                player.receive_card(self.deck.draw(1)[0])
                player.receive_card(self.deck.draw(1)[0])

    def determine_winner(self):
        #TODO
        pass

