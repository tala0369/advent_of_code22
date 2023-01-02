from pathlib import Path
import copy
import csv
import math

def get_input_csv(field_names, delimiter = ",", filename="input.csv"):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=delimiter, fieldnames=field_names)
        return [row for row in reader]
    
def tail_move(old_head_cord, new_head_cord, tail_cord):
    if math.dist(new_head_cord, tail_cord) <= math.sqrt(2):
        return tail_cord
    else:
        return old_head_cord
    
def tail_multi_move(old_head_cord, new_head_cord, tail_cord):
    if math.dist(new_head_cord, tail_cord) <= math.sqrt(2):
        return tail_cord
    else:
        normer = lambda x: x/max(abs(x),1)
        x_diff = new_head_cord[0] - tail_cord[0]
        y_diff = new_head_cord[1] - tail_cord[1]
        new_tail = [tail_cord[0] + normer(x_diff), tail_cord[1] + normer(y_diff)]
        return new_tail
    
def head_move(dir, head_cord):
    new_head_cord = copy.deepcopy(head_cord)
    if dir == "L":
        new_head_cord[0] -= 1
    elif dir == "R":
        new_head_cord[0] += 1
    elif dir == "U":
        new_head_cord[1] += 1
    else:
        new_head_cord[1] -= 1
    return new_head_cord
    
def get_playout(moves):
    head_cord = [0,0]
    tail_cord = [0,0]
    played_out = []
    for move in moves:
        dir = move["dir"]
        num_spaces = int(move["num_spaces"])
        for space in range(0, num_spaces):
            new_head_cord = head_move(dir, head_cord)
            tail_cord = tail_move(head_cord, new_head_cord, tail_cord)
            head_cord = new_head_cord
            played_out.append((tuple(head_cord), tuple(tail_cord)))
    return played_out

def get_multi_playout(moves):
    cords = [[0,0]]*10
    played_out = [[tuple(c) for c in cords]]
    for move in moves:
        dir = move["dir"]
        num_spaces = int(move["num_spaces"])
        for space in range(0, num_spaces):
            new_head_cord = head_move(dir, cords[0])
            for i in range(0, len(cords)-1):
                new_tail_cord = tail_multi_move(
                    cords[i], # Old head cord
                    new_head_cord,
                    cords[i+1] # Old tail cord
                )
                cords[i] = new_head_cord # Reassign head to it's new cord
                new_head_cord = new_tail_cord # Your tail becomes your next head
            cords[-1] = new_head_cord
            tupled = [tuple(c) for c in cords]
            played_out.append(tupled)
    return played_out

def get_num_unique_spots(plays, ind=1):
    tail_moves = [i[ind] for i in plays]
    unique = set(tuple(i) for i in tail_moves)
    print(len(unique))
    
if __name__ == "__main__":
    moves = get_input_csv(["dir", "num_spaces"], delimiter=" ")
    plays = get_playout(moves)
    get_num_unique_spots(plays)
    multi_plays = get_multi_playout(moves)
    get_num_unique_spots(multi_plays, 9)
    print("Done")