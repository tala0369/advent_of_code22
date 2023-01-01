from pathlib import Path
import numpy as np

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
        trees = [[int(i) for i in line] for line in lines]
        return trees
    
def get_zeroed_arr(array):
    new_arr = []
    max_height = 0
    for i in range(0, len(array)):
        new_val = array[i] if array[i] > max_height else 0
        new_arr.append(new_val)
        max_height = max(max_height, new_val)
    return np.array(new_arr)

def trees_from(tree_matrix, num_rotations, call_me=get_zeroed_arr):
    zeroes = np.array([call_me(i) for i in np.rot90(tree_matrix, k=num_rotations)])
    return np.rot90(zeroes, k=(4-num_rotations))

def count_visible_trees(array):
    target_height = array[0]
    tree_count = 0
    max_height = 1
    for tree in array[1:]:
        tree_count += 1
        max_height = tree
        if tree >= target_height:
            break
    return tree_count

def get_count_arr(array):
    new_arr = []
    for i in range(0, len(array)):
        if (array[i] == 0) or (i == (len(array) -1)) or (i == 0):
            new_val = 0
        else:
            new_val = count_visible_trees(array[i:])
        new_arr.append(new_val)
    return np.array(new_arr)

def get_view_scores(tree_matrix):
    from_left = trees_from(tree_matrix, 0, call_me=get_count_arr)
    from_top = trees_from(tree_matrix, 1, call_me=get_count_arr)
    from_right = trees_from(tree_matrix, 2, call_me=get_count_arr)
    from_bottom = trees_from(tree_matrix, 3, call_me=get_count_arr)
    all_views = np.dstack([from_left,from_top,from_right, from_bottom])
    views = all_views.prod(axis=2)
    max = np.max(views)
    print(max)
    return views
    
def get_visible_trees(tree_matrix):
    from_left = trees_from(tree_matrix, 0)
    from_top = trees_from(tree_matrix, 1)
    from_right = trees_from(tree_matrix, 2)
    from_bottom = trees_from(tree_matrix, 3)
    all_views = np.dstack([from_left,from_top,from_right, from_bottom])
    zeroed_trees = all_views.max(axis=2)
    (length, width) = np.shape(zeroed_trees)
    perimeter_count = 2*width + 2*(length-2)
    inside_trees = zeroed_trees[1:width-1,1:length-1]
    num_visible_inside = np.count_nonzero(inside_trees)
    nonzero_count = perimeter_count + num_visible_inside
    print(nonzero_count)
    return zeroed_trees
    
if __name__ == "__main__":
    tree_array = get_input_data()
    tree_matrix = np.array(tree_array)
    visible_trees = get_visible_trees(tree_matrix)
    get_view_scores(tree_matrix)