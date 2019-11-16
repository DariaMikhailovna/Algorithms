from incremental_array import *


class FactorArray(IncrementalArray):
    def __init__(self, factor=100, init_length=1):
        super().__init__(init_length)
        self.__factor = factor

    def _next_size(self):
        return self.size() + (self.size() * self.__factor + 99) // 100
