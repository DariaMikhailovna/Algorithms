class Edge:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def __str__(self):
        return str((self.x, self.y, self.weight))


class DSU:
    def __init__(self, vertex_count):
        self.pr = [i for i in range(vertex_count)]
        self.size = [1] * vertex_count

    def unite(self, u, v):
        u = self.get_root(u)
        v = self.get_root(v)
        if u == v:
            return False
        if self.size[u] > self.size[v]:
            u, v = v, u
        self.pr[u] = v
        self.size[v] += self.size[u]
        return True

    def get_root(self, vertex):
        if self.pr[vertex] == vertex:
            return vertex
        self.pr[vertex] = self.get_root(self.pr[vertex])
        return self.pr[vertex]


class Kruskal:
    def __init__(self, adjacency_vector):
        self.edges = []
        for i in range(len(adjacency_vector)):
            for vertex, weight in adjacency_vector[i]:
                edge = Edge(i, vertex, weight)
                self.edges.append(edge)
        self.edges_count = len(self.edges)
        self.dsu = DSU(len(adjacency_vector))

    def run_algorithm(self):
        self.edges.sort(key=lambda edge: edge.weight)
        ostov = []
        for edge in self.edges:
            if self.dsu.unite(edge.x, edge.y):
                ostov.append(edge)
        return ostov


def main():
    adjacency_vector = [
        [(1, 7), (2, 9), (5, 14)],
        [(0, 7), (2, 10), (3, 15)],
        [(0, 9), (1, 10), (3, 11), (5, 2)],
        [(1, 15), (2, 11), (4, 6)],
        [(3, 6), (5, 9)],
        [(0, 14), (2, 2), (4, 9)]
    ]
    kruskal = Kruskal(adjacency_vector)
    result = kruskal.run_algorithm()
    print(*result)


if __name__ == '__main__':
    main()
