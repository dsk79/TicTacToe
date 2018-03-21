import math
import numpy as np
import pandas as pd


class Board:
    def __init__(self, length):
        self.rows = length
        self.cols = length
        self.board = self.create_board()

    def create_board(self):
        # N x N board (always square, any size)
        print('Hello world again')

        return np.full((self.rows, self.cols), fill_value=None)


    def set_mark(self, x, y, symbol):
        if x >= self.rows or x < 0 or y >= self.cols or y < 0:
            print('Coordinates are out of range', x, y)
            return False

        if self.board[x][y] is not None:
            print("Coordinates is already marked ", self.board[x][y], x, y)
            return False

        assert isinstance(symbol, str)
        self.board[x][y] = symbol
        return self.board

    ''' Check for winning state with N connected marks along any row, col, or diagonal'''
    def check_state(self):
        if board[0][0] is None:
            return False

        for i in range (0, self.rows):
            if self.board[i][1:] == self.board[i][:-1]:
                return True


        return False

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

