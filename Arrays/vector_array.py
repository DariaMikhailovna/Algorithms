from fixed_array import *


class VectorArray:
    def __init__(self, vector=10):
        self.__size = 0
        self.__array = FixedArray(0)
        self.__vector = vector

    def __str__(self):
        return str(self.__array)

    def __getitem__(self, index):
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__array[index] = value

    def size(self):
        return self.__size

    def resize(self):
        new_array = FixedArray(self.__size + self.__vector)
        FixedArray.mem_copy(self.__array, 0, new_array, 0, self.__size)
        self.__array = new_array

    def add(self, item, index=None):
        if self.__size == len(self.__array):
            self.resize()
        if index is None:
            self.__array[self.__size] = item
        else:
            t = self.__array[index]
            self.__array[index] = item
            for i in range(index + 1, self.__size + 1):
                tt = self.__array[i]
                self.__array[i] = t
                t = tt
        self.__size += 1

    def remove(self, index):
        item = self.__array[index]
        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1
        return item
