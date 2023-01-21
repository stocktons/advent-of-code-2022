# head moves
# # move all other knots as needed

# create a list to hold all the knot positions
# iterate over the list and update each coord after each head move
# by comparing each index to the one before it

# start
[[4, 0], [4, 0], [4, 0],[4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0], [4, 0]]

# R4

[[4, 1], ...]

def track_tail(file, grid, starting_coords, num_knots):

     with open(file, 'r', encoding="utf-8") as f:

        row, col = starting_coords
        head_pos = [row, col]
        # create a list to represent the rope with all knots at the starting position
        rope = [head_pos for i in range(num_knots)]
        grid[row][col] = "#"


        lines = f.readlines()

        for line in lines:
            direction, steps = line.strip().split(" ")
            num_steps = int(steps)

            for i in range(num_steps):
                if direction == "R":
                    # move head to the right
                    head_pos[1] += 1
                    # update rope list with new head position
                    rope[0] = head_pos 

                    # move each subsequent knot in the rope if needed
                    for i in range(len(rope)-1): 
                        # think of the knots in pairs, a lead and a next
                        lead_knot_pos = rope[i] 
                        next_knot_pos = rope[i + 1] 
                        # if the lead gets too far away, scootch the next up to 
                        # be within range
                        if abs(lead_knot_pos[1] - next_knot_pos[1]) > 1:
                            rope[i + 1] = [lead_knot_pos[0], next_knot_pos[1] + 1]
                    # grab the current tail location from the rope array
                    row, col = rope[-1]  
                    # update the current tail location on the grid     
                    grid[row][col] = "#"

                if direction == "U":
                    head_pos[0] -= 1
                    if abs(tail_pos[0] - head_pos[0]) > 1:
                        tail_pos = [tail_pos[0] - 1, head_pos[1]]
                        grid[tail_pos[0]][tail_pos[1]] = "#"

                if direction == "L":
                    head_pos[1] -= 1
                    if abs(head_pos[1] - tail_pos[1]) > 1:
                        tail_pos = [head_pos[0], tail_pos[1] - 1]
                        grid[tail_pos[0]][tail_pos[1]] = "#"

                if direction == "D":
                        head_pos[0] += 1
                        if abs(tail_pos[0] - head_pos[0]) > 1:
                            tail_pos = [tail_pos[0] + 1, head_pos[1]]
                            grid[tail_pos[0]][tail_pos[1]] = "#"

        unique_tail_positions = 0
        for row in grid:
            unique_tail_positions += row.count("#")

        print("unique tail positions", unique_tail_positions)



track_tail('rope.txt', rope_grid, starting_coords)
# print(rope_grid)