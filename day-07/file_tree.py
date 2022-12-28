from tree import Tree, TreeNode

with open('terminal.txt', 'r', encoding="utf-8") as f:
    
    file_system = Tree(TreeNode("/", "dir"))
    current_dir = file_system.root
    
    lines = f.readlines()

    for line_num, line in enumerate(lines, start=1):
        # print(line_num)
        if not line.startswith("$"):
            val, file_name = line.split(" ")
            current_dir.add_child(TreeNode(file_name.strip(), val.strip(), current_dir, []))

        if line.startswith("$ cd"):
            path = line.split(" ")[2].strip()
  
            if path != "..":
                next_dir = path
            else:
                try: 
                    next_dir = current_dir.parent.file_name
                except AttributeError:
                    print("file_name", current_dir.file_name,"line num", line_num)
                    next_dir = file_system.root.file_name

            current_dir = file_system.find(next_dir)

file_system.find_sum_all_dirs_less_than_100000()
