from shell_sort import *


def heap_sort(arr):
    def down(size, root):
        l = 2 * root + 1
        r = l + 1
        mx = root
        if l < size and arr[l] > arr[mx]:
            mx = l
        if r < size and arr[r] > arr[mx]:
            mx = r
        if mx != root:
            arr[root], arr[mx] = arr[mx], arr[root]
            down(size, mx)

    for node in range(len(arr) - 1, -1, -1):
        down(len(arr), node)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        down(i, 0)
    return arr


def get_work_time(arr):
    start = time.time()
    heap_sort(arr)
    end = time.time()
    return round(end - start, 3)


if __name__ == '__main__':
    size = 2 ** 20
    arr_sort = list(range(size))
    arr_rnd = copy.deepcopy(arr_sort)
    random.shuffle(arr_rnd)
    arr_rnd_5percent = copy.deepcopy(arr_sort)
    shuffle_k_elements(arr_rnd_5percent, size // 5)
    print(f'Время работы алгоритма shell сортировки с асимптотикой n^(3/2) с количеством элементов {size}:')
    print('случайный массив: ' + str(get_time_work(arr_rnd, gaps_n_3div2)) + ' секунды')
    print('5% элементов случайны: ' + str(get_time_work(arr_rnd_5percent, gaps_n_3div2)) + ' секунды')
    print()
    print(f'Время работы алгоритма heap_sort с количеством элементов {size}:')
    print('случайный массив: ' + str(get_work_time(arr_rnd)) + ' секунды')
    print('5% элементов случайны: ' + str(get_work_time(arr_rnd_5percent)) + ' секунды')


