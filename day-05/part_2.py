from helpers import make_box_dict

def cratemover_9001(box_dict):
    """Work with a dictionary of boxes and instructions in a text file to sort 
    those boxes and return the top boxes in each stack. Rather than moving boxes 
    one at a time, the CrateMover 9001 moves stacks of boxes, maintaining their 
    order.

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
        'MCD'
    """

    with open('instructions.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
    # split on spaces, use indexes [1, 3, 5] for [move, from, to] values
        dirs = line.split(' ')
        move_num = int(dirs[1])
        from_stack = int(dirs[3])
        to_stack = int(dirs[5])

        # move number is now the length of the slice to take from the end of the 
        # from_stack and append to the end of the to_stack
        box_dict[to_stack] += box_dict[from_stack][-move_num:]

        # delete the moved boxes from the from_stack
        del box_dict[from_stack][-move_num:]

    # loop through dictionary, get the last item from each value array, and turn 
    # those items into a string
    print(''.join([stack[-1] for stack in box_dict.values()]))

stacks = make_box_dict()
cratemover_9001(stacks)
