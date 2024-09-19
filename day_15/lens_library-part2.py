"""
Advent of Code 2023
Day 15 - Lens Library (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

NUM_BOXES = 256

# Parse arguments
args = get_args(14, "Lens Library (Part 1)")

# Read in input
with args.input_file as file:
    initialization_sequence = file.readline().strip().split(',')

def get_box_number(string):
    """
    Returns the box number calculated by running the HASH algorithm on
    a passed-in string of letters.
    """
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

def get_lens_position(box, lens_label):
    """
    Returns the index position of the lens with the matching label.
    Returns -1 if the lens is not present in the boz
    """
    return next((i for i, t in enumerate(box) if t[0] == lens_label), -1)

# Place the lenses in their respective boxes per the initialization sequence
lens_boxes = [[] for _ in range(NUM_BOXES)]
for step in initialization_sequence:
    if step[-1] == '-':
        # Remove a lens
        label = step[:-1]
        box_num = get_box_number(label)
        lens_index = get_lens_position(lens_boxes[box_num], label)
        if lens_index >= 0:
            lens_boxes[box_num].pop(lens_index)
    else:
        # Add or replace a lens
        focal_length = int(step[-1])
        label = step[:-2]
        box_num = get_box_number(label)
        lens_index = get_lens_position(lens_boxes[box_num], label)
        if lens_index >= 0:
            # Replace the lens with the matching label
            lens_boxes[box_num][lens_index] = (label, focal_length)
        else:
            # Add the lens to the end of the row
            lens_boxes[box_num].append((label, focal_length))
