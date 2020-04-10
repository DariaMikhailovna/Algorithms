def get_width():
    n = int(input())
    m = []
    for i in range(n):
        m.append(int(input()))
    l = []
    r = []
    for i in range(n):
        j = i
        while j >= 0 and m[j] >= m[i]:
            j -= 1
        l.append(j + 1)
    for i in range(n):
        j = i
        while j < n and m[j] >= m[i]:
            j += 1
        r.append(j - 1)
    print(*l)
    print(*r)


if __name__ == '__main__':
    get_width()
