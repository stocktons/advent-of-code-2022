def find_marker():
    """Analyze a string to find the first four-letter group that has no duplicate
    letters in it. Return the index + 1 of the last letter of this group.

    Examples:
    bvwbjplbgvbhsrlpgdmjqwftvncz: returns 5
    nppdvjthqldpwncqszvftbrmjlhg: returns 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: returns 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: returns 11
    """

    with open('signal.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        signal = lines[0]

        # create pointers for a sliding window approach
        pointer_1_idx = 0
        pointer_2_idx = 4

        while pointer_2_idx < len(signal):
            marker = signal[pointer_1_idx:pointer_2_idx]

            # create a set of the letters in the window. If the length is still 4, 
            # there are no duplicates, and we've found our marker.
            if len(set(marker)) == 4:
                print(pointer_2_idx)
                break

            # if the length is less than 4, then there were duplicates, so slide 
            # the window to the next group of four letters.
            else:
                pointer_1_idx += 1
                pointer_2_idx += 1
        
find_marker()
