import argparse


def get_args(day, puzzle_name):
    """
    Boilerplate for parsing input file arguments for Advent of Code puzzles
    """

    # Set up description string
    puzzle_str = str(day) + ' puzzle - "' + puzzle_name + '"'
    desc_str = 'A solution to Advent of Code 2023 day ' + puzzle_str

    # Parse arguments
    parser = argparse.ArgumentParser(description=desc_str)
    parser.add_argument('input_file',
                        type=argparse.FileType('r'),
                        help="Input file path")
    return parser.parse_args()
