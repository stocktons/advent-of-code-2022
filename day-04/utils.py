def find_lower(elf_1, elf_2):
    """Takes in two elves' cleaning sections and returns the 
    number of the elf who starts with the lower-numbered section.

    If there is a tie, favor the elf with the larger section.
    
    >>> find_lower('2-4', '6-8')
    1

    >>> find_lower('100-199', '99-300')
    2

    >>> find_lower('100-199', '100-199')
    1

    >>> find_lower('100-199', '100-150')
    1
    """

    elf_1_start, elf_1_end, elf_1_length = get_elf_info(elf_1)
    elf_2_start, elf_2_end, elf_2_length = get_elf_info(elf_2)

    # if the first number is the same, return the longest elf section
    if elf_1_start == elf_2_start:
        return 1 if elf_1_length >= elf_2_length else 2

    # the the first numbers are different, find the lower one
    return 1 if elf_1_start < elf_2_start else 2


def find_higher(elf_1, elf_2):
    """Takes in two elves' cleaning sections and returns the 
    number of the elf who ends with the higher-numbered section.
    
    If there is a tie, favor the elf with the larger section.

    >>> find_higher('2-4', '6-8')
    2

    >>> find_higher('100-199', '99-198')
    1

    >>> find_higher('100-199', '100-199')
    1

    >>> find_higher('99-150', '100-150')
    1
    """

    elf_1_start, elf_1_end, elf_1_length = get_elf_info(elf_1)
    elf_2_start, elf_2_end, elf_2_length = get_elf_info(elf_2)

    # if last number is the same, return the longest elf section 
    if elf_1_end == elf_2_end:
        return 1 if elf_1_length >= elf_2_length else 2

    return 1 if elf_1_end > elf_2_end else 2


def get_elf_info(elf):
    """Take in a string that represents an elf's cleaning area, like '99-150'.
    Return a list with the starting number, ending number, and the length of the 
    section as integers, like:
    [99, 150, 51]

    >>> get_elf_info('99-150')
    [99, 150, 51]
    """
    elf_start, elf_end = elf.split("-")
    elf_length = abs(int(elf_start) - int(elf_end))

    return [int(elf_start), int(elf_end), elf_length]
