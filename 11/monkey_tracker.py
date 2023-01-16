from pathlib import Path
from dataclasses import dataclass
import copy
from functools import reduce

def get_input_data(filename="input.txt"):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        reader = f.read().split("\n\n")
        monkey_raw = [r.splitlines() for r in reader]
        all_monkeys = []
        get_key_val = lambda stringer: [i.lstrip() for i in stringer.split(":")]
        for m in monkey_raw:
            m_num_key = get_key_val(m[0])[0]
            num = int(m_num_key.split(" ")[-1])
            
            starting_val = get_key_val(m[1])[-1]
            starting_items = [int(i) for i in starting_val.split(", ")]
            
            operation = get_key_val(m[2])[-1]
            operation = operation.split(" = ")[-1]
            
            test_val = get_key_val(m[3])[-1]
            test_num = int(test_val.split(" ")[-1])
            
            if_true_val = get_key_val(m[4])[-1]
            if_true_pass = int(if_true_val.split(" ")[-1])
            
            if_false_val = get_key_val(m[5])[-1]
            if_false_pass = int(if_false_val.split(" ")[-1])
            
            m = Monkey(
                num,
                starting_items,
                operation,
                test_num,
                if_true_pass,
                if_false_pass,
                [i for i in starting_items],
                []
            )
            all_monkeys.append(m)
            print(f"Monkey:\n{m.__dict__}")
        return all_monkeys

@dataclass
class Monkey():
    num: int
    starting_items: list
    operation: str
    test_num: int
    if_true_pass: int
    if_false_pass: int
    current_items: list
    current_factors: list
    item_inspect_count: int = 0

def take_monkey_turn(monkey, all_monkeys):
    #print(f"Monkey {monkey.num}")
    for item in monkey.current_items:
        #print(f" Inspecting: {item}")
        monkey.item_inspect_count += 1
        # Perform operation
        old = item
        new = eval(monkey.operation)//3
        #print(f"    New Val: {new}")
        test_passed = new % monkey.test_num == 0
        #print(f"    Test passed?: {test_passed}")
        pass_to = monkey.if_true_pass if test_passed else monkey.if_false_pass
        monkey.current_items = monkey.current_items[1:]
        all_monkeys[pass_to].current_items.append(new)
        #print(f"    Passing to monkey: {pass_to}")
        
def print_status(all_monkeys):
    for m in all_monkeys:
        print(f"Monkey {m.num}: {m.current_items}")
    
def run_turns(original_monkeys, turn_count):
    all_monkeys = copy.deepcopy(original_monkeys)
    current_turn = 0
    while current_turn < turn_count:
        current_turn += 1
        #print(f"Starting Round: {turn}")
        for monkey in all_monkeys:
            take_monkey_turn(monkey, all_monkeys)
        #print_status(all_monkeys)
    return all_monkeys

def print_monkey_biz(end_monkeys):
    vals = [m.item_inspect_count for m in end_monkeys]
    top_two = sorted(vals, reverse=True)[0:2]
    mbiz = reduce(lambda x, y: x*y, top_two)
    print(mbiz)
    return

def print_item_count(all_monkeys):
    for m in all_monkeys:
        print(f"Monkey {m.num} has inspected {m.item_inspect_count} items")

def run_turns_no_div(original_monkeys, turn_count):
    all_monkeys = copy.deepcopy(original_monkeys)
    current_turn = 0
    while current_turn < turn_count:
        for monkey in all_monkeys:
            take_monkey_turn_no_div(monkey, all_monkeys)
        if current_turn % 1000 == 0:
            print(f"Starting Round: {current_turn}")
            print_item_count(all_monkeys)
            current_turn += 1
    return all_monkeys

def take_monkey_turn_no_div(monkey, all_monkeys):
    primes = [m.test_num for m in all_monkeys]
    
    
if __name__ == "__main__":
    original_monkeys = get_input_data()
    turn_count = 20
    post_20_monkeys = run_turns(original_monkeys, turn_count)
    print_monkey_biz(post_20_monkeys)
    print("Done")
        