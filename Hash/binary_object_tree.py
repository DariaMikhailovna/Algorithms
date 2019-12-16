from typing import Optional


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data: Optional[()] = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, data):
        self.root = self._insert_rec(data, self.root)

    def _insert_rec(self, data, curr=None):
        if curr is None:
            return Node(data)
        if data[0] == curr.data[0]:
            curr[1] = data[1]
            return curr
        if data[0] < curr.data[0]:
            curr.left = self._insert_rec(data, curr.left)
            return curr
        if data[0] > curr.data[0]:
            curr.right = self._insert_rec(data, curr.right)
            return curr

    def search(self, key):
        return self._search_rec(key, self.root)

    def _search_rec(self, key, curr=None):
        if curr is None:
            return None
        if curr.data[0] == key:
            return curr
        if key < curr.data[0]:
            return self._search_rec(key, curr.left)
        if key > curr.data[0]:
            return self._search_rec(key, curr.right)

    def remove(self, key):
        self.root = self._remove_rec(key, self.root)

    def _remove_rec(self, key, curr):
        if curr is None:
            return None
        if key < curr.data[0]:
            curr.left = self._remove_rec(key, curr.left)
            return curr
        if key > curr.data[0]:
            curr.right = self._remove_rec(key, curr.right)
            return curr
        if curr.left is None:
            return curr.right
        else:
            res = curr.left
            tmp = curr.right
            curr = curr.left
            while curr.right:
                curr = curr.right
            curr.right = tmp
            return res
