"""
Advent of Code 2023
Day 8 - Haunted Wasteland (Part 2)

Solution by Jacob Barber
"""

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
current_nodes = []
for node in desert_map.keys():
    if node[2] == 'A':
        current_nodes.append(node)

# Traverse the map following the instructions, summing the number of steps
at_destination = False
num_steps = 0
i = 0
while not at_destination:
    at_destination = True
    instruction = instructions[i]

    # Update all the current nodes
    for j in range(len(current_nodes)):
        node = current_nodes[j]
        if instruction == 'L':
            current_nodes[j] = desert_map[node][0]
        else:
            current_nodes[j] = desert_map[node][1]
        if current_nodes[j][2] != 'Z':
            at_destination = False

    # Prepare for next loop
    num_steps += 1
    i += 1
    if i == len(instructions):
        i = 0

# Display total steps required
print(num_steps)