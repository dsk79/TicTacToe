import random
from random import randint


class Player:
    def __init__(self, symbol, amount):
        self.balance = amount
        self.symbol = symbol
        self.current_bid = 0

        if symbol == 'x':
            self.label = 'Player 1'
            self.opponent = 'o'
        else:
            self.label = 'Player 2'
            self.opponent = 'x'

    def request_bid(self, game):
        bid = self.generate_bid(game)
        self.current_bid = bid
        return bid

    def request_move(self, game):
        x, y = self.generate_move(game)
        return x, y

    # adjust bid to max of opponent's balance, transfer money to opponent's balance
    def generate_bid(self, game):
        # bid no more than 1 than opponent's balance
        opponent = game.players[self.opponent]
        opponent_balance = opponent.balance

        bid = randint(0, self.balance)
        if self.balance > bid >= opponent_balance:
            bid = opponent_balance + 1

        print("(player)", self.label, "Generating bid of ", bid, "current balance:", self.balance)
        return bid

    '''Bid has been accepted.  Game engine requests move based on available spots'''
    def generate_move(self, game):
        # Subtract bid from your balance and transfer your bid to opponent's balance
        self.balance -= self.current_bid
        game.players[self.opponent].balance += self.current_bid
        self.current_bid = 0

        move = random.choice(game.valid_moves)
        #print(game.valid_moves, move)
        x = move // game.rows
        y = move % game.rows

        print("(player)", self.label, "is generating move of row", x, "col", y, "Remaining balance is", self.balance)
        return x, y

