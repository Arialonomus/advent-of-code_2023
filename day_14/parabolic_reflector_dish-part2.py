"""
Advent of Code 2023
Day 14 - Parabolic Reflector Dish (Part 2)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

NUM_CYCLES = 1000000000

# Parse arguments
args = get_args(14, "Parabolic Reflector Dish (Part 2)")

# Read in input schematic
with args.input_file as file:
    rock_positions = np.array([list(line) for line in file.read().splitlines()], dtype='U1')

def get_open_ranges(schematic):
    """
    Calculates the range(s) of open cells for each row in the passed-in schematic.
    Assumes the schematic is oriented with the tilt direction towards the right
    """
    open_ranges = []
    for row in schematic:
        row_ranges = []
        start = 0
        range_started = False
        for i in range(row.size):
            if row[i] == '#':
                if range_started:
                    # Denotes the leftmost boundary of one or more cubes
                    row_ranges.append((start, i))
                    range_started = False
            elif not range_started:
                # Begin tracking an open range
                start = i
                range_started = True
        if range_started:
            # Row ends at grid boundary
            row_ranges.append((start, row.size))
        open_ranges.append(row_ranges)

    return open_ranges

# Determine the open ranges for each tilt direction
# Ranges will be for each tilt direction oriented rightward
north_open_ranges = get_open_ranges(rock_positions.T[:, ::-1])
west_open_ranges = get_open_ranges(rock_positions[:, ::-1])
south_open_ranges = get_open_ranges(rock_positions.T)
east_open_ranges = get_open_ranges(rock_positions)

def tilt(oriented_schematic, open_ranges):
    """
    Tilts the platform so that all rocks roll as far as they can go. Updates
    the schematic with the new rock positions. Input schematic must be
    oriented such that the desired tilt direction is rightward.
    """
    for i in range(oriented_schematic.shape[0]):
        row = oriented_schematic[i]
        for open_range in open_ranges[i]:
            start = open_range[0]
            boundary = open_range[1]
            num_rocks = np.count_nonzero(row[start:boundary] == 'O')
            row[start:boundary - num_rocks] = '.'
            row[boundary - num_rocks:boundary] = 'O'

# Calculate cycle outcomes until a pattern is found
memo = {}
pattern_found = False
output_pattern = []
current_schematic = rock_positions.copy()
cycle = 0
while cycle < NUM_CYCLES and not pattern_found:
    if current_schematic.tobytes() in memo.keys():
        if output_pattern and np.array_equal(current_schematic, output_pattern[0]):
            pattern_found = True
        else:
            output_pattern.append(current_schematic)
            current_schematic = memo[current_schematic.tobytes()]
    else:
        prev_schematic = current_schematic.copy()

        # Tilt north
        tilt(current_schematic.T[:, ::-1], north_open_ranges)

        # Tilt west
        tilt(current_schematic[:, ::-1], west_open_ranges)

        # Tilt south
        tilt(current_schematic.T, south_open_ranges)

        # Tilt east
        tilt(current_schematic, east_open_ranges)

        memo[prev_schematic.tobytes()] = current_schematic.copy()
    cycle += 1

# Determine the output of the final cycle from the pattern list
final_output_index = ((NUM_CYCLES - cycle) % len(output_pattern)) + 1
final_output = output_pattern[final_output_index]

# Calculate the load for each row
total_load = 0
for i in range(final_output.shape[0]):
    row = final_output[i]
    num_rocks = np.count_nonzero(row == 'O')
    total_load += num_rocks * (final_output.shape[0] - i)
print(total_load)
