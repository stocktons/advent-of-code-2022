from part_1 import create_grid, starting_coords

grid = create_grid("sample-rope.txt")

# head moves
# # move all other knots as needed

# create a list to hold all the knot positions
# iterate over the list and update each coord after each head move
# by comparing each index to the one before it

# start
[[4, 0], [4, 0], [4, 0],[4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0]]

# R4

[[4, 1], ...]

def move_head(row_or_col, sign):
    return f"head_pos[{row_or_col}] {sign}= 1"

def update_tail_position_on_grid(grid, rope_tail_coords):
    # grab the current tail location from the rope array
    tail_row, tail_col = rope_tail_coords
    # update the current tail location on the grid
    grid[tail_row][tail_col] = "#"

def track_tail_pt_2(file, grid, start_coords, num_knots=10):
    print("grid at start", grid)

    with open(file, 'r', encoding="utf-8") as f:

        row, col = start_coords
        head_pos = [row, col]
        # create a list to represent the rope with all knots at the starting position
        # must make a deep copy of head_pos, otherwise every index in rope gets updated when
        # head_pos is updated
        head_pos_copy = head_pos[:]
        rope = [head_pos_copy for i in range(num_knots)]
        print("new rope at top", rope)
        grid[row][col] = "#"

        lines = f.readlines()

        for line in lines:
            direction, steps = line.strip().split(" ")
            num_steps = int(steps)

            for i in range(num_steps):
                if direction == "R":
                    print("moving right")
                    # move head to the right
                    head_pos[1] += 1
                    # update rope list with new head position
                    rope[0] = head_pos

                    # move each subsequent knot in the rope if needed
                    for i in range(len(rope) - 1):
                        # think of the knots in pairs, a lead and a next
                        lead_knot_pos = i
                        next_knot_pos = i + 1
                        # if the lead gets too far away, scootch the next up to
                        # be within range
                        if abs(rope[lead_knot_pos][1] - rope[next_knot_pos][1]) > 1:
                            rope[next_knot_pos] = [rope[lead_knot_pos][0], rope[next_knot_pos][1] + 1]
                    # # grab the current tail location from the rope array
                    # tail_row, tail_col = rope[-1]
                    # # update the current tail location on the grid
                    # grid[tail_row][tail_col] = "#"
                    update_tail_position_on_grid(grid, rope[-1])
                    print("rope after moves", rope)
                    print("grid updated", grid)

                if direction == "U":
                    print("moving up")
                    # move head up
                    head_pos[0] -= 1
                    # update rope list with new head position
                    rope[0] = head_pos

                    # move each subsequent knot in the rope if needed
                    for i in range(len(rope) - 1):
                        # think of the knots in pairs, a lead and a next
                        lead_knot_pos = i
                        next_knot_pos = i + 1
                        # if the lead gets too far away, scootch the next up to
                        # be within range
                        if abs(rope[lead_knot_pos][0] - rope[next_knot_pos][0]) > 1:
                            rope[next_knot_pos] = [rope[next_knot_pos][0] - 1, rope[lead_knot_pos][1]]

                    # # grab the current tail location from the rope array
                    # tail_row, tail_col = rope[-1]
                    # # update the current tail location on the grid
                    # grid[tail_row][tail_col] = "#"
                    update_tail_position_on_grid(grid, rope[-1])
                    print("rope after moves", rope)

                if direction == "L":
                    print("moving left")
                    # move head left
                    head_pos[1] -= 1
                    # update rope list with new head position
                    rope[0] = head_pos

                    # move each subsequent knot in the rope if needed
                    for i in range(len(rope) - 1):
                        # think of the knots in pairs, a lead and a next
                        lead_knot_pos = i
                        next_knot_pos = i + 1
                        # if the lead gets too far away, scootch the next up to
                        # be within range
                        if abs(rope[lead_knot_pos][1] - rope[next_knot_pos][1]) > 1:
                            rope[next_knot_pos] = [rope[lead_knot_pos][0], rope[next_knot_pos][1] - 1]

                    update_tail_position_on_grid(grid, rope[-1])
                    print("rope after moves", rope)

                if direction == "D":
                    print("moving down")
                    # move head down
                    head_pos[0] += 1
                    # update rope list with new head position
                    rope[0] = head_pos

                    # move each subsequent knot in the rope if needed
                    for i in range(len(rope) - 1):
                        # think of the knots in pairs, a lead and a next
                        lead_knot_pos = i
                        next_knot_pos = i + 1
                        # if the lead gets too far away, scootch the next up to
                        # be within range
                        if abs(rope[lead_knot_pos][0] - rope[next_knot_pos][0]) > 1:
                            rope[next_knot_pos] = [rope[next_knot_pos][0] + 1, rope[lead_knot_pos][1]]

                    update_tail_position_on_grid(grid, rope[-1])
                    print("rope after moves", rope)

        unique_tail_positions = 0
        for row in grid:
            unique_tail_positions += row.count("#")

        print("unique tail positions", unique_tail_positions)




# eval vs exec

track_tail_pt_2('sample-rope.txt', grid, starting_coords)