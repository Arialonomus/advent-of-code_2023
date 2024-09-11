"""
Advent of Code 2023
Day 6 - Wait For It (Part 2)

Solution by Jacob Barber
"""

from aoc_utils import get_args
import math
import numpy as np

# Parse arguments
args = get_args(6, "Wait For It")

with args.input_file as file:
    # Parse input data
    time = int(file.readline().replace(" ", "").strip("Time:").strip())
    distance = int(file.readline().replace(" ", "").strip("Distance:").strip())

    # Solutions for the longest and shortest times the button can be held
    # is given by v^2 - tv + d = 0 where v = time held, t = race time,
    # and d = the minimum distance needed to win (distance + 1)
    coefficients = [1, time * -1, distance + 1]
    solutions = np.roots(coefficients)

    # Calculate the number of ways to win the race
    # solutions[0] represents the max number of ms the button can be held, must round down
    # solutions[1] represents the min number of ms, must round up
    # Add 1 to make the range inclusive
    num_permutations = math.floor(solutions[0]) - math.ceil(solutions[1]) + 1
    print(num_permutations)
