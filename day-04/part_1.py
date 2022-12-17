from utils import find_lower, find_higher

# check which elf's first section is <= the other's
# then check if that elf's last section is >= the other's
# if true, add to count

contained_sections = 0

with open('camp-sections.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # strip newlines
        elf_sections = line.strip()

        elf_1, elf_2 = elf_sections.split(",")

        first_elf = find_lower(elf_1, elf_2)
        last_elf = find_higher(elf_1, elf_2)

        if first_elf == last_elf:
            contained_sections += 1

print(contained_sections)





