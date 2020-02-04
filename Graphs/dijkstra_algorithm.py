
class Dijkstra:
    inf = float('inf')

    def __init__(self, adjacency_vector, start_vertex):
        self.adjacency_vector = adjacency_vector
        self.start_vertex = start_vertex
        self.vertex_count = len(adjacency_vector)
        self.weight = [self.inf] * self.vertex_count
        self.used = [False] * self.vertex_count

    def run_algorithm(self, end_vertex=None):
        self.weight[self.start_vertex] = 0
        while True:
            mn = None
            for i in range(self.vertex_count):
                if not self.used[i]:
                    if mn is None:
                        mn = i
                    if self.weight[i] < self.weight[mn]:
                        mn = i
            if mn is None or self.weight[mn] == self.inf:
                break
            if mn == end_vertex:
                return self.weight[mn]
            for vertex, weight in self.adjacency_vector[mn]:
                if not self.used[vertex]:
                    new_weight = self.weight[mn] + weight
                    if new_weight < self.weight[vertex]:
                        self.weight[vertex] = new_weight
            self.used[mn] = True
        return None


def main():
    adjacency_vector = [
        [(1, 7.), (2, 9.), (5, 14.)],
        [(2, 10.), (3, 15.)],
        [(3, 11.), (5, 2.)],
        [(4, 6.)],
        [(5, 9)],
        [(4, 9.)]
    ]
    dijkstra = Dijkstra(adjacency_vector, 0)
    dijkstra.run_algorithm()
    print(*dijkstra.weight)
    dijkstra = Dijkstra(adjacency_vector, 0)
    print(dijkstra.run_algorithm(1))


if __name__ == '__main__':
    main()
