from utils import find_lower, find_higher, get_elf_info

# Compare two elves' ranges. Find if the highest number of the lower range is 
# greater than or equal to the lowest of the higher range. If it is, add 1 to the 
# overlapping_sections count.
# For example: [1, 4] and [2, 5]
# The lower range is [1, 4], and the highest number of that range is 4.
# The higher range is [2, 5], and the lowest number of that range is 2. 
# 4 is greater than or equal to 2, so the ranges overlap, and we'd add 1 to 
# the count. 
# Return the number of overlapping sections.

overlapping_sections = 0

with open('camp-sections.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # strip newlines
        elf_sections = line.strip()

        elf_1, elf_2 = elf_sections.split(",")

        first_elf = find_lower(elf_1, elf_2) # returns 1 or 2

        # if it's a 1, elf_1 is lower
        if first_elf == 1:
            first_elf_high = get_elf_info(elf_1)[1]
        else: 
            first_elf_high = get_elf_info(elf_2)[1]

        last_elf = find_higher(elf_1, elf_2) # returns 1 or 2

        # if it's a 1, elf_1 is higher
        if last_elf == 1:
            last_elf_low = get_elf_info(elf_1)[0]
        else: 
            last_elf_low = get_elf_info(elf_2)[0]

        if first_elf_high >= last_elf_low:
            overlapping_sections += 1

print(overlapping_sections)





