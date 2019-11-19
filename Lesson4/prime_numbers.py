def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_prime_fast(number):
    if number == 1:
        return False
    if number != 2 and number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


p = []


def is_prime_fast_fast(number):
    if number == 1:
        return False
    if number != 2 and number % 2 == 0:
        return False
    i = 0
    while i < len(p) and p[i] * p[i] <= number:
        if number % p[i] == 0:
            return False
        i += 1
    p.append(number)
    return True


def eratosthenes(number):
    a = [True] * (number + 1)
    a[0] = False
    a[1] = False
    for i in range(number + 1):
        if a[i]:
            l = i * i
            if l > number:
                break
            for j in range(l, number + 1, i):
                a[j] = False
    return sum(a)


if __name__ == '__main__':
    print(is_prime(25))
    print(is_prime_fast(2))
    res = 0
    for i in range(1, 1000 + 1):
        if is_prime_fast(i):
            res += 1
    print(res)
    res = 0
    for i in range(1, 10000 + 1):
        if is_prime_fast_fast(i):
            res += 1
    print(res)
    print(eratosthenes(100000000))
