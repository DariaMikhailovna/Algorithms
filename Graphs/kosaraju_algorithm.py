
class DFS:
    def __init__(self, adjacency_vector):
        self.adjacency_vector = adjacency_vector
        self.size = len(adjacency_vector)
        self.used = [False] * self.size
        self.order = []

    def dfs(self, vertex):
        self.used[vertex] = True
        for next_vertex in self.adjacency_vector[vertex]:
            if not self.used[next_vertex]:
                self.dfs(next_vertex)
        self.order.append(vertex)


def inverse(vector):
    size = len(vector)
    invert_vector = [[] for i in range(size)]
    for i in range(size):
        for j in range(len(vector[i])):
            invert_vector[vector[i][j]].append(i)
    return invert_vector


def get_strongly_connected_components(adjacency_vector):
    res_components = []
    dfs = DFS(inverse(adjacency_vector))
    for i in range(len(adjacency_vector)):
        if not dfs.used[i]:
            dfs.dfs(i)
    order = list(reversed(dfs.order))
    dfs = DFS(adjacency_vector)
    for vertex in order:
        if not dfs.used[vertex]:
            dfs.dfs(vertex)
            res_components.append(dfs.order)
            dfs.order = []
    return res_components


def main():
    adjacency_vector = [
        [1],
        [2, 4, 5],
        [3, 6],
        [2, 7],
        [0, 5],
        [6],
        [5],
        [3, 6]
    ]
    # adjacency_vector = [
    #     [1],
    #     [0]
    # ]
    # adjacency_vector = [
    #     [1, 2],
    #     [0],
    #     []
    # ]
    # adjacency_vector = [
    #     [1, 2],
    #     [0, 2],
    #     [1]
    # ]
    results = get_strongly_connected_components(adjacency_vector)
    for res in results:
        print(*res)


if __name__ == '__main__':
    main()
