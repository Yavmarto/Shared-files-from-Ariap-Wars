# Tree templates
long_tree = [0, 12, 0, 1, 12, 1, 65536, 12, 65536, 65537, 12, 65537, 131072, 12, 131072, 131073, 12, 131073, 196608, 12, 196608, 196609, 12, 196609, 262144, 12, 262144, 262145, 12, 262145 ]
wide_tree = [0, 34, 0, 1, 34, 1, 2, 34, 2, 65536, 34, 65536, 65537, 34, 65537, 65538, 34, 65538, 131072, 34, 131072, 131073, 34, 131073, 131074, 34, 131074, 196608, 34, 196608, 196609, 34, 196609, 196610, 34, 196610 ]
small_tree = [0, 35, 0, 1, 35, 1, 65536, 35, 65536, 65537, 35, 65537, 131072, 35, 131072, 131073, 35, 131073 ]

# -----------------------
# User variables
# -----------------------

# number of trees in x
number_of_trees_x = 5

# starting position of first tile
start_pos_x = 4
start_pos_y = 2

chosen_tree = long_tree


# -----------------------
# Non User variables
# -----------------------

# trees type varibales
tree_height = 0
tree_height_small = 3
tree_height_wide = 4
tree_height_long = 5
tree_width = 2

# tree variables misc
step_size_x = 0
GD_STEP_SIZE = 65536

# set width and height of trees
if chosen_tree == long_tree:
    tree_height = tree_height_long
elif chosen_tree == wide_tree:
    tree_width = 3
    tree_height = tree_height_wide
elif chosen_tree == small_tree:
    tree_height = tree_height_small

single_tree_line = []

# create the first trees
for i in range(number_of_trees_x):
    if i > 0:
        step_size_x = tree_width
    else:
        step_size_x = (GD_STEP_SIZE * start_pos_y) + start_pos_x 
    for i in range(len(chosen_tree)):
        if i == 0:
            chosen_tree[i] += step_size_x 
        elif i % 3 == 0:
            chosen_tree[i] += step_size_x

    for j in chosen_tree:
        single_tree_line.append(j)


second_tree_line = []

for i in range(len(single_tree_line)):
    if i == 0 or i % 3 == 0:
        new_pos = []
        new_pos = single_tree_line[i] + 1 + GD_STEP_SIZE
        second_tree_line.append(new_pos)
    else:
        second_tree_line.append(single_tree_line[i])

print("----- First tree -----")
print(single_tree_line)
print("----- Second tree -----")
print(second_tree_line)

# ---- How to use ----
# You pick a tree type, set the starting position and set the number of tree
# 2 lines will be generated and it's up to you whether you want to use both.
# The first one goes into the flying map and the second one goes in to the flying extra map
