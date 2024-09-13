"""
Advent of Code 2023
Day 10 - Pipe Maze (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(10, "Pipe Maze (Part 1)")

# Read in the map, preserving the starting position
maze_map = []
starting_pos = ()
with args.input_file as file:
    row = 0
    tile = file.read(1)
    while tile != '':
        maze_row = []
        col = 0
        while tile != '\n':
            maze_row.append(tile)
            if tile == 'S':
                starting_pos = (row, col)
            tile = file.read(1)
            col += 1
        maze_map.append(maze_row)
        row += 1
        tile = file.read(1)

# Construct parallel map for loop distances
loop_distances = [[0] * len(maze_map[0]) for row in maze_map]
loop_distances[starting_pos[0]][starting_pos[1]] = 'S'

def get_valid_moves(maze_map, position):
    """Returns a list of valid moves for the given position"""
    row = position[0]
    col = position[1]
    current_tile = maze_map[row][col]
    valid_moves = []

    # Check north cell
    if (current_tile in ['S', '|', 'L', 'J']
            and row > 0
            and maze_map[row - 1][col] in ['|', 'F', '7']):
        valid_moves.append((row - 1, col))

    # Check east cell
    if (current_tile in ['S', '-', 'L', 'F']
            and col < len(maze_map[0]) - 1
            and maze_map[row][col + 1] in ['-', 'J', '7']):
        valid_moves.append((row, col + 1))

    # Check south cell
    if (current_tile in ['S', '|', '7', 'F'] and
            row < len(maze_map) - 1
            and maze_map[row + 1][col] in ['|', 'J', 'L']):
        valid_moves.append((row + 1, col))

    # Check west cell
    if (current_tile in ['S', '-', '7', 'J'] and
            col > 0
            and maze_map[row][col - 1] in ['-', 'F', 'L']):
        valid_moves.append((row, col - 1))

    return valid_moves

# Traverse the loop with 2 actors until loop is mapped
distance = 0
loop_complete = False
actor_a_pos, actor_b_pos = get_valid_moves(maze_map, starting_pos)
while not loop_complete:
    distance += 1

    # Actor A
    loop_distances[actor_a_pos[0]][actor_a_pos[1]] = distance
    actor_a_moves = get_valid_moves(maze_map, actor_a_pos)
    if loop_distances[actor_a_moves[0][0]][actor_a_moves[0][1]] == 0:
        actor_a_pos = actor_a_moves[0]
    else:
        actor_a_pos = actor_a_moves[1]

    # Actor B
    if loop_distances[actor_b_pos[0]][actor_b_pos[1]] != 0:
        loop_complete = True
    else:
        loop_distances[actor_b_pos[0]][actor_b_pos[1]] = distance
        actor_b_moves = get_valid_moves(maze_map, actor_b_pos)
        if loop_distances[actor_b_moves[0][0]][actor_b_moves[0][1]] == 0:
            actor_b_pos = actor_b_moves[0]
        else:
            actor_b_pos = actor_b_moves[1]

# Display final distance
print(distance)