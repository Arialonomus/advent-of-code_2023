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

def span_fill(grid, row, col):
    """
    Fill the inside the outline using a span fill algorithm.
    Algorithm adapted from Glassner's optimized algorithm, presented in pseudocode
    at https://en.wikipedia.org/wiki/Flood_fill
    """

    grid_height, grid_width = grid.shape

    def inside(cur_row, cur_col):
        """
        Helper function to determine if tile is an inside tile
        """
        return 0 <= cur_row < grid_height and 0 <= cur_col < grid_width and grid[cur_row][cur_col] == '.'

    # Early return if the tile is not inside the outline
    if not inside(row, col):
        return grid

    queue = [(col, col, row, 1), (col, col, row - 1, -1)]
    while queue:
        entry = queue.pop(0)
        x1, x2, y, dy = entry
        x = x1
        if inside(y, x):
            while inside(y, x - 1):
                grid[y][x - 1] = '#'
                x -= 1
            if x < x1:
                queue.append((x, x1 - 1, y - dy, -dy))
        while x1 <= x2:
            while inside(y, x1):
                grid[y][x1] = '#'
                x1 += 1
            if x1 > x:
                queue.append((x, x1 - 1, y + dy, dy))
            if x1 - 1 > x2:
                queue.append((x2 + 1, x1 - 1, y - dy, -dy))
            x1 += 1
            while x1 < x2 and not inside(y, x1):
                x1 += 1
            x = x1
    return grid

# Fill the trench and count the number of filled tiles
start_row, start_col = start
span_fill(lagoon_map, start_row + 1, start_col + 1)
num_filled_tiles = np.count_nonzero(lagoon_map == '#')
print(num_filled_tiles)