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

def get_max_calories(food_list):
    max_calorie_count = 0
    for i in range(0, len(food_list)):
        total_cals = sum(food_list[i])
        if total_cals > max_calorie_count:
            max_calorie_count = total_cals
            max_elf = i
    print(f"Elf {max_elf} @ {max_calorie_count}")
        
        

if __name__ == "__main__":
    food_list = get_input_data()
    get_max_calories(food_list)
    print("Done")