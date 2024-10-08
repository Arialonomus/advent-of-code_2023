"""
Advent of Code 2023
Day 17 - Clumsy Crucible (Part 2)

Solution by Jacob Barber
"""

import numpy as np
import heapq
from aoc_utils import get_args

INF_INT = np.iinfo(np.int64).max
MIN_NUM_BLOCKS = 4
MAX_NUM_BLOCKS = 10

# Parse arguments
args = get_args(17, "Clumsy Crucible (Part 2)")

# Read in input
with args.input_file as file:
    city_map = np.array([list(line) for line in file.read().splitlines()], dtype=int)

def find_minimal_path(heat_map, start_pos, goal_pos):
    """
    Find the path with the smallest heat loss using a modified
    Dijkstra's algorithm with directional states.
    """

    height, width = heat_map.shape

    def get_tile_position(position, direction):
        """
        Returns the position of the adjacent grid tile in the orthogonal direction.
        Returns an empty tuple if the tile is not valid (i.e. is off the grid edge)
        """
        new_row, new_col = position
        match direction:
            case 'N':
                new_row -= 1
            case 'E':
                new_col += 1
            case 'S':
                new_row += 1
            case 'W':
                new_col -= 1

        if 0 <= new_row < height and 0 <= new_col < width:
            new_position = (new_row, new_col)
            return new_position

        return ()

    heat_loss = np.full((height, width, 4, MAX_NUM_BLOCKS), INF_INT)
    direction_map = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    priority_queue = []
    start_directions = ['N', 'E', 'S', 'W']

    # Check all possible starting directions
    for start_dir in start_directions:
        next_pos = get_tile_position(start_pos, start_dir)
        if next_pos:
            next_row, next_col = next_pos
            dir_index = direction_map[start_dir]
            heat_loss[next_row][next_col][dir_index][0] = heat_map[next_row][next_col]
            heapq.heappush(priority_queue, (heat_map[next_row][next_col], next_pos, dir_index, 0))

    # Direction dictionaries
    left = { 'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S' }
    right = { 'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N' }

    while priority_queue:
        # Check the tile with the lowest heat loss in the priority queue
        current_heat_loss, current_pos, current_dir_index, current_num_blocks = heapq.heappop(priority_queue)

        # If we've reached the end we can stop early
        if current_pos == goal_pos:
            return current_heat_loss

        # Build the list of directions to explore
        current_dir = list(direction_map.keys())[current_dir_index]
        directions = []
        if current_num_blocks >= MIN_NUM_BLOCKS - 1:
            directions = [left[current_dir], right[current_dir]]
        if current_num_blocks < MAX_NUM_BLOCKS - 1:
            directions.append(current_dir)

        # Explore the valid directions
        for next_dir in directions:
            next_pos = get_tile_position(current_pos, next_dir)
            if next_pos:
                next_row, next_col = next_pos
                new_heat_loss = current_heat_loss + heat_map[next_row][next_col]
                next_dir_index = direction_map[next_dir]
                new_num_blocks = current_num_blocks + 1 if next_dir == current_dir else 0

                # If a more minimal path to the neighbor is found, update it
                if new_heat_loss < heat_loss[next_row][next_col][next_dir_index][new_num_blocks]:
                    heat_loss[next_row][next_col][next_dir_index][new_num_blocks] = new_heat_loss
                    heapq.heappush(priority_queue, (new_heat_loss, next_pos, next_dir_index, new_num_blocks))

# Find the minimal path from the top-left to bottom-right tiles
start = (0, 0)
end = (city_map.shape[0] - 1, city_map.shape[1] - 1)
minimal_heat_loss = find_minimal_path(city_map, start, end)
print(minimal_heat_loss)