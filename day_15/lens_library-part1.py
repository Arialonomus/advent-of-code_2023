"""
Advent of Code 2023
Day 15 - Lens Library (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(14, "Lens Library (Part 1)")

# Read in input
with args.input_file as file:
    initialization_sequence = file.readline().strip().split(',')

# Hash the initialization sequence and sum the value of each step
sum_step_values = 0
for step in initialization_sequence:
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    sum_step_values += current_value
print(sum_step_values)
