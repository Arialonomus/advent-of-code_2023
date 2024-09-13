"""
Advent of Code 2023
Day 10 - Pipe Maze (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(10, "Pipe Maze (Part 1)")

# Read in the map, preserving the starting position
maze_map = []
with args.input_file as file:
    row = 0
    starting_pos = ()
    cell = file.read(1)
    while cell != '':
        maze_row = []
        col = 0
        while cell != '\n':
            maze_row.append(cell)
            if cell == 'S':
                starting_pos = (row, col)
            cell = file.read(1)
            col += 1
        maze_map.append(maze_row)
        row += 1
        cell = file.read(1)
