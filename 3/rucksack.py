from pathlib import Path
import string
from collections import Counter

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath, "r") as f:
        return f.read().splitlines()


def get_rucksack_contents(raw_data):
    rucksacks = []
    for i in range(0, len(raw_data)):
        row = raw_data[i]
        first_comp, second_comp = row[:len(row)//2], row[len(row)//2:]
        sack = {
            "whole_enchilada": row,
            "first_comp": first_comp,
            "second_comp": second_comp,
            "common_char": next(char for char in first_comp if char in second_comp)
        }
        rucksacks.append(sack)
    return rucksacks

def get_common_char_priority_score(rucksacks):
    total_priority_score = 0
    for sack in rucksacks:
        score = string.ascii_letters.index(sack["common_char"]) + 1
        total_priority_score += score
    print(f"total score: {total_priority_score}")
    
def get_group_score(rucksacks):
    total_score = 0
    for i in range(0, len(rucksacks), 3):
        group_rucksacks = rucksacks[i:i+3]
        group_score = get_common_char_score(group_rucksacks)
        total_score += group_score
    print(f"Total score: {total_score}")
    
def get_common_char_score(rucksacks):
    assert len(rucksacks) == 3
    all_vals = [i["whole_enchilada"] for i in rucksacks]
    badge_char = next(c for c in all_vals[0] if c in all_vals[1] and c in all_vals[2])
    badge_char_score = string.ascii_letters.index(badge_char) + 1
    return badge_char_score

if __name__ == "__main__":
    data = get_input_data()
    rucksacks = get_rucksack_contents(data)
    get_group_score(rucksacks)
    print("Done")