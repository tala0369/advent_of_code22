from pathlib import Path
import csv
import itertools

def get_score_matrix():
    opts = ["Rock", "Paper", "Scissors"]
    cross = itertools.product(opts, opts)

    WIN_LOSE_MATRIX = [
        [0, 1, -1],
        [-1, 0, 1],
        [1, -1, 0]
    ]

    matrix = []
    for (elf_result, my_result) in cross:
        elf_index = opts.index(elf_result)
        my_index = opts.index(my_result)
        result = WIN_LOSE_MATRIX[my_index][elf_index]
        elf_score = 3 + result*3
        my_score = 3 + result*-3
        result = {
            "elf_pick": elf_result,
            "my_pick": my_result,
            "elf_pick_score": 1+elf_index,
            "my_pick_score": 1+my_index,
            "elf_score": elf_score,
            "my_score": my_score,
            "elf_total_score": elf_score + 1 + elf_index,
            "my_total_score": my_score + 1 + my_index
        }
        matrix.append(result)
    return matrix

def get_score_dict_from_pick(elf_pick, my_pick, score_matrix):
    score_card = next(
        card for card in score_matrix
        if card["elf_pick"] == elf_pick and card["my_pick"] == my_pick
    )
    return score_card

def get_input_data(filename):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=" ", fieldnames=["elf_raw", "my_raw"])
        return [row for row in reader]
    
def expand_p1(strategy):
    strategy_key = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }
    score_matrix = get_score_matrix()
    
    all_results = []
    
    for round in strategy:
        elf_pick = strategy_key[round["elf_raw"]]
        my_pick = strategy_key[round["my_raw"]]
        score_card = next(
            card for card in score_matrix
            if card["elf_pick"] == elf_pick and card["my_pick"] == my_pick
        )
        all_results.append(score_card)
    return all_results

def get_total_score(expanded_strategy, score_col="my_total_score"):
    total = sum([i[score_col] for i in expanded_strategy])
    print(f"My total for col {score_col}: {total}")
    
def switchup_strategy(expanded_strategy):
    strategy_key_elf = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors"
    }
    strategy_key_me = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    score_matrix = get_score_matrix()
    
    all_results = []
    
    for round in strategy:
        elf_pick = strategy_key_elf[round["elf_raw"]]
        my_score = strategy_key_me[round["my_raw"]]
        score_card = next(
            card for card in score_matrix
            if card["elf_pick"] == elf_pick and card["my_score"] == my_score
        )
        all_results.append(score_card)
    return all_results
        

if __name__ == "__main__":
    strategy = get_input_data("input.csv")
    expanded_strategy = expand_p1(strategy)
    get_total_score(expanded_strategy)
    switched = switchup_strategy(strategy)
    get_total_score(switched)
    print("Done")