from Board import Board
import numpy as np


def main():
    game = Board(3)

  #  print(game.create_board())

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
    game.mark(0, 2, 'o')
    game.mark(1, 1, 'o')
#    game.mark(1, 1, 'x')
    game.mark(1, 2, 'o')
    #game.mark(2, 0, 'p')
#    game.mark(2, 1, 'x')
    game.mark(2, 0, 'o')
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
