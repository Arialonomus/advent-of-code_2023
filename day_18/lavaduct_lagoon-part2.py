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
    num_boundary_points = 0 # Number of boundary points will always be the sum of the distances
    vertices = [(0,0)]
    x, y = 0, 0
    for line in file:
        # Parse the hex code into direction and distance
        hex_string = line.strip()[-7:-1]
        direction = int(hex_string[-1])
        distance = int(hex_string[:-1], 16)

        # Accumulate boundary points
        num_boundary_points += distance

        # Calculate the next vertex in the shape
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

# Apply the shoelace formula to calculate the area of the shape
num_vertices = len(vertices)
area_sum = 0
for i in range(num_vertices - 1):
    x1, y1 = vertices[i]
    x2, y2 = vertices[i + 1]
    area_sum += ((x1 * y2) - (x2 * y1))
area = abs(area_sum) // 2

# Calculate the total number of points enclosed in the shape using Pick's Theorem
num_interior_points = area - (num_boundary_points // 2) + 1
lagoon_size = num_interior_points + num_boundary_points
print(lagoon_size)
