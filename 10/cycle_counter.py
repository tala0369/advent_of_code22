from pathlib import Path
import copy
import csv
from pprint import pprint
import math

def get_input_csv(field_names, delimiter = ",", filename="input.csv"):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        reader = csv.reader(f, delimiter=' ')
        return [
            int(row[-1])
            if len(row) ==2
            else 0
            for row in reader
        ]
        
def get_x_for_cycle(cycle_num, cycles):
    x = 1
    index_num = 0
    cycle_count = 1
    while cycle_count < cycle_num:
        this_cycle = cycles[index_num]
        if this_cycle == 0:
            cycle_count += 1
        else:
            cycle_count += 2
            if cycle_count <= cycle_num:
                x += this_cycle
        index_num += 1
    return x
        
def get_strength_for_cycle(cycle_num, cycles):
    x = get_x_for_cycle(cycle_num, cycles)
    cycle_strength = cycle_num * x
    print(cycle_strength)
    return cycle_strength

def write_pixel(x, cycle_num):
    print(f"Cycle #: {cycle_num}")
    print(f"X: {x}")
    ind = cycle_num%40
    sprite_in_window = x <= ind <= x+2
    pixel = "#" if sprite_in_window else "."
    return pixel

def print_crt(crt):
    n = 40 # chunk length
    rows = ["".join(crt[i:i+n]) for i in range(0, len(crt), n)]
    pprint(rows)

def get_crt_image(commands):
    crt = ["-"]*(40*6)
    cycle_num = 1
    x = 1
    for cmd in commands:
        if cmd != 0:
            crt[cycle_num-1] = write_pixel(x, cycle_num)
            cycle_num += 1
            #print_crt(crt)
        crt[cycle_num-1] = write_pixel(x, cycle_num)
        x += cmd
        cycle_num += 1
        #print_crt(crt)
        
    print_crt(crt)
    
if __name__ == "__main__":
    cycles = get_input_csv(["dir", "num_spaces"], delimiter=" ")
    cycle20 = get_strength_for_cycle(20, cycles)
    cycle60 = get_strength_for_cycle(60, cycles)
    cycle100 = get_strength_for_cycle(100, cycles)
    cycle140 = get_strength_for_cycle(140, cycles)
    cycle180 = get_strength_for_cycle(180, cycles)
    cycle220 = get_strength_for_cycle(220, cycles)
    print(cycle20 + cycle60 + cycle100 + cycle140 + cycle180 + cycle220)
    
    get_crt_image(cycles)
    
    print("Done")