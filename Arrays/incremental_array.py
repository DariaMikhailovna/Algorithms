from fixed_array import *


class IncrementalArray:
    def __init__(self, reserved_size):
        self.__size = 0
        self.__array = FixedArray(reserved_size)

    def __str__(self):
        return str(self.__array[:self.__size])

    def __getitem__(self, index):
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__array[index] = value

    def size(self):
        return self.__size

    def _next_size(self):
        raise NotImplementedError()

    def resize(self):
        new_array = FixedArray(self._next_size())
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
