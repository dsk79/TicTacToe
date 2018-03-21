from Board import Board


def main():
    game = Board(5)
    print(game.create_board())
    print(game.board[1][2])

    print(game.set_mark(1,2, 'x'))
    print(game.board[1][2])
    print(game.set_mark(1,3, 'o'))
    print(game.set_mark(5,1, 'x'))
    print(game.set_mark(1,5,'o'))
    print(game.set_mark(1,6, 'x'))
    print(game.set_mark(6,1, 'x'))
    print(game.set_mark(0,0,'o'))
    print(game.set_mark(3,0,'x'))


if __name__ == '__main__':
    main()
