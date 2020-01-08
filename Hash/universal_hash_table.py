from hash_table import *
from universal_hash import *


class UnivHashTable(HashTable):
    def __init__(self):
        self._get_hash = None
        super().__init__()

    def _resize(self, new_size):
        self._get_hash = UnivHash(new_size)
        super()._resize(new_size)


if __name__ == '__main__':
    uh = UnivHashTable()
    for i in range(30):
        uh[i] = i + 1
    for i in range(3):
        print(uh[i])
