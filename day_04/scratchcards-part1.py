"""
Advent of Code 2023
Day 4 - Scratchcards (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(4, "Scratchcards")

# Loop through each card, summing the points won on each card
sum_points = 0
with args.input_file as file:
    for line in file:
        # Split each game into game ID and numbers
        line = line.strip()
        game_id_str, numbers_str = line.split(': ')

        # Separate the winning and owned numbers into integer lists
        winning_nums_str, my_nums_str = numbers_str.split('|')
        winning_nums = list(map(int, winning_nums_str.split()))
        my_nums = list(map(int, my_nums_str.split()))

        # Check each winning number against the owned numbers for a match
        num_matches = 0
        points = 0
        for num in winning_nums:
            if num in my_nums:
                points = 2**num_matches
                num_matches += 1
        sum_points += points

    # Display points for pile of scratchcards
    print(sum_points)