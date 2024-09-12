"""
Advent of Code 2023
Day 8 - Haunted Wasteland (Part 2)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

# Parse arguments
args = get_args(8, "Haunted Wasteland (Part 2)")

# Read in input from file
desert_map = {}
with args.input_file as file:
    instructions = file.readline().rstrip()
    file.readline() # Consume newline
    translation_table = str.maketrans('', '', '=(,)')
    for line in file:
        node, left, right = line.translate(translation_table).split()
        desert_map[node] = (left, right)

# Construct the list of starting nodes
starting_nodes = []
for node in desert_map.keys():
    if node[2] == 'A':
        starting_nodes.append(node)
num_starting_nodes = len(starting_nodes)

# Each starting node only has one looping path,
# count the number of steps for each path
step_counts = []
for starting_node in starting_nodes:
    current_node = starting_node
    num_steps = 0
    ins_idx = 0

    # Follow instructions until ending node is reached
    while current_node[2] != 'Z':
        instruction = instructions[ins_idx]
        if instruction == 'L':
            current_node = desert_map[current_node][0]
        else:
            current_node = desert_map[current_node][1]
        num_steps += 1
        # Loop to instruction start, if necessary
        ins_idx = (ins_idx + 1) % len(instructions)

    step_counts.append(num_steps)

# Display total steps required
steps_required = np.lcm.reduce(step_counts)
print(steps_required)