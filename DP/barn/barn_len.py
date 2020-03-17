def main():
    n, m = map(int, input().split())
    t = int(input())
    matrix = [[1] * n for _ in range(m)]
    for i in range(t):
        c, r = list(map(int, input().strip().split()))
        matrix[r][c] = 0
    for m_ in range(1, m):
        for n_ in range(n):
            if matrix[m_][n_] != 0:
                matrix[m_][n_] = matrix[m_ - 1][n_] + 1
    for i in range(m):
        print(*matrix[i])


if __name__ == '__main__':
    main()
