def main():
    n = int(input())
    if n == 1:
        print(2)
        return
    f55 = 1
    f58 = 1
    f85 = 1
    f88 = 1
    for i in range(3, n + 1):
        n55 = f58
        n58 = f85 + f88
        n85 = f55 + f58
        n88 = f85
        f55 = n55
        f58 = n58
        f85 = n85
        f88 = n88
    print(f55 + f58 + f85 + f88)


if __name__ == '__main__':
    main()
