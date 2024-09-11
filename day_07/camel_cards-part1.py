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

def get_value(card):
    """
    Returns the numerical value of a passed in card
    """
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 11
        case 'T':
            return 10
        case _:
            return int(card)

def is_stronger(hand_a, hand_b):
    """
    Compares two passed in hands, and returns True if hand_a is
    stronger than hand_b
    """
    for i in range(len(hand_a)):
        card_a = get_value(hand_a[i])
        card_b = get_value(hand_b[i])
        if card_a == card_b:
            continue
        if card_a > card_b:
            return True
        if card_a < card_b:
            return False

def sort_by_strength(games):
    """Takes in an unordered list of games (hands, bids) of the same type
    and returns the list sorted from weakest to strongest hand"""
    for i in range(len(games) - 1):
        # Locate the index of the weakest hand in the sub array
        weakest = i
        for j in range(i + 1, len(games)):
            if is_stronger(games[weakest][0], games[j][0]):
                weakest = j

        # Swap the weakest game with the first game in the subarray
        games[i], games[weakest] = games[weakest], games[i]

    return games

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

# Sort all the hands of a given type by strength
for i in range(NUM_TYPES):
    games_by_type[i] = sort_by_strength(games_by_type[i])
