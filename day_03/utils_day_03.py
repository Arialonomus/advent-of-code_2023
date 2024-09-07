def check_cell(cell_contents):
    """
    Checks the passed in contents of a cell to determine if it is a symbol.
    Returns true if so, otherwise returns false.
    """
    if cell_contents.isdigit() or check_cell == '.':
        return False
    else:
        return True
