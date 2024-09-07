"""
Advent of Code 2023
Day 3 - Gear Ratios (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args
from .utils_day_03 import check_part_num

# Parse arguments
args = get_args(3, "Gear Ratios")

with args.input_file as file:
    # Read in data
    schematic = file.read().splitlines()
    num_rows = len(schematic)
    num_cols = len(schematic[0])

    # Iterate through the map recording valid part numbers
    part_list = []
    row = 0
    while row < num_rows:
        col = 0
        while col < num_cols:
            if schematic[row][col].isdigit():
                # Check the entire found number to see if it is valid,
                # when function returns it points to the column position
                # of the last digit in the number
                col = check_part_num(schematic, row, num_rows, col, num_cols, part_list)
            col += 1
        row += 1

    # Calculate the sum of the part nums
    sum_part_nums = sum(part_list)
    print(sum_part_nums)
