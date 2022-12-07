from convert import convert_to_priority

badges_sum = 0
elf_group = []

with open('rucksacks.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # strip spaces and newlines
        rucksack = line.replace(" ", "").strip()

        # limit an elf group to 3 elves at a time
        if len(elf_group) < 4:
            elf_group.append(rucksack)

        # when there are 3 elves in the group
        if len(elf_group) == 3:
            # create sets from each elf's rucksack 
            group_rucksacks = [set(group) for group in elf_group]

            # find the common item/badge among rucksacks
            badge = group_rucksacks[0].intersection(group_rucksacks[1], group_rucksacks[2])
            badge_to_s = ', '.join(badge)

            # look up the priority value of the badge and add it to the running total 
            priority = convert_to_priority(badge_to_s)
            badges_sum += priority

            # clear the elves to make room for the next group of 3
            elf_group = []
            
print(badges_sum)

