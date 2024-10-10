"""
Advent of Code 2023
Day 19 - Aplenty (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse arguments
args = get_args(19, "Aplenty (Part 1)")

# Comparison functions for storing in workflows
def greater_than(a, b):
    return a > b

def less_than(a, b):
    return a < b

# Parse input
with args.input_file as file:
    # Read in line sections
    input_lines = file.read().split('\n\n')
    workflow_lines = input_lines[0].splitlines()
    part_rating_lines = input_lines[1].splitlines()

# Parse workflows
workflows = {}
for line in workflow_lines:
    rule_name, rules_str = line[:-1].split('{')
    rules_str_list = rules_str.split(',')
    rules = []
    for i in range(len(rules_str_list) - 1):
        condition, destination = rules_str_list[i].split(':')
        category = condition[0]
        comparator = greater_than if condition[1] == '>' else less_than
        value = int(condition[2:])
        rules.append((category, comparator, value, destination))
    default_destination = rules_str_list[-1]
    workflows[rule_name] = (rules, default_destination)

# Parse part ratings
parts = []
for line in part_rating_lines:
    ratings = line[1:-1].split(',')
    parts.append(tuple(int(rating[2:]) for rating in ratings))
