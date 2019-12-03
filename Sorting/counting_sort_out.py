import random as rnd
import time


def create_file_with_numbers(count_numbers, file):
    with open(file, 'wb') as f:
        for i in range(count_numbers):
            f.write(rnd.randint(0, 65535).to_bytes(2, byteorder='big'))


def counting_sort_out(file, count_numbers):
    arr = [0]
    with open(file, 'r+b') as f:
        while count_numbers:
            count_numbers -= 1
            num = int.from_bytes(f.read(2), byteorder='big')
            while num >= len(arr):
                arr.append(0)
            arr[num] += 1
        f.seek(0, 0)
        for i in range(len(arr)):
            for j in range(arr[i]):
                f.write(i.to_bytes(2, byteorder='big'))


def get_work_time(function, file, count_numbers):
    start = time.time()
    function(file, count_numbers)
    end = time.time()
    return round(end - start, 3)


def main(count_numbers):
    file = 'rnd_numbers.bin'
    create_file_with_numbers(count_numbers, file)
    print(f'Время работы внешней сортировки подсчетом массива из {count_numbers} элементов:')
    print(str(get_work_time(counting_sort_out, file, count_numbers)) + ' секунд')
    print()


if __name__ == '__main__':
    main(100000000)
