import re

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
    1: ['Z', 'N', 'D'], 
    2: ['M', 'C'], 
    3: ['P']    
    }
    """

    box_dict = {}

    with open('sample-data.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            print(lines[i])
            print([x.split(" ")[i] for x in lines])
            box_stack = [
                re.sub(r'[\[\]]', '', box) # remove brackets from each box (["A"] => "A")
                for box 
                # create a list from all boxes in column i and reverse it
                in [x.split(" ")[i] for x in lines][::-1] 
            ]
            # remove empty boxes (empty strings)
            stripped_box_stack = [box for box in box_stack if box != ""]
            # add box stack to box_dict at key of stack number
            box_dict[i + 1] = box_stack
  
    return box_dict

def sort_boxes(box_dict):
    """Work with a dictionary of boxes and instructions in a text file to sort 
    those boxes and return the top boxes in each stack.

    Sample dictionary:
         {
            1: ['Z', 'N', 'D'], 
            2: ['M', 'C'], 
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

    pass

make_box_dict()