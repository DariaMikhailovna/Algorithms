from typing import TextIO


def get_len(string):
    return len(string)


def get_len_f(f_in: TextIO, f_out: TextIO):
    string = f_in.readline().rstrip()
    res = get_len(string)
    print(res, file=f_out)
