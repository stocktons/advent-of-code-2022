with open('forest.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    # create a matrix from the text file, like 
    # [
    #   [3, 0, 3, 7, 3]
    #   [2, 5, 5, 1, 2]
    #   [6, 5, 3, 3, 2]
    #   [3, 3, 5, 4, 9]
    #   [3, 5, 3, 9, 0]
    # ]
    forest_rows = [[int(tree) for tree in line.strip()] for line in lines]

    # spin the matrix 90 degrees to make the first column into the first row, etc
    forest_cols = list(zip(*forest_rows))

    # a grid filled with False of the same dimensions as the forest - used to track
    # which trees are visible from any direction. If one can be see even once, the 
    # False is flipped to True
    forest_tracker = [[False] * len(forest_cols) for i in range(len(forest_rows))]

    visible_tree_count = 0

    for row_idx, row in enumerate(forest_rows):
        tallest_from_left = -1 # trees of height 0 still count as visible
        tallest_from_right = -1

        for col_idx, tree in enumerate(row):
            if tree > tallest_from_left:
                tallest_from_left = tree
                forest_tracker[row_idx][col_idx] = True

        for col_idx, tree in enumerate(reversed(row)):
            if tree > tallest_from_right:
                tallest_from_right = tree
                forest_tracker[row_idx][(len(row) - 1) - col_idx] = True

    # flipped matrix - columns look like rows
    for sideways_col_idx, sideways_col in enumerate(forest_cols): 
        tallest_from_top = -1
        tallest_from_bottom = -1

        for sideways_row_idx, tree in enumerate(sideways_col):
            if tree > tallest_from_top:
                tallest_from_top = tree
                forest_tracker[sideways_row_idx][sideways_col_idx] = True

        for sideways_row_idx, tree in enumerate(reversed(sideways_col)):
            if tree > tallest_from_bottom:
                tallest_from_bottom = tree
                forest_tracker[(len(sideways_col) - 1) - sideways_row_idx][sideways_col_idx] = True

    for row in forest_tracker:
        visible_tree_count += row.count(True) 

    print("visible trees", visible_tree_count)    




        