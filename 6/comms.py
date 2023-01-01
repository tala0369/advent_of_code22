from pathlib import Path

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath, "r") as f:
        return f.read()
    
def get_first_marker(comm_str):
    chars = [*comm_str]
    for i in range(0,len(chars)-14):
        subset = chars[i:i+14]
        if len(subset) == len(set(subset)):
            print(i+14)
            print(subset)
            return i+14
    
    
if __name__ == "__main__":
    comm_str = get_input_data()
    get_first_marker(comm_str)