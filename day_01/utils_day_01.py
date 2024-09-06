def name_to_digit(str):
    """Converts a string representing the name of a single digit
    to the corresponding character 1-9, returns '0' on error
    """
    match str:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
        case _:
            return '0'
