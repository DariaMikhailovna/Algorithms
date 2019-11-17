class FixedArray:
    def __init__(self, size):
        self.__size = size
        self.__array = [None] * size

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__array[index] = value

    def __repr__(self):
        return repr(self.__array)

    @staticmethod
    def mem_copy(array_from, index_from, array_to, index_to, size):
        for i in range(size):
            array_to[index_to + i] = array_from[index_from + i]
