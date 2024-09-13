"""
Advent of Code 2023
Day 9 - Mirage Maintenance (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(9, "Mirage Maintenance (Part 1)")

# Parse histories from input
histories = []
with args.input_file as file:
    for line in file:
        history = list(map(int, line.strip().split()))
        histories.append(history)

def get_next_value(sequence):
    """
    Recursively calculates the next value in a sequence by calculating
    the next value in subsequent difference sequences
    """
    diff_sequence = []
    for i in range (1, len(sequence)):
        difference = sequence[i] - sequence[i-1]
        diff_sequence.append(difference)
    # Base Case - Zero sequence
    if sum(diff_sequence) == 0:
        return sequence[-1]
    # Recursive Case - Calculate next difference subsequence
    return sequence[-1] + get_next_value(diff_sequence)

# Calculate the sum of the next values for each history
sum_values = 0
for history in histories:
    sum_values += get_next_value(history)
print(sum_values)