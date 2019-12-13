from typing import TextIO


def get_ascii_table(f_in: TextIO, f_out: TextIO):
    table = ['  +-----------------+',
             '8 | . . . . . . . . |',
             '7 | . . . . . . . . |',
             '6 | . . . . . . . . |',
             '5 | . . . . . . . . |',
             '4 | . . . . . . . . |',
             '3 | . . . . . . . . |',
             '2 | . . . . . . . . |',
             '1 | . . . . . . . . |',
             '  +-----------------+',
             '    a b c d e f g h  ']
    fen = f_in.readline().rstrip().split('/')
    fen[len(fen) - 1] = fen[len(fen) - 1].split()[0]
    table_ind = 1
    for line in fen:
        table_line_ind = 4
        for i in range(len(line)):
            if line[i].isdigit():
                table_line_ind += int(line[i]) * 2
                continue
            else:
                table[table_ind] = table[table_ind][:table_line_ind] + line[i] + table[table_ind][table_line_ind + 1:]
            table_line_ind += 2
        table_ind += 1
    for line in table:
        print(line, file=f_out)
