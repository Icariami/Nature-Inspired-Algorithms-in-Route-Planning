from read_map import read_map
from Node import Node


class Graph:
    def __init__(self, map_data):
        self.edges = set()
        self.nodes = {}
        self.pheromones = {}
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
                    neighbors = current_node.get_neighbors(i, j, height, width)
                    for neighbor in neighbors:
                        if map_data[neighbor[0]][neighbor[1]] == '.':
                            current_node.neighbors.append(self.nodes[neighbor])
        self.edges = self.get_edges()
        self.initialize_pheromones()

    def get_edges(self):
        edges = set()
        for node in self.nodes.values():
            for neighbor in node.neighbors:
                if (node, neighbor) not in edges and (neighbor, node) not in edges:
                    edges.add((node, neighbor))
        return sorted(edges, key=lambda edge: (edge[0].coordinates, edge[1].coordinates))

    def initialize_pheromones(self):
        for edge in self.edges:
            self.pheromones[edge] = 1.0

    def print_graph(self):
        for node in self.nodes.values():
            print("Node:", node.coordinates)
            print("Neighbors:", [neighbor.coordinates for neighbor in node.neighbors])
            print()

    def print_edges(self):
        print("\nEdges:")
        for edge in self.edges:
            print(f"{edge[0]} -> {edge[1]}")




