# Find the 3 elves carrying the most calories

# track the three highest counts
highest = [0, 0, 0]

# current elf's running tally
current = 0

# read the numbers from the data file
with open('data.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # line contains a number, add it to the current tally
        if line.strip() != "":
            current += int(line)

        else:
            # it's a blank line.
            # we are at the end of an elf, so see what the total is and check to see if it's greater than 
            # any number in the top 3
            if (current > min(highest)):
                # if, so find the current lowest of the highest, and replace it with the new number
                highest[highest.index(min(highest))] = current
    
            # reset the counter for the next elf
            current = 0

print(highest)
print(sum(highest))