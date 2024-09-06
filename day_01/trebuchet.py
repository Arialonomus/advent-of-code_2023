"""
Advent of Code 2023
Day 1 - Trebuchet!?

Solution by Jacob Barber
"""

import argparse
import regex
from utils_day_01 import name_to_digit

# Parse arguments
parser = argparse.ArgumentParser(
    description="A solution to Advent of Code 2023 puzzle 'Trebuchet!?'")
parser.add_argument('input_file',
                    type=argparse.FileType('r'),
                    help="Input file path")
args = parser.parse_args()

# Read each line and parse two digit numbers from them
sum = 0
with args.input_file as file:
    for line in file:
        # Parse digits in line into list
        pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
        digits = regex.findall(pattern, line, overlapped=True)

        # Select first and last digits (same if only 1 digit present)
        first = digits[0]
        if len(first) > 1:
            first = name_to_digit(first)
        last = digits[-1]
        if len(last) > 1:
            last = name_to_digit(last)

        # Combine digits into calibration value and add to sum
        digit_str = first + last
        sum += int(digit_str)

# Print the sum of the digits in each line
print(sum)
