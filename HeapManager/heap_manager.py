# менеджер для массивов интов. Использован метод First fit
class HeapManager:
    class BlocksList:
        def __init__(self, total_memory):
            self.first_item = Item(self, 0, total_memory, True)

        def __iter__(self):
            curr_item = self.first_item
            while curr_item:
                yield curr_item
                curr_item = curr_item.next

    def __init__(self, total_memory):
        self.__total_memory = total_memory
        self.__data = [0] * total_memory
        self.__blocks = self.BlocksList(total_memory)

    def __repr__(self):
        return '[' + ', '.join(map(repr, self.__blocks)) + ']'

    def debug(self):
        return str(list(self.__data))

    def allocate(self, array_size):
        for curr_item in self.__blocks:
            if curr_item.is_free and len(curr_item) >= array_size:
                return self.__allocate_from(curr_item, array_size)
        raise MemoryError()

    def __allocate_from(self, curr_item, array_size):
        if not curr_item.is_free:
            raise AssertionError("Bad use of __allocate_from")
        if len(curr_item) > array_size:
            return Array(curr_item.split(array_size), self.__data)
        elif len(curr_item) == array_size:
            curr_item.is_free = False
            return Array(curr_item, self.__data)
        else:
            raise AssertionError("Bad use of __allocate_from")

    def add_memory(self, count_memory):
        self.__data.extend([0] * count_memory)


class Item:
    next = None
    prev = None

    def __init__(self, container, start, end, is_free):
        self.container = container
        self.start = start
        self.end = end
        self.is_free = is_free

    def __repr__(self):
        return str((self.start, self.end, self.is_free))

    def free(self):
        self.is_free = True
        if self.prev and self.prev.is_free:
            self.start = self.prev.start
            self.prev = self.prev.prev
            if self.prev:
                self.prev.next = self
            else:
                self.container.first_item = self
        if self.next and self.next.is_free:
            self.end = self.next.end
            self.next = self.next.next
            if self.next:
                self.next.prev = self

    def split(self, array_size):
        item = Item(self.container, self.start, self.start + array_size, False)
        if self.prev:
            self.prev.next = item
            item.prev = self.prev
        else:
            self.container.first_item = item
        item.next = self
        self.prev = item
        self.start += array_size
        return item

    def __len__(self):
        return self.end - self.start


class Array:
    def __init__(self, item, data):
        self.__item: Item = item
        self.__data = data

    def __setitem__(self, key, value):
        self.__data[self.__item.start + key] = value

    def __getitem__(self, key):
        return self.__data[self.__item.start + key]

    def __del__(self):
        self.__item.free()

    def __len__(self):
        return len(self.__item)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __str__(self):
        return str(list(self))

    def fill(self, value):
        for i in range(len(self)):
            self[i] = value


def test():
    class Tester:
        def __init__(self, size):
            self.manager = HeapManager(size)
            self.id = 1
            self.arrays = {}
            self.debug()

        def debug(self):
            print(self.manager.debug())
            print(repr(self.manager))

        def allocate(self, size):
            curr_id = self.id
            self.id += 1
            print(f'array #{curr_id} = allocate {size} elements')
            self.arrays[curr_id] = self.manager.allocate(size)
            self.arrays[curr_id].fill(curr_id)
            self.debug()
            return curr_id

        def free(self, curr_id):
            print(f'free array #{curr_id}')
            self.arrays[curr_id].fill(0)
            del self.arrays[curr_id]
            self.debug()

    tester = Tester(10)
    arr = tester.allocate(2)
    tester.free(arr)
    arr = tester.allocate(2)
    tester.free(arr)
    arr = tester.allocate(10)
    tester.free(arr)
    try:
        arr = tester.allocate(11)
        tester.free(arr)
    except MemoryError:
        print('MemoryError')
    arr = tester.allocate(5)
    arr2 = tester.allocate(5)
    tester.free(arr)
    tester.free(arr2)
    arr1 = tester.allocate(3)
    arr2 = tester.allocate(3)
    arr3 = tester.allocate(3)
    tester.free(arr2)
    try:
        arr = tester.allocate(4)
        tester.free(arr)
    except MemoryError:
        print('MemoryError')
    arr4 = tester.allocate(2)
    tester.free(arr4)
    tester.free(arr3)
    arr5 = tester.allocate(1)
    arr6 = tester.allocate(4)
    tester.free(arr5)
    arr7 = tester.allocate(2)
    tester.free(arr6)
    tester.free(arr7)
    tester.free(arr1)


if __name__ == '__main__':
    test()
