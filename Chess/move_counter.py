from typing import TextIO


def get_move_counter(f_in: TextIO, f_out: TextIO):
    fen = f_in.readline().rstrip().split('/')
    new_fen = '/'.join(fen[:-1]) + '/'
    end = fen[-1].split()
    is_b = False
    for i in range(len(end) - 1):
        if i == 1:
            if end[i] == 'w':
                new_fen += 'b '
            if end[i] == 'b':
                new_fen += 'w '
                is_b = True
        else:
            new_fen += end[i] + ' '
    if is_b:
        new_count = int(end[len(end) - 1]) + 1
        new_fen += str(new_count)
    else:
        new_fen += end[len(end) - 1]
    print(new_fen, file=f_out)
