class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        return f"Card(rank={self.rank}, suit={self.suit})"
