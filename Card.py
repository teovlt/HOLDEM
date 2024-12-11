class Card:
    def __init__(self, rank, suit):
        self.rank = rank  # Exemple: "As", "10", "Roi"
        self.suit = suit  # Exemple: "Cœur", "Carreau", "Trèfle", "Pique"

    def __str__(self):
        return f"{self.rank} de {self.suit}"
