from enum import Enum
from typing import Optional
import sys
import threading
from binary_tree import main


class Color(Enum):
    RED = 0
    BLACK = 1


class Side(Enum):
    LEFT = 0
    RIGHT = 1

    @staticmethod
    def opposite(side):
        return Side.RIGHT if side == Side.LEFT else Side.LEFT


class Node:
    def __init__(self, data=None, left=None, right=None, count=1):
        self.data = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right
        self.color = Color.RED
        self.count = count

    def __getitem__(self, side):
        return self.left if side == Side.LEFT else self.right

    def __setitem__(self, side, value):
        if side == Side.LEFT:
            self.left = value
        else:
            self.right = value


class RedBlackTree:
    def __init__(self):
        self.root: Optional[Node] = None

    @staticmethod
    def get_color(node):
        if node is None:
            return Color.BLACK
        return node.color

    def search(self, data):
        return self._search_rec(data, self.root)

    def _search_rec(self, data, curr=None):
        if curr is None:
            return False
        if curr.data == data:
            return True
        if data < curr.data:
            return self._search_rec(data, curr.left)
        if data > curr.data:
            return self._search_rec(data, curr.right)

    def insert(self, data):
        self.root = self._insert_rec(data, self.root)
        if self.get_color(self.root) == Color.RED:
            self.root.color = Color.BLACK

    def _insert_rec(self, data, curr=None):
        if curr is None:
            return Node(data)
        if data == curr.data:
            curr.count += 1
            return curr
        if data < curr.data:
            curr.left = self._insert_rec(data, curr.left)
            return self.rebalance(curr, Side.LEFT)
        if data > curr.data:
            curr.right = self._insert_rec(data, curr.right)
            return self.rebalance(curr, Side.RIGHT)

    def rebalance(self, curr, side):
        op_side = Side.opposite(side)
        if self.get_color(curr[side]) == Color.RED:
            if self.get_color(curr[side][op_side]) == Color.RED:
                curr[side] = self.rotate(curr[side], side)
            if self.get_color(curr[side][side]) == Color.RED:
                if self.get_color(curr[op_side]) == Color.RED:
                    self.recolor_red(curr)
                else:
                    curr = self.rotate(curr, op_side)
                    self.recolor_black(curr)
        return curr

    @staticmethod
    def rotate(curr: Node, side):
        op_side = Side.opposite(side)
        new_root = curr[op_side]
        tmp = new_root[side]
        new_root[side] = curr
        curr[op_side] = tmp
        return new_root

    @staticmethod
    def recolor_red(curr: Node):
        curr.color = Color.RED
        curr.right.color = Color.BLACK
        curr.left.color = Color.BLACK

    @staticmethod
    def recolor_black(curr: Node):
        curr.color = Color.BLACK
        curr.right.color = Color.RED
        curr.left.color = Color.RED

    def remove(self, data):
        pass

    def _remove_rec(self, data, curr):
        pass


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(10 ** 8)
    tree1 = RedBlackTree()
    tree2 = RedBlackTree()
    t = threading.Thread(target=lambda: main(20000, tree1, tree2))
    t.start()
    t.join()