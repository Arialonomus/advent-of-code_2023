def check_part_num(schematic, start_row, num_rows, start_col, num_cols, gear_list):
    """
    Checks to see if part number is adjacent to a gear. If so adds it to the gear_list
    dictionary, appending it to the list of part numbers for the gear at that position.
    Returns the column position of the last digit of the part number.
    """

    # Initialize variables
    part_num_str = ''
    adjacent_cells = []
    cur_row = start_row
    cur_col = start_col
    is_last_digit = False

    # Build the adjacent cell list
    # Upper-left adjacent
    if cur_row > 0 and cur_col > 0:
        adjacent_cells.append((cur_row - 1, cur_col - 1))

    # Left adjacent
    if cur_col > 0:
        adjacent_cells.append((cur_row, cur_col - 1))

    # Lower-left adjacent
    if cur_row < num_rows - 1 and cur_col > 0:
        adjacent_cells.append((cur_row + 1, cur_col - 1))

    # Iterate through the remaining digits, logging adjacent cells
    while not is_last_digit:
        # Above adjacent
        if cur_row > 0:
            adjacent_cells.append((cur_row - 1, cur_col))

        # Below adjacent
        if cur_row < num_rows - 1:
            adjacent_cells.append((cur_row + 1, cur_col))

        # Add the digit to the part number string
        part_num_str += schematic[cur_row][cur_col]

        # Check if digit is last digit in number
        if cur_col < num_cols - 1 and schematic[cur_row][cur_col + 1].isdigit():
            cur_col += 1
        else:
            is_last_digit = True

            # Upper-right adjacent
            if cur_row > 0 and cur_col < num_cols - 1:
                adjacent_cells.append((cur_row - 1, cur_col + 1))

            # Right adjacent
            if cur_col < num_cols - 1:
                adjacent_cells.append((cur_row, cur_col + 1))

            # Lower-right adjacent
            if cur_row < num_rows - 1 and cur_col < num_cols - 1:
                adjacent_cells.append((cur_row + 1, cur_col + 1))

    # Cycle through list of adjacent cells to see if any is a gear
    gear_pos = ()
    has_gear = False
    i = 0
    while i < len(adjacent_cells) and not has_gear:
        if schematic[adjacent_cells[i][0]][adjacent_cells[i][1]] == '*':
            gear_pos = (adjacent_cells[i][0], adjacent_cells[i][1])
            if gear_pos in gear_list.keys():
                gear_list[gear_pos].append(int(part_num_str))
            else:
                gear_list[gear_pos] = [int(part_num_str)]
            has_gear = True
        else:
            i += 1

    # Return position of last digit to continue search
    return cur_col
