import random
from random import randint


class Player:
    def __init__(self, symbol, amount):
        self.balance = amount
        self.symbol = symbol

        if symbol == 'x':
            self.label = 'Player 1'
            self.opponent = 'o'
        else:
            self.label = 'Player 2'
            self.opponent = 'x'

    ''' Game engine requesting a bid '''
    def request_bid(self, game):
        bid = self.generate_bid(game)
        return bid

    ''' Game engine requesting a move '''
    def request_move(self, game):
        x, y = self.generate_move(game)
        return x, y

    ''' Create a bid.  Learning function will be used here instead in future '''
    def generate_bid(self, game):
        # bid no more than 1 than opponent's balance
        opponent = game.players[self.opponent]
        opponent_balance = opponent.balance

        # Careful not to bid more than current balance (when current bid is equal to balance)
        bid = randint(0, self.balance)
        if self.balance > bid >= opponent_balance:
            bid = opponent_balance + 1

        print("(player)", self.label, "Generating bid of ", bid, "\tcurrent balance:", self.balance,
              "\tOpponent Balance:", opponent_balance)
        return bid

    ''' Bid has been accepted.  Game engine requests move based on available spots '''
    ''' Learning algorithm will be used here instead in the future '''
    def generate_move(self, game):
        move = random.choice(game.valid_moves)
        #print(game.valid_moves, move)
        x = move // game.rows
        y = move % game.rows

        print("(player)", self.label, "is generating move of row", x, "col", y, "Remaining balance is", self.balance)
        return x, y

    ''' Instructions from the game engine to update balance '''
    def update_balance(self, self_bid, opponent_bid):
        self.balance -= self_bid
        self.balance += opponent_bid
