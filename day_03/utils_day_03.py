def check_cell(cell_contents):
    """
    Checks the passed in contents of a cell to determine if it is a symbol.
    Returns true if so, otherwise returns false.
    """
    if cell_contents.isdigit() or cell_contents == '.':
        return False
    else:
        return True


def check_part_num(schematic, start_row, num_rows, start_col, num_cols, part_list):
    """
    Checks to see if number in schematic is a valid part number.
    If so, adds to the part_list list using a dictionary structure.
    Returns the column position of the last digit in the number.
    """

    # Initialize part number
    part_num_str = ''
    cur_row = start_row
    cur_col = start_col
    is_valid = False
    is_last_digit = False

    # Check upper-left adjacency
    if cur_row > 0 and cur_col > 0:
        is_valid = check_cell(schematic[cur_row - 1][cur_col - 1])

    # Check left adjacency
    if not is_valid and cur_col > 0:
        is_valid = check_cell(schematic[cur_row][cur_col - 1])

    # Check lower-left adjacency
    if not is_valid and cur_row < num_rows - 1 and cur_col > 0:
        is_valid = check_cell(schematic[cur_row + 1][cur_col - 1])

    # Iterate through the remaining digits, checking adjacent cells
    while not is_last_digit:
        # Check above adjacency
        if not is_valid and cur_row > 0:
            is_valid = check_cell(schematic[cur_row - 1][cur_col])

        # Check below adjacency
        if not is_valid and cur_col < num_cols - 1:
            is_valid = check_cell(schematic[cur_row][cur_col + 1])

        # Add the digit to the part number string
        part_num_str += schematic[cur_row][cur_col]

        # Check if digit is last digit in number
        if cur_col < num_cols - 1 and schematic[cur_row][cur_col + 1].isdigit():
            cur_col += 1
        else:
            is_last_digit = True

            # Check upper-right adjacency
            if not is_valid and cur_row > 0 and cur_col < num_cols - 1:
                is_valid = check_cell(schematic[cur_row - 1][cur_col + 1])

            # Check right adjacency
            if not is_valid and cur_col < num_cols - 1:
                is_valid = check_cell(schematic[cur_row][cur_col + 1])

            # Check lower-right adjacency
            if not is_valid and cur_row < num_rows - 1 and cur_col < num_cols - 1:
                is_valid = check_cell(schematic[cur_row + 1][cur_col + 1])

    # If valid, add number to part list and return col position of last digit
    if is_valid:
        part_list.append(int(part_num_str))
    return cur_col
