from Board import Board
from Player import Player

import numpy as np
from random import randint

P1 = 'x'
P2 = 'o'


def main():
    # Set up new board
    game = Board(3)

    # Generate 2 players with starting money balances
    p1 = Player(P1, 1000)
    p2 = Player(P2, 1000)
    print(p1.symbol, p1.balance)
    print(p2.symbol, p2.balance)

    # Decide who goes first
    x = randint(0, 1)
    turn = p1 if x == 0 else p2

    #print("initial", x, turn.symbol)

    while True:
        # TODO: Need to handle same bids
        # TODO: Need to handle when players have no more money
        p1_bid = p1.request_bid()
        p2_bid = p2.request_bid()

        if p1_bid > p2_bid:
            current_player = p1
        else:
            current_player = p2

        mark = current_player.symbol
        print("\n(game engine)Current player is", current_player.label, "symbol is ", mark)
        x, y = current_player.request_move(game)
        print("(game engine) Move selected is row", x, "col", y, "\n")

        game.mark(x, y, mark)
        print(game.board, "\n-------------\n" )

        terminal, symbol = game.check_state()

        if terminal is True:
            print("Terminal state found. ")
            if symbol == -1:
                print("Game is a draw.  Game took", game.turn, " turns")
            else:
                print(current_player.label, "(", symbol, ") has won.  Game took", game.turn, "turns.")

            break

def test1(game):
    print(game.board[1][2])

    print(game.mark(1, 2, 'x'))
    print(game.board[1][2])

    print(game.mark(1, 3, 'o'))
    print(game.mark(5, 1, 'x'))
    print(game.mark(1, 5, 'o'))
    print(game.mark(1, 6, 'x'))
    print(game.mark(6, 1, 'x'))
    print(game.mark(0, 0, 'o'))
    print(game.mark(3, 0, 'x'))

def test2(game):
#    game.mark(0, 0, 'x')
#    game.mark(0, 1, 'x')
    #game.mark(0, 0, 'x')
    game.mark(1, 1, 'x')
#    game.mark(1, 1, 'x')
    game.mark(1, 2, 'o')
    #game.mark(2, 0, 'p')
#    game.mark(2, 1, 'x')
    game.mark(2, 2, 'x')
    print(game.board)

    game.check_state()

    '''
    temp2 = temp == game.board[0, :]
    print(game.board[0, :])
    print(temp2)

    temp2 = temp == game.board[1, :]
    print(game.board[1, :])
    print(temp2)

    temp2 = temp == game.board[2, :]
    print(game.board[2, :])
    print(temp2)
    '''

    #temp2 = temp == game.board[:, 0]
    #print(game.board[:, 0])
    #print(temp2)

   # temp2 = temp == game.board[:, 1]
   # print(game.board[:, 1])
   # print(temp2)

   # temp2 = temp == game.board[:, 2]
   # print(game.board[:, 2])
  #  print(temp2)

  #  a = np.all(temp == game.board[0, :])
  #  print(a)

  #  a = np.all(temp == game.board[1, :])
  #  print(a)

  #  a = np.all(temp == game.board[2, :])
  #  print(a)

 #   a = np.all(temp == game.board[:, 0])
 #   print(a)
 #   a = np.all(temp == game.board[:, 1])
 #   print(a)
 #   a = np.all(temp == game.board[:, 2])
 #   print(a)

#    print(game.board[0, :])
#    print(game.board[1, :])
#    print(game.board[2, :])
#    print(game.board[:, 0])
#    print(game.board[:, 1])
#    print(game.board[:, 2])


#    print(game.board[0])
#    print(game.board[0][1:])
#    print(game.board[0][:-1])
#    print(game.board[0][1:] == game.board[0][:-1])
       # self.board[i][1:] == self.board[i][:-1]:

if __name__ == '__main__':
    main()
