"""
Advent of Code 2023
Day 1 - Trebuchet!? - Puzzle 1

Solution by Jacob Barber
"""

import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="A solution to Advent of Code '23 puzzle 'Trebuchet!?' Part 1.")
parser.add_argument('input_file',
                    type=argparse.FileType('r'),
                    help="Input file path")
args = parser.parse_args
