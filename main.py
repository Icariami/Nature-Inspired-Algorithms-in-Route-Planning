import numpy as np

from visualize import visualize_grid
from ACO import ACO
from read_map import read_map


def main():
    # grid = np.zeros((10, 10))
    # grid[3, 0:7] = 1  # example of obstacles
    # grid[5, 1:10] = 1  # example of obstacles

    grid = read_map('maps/den009d.map')

    aco = ACO(grid, ants=10, alpha=0.5, beta=1.0, evaporation=0.5, iterations=1000)
    start = (3, 5)
    end = (5, 40)
    path = aco.find_path(start, end)

    if path:
        print("Path found:", path)
    else:
        print("No path found")

    visualize_grid(grid, path)


if __name__ == "__main__":
    main()
