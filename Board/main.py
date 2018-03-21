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
    p2 = Player(P2, 5000)
    print(p1.symbol, p1.money)
    print(p2.symbol, p2.money)

    # Decide who goes first
    x = randint(0, 1)
    turn = p1 if x == 0 else p2

    print("initial", x, turn.symbol)

    i = 0
#   while not game.check_state():
    while True:
        turn = p2 if turn == p1 else p1
        print(turn.symbol, turn.label)
        i = i+1

        if i == 10:
            break;

    test2(game)

  #  print("Checking winning state", game.check_state())


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
