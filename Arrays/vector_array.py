from incremental_array import *


class VectorArray(IncrementalArray):
    def __init__(self, vector=10):
        super().__init__(0)
        self.__vector = vector

    def _next_size(self):
        return self.size() + self.__vector
