"""
Advent of Code 2023
Day 5 - If You Give A Seed A Fertilizer (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(5, "If You Give A Seed A Fertilizer")

with args.input_file as file:
    # Parse the list of initial seed numbers
    initial_seeds = list(map(int, file.readline().rstrip().strip("seeds: ").split()))

    # Construct the almanac by parsing the remainder of the file
    almanac = []
    line = file.readline()      # Consume newline for first mapping
    # Read in lines until EOF
    while line != '':
        mapping_title = file.readline().rstrip(" map:\n")
        mapping = []
        line = file.readline()  # Read first mapping line
        # Parse each mapping line into tuple of range start, range end, and function map
        while line != '\n' and line != '':
            destination, source, range_len = list(map(int, line.rstrip().split()))
            mapping.append((source, source + range_len, destination - source))
            line = file.readline()
        almanac.append({
            'title': mapping_title,
            'mapping': sorted(mapping)
        })

    # Calculate the locations for each seed
    locations = initial_seeds
    for entry in almanac:
        for i in range(0, len(locations)):
            mapping_found = False
            j = 0
            while j < len(entry['mapping']) and not mapping_found:
                mapping = entry['mapping'][j]
                if mapping[1] > locations[i] >= mapping[0]:
                    locations[i] += mapping[2]
                    mapping_found = True
                else:
                    j += 1

    # Determine and print the lowest location
    lowest_location = min(locations)
    print(lowest_location)
