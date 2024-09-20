"""
Advent of Code 2023
Day 16 - The Floor Will Be Lava (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

# Parse arguments
args = get_args(16, "The Floor Will Be Lava (Part 1)")

# Read in input
with args.input_file as file:
    layout = np.array([list(line) for line in file.read().splitlines()], dtype='U1')

# Trace the path of each light beam through the cave
layout_height, layout_width = layout.shape
light_path = np.array([['.'] * layout_width for _ in range(layout_height)], dtype='U1')
light_beams = [((0, 0), (0, 1))]
while light_beams:
    current_pos, trajectory = light_beams[0]
    row, col = current_pos
    if not 0 <= row < layout_height or not 0 <= col < layout_width:
        # Beam has reached layout edge, end path tracing
        light_beams.pop(0)
        continue

    # Update light path with energized tile
    if light_path[row][col] == ".":
        light_path[row][col] = '#'

    # Calculate the next position for this light beam
    match layout[row][col]:
        case '.':
            # Continue in  current direction
            light_beams[0] = ((row + trajectory[0], col + trajectory[1]), trajectory)
        case '\\':
            # Rotate 90 degrees N/W or S/E
            trajectory = (trajectory[1], trajectory[0])
            light_beams[0] = ((row + trajectory[0], col + trajectory[1]), trajectory)
        case '/':
            # Rotate 90 degrees N/E or S/W
            trajectory = (-trajectory[1], -trajectory[0])
            light_beams[0] = ((row + trajectory[0], col + trajectory[1]), trajectory)
        case '|':
            # Horizontal splitter
            if trajectory[1] == 0:
                light_beams[0] = ((row + trajectory[0], col + trajectory[1]), trajectory)
            elif light_path[row][col] != 'S':
                light_beams[0] = ((row - 1, col), (-1,0))
                light_beams.append(((row + 1, col), (1, 0)))
                light_path[row][col] = 'S'
            else:
                # Splitter has already been traversed, pop to not end up in a loop
                light_beams.pop(0)
        case '-':
            # Vertical splitter
            if trajectory[0] == 0:
                light_beams[0] = ((row + trajectory[0], col + trajectory[1]), trajectory)
            elif light_path[row][col] != 'S':
                light_beams[0] = ((row, col -1), (0, -1))
                light_beams.append(((row, col + 1), (0, 1)))
                light_path[row][col] = 'S'
            else:
                # Splitter has already been traversed, pop to not end up in a loop
                light_beams.pop(0)

# Count and display the energized tiles
energized_tile_count = light_path.size - np.count_nonzero(light_path == '.')
print(energized_tile_count)