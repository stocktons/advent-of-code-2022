# make this a function called create_grid

with open('rope.txt', 'r', encoding="utf-8") as f:
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
        # calculate the size of the grid needed
        # find the highest/lowest vertical points

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

    def find_val_in_matrix(matrix, char):
        for sub_list in matrix:
            if char in sub_list:
                return (matrix.index(sub_list), sub_list.index(char))
        raise ValueError("'{char}' is not in list".format(char = char))

    # We started moving from 0, so the starting position must be highest and leftmost 
    # count over of indexes in our new grid. Select that index and change value to "s"

    # sample grid. We started at "s" as 0, but to reorient it to match the indexes 
    # of a matrix, we have to reorient (0, 0) to be the upper left corner
    # ......
    # ......
    # ......  
    # ......
    # s.....

    # highest will always be >= 0, leftmost will always be <= 0
    rope_grid[highest][abs(leftmost)] = "s"
    start = find_val_in_matrix(rope_grid, "s")
    print("starting position", start)

    print(lowest, "lowest") 
    print(highest, "highest") 
    print(leftmost, "leftmost")
    print(rightmost, "rightmost") 
    print(width, "width")
    print(height, "height") 

# should be (4, 0) for sample-rope.txt
# (93, 179) for rope.txt

# from rope.txt: 
# lowest -142
# highest 93
# leftmost -179
# rightmost 3
# width 183
# height 236 
