import copy

def run_computer(data):
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        elif data[i] == 99:
            return data[0]

with open("input.txt", "r") as f:
    raw_data = [int(x) for x in f.read().split(",")]

def run():
    for noun in range(100):
        for verb in range(100):
            data = copy.deepcopy(raw_data)
            data[1] = noun
            data[2] = verb
            if run_computer(data) == 19690720:
                print(noun, verb)
                return

run()
