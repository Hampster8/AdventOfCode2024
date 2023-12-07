def parse_round_details(round_description):
    """Parses a round description into a dictionary of color counts."""
    color_counts = {'red': 0, 'green': 0, 'blue': 0}
    for segment in round_description.split(", "):
        quantity, color = segment.split(" ")
        color_counts[color] += int(quantity)
    return color_counts

def find_minimum_cubes_per_game(game_description):
    """Determines the minimum set of cubes needed for each game."""
    minimum_cubes_required = {'red': 0, 'green': 0, 'blue': 0}
    for round_description in game_description.split("; "):
        counts_per_round = parse_round_details(round_description)
        for color in minimum_cubes_required:
            minimum_cubes_required[color] = max(minimum_cubes_required[color], counts_per_round[color])
    return minimum_cubes_required

def calculate_power_of_cube_set(cube_set):
    """Calculates the power of a given set of cubes."""
    return cube_set['red'] * cube_set['green'] * cube_set['blue']

def calculate_total_power_of_games(game_data):
    """Calculates the total power across all games."""
    total_power = 0
    for game in game_data.strip().split("\n"):
        game_rounds = game.split(": ")[1]
        min_cubes_for_game = find_minimum_cubes_per_game(game_rounds)
        total_power += calculate_power_of_cube_set(min_cubes_for_game)
    return total_power

# Read data from file and calculate the total power
file_path = '/Users/hampusandersson/Documents/VscodeProjects/AdventOfCode2024/Day2/puzzleinput.txt'
with open(file_path, 'r') as file:
    game_data = file.read()

print(f"Total power of minimum cube sets: {calculate_total_power_of_games(game_data)}")
