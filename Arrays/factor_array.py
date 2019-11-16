from fixed_array import *


class FactorArray:
    def __init__(self, factor=100, init_length=1):
        self.__size = 0
        self.__array = FixedArray(init_length)
        self.__factor = factor

    def __str__(self):
        return str(self.__array[:self.__size])

    def __getitem__(self, index):
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__array[index] = value

    def size(self):
        return self.__size

    def resize(self):
        new_array = FixedArray(self.__size + (self.__size * self.__factor + 99) // 100)
        FixedArray.mem_copy(self.__array, 0, new_array, 0, self.__size)
        self.__array = new_array

    def add(self, item, index=None):
        if self.__size == len(self.__array):
            self.resize()
        if index is None:
            self.__array[self.__size] = item
        else:
            for i in range(self.__size, index, -1):
                self.__array[i] = self.__array[i - 1]
            self.__array[index] = item
        self.__size += 1

    def remove(self, index):
        item = self.__array[index]
        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1
        return item
