from heap_sort import heap_sort
import random as rnd
import time
import copy


def merge(arr, left, center, right):
    res = []
    i = left
    j = center
    while i < center and j < right:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    if i < center:
        res.extend(arr[i:center])
    if j <= right:
        res.extend(arr[j:right])
    arr[left:right] = res


def merge_sort(arr, left, right):
    if right - left <= 1:
        return
    center = left + (right - left) // 2
    merge_sort(arr, left, center)
    merge_sort(arr, center, right)
    merge(arr, left, center, right)


def merge_sort_composite(arr, left, right):
    if right - left <= 1:
        return
    if right - left <= 1024:
        arr[left:right] = heap_sort(arr[left:right])
        return
    center = left + (right - left) // 2
    merge_sort_composite(arr, left, center)
    merge_sort_composite(arr, center, right)
    merge(arr, left, center, right)


def get_work_time(function, arr):
    start = time.time()
    function(arr, 0, len(arr))
    end = time.time()
    return round(end - start, 3)


def main(count_numbers):
    # arr = [1, 245, 5, 7, 9, 100, 2, 4, 6, 8, 900, 0]
    # merge_sort(arr, 0, len(arr))
    # print(arr)
    arr = []
    for i in range(count_numbers):
        arr.append(rnd.randint(0, 65535))
    print(f'Время работы обычной сортировки слиянием (внутренней) массива из {count_numbers} элементов:')
    print(str(get_work_time(merge_sort, copy.deepcopy(arr))) + ' секунд')
    print()
    print(f'Время работы комбинированной сортировки слиянием (внутренней) массива из {count_numbers} элементов:')
    print(str(get_work_time(merge_sort_composite, copy.deepcopy(arr))) + ' секунд')


if __name__ == '__main__':
    main(10000)
