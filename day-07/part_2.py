from tree import Tree, TreeNode
from file_tree import create_file_system

total_disk_space = 70000000

file_system = create_file_system()

total_used_space = file_system.sum_values()

available_space = total_disk_space - total_used_space

needed_space = 30000000

space_to_free_up = needed_space - available_space

delete_folder = file_system.find_smallest_val_above_target_val(space_to_free_up, total_disk_space)

print("total filesystem sumvalues", total_used_space)
print("space to free up", space_to_free_up)
print("folder to delete", delete_folder)


