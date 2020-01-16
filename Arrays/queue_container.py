from linked_list import *


class QueueContainer:
    def __init__(self):
        self.__array = LinkedList()

    def __len__(self):
        return len(self.__array)

    def push(self, item):
        self.__array.push_back(item)

    def pop(self):
        return self.__array.pop_front()

