from random import randint


class Player:
    def __init__(self, symbol, amount):
        self.balance = amount
        self.symbol = symbol

        if symbol == 'x':
            self.label = 'Player 1'
        else:
            self.label = 'Player 2'

    def request_bid(self):
        bid = self.generate_bid()
        return bid

    def request_move(self, game):
        x, y = self.generate_move(game)
        return x, y

    def generate_bid(self):
        bid = randint(0, self.balance)
        self.balance -= bid
        print(self.label, "Generating bid of ", bid)
        return bid

    def generate_move(self, game):
#        print(game.board)

        # More intelligent way will be to see which spaces are available and pick from only those spaces.
        # Picking blindly and hoping for a space may lead to long run times in very big, nearly filled matrices

        valid = False
        while not valid:
            x = randint(0, game.rows - 1)
            y = randint(0, game.cols - 1)
            if game.board[x][y] is None:
                valid = True

        print("Generating move of ", x, y)
        return x, y

