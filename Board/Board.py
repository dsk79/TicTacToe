import math
import numpy as np
import pandas as pd


class Board:
    def __init__(self, length):
        self.rows = length
        self.cols = length
        self.board = self.create_board()
        self.turn = 0

    def create_board(self):
        # N x N board (always square, any size)
        print('Hello world again')
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
        return self.board

    ''' Check for winning state with N connected marks along any row, col, or diagonal'''
    def check_state(self):
        is_draw = True
        # check all columns
        for i in range(0, self.cols):
            # Check if a none exists in any column, that is sufficient to very a completed board or not
            if None in self.board[:, i]:
                print("Found a none in col: ", i)
                is_draw = False

            symbol = self.board[0][i]
            if symbol is None:
#                print("Found a none on column check, continuing")
                continue

            if np.all(symbol == self.board[:, i]):
#                print("match found on col: ", i, self.board[:, i])
                return True, symbol

        # check all rows
        for i in range(0, self.rows):
            symbol = self.board[i][0]
            if symbol is None:
 #               print("Found a none on row check, continuing")
                continue

            if np.all(symbol == self.board[i, :]):
  #              print("match found on row: ", i, self.board[i, :])
                return True, symbol


        # TODO: CLEAN UP THE DIAGONALS CHECKS

        # check both diagonals
        winning_state = True
        symbol = self.board[0][0]
        if symbol is not None:
            for i in range(0, self.rows):
                if symbol != self.board[i][i]:
                    print("Found mismatch along diagonal at ", i, i)
                    winning_state = False
                    break
        else:
            winning_state = False
            # print("Found a None on diagonal check, breaking")

        if winning_state:
            print("Found a match on diagonal symbol ", symbol, i)
            return True, symbol

        winning_state = True
        symbol = self.board[self.rows-1][0]
        if symbol is not None:
            for i in range(0, self.rows):
                if symbol != self.board[i][self.rows-1 - i]:
                    print("Found a None on reverse diagonal at ", i, self.rows-1-i)
                    winning_state = False
                    break
        else:
            winning_state = False

 #           print("Found a None on reverse diagonal check, breaking")

        if winning_state:
            print("Found a match on reverse diagonal symbol ", symbol, i)
            return True, symbol

        if is_draw:
            print("Declaring a draw")
            return True, -1

        # No winning state found on all rows, cols, diagonals
        return False, -1

    def sqrt(num, precision):
        low = 0.0
        high = num
        guess = num

        delta = math.pow(0.1, precision)
        print(delta)

        for i in range(0, precision * 5):
            print(math.fabs(num - guess * guess), delta)
            guess = (high + low) / 2

            if math.pow(guess, 2) == num:
                print('returning exact match')
                return guess

            if math.pow(guess, 2) < num:
                high = high
                low = guess
                print('too low . making larger', high, low, guess)
            else:
                high = guess
                low = low
                print('too high, making smaller', high, low, guess)

            if math.fabs(num - guess * guess) < delta:
                return round(guess, precision)

        print("final is ", guess, guess * guess)
        return n + guess

    def sqrt2(self, num, precision):
        n = 0;
        while (n * n < num):
            n = n+1

        # n is now first whole number less than num
        n = n-1
        dec = 1.0
        guess = n+dec

        low = 0.0
        high = 1.0
        dec = high


        delta = math.pow(0.1, precision)
        print(delta)

        for i in range(0, precision*5):
            print(num-guess*guess, delta)
            dec = (high+low)/2
            guess = n + dec

            if math.pow(guess, 2) == num:
                print('returning exact match')
                return n + dec

            if math.pow(guess, 2) < num:
                high = high
                low = dec
                print('too low . making larger', high, low, dec)
            else:
                high = dec
                low = low
                print('too high, making smaller', high, low, dec)

            if math.fabs(num - guess*guess) < delta:
                return round(guess, precision)

        print("final is ", guess, guess*guess)
        return n+dec

