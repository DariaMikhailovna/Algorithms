def get_nod(a, b):
    if not b:
        return abs(a)
    return get_nod(b, a % b)


def main():
    ab, cd = input().split('+')
    a, b = map(int, ab.split('/'))
    c, d = map(int, cd.split('/'))
    sm = a * d + c * b
    div = b * d
    nod = get_nod(sm, div)
    print(f'{sm // nod}/{div // nod}')


if __name__ == '__main__':
    main()
