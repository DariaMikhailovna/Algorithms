from Hash.binary_object_tree import BinaryTree
from copy import deepcopy


class HashTable:
    def __init__(self):
        self.__data = []
        self._resize(10)
        self.__size = 0

    def __setitem__(self, key, value):
        self.__size += 1
        if self.__size > len(self.__data):
            self._resize(2 * len(self.__data))
        index = self._get_hash(key)
        if type(self.__data[index]) == list:
            exists = False
            for i, x in enumerate(self.__data[index]):
                if x[0] == key:
                    exists = True
                    self.__data[index][i] = (key, value)
                    self.__size -= 1
                    break
            if not exists:
                self.__data[index].append((key, value))
            if len(self.__data[index]) >= 32:
                arr = self.__data[index]
                bst = BinaryTree()
                for key, value in arr:
                    bst[key] = value
                self.__data[index] = bst
        else:
            if not self.__data[index].insert(key, value):
                self.__size -= 1

    def __getitem__(self, key):
        index = self._get_hash(key)
        if type(self.__data[index]) == BinaryTree:
            return self.__data[index][key]
        for x in self.__data[index]:
            if x[0] == key:
                return x[1]
        raise KeyError()

    def __delitem__(self, key):
        index = self._get_hash(key)
        if type(self.__data[index]) == BinaryTree:
            del self.__data[index][key]
            self.__size -= 1
            return
        for i in range(len(self.__data[index])):
            if self.__data[index][i][0] == key:
                del self.__data[index][i]
                self.__size -= 1
                return
        raise KeyError()

    def _get_hash(self, key):
        return int(key) % len(self.__data)

    def _resize(self, new_size):
        arr = deepcopy(self.__data)
        self.__data = [[] for _ in range(new_size)]
        self.__size = 0
        for x in arr:
            for key, value in x:
                self[key] = value


if __name__ == '__main__':
    h = HashTable()
    for i in range(35):
        h[i] = i
    for i in range(35):
        h[i] = i + 1
        t = h[i]
    for i in range(35):
        print(h[i])
    for i in range(35):
        del h[i]
