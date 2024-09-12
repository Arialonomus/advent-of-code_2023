"""
Advent of Code 2023
Day 8 - Haunted Wasteland (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

START_NODE = 'AAA'
END_NODE = 'ZZZ'

# Parse arguments
args = get_args(8, "Haunted Wasteland (Part 1)")

# Read in input from file
desert_map = {}
with args.input_file as file:
    instructions = file.readline().rstrip()
    file.readline() # Consume newline
    translation_table = str.maketrans('', '', '=(,)')
    for line in file:
        node, left, right = line.translate(translation_table).split()
        desert_map[node] = (left, right)
