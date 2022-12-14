from helpers import make_box_dict

def sort_boxes(box_dict):
    """Work with a dictionary of boxes and instructions in a text file to sort 
    those boxes and return the top boxes in each stack.

    Sample dictionary:
         {
            1: ['Z', 'N'], 
            2: ['M', 'C', 'D'], 
            3: ['P']    
        }

    Sample instructions:
        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2

    Sample output: 
        'CMZ'
    """
    print("running sort_boxes")

    with open('instructions.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
    # split on spaces, use indexes [1, 3, 5] for [move, from, to] values
        dirs = line.split(' ')
        move_num = int(dirs[1])
        from_stack = int(dirs[3])
        to_stack = int(dirs[5])

        # repeat removing a box from the from_stack and placing it on the 
        # to_stack "move" number of times
        for i in range(move_num):
            # remove top box from old stack
            box_to_move = box_dict[from_stack].pop()
            # place on the new stack
            box_dict[to_stack].append(box_to_move)

    # loop through dictionary, get the last item from each value array, and turn 
    # those items into a string
    print(''.join([stack[-1] for stack in box_dict.values()]))

stacks = make_box_dict()
sort_boxes(stacks)