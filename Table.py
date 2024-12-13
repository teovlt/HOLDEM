from Deck import Deck


class Table:
    def __init__(self):
        self.community_cards = []
        self.pot = 0
        self.players = []
        self.deck = Deck()

    def add_community_cards(self, cards):
        self.community_cards.extend(cards)

    def deal_to_players(self):
        for player in self.players:
            if player.is_active:
                player.receive_card(self.deck.draw(2))

    def determine_winner(self):
        # TODO: Implémenter la logique de détermination du gagnant
        pass

    """
    Vérifie si la partie est terminée :
    - Si un seul joueur a des jetons restants.
    Retourne True si la partie est terminée, sinon False.
    """
    def GameIsOver(self):
        remaining_players = [player for player in self.players if player.chips > 0]
        if len(remaining_players) == 1:
            return True
        return False
