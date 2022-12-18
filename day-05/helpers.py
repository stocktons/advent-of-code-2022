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
    print("running make_box_dict")
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