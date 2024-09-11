"""
Advent of Code 2023
Day 6 - Wait For It (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args
import math
import numpy as np

# Parse arguments
args = get_args(6, "Wait For It")

with args.input_file as file:
    # Parse input data
    times = list(map(int, file.readline().strip("Time:").strip().split()))
    distances = list(map(int, file.readline().strip("Distance:").strip().split()))

    num_races = len(times)
    paths_to_victory = [0] * num_races
    for i in range(num_races):
        time = times[i]
        min_distance = distances[i] + 1

        # Solutions for the longest and shortest times the button can be held
        # is given by v^2 - tv + d = 0 where v = time held, t = race time,
        # and d = the minimum distance needed to win (distance + 1)
        coefficients = [1, time * -1, min_distance]
        solutions = np.roots(coefficients)

        # Calculate the number of ways to win the race
        # solutions[0] represents the max number of ms the button can be held, must round down
        # solutions[1] represents the min number of ms, must round up
        # Add 1 to make the range inclusive
        paths_to_victory[i] = math.floor(solutions[0]) - math.ceil(solutions[1]) + 1

    # Print total number of paths to victory
    num_permutations = np.prod(paths_to_victory)
    print(num_permutations)
