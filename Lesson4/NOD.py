def search_using_subtraction(a, b):
    a = abs(a)
    b = abs(b)
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a + b


def search_using_remainder(a, b):
    if not b:
        return abs(a)
    return search_using_remainder(b, a % b)


if __name__ == '__main__':
    res1 = search_using_remainder(320, -45)
    res2 = search_using_subtraction(320, 45)
    print(res1)
    print(res2)
