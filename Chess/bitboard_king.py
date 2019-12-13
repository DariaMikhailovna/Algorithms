from typing import TextIO


def get_king_moves(king_nr):
    res = []
    moves_count = 0
    king_bits = 1 << king_nr
    n_a = 0xFeFeFeFeFeFeFeFe
    n_h = 0x7f7f7f7f7f7f7f7f
    moves_bits = n_h & (king_bits << 1 | king_bits << 7 | king_bits << 9) | king_bits << 8 \
                | n_a & (king_bits >> 1 | king_bits >> 7 | king_bits >> 9) | king_bits >> 8
    res.append(moves_bits)
    while moves_bits != 0:
        moves_bits &= (moves_bits - 1)
        moves_count += 1
    res.append(moves_count)
    return reversed(res)


def get_king_moves_f(f_in: TextIO, f_out: TextIO):
    king_nr = int(f_in.readline().rstrip())
    res = get_king_moves(king_nr)
    for line in res:
        print(line, file=f_out)
