with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split(",")]

def run_computer(data):
    i = 0
    while str(data[i])[:-3:-1] != "99":
        jump = 0
        full_code = str(data[i]).zfill(5)
        opcode = int(full_code[3:])
        # Get arguments
        if opcode in [1, 2, 4, 5, 6, 7, 8]:
            arg1 = data[i + 1] if int(full_code[2]) else data[data[i + 1]]
        if opcode in [1, 2, 5, 6, 7, 8]:
            arg2 = data[i + 2] if int(full_code[1]) else data[data[i + 2]]

        if opcode in [1, 2, 7, 8]:
            arg3 = data[i + 3]
            jump = 4
            if opcode == 1:
                data[arg3] = arg1 + arg2
            elif opcode == 2:
                data[arg3] = arg1 * arg2
            elif opcode == 7:
                data[arg3] = 1 if arg1 < arg2 else 0
            elif opcode == 8:
                data[arg3] = 1 if arg1 == arg2 else 0
        elif opcode in [3, 4]:
            jump = 2
            if opcode == 3:
                data[data[i + 1]] = int(input()) # Input: 5
            else:
                print(arg1)
        elif opcode in [5, 6]:
            if opcode == 5 and arg1:
                i = arg2
            elif opcode == 6 and not arg1:
                i = arg2
            else:
                jump = 3
        i += jump

run_computer(data)
