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
            exists = False
            for i, x in enumerate(self.data[index]):
                if x[0] == key:
                    exists = True
                    self.data[index][i] = (key, value)
                    self.size -= 1
                    break
            if not exists:
                self.data[index].append((key, value))
            if len(self.data[index]) >= 0:
                arr = self.data[index]
                bst = BinaryTree()
                for i in range(len(arr)):
                    bst.insert(*arr[i])
                self.data[index] = bst
        else:
            if not self.data[index].insert(key, value):
                self.size -= 1

    def __getitem__(self, key):
        index = self.get_hash(key)
        if type(self.data[index]) == BinaryTree:
            item = self.data[index].search(key)
            if item:
                return item.value
            else:
                raise KeyError()
        for x in self.data[index]:
            if x[0] == key:
                return x[1]
        raise KeyError()

    def remove(self, key):
        index = self.get_hash(key)
        if type(self.data[index]) == BinaryTree:
            if not self.data[index].remove(key):
                raise KeyError()
            self.size -= 1
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
        self.size = 0
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
