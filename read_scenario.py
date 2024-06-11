def read_scenario(file_path):
    scenarios = []
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]  # bez naglowka
    for line in lines:
        parts = line.split()
        scenario = {
            'id': int(parts[0]),
            'map_name': parts[1],
            'map_width': int(parts[2]),
            'map_height': int(parts[3]),
            'start_x': int(parts[4]),
            'start_y': int(parts[5]),
            'goal_x': int(parts[6]),
            'goal_y': int(parts[7]),
            'optimal_length': float(parts[8])
        }
        scenarios.append(scenario)
    return scenarios


# scenarios = read_scenario('scenarios/Berlin_0_256.map.scen')
# for scenario in scenarios:
#     print(scenario)
#
# print("")
# print(scenarios[0])
