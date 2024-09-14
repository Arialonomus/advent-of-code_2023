"""
Advent of Code 2023
Day 11 - Cosmic Expansion (Part 1)

Solution by Jacob Barber
"""

from itertools import combinations
from aoc_utils import get_args

# Parse arguments
args = get_args(11, "Cosmic Expansion (Part 1)")

# Read in the map, storing information about the galaxies
galaxy_map = []
galaxy_cols = set()
with args.input_file as file:
    for line in file:
        galaxy_positions = {i for i, c in enumerate(line) if c == '#'}
        if not galaxy_positions:
            # Append an extra row for galaxy expansion
            galaxy_map.append(list(line.strip()))
        else:
            galaxy_cols.update(galaxy_positions)
        galaxy_map.append(list(line.strip()))

# Expand the galaxy map horizontally by doubling the columns without galaxies
empty_cols = set(range(len(galaxy_map[0]))).difference(galaxy_cols)
for row in galaxy_map:
    i = 0
    for index in empty_cols:
        row.insert(index + i, '.')
        i += 1

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
    distance = abs(galaxy_b[0] - galaxy_a[0]) + abs(galaxy_b[1] - galaxy_a[1])
    sum_distances += distance
print(sum_distances)