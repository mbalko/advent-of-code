with open("input.txt", "r") as f:
    data = [x.split(",") for x in f.read().split()]

decisions = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
points = ({}, {})

for i in range(2):
    x, y, steps = 0, 0, 0
    for ins in data[i]:
        for _ in range(int(ins[1:])):
            x += decisions[ins[0]][0]
            y += decisions[ins[0]][1]
            steps += 1
            if (x, y) not in points[i]:
                points[i][(x, y)] = steps

same_points = points[0].keys() & points[1].keys()
print(min([points[0][x] + points[1][x] for x in same_points]))
