from typing import Optional


class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self._root: Optional[Node] = None

    def __iter__(self):
        return self._iter_rec(self._root)

    def _iter_rec(self, curr):
        if curr is None:
            return
        for key, value in self._iter_rec(curr.left):
            yield key, value
        yield curr.key, curr.value
        for key, value in self._iter_rec(curr.right):
            yield key, value

    def __setitem__(self, key, value):
        self.insert(key, value)

    def insert(self, key, value):
        self._root, ret = self._insert_rec(key, value, self._root)
        return ret

    def _insert_rec(self, key, value, curr=None):
        if curr is None:
            return Node(key, value), True
        if key == curr.key:
            curr.value = value
            return curr, False
        if key < curr.key:
            curr.left, ret = self._insert_rec(key, value, curr.left)
            return curr, ret
        if key > curr.key:
            curr.right, ret = self._insert_rec(key, value, curr.right)
            return curr, ret

    def __getitem__(self, key):
        item = self.search(key)
        if item is None:
            raise KeyError()
        return item.key

    def search(self, key):
        return self._search_rec(key, self._root)

    def _search_rec(self, key, curr=None):
        if curr is None:
            return None
        if curr.key == key:
            return curr
        if key < curr.key:
            return self._search_rec(key, curr.left)
        if key > curr.key:
            return self._search_rec(key, curr.right)

    def __delitem__(self, key):
        if not self.remove(key):
            raise KeyError()

    def remove(self, key):
        self._root, ret = self._remove_rec(key, self._root)
        return ret

    def _remove_rec(self, key, curr):
        if curr is None:
            return None, False
        if key < curr.key:
            curr.left, ret = self._remove_rec(key, curr.left)
            return curr, ret
        if key > curr.key:
            curr.right, ret = self._remove_rec(key, curr.right)
            return curr, ret
        if curr.left is None:
            return curr.right, True
        else:
            res = curr.left
            tmp = curr.right
            curr = curr.left
            while curr.right:
                curr = curr.right
            curr.right = tmp
            return res, True
