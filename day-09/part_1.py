def create_grid(file):
    """Reads a text file with directions and steps and finds the maximum dimensions 
    from the starting point. Creates a grid filled with dots of those dimensions, 
    and marks the starting position with an 's'. 
    """

    with open(file, 'r', encoding="utf-8") as f:
        lowest = 0
        highest = 0
        leftmost = 0
        rightmost = 0
        current_vert = 0
        current_horiz = 0

        lines = f.readlines()

        for line in lines:
            direction, steps = line.strip().split(" ")
            num_steps = int(steps)

            # calculate the size of the grid needed by
            # finding the highest/lowest vertical points
            if direction == "U":
                current_vert += num_steps
                if current_vert > highest:
                    highest = current_vert
            if direction == "R":
                current_horiz += num_steps
                if current_horiz > rightmost:
                    rightmost = current_horiz
            if direction == "D":
                current_vert -= num_steps
                if current_vert < lowest:
                    lowest = current_vert
            if direction == "L":
                current_horiz -= num_steps
                if current_horiz < leftmost:
                    leftmost = current_horiz

        width = rightmost - leftmost + 1
        height = highest - lowest + 1

        # create rope grid of needed height and width, fill with "."
        rope_grid = [["."] * width for i in range(height)]

        # We started moving from 0, so the starting position must be highest and leftmost 
        # count over of indexes in our new grid. Select that index and change value to "s"

        # sample grid. We started at "s" as 0, but to reorient it to match the indexes 
        # of a matrix, we have to reorient (0, 0) to be the upper left corner, so now
        # in the example becomes (4, 0)

        # example:

        # ......
        # ......
        # ......  
        # ......
        # s.....

        # highest will always be >= 0, leftmost will always be <= 0
        rope_grid[highest][abs(leftmost)] = "s"

        return rope_grid

def find_val_in_matrix(matrix, char):
    """Takes in a matrix and a character to search for. Returns the coordinates 
    in a tuple like (row, col). Finds the 's' in the rope_grid, for example.
    """

    for sub_list in matrix:
        if char in sub_list:
            return (matrix.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))

# def track_head(file, matrix, starting_coords):

#      with open(file, 'r', encoding="utf-8") as f:

#         current_row_head, current_col_head = starting_coords

#         lines = f.readlines()

#         for line in lines:
#             direction, steps = line.strip().split(" ")
#             num_steps = int(steps)

#             if direction == "U":
#                 current_row_head -= num_steps
#             if direction == "R":
#                 current_col_head += num_steps
#             if direction == "D":
#                 current_row_head += num_steps
#             if direction == "L":
#                 current_col_head -= num_steps

#             print(current_row_head, current_col_head)
#             matrix[current_row_head][current_col_head] = "H"

#         return matrix


rope_grid = create_grid('rope.txt')
starting_coords = find_val_in_matrix(rope_grid, 's')

def track_tail(file, grid, starting_coords):

     with open(file, 'r', encoding="utf-8") as f:

        row, col = starting_coords
        head_pos = [row, col]
        tail_pos = [row, col]
        grid[row][col] = "#"

        lines = f.readlines()

        for line in lines:
            direction, steps = line.strip().split(" ")
            num_steps = int(steps)

            for i in range(num_steps):
                if direction == "R":
                    head_pos[1] += 1
                    if abs(head_pos[1] - tail_pos[1]) > 1:
                        tail_pos = [head_pos[0], tail_pos[1] + 1]
                        grid[tail_pos[0]][tail_pos[1]] = "#"

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