import numpy as np


class AntColonyOptimizer:
    def __init__(self, cost_matrix, num_ants, num_iterations, decay, alpha=1, beta=2):
        self.cost_matrix = cost_matrix
        self.pheromone = np.ones(self.cost_matrix.shape) / len(cost_matrix)
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self, start, end):
        for _ in range(self.num_iterations):
            all_paths = self.construct_solutions(start, end)
            self.update_pheromone(all_paths)
        shortest_path = min(all_paths, key=lambda x: x[1])
        return shortest_path

    def construct_solutions(self, start, end):
        all_paths = []
        for _ in range(self.num_ants):
            path, cost = self.construct_single_solution(start, end)
            all_paths.append((path, cost))
        return all_paths

    def construct_single_solution(self, start, end):
        path = [start]
        visited = set()
        visited.add(start)
        current = start
        total_cost = 0

        while current != end:
            moves = self.get_possible_moves(current, visited)
            if not moves:
                return path, float('inf')  # Return infinitely bad path if stuck

            move_probs = self.calculate_move_probs(current, moves)
            next_move = np.random.choice(moves, p=move_probs)
            path.append(next_move)
            total_cost += self.cost_matrix[current][next_move]
            visited.add(next_move)
            current = next_move

        return path, total_cost

    def get_possible_moves(self, position, visited):
        # Example to get possible moves in 8 directions
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for d in directions:
            move = (position[0] + d[0], position[1] + d[1])
            if 0 <= move[0] < self.cost_matrix.shape[0] and 0 <= move[1] < self.cost_matrix.shape[1]:
                if move not in visited and self.cost_matrix[move] > 0:
                    moves.append(move)
        return moves

    def calculate_move_probs(self, current, moves):
        move_probs = []
        for move in moves:
            move_prob = self.pheromone[current][move] ** self.alpha * (self.cost_matrix[current][move] ** -self.beta)
            move_probs.append(move_prob)
        return move_probs / np.sum(move_probs)

    def update_pheromone(self, all_paths):
        self.pheromone *= self.decay
        for path, cost in all_paths:
            for move in path:
                self.pheromone[move[0], move[1]] += 1.0 / cost


if __name__ == "__main__":
    n = 10
    # Example usage:
    cost_matrix = np.array([...])  # Your cost matrix where high values represent obstacles
    aco = AntColonyOptimizer(cost_matrix, num_ants=10, num_iterations=100, decay=0.95)
    shortest_path = aco.run((0, 0), (n - 1, n - 1))  # From top-left to bottom-right
    print(shortest_path)
