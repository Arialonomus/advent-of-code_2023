"""
Advent of Code 2023
Day 12 - Point of Incidence (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

HORIZONTAL_REFLECTION_FACTOR = 100

# Parse arguments
args = get_args(13, "Point of Incidence (Part 1)")

# Parse input patterns into rows and columns
patterns = []
with args.input_file as file:
    line = file.readline()
    while line != '':
        rows = []
        cols = [[] for char in line.strip()]
        index = 0
        while line not in ['\n', '']:
            row = list(line.strip())
            rows.append(row)
            for i in range(len(row)):
                cols[i].append(row[i])
            line = file.readline()
        patterns.append((rows, cols))
        line = file.readline()
