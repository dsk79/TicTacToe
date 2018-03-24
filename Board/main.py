from Board import Board
from Player import Player

''' Symbol constants '''
spacer = "***********************************************"
half_spacer = "*******************"
P1 = 'x'
P2 = 'o'

''' Configurable params '''
p1_balance = 1000
p2_balance = 1000
board_size = 3


def main():
    games_to_run = 100

    results = {'x': 0, 'o': 0, 'draw': 0}

    for i in range(0, games_to_run):
        print(spacer + "\n" + half_spacer + " GAME ", i+1, half_spacer + "\n" + spacer)
        game_result = game_engine()
        results[game_result] += 1

    print('Final results\nWins:', results)


def initialize_players():
    p1 = Player(P1, p1_balance)
    p2 = Player(P2, p2_balance)
    return p1, p2


def game_engine():
    # Create the 2 players
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

        # Reduce each player's balance by their bid, and increase by opponent's bid
        p1.update_balance(p1_bid, p2_bid)
        p2.update_balance(p2_bid, p1_bid)

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
    print("Current turn is", turn, "\n")
    return turn


if __name__ == '__main__':
    main()
