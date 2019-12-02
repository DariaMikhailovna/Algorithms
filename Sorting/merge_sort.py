from heap_sort import heap_sort
import random as rnd
import time
import copy
import tempfile


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
        arr[left:right] = sorted(arr[left:right])
        return
    center = left + (right - left) // 2
    merge_sort_composite(arr, left, center)
    merge_sort_composite(arr, center, right)
    merge(arr, left, center, right)


def create_file_with_numbers(count_numbers, file):
    with open(file, 'wb') as f:
        for i in range(count_numbers):
            t = rnd.randint(48, 57) * 256 + rnd.randint(48, 57)
            f.write(t.to_bytes(2, byteorder='big'))


def merge_out(file, left, center, right):
    with tempfile.TemporaryFile(mode='w+b') as temp:
        i = left
        j = center
        with open(file, 'r+b') as fi:
            with open(file, 'r+b') as fj:
                fi.seek(2 * i, 0)
                fj.seek(2 * j, 0)
                while i < center and j < right:
                    num_i = fi.read(2)
                    num_j = fj.read(2)
                    if num_i < num_j:
                        temp.write(num_i)
                        i += 1
                    else:
                        temp.write(num_j)
                        j += 1
                while i < center:
                    temp.write(fi.read(2))
                    i += 1
                while j < right:
                    temp.write(fj.read(2))
                    j += 1
        with open(file, 'r+b') as f:
            r = temp.read()
            temp.seek(0, 2)
            end = temp.tell()
            temp.seek(0, 0)
            f.seek(left * 2, 0)
            while True:
                if temp.tell() == end:
                    break
                num = temp.read(2)
                f.write(num)


def merge_sort_out(file, left, right):
    if right - left <= 1:
        return
    center = left + (right - left) // 2
    merge_sort_out(file, left, center)
    merge_sort_out(file, center, right)
    merge_out(file, left, center, right)


def get_work_time(function, arr=None, file=None, count_numbers=None):
    start = time.time()
    if arr is None:
        function(file, 0, count_numbers)
    else:
        function(arr, 0, len(arr))
    end = time.time()
    return round(end - start, 3)


def main(count_numbers):
    # arr = [1, 245, 5, 7, 9, 100, 2, 4, 6, 8, 900, 0]
    # merge_sort(arr, 0, len(arr))
    # print(arr)
    file = 'rnd_numbers.bin'
    create_file_with_numbers(count_numbers, file)
    arr = []
    # for i in range(count_numbers):
    #     arr.append(rnd.randint(0, 65535))
    # print(f'Время работы обычной сортировки слиянием (внутренней) массива из {count_numbers} элементов:')
    # print(str(get_work_time(function=merge_sort, arr=copy.deepcopy(arr))) + ' секунд')
    # print()
    # print(f'Время работы комбинированной сортировки слиянием (внутренней) массива из {count_numbers} элементов:')
    # print(str(get_work_time(function=merge_sort_composite, arr=copy.deepcopy(arr))) + ' секунд')
    print()
    print(f'Время работы обычной сортировки слиянием (внешней) массива из {count_numbers} элементов:')
    print(str(get_work_time(function=merge_sort_out, file=file, count_numbers=count_numbers)) + ' секунд')


if __name__ == '__main__':
    main(10)
