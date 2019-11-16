from single_array import *
from vector_array import *
from factor_array import *
from matrix_array import *
from linked_list import *
from double_linked_list import *
from stack import *
from queue_container import *

import time


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


if __name__ == '__main__':
    run(1000)
    run(10000)
    run(100000)

