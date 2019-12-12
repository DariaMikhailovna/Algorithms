from math import log
import sys


def update(arr, pos, new_val):
    delta = new_val - arr[pos]
    arr[pos] = new_val
    pos //= 2
    while pos > 0:
        arr[pos] += delta
        pos //= 2


def get_sum(arr, left, right):
    res = 0
    while left <= right:
        if left & 1:
            res += arr[left]
        if right & 1 == 0:
            res += arr[right]
        left = (left + 1) // 2
        right = (right - 1) // 2
    return res


def build(arr, count_numbers):
    h = int(log(count_numbers, 2)) + 1
    size = int(2 ** (h + 1))
    res = [0] * size
    l = 2 ** h
    r = l + count_numbers
    res[l:r] = arr
    for i in range(l - 1, 0, -1):
        res[i] = res[i * 2] + res[i * 2 + 1]
    return res


def main():
    count_numbers, count_query = map(int, raw_input().split())
    count_numbers += 1
    h = int(log(count_numbers, 2)) + 1
    delta = 2 ** h
    arr = [0] * count_numbers
    arr = build(arr, count_numbers)
    for i in range(count_query):
        query = raw_input().split()
        if query[0] == 'A':
            update(arr, delta + int(query[1]), int(query[2]))
        elif query[0] == 'Q':
            print(get_sum(arr, delta + int(query[1]), delta + int(query[2])))


if __name__ == '__main__':
    with open('sum.in', 'r') as fin:
        with open('sum.out', 'w') as fout:
            sys.stdin = fin
            sys.stdout = fout
            main()
