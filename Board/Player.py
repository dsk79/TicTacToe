import random
from random import randint


class Player:
    def __init__(self, symbol, amount):
        self.balance = amount
        self.symbol = symbol
        self.current_bid = 0

        if symbol == 'x':
            self.label = 'Player 1'
        else:
            self.label = 'Player 2'

    def request_bid(self):
        bid = self.generate_bid()
        self.current_bid = bid
        return bid

    def request_move(self, game):
        x, y = self.generate_move(game)
        return x, y

    def generate_bid(self):
        bid = randint(0, self.balance)
        print("(player)", self.label, "Generating bid of ", bid, "current balance:", self.balance)
        return bid

    def generate_move(self, game):
        self.balance -= self.current_bid

        move = random.choice(game.valid_moves)
        #print(game.valid_moves, move)
        x = move // game.rows
        y = move % game.rows

        print("(player)", self.label, "is generating move of row", x, "col", y, "Remaining balanace is", self.balance)
        return x, y

