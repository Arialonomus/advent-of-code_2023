"""
Advent of Code 2023
Day 2 - Cube Conundrum

Solution by Jacob Barber
"""

from aoc_utils import get_args
from functools import reduce
import operator

# Parse arguments
args = get_args(2, "Cube Conundrum")

# Loop through input, checking which games are possible and sum their IDs
sum_powers = 0
with args.input_file as file:
    for line in file:
        # Split string into ID and rounds
        line = line.strip()
        game_str, rounds_str = line.split(": ")
        rounds_list = rounds_str.split("; ")

        # Loop through rounds to calculate the smallest possible value for each color
        minimum_values = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in rounds_list:
            # Split round into pulls and log in dictonary
            pulls_list = round.split(', ')
            for pull in pulls_list:
                value, color = pull.split()
                value = int(value)
                if value > minimum_values[color]:
                    minimum_values[color] = value

        power = reduce(operator.mul, minimum_values.values())
        sum_powers += power

print(sum_powers)
