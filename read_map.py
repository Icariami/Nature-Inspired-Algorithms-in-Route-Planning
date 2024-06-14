import numpy as np


def read_map(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    height = int(lines[1].split()[1])
    width = int(lines[2].split()[1])
    map_data = [line.strip() for line in lines[4:4 + height]]
    result = [[0 if char == '.' else 1 for char in row] for row in map_data]
    return np.array(result)


if __name__ == '__main__':
    print(read_map('maps/Berlin_0_256.map'))
