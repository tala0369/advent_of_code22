from pathlib import Path
import string

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath, "r") as f:
        return f.read().splitlines()


def get_rucksack_contents(raw_data):
    rucksacks = {}
    for i in range(0, len(raw_data)):
        row = raw_data[i]
        first_comp, second_comp = row[:len(row)//2], row[len(row)//2:]
        rucksacks[i] = {
            "first_comp": first_comp,
            "second_comp": second_comp,
            "common_char": next(char for char in first_comp if char in second_comp)
        }
    return rucksacks

def get_common_char_priority_score(rucksacks):
    total_priority_score = 0
    for sack in rucksacks.values():
        score = string.ascii_letters.index(sack["common_char"]) + 1
        total_priority_score += score
    print(f"total score: {total_priority_score}")

if __name__ == "__main__":
    data = get_input_data()
    rucksacks = get_rucksack_contents(data)
    get_common_char_priority_score(rucksacks)
    print("Done")