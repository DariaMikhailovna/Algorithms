import random
import time
import copy


def get_gap():
    pass


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        i = 0
        while i + gap < len(arr):
            j = i + gap
            tmp = arr[j]
            while j - gap >= 0 and arr[j - gap] > tmp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = tmp
            i += 1
        gap //= 2
    return arr


def get_arr(size):
    arr = []
    for i in range(size):
        arr.append(i)
    return arr


def get_time_work(arr):
    start = time.time()
    shell_sort(arr)
    end = time.time()
    return int((end - start))


if __name__ == '__main__':
    size = 500000
    arr_sort = get_arr(size)
    arr_rnd = copy.deepcopy(arr_sort)
    random.shuffle(arr_rnd)
    arr_rnd_10percent = copy.deepcopy(arr_sort)
    for i in range(size // 10):
        rnd_ind = random.randint(0, size - 1)
        arr_rnd_10percent[rnd_ind] = i
    arr_rnd_5el = copy.deepcopy(arr_sort)
    for i in range(5):
        rnd_ind = random.randint(0, size - 1)
        rnd_val = random.randint(0, size - 1)
        arr_rnd_5el[rnd_ind] = rnd_val
    print(f'Время работы алгоритма сортировки с шагом gap //= 2 и размером {size}:')
    print('сортированный массив: ' + str(get_time_work(arr_sort)) + ' секунды')
    print('случайный массив: ' + str(get_time_work(arr_rnd)) + ' секунды')
    print('10% элементов случайны: ' + str(get_time_work(arr_rnd_10percent)) + ' секунды')
    print('5 элементов случайны: ' + str(get_time_work(arr_rnd_5el)) + ' секунды')

