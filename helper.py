from pathlib import Path

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / {filename}
    with open(filepath, "r") as f:
        return f.read().splitlines()
