from queue_container import *


def get_strongly_connected_components(adjacency_vector):
    res_components = []
    invert_adjacency_vector = adjacency_vector[:]
    for i in range(len(adjacency_vector)):
        for j in range(len(adjacency_vector[i])):
            invert_adjacency_vector[i][j] = ~adjacency_vector[i][j] + 1
    return res_components


def deep_search():
    pass


if __name__ == '__main__':
    adjacency_vector = [
        [-1, +4],
        [+0, -2, -4, -5],
        [+1, -3, +3, -6],
        [-2, +2, -7, +7],
        [-0, +1, -5],
        [+1, -4, -6, +6],
        [+2, -5, +5, +7],
        [-3, +3, -6]
    ]
    results = get_strongly_connected_components(adjacency_vector)
    for res in results:
        print(*res)
