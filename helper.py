from pathlib import Path

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / {filename}
    with open(filepath, "r") as f:
        line_chunks = f.read().split("\n\n")
    
    lines = [
        [int(num) for num in l.splitlines()]
        for l in line_chunks
    ]
    return lines