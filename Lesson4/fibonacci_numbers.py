import math


def rec(n):
    if n <= 2:
        return 1
    else:
        return rec(n - 1) + rec(n - 2)


def dynamic(n):
    a = 1
    b = 1
    for i in range(3, n + 1):
        t = a + b
        a = b
        b = t
    return b


def golden_ratio(n):
    f = (1 + math.sqrt(5)) / 2
    return int((math.pow(f, n) / math.sqrt(5)) + 0.5)


if __name__ == '__main__':
    print(rec(13))
    print(dynamic(100))
    print(golden_ratio(100))
