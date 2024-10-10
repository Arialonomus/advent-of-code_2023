"""
Advent of Code 2023
Day 18 - Lavaduct Lagoon (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

# Parse arguments
args = get_args(18, "Lavaduct Lagoon (Part 1)")

# Read in input and calculate canvas size for lagoon map
with args.input_file as file:
    dig_plan = []
    top, bottom, left, right = 0, 0, 0, 0
    x, y = 0, 0
    for line in file:
        direction, length, color = line.strip().split()
        length = int(length)
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
        dig_plan.append((direction, length, color[1:-1]))

def draw_trench(canvas, instructions, start_pos):
    """
    Draws a trench on a 2x2 matrix initialized to the correct size
    by following a set of instructions passed in as a list of tuples.
    """

    # Draw trench in lagoon map based on instructions
    row, col = start_pos
    for instruction in instructions:
        current_dir, current_len, current_color = instruction
        match current_dir:
            case 'U':
                canvas[row - current_len:row, col] = '#'
                row -= current_len
            case 'D':
                row += 1
                canvas[row:row + current_len, col] = '#'
                row += (current_len - 1)
            case 'R':
                col += 1
                canvas[row, col:col + current_len] = '#'
                col += (current_len - 1)
            case 'L':
                canvas[row, col - current_len:col] = '#'
                col -= current_len

# Initialize lagoon map
width = abs(right - left) + 1
height = abs(top - bottom) + 1
lagoon_map = np.full((height, width), '.')
start = (height + bottom - 1, width - right - 1)
draw_trench(lagoon_map, dig_plan, start)

