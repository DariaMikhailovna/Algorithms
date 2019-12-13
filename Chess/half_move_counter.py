from typing import TextIO

d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def get_half_move_counter(f_in: TextIO, f_out: TextIO):
    fen = f_in.readline().rstrip()
    fen2 = ''
    for i in range(len(fen)):
        if fen[i] == '/':
            continue
        if fen[i].isdigit():
            numb = int(fen[i])
            while numb > 0:
                fen2 += '1'
                numb -= 1
            continue
        fen2 += fen[i]
    fen = fen.split('/')
    move = f_in.readline().strip()
    new_fen = ''
    flag = False
    t1 = fen2[(8 - int(move[1])) * 8 + d[move[0]]]
    t2 = fen2[(8 - int(move[3])) * 8 + d[move[2]]]
    if t1 == 'p' or t1 == 'P' or not t2.isdigit():
        flag = True
    print(new_fen, file=f_out)
