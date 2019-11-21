import random
import time
import copy


def gaps_n_2(n):
    n //= 2
    while n > 0:
        yield n
        n //= 2


def gaps_n_3div2(n):
    max_k = 0
    while 2 ** max_k - 1 < n:
        max_k += 1
    for k in range(max_k - 1, -1, -1):
        yield 2 ** k - 1


def gaps_n_log_2_n(n):
    res = []
    p = 1
    while p < n:
        q = p
        while q < n:
            res.append(q)
            q *= 3
        p *= 2
    res.sort(reverse=True)
    return res


def shell_sort(arr, gaps):
    for gap in gaps(len(arr)):
        i = 0
        while i + gap < len(arr):
            j = i + gap
            tmp = arr[j]
            while j - gap >= 0 and arr[j - gap] > tmp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = tmp
            i += 1
    return arr


def get_time_work(arr, gaps):
    start = time.time()
    shell_sort(arr, gaps)
    end = time.time()
    return round(end - start, 3)


def shuffle_k_elements(arr, k):
    assert len(arr) >= k
    positions = set()
    while len(positions) < k:
        pos = random.randint(0, len(arr) - 1)
        positions.add(pos)
    positions = list(positions)
    values = [arr[pos] for pos in positions]
    random.shuffle(values)
    for pos, val in zip(positions, values):
        arr[pos] = val


def run(gaps):
    size = 2 ** 18
    arr_sort = list(range(size))
    arr_rnd = copy.deepcopy(arr_sort)
    random.shuffle(arr_rnd)
    arr_rnd_10percent = copy.deepcopy(arr_sort)
    shuffle_k_elements(arr_rnd_10percent, size // 10)
    arr_rnd_5el = copy.deepcopy(arr_sort)
    shuffle_k_elements(arr_rnd_5el, 5)
    print(f'Время работы алгоритма сортировки с шагом {gaps.__name__} с количеством элементов {size}:')
    print('сортированный массив: ' + str(get_time_work(arr_sort, gaps)) + ' секунды')
    print('случайный массив: ' + str(get_time_work(arr_rnd, gaps)) + ' секунды')
    print('10% элементов случайны: ' + str(get_time_work(arr_rnd_10percent, gaps)) + ' секунды')
    print('5 элементов случайны: ' + str(get_time_work(arr_rnd_5el, gaps)) + ' секунды')
    print()


def main():
    for gaps in [gaps_n_2, gaps_n_3div2, gaps_n_log_2_n]:
        run(gaps)


if __name__ == '__main__':
    main()
