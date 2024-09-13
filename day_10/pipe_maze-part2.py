"""
Advent of Code 2023
Day 10 - Pipe Maze (Part 2)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(10, "Pipe Maze (Part 2)")

# Read in the map, preserving the starting position
maze_map = []
starting_position = ()
with args.input_file as file:
    row = 0
    tile = file.read(1)
    while tile != '':
        maze_row = []
        col = 0
        while tile != '\n':
            maze_row.append(tile)
            if tile == 'S':
                starting_position = (row, col)
            tile = file.read(1)
            col += 1
        maze_map.append(maze_row)
        row += 1
        tile = file.read(1)

# Construct parallel map for loop enclosures
enclosure_map = [['.'] * len(maze_map[0]) for row in maze_map]
enclosure_map[starting_position[0]][starting_position[1]] = 'S'

def get_valid_moves(maze_map, position, previous=()):
    """Returns a list of valid moves for the given position"""
    cur_row = position[0]
    cur_col = position[1]
    current_tile = maze_map[cur_row][cur_col]
    valid_moves = []

    # Check north cell
    if (current_tile in ['S', '|', 'L', 'J']
            and cur_row > 0
            and maze_map[cur_row - 1][cur_col] in ['|', 'F', '7']):
        valid_moves.append((cur_row - 1, cur_col))

    # Check east cell
    if (current_tile in ['S', '-', 'L', 'F']
            and cur_col < len(maze_map[0]) - 1
            and maze_map[cur_row][cur_col + 1] in ['-', 'J', '7']):
        valid_moves.append((cur_row, cur_col + 1))

    # Check south cell
    if (current_tile in ['S', '|', '7', 'F'] and
            cur_row < len(maze_map) - 1
            and maze_map[cur_row + 1][cur_col] in ['|', 'J', 'L']):
        valid_moves.append((cur_row + 1, cur_col))

    # Check west cell
    if (current_tile in ['S', '-', '7', 'J'] and
            cur_col > 0
            and maze_map[cur_row][cur_col - 1] in ['-', 'F', 'L']):
        valid_moves.append((cur_row, cur_col - 1))

    # Discard previous position to avoid backtracking
    if previous in valid_moves:
        valid_moves.remove(previous)

    return valid_moves


# Determine the valid starting paths and create actors for each
current_positions = get_valid_moves(maze_map, starting_position)
num_actors = len(current_positions)
prev_positions = [starting_position] * num_actors

# Trace the loop into the enclosure map
loop_complete = False
while not loop_complete:
    for i in range(num_actors):
        x = current_positions[i][0]
        y = current_positions[i][1]
        if enclosure_map[x][y] != '.':
            loop_complete = True
        else:
            enclosure_map[x][y] = maze_map[x][y]
            next_moves = get_valid_moves(maze_map, current_positions[i], prev_positions[i])
            prev_positions[i] = current_positions[i]
            # Because path is a loop, each actor will only have one valid move
            current_positions[i] = next_moves[0]
