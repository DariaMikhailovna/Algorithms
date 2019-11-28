from typing import TextIO

figures = {
    'P': 0,
    'N': 1,
    'B': 2,
    'R': 3,
    'Q': 4,
    'K': 5,

    'p': 6,
    'n': 7,
    'b': 8,
    'r': 9,
    'q': 10,
    'k': 11
}


def get_bitboard_by_fen(fen):
    bitboard = 0
    board = [bitboard] * 12
    rows = fen.split('/')
    for row in range(len(rows)):
        i = 0
        for symbol in rows[row]:
            if symbol.isdigit():
                i += int(symbol)
            else:
                num_board = figures[symbol]
                board[num_board] = board[num_board] | (1 << ((7 - row) * 8 + i))
                i += 1
    return board


def get_bitboard_by_fen_f(f_in: TextIO, f_out: TextIO):
    fen = f_in.readline().rstrip()
    board = get_bitboard_by_fen(fen)
    for line in board:
        print(line, file=f_out)


if __name__ == '__main__':
    boards = get_bitboard_by_fen('7k/8/8/8/8/8/8/K7')
    for b in boards:
        print(b)
