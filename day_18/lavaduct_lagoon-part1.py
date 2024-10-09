"""
Advent of Code 2023
Day 18 - Lavaduct Lagoon (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

# Parse arguments
args = get_args(18, "Lavaduct Lagoon (Part 1)")

# Read in input
with args.input_file as file:
    dig_plan = []
    for line in file:
        direction, length, color = line.strip().split()
        dig_plan.append((direction, int(length), color[1:-1]))

top, bottom, left, right = 0, 0, 0, 0
x, y = 0, 0
for instruction in dig_plan:
    direction, length, color = instruction
    match direction:
        case 'U':
            y += length
            if y > top:
                top = y
        case 'D':
            y -= length
            if y < bottom:
                bottom = y
        case 'R':
            x += length
            if x > right:
                right = x
        case 'L':
            x -= length
            if x < left:
                left = x

width = abs(right - left) + 1
height = abs(top - bottom) + 1
lagoon_map = np.full((height, width), '.')
start = (height + bottom - 1, width - right - 1)
row, col = start
for instruction in dig_plan:
    direction, length, color = instruction
    match direction:
        case 'U':
            lagoon_map[row - length:row, col] = '#'
            row -= length
        case 'D':
            row += 1
            lagoon_map[row:row + length, col] = '#'
            row += (length - 1)
        case 'R':
            col += 1
            lagoon_map[row, col:col + length] = '#'
            col += (length - 1)
        case 'L':
            lagoon_map[row, col - length:col] = '#'
            col -= length
for row in lagoon_map:
    print(''.join(row))