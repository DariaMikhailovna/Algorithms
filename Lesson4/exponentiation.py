def power_slow(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res


def power_fast(a, n):
    res = a
    k = 1
    while k < n // 2:
        res *= res
        k *= 2
    while k < n:
        k += 1
        res *= a
    return res


def power_fast_fast(a, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= a
        a *= a
        n //= 2
    return res


if __name__ == '__main__':
    res1 = power_slow(3, 9)
    res3 = power_fast(3, 11)
    # res2 = power_fast_fast(2, 1000000000000000)
    res2 = power_fast_fast(3, 11)
    print(res1)
    print(res2)
    print(res3)
