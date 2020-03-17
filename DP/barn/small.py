def main():
    def calc():
        max_square = 0
        for nn in range(n):
            for mm in range(m):
                new_square = find_max_square(nn, mm)
                if new_square > max_square:
                    max_square = new_square
        return max_square

    def find_max_square(nn, mm):
        len_m = 1
        limit_len = find_way_len(nn, mm)
        max_square = len_m * limit_len
        for mi in range(mm + 1, m):
            len_m += 1
            len_n = find_way_len(nn, mi)
            if limit_len > len_n:
                limit_len = len_n
            if len_n > limit_len:
                len_n = limit_len
            if max_square < len_m * len_n:
                max_square = len_m * len_n
        return max_square

    def find_way_len(nn, mm):
        way_len = 0
        while nn < n:
            if matrix[nn][mm] == 1:
                break
            way_len += 1
        return way_len

    n, m = map(int, input().split())
    matrix = []
    for i in range(m):
        s = list(map(int, input().strip().split()))
        matrix.append(s)
    print(calc())


if __name__ == '__main__':
    main()
