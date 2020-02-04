from math import sqrt


class AStar:
    inf = float('inf')

    def __init__(self, adjacency_vector, start_vertex, end_vertex, list_coords, coef=1):
        self.adjacency_vector = adjacency_vector
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.vertex_count = len(adjacency_vector)
        self.list_coords = list_coords
        self.weight = [self.inf] * self.vertex_count
        self.used = [False] * self.vertex_count
        self.coef = coef

    def get_distance(self, vertex):
        delta_x = self.list_coords[vertex][0] - self.list_coords[self.end_vertex][0]
        delta_y = self.list_coords[vertex][1] - self.list_coords[self.end_vertex][1]
        return sqrt(delta_x ** 2 + delta_y ** 2) * self.coef

    def run_algorithm(self):
        self.weight[self.start_vertex] = 0
        while True:
            mn = None
            for i in range(self.vertex_count):
                if not self.used[i]:
                    if mn is None:
                        mn = i
                    if self.weight[i] + self.get_distance(i) < self.weight[mn] + self.get_distance(mn):
                        mn = i
            if mn is None or self.weight[mn] == self.inf:
                break
            if mn == self.end_vertex:
                return self.weight[mn]
            for vertex, weight in self.adjacency_vector[mn]:
                if not self.used[vertex]:
                    new_weight = self.weight[mn] + weight
                    if new_weight < self.weight[vertex]:
                        self.weight[vertex] = new_weight
                        self.used[vertex] = False  # для правильной работы при плохой эвристике
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
    list_coords = [(0, 0), (0, 1), (2, 3), (5, 2), (6, 1), (4, 7)]
    a_star = AStar(adjacency_vector, 0, 4, list_coords)
    print(a_star.run_algorithm())


if __name__ == '__main__':
    main()
