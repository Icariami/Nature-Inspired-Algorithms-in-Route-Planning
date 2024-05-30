from read_map import read_map


def get_neighbors(i, j, height, width):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < height - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < width - 1:
        neighbors.append((i, j + 1))
    return neighbors


class Graph:
    def __init__(self, map_data):
        self.nodes = {}
        self.construct_graph(map_data)

    def construct_graph(self, map_data):
        height = len(map_data)
        width = len(map_data[0])

        for i in range(height):
            for j in range(width):
                if map_data[i][j] == '.':  # if is a traversable terrain
                    self.nodes[(i, j)] = Node((i, j))

        for i in range(height):
            for j in range(width):
                if map_data[i][j] == '.':
                    current_node = self.nodes[(i, j)]
                    neighbors = get_neighbors(i, j, height, width)
                    for neighbor in neighbors:
                        if map_data[neighbor[0]][neighbor[1]] == '.':
                            current_node.neighbors.append(self.nodes[neighbor])


class Node:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.neighbors = []


def print_graph(graph):
    for node in graph.nodes.values():
        print("Node:", node.coordinates)
        print("Neighbors:", [neighbor.coordinates for neighbor in node.neighbors])
        print()


map_data = read_map('maps/A_easiest_example.map')
graph = Graph(map_data)
print_graph(graph)
