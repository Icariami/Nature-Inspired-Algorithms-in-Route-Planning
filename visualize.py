import os
import string

import numpy as np


def visualize_grid(grid, path, filepath='result1.txt'):
    # save in the same directory
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, filepath)
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Create a copy of the grid to avoid modifying the original grid.
    visual_grid = np.full(grid.shape, '.', dtype=str)

    # Place obstacles
    visual_grid[grid == 1] = '@'

    # Define the sequence of English letters
    letters = string.ascii_lowercase

    # Place path points with letters
    if path is not None:
        for idx, point in enumerate(path):
            visual_grid[point] = letters[idx % len(letters)]

    # Open the file and write the visual grid row-wise
    with open(filepath, 'w') as file:
        for row in visual_grid:
            file.write(' '.join(row) + '\n')
