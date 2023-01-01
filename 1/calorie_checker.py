from pathlib import Path

def get_input_data():
    filepath = Path(__file__).parent / "input.txt"
    with open(filepath, "r") as f:
        line_chunks = f.read().split("\n\n")
    
    lines = [
        [int(num) for num in l.splitlines()]
        for l in line_chunks
    ]
    return lines

def get_calorie_count(food_list):
    elves = []
    for i in range(0, len(food_list)):
        elf = {
            "num": i,
            "snack_list": food_list[i],
            "total_calorie_count": sum(food_list[i])
        }
        elves.append(elf)
    elves_sorted = sorted(elves, key=lambda d: d['total_calorie_count'], reverse=True)
    return elves_sorted

def get_max_calories(calorie_ref, num):
    total_cals = 0
    for i in range(0,num):
        elf = calorie_ref[i]
        this_elf_num = elf["num"]
        this_elf_cals = elf["total_calorie_count"]
        print(f"Elf {this_elf_num} @ {this_elf_cals}")
        total_cals += this_elf_cals
    print(f"Total Cals: {total_cals}")
        
        
if __name__ == "__main__":
    food_list = get_input_data()
    calorie_ref = get_calorie_count(food_list)
    get_max_calories(calorie_ref, 1)
    get_max_calories(calorie_ref, 3)
    print("Done")