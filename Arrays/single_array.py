from fixed_array import *


class SingleArray:
    def __init__(self):
        self.__size = 0
        self.__array = FixedArray(0)

    def __repr__(self):
        return repr(self.__array)

    def __getitem__(self, index):
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__array[index] = value

    def size(self):
        return self.__size

    def add(self, item, index=None):
        if index is None:
            index = self.__size
        new_array = FixedArray(self.__size + 1)
        FixedArray.mem_copy(self.__array, 0, new_array, 0, index)
        new_array[index] = item
        FixedArray.mem_copy(self.__array, index, new_array, index + 1, self.__size - index)
        self.__size += 1
        self.__array = new_array

    def remove(self, index):
        item = self.__array[index]
        new_array = FixedArray(self.__size - 1)
        FixedArray.mem_copy(self.__array, 0, new_array, 0, index)
        FixedArray.mem_copy(self.__array, index + 1, new_array, index, self.__size - index - 1)
        self.__size -= 1
        self.__array = new_array
        return item
