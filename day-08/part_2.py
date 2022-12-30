with open('forest.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    forest = [[int(tree) for tree in line.strip()] for line in lines]

    greatest_scenic_score = 0

    # loop over the forest
    # on each tree look nesw and calculate the viewing distance
    # 
    # check the first number, add it to the view count. 
    # is it shorter than the tree we are in? 
    # if yes, repeat that loop
    # if no, move on to check the next direction
    # when done, multiply the 4 numbers together to get a scenic score
    # check against the current highest scenic score, replace if it's higher

    for row_idx, row in enumerate(forest):
        for col_idx, tree in enumerate(row):

            # look east
            east_view_count = 0
            tree_idx_to_check_east = col_idx + 1
            try:
                while tree_idx_to_check_east < len(row):
                    next_tree = forest[row_idx][tree_idx_to_check_east]
                    east_view_count += 1
                    tree_idx_to_check_east += 1
                    if next_tree >= tree:
                        break
            
            except IndexError:
                pass
           
            # look west
            west_view_count = 0
            tree_idx_to_check_west = col_idx - 1
            try:
                while tree_idx_to_check_west > -1:
                    next_tree = forest[row_idx][tree_idx_to_check_west]
                    west_view_count += 1
                    tree_idx_to_check_west -= 1
                    if next_tree >= tree:
                        break

            except IndexError:
                pass

            # look north
            north_view_count = 0
            tree_idx_to_check_north = row_idx - 1
            try:
                while tree_idx_to_check_north > -1:
                    next_tree = forest[tree_idx_to_check_north][col_idx]
                    north_view_count += 1
                    tree_idx_to_check_north -= 1
                    if next_tree >= tree:
                        break

            except IndexError:
                pass

            # look south
            south_view_count = 0
            tree_idx_to_check_south = row_idx + 1
            try:
                while tree_idx_to_check_south < len(forest):
                    next_tree = forest[tree_idx_to_check_south][col_idx]
                    south_view_count += 1
                    tree_idx_to_check_south += 1
                    if next_tree >= tree:
                        break

            except IndexError:
                pass

            tree_scenic_score = (
                east_view_count * 
                west_view_count * 
                north_view_count * 
                south_view_count
            )

            if tree_scenic_score > greatest_scenic_score:
                greatest_scenic_score = tree_scenic_score

    print("greatest scenic score", greatest_scenic_score)