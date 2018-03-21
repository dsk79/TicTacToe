class Player:
    def __init__(self, symbol, amount):
        self.money = amount
        self.symbol = symbol

        if symbol == 'x':
            self.label = 'Player 1'
        else:
            self.label = 'Player 2'

    def bid(self, amount):
        self.money -= amount
