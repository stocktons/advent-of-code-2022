def convert_to_priority(letter):
    """
    Takes in a letter and returns its numeric priority.
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    
    >>> convert_to_priority('a')
    1

    >>> convert_to_priority('B')
    28
    """
    ascii_to_elf_difference_upper = 38
    ascii_to_elf_difference_lower = 96

    # convert letter to ascii code
    ascii_code = ord(letter)

    if letter.isupper():
        return ascii_code - ascii_to_elf_difference_upper

    else:
        return ascii_code - ascii_to_elf_difference_lower
