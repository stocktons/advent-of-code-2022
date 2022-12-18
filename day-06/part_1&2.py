def find_marker(marker_length):
    """
    Part 1
    Analyze a string to find the first four-letter group that has no duplicate
    letters in it. Return the index + 1 of the last letter of this group.

    Examples:
    bvwbjplbgvbhsrlpgdmjqwftvncz: returns 5
    nppdvjthqldpwncqszvftbrmjlhg: returns 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: returns 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: returns 11

    Part 2
    Do the same thing, but for 14-letter groups
    """

    with open('signal.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        signal = lines[0]

        # create pointers for a sliding window approach
        pointer_1_idx = 0
        pointer_2_idx = marker_length

        while pointer_2_idx < len(signal):
            marker = signal[pointer_1_idx:pointer_2_idx]

            # create a set of the letters in the window. If the length is still 4, 
            # there are no duplicates, and we've found our marker.
            if len(set(marker)) == marker_length:
                print(pointer_2_idx)
                break

            # if the length is less than 4, then there were duplicates, so slide 
            # the window to the next group of four letters.
            else:
                pointer_1_idx += 1
                pointer_2_idx += 1

# Part 1:        
find_marker(4)

# Part 2: 
find_marker(14)
