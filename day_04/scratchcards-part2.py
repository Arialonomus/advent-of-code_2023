"""
Advent of Code 2023
Day 4 - Scratchcards (Part 2)

Solution by Jacob Barber
"""

from aoc_utils import get_args

def count_elements(input_list):
    """Recursively counts the elements in a list, including nested list elements"""
    total = 0
    for element in input_list:
        if isinstance(element, list):
            total += count_elements(element)
        else:
            total += 1
    return total

# Parse arguments
args = get_args(4, "Scratchcards")

with args.input_file as file:
    # Build dictionary of scratchcards
    scratchcards = {}
    for line in file:
        # Split each game into game ID and numbers
        line = line.strip()
        game_id_str, numbers_str = line.split(': ')
        game_id = int(game_id_str.strip('Card '))

        # Separate the winning and owned numbers into integer lists
        winning_nums_str, my_nums_str = numbers_str.split('|')
        winning_nums = list(map(int, winning_nums_str.split()))
        my_nums = list(map(int, my_nums_str.split()))

        # Assemble the cards into the dictionary
        scratchcards[game_id] = {
            "winning": winning_nums,
            "mine": my_nums
        }

    # Calculate the number of matches for each scratchcard
    num_original = len(scratchcards)
    matches = [0] * num_original
    for card in scratchcards:
        for num in scratchcards[card]["winning"]:
            if num in scratchcards[card]["mine"]:
                matches[card - 1] += 1

    # Construct a list tree for the cards won
    cards_won = [0] * num_original
    for i in range(num_original - 1, -1, -1):
        cards_won[i] = [i+1]
        if matches[i] > 0:
            for j in range(i + 1, i + matches[i] + 1):
                cards_won[i].append(cards_won[j])

    # Count and print the number of cards won
    num_cards = count_elements(cards_won)
    print(num_cards)