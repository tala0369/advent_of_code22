
from pathlib import Path
import csv

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / {filename}
    with open(filepath, "r") as f:
        return f.read().splitlines()
    
def get_input_csv(field_names, delimiter = ",", filename="input.csv"):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=delimiter, fieldnames=field_names)
        return [row for row in reader]