from incremental_array import *


class QueueContainer:

    def __init__(self):
        self.__array = IncrementalArray(10)

    def push(self, item):
        self.__array.add(item)

    def pop(self):
        item = self.__array[0]
        self.__array.remove(0)
        return item
