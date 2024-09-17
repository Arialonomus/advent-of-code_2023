"""
Advent of Code 2023
Day 12 - Point of Incidence (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

HORIZONTAL_REFLECTION_FACTOR = 100

# Parse arguments
args = get_args(13, "Point of Incidence (Part 1)")

# Parse input patterns into rows and columns
patterns = []
with args.input_file as file:
    line = file.readline()
    while line != '':
        rows = []
        cols = [[] for char in line.strip()]
        index = 0
        while line not in ['\n', '']:
            row = list(line.strip())
            rows.append(row)
            for i in range(len(row)):
                cols[i].append(row[i])
            line = file.readline()
        patterns.append((rows, cols))
        line = file.readline()

def get_total_reflections(pattern):
    """
    Returns the number of horizontal and vertical reflections for
    a passed in pattern, with the horizontal reflections scaled
    by a pre-set Horizontal Reflection Factor.
    """

    def count_reflections(tile_list):
        """
        Returns the number of reflected rows/columns across a line of
        prefect reflection found within the passed in list of rows/columns.
        If no line of perfect reflection is found, returns zero.
        """

        list_len = len(tile_list)
        for i in range(list_len - 1):
            # Check if adjacent lines are reflected
            list_a = tile_list[i]
            list_b = tile_list[i + 1]
            if list_a == list_b:
                # Line of reflection found
                a = i - 1
                b = i + 2
                perfect_reflection = True
                while a >= 0 and b < list_len and perfect_reflection:
                    if tile_list[a] == tile_list[b]:
                        a -= 1
                        b += 1
                    else:
                        perfect_reflection = False
                if perfect_reflection:
                    return i + 1

        return 0

    row_list, column_list = pattern
    num_reflected_rows = count_reflections(row_list)
    num_reflected_cols = count_reflections(column_list)

    return (HORIZONTAL_REFLECTION_FACTOR * num_reflected_rows) + num_reflected_cols

# Calculate and display the sum of total reflections across all patterns
sum_reflection_counts = 0
for pattern in patterns:
    sum_reflection_counts += get_total_reflections(pattern)
print(sum_reflection_counts)
