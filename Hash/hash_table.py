from Hash.binary_object_tree import BinaryTree
from copy import deepcopy


class HashTable:
    def __init__(self):
        self.data = [[] for _ in range(10)]
        self.size = 0

    def __setitem__(self, key, value):
        self.size += 1
        if self.size > len(self.data):
            self.resize()
        index = self.get_hash(key)
        if type(self.data[index]) == list:
            is_exists = False
            for x in self.data[index]:
                if x[0] == key:
                    is_exists = True
                    x = (key, value)
                    self.size -= 1
                    break
            if not is_exists:
                self.data[index].append((key, value))
            if len(self.data[index]) >= 32:
                arr = self.data[index]
                bst = BinaryTree()
                for i in range(len(arr)):
                    bst.insert(arr[i])
                self.data[index] = bst
        else:
            self.data[index].insert((key, value))

    def __getitem__(self, key):
        index = self.get_hash(key)
        if type(self.data[index]) == BinaryTree:
            item = self.data[index].search(key)
            if item:
                return item[1]
            else:
                raise KeyError()
        for x in self.data[index]:
            if x[0] == key:
                return x[1]
        raise KeyError()

    def remove(self, key):
        index = self.get_hash(key)
        if type(self.data[index]) == BinaryTree:
            if not self.data[index].search(key):
                raise KeyError()
            self.data[index].remove(key)
            return
        for i in range(len(self.data[index])):
            if self.data[index][i][0] == key:
                del self.data[index][i]
                self.size -= 1
                return
        raise KeyError()

    def get_hash(self, key):
        return int(key) % len(self.data)

    def resize(self):
        arr = deepcopy(self.data)
        self.data = [[] for _ in range(2 * len(self.data))]
        for x in arr:
            for y in x:
                self.__setitem__(y[0], y[1])


if __name__ == '__main__':
    h = HashTable()
    for i in range(12):
        h[i] = i
    for i in range(12):
        h[i] = i + 1
        t = h[i]
