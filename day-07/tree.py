from collections import deque

class TreeNode:
    "A single node in a tree."

    def __init__(self, file_name, val, parent = None, children = []):
        self.file_name = file_name
        self.val = 0 if val == "dir" else val
        self.children = children
        self.parent = parent
        for child in self.children:
            child.parent = self

    def __repr__(self):
        return f"< file_name: {self.file_name}, value: {self.val}, num_children: {len(self.children)}, parent: {self.parent}  >"

    def sum_values(self):
        """Add up all values of invoking node and its children. 
        Returns sum as an integer."""

        sum = int(self.val)

        for child in self.children:
            sum += child.sum_values()

        return sum

    def add_child(self, child):
        """Slightly shorter way to append a child."""

        self.children.append(child)

class Tree:
    """Wrapper class for a group of TreeNodes."""

    def __init__(self, root = None):
        self.root = root
        self.parent = None
    
    def __repr__(self):
        return f"< file_name: {self.root.file_name}, value: {self.root.val}, num_children: {len(self.root.children)}>"

    def sum_values(self):
        """Add up all values in the tree."""

        if self.root == None:
            return 0

        return self.root.sum_values()

    def find(self, dir_name):
        """Search entire tree for a particular file_name. Not needed in final 
        solution."""

        to_visit = deque()
        to_visit.append(self.root)

        while len(to_visit):
            current = to_visit.popleft()

            if current.file_name == dir_name:
                return current

            for child in current.children:
                to_visit.append(child)

    def find_all(self, dir_name):
        """Search entire tree for all instances of a particular file_name. Not needed in final 
        solution, but handy for debugging."""

        to_visit = deque()
        to_visit.append(self.root)
        all_matches = []

        while len(to_visit):
            current = to_visit.popleft()

            if current.file_name == dir_name:
                all_matches.append(current)

            for child in current.children:
                to_visit.append(child)

        return all_matches

    def find_sum_all_dirs_less_than_100000(self):
        """Find any directory that sums up to a value of less than 100000. Will 
        count nested directories' values more than once."""

        total = 0

        to_visit = deque()
        to_visit.append(self.root)

        while len(to_visit):
            current = to_visit.popleft()
            dir_total = current.sum_values()

            if dir_total <= 100000: 
                total += dir_total

            for child in current.children:
                if child.children != []: # only search directories
                    to_visit.append(child)
        
        print("TOTAL =", total)
        return total


######## sample data for testing
sample_tree = Tree(
    TreeNode("/", 0, None, [ 
        TreeNode("a", 0, None, [ 
            TreeNode("e", 0, None, [
                TreeNode("i", 584, None, [])
            ]), 
            TreeNode("f", 29116, None, []), 
            TreeNode("g", 2557, None, []), 
            TreeNode("h.lst", 62596, None, []) 
        ]),
        TreeNode("b", 14848514, []), 
        TreeNode("c", 8504156, []), 
        TreeNode("d", 0, None, [
            TreeNode("j", 4060174, None, []), 
            TreeNode("d.log", 8033020, None, []), 
            TreeNode("d.ext", 5626152, None, []), 
            TreeNode("k", 7214296, None, []) 
        ])
    ])
)

# print("tree", sample_tree)
# print("root", sample_tree.root)
# print(sample_tree.sum_values())
# print(sample_tree.find_sum_all_dirs_less_than_100000())
