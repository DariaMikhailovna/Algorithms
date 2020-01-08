import random


class UnivHash:
    p = 2305843009213693951  # 9е простое число Мерсенна

    def __init__(self, m):
        self.m = m
        self.a = random.randint(0, self.p - 1)
        self.b = random.randint(1, self.p - 1)

    def __call__(self, key):
        if not 0 <= key < self.p:
            raise KeyError(f"Key should be in range [0, {self.p - 1}]: {key}")
        return ((self.a * key + self.b) % self.p) % self.m
