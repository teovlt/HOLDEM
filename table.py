from deck import Deck
from treys import Evaluator


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

    def run_betting_round(self):

        # TODO: Implémenter la logique de paris
        pass

    def has_best_hand(self):
        evaluator = Evaluator()
        evaluations = []

        for player in self.players:
            if player.is_active:
                evaluation_score = evaluator.evaluate(self.community_cards, player.hand)
                evaluations.append({"player": player, "evaluation": evaluation_score})

        if not evaluations:
            return []

        max_score = max(evaluations, key=lambda x: x["evaluation"])["evaluation"]

        # Trouver tous les joueurs ayant le score maximum
        best_players = [entry["player"] for entry in evaluations if entry["evaluation"] == max_score]
        return best_players

    def is_game_over(self):
        return len([p for p in self.players if p.chips > 0]) <= 1

    def remove_bankrupt_players(self):
        self.players = [p for p in self.players if p.chips > 0]
