from single_array import *
from vector_array import *


class StaticVector(IncrementalArray):
    def __init__(self, reserved_size):
        super().__init__(reserved_size)

    def _next_size(self):
        raise NotImplementedError("StaticVector should never reallocate memory")


class MatrixArray:

    def __init__(self, vector=100):
        self.__size = 0
        self.__vector = vector
        self.__array = SingleArray()

    def __repr__(self):
        return repr(self.__array)

    def __getitem__(self, index):
        return self.__array[index // self.__vector][index % self.__vector]

    def size(self):
        return self.__size

    def add(self, item, index=None):
        if self.__size == self.__array.size() * self.__vector:
            self.__array.add(StaticVector(self.__vector))
        if index is not None:
            row = index // self.__vector
            column = index % self.__vector
            for i in range(self.__array.size() - 1, row, -1):
                t = self.__array[i - 1].remove(self.__vector - 1)
                self.__array[i].add(t, 0)
            self.__array[row].add(item, column)
        else:
            index = self.__size
            self.__array[index // self.__vector].add(item)
        self.__size += 1

    def remove(self, index):
        row = index // self.__vector
        column = index % self.__vector
        self.__array[row].remove(column)
        for i in range(row + 1, self.__array.size()):
            t = self.__array[i].remove(0)
            self.__array[i - 1].add(t, self.__vector - 1)
        self.__size -= 1
        if self.__array[self.__array.size() - 1].size() == 0:
            self.__array.remove(self.__array.size() - 1)
