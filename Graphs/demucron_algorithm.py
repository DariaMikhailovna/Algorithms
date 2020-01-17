class DemucronAlgorithm:
    def __init__(self, adjacency_vector):
        self.adjacency_vector = adjacency_vector
        self.degree = [0] * len(adjacency_vector)
        self.next_null = []
        self.set_degree()
        self.set_next_null()

    def set_degree(self):
        for i in range(len(self.adjacency_vector)):
            for j in range(len(self.adjacency_vector[i])):
                self.degree[self.adjacency_vector[i][j]] += 1

    def set_next_null(self):
        for i in range(len(self.degree)):
            if self.degree[i] == 0:
                self.next_null.append(i)

    def run_algorithm(self):
        result = []
        while len(self.next_null) != 0:
            next_null = []
            result.append(self.next_null)
            for next in self.next_null:
                for vertex in self.adjacency_vector[next]:
                    self.degree[vertex] -= 1
                    if self.degree[vertex] == 0:
                        next_null.append(vertex)
            self.next_null = next_null
        return result


def main():
    adjacency_vector = [
        [1, 2],
        [3],
        [3],
        []
    ]
    # adjacency_vector = [
    #     [1, 2],
    #     [2, 3],
    #     [3],
    #     []
    # ]
    demucron = DemucronAlgorithm(adjacency_vector)
    results = demucron.run_algorithm()
    for res in results:
        print(*res)


if __name__ == '__main__':
    main()
