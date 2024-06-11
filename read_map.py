def read_map(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    height = int(lines[1].split()[1])
    width = int(lines[2].split()[1])
    map_data = [line.strip() for line in lines[4:4 + height]]
    return map_data


def is_traversable(cell):
    return cell == '.'


def is_non_traversable(cell):
    return cell == '@'

# map_data = read_map('maps/Berlin_0_256.map')
# for row in map_data:
#     print(row)
