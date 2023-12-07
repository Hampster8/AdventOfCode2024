# Bag capacity
bag_capacity = {'red': 12, 'green': 13, 'blue': 14}

# Function to check if a round can be played
def can_play_round(round_data, bag_capacity):
    for color, count in round_data.items():
        if count > bag_capacity[color]:
            return False
    return True

# Function to process each game
def process_games(data):
    playable_games = []
    for game in data.strip().split("\n"):
        game_number, rounds = game.split(": ")
        game_number = int(game_number.split(" ")[1])
        all_rounds_playable = True

        for round in rounds.split("; "):
            round_data = {'red': 0, 'green': 0, 'blue': 0}
            for part in round.split(", "):
                count, color = part.split(" ")
                round_data[color] += int(count)

            if not can_play_round(round_data, bag_capacity):
                all_rounds_playable = False
                break

        if all_rounds_playable:
            playable_games.append(game_number)

    return sum(playable_games)

# Read data from file and calculate the sum of playable games
file_path = '/Users/hampusandersson/Documents/VscodeProjects/AdventOfCode2024/Day2/puzzleinput.txt'
with open(file_path, 'r') as file:
    data = file.read()

sum_of_playable_games = process_games(data)
print("Sum of playable games:", sum_of_playable_games)
