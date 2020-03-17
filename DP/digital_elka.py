def main():
    n = int(input())
    elka = []
    for i in range(1, n + 1):
        s = list(map(int, input().strip().split()))
        elka.append(s)
    if n == 1:
        print(elka[0][0])
        return
    for i in range(n - 2, -1, -1):
        for j in range(len(elka[i])):
            elka[i][j] += max(elka[i + 1][j], elka[i + 1][j + 1])
    print(elka[0][0])


if __name__ == '__main__':
    main()
