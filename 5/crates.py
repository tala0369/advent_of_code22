from pathlib import Path
from copy import deepcopy

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath, "r") as f:
        initial_split = f.read().split("\n\n")
        stacks_raw = initial_split[0].splitlines()
        stacks = [
            [
                "".join(c for c in line[i:i+4] if c.isalnum())
                for i in range(0, len(line), 4)
            ] 
            for line in stacks_raw
        ]
        stacks.reverse()
        moves = initial_split[-1].splitlines()
        return stacks, moves
    
def rearrange_stacks(raw_stacks):
    stacker = {}
    for i in range(0, len(raw_stacks[0])):
        crate_list=[row[i] for row in raw_stacks[1:] if row[i]]
        stacker[i+1] = crate_list
    return stacker

def parse_moves(raw_moves):
    parsed_moves = []
    for move in raw_moves:
        ints = [int(s) for s in move.split() if s.isdigit()]
        this_move = {
            "num_crates": ints[0],
            "start_col": ints[1],
            "end_col": ints[2]
        }
        parsed_moves.append(this_move)
    return parsed_moves

def execute_stack_plan(stacks, moves):
    new_stacks = deepcopy(stacks)
    for move in moves:
        for i in range(0,move["num_crates"]):
            last_in_stack = new_stacks[move["start_col"]].pop(-1)
            new_stacks[move["end_col"]].append(last_in_stack)
    return new_stacks
    
if __name__ == "__main__":
    stacks, moves = get_input_data()
    rearranged_stacks = rearrange_stacks(stacks)
    parsed_moves = parse_moves(moves)
    final_stacks = execute_stack_plan(rearranged_stacks, parsed_moves)
    print("Done")