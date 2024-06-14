import numpy as np
import random

from visualize import visualize_grid


class ACO:
    def __init__(self, grid, ants=10, alpha=1.0, beta=2.0, evaporation=0.5, iterations=100):
        self.grid = grid
        self.ants = ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.iterations = iterations
        self.pheromone = np.ones(grid.shape)

    def heuristic(self, start, end):
        return np.linalg.norm(np.array(start) - np.array(end))

    def find_path(self, start, end):
        all_paths = []
        for iteration in range(self.iterations):
            if iteration % 100 == 0:
                print(iteration/100, "of", self.iterations/100)

            for _ in range(self.ants):
                path = self.construct_path(start, end)
                if path:
                    all_paths.append((path, self.path_length(path)))

            all_paths.sort(key=lambda x: x[1])
            self.update_pheromone(all_paths)

        if len(all_paths) == 0:
            return None
        best_path, _ = all_paths[0]
        return best_path

    def construct_path(self, start, end):
        path = [start]
        while path[-1] != end:
            current = path[-1]
            neighbors = self.get_neighbors(current)
            moves = [(neighbor, self.move_probability(current, neighbor, end, path))
                     for neighbor in neighbors if neighbor not in path]

            if not moves:
                return None

            next_move = random.choices([move[0] for move in moves], weights=[max(min(move[1], 10**10), 0.001) for move in moves])[0]
            path.append(next_move)

        return path

    def move_probability(self, current, neighbor, end, path):
        tau = self.pheromone[neighbor]
        with np.errstate(divide='ignore'):
            eta = 1 / self.heuristic(neighbor, end)

        result = (tau ** self.alpha) * (eta ** self.beta)
        # if result > 20:
        #     print(current, neighbor, end, path, sep="\n")
        #     print(result)
        #     exit()

        return result

    def update_pheromone(self, all_paths):
        self.pheromone *= self.evaporation
        for path, length in all_paths:
            for pos in path:
                self.pheromone[pos] += 1.0 / length

    def get_neighbors(self, pos):
        x, y = pos
        potential_neighbors = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                               (x, y - 1), (x, y + 1),
                               (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        return [(nx, ny) for nx, ny in potential_neighbors
                if 0 <= nx < self.grid.shape[0] and 0 <= ny < self.grid.shape[1]
                and self.grid[nx, ny] != 1]

    def path_length(self, path):
        return sum(self.heuristic(path[i], path[i + 1]) for i in range(len(path) - 1))


