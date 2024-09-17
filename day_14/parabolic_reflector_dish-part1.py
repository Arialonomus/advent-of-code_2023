"""
Advent of Code 2023
Day 14 - Parabolic Reflector Dish (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

# Parse arguments
args = get_args(14, "Parabolic Reflector Dish (Part 1)")

# Read in input schematic
with args.input_file as file:
    # Transpose the matrix and reverse each line so we can work with columns as rows
    # with North being represented as towards the end of the array
    rock_positions = np.array([list(line) for line in file.read().splitlines()], dtype='U1').T
    rock_positions = rock_positions[:, ::-1]

# Calculate the load for each row
total_load = 0
for row in rock_positions:
    # Determine the left-most position for each grouping of cube rocks
    cube_positions = np.where(row == '#')[0]
    if cube_positions.size > 0:
        non_consecutive_indices = np.where(np.diff(cube_positions) > 1)[0] + 1
        cube_positions = np.insert(cube_positions[non_consecutive_indices], 0, cube_positions[0])

    # Append the start and end positions for row slicing
    cube_positions = np.unique(np.concatenate(([0], cube_positions, [len(row)])))

    # Calculate the load up to each obstacle in the row and add to the total
    for i in range(cube_positions.size - 1):
        start = cube_positions[i]
        boundary = cube_positions[i + 1]
        num_rocks = np.count_nonzero(row[start:boundary] == 'O')
        total_load += num_rocks * (2 * boundary - (num_rocks - 1)) // 2

# Display final total
print(total_load)