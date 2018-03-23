import numpy as np


class Board:
    def __init__(self, length):
        self.rows = length
        self.cols = length
        self.board = self.create_board()
        self.turn = 0
        self.valid_moves = list(range(0, self.rows * self.cols))

    def create_board(self):
        # N x N board (always square, any size)
        return np.full((self.rows, self.cols), fill_value=None)

    ''' Set a player's mark on the coordinates '''
    def mark(self, x, y, symbol):
        if x >= self.rows or x < 0 or y >= self.cols or y < 0:
            print('Coordinates are out of range', x, y)
            return False

        if self.board[x][y] is not None:
            print("Coordinates is already marked ", self.board[x][y], x, y)
            return False

        assert isinstance(symbol, str)
        self.board[x][y] = symbol
        self.turn += 1
        self.valid_moves.remove((self.rows * x) + y)
        return self.board

    ''' Check for winning state with N connected marks along any row, col, or diagonal'''
    def check_state(self):
        is_draw = True
        # check all columns
        for i in range(0, self.cols):
            # Check if a none exists in any column, that is sufficient to very a completed board or not
            if None in self.board[:, i]:
                #print("Found a none in col: ", i)
                is_draw = False

            symbol = self.board[0][i]
            if symbol is None:
                continue

            if np.all(symbol == self.board[:, i]):
                return True, symbol

        # check all rows
        for i in range(0, self.rows):
            symbol = self.board[i][0]
            if symbol is None:
                continue

            if np.all(symbol == self.board[i, :]):
                return True, symbol


        # TODO: CLEAN UP THE DIAGONALS CHECKS
        # check both diagonals
        winning_state = True
        symbol = self.board[0][0]
        if symbol is not None:
            for i in range(0, self.rows):
                if symbol != self.board[i][i]:
                    winning_state = False
                    break
        else:
            winning_state = False

        if winning_state:
            return True, symbol

        winning_state = True
        symbol = self.board[self.rows-1][0]
        if symbol is not None:
            for i in range(0, self.rows):
                if symbol != self.board[i][self.rows-1 - i]:
             #       print("Found a None on reverse diagonal at ", i, self.rows-1-i)
                    winning_state = False
                    break
        else:
            winning_state = False

        if winning_state:
            #print("Found a match on reverse diagonal symbol ", symbol, i)
            return True, symbol

        if is_draw:
            print("Declaring a draw")
            return True, -1

        # No winning state found on all rows, cols, diagonals
        return False, -1
