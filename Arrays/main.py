from single_array import *
from vector_array import *
from factor_array import *
from matrix_array import *
from linked_list import *
from double_linked_list import *
from stack import *
from queue_container import *

import time


# def add_items(cls, cnt, arg1=None, arg2=None):
#     start = time.time()
#     if arg1 and not arg2:
#         arr = cls(arg1)
#     elif arg2:
#         arr = FactorArray(arg1, arg2)
#     else:
#         arr = cls()
#     for i in range(cnt):
#         arr.add(i)
#     end = time.time()
#     print(int((end - start) * 1000))
#     return arr


def remove_items(arr):
    start = time.time()
    for i in range(arr.size() - 1):
        arr.remove(0)
    end = time.time()
    print(int((end - start) * 1000))


def test_array(cls, arg1=None, arg2=None):
    # if arg1 and not arg2:
    #     arr = cls(arg1)
    # elif arg2:
    #     arr = FactorArray()
    # else:
    #     arr = cls()
    arr = MatrixArray(10)
    for i in range(35):
        arr.add(i)
    arr.add(100, 0)
    arr.add(1, 12)
    print(arr)
    print(arr[0])
    arr.add(2)
    print(arr)
    arr.add(3, 1)
    print(arr)
    arr.remove(1)
    print(arr)


def run(n):
    print(str(n) + ' items:')

    a = []
    start = time.time()
    for i in range(n):
        a.append(i)
    end = time.time()
    t1 = int((end - start) * 1000)
    start = time.time()
    for i in range(n):
        a.pop(0)
    end = time.time()
    t2 = int((end - start) * 1000)
    print('[]: ' + 't add: ' + str(t1) + ', t remove: ' + str(t2))

    a = SingleArray()
    start = time.time()
    for i in range(n):
        a.add(i)
    end = time.time()
    t1 = int((end - start) * 1000)
    start = time.time()
    for i in range(n):
        a.remove(0)
    end = time.time()
    t2 = int((end - start) * 1000)
    print('SingleArray: ' + 't add: ' + str(t1) + ', t remove: ' + str(t2))

    a = VectorArray(100)
    start = time.time()
    for i in range(n):
        a.add(i)
    end = time.time()
    t1 = int((end - start) * 1000)
    start = time.time()
    for i in range(n):
        a.remove(0)
    end = time.time()
    t2 = int((end - start) * 1000)
    print('VectorArray: ' + 't add: ' + str(t1) + ', t remove: ' + str(t2))

    a = FactorArray(100 + n // 4, 500 + n // 100)
    start = time.time()
    for i in range(n):
        a.add(i)
    end = time.time()
    t1 = int((end - start) * 1000)
    start = time.time()
    for i in range(n):
        a.remove(0)
    end = time.time()
    t2 = int((end - start) * 1000)
    print('FactorArray: ' + 't add: ' + str(t1) + ', t remove: ' + str(t2))

    a = MatrixArray(10)
    start = time.time()
    for i in range(n):
        a.add(i)
    end = time.time()
    t1 = int((end - start) * 1000)
    start = time.time()
    for i in range(n):
        a.remove(0)
    end = time.time()
    t2 = int((end - start) * 1000)
    print('MatrixArray: ' + 't add: ' + str(t1) + ', t remove: ' + str(t2))


if __name__ == '__main__':
    test_array(MatrixArray, 100)
    run(1000)
    run(10000)
    run(100000)

