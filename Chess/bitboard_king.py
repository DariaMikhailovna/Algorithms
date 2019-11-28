from typing import TextIO


def get_king_moves(king_nr):
    res = []
    moves_count = 0
    king_bits = 1 << king_nr
    n_a = 0xFeFeFeFeFeFeFeFe
    n_ab = 0xFcFcFcFcFcFcFcFc
    n_h = 0x7f7f7f7f7f7f7f7f
    n_gh = 0x3f3f3f3f3f3f3f3f
    moves_bits = n_gh & (king_bits << 1 | king_bits >> 1) | n_h & (king_bits << 15 | king_bits >> 17) \
                | n_a & (king_bits << 17 | king_bits >> 15) | n_ab & (king_bits << 10 | king_bits >> 6)
    res.append(moves_bits)
    while moves_bits != 0:
        moves_bits &= (moves_bits - 1)
        moves_count += 1
    res.append(moves_count)
    return res[-1:]


def get_king_moves_f(f_in: TextIO, f_out: TextIO):
    king_nr = int(f_in.readline().rstrip())
    res = get_king_moves(king_nr)
    for line in res:
        print(line, file=f_out)
