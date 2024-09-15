"""
Advent of Code 2023
Day 11 - Cosmic Expansion (Part 2)

Solution by Jacob Barber
"""

from itertools import combinations
from aoc_utils import get_args

DISTANCE_FACTOR = 1000000

# Parse arguments
args = get_args(11, "Cosmic Expansion (Part 2)")

# Read in the map, storing information about the galaxies
galaxy_map = []
galaxy_cols = set()
empty_rows = []
with args.input_file as file:
    row = 0
    for line in file:
        galaxy_positions = {i for i, c in enumerate(line) if c == '#'}
        if not galaxy_positions:
            empty_rows.append(row)
        else:
            galaxy_cols.update(galaxy_positions)
        galaxy_map.append(list(line.strip()))
        row += 1

# Determine the indices of the empty columns
empty_cols = sorted(list(set(range(len(galaxy_map[0]))).difference(galaxy_cols)))

# Get the coordinates for each galaxy and build a list of pairs
galaxy_coordinates = []
for y in range(len(galaxy_map)):
    columns = [i for i, c in enumerate(galaxy_map[y]) if c == '#']
    for x in columns:
        galaxy_coordinates.append((x, y))
galaxy_pairs = list(combinations(galaxy_coordinates, 2))

# Calculate and display the sum of the distances between each galaxy
sum_distances = 0
for pair in galaxy_pairs:
    galaxy_a, galaxy_b = pair[0], pair[1]
    a_x, a_y = galaxy_a
    b_x, b_y = galaxy_b
    distance = abs(b_x - a_x) + abs(b_y - a_y)
    for col in empty_cols:
        if min(a_x, b_x) < col < max(a_x, b_x):
            distance += DISTANCE_FACTOR - 1
    for row in empty_rows:
        if min(a_y, b_y) < row < max(a_y, b_y):
            distance += DISTANCE_FACTOR - 1
    sum_distances += distance
print(sum_distances)