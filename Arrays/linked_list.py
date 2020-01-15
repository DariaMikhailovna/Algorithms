from typing import Optional


class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first: Optional[Item] = None
        self.last: Optional[Item] = None

    def push_front(self, value):
        item = Item(value)
        item.next = self.first
        self.first = item

    def push_back(self, value):
        item = Item(value)
        if not self.first:
            self.first = item
            self.last = item
            return
        self.last.next = item
        self.last = item

    def pop_front(self):
        if not self.first:
            raise IndexError()
        res = self.first.value
        self.first = self.first.next
        return res

