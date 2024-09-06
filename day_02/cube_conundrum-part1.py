"""
Advent of Code 2023
Day 2 - Cube Conundrum (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(2, "Cube Conundrum")

# Define parameters for possibility check
GAME_PARAMS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# Loop through input, checking which games are possible and sum their IDs
sum_ids = 0
with args.input_file as file:
    for line in file:
        # Split string into ID and rounds
        line = line.strip()
        id_str, rounds_str = line.split(": ")
        id = int(id_str.strip("Game "))
        rounds_list = rounds_str.split("; ")

        # Process each round to check if game is possible
        is_possible = True
        for round in rounds_list:
            # Reset starting dictonary for pulls this round
            round_dict = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            # Split round into pulls and log in dictonary
            pulls_list = round.split(', ')
            for pull in pulls_list:
                value, color = pull.split()
                round_dict[color] = int(value)

            # Check round against parameters to determine game possibility
            is_possible = all(round_dict[key] <= GAME_PARAMS[key] for key in round_dict)
            if not is_possible:
                break

        if is_possible:
            sum_ids += id

print(sum_ids)
