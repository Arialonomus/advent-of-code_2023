"""
Advent of Code 2023
Day 13 - Point of Incidence (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

HORIZONTAL_REFLECTION_FACTOR = 100

# Parse arguments
args = get_args(13, "Point of Incidence (Part 1)")

# Read in input patterns
with args.input_file as file:
    pattern_blocks = file.read().strip().split("\n\n")
    patterns = [np.array([list(line) for line in block.splitlines()], dtype='U1')
                for block in pattern_blocks]

def get_total_reflections(pattern):
    """
    Returns the number of horizontal and vertical reflections for
    a passed in pattern, with the horizontal reflections scaled
    by a pre-set Horizontal Reflection Factor.
    """

    def count_reflections(layout):
        """
        Returns the number of reflected rows across a line of
        prefect reflection found within the passed in list of rows.
        If no line of perfect reflection is found, returns zero.
        """

        list_len = len(layout)
        for i in range(list_len - 1):
            # Check if adjacent lines are reflected
            upper_row = layout[i]
            lower_row = layout[i + 1]
            if np.array_equal(upper_row, lower_row):
                # Line of reflection found, check outer rows for reflections
                a = i - 1
                b = i + 2
                perfect_reflection = True
                while a >= 0 and b < list_len and perfect_reflection:
                    if np.array_equal(layout[a], layout[b]):
                        a -= 1
                        b += 1
                    else:
                        perfect_reflection = False
                if perfect_reflection:
                    return i + 1

        # No perfect reflections found
        return 0

    num_reflected_rows = count_reflections(pattern)
    if num_reflected_rows == 0:
        return count_reflections(pattern.T)
    else:
        return HORIZONTAL_REFLECTION_FACTOR * num_reflected_rows

# Calculate and display the sum of total reflections across all patterns
sum_reflection_counts = 0
for pattern in patterns:
    sum_reflection_counts += get_total_reflections(pattern)
print(sum_reflection_counts)
