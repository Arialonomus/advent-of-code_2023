"""
Advent of Code 2023
Day 1 - Trebuchet!? - Puzzle 1

Solution by Jacob Barber
"""

import argparse
import re

# Parse arguments
parser = argparse.ArgumentParser(
    description="A solution to Advent of Code '23 puzzle 'Trebuchet!?'")
parser.add_argument('input_file',
                    type=argparse.FileType('r'),
                    help="Input file path")
args = parser.parse_args()

# Read each line and parse two digit numbers from them
sum = 0
with args.input_file as file:
    for line in file:
        # Parse digits in line into list
        digits = re.findall(r'\d', line)

        # Select first and last digits (same if only 1 digit present)
        first = digits[0]
        last = digits[len(digits) - 1]

        # Combine digits into calibration value and add to sum
        digit_str = first + last
        sum += int(digit_str)

# Print the sum of the digits in each line
print(sum)
