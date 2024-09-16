"""
Advent of Code 2023
Day 12 - Hot Springs (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(12, "Hot Springs (Part 1)")

# Read in spring rows and damaged group parts
spring_rows = []
with args.input_file as file:
    for line in file:
        spring_row, damaged_count = line.strip().split()
        spring_rows.append((list(spring_row), list(map(int, damaged_count.split(',')))))

def num_valid_arrangements(layout, current, counts):
    """
    Recursively calculate the number of valid arrangements of broken spring groups
    for a given row based on the spring counts for each contiguous group.
    """
    while current < len(layout):
        match layout[current]:
            case '#':
                if counts:
                    # Add this spring to the current grouping
                    counts[0] -= 1
                if not counts or counts[0] < 0:
                    # There are no remaining groupings or this grouping is too large
                    return 0
            case '.':
                if counts:
                    # There are some groupings remaining
                    if counts[0] == 0:
                        # This spring denotes the end of a broken group
                        counts.pop(0)
                    elif current > 0 and layout[current - 1] == '#':
                        # The current grouping is too small
                        return 0
            case '?':
                num_valid = 0
                if counts and counts[0] != 0:
                    # This space could fit a broken spring
                    row_with_broken = layout.copy()
                    row_with_broken[current] = '#'
                    num_valid += num_valid_arrangements(row_with_broken, current, counts.copy())
                # This space must be a working spring
                row_with_working = layout.copy()
                row_with_working[current] = '.'
                num_valid += num_valid_arrangements(row_with_working, current, counts.copy())

                # Return the valid permutations emerging from this tile
                return num_valid
        # Move to the next space
        current += 1

    if not counts or counts == [0]:
        return 1
    else:
        return 0

# Calculate and display the sum of valid permutations for all rows
sum_valid_arrangements = 0
for row in spring_rows:
    spring_layout, grouping_counts = row
    sum_valid_arrangements += num_valid_arrangements(spring_layout, 0, grouping_counts)
print(sum_valid_arrangements)