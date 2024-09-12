"""
Advent of Code 2023
Day 7 - Camel Cards (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

#* Helper Functions *#

# Types of games correspond to a list index in the following order
# 0 - High Card
# 1 - One Pair
# 2 - Two Pair
# 3 - Three of a Kind
# 4 - Full House
# 5 - Four of a Kind
# 6 - Five of a Kind
NUM_TYPES = 7

def find_hand_type(hand):
    """
    Takes in a string representing a Camel Card hand and
    returns an integer representing the hand type (see above)
    """
    # Calculate the counts for each card in the hand
    card_count = {}
    for card in hand:
        if card not in card_count:
            card_count[card] = 1
        else:
            card_count[card] += 1

    # Determine the type based on the card count
    if any(count == 5 for count in card_count.values()):
        # Five of a Kind
        return 6

    if any(count == 4 for count in card_count.values()):
        # Four of a Kind
        return 5

    num_pairs = sum(1 for count in card_count.values() if count == 2)
    if any(count == 3 for count in card_count.values()):
        if num_pairs == 1:
            # Full House
            return 4
        # Three of a Kind
        return 3

    if num_pairs == 2:
        # Two Pair
        return 2

    if num_pairs == 1:
        # One Pair
        return 1

    # High Card
    return 0

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
    """
    Takes in an unordered list of games (hands, bids) of the same type
    and returns the list sorted from weakest to strongest hand
    """
    for i in range(len(games) - 1):
        # Locate the index of the weakest hand in the sub array
        weakest = i
        for j in range(i + 1, len(games)):
            if is_stronger(games[weakest][0], games[j][0]):
                weakest = j

        # Swap the weakest game with the first game in the subarray
        games[i], games[weakest] = games[weakest], games[i]

    return games

#* Script *#

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
    game_type = find_hand_type(hand)
    games_by_type[game_type].append(game)

# Sort all the hands of a given type by strength
# then combine into a single list of games sorted by rank
games_by_rank = []
for i in range(NUM_TYPES):
    games_by_type[i] = sort_by_strength(games_by_type[i])
    games_by_rank += games_by_type[i]

# Calculate and display the total winnings for all games
total_winnings = 0
for i in range(len(games_by_rank)):
    bid = games_by_rank[i][1]
    rank = i + 1
    total_winnings += bid * rank
print(total_winnings)
