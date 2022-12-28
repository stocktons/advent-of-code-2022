from tree import Tree, TreeNode

with open('terminal.txt', 'r', encoding="utf-8") as f:
    
    file_system = Tree(TreeNode("/", "dir"))
    current_dir = file_system.root
    
    lines = f.readlines()[1:] # start at line 2 since we've already established the root dir

    for line in lines:
        if not line.startswith("$"):
            val, file_name = line.split(" ")
            current_dir.add_child(TreeNode(file_name.strip(), val.strip(), current_dir, []))

        if line.startswith("$ cd"): 
            path = line.split(" ")[2].strip()
  
            if path != "..":
                for child in current_dir.children:
                    if child.file_name == path:
                        next_dir = child
                        continue
            else:
                next_dir = current_dir.parent

            current_dir = next_dir 

file_system.find_sum_all_dirs_less_than_100000()
