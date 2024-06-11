import numpy as np


class Node:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.neighbors = []

    def __str__(self):
        return f"{self.coordinates}"

    def distance_to(self, other_node):
        return np.sqrt((self.coordinates[0] - other_node.coordinates[0]) ** 2 + (
                self.coordinates[1] - other_node.coordinates[1]) ** 2)

    def get_neighbors(self, i, j, height, width):
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
