# rock = A = X = 1
# paper = B = Y = 2
# scissors = C = Z = 3
# lose = 0
# draw = 3
# win = 6

# total = shape selected (col 2) + result from col 2 perspective

# Wins
# Rock beats Scissors (C X)
# Scissors beats Paper (B Z)
# Paper beats Rock (A Y)

# Ties 
# (A X)
# (B Y)
# (C Z)

# Losses 
# Rock beats Scissors (A Z)
# Scissors beats Paper (C Y)
# Paper beats Rock (B X)

# example: 
# A Y --> 8
# B X --> 1
# C Z --> 6
# total score: 15

# all possible wins, ties, losses, and second letters
key = {
    "CX": 6,
    "BZ": 6,
    "AY": 6,
    "AX": 3,
    "BY": 3,
    "CZ": 3,
    "AZ": 0,
    "CY": 0,
    "BX": 0,
    "X": 1,
    "Y": 2,
    "Z": 3
}

total_score = 0

with open('data.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        # strip spaces and newlines
        parsed = line.replace(" ", "").strip()
        # look up score for letter combo + final letter and add it to the 
        # running total
        total_score += (key[parsed] + key[parsed[-1]])

print(total_score)