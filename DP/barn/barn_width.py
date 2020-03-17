def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append(int(input()))
    l = [0]
    r = []
    for i in range(1, n):
        if m[i] == m[i - 1] and len(l):
            l.append(l[-1])
            continue
        j = i
        while j >= 0 and m[j] >= m[i]:
            j -= 1
        l.append(j + 1)
    for i in range(n - 1):
        if i > 0 and m[i] == m[i - 1] and len(r):
            r.append(r[-1])
            continue
        j = i
        while j < n and m[j] >= m[i]:
            j += 1
        r.append(j - 1)
    r.append(len(m) - 1)
    print(*l)
    print(*r)


if __name__ == '__main__':
    main()
