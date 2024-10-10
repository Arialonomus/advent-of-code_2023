"""
Advent of Code 2023
Day 18 - Lavaduct Lagoon (Part 2)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(18, "Lavaduct Lagoon (Part 2)")

# Read in input and parse the instructions into vertices
with args.input_file as file:
    vertices = [(0,0)]
    x, y = 0, 0
    for line in file:
        hex_string = line.strip()[-7:-1]
        direction = int(hex_string[-1])
        distance = int(hex_string[:-1], 16)
        match direction:
            # Right
            case 0:
                x += distance
            # Down
            case 1:
                y -= distance
            # Left
            case 2:
                x -= distance
            # Up
            case 3:
                y += distance
        vertices.append((x,y))

# Calculate the boundary points and area sum for the shape
num_boundary_points = 0
num_vertices = len(vertices)
area_sum = 0
for i in range(num_vertices - 1):
    # For each pair of vertices, we will count the points along the line
    vertex1, vertex2 = vertices[i], vertices[i + 1]
    x1, y1 = vertex1
    x2, y2 = vertex2

    # Since all lines are horizontal or vertical, one result will always be zero
    num_boundary_points += max(abs(x2 - x1), abs(y2 - y1))

    # Calculate the area sum for use in the shoelace formula
    area_sum += ((x1 * y2) - (x2 * y1))

# Apply the shoelace formula to get the integer area of the shape
area = abs(area_sum) // 2

# Calculate the total number of points enclosed in the shape using Pick's Theorem
num_interior_points = area - (num_boundary_points // 2) + 1
lagoon_size = num_interior_points + num_boundary_points
print(lagoon_size)
