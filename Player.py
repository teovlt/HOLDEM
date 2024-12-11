class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.is_active = True

    def bet(self, amount):
        if amount > self.chips:
            return False
        self.chips -= amount
        return True

    def fold(self):
        self.is_active = False

    def receive_card(self, card):
        if len(self.hand) < 2:
            self.hand.append(card)
