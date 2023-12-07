# Constants representing the bag's capacity for each color
RED_CAPACITY = 12
GREEN_CAPACITY = 13
BLUE_CAPACITY = 14

def parse_round_data(round_str):
    """Parse a round string into a dictionary of color counts."""
    color_counts = {'red': 0, 'green': 0, 'blue': 0}
    for part in round_str.split(", "):
        count, color = part.split(" ")
        color_counts[color] += int(count)
    return color_counts

def is_round_playable(round_data):
    """Check if a round can be played with the given bag capacity."""
    return (round_data['red'] <= RED_CAPACITY and
            round_data['green'] <= GREEN_CAPACITY and
            round_data['blue'] <= BLUE_CAPACITY)

def is_game_playable(game_rounds):
    """Check if all rounds in a game are playable."""
    for round_str in game_rounds.split("; "):
        round_data = parse_round_data(round_str)
        if not is_round_playable(round_data):
            return False
    return True

def sum_playable_game_ids(data):
    """Calculate the sum of IDs of games that can be played."""
    sum_of_ids = 0
    for game in data.strip().split("\n"):
        game_id_str, game_rounds = game.split(": ")
        game_id = int(game_id_str.split(" ")[1])

        if is_game_playable(game_rounds):
            sum_of_ids += game_id

    return sum_of_ids

# Read data from file and calculate the sum of playable game IDs
file_path = '/Users/hampusandersson/Documents/VscodeProjects/AdventOfCode2024/Day2/puzzleinput.txt'
with open(file_path, 'r') as file:
    data = file.read()

print("Sum of playable game IDs:", sum_playable_game_ids(data))
