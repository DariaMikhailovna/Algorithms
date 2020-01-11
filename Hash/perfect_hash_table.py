from universal_hash import *


class PerfectHashTableKeyError(KeyError):
    pass


class SimpleHashTable:
    def __init__(self, size):
        self.get_second_hash = UnivHash(size)
        self.__size = size
        self.data = [None] * size

    def __setitem__(self, key, value):
        second_hash = self.get_second_hash(key)
        assert self.data[second_hash][0] == key
        self.data[second_hash] = (key, value)

    def __getitem__(self, key):
        second_hash = self.get_second_hash(key)
        assert self.data[second_hash][0] == key
        return self.data[second_hash][1]

    def __delitem__(self, key):
        second_hash = self.get_second_hash(key)
        assert self.data[second_hash][0] == key
        self.data[second_hash] = (key, None)


class PerfectHashTable:
    def __init__(self, keys):
        self.__keys_count = len(keys)
        self.__data = [[] for _ in range(self.__keys_count)]
        self.__size = 0
        self.__keys = keys
        self.get_first_hash = UnivHash(self.__keys_count)
        self.build()

    def __setitem__(self, key, value):
        self.__size += 1
        first_hash = self.get_first_hash(key)
        if type(self.__data[first_hash]) is SimpleHashTable:
            second_hash = self.__data[first_hash].get_second_hash(key)
            assert self.__data[first_hash].data[second_hash][0] == key
            self.__data[first_hash].data[second_hash] = (key, value)
        else:
            assert self.__data[first_hash][0] == key
            self.__data[first_hash] = (key, value)

    def __getitem__(self, key):
        first_hash = self.get_first_hash(key)
        data = self.__data[first_hash]
        if data is None:
            raise PerfectHashTableKeyError
        if type(data) is SimpleHashTable:
            return data[key]
        else:
            return data[1]

    def __delitem__(self, key):
        first_hash = self.get_first_hash(key)
        data = self.__data[first_hash]
        if data is None:
            raise PerfectHashTableKeyError
        if type(data) is SimpleHashTable:
            del self.__data[first_hash][key]
        else:
            self.__data[first_hash] = (key, None)

    def build(self):
        for key in self.__keys:
            first_hash = self.get_first_hash(key)
            self.__data[first_hash].append(key)
        for i in range(self.__keys_count):
            size = len(self.__data[i])
            if size == 0:
                self.__data[i] = None
            elif size == 1:
                self.__data[i] = (self.__data[i][0], None)
            else:
                keys = self.__data[i]
                size = size * size
                while True:
                    flag = True
                    self.__data[i] = SimpleHashTable(size)
                    for key in keys:
                        second_hash = self.__data[i].get_second_hash(key)
                        if self.__data[i].data[second_hash] is None:
                            self.__data[i].data[second_hash] = (key, None)
                        else:
                            flag = False
                            break
                    if flag:
                        break


if __name__ == '__main__':
    pht = PerfectHashTable(range(0, 100))
    for i in range(31):
        pht[i] = i + 1
    for i in range(10):
        del pht[i]
    for i in range(30):
        print(pht[i])
    print(pht[101])
