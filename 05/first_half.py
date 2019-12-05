with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]

def run_computer(data):
    i = 0
    while str(data[i])[:-3:-1] != "99":
        jump = 0
        full_code = str(data[i]).zfill(5)
        opcode = int(full_code[3:])
        if opcode in [1, 2]:
            jump = 4
            arg1 = data[i + 1] if int(full_code[2]) else data[data[i + 1]]
            arg2 = data[i + 2] if int(full_code[1]) else data[data[i + 2]]
            arg3 = data[i + 3]
            if opcode == 1:
                data[arg3] = arg1 + arg2
            else:
                data[arg3] = arg1 * arg2
        elif opcode in [3, 4]:
            jump = 2
            if opcode == 3:
                data[data[i + 1]] = int(input()) # Input: 1
            else:
                arg1 = data[i + 1] if int(full_code[2]) else data[data[i + 1]]
                print(arg1)
        i += jump

run_computer(data)
