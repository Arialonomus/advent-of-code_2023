"""
Advent of Code 2023
Day 12 - Hot Springs (Part 2)

Solution by Jacob Barber
"""

import math
import operator
from functools import reduce
from aoc_utils import get_args

UNFOLD_FACTOR = 5

# Parse arguments
args = get_args(12, "Hot Springs (Part 2)")

spring_rows = []
with args.input_file as file:
    for line in file:
        spring_row, damaged_count = line.strip().split()
        spring_rows.append((list(spring_row), list(map(int, damaged_count.split(',')))))

"""# Read in spring rows and damaged group parts
spring_rows = []
with args.input_file as file:
    for line in file:
        spring_row, damaged_count = line.strip().split()
        spring_row_unfolded = '?'.join([spring_row] * UNFOLD_FACTOR)
        damaged_count_unfolded = ','.join([damaged_count] * UNFOLD_FACTOR)
        spring_rows.append((list(spring_row_unfolded), list(map(int, damaged_count_unfolded.split(',')))))"""

def count_valid_arrangements(layout, counts):

    row_len = len(layout)
    num_groups = len(counts)
    permutation_counts = [1] * num_groups
    spring = 0
    group = 0
    while spring < row_len and group < num_groups:
        match layout[spring]:
            case '.':
                if counts[group] == 0:
                    group += 1
                spring += 1
            case '#':
                while counts[group] > 0 and spring < row_len and layout[spring] != '.':
                    counts[group] -= 1
                    spring += 1
            case '?':
                if counts[group] == 0:
                    group += 1
                    spring += 1
                else:
                    # Get the length of the unknown group
                    end = spring
                    while end < row_len and layout[end] == '?':
                        end += 1
                    unknown_len = end - spring

                    if end == row_len or layout[end] == '.':
                        # Grouping is all broken springs, only one possible permutation
                        if unknown_len == counts[group]:
                            group += 1

                        # Calculate number of unique permutations for this unknown group
                        elif unknown_len > counts[group]:
                            # Determine how many broken groups can be contained in this unknown group
                            total_len = counts[group]
                            group_end = group + 1
                            while group_end < num_groups and unknown_len > total_len + counts[group_end]:
                                total_len += counts[group_end]
                                group_end += 1

                            # Calculate permutations as a stars and bars problem
                            num_counts = group_end - group
                            empty_count = unknown_len - total_len - (num_counts - 1)
                            num_permutations = math.comb(empty_count + num_counts, num_counts)
                            permutation_counts[group_end - 1] = num_permutations
                            group = group_end
                        spring = end

                    elif layout[end] == '#':
                        num_broken = unknown_len
                        while end < row_len and layout[end] == '#':
                            num_broken += 1
                            end += 1
                        if num_broken <= counts[group]:
                            counts[group] -= num_broken
                            spring = end
                        else:
                            spring += 1

    return reduce(operator.mul, permutation_counts)


# Calculate and display the sum of valid permutations for all rows
sum_valid_arrangements = 0
for row in spring_rows:
    spring_layout, grouping_counts = row
    sum_valid_arrangements += count_valid_arrangements(spring_layout, grouping_counts)
print(sum_valid_arrangements)