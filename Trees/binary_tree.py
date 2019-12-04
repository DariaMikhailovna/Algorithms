import random as rnd
from time import time
import sys
import threading


class Node:
    def __init__(self, data=None, left=None, right=None, count=1):
        self.data = data
        self.left = left
        self.right = right
        self.count = count


class BinaryTree:
    def __init__(self, data=None):
        self.root: Node = data

    def insert(self, data):
        self.root = self._insert_rec(data, self.root)

    def _insert_rec(self, data, curr=None):
        if curr is None:
            return Node(data)
        if data == curr.data:
            curr.count += 1
            return curr
        if data < curr.data:
            curr.left = self._insert_rec(data, curr.left)
            return curr
        if data > curr.data:
            curr.right = self._insert_rec(data, curr.right)
            return curr

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

    def remove(self, data):
        self.root = self._remove_rec(data, self.root)

    def _remove_rec(self, data, curr):
        if curr is None:
            return None
        if data < curr.data:
            curr.left = self._remove_rec(data, curr.left)
            return curr
        if data > curr.data:
            curr.right = self._remove_rec(data, curr.right)
            return curr
        if curr.count > 1:
            curr.count -= 1
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


def add_rnd_numbers(tree, count_numbers):
    for i in range(count_numbers):
        rnd_number = rnd.randint(0, count_numbers)
        tree.insert(rnd_number)


def add_sorted_numbers(tree, count_numbers):
    for i in range(count_numbers):
        tree.insert(i)


def search_numbers(tree, count_numbers):
    for i in range(count_numbers):
        rnd_number = rnd.randint(0, count_numbers * 10)
        tree.search(rnd_number)


def remove_numbers(tree, count_numbers):
    for i in range(count_numbers):
        rnd_number = rnd.randint(0, count_numbers * 10)
        tree.remove(rnd_number)


def get_work_time(function, tree, count_numbers):
    start = time()
    function(tree, count_numbers)
    end = time()
    return round(end - start, 5)


def main(count_numbers):
    tree_sort = BinaryTree()
    tree_rnd = BinaryTree()
    print(f'Добавление {count_numbers} элементов:')
    work_time = get_work_time(add_rnd_numbers, tree_rnd, count_numbers)
    print('В случайном порядке: ' + str(work_time) + ' секунд')
    work_time = get_work_time(add_sorted_numbers, tree_sort, count_numbers)
    print('В возрастающем порядке: ' + str(work_time) + ' секунд')
    print()

    print(f'Искать {count_numbers} элементов:')
    work_time = get_work_time(search_numbers, tree_rnd, count_numbers // 10)
    print('В случайном порядке: ' + str(work_time) + ' секунд')
    work_time = get_work_time(search_numbers, tree_sort, count_numbers // 10)
    print('В возрастающем порядке: ' + str(work_time) + ' секунд')
    print()

    print(f'Удалить {count_numbers} элементов:')
    work_time = get_work_time(remove_numbers, tree_rnd, count_numbers // 10)
    print('В случайном порядке: ' + str(work_time) + ' секунд')
    work_time = get_work_time(remove_numbers, tree_sort, count_numbers // 10)
    print('В возрастающем порядке: ' + str(work_time) + ' секунд')
    print()


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    threading.stack_size(10 ** 8)
    t = threading.Thread(target=lambda: main(20000))
    t.start()
    t.join()
