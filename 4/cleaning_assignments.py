from pathlib import Path
import csv

def get_input_csv(field_names, delimiter = ",", filename="input.csv"):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=delimiter, fieldnames=field_names)
        return [row for row in reader]
    
def parse_raw(raw_data):
    parsed_data = []
    for row in raw_data:
        elf1_start, elf1_end = row["elf1"].split("-")
        elf2_start, elf2_end = row["elf2"].split("-")
        row["elf1_start"] = int(elf1_start)
        row["elf1_end"] = int(elf1_end)
        row["elf2_start"] = int(elf2_start)
        row["elf2_end"] = int(elf2_end)
        parsed_data.append(row)
    return parsed_data

def get_encapsulated_pairs(parsed_ranges):
    encapsulated_pairs = []
    for pair in parsed_ranges:
        min_start = min(pair["elf1_start"], pair["elf2_start"])
        max_end = max(pair["elf1_end"], pair["elf2_end"])
        max_range = f"{min_start}-{max_end}"
        if max_range in [pair["elf1"], pair["elf2"]]:
            encapsulated_pairs.append(pair)
    print(len(encapsulated_pairs))
    
def get_overlapping_pairs(parsed_ranges):
    overlapping_pairs = []
    for pair in parsed_ranges:
        if pair["elf1_end"] >= pair["elf2_start"] and pair["elf2_end"] >= pair["elf1_start"]:
            overlapping_pairs.append(pair)
    print(len(overlapping_pairs))
    
if __name__ == "__main__":
    raw_data = get_input_csv(["elf1", "elf2"])
    parsed_data = parse_raw(raw_data)
    get_encapsulated_pairs(parsed_data)
    get_overlapping_pairs(parsed_data)
    print("Done")
