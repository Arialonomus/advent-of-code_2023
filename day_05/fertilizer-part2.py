"""
Advent of Code 2023
Day 5 - If You Give A Seed A Fertilizer (Part 2)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(5, "If You Give A Seed A Fertilizer")

with args.input_file as file:
    # Parse the list of seed ranges
    initial_seeds = list(map(int, file.readline().rstrip().strip("seeds: ").split()))
    seed_ranges = []
    j = 0
    while j < len(initial_seeds) - 1:
        seed_ranges.append((initial_seeds[j], initial_seeds[j] + initial_seeds[j + 1]))
        j += 2
    seed_ranges.sort()

    # Construct the almanac by parsing the remainder of the file
    almanac = []
    line = file.readline()      # Consume newline before first mapping
    # Read in lines until EOF
    while line != '':
        mapping_title = file.readline().rstrip(" map:\n")
        mapping = []
        line = file.readline()  # Read first mapping line
        while line != '\n' and line != '':
            # Parse line into tuple of range start, range end, and transformation
            destination, source, range_len = list(map(int, line.rstrip().split()))
            mapping.append((source, source + range_len, destination - source))

            # Read in next line
            line = file.readline()
        almanac.append(sorted(mapping))

# Map the input ranges to their final locations
inputs = seed_ranges
outputs = []
for mapping_set in almanac:
    while inputs:
        input_start, input_end = inputs.pop(0)
        match_found = False
        i = 0
        while i < len(mapping_set) and not match_found:
            map_range_start, map_range_end, transformation = mapping_set[i]
            if input_start < map_range_end:
                # Input range within ending boundary of map range
                if input_start < map_range_start:
                    # Input range start falls before or between mappings
                    output_start = input_start
                    if input_end < map_range_start:
                        # Input range is outside any mapping
                        output_end = input_end
                    else:
                        # Subdivide input range with new start boundary at map start
                        output_end = map_range_start
                        inputs.insert(0, (map_range_start, input_end))
                else:
                    # Input range within starting boundary of map range
                    output_start = input_start + transformation
                    if input_end < map_range_end:
                        # Input range fully contained in map range
                        output_end = input_end + transformation
                    else:
                        # Subdivide input range with new start boundary at map end
                        output_end = map_range_end + transformation
                        inputs.insert(0, (map_range_end, input_end))
                outputs.append((output_start, output_end))
                match_found = True
            i += 1
        if not match_found:
            # Input range falls beyond outer bounds of all mappings in this step
            outputs.append((input_start, input_end))

    # Swap buffers for next iteration
    inputs = sorted(outputs)
    outputs = []

# Final locations will be stored in inputs
locations = inputs
lowest_location_number = locations[0][0]
print(lowest_location_number)