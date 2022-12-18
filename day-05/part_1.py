import re
import math

def make_box_dict():
    """ Create a dictionary from columns in a text file.

    The file starts with letters in brackets in columns like:
        [D]        
    [N] [C]    
    [Z] [M] [P]

    Turn those into lists of the items in the columns from bottom to top and 
    put them in a dictionary with the key of the column number. Remove brackets.

    Output looks like:
    {
    1: ['Z', 'N'], 
    2: ['M', 'C', 'D'], 
    3: ['P']    
    }
    """

    box_dict = {}

    with open('stacks.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

        # loop through each line, grab the letter or space at the indexes we want, 
        # put them in a list
        
        s = 1 # start index of the first letter
        e = 2 # end index of the first letter
     
        # Get the number of stacks we should be checking. Grab the length of the 
        # bottom line (just to be safe), and divide by 4 
        # to account for the length of each box (bracket, letter, bracket, space),
        # and round up since the last box doesn't have a space after it. Loop 
        # this many times.  
        for i in range(math.ceil(len(lines[-1]) / 4)):
            # go through every line and grab the character at the index
            # make a new list of these characters and reverse it
            box_stack = [line[s:e] for line in lines][::-1]
            # remove empty boxes (empty spaces)
            stripped_box_stack = [box for box in box_stack if box != " "]
            # add box stack to box_dict at key of stack number
            box_dict[i + 1] = stripped_box_stack

            # jump to the index of the next letter
            s += 4 
            e += 4
    print(box_dict)
    return box_dict

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

    with open('instructions.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
    # split on spaces, use indexes [1, 3, 5] for [move, from, to] values
        dirs = line.split(' ')
        move_num = int(dirs[1])
        from_stack = int(dirs[3])
        print("from_stack", from_stack)
        to_stack = int(dirs[5])
        print("to_stack", to_stack)

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