from get_len import get_len_f
from bitboard_fen import get_bitboard_by_fen_f
from bitboard_knight import get_knight_moves_f
from bitboard_king import get_king_moves
from fen_ascii import get_ascii_table
from move_counter import get_move_counter
from half_move_counter import get_half_move_counter


import os
import io


def run_tests(function, test_dir):
    files = os.listdir(test_dir)
    for file_in in files:
        if file_in[-2:] == 'in':
            file_out = list(filter(lambda x: x[5] == file_in[5] and x[-3:] == 'out', files))[0]
            with open(os.path.join(test_dir, file_in), 'r') as f_in:
                f_out = io.StringIO()
                function(f_in, f_out)
                res = f_out.getvalue()
            with open(os.path.join(test_dir, file_out), 'r') as f:
                txt_out = f.read()
            assert res.rstrip('\n') == txt_out.rstrip('\n')


def main():
    run_tests(get_len_f, '!.TESTS')
    run_tests(get_bitboard_by_fen_f, '0.BITS\\1744.0.Bitboard - FEN')
    run_tests(get_knight_moves_f, '0.BITS\\3710.0.Bitboard - Конь')
    # run_tests(get_king_moves, '0.BITS\\3733.0.Bitboard - Король')
    run_tests(get_ascii_table, '1.FEN\\1743.1.FEN - ASCII')
    run_tests(get_move_counter, '1.FEN\\1746.1.Счётчик ходов')
    # run_tests(get_half_move_counter, '1.FEN\\3694.1.Счётчик полуходов')
    pass


if __name__ == '__main__':
    main()
