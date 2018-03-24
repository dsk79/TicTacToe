from Board import Board
from Player import Player

P1 = 'x'
P2 = 'o'
p1_balance = 1000
p2_balance = 1000
board_size = 3


def main():
    games_to_run = 1000

    results = {'x': 0, 'o': 0, 'draw': 0}

    for i in range(0, games_to_run):
        print("*************************************************")
        print("*******************  GAME ", i+1, " *******************")
        print("*************************************************")
        game_result = game_engine()
        results[game_result] += 1

    print('Wins:', results)


def initialize_players():
    p1 = Player(P1, p1_balance)
    p2 = Player(P2, p2_balance)
    return p1, p2


def game_engine():
    p1, p2 = initialize_players()

    # Set up new board
    game = Board(board_size, p1, p2)

    turn = 0

    game_over = False
    while not game_over:
        turn = update_turn(turn)

        p1_bid = 0
        p2_bid = 0
        while p1_bid == p2_bid:
            p1_bid = p1.request_bid(game)
            p2_bid = p2.request_bid(game)

        if p1_bid > p2_bid:
            current_player = p1
        else:
            current_player = p2

        mark = current_player.symbol
        print("\n(game engine)Current player is", current_player.label, "symbol is ", mark)
        x, y = current_player.request_move(game)
        print("(game engine) Move selected is row", x, "col", y,
              "Player 1 balance: ", p1.balance, "\tPlayer 2 balance:", p2.balance, "\n")

        game.mark(x, y, mark)
        print(game.board, "\n\n------------------\n")

        game_over, symbol = game.check_state()

        if game_over is True:
            print("Terminal state found.")
            if symbol == -1:
                print("Game is a draw.  Game took", turn, " turns\n")
                return "draw"
            else:
                print(current_player.label, "(" + symbol + ") has won.  Game took", turn, "turns.\n")
                return symbol

def update_turn(turn):
    turn += 1
    print("Current turn is", turn ,"\n")
    return turn

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
