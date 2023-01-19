## Mapping out sample movements to confirm algorithm

head_pos = [4, 0]
tail_pos = [4, 0] # mark with #

# R 4
# if R or L we change head_pos[1]
# loop until head_pos[1] = head_pos[1] + 4

# MOVE
head_pos = [4, 1]

# is tail_pos[1] > 1 away? 
# No. 
# Don't move
tail_pos = [4, 0]

# MOVE
head_pos = [4, 2]

# is tail_pos[1] > 1 away? 
# Yes. 
# Move
tail_pos = [4, 1]
# mark

# MOVE
head_pos = [4, 3]

# is tail_pos > 1 away? 
# Yes. 
# Move
tail_pos = [4, 2]
# mark

# MOVE
head_pos = [4, 4]

# is tail_pos > 1 away? 
# Yes. 
# Move
tail_pos = [4, 3]
# mark

# end 

############################

head_pos = [4, 4]
tail_pos = [4, 3]

# U 4
# if U or D we change head_pos[0]

# loop until head_pos[0] = head_pos[0] - 4

# MOVE
head_pos = [3, 4]
# is tail_pos > 1 away? 
# No. 
# Don't move.
tail_pos = [4, 3]

# MOVE
head_pos = [2, 4]
# is tail_pos[0] > 1 away?
# Yes.
# Move [0] and match [1]
tail_pos = [3, 4]
# mark

# MOVE
head_pos = [1, 4]
# is tail_pos[0] > 1 away? 
# Yes.
# Move [0] and match [1] 
tail_pos = [2, 4]
# mark

# MOVE 
head_pos = [0, 4]
# is tail_pos[0] > 1 away?
# Yes.
# Move [0] and match [1]
tail_pos = [1, 4]

################

# L 3
# if R or L we change head_pos[1]
# loop until head_pos[1] = head_pos[1] - 3

head_pos = [0, 4]
tail_pos = [1, 4]

# MOVE
head_pos = [0, 3]
# is tail_pos[1] > 1 away? 
# No. 
# Don't move
tail_pos = [1, 4]

# MOVE
head_pos = [0, 2]
# is tail_pos[1] > 1 away?
# Yes. 
# Move [1] and match [0]
tail_pos = [0, 3]
# mark

# MOVE 
head_pos = [0, 1]
# is tail_pos[1] > 1 away? 
# Yes.
# Move [1] and match [0]
tail_pos = [0, 2]
# mark


############################

head_pos = [0, 1]
tail_pos = [0, 2]

# D 1
# if U or D we change head_pos[0]

# loop until head_pos[0] = head_pos[0] + 1

# MOVE
head_pos = [1, 1]
# is tail_pos[0] > 1 away? 
# No. 
# Don't move.
tail_pos = [0, 2]


################

# R 4
# if R or L we change head_pos[1]
# loop until head_pos[1] = head_pos[1] - 4

head_pos = [1, 1]
tail_pos = [0, 2]

# MOVE
head_pos = [1, 2]
# is tail_pos[1] > 1 away? 
# No. 
# Don't move
tail_pos = [0, 2]

# MOVE
head_pos = [1, 3]
# is tail_pos[1] > 1 away?
# No. 
# Don't move
tail_pos = [0, 2]

# MOVE
head_pos = [1, 4]
# is tail_pos[1] > 1 away? 
# Yes. 
# Move [1] and match [0]
tail_pos = [1, 3]
# mark

# MOVE
head_pos = [1, 5]
# is tail_pos[1] > 1 away? 
# Yes. 
# Move [1] and match [0]
tail_pos = [1, 4]









