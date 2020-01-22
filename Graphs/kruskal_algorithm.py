class Edge:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight


class Kruskal:
    def __init__(self, adjacency_vector):
        self.edges = []
        for i in range(len(adjacency_vector)):
            for vertex, weight in adjacency_vector[i]:
                edge = Edge(i, vertex, weight)
                self.edges.append(edge)
        self.edges_count = len(self.edges)
        self.pr = [i for i in range(self.edges_count)]

    def sort(self):
        new_edges = []
        mn = (None, None, float('inf'))
        while len(new_edges) < self.edges_count:
            j = None
            for i in range(self.edges_count):

                if self.edges[i].weight < mn[2]:
                    j = i
                    mn = (self.edges[i].x, self.edges[i].y, self.edges[i].weight)
            self.edges[j] = Edge(None, None, float('inf'))
            new_edges.append(Edge(mn[0], mn[1], mn[2]))
            mn = (None, None, float('inf'))
        self.edges = new_edges

    def run_algorithm(self):
        self.sort()
        ostov = []
        for edge in self.edges:
            if self.get_root(edge.x) != self.get_root(edge.y):
                self.unite(edge.x, edge.y)
                ostov.append(edge)
        return ostov

    def unite(self, u, v):
        u = self.get_root(u)
        v = self.get_root(v)
        # if u.size > v.size:
        #     u, v = v, u
        # self.pr[u] = v
        # v.size += u.size
        self.pr[u] = v

    def get_root(self, vertex):
        if self.pr[vertex] == vertex:
            return vertex
        self.pr[vertex] = self.get_root(self.pr[vertex])
        return self.pr[vertex]


def main():
    adjacency_vector = [
        [(1, 7.), (3, 5.)],
        [(2, 8.), (3, 9.), (4, 7.)],
        [(4, 5.)],
        [(4, 15.), (5, 6.)],
        [(5, 8.), (6, 9,)],
        [(6, 11.)]
    ]
    kruskal = Kruskal(adjacency_vector)
    result = kruskal.run_algorithm()
    print(*result)


if __name__ == '__main__':
    main()
