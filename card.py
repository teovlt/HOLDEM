class Card:
    def __init__(self, rank, suit):
        self.rank = rank  # Par exemple, "As", "10", "Roi"
        self.suit = suit  # Par exemple, "Cœur", "Pique", "Trèfle", "Carreau"

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        return self.__str__()
