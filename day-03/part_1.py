from convert import convert_to_priority

priorities_sum = 0

with open('rucksacks.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # strip spaces and newlines
        rucksack = line.replace(" ", "").strip()

        # split rucksack into compartments
        half_rucksack_idx = int(len(rucksack)/2)
        compartment_1 = set(rucksack[:half_rucksack_idx])
        compartment_2 = set(rucksack[half_rucksack_idx:])

        # find the shared item
        shared_item = compartment_1.intersection(compartment_2)
        shared_item_to_s = ', '.join(shared_item)

        # get priority of shared item
        priority = convert_to_priority(shared_item_to_s)

        # add priority to running total
        priorities_sum += priority

print(priorities_sum)
