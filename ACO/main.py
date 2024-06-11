from ACO.Ant import Ant
from ACO.Graph import Graph
from read_map import read_map


def main():
    map_data = read_map('../maps/A_second_example.map')
    graph = Graph(map_data)
    start_node = graph.nodes[(0, 0)]
    end_node = graph.nodes[(9, 4)]
    ant = Ant(start_node, graph)
    path, total_cost = ant.find_path(end_node)
    print("Found path:", [(node.coordinates, next_node.coordinates) for node, next_node in path])
    print("Total cost:", total_cost)


if __name__ == '__main__':
    main()
