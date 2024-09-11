"""
Advent of Code 2023
Day 7 - Camel Cards (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Types of games correspond to a list index in the following order
# 0 - Five of a Kind
# 1 - Four of a Kind
# 2 - Full House
# 3 - Three of a Kind
# 4 - Two Pair
# 5 - One Pair
# 6 - High Card
NUM_TYPES = 7

def find_hand_type(hand):
    """
    Takes in a string representing a Camel Card hand and
    returns an integer representing the hand type (see above)
    """
    # Determine the counts for each card in the hand
    card_count = {}
    for card in hand:
        if card not in card_count:
            card_count[card] = 1
        else:
            card_count[card] += 1

    # Determine the type based on the card count
    # Five of a Kind
    if any(count == 5 for count in card_count.values()):
        return 0

    # Four of a Kind
    if any(count == 4 for count in card_count.values()):
        return 1

    # Four of a Kind
    if any(count == 3 for count in card_count.values()):
        # Full House
        if any(count == 2 for count in card_count.values()):
            return 2
        # Three of a Kind
        else:
            return 3

    num_pairs = sum(1 for count in card_count.values() if count == 2)
    # Two Pair
    if num_pairs == 2:
        return 4
    # One Pair
    if num_pairs == 1:
        return 5
    # High Card
    else:
        return 6

# Parse arguments
args = get_args(7, "Camel Cards (Part 1)")

# Read in hands and bids
games = []
with args.input_file as file:
    for line in file:
        hand, bid = line.split()
        games.append((hand, int(bid)))

# Arrange games by type
games_by_type = [[] for _ in range(NUM_TYPES)]
for game in games:
    hand = game[0]
    type = find_hand_type(hand)
    games_by_type[type].append(game)
