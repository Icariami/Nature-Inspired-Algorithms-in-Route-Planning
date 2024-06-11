import random


class Ant:
    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph
        self.path = []
        self.visited_nodes = set()
        self.total_cost = 0.0
        self.current_node = start_node

    def choose_next_node(self):
        neighbors = self.current_node.neighbors
        probabilities = self.calculate_probabilities(neighbors)

        # If all neighbors are already visited, return None or handle accordingly
        if not any(probabilities):
            return None

        next_node = random.choices(neighbors, weights=probabilities, k=1)[0]
        return next_node

    def calculate_probabilities(self, neighbors):
        tau_eta = []
        for neighbor in neighbors:
            if neighbor in self.visited_nodes:
                tau_eta.append(0.0)
            else:
                edge = tuple(sorted([self.current_node, neighbor], key=lambda x: x.coordinates))
                tau = self.graph.pheromones[edge]
                eta = 1.0 / self.current_node.distance_to(neighbor)
                tau_eta.append(tau * eta)
        sum_tau_eta = sum(tau_eta)
        if sum_tau_eta == 0.0:
            # If all tau_eta are zero, choose uniformly among non-visited neighbors
            tau_eta = [1.0 if neighbor not in self.visited_nodes else 0.0 for neighbor in neighbors]
            sum_tau_eta = sum(tau_eta)
        if sum_tau_eta == 0.0:
            # If still zero, means no available non-visited neighbors
            return [0] * len(neighbors)
        return [x / sum_tau_eta for x in tau_eta]

    def move_to_next_node(self, next_node):
        if next_node:
            edge = tuple(sorted([self.current_node, next_node], key=lambda x: x.coordinates))
            self.path.append(edge)
            self.visited_nodes.add(next_node)
            self.total_cost += self.current_node.distance_to(next_node)
            self.current_node = next_node
        else:
            print("No available moves, terminating the pathfinding.")
            self.current_node = None  # Indicates no move is possible

    def find_path(self, end_node):
        self.visited_nodes.add(self.start_node)
        self.path = []
        self.total_cost = 0.0
        self.current_node = self.start_node

        while self.current_node and self.current_node != end_node:
            next_node = self.choose_next_node()
            self.move_to_next_node(next_node)

        return self.path, self.total_cost

    def update_pheromones(self, pheromone_deposit):
        for edge in self.path:
            self.graph.pheromones[edge] += pheromone_deposit
