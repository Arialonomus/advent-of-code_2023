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
    part_dictionary = {
        'x': int(ratings[0][2:]),
        'm': int(ratings[1][2:]),
        'a': int(ratings[2][2:]),
        's': int(ratings[3][2:])
    }
    parts.append(part_dictionary)

# Determine the accepted parts based on the ratings and workflows
sum_accepted_parts = 0
for part in parts:
    target_rule = 'in' # Always begin with the rule 'in'

    # Move through workflows until a part is accepted or rejected
    while target_rule not in ['R', 'A']:
        # Get the rules for this workflow
        rules_list, default_rule = workflows[target_rule]

        # Iterate through rules until a match is found
        num_rules = len(rules_list)
        match_found = False
        i = 0
        while i < num_rules and not match_found:
            rule_category, comparison_function, comparison_value, target_if_true = rules_list[i]
            test_value = part[rule_category]
            if comparison_function(test_value, comparison_value):
                target_rule = target_if_true
                match_found = True
            i += 1

        # Use the default destination if no match was found
        if not match_found:
            target_rule = default_rule

    # Add the accepted part ratings to the sum
    if target_rule == 'A':
        sum_accepted_parts += sum(part.values())

# Print the final sum of the ratings of accepted parts
print(sum_accepted_parts)
