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

    # Construct the almanac by parsing the remainder of the file
    almanac = []
    line = file.readline()      # Consume newline before first mapping
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
    locations = []
    for i in range(0, len(seed_ranges)):
        seed_range = seed_ranges[i]
        locations.append(seed_range[0])
        for seed in range(seed_range[0], seed_range[1]):
            for entry in almanac:
                mapping_found = False
                j = 0
                while j < len(entry['mapping']) and not mapping_found:
                    mapping = entry['mapping'][j]
                    if mapping[1] > seed >= mapping[0]:
                        seed += mapping[2]
                        mapping_found = True
                    else:
                        j += 1
            if seed < locations[i]:
                locations[i] = seed

    # Determine and print the lowest location
    lowest_location = min(locations)
    print(lowest_location)
