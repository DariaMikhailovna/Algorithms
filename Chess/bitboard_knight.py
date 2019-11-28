from typing import TextIO


def get_knight_moves(knight_nr):
    res = []
    moves_count = 0
    knight_bits = 1 << knight_nr
    n_a = 0xFeFeFeFeFeFeFeFe
    n_ab = 0xFcFcFcFcFcFcFcFc
    n_h = 0x7f7f7f7f7f7f7f7f
    n_gh = 0x3f3f3f3f3f3f3f3f
    moves_bits = n_gh & (knight_bits << 6 | knight_bits >> 10) | n_h & (knight_bits << 15 | knight_bits >> 17) \
                | n_a & (knight_bits << 17 | knight_bits >> 15) | n_ab & (knight_bits << 10 | knight_bits >> 6)
    res.append(moves_bits)
    while moves_bits != 0:
        moves_bits &= (moves_bits - 1)
        moves_count += 1
    res.append(moves_count)
    return reversed(res)


def get_knight_moves_f(f_in: TextIO, f_out: TextIO):
    knight_nr = int(f_in.readline().rstrip())
    res = get_knight_moves(knight_nr)
    for line in res:
        print(line, file=f_out)
