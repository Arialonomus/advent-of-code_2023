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

# Construct parallel map for loop enclosures with additional 1 tile border
num_puzzle_rows = len(maze_map)
num_puzzle_cols = len(maze_map[0])
enclosure_map = [['.'] * (num_puzzle_cols + 2) for row in range(num_puzzle_rows + 2)]
enclosure_map[starting_position[0] + 1][starting_position[1] + 1] = 'S'

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
        if enclosure_map[x + 1][y + 1] != '.':
            loop_complete = True
        else:
            enclosure_map[x + 1][y + 1] = maze_map[x][y]
            next_moves = get_valid_moves(maze_map, current_positions[i], prev_positions[i])
            prev_positions[i] = current_positions[i]
            # Because path is a loop, each actor will only have one valid move
            current_positions[i] = next_moves[0]

# Expand the enclosure map and copy the enclosure map over
expanded_enclosure_map = [['#'] * (2 * (num_puzzle_cols + 2)) for row in range(2 * (num_puzzle_rows + 2))]
for i in range(len(enclosure_map)):
    for j in range(len(enclosure_map[0])):
        tile = enclosure_map[i][j]
        expanded_enclosure_map[i * 2][j * 2] = tile
        match tile:
            case 'F':
                expanded_enclosure_map[(i * 2) + 1][(j * 2)] = '|'
                expanded_enclosure_map[(i * 2)][(j * 2) + 1] = '-'
            case '7':
                expanded_enclosure_map[(i * 2) + 1][(j * 2)] = '|'
                expanded_enclosure_map[(i * 2)][(j * 2) - 1] = '-'
            case 'J':
                expanded_enclosure_map[(i * 2) - 1][(j * 2)] = '|'
                expanded_enclosure_map[(i * 2)][(j * 2) - 1] = '-'
            case 'L':
                expanded_enclosure_map[(i * 2) - 1][(j * 2)] = '|'
                expanded_enclosure_map[(i * 2)][(j * 2) + 1] = '-'
            case '|':
                expanded_enclosure_map[(i * 2) - 1][(j * 2)] = '|'
                expanded_enclosure_map[(i * 2) + 1][(j * 2)] = '|'
            case '-':
                expanded_enclosure_map[(i * 2)][(j * 2) - 1] = '-'
                expanded_enclosure_map[(i * 2)][(j * 2) + 1] = '-'

for line in expanded_enclosure_map:
    print(''.join(line))