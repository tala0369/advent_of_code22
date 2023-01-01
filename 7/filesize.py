from pathlib import Path
from flatten_dict import unflatten, flatten
from collections import defaultdict

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath, "r") as f:
        return f.read().splitlines()
    

    
def parse_terminal_output(terminal_output):
    directories = {}
    cwd = ["home"]
    for line in terminal_output:
        detail_line = line.split(" ")
        if line.startswith("$ cd"):
            if detail_line[2] == '..':
                cwd.pop()
            elif detail_line[2] != "/":
                cwd.append(detail_line[2])
        elif not detail_line[0] in ["$", "dir"]:
            value = int(detail_line[0])
            dirs = cwd + [detail_line[1]]
            directories["/".join(dirs)] = value
    return directories

def get_dir_sizes(files):
    dir_sizes = defaultdict(int)

    for key, value in files.items():
        path_parts = key.split("/")[0:-1] # Don't include filename
        dir_names = ["/".join(path_parts[0:i]) for i in range(1,len(path_parts)+1)]
        for dir in dir_names:
            dir_sizes[dir] += value
    return dir_sizes

def get_under_100000(dir_sizes):
    cutoff = 100000
    small_dirs = [v for k, v in dir_sizes.items() if v < cutoff]
    print(sum(small_dirs))
    return

def find_delete_dir(dir_sizes):
    total_space_used = dir_sizes["home"]
    total_space_available = 70000000
    free_space_required = 30000000
    bytes_to_delete = total_space_used + free_space_required - total_space_available
    big_enough_dirs = [v for v in dir_sizes.values() if v >= bytes_to_delete]
    best_pick = min(big_enough_dirs)
    print(best_pick)
    return
    
    
if __name__ == "__main__":
    terminal_output = get_input_data()
    file_list = parse_terminal_output(terminal_output)
    dir_sizes = get_dir_sizes(file_list)
    get_under_100000(dir_sizes)
    find_delete_dir(dir_sizes)
    print("Done")