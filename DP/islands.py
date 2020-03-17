def main():
    def walk(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return
        if matrix[x][y] == 0:
            return
        matrix[x][y] = 0
        walk(x - 1, y)
        walk(x + 1, y)
        walk(x, y + 1)
        walk(x, y - 1)

    n = int(input())
    matrix = []
    for i in range(n):
        s = list(map(int, input().split()))
        matrix.append(s)
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1
                walk(i, j)
    print(count)


if __name__ == '__main__':
    main()
