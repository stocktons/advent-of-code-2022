from collections import deque

class TreeNode:
    "A single node in a tree."

    def __init__(self, name, val, children = [], parent = None):
        self.name = name
        self.val = 0 if val == dir else val
        self.children = children
        self.parent = None
        for child in self.children:
            child.parent = self

    def __repr__(self):
        return f"< name: {self.name}, value: {self.val}, parent: {self.parent.name} >"

    def sum_values(self):
        """Add up all values of invoking node and its children. 
        Returns sum as an integer."""

        sum = self.val
        # print("self.val in sum_values", self.val)

        for child in self.children:
            sum += child.sum_values()

        return sum

    def add_child(self, child):
        new_child = self.children.append(child)
        new_child.parent = self


class Tree:
    def __init__(self, root = None):
        self.root = root
        self.parent = None
    
    def __repr__(self):
        return f"< name: {self.root.name}, value: {self.root.val}, children: {self.root.children}>"

    def sum_values(self):
        """Add up all values in the tree."""

        if self.root == None:
            return 0

        return self.root.sum_values()

    def find_sum_all_dirs_less_than_100000(self):

        total = 0

        to_visit = deque()
        to_visit.append(self.root)

        while len(to_visit):
            current = to_visit.popleft()
            dir_total = current.sum_values()
            # print("name and value: ", current.name, current.sum_values())

            if dir_total <= 100000: 
                total += dir_total
                print("adding to total", current.name, dir_total, total)

            for child in current.children:
                if child.children != []:
                    to_visit.append(child)
        
        print("TOTAL =", total)
        return total

sample_tree = Tree(
    TreeNode("/", 0, [ 
        TreeNode("a", 0, [ 
            TreeNode("e", 0, [
                TreeNode("i", 584, [])
            ]), 
            TreeNode("f", 29116, []), 
            TreeNode("g", 2557, []), 
            TreeNode("h.lst", 62596, []) 
        ]),
        TreeNode("b", 14848514, []), 
        TreeNode("c", 8504156, []), 
        TreeNode("d", 0, [
            TreeNode("j", 4060174, []), 
            TreeNode("d.log", 8033020, []), 
            TreeNode("d.ext", 5626152, []), 
            TreeNode("k", 7214296, []) 
        ])
    ])
)

# print(sample_tree)
# print(sample_tree.sum_values())
print(sample_tree.find_sum_all_dirs_less_than_100000())
